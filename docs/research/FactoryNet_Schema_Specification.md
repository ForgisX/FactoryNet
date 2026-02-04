# FactoryNet Dataset Schema Specification

*Version: 0.1 Draft*
*Last Updated: 2026-02-04*

---

## 1. Design Philosophy

FactoryNet is designed around **machine understanding**, not just fault classification. The schema supports:

1. **Episode-centric structure** (like Open X-Embodiment) for temporal reasoning
2. **Hierarchical taxonomy** (like WordNet/ImageNet) for cross-machine transfer
3. **Q&A evaluation** (like CLEVRER) for testing genuine understanding
4. **Semantic priors** (manuals, URDF) for grounding

---

## 2. Taxonomy Synset IDs

### 2.1 ID Format

```
{Dimension}.{L1}.{L2}.{L3}.{L4}.{L5}

Dimensions:
- M = Machine
- S = State
- Y = Symptom (Y to avoid confusion with State)
- C = Cause
- A = Action
```

### 2.2 Machine Dimension (M)

```yaml
M:
  rob:  # robot
    ind:  # industrial
      art:  # articulated
        6ax:  # 6-axis
          abb:
            irb2600: "ABB IRB 2600"
            irb6700: "ABB IRB 6700"
          kuka:
            kr10: "KUKA KR10"
            kr6: "KUKA KR6"
          fanuc:
            m20: "Fanuc M-20"
        7ax:  # 7-axis
          kuka:
            lbr: "KUKA LBR iiwa"
      sca:  # SCARA
        epson:
          g6: "Epson G6"
      del:  # delta
        abb:
          flexpicker: "ABB FlexPicker"
    col:  # collaborative
      abb:
        yumi: "ABB YuMi"
      ur:  # Universal Robots
        ur3: "UR3"
        ur5: "UR5"
        ur10: "UR10"
      franka:
        panda: "Franka Emika Panda"
  con:  # conveyor
    belt:
      std: "Standard belt conveyor"
    roller:
      grav: "Gravity roller"
      pow: "Powered roller"
    chain:
      std: "Chain conveyor"
  lab:  # labeling machine
    herma:
      h400: "Herma H400"
    spr:
      max: "SPR Max"
  sen:  # sensor
    prox:  # proximity
      ind: "Inductive"
      cap: "Capacitive"
      opt: "Optical"
    ft:  # force-torque
      ati: "ATI F/T sensor"
    vis:  # vision
      cam2d: "2D camera"
      cam3d: "3D camera"
```

### 2.3 State Dimension (S)

```yaml
S:
  nor:  # normal
    idl: "Idle"
    exe: "Executing program"
    man: "Manual mode"
    hom: "Homing"
  deg:  # degraded
    red:  # reduced performance
      spd: "Reduced speed"
      tor: "Reduced torque"
      pre: "Reduced precision"
    int: "Intermittent operation"
  flt:  # fault
    mec:  # mechanical
      wea:  # wear
        bea:  # bearing
          inn: "Inner race wear"
          out: "Outer race wear"
          bal: "Ball wear"
          cag: "Cage wear"
        gea: "Gear wear"
        sea: "Seal wear"
      str:  # structural
        crk: "Crack"
        def: "Deformation"
        cor: "Corrosion"
      ali:  # alignment
        mis:
          ang: "Angular misalignment"
          par: "Parallel misalignment"
        imb:
          sta: "Static imbalance"
          dyn: "Dynamic imbalance"
      lub:  # lubrication
        ins: "Insufficient lubrication"
        con: "Contaminated lubricant"
        wrg: "Wrong lubricant"
    ele:  # electrical
      pow:  # power
        ovv: "Overvoltage"
        unv: "Undervoltage"
        los: "Power loss"
      cur:  # current
        ovc: "Overcurrent"
        phi: "Phase imbalance"
        gnd: "Ground fault"
        sht: "Short circuit"
      sig:  # signal
        dri: "Signal drift"  # [BIAS]
        noi: "Signal noise"  # [VARIANCE]
        los: "Signal loss"   # [DROPOUT]
    the:  # thermal
      ovh: "Overheating"
      cyc: "Thermal cycling"
    pne:  # pneumatic
      pre:
        low: "Low pressure"
        flu: "Pressure fluctuation"
      lea: "Leakage"
    sof:  # software
      com:  # communication
        tim: "Timeout"
        pkt: "Packet loss"
        pro: "Protocol error"
      par: "Parameter fault"
      plc:
        prg: "Program error"
        wdg: "Watchdog timeout"
    pro:  # process
      cyc: "Cycle time deviation"
      pos: "Position error"
      qua: "Quality defect"
  eme:  # emergency
    saf: "Safety stop"
    est: "Emergency stop"
```

### 2.4 State Attributes (Orthogonal)

```yaml
state_attributes:
  temporal:
    - sudden      # Instant onset
    - gradual     # Progressive degradation
    - intermittent # Comes and goes
    - cyclic      # Periodic occurrence
  spatial:
    - point       # Single location
    - distributed # Multiple locations
    - propagating # Spreading
  dynamic:
    - static      # Constant characteristics
    - dynamic     # Changing characteristics
    - progressive # Worsening over time
  severity:
    - minor       # No immediate impact
    - moderate    # Reduced performance
    - critical    # Requires immediate action
```

### 2.5 Symptom Dimension (Y)

```yaml
Y:
  vib:  # vibration
    low:  # <100 Hz
      imb: "Imbalance (1x RPM)"
      mis: "Misalignment (2x RPM)"
    mid:  # 100-1000 Hz
      gea: "Gear mesh frequency"
    hig:  # >1000 Hz
      bea:  # bearing
        bpfo: "Ball pass freq outer"
        bpfi: "Ball pass freq inner"
        bsf: "Ball spin frequency"
        ftf: "Fundamental train freq"
      ele: "Electrical noise"
  aco:  # acoustic
    gri: "Grinding"
    cli: "Clicking"
    hum: "Humming"
    squ: "Squealing"
  the:  # thermal
    loc: "Localized hotspot"
    gen: "General temperature rise"
  vis:  # visual
    smo: "Smoke"
    spa: "Sparks"
    dis: "Discoloration"
    oil: "Oil leak"
    phy: "Physical damage"
  per:  # performance
    spd: "Reduced speed"
    tor: "Reduced torque"
    pre:
      pos: "Positioning error"
      rep: "Repeatability error"
    cyc: "Increased cycle time"
  tel:  # telemetry
    cur:
      spk: "Current spike"
      rip: "Current ripple"
      imb: "Current imbalance"
    vol: "Voltage anomaly"
    tmp: "Temperature anomaly"
    pos:
      fol: "Following error"
      dri: "Position drift"
  alm:  # alarm
    drv: "Drive fault code"
    plc: "PLC alarm"
    saf: "Safety fault"
  prc:  # process
    rej: "Reject rate increase"
    thr: "Throughput decrease"
    qua: "Quality deviation"
```

### 2.6 Cause Dimension (C)

```yaml
C:
  ope:  # operational
    ovl:  # overload
      con: "Continuous overload"
      int: "Intermittent overload"
    par: "Wrong parameters"
    mis: "Misuse"
  mai:  # maintenance
    ina:  # inadequate
      mis: "Missed maintenance"
      lub: "Inadequate lubrication"
      cle: "Inadequate cleaning"
    imp:  # improper
      prt: "Wrong parts"
      lub: "Wrong lubricant"
      asm: "Improper assembly"
    non: "No maintenance"
  env:  # environmental
    cnt:  # contamination
      dst: "Dust"
      moi: "Moisture"
      chm: "Chemical"
    tmp:
      hig: "High temperature"
      low: "Low temperature"
    vib: "External vibration"
  des:  # design
    und: "Undersized component"
    mat: "Material defect"
    mfg: "Manufacturing defect"
  ins:  # installation
    ali: "Improper alignment"
    mnt: "Improper mounting"
    wir: "Improper wiring"
  age:  # age-related
    wea: "Normal wear"
    fat: "Material fatigue"
```

### 2.7 Action Dimension (A)

```yaml
A:
  dia:  # diagnose
    ins:  # inspect
      vis: "Visual inspection"
      the: "Thermal inspection"
      vib: "Vibration inspection"
    mea:  # measure
      cur: "Measure current"
      vol: "Measure voltage"
      res: "Measure resistance"
      tmp: "Measure temperature"
      vib: "Measure vibration"
    tst:  # test
      con: "Continuity test"
      iso: "Insulation test"
      fun: "Functional test"
  mai:  # maintain
    cle:  # clean
      fil: "Clean filter"
      sen: "Clean sensor"
      sur: "Clean surface"
    lub:  # lubricate
      gre: "Apply grease"
      oil: "Apply oil"
    adj:  # adjust
      ali: "Adjust alignment"
      ten: "Adjust tension"
      pre: "Adjust pressure"
      par: "Adjust parameter"
    tig: "Tighten"
  rep:  # repair
    rep:  # replace
      bea:  # bearing
        "6205": "Replace bearing 6205"
        "6206": "Replace bearing 6206"
        "7206": "Replace bearing 7206"
      sea: "Replace seal"
      blt: "Replace belt"
      mot: "Replace motor"
      enc: "Replace encoder"
      cab: "Replace cable"
    rew: "Rewire"
  res:  # reset
    flt:  # fault
      drv: "Reset drive fault"
      plc: "Reset PLC alarm"
    rst:  # restart
      plc: "Restart PLC"
      drv: "Restart drive"
    cal:  # calibrate
      enc: "Calibrate encoder"
      fts: "Calibrate force sensor"
  esc:  # escalate
    mfr: "Contact manufacturer"
    eng: "Contact engineer"
    ord: "Order replacement"
```

---

## 3. Episode Schema

### 3.1 Top-Level Structure

```python
@dataclass
class FactoryNetEpisode:
    # === Identification ===
    episode_id: str                    # "FN-2026-00001"
    source: str                        # "real" | "adapted" | "synthetic"
    version: str                       # "1.0.0"

    # === Machine ===
    machine_synset: str                # "M.rob.col.ur.ur3"
    machine_instance: str              # "UR3-FACTORY-001"
    machine_serial: Optional[str]      # Actual serial number

    # === Temporal ===
    timestamp_start: datetime
    timestamp_end: datetime
    duration_seconds: float
    sampling_rate_hz: float

    # === Multimodal Data ===
    steps: List[TimeStep]              # T timesteps

    # === Labels ===
    state_annotation: StateAnnotation
    cause_synset: Optional[str]
    action_sequence: List[str]

    # === Semantic Priors ===
    semantic_priors: SemanticPriors

    # === Q&A Annotations ===
    qa_pairs: List[QAPair]

    # === Metadata ===
    metadata: EpisodeMetadata
```

### 3.2 TimeStep Schema

```python
@dataclass
class TimeStep:
    # === Temporal ===
    step_index: int
    timestamp_offset: float            # Seconds from episode start

    # === Proprioception ===
    proprioception: Proprioception

    # === Exteroception ===
    exteroception: Optional[Exteroception]

    # === Condition Monitoring ===
    condition_monitoring: ConditionMonitoring

    # === Discrete State ===
    discrete_state: DiscreteState


@dataclass
class Proprioception:
    joint_positions: np.ndarray        # [N_joints] radians
    joint_velocities: np.ndarray       # [N_joints] rad/s
    joint_torques: np.ndarray          # [N_joints] Nm
    motor_currents: np.ndarray         # [N_joints] Amps
    end_effector_pose: np.ndarray      # [7] xyz + quaternion
    gripper_state: Optional[float]     # 0=open, 1=closed


@dataclass
class Exteroception:
    rgb_image: Optional[np.ndarray]    # [H, W, 3] uint8
    depth_image: Optional[np.ndarray]  # [H, W] float32 meters
    force_torque: Optional[np.ndarray] # [6] Fx,Fy,Fz,Tx,Ty,Tz


@dataclass
class ConditionMonitoring:
    vibration: Optional[np.ndarray]    # [N_channels, N_samples] or features
    temperature: Optional[np.ndarray]  # [N_sensors] Celsius
    acoustic: Optional[np.ndarray]     # [N_mics, N_samples] or features

    # Pre-computed features (optional)
    vibration_features: Optional[Dict[str, float]]  # RMS, kurtosis, etc.
    spectral_features: Optional[np.ndarray]         # FFT magnitudes


@dataclass
class DiscreteState:
    plc_state: Dict[str, Any]          # PLC variable values
    error_codes: List[str]             # Active error codes
    safety_status: str                 # "normal" | "warning" | "stop"
    program_state: str                 # Current program/task
```

### 3.3 State Annotation Schema

```python
@dataclass
class StateAnnotation:
    # Primary state
    state_synset: str                  # "S.flt.mec.wea.bea.inn"

    # Attributes
    temporal: str                      # "sudden" | "gradual" | "intermittent"
    spatial: str                       # "point" | "distributed" | "propagating"
    dynamic: str                       # "static" | "dynamic" | "progressive"
    severity: str                      # "minor" | "moderate" | "critical"

    # Temporal bounds
    onset_step: Optional[int]          # When fault started (if applicable)
    offset_step: Optional[int]         # When fault ended (if applicable)

    # Severity trajectory (for progressive faults)
    severity_trajectory: Optional[np.ndarray]  # [T] 0.0-1.0

    # Confidence
    annotation_confidence: float       # 0.0-1.0
    annotator_id: str                  # For quality tracking
```

### 3.4 Semantic Priors Schema

```python
@dataclass
class SemanticPriors:
    # URDF/CAD
    urdf_path: Optional[str]           # Path to URDF file
    cad_path: Optional[str]            # Path to CAD model

    # Manual references
    manual_refs: List[ManualReference]

    # Error code database
    error_code_docs: Dict[str, str]    # code -> description

    # Pre-computed embeddings
    manual_embeddings: Optional[np.ndarray]  # [N_sections, D]


@dataclass
class ManualReference:
    document: str                      # "ABB_IRB_2600_Manual_v3.pdf"
    section: str                       # "3.5.2 Bearing Replacement"
    page: int
    relevance_score: float             # 0.0-1.0
    content_snippet: str               # Relevant text excerpt
    embedding: Optional[np.ndarray]    # [D] pre-computed
```

### 3.5 Q&A Schema

```python
@dataclass
class QAPair:
    qa_id: str                         # "FN-2026-00001-Q001"

    # Question
    question_text: str
    question_type: str                 # "state" | "prediction" | "causal" |
                                       # "counterfactual" | "procedural" | "diagnostic"
    question_difficulty: str           # "easy" | "medium" | "hard"

    # Answer
    answer_text: str
    answer_type: str                   # "text" | "numeric" | "boolean" |
                                       # "multiple_choice" | "sequence"
    answer_options: Optional[List[str]]  # For multiple choice

    # Grounding
    evidence_steps: List[int]          # Relevant timesteps
    evidence_sensors: List[str]        # Relevant sensor types
    manual_refs: List[str]             # Relevant manual sections

    # Reasoning (for training/analysis)
    reasoning_chain: Optional[str]     # Step-by-step reasoning

    # Metadata
    template_id: Optional[str]         # If generated from template
    annotator_id: str
    confidence: float
```

---

## 4. File Format Specification

### 4.1 Directory Structure

```
factorynet/
├── README.md
├── LICENSE
├── taxonomy/
│   ├── machine_taxonomy.yaml
│   ├── state_taxonomy.yaml
│   ├── symptom_taxonomy.yaml
│   ├── cause_taxonomy.yaml
│   ├── action_taxonomy.yaml
│   └── relations.yaml
├── episodes/
│   ├── real/
│   │   ├── abb_irb_2600/
│   │   │   ├── FN-2026-00001/
│   │   │   │   ├── metadata.json
│   │   │   │   ├── timeseries.parquet
│   │   │   │   ├── images/           # Optional
│   │   │   │   │   ├── 000000.jpg
│   │   │   │   │   └── ...
│   │   │   │   ├── audio/            # Optional
│   │   │   │   │   └── audio.wav
│   │   │   │   ├── qa_pairs.json
│   │   │   │   └── semantic_priors.json
│   │   │   └── ...
│   │   ├── ur3/
│   │   └── ...
│   ├── adapted/
│   │   ├── cwru/
│   │   ├── paderborn/
│   │   └── ...
│   └── synthetic/
│       ├── isaac_sim/
│       └── ...
├── splits/
│   ├── train.txt
│   ├── val.txt
│   ├── test.txt
│   ├── test_cross_machine.txt
│   ├── test_cross_manufacturer.txt
│   └── test_cross_category.txt
├── semantic_priors/
│   ├── urdfs/
│   │   ├── abb_irb_2600.urdf
│   │   └── ...
│   ├── manuals/
│   │   ├── ABB_IRB_2600_Manual.pdf
│   │   └── ...
│   └── embeddings/
│       ├── manual_embeddings.npy
│       └── ...
└── evaluation/
    ├── baseline_predictions/
    └── leaderboard_submissions/
```

### 4.2 Metadata JSON Schema

```json
{
  "$schema": "https://factorynet.forgis.com/schema/episode-metadata-v1.json",
  "episode_id": "FN-2026-00001",
  "source": "real",
  "version": "1.0.0",

  "machine": {
    "synset": "M.rob.col.ur.ur3",
    "instance": "UR3-FACTORY-001",
    "serial": "UR3-2023-XXXXX"
  },

  "temporal": {
    "timestamp_start": "2026-02-04T14:30:00Z",
    "timestamp_end": "2026-02-04T14:32:00Z",
    "duration_seconds": 120.5,
    "sampling_rate_hz": 100,
    "num_steps": 12050
  },

  "state_annotation": {
    "state_synset": "S.flt.mec.wea.bea.inn",
    "attributes": {
      "temporal": "gradual",
      "spatial": "point",
      "dynamic": "progressive",
      "severity": "moderate"
    },
    "onset_step": 4500,
    "annotation_confidence": 0.95,
    "annotator_id": "expert_001"
  },

  "cause_synset": "C.mai.ina.lub",
  "action_sequence": ["A.dia.ins.vib", "A.rep.rep.bea.6205"],

  "data_files": {
    "timeseries": "timeseries.parquet",
    "images": "images/",
    "audio": "audio/audio.wav",
    "qa_pairs": "qa_pairs.json",
    "semantic_priors": "semantic_priors.json"
  },

  "quality": {
    "sensor_completeness": 0.98,
    "annotation_status": "verified",
    "qa_pairs_count": 25
  }
}
```

### 4.3 Timeseries Parquet Schema

```
Columns:
- step_index: int64
- timestamp_offset: float64

# Proprioception (variable by robot)
- joint_0_position: float64
- joint_0_velocity: float64
- joint_0_torque: float64
- joint_0_current: float64
... (for each joint)
- ee_x, ee_y, ee_z: float64
- ee_qw, ee_qx, ee_qy, ee_qz: float64
- gripper_state: float64

# Condition monitoring
- vib_ch0_rms: float64
- vib_ch0_kurtosis: float64
- vib_ch0_peak_freq: float64
... (for each vibration channel)
- temp_0: float64
... (for each temperature sensor)

# Discrete state
- error_codes: string (JSON array)
- safety_status: string
- program_state: string

# Pre-computed features (optional)
- severity_estimate: float64
```

### 4.4 Q&A Pairs JSON Schema

```json
{
  "episode_id": "FN-2026-00001",
  "qa_pairs": [
    {
      "qa_id": "FN-2026-00001-Q001",
      "question_text": "What is the current state of joint 3?",
      "question_type": "state",
      "question_difficulty": "easy",
      "answer_text": "Joint 3 is at 45.2 degrees, stationary",
      "answer_type": "text",
      "evidence_steps": [100, 101, 102],
      "evidence_sensors": ["joint_2_position", "joint_2_velocity"],
      "manual_refs": [],
      "reasoning_chain": "Read joint_2_position (45.2°) and joint_2_velocity (0 rad/s) at current timestep.",
      "template_id": "state_joint_position",
      "annotator_id": "auto_001",
      "confidence": 1.0
    },
    {
      "qa_id": "FN-2026-00001-Q002",
      "question_text": "What caused the vibration spike at t=45s?",
      "question_type": "causal",
      "question_difficulty": "hard",
      "answer_text": "Inner race bearing defect on joint 3. The characteristic frequency of 147Hz matches the BPFI for this bearing at the current speed of 1500 RPM.",
      "answer_type": "text",
      "evidence_steps": [4500, 4501, 4502],
      "evidence_sensors": ["vib_ch0", "joint_2_velocity"],
      "manual_refs": ["ABB_IRB_2600_Manual.pdf#section_3.5.2"],
      "reasoning_chain": "1. Observe vibration spike at t=45s. 2. Extract frequency spectrum. 3. Identify peak at 147Hz. 4. Calculate expected BPFI: (N/2) * RPM/60 * (1 + Bd*cos(θ)/Pd) = 147Hz. 5. Match to inner race defect.",
      "template_id": "causal_vibration_bearing",
      "annotator_id": "expert_001",
      "confidence": 0.85
    }
  ]
}
```

---

## 5. Feature Extraction Guidelines

### 5.1 Vibration Features

| Feature | Formula | Unit |
|---------|---------|------|
| RMS | √(Σx²/N) | m/s² or mm/s |
| Peak | max(|x|) | m/s² or mm/s |
| Crest Factor | Peak / RMS | dimensionless |
| Kurtosis | E[(x-μ)⁴]/σ⁴ | dimensionless |
| Skewness | E[(x-μ)³]/σ³ | dimensionless |
| BPFO | (N/2) × fr × (1 - Bd×cos(θ)/Pd) | Hz |
| BPFI | (N/2) × fr × (1 + Bd×cos(θ)/Pd) | Hz |
| BSF | (Pd/2Bd) × fr × (1 - (Bd×cos(θ)/Pd)²) | Hz |
| FTF | (fr/2) × (1 - Bd×cos(θ)/Pd) | Hz |

### 5.2 Current Features

| Feature | Description |
|---------|-------------|
| RMS Current | Per-phase RMS |
| Current Imbalance | Max deviation from mean |
| THD | Total harmonic distortion |
| Negative Sequence | Indicator of asymmetry |

### 5.3 Thermal Features

| Feature | Description |
|---------|-------------|
| Absolute Temperature | Direct reading |
| Temperature Rise | Delta from baseline |
| Rate of Change | dT/dt |
| Gradient | Spatial temperature difference |

---

## 6. Splits Definition

### 6.1 Standard Splits

```yaml
splits:
  train:
    ratio: 0.7
    strategy: stratified_random
    stratify_by: [machine_synset, state_synset_l2]

  val:
    ratio: 0.1
    strategy: stratified_random
    stratify_by: [machine_synset, state_synset_l2]

  test:
    ratio: 0.2
    strategy: stratified_random
    stratify_by: [machine_synset, state_synset_l2]
```

### 6.2 Transfer Splits

```yaml
transfer_splits:
  cross_machine:
    train_machines: ["M.rob.col.ur.ur3", "M.rob.ind.art.6ax.abb.irb2600", "M.rob.ind.art.6ax.kuka.kr10"]
    test_machines: ["M.rob.col.abb.yumi"]

  cross_manufacturer:
    train_machines: ["M.rob.col.abb.*", "M.rob.ind.art.6ax.kuka.*"]
    test_machines: ["M.rob.col.ur.*"]

  cross_category:
    train_machines: ["M.rob.*"]
    test_machines: ["M.lab.*", "M.con.*"]

  zero_shot_fault:
    train_faults: ["S.flt.mec.wea.bea.*", "S.flt.mec.ali.*", "S.flt.ele.*"]
    test_faults: ["S.flt.mec.wea.gea.*"]  # Held-out gear faults
```

---

## 7. Evaluation API

### 7.1 Submission Format

```json
{
  "submission_id": "sub_2026_001",
  "model_name": "FactoryBERT",
  "predictions": [
    {
      "qa_id": "FN-2026-00001-Q001",
      "predicted_answer": "Joint 3 is at 45.0 degrees",
      "confidence": 0.92
    },
    ...
  ]
}
```

### 7.2 Evaluation Metrics API

```python
from factorynet.evaluation import evaluate

results = evaluate(
    predictions_path="predictions.json",
    split="test",
    metrics=["accuracy", "hierarchical_accuracy", "f1", "bleu"]
)

print(results)
# {
#   "overall": {"fns": 0.72, "accuracy": 0.68},
#   "by_type": {
#     "state": {"accuracy": 0.85},
#     "prediction": {"accuracy": 0.71},
#     "causal": {"accuracy": 0.62},
#     ...
#   },
#   "by_difficulty": {...},
#   "transfer": {...}
# }
```

---

## 8. Implementation Checklist

### 8.1 Data Collection
- [ ] Define sensor configurations for each machine
- [ ] Implement data collection pipeline
- [ ] Create annotation tool for state labeling
- [ ] Build Q&A generation templates

### 8.2 Schema Implementation
- [ ] Create Pydantic/dataclass models
- [ ] Implement Parquet serialization
- [ ] Build validation scripts
- [ ] Create HuggingFace dataset loader

### 8.3 Taxonomy
- [ ] Finalize all synset IDs
- [ ] Define all relations
- [ ] Create visualization tools
- [ ] Build hierarchy navigation API

### 8.4 Evaluation
- [ ] Implement all metrics
- [ ] Build submission validation
- [ ] Create leaderboard backend
- [ ] Set up CI/CD for evaluation

---

*This specification is version 0.1. Updates will be tracked in CHANGELOG.md.*
