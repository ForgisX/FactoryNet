
from typing import Any, Dict, Iterable, List, Optional, Sequence

from dataclasses import dataclass, field

@dataclass(frozen=True)
class Machine:
    """Physical machine in the factory."""

    machine_id: str
    factory_id: str
    machine_type: str
    vendor: str
    year: Optional[int] = None
    location: Optional[str] = None
    extra: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ManualSection:
    """Section of a machine manual."""

    manual_id: str
    machine_id: str
    section_index: int
    title: str
    text: str
    language: str = "en"


@dataclass(frozen=True)
class ProcessNode:
    """Single step or station in the production process."""

    node_id: str
    factory_id: str
    name: str
    step_type: str
    machine_id: Optional[str] = None


@dataclass(frozen=True)
class ProcessEdge:
    """Directed edge between process nodes describing dependencies."""

    edge_id: str
    src_node_id: str
    dst_node_id: str
    relation_type: str


@dataclass(frozen=True)
class Run:
    """Single execution of a machine (one multivariate time series)."""

    run_id: str
    machine_id: str

    timestamps: Sequence[float]
    values: Sequence[Sequence[float]]
    channel_names: Sequence[str]
    sampling_rate_hz: float

    label: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    
    
    
@dataclass(frozen=True)
class RunRecord:
    """Single training record: one run with all attached context."""

    # identifiers
    run_id: str
    machine_id: str

    # machine metadata (flattened for easier model use)
    factory_id: str
    machine_type: str
    machine_vendor: str
    machine_year: Optional[int]
    machine_location: Optional[str]

    # time series
    timestamps: Sequence[float]
    values: Sequence[Sequence[float]]
    channel_names: Sequence[str]
    sampling_rate_hz: float

    # labels / annotations
    label: Optional[str]

    # attached documentation and process graph
    manual_sections: Sequence[ManualSection] = field(default_factory=list)
    process_nodes: Sequence[ProcessNode] = field(default_factory=list)
    process_edges: Sequence[ProcessEdge] = field(default_factory=list)

    @classmethod
    def from_domain(
        cls,
        run: Run,
        machine: Machine,
        manual_sections: Sequence[ManualSection],
        process_nodes: Sequence[ProcessNode],
        process_edges: Sequence[ProcessEdge],
    ) -> "RunRecord":
        return cls(
            run_id=run.run_id,
            machine_id=run.machine_id,
            factory_id=machine.factory_id,
            machine_type=machine.machine_type,
            machine_vendor=machine.vendor,
            machine_year=machine.year,
            machine_location=machine.location,
            timestamps=list(run.timestamps),
            values=[list(row) for row in run.values],
            channel_names=list(run.channel_names),
            sampling_rate_hz=float(run.sampling_rate_hz),
            label=run.label,
            manual_sections=list(manual_sections),
            process_nodes=list(process_nodes),
            process_edges=list(process_edges),
        )

    def to_hf_row(self) -> Dict[str, Any]:
        """Convert to a row suitable for Hugging Face Datasets."""

        return {
            "run_id": self.run_id,
            "machine_id": self.machine_id,
            "factory_id": self.factory_id,
            "machine_type": self.machine_type,
            "machine_vendor": self.machine_vendor,
            "machine_year": self.machine_year,
            "machine_location": self.machine_location,
            "timestamps": list(self.timestamps),
            "values": [list(row) for row in self.values],
            "channel_names": list(self.channel_names),
            "sampling_rate_hz": float(self.sampling_rate_hz),
            "label": self.label,
            "manual_sections": [
                {
                    "manual_id": section.manual_id,
                    "machine_id": section.machine_id,
                    "section_index": section.section_index,
                    "title": section.title,
                    "text": section.text,
                    "language": section.language,
                }
                for section in self.manual_sections
            ],
            "process_nodes": [
                {
                    "node_id": node.node_id,
                    "factory_id": node.factory_id,
                    "name": node.name,
                    "step_type": node.step_type,
                    "machine_id": node.machine_id,
                }
                for node in self.process_nodes
            ],
            "process_edges": [
                {
                    "edge_id": edge.edge_id,
                    "src_node_id": edge.src_node_id,
                    "dst_node_id": edge.dst_node_id,
                    "relation_type": edge.relation_type,
                }
                for edge in self.process_edges
            ],
        }


@dataclass
class FactoryDataset:
    """In-memory representation of all data in a factory.

    This is your main application-level interface. It keeps the domain model
    fully separate from any storage / Hugging Face concerns.
    """

    machines: Dict[str, Machine]
    runs: Dict[str, Run]
    manual_sections: List[ManualSection]
    process_nodes: List[ProcessNode]
    process_edges: List[ProcessEdge]

    def iter_run_records(self) -> Iterable["RunRecord"]:
        """Yield RunRecord objects that are ready for model training."""

        manuals_by_machine: Dict[str, List[ManualSection]] = {}
        for section in self.manual_sections:
            manuals_by_machine.setdefault(section.machine_id, []).append(section)

        nodes_by_factory: Dict[str, List[ProcessNode]] = {}
        nodes_by_machine: Dict[str, List[ProcessNode]] = {}
        for node in self.process_nodes:
            nodes_by_factory.setdefault(node.factory_id, []).append(node)
            if node.machine_id:
                nodes_by_machine.setdefault(node.machine_id, []).append(node)

        for run in self.runs.values():
            machine = self.machines[run.machine_id]
            manual_sections = manuals_by_machine.get(run.machine_id, [])

            factory_nodes = nodes_by_factory.get(machine.factory_id, [])
            machine_nodes = nodes_by_machine.get(machine.machine_id, [])
            nodes_for_run = {n.node_id: n for n in (*factory_nodes, *machine_nodes)}

            node_ids = set(nodes_for_run.keys())
            edges_for_run = [
                edge
                for edge in self.process_edges
                if edge.src_node_id in node_ids or edge.dst_node_id in node_ids
            ]

            yield RunRecord.from_domain(
                run=run,
                machine=machine,
                manual_sections=manual_sections,
                process_nodes=list(nodes_for_run.values()),
                process_edges=edges_for_run,
            )