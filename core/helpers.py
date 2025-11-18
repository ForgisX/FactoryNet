from typing import Sequence

from datasets import Array2D, Dataset, Features, Sequence as HFSequence, Value

from core.dataclass import FactoryDataset, RunRecord


def run_features() -> Features:
    """HF Features definition for RunRecord rows."""

    return Features(
        {
            "run_id": Value("string"),
            "machine_id": Value("string"),
            "factory_id": Value("string"),
            "machine_type": Value("string"),
            "machine_vendor": Value("string"),
            "machine_year": Value("int32"),
            "machine_location": Value("string"),
            "timestamps": HFSequence(Value("float64")),
            "values": Array2D(shape=(None, None), dtype="float32"),
            "channel_names": HFSequence(Value("string")),
            "sampling_rate_hz": Value("float32"),
            "label": Value("string"),
            "manual_sections": HFSequence(
                feature={
                    "manual_id": Value("string"),
                    "machine_id": Value("string"),
                    "section_index": Value("int32"),
                    "title": Value("string"),
                    "text": Value("string"),
                    "language": Value("string"),
                }
            ),
            "process_nodes": HFSequence(
                feature={
                    "node_id": Value("string"),
                    "factory_id": Value("string"),
                    "name": Value("string"),
                    "step_type": Value("string"),
                    "machine_id": Value("string"),
                }
            ),
            "process_edges": HFSequence(
                feature={
                    "edge_id": Value("string"),
                    "src_node_id": Value("string"),
                    "dst_node_id": Value("string"),
                    "relation_type": Value("string"),
                }
            ),
        }
    )


def build_run_dataset(records: Sequence[RunRecord]) -> Dataset:
    """Create a Hugging Face Dataset from RunRecord objects."""

    rows = [record.to_hf_row() for record in records]
    return Dataset.from_list(list(rows), features=run_features())


def build_run_dataset_from_factory(factory_dataset: FactoryDataset) -> Dataset:
    """Create a Hugging Face Dataset directly from a FactoryDataset."""

    return build_run_dataset(list(factory_dataset.iter_run_records()))
