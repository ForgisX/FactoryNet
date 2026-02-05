# FactoryNet: A Large-Scale Hierarchical Dataset for Industrial Machine Understanding

**NeurIPS 2026 Datasets and Benchmarks Track - DRAFT**

*Authors: Karim [SURNAME], Jonas Petersen, [ETH Co-author], [Imperial Co-author], et al.*
*Affiliation: Forgis AG, ETH Zurich, Imperial College London*

---

## Abstract

We introduce **FactoryNet**, a large-scale hierarchical dataset for industrial machine understanding. Unlike existing fault detection datasets that focus on classification, FactoryNet tests machine understanding through a comprehensive question-answering framework inspired by reading comprehension benchmarks. Given sensor data (telemetry, vision, audio) and semantic priors (manuals, CAD/URDF), models must answer questions about machine state, predict behavior under interventions, reason about causes and effects, and generate actionable responses. We contribute: (1) a hierarchical taxonomy of 500+ machine states organized across five dimensions (Machine, State, Symptom, Cause, Action) inspired by WordNet; (2) 50,000+ annotated episodes from 7 machine types including 4 collaborative robots; (3) a Q&A evaluation framework with 200,000+ questions spanning 6 reasoning types; (4) comprehensive baselines including LLMs, vision-language models, and specialized architectures. FactoryNet enables rigorous evaluation of industrial world models—systems that understand machine physics well enough to answer arbitrary questions about behavior. We release the dataset, evaluation toolkit, and leaderboard at [URL].

**Keywords:** Dataset, Industrial AI, World Models, Multimodal, Hierarchical Taxonomy, Robotics

---

## 1. Introduction

Modern manufacturing loses $50 billion annually to unplanned downtime [1]. While AI has transformed image recognition and natural language understanding, industrial machines remain largely opaque to learning systems. Existing approaches treat fault detection as classification—mapping sensor patterns to discrete labels—but this misses a deeper goal: **machine understanding**.

Consider a technician diagnosing a malfunctioning robot. They don't simply classify the fault; they reason: *"The vibration signature at 147 Hz suggests bearing wear on joint 3. If I continue operating, the bearing will fail within 200 hours. To fix it, I need to replace the SKF 6205 bearing following procedure 3.5.2 in the manual."* This requires understanding the machine's physics, not just pattern matching.

We propose that true machine understanding should be evaluated the same way we evaluate language understanding—through **question answering**. Just as GLUE [2] and SuperGLUE [3] test whether language models understand text by asking comprehension questions, FactoryNet tests whether models understand machines by asking questions about their state, behavior, and repair.

**Key Insight (Figure 1):** Instead of generating images of predicted states (computationally expensive, hard to evaluate), we probe understanding through questions:
- *"What is the current state of joint 3?"* (State Recognition)
- *"If motor speed increases to 3000 RPM, will the part clear the obstacle?"* (Prediction)
- *"What caused the conveyor to stop?"* (Causal Reasoning)
- *"If sensor S2 hadn't failed, would the collision have occurred?"* (Counterfactual)

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   TRADITIONAL APPROACH              FACTORYNET APPROACH                     │
│   ──────────────────────           ─────────────────────                    │
│                                                                             │
│   Sensors ───► Classifier ───► Fault Label    Sensors ─┬─► Q&A Model ───►  │
│                    │                          Manual ──┤     │              │
│                    │                          CAD/URDF ┘     ▼              │
│              "bearing_fault"                          Answers + Reasoning   │
│                                                                             │
│   Limited to predefined classes     Tests genuine understanding through     │
│   No reasoning explanation          arbitrary questions about physics       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                        Figure 1: FactoryNet Evaluation Philosophy
```

### Contributions

1. **Hierarchical Taxonomy:** A 5-dimensional ontology (Machine × State × Symptom × Cause × Action) with 500+ concepts organized like WordNet, enabling hierarchical evaluation and cross-machine transfer testing.

2. **Large-Scale Dataset:** 50,000+ episodes from 7 machine types (4 cobots, 2 labeling machines, 1 conveyor), with synchronized multimodal data (telemetry, vision, audio) and semantic priors (manuals, URDF).

3. **Q&A Evaluation Framework:** 200,000+ questions across 6 reasoning types (state, prediction, causal, counterfactual, procedural, diagnostic), with anti-shortcut measures inspired by CLEVRER [4].

4. **Comprehensive Baselines:** Evaluation of classical methods, deep learning architectures, and LLM-based approaches, establishing performance benchmarks for future research.

5. **Open Resources:** Dataset, evaluation toolkit, pre-computed embeddings, and live leaderboard released under CC-BY-4.0 license.

---

## 2. Related Work

### Industrial Fault Datasets

| Dataset | Samples | Modalities | Machines | Task | Limitation |
|---------|---------|------------|----------|------|------------|
| C-MAPSS [5] | 4 subsets | 21 sensors | Turbofan (sim) | RUL | Simulated, single domain |
| CWRU [6] | ~480 files | Vibration | Bearings | Classification | Single component |
| MAFAULDA [7] | 1,951 | Vibration, audio | Rotating machinery | Classification | Lab testbed only |
| PHM 2010 [8] | 315 runs | Force, vibration, AE | CNC milling | Wear prediction | Single machine |
| XJTU-SY [25] | 15 bearings | Vibration | Bearings | RUL | Single component |
| Tennessee Eastman [26] | 21 faults | 52 sensors | Chemical process | Fault detection | Simulated |
| MetroPT [27] | 15 failures | Multimodal | Metro system | Predictive maint. | Domain-specific |
| **FactoryNet** | **50,000+** | **Multi-modal** | **7 machine types** | **Q&A Understanding** | - |

Existing datasets focus on **fault classification** for single machine types. FactoryNet shifts the paradigm to **machine understanding** across heterogeneous equipment.

### Robotics Datasets

Open X-Embodiment [9] demonstrated positive transfer across 22 robot types for manipulation policies. We adopt their episode-centric data format but focus on understanding rather than control. DROID [10] and RoboNet [11] provide large-scale robot video but lack fault annotations. FactoryNet bridges robotics and industrial fault diagnosis.

### Physical Reasoning Benchmarks

CLEVRER [4] introduced a taxonomy of physical reasoning questions (descriptive, explanatory, predictive, counterfactual) for video understanding. PHYRE [12] tests physical reasoning through interactive puzzles. IntPhys [13] uses violation-of-expectation to probe intuitive physics. We adapt these insights for industrial machines, adding domain-specific question types (procedural, diagnostic).

### World Models

DreamerV3 [14] learns latent dynamics for imagination-based planning. RT-2 [15] and PaLM-E [16] ground language models in robotic perception. We evaluate whether such approaches achieve genuine machine understanding, not just task completion.

---

## 3. The FactoryNet Taxonomy

### 3.1 Design Principles

Inspired by WordNet [17] and Gene Ontology [18], we organize industrial concepts across **five orthogonal dimensions**, each structured as a directed acyclic graph (DAG):

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         FACTORYNET TAXONOMY                                  │
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   MACHINE   │  │    STATE    │  │   SYMPTOM   │  │    CAUSE    │        │
│  │   (What)    │  │   (What     │  │    (How     │  │    (Why)    │        │
│  │             │  │  condition) │  │  observed)  │  │             │        │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘        │
│         │                │                │                │               │
│         ▼                ▼                ▼                ▼               │
│  ┌─────────────────────────────────────────────────────────────────┐       │
│  │                        ACTION (How to respond)                   │       │
│  └─────────────────────────────────────────────────────────────────┘       │
│                                                                             │
│  Relations: is_a, part_of, has_symptom, caused_by, fixed_by, indicates     │
└─────────────────────────────────────────────────────────────────────────────┘
                        Figure 2: Five-Dimensional Taxonomy
```

### 3.2 Machine Dimension (Depth: 6 levels)

```
machine
├── robot
│   ├── collaborative_robot
│   │   ├── abb_yumi
│   │   ├── universal_robots
│   │   │   └── ur3 ← [FactoryNet instance]
│   │   └── ...
│   └── industrial_robot
│       └── 6_axis_robot
│           ├── abb_irb_2600 ← [FactoryNet instance]
│           └── kuka_kr10 ← [FactoryNet instance]
├── conveyor
│   └── belt_conveyor ← [FactoryNet instance]
└── labeling_machine
    ├── herma_labeler ← [FactoryNet instance]
    └── spr_labeler ← [FactoryNet instance]
```

**Cross-Machine Transfer Evaluation:**
| Split | Train | Test | Tests |
|-------|-------|------|-------|
| Within-family | ABB IRB 2600 | ABB YUMI | Same manufacturer |
| Cross-manufacturer | ABB + KUKA | UR3 | Different manufacturers |
| Cross-category | All robots | Labeling machines | Different machine types |

### 3.3 State Dimension (Karim's Fault Framework)

We integrate the fault characteristics framework (time, space, dynamic, dropout, bias, variance) as **orthogonal attributes** on state concepts:

```
state
├── normal_operation
│   ├── idle
│   ├── executing_program
│   └── manual_mode
├── degraded_operation
│   ├── reduced_performance
│   │   └── [temporal: gradual, spatial: distributed]
│   └── intermittent_fault
│       └── [temporal: intermittent, spatial: point]
├── fault_state
│   ├── mechanical_fault
│   │   ├── wear_fault
│   │   │   └── bearing_wear
│   │   │       ├── inner_race_wear
│   │   │       ├── outer_race_wear
│   │   │       └── ball_wear
│   │   └── alignment_fault
│   ├── electrical_fault
│   │   ├── signal_drift [BIAS]
│   │   ├── signal_noise [VARIANCE]
│   │   └── signal_loss [DROPOUT]
│   └── software_fault
│       └── communication_timeout [DROPOUT]
└── emergency_state
    └── safety_stop
```

**Attribute Schema:**
```yaml
state_attributes:
  temporal: [sudden, gradual, intermittent, cyclic]
  spatial: [point, distributed, propagating]
  dynamic: [static, dynamic, progressive]
  severity: [minor, moderate, critical]
```

### 3.4 Synset ID Encoding

Each concept has a unique hierarchical ID (inspired by ICD codes):

```
Format: {Dimension}.{L1}.{L2}.{L3}.{L4}.{L5}

Examples:
M.rob.col.ur.ur3        → Machine > Robot > Collaborative > UR > UR3
S.flt.mec.wea.bea.inn   → State > Fault > Mechanical > Wear > Bearing > Inner
Y.vib.hig.bea.bpfo      → Symptom > Vibration > High-freq > Bearing > BPFO
C.mai.ina.lub           → Cause > Maintenance > Inadequate > Lubrication
A.rep.rep.bea.6205      → Action > Repair > Replace > Bearing > 6205
```

### 3.5 Taxonomy Statistics

| Dimension | Concepts | Max Depth | Relations |
|-----------|----------|-----------|-----------|
| Machine | 47 | 6 | is_a, part_of |
| State | 156 | 6 | is_a, temporal/spatial attributes |
| Symptom | 89 | 5 | is_a, indicates |
| Cause | 73 | 5 | is_a, caused_by |
| Action | 134 | 6 | is_a, fixed_by, requires_tool |
| **Total** | **499** | - | **1,247 relations** |

---

## 4. Dataset Construction

### 4.1 Data Sources

FactoryNet combines three data streams:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         DATA SOURCES                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   REAL DATA     │  │  ADAPTED DATA   │  │ SYNTHETIC DATA  │             │
│  │  (FactoryCell)  │  │ (Open Datasets) │  │  (Simulation)   │             │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘             │
│           │                    │                    │                       │
│  • 4 cobots           • CWRU bearings      • Isaac Sim robots               │
│  • 2 labelers         • Paderborn          • Domain randomization           │
│  • 1 conveyor         • MAFAULDA           • Physics-based faults           │
│  • 10,000 episodes    • PHM 2010           • 30,000 episodes                │
│                       • 10,000 adapted                                      │
│                                                                             │
│           └────────────────────┼────────────────────┘                       │
│                                ▼                                            │
│                    ┌─────────────────────┐                                  │
│                    │   UNIFIED SCHEMA    │                                  │
│                    │   50,000+ episodes  │                                  │
│                    └─────────────────────┘                                  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                        Figure 3: Data Source Integration
```

### 4.2 FactoryCell Hardware Testbed

[TODO: Insert photo of mini-factory]

| Equipment | Model | Sensors | Episodes |
|-----------|-------|---------|----------|
| Cobot 1 | ABB IRB 2600 | Joint encoders, current, F/T, camera | 2,500 |
| Cobot 2 | ABB YUMI | Dual-arm encoders, current, camera | 2,000 |
| Cobot 3 | Universal Robots UR3 | Joint encoders, current, camera | 2,500 |
| Cobot 4 | KUKA KR10 | Joint encoders, current, camera | 2,000 |
| Labeler 1 | Herma H400 | Vibration, current, vision | 500 |
| Labeler 2 | SPR Max | Vibration, current, vision | 300 |
| Conveyor | Custom belt | Vibration, current, proximity | 200 |
| **Total** | - | - | **10,000** |

### 4.3 Adapted Open Datasets

We adapt 6 open-source datasets to FactoryNet schema:

| Source | Original Domain | Adapted Samples | License |
|--------|-----------------|-----------------|---------|
| CWRU [6] | Bearings | 2,500 | Academic |
| Paderborn [19] | Bearings | 2,000 | CC-BY-4.0 |
| XJTU-SY [25] | Bearings (run-to-failure) | 2,000 | Academic |
| MAFAULDA [7] | Rotating machinery | 1,500 | CC-like |
| IMS/NASA [20] | Bearings | 1,000 | Public domain |
| PHM 2010 [8] | CNC milling | 1,000 | Research |
| **Total** | - | **10,000** | - |

**Adaptation Process:**
1. Map original labels to FactoryNet taxonomy
2. Extract standardized features (vibration spectra, RMS, kurtosis)
3. Generate Q&A annotations using templates + expert review
4. Add synthetic semantic priors (generic bearing/motor manuals)

### 4.4 Synthetic Data Generation

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SYNTHETIC DATA PIPELINE                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐                │
│  │ Robot URDF   │────▶│  Isaac Sim   │────▶│   Sensors    │                │
│  │ + CAD Models │     │  + Physics   │     │   Streams    │                │
│  └──────────────┘     └──────────────┘     └──────────────┘                │
│                              │                    │                         │
│                              ▼                    │                         │
│                    ┌──────────────┐               │                         │
│                    │Fault Injection│               │                         │
│                    │    Engine     │               │                         │
│                    └──────────────┘               │                         │
│                              │                    │                         │
│   Fault Models:              ▼                    ▼                         │
│   • Bearing wear      ┌──────────────────────────────┐                     │
│   • Motor degradation │   Domain Randomization       │                     │
│   • Misalignment      │   • Physics params (±20%)    │                     │
│   • Sensor drift      │   • Visual (lighting, tex)   │                     │
│   • Communication     │   • Sensor noise (1-5%)      │                     │
│                       └──────────────────────────────┘                     │
│                                      │                                      │
│                                      ▼                                      │
│                       ┌──────────────────────────────┐                     │
│                       │     30,000 Synthetic         │                     │
│                       │        Episodes              │                     │
│                       └──────────────────────────────┘                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                        Figure 4: Synthetic Data Pipeline
```

**Physics-Based Fault Models:**

| Fault Type | Model | Parameters |
|------------|-------|------------|
| Bearing wear | Spall propagation + characteristic frequencies | Defect size, growth rate |
| Motor fault | Torque ripple + current harmonics | Shorted turns, eccentricity |
| Misalignment | Angular/parallel offset + vibration signatures | Offset magnitude, direction |
| Sensor drift | Linear/nonlinear bias accumulation | Drift rate, noise level |

**Domain Randomization Ranges:**

| Parameter | Range | Purpose |
|-----------|-------|---------|
| Mass | ±20% | Part variation |
| Friction | 0.3-1.2 | Surface conditions |
| Sensor noise | 1-5% | Sensor quality |
| Lighting | 0.3-2.0× | Visual variation |
| Latency | 0-50ms | Communication |

### 4.5 Semantic Prior Integration

Each episode is linked to semantic priors:

```yaml
semantic_priors:
  urdf_path: "/models/abb_irb_2600.urdf"
  manual_sections:
    - path: "ABB_IRB_2600_Manual.pdf#page=147"
      content_embedding: Tensor[768]  # Pre-computed
      relevant_topics: ["bearing_replacement", "joint_3"]
  error_code_database:
    - code: "10036"
      description: "Joint 3 following error exceeded"
      manual_ref: "Section 5.2.1"
  cad_model: "/models/abb_irb_2600.step"
```

### 4.6 Episode Schema

```python
FactoryNetEpisode = {
    # Identification
    "episode_id": "FN-2026-00001",
    "source": "factorynet_real",  # real | adapted | synthetic
    "machine_synset": "M.rob.col.ur.ur3",
    "machine_instance": "UR3-FACTORY-001",

    # Temporal
    "timestamp_start": "2026-02-04T14:30:00Z",
    "duration_seconds": 120.5,
    "sampling_rate_hz": 100,

    # Multimodal Data
    "steps": [  # T timesteps
        {
            "timestamp": float,
            "proprioception": {
                "joint_positions": Tensor[N_joints],
                "joint_velocities": Tensor[N_joints],
                "joint_torques": Tensor[N_joints],
                "motor_currents": Tensor[N_joints],
            },
            "exteroception": {
                "rgb_image": Tensor[H, W, 3],  # Optional
                "depth_image": Tensor[H, W],   # Optional
                "force_torque": Tensor[6],
            },
            "condition_monitoring": {
                "vibration": Tensor[N_channels],
                "temperature": Tensor[N_sensors],
                "acoustic": Tensor[N_mics],
            },
            "discrete_state": {
                "plc_state": Dict,
                "error_codes": List[str],
                "safety_status": str,
            },
        },
        ...
    ],

    # Labels
    "state_trajectory": {
        "state_synset": "S.flt.mec.wea.bea.inn",
        "onset_step": 450,
        "severity_trajectory": Tensor[T],
        "attributes": {
            "temporal": "gradual",
            "spatial": "point",
        },
    },
    "cause_synset": "C.mai.ina.lub",
    "action_sequence": ["A.dia.ins.vib", "A.rep.rep.bea.6205"],

    # Semantic Priors
    "semantic_priors": {
        "urdf_path": str,
        "manual_embeddings": Tensor[N_sections, 768],
        "relevant_manual_pages": List[str],
    },

    # Q&A Annotations (Section 5)
    "qa_annotations": List[QAPair],  # Each QAPair includes difficulty, criticality, required_expertise
}
```

### 4.7 Dataset Statistics

| Statistic | Value |
|-----------|-------|
| Total episodes | 50,000+ |
| Total timesteps | ~500M |
| Unique machines | 7 types, 15 instances |
| Unique states | 156 taxonomy concepts |
| State distribution | 60% normal, 40% fault/degraded |
| Avg episode duration | 120 seconds |
| Storage size | ~2 TB (full), ~50 GB (features only) |

---

## 5. Question-Answering Evaluation Framework

### 5.1 Question Taxonomy

Inspired by CLEVRER [4], we define 6 question types that probe different aspects of machine understanding:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         QUESTION TAXONOMY                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TYPE 1: STATE RECOGNITION (What is happening?)                             │
│  ──────────────────────────────────────────────                             │
│  Q: "What is the current state of joint 3?"                                 │
│  A: "Joint 3 is in position 45.2° with velocity 0 rad/s (stationary)"       │
│                                                                             │
│  Q: "Is the gripper open or closed?"                                        │
│  A: "The gripper is closed with 15N grip force"                             │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TYPE 2: PREDICTION (What will happen?)                                     │
│  ──────────────────────────────────────                                     │
│  Q: "If motor speed increases to 3000 RPM, will temperature exceed 80°C?"   │
│  A: "Yes, based on thermal model, temperature will reach ~95°C in 5 min"    │
│                                                                             │
│  Q: "How far will the arm rotate if I send command move_joint(2, 45)?"      │
│  A: "Joint 2 will rotate 45° from current position, reaching 90° absolute"  │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TYPE 3: CAUSAL REASONING (Why did it happen?)                              │
│  ─────────────────────────────────────────────                              │
│  Q: "What caused the vibration spike at t=45s?"                             │
│  A: "Inner race bearing defect - characteristic frequency 147Hz matches     │
│      BPFI for this bearing at current speed"                                │
│                                                                             │
│  Q: "Why did the conveyor stop?"                                            │
│  A: "Safety sensor S3 detected object in restricted zone, triggering E-stop"│
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TYPE 4: COUNTERFACTUAL (What if?)                                          │
│  ─────────────────────────────────                                          │
│  Q: "If sensor S2 hadn't failed, would the collision have occurred?"        │
│  A: "No - S2 would have detected the obstacle and triggered avoidance"      │
│                                                                             │
│  Q: "What if we had replaced the bearing last month?"                       │
│  A: "The current fault would not have occurred; bearing was at 85% wear"    │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TYPE 5: PROCEDURAL (How to do it?)                                         │
│  ──────────────────────────────────                                         │
│  Q: "What is the correct sequence to restart after E-stop?"                 │
│  A: "1) Clear obstruction 2) Reset E-stop 3) Re-home robot 4) Resume prog"  │
│                                                                             │
│  Q: "How do I replace the bearing on joint 3?"                              │
│  A: "Per manual 3.5.2: 1) Power off 2) Remove cover 3) Use puller..."       │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  TYPE 6: DIAGNOSTIC (What's wrong and is it possible?)                      │
│  ────────────────────────────────────────────────────                       │
│  Q: "Is this sensor reading physically possible given the robot's state?"   │
│  A: "No - joint 3 encoder shows 180° but motor current suggests 90°"        │
│                                                                             │
│  Q: "Given symptoms X, Y, Z, what is the most likely fault?"                │
│  A: "85% probability of outer race bearing fault based on BPFO + thermal"   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                        Figure 5: Question Taxonomy with Examples
```

### 5.2 Question Generation Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│  Episode Data ──────┐                                                       │
│                     │                                                       │
│  Taxonomy ──────────┼──► Template Engine ──► Candidate Questions            │
│                     │          │                    │                       │
│  Manual Knowledge ──┘          │                    ▼                       │
│                                │         ┌─────────────────────┐            │
│                                │         │  Expert Filtering   │            │
│                                │         │  • Answerability    │            │
│                                │         │  • Difficulty       │            │
│                                │         │  • Balance          │            │
│                                │         └──────────┬──────────┘            │
│                                │                    │                       │
│                                ▼                    ▼                       │
│                    ┌─────────────────────────────────────────┐              │
│                    │         Final Q&A Pairs                 │              │
│                    │   200,000+ questions across 6 types     │              │
│                    └─────────────────────────────────────────┘              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Template Examples:**
```python
STATE_TEMPLATES = [
    "What is the current {quantity} of {component}?",
    "Is {component} in {state} state?",
    "What error codes are currently active?",
]

PREDICTION_TEMPLATES = [
    "If {action}, will {outcome}?",
    "What will be the {quantity} after {duration} of operation?",
    "If {parameter} changes to {value}, what happens to {target}?",
]

COUNTERFACTUAL_TEMPLATES = [
    "If {event} had not occurred, would {outcome} have happened?",
    "What would be different if {alternative_action} instead of {actual_action}?",
]
```

### 5.3 Anti-Shortcut Measures

To prevent models from exploiting superficial patterns, we implement:

| Measure | Description | Implementation |
|---------|-------------|----------------|
| **Compositional splits** | Test on novel machine × fault combinations | Hold out specific pairs |
| **Contrastive pairs** | Same episode, opposite answers required | Generate paired questions |
| **Balanced answers** | 50/50 yes/no for binary questions | Template balancing |
| **Reasoning required** | Explanation must be consistent with answer | Score reasoning chain |
| **Grounding verification** | Model must cite evidence | Check source references |

**Example Contrastive Pair:**
- Q1: "Did bearing wear cause the vibration?" A1: "Yes" (episode with bearing fault)
- Q2: "Did bearing wear cause the vibration?" A2: "No" (similar vibration, different cause)

### 5.4 Q&A Statistics

| Question Type | Count | Avg Length | Answer Types |
|---------------|-------|------------|--------------|
| State | 45,000 | 12 words | Numeric, categorical |
| Prediction | 38,000 | 18 words | Yes/no, numeric |
| Causal | 42,000 | 15 words | Free-form, multiple choice |
| Counterfactual | 28,000 | 20 words | Yes/no + explanation |
| Procedural | 25,000 | 14 words | Sequence, reference |
| Diagnostic | 22,000 | 16 words | Categorical, probability |
| **Total** | **200,000** | 16 words | Mixed |

### 5.5 Q&A Assessment Metadata

Each question is annotated with three assessment dimensions enabling nuanced evaluation beyond raw accuracy:

**Difficulty** (estimated reasoning complexity):
- **Easy** (40%): Direct sensor lookup, single-step reasoning
- **Medium** (35%): Combining 2-3 information sources, basic domain knowledge
- **Hard** (25%): Multi-step reasoning, expert domain knowledge required

**Criticality** (impact of incorrect answers):
- **Safety-critical** (15%): Incorrect answer could lead to injury, equipment damage, or hazardous conditions (e.g., E-stop procedures, collision avoidance, failure predictions)
- **Operational** (55%): Affects machine efficiency, maintenance scheduling, or production quality
- **Informational** (30%): General knowledge queries with no immediate operational impact

**Required Expertise** (domain knowledge level):
- **Operator** (35%): Basic machine operation knowledge
- **Technician** (40%): Maintenance and troubleshooting skills
- **Engineer** (25%): Deep domain expertise, physics understanding

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Q&A ASSESSMENT METADATA                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  DIFFICULTY                  CRITICALITY              REQUIRED EXPERTISE    │
│  ──────────                  ───────────              ──────────────────    │
│                                                                             │
│  ┌─────────┐ 40%            ┌─────────────┐ 15%      ┌──────────┐ 35%      │
│  │  Easy   │                │   Safety-   │          │ Operator │          │
│  └─────────┘                │   Critical  │          └──────────┘          │
│  ┌─────────┐ 35%            └─────────────┘          ┌──────────┐ 40%      │
│  │ Medium  │                ┌─────────────┐ 55%      │Technician│          │
│  └─────────┘                │ Operational │          └──────────┘          │
│  ┌─────────┐ 25%            └─────────────┘          ┌──────────┐ 25%      │
│  │  Hard   │                ┌─────────────┐ 30%      │ Engineer │          │
│  └─────────┘                │Informational│          └──────────┘          │
│                             └─────────────┘                                 │
│                                                                             │
│  Enables: Difficulty-       Enables: Safety-         Enables: Expertise-   │
│  stratified analysis        weighted scoring         level benchmarking    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                        Figure 6: Q&A Assessment Metadata Distribution
```

**Key Insight:** A model with 90% overall accuracy but only 60% on safety-critical questions may be less suitable for deployment than a model with 85% overall but 80% on safety-critical questions. These metadata fields enable such nuanced comparisons.

---

## 6. Evaluation Metrics

### 6.1 Per-Question-Type Metrics

| Type | Primary Metric | Secondary Metrics |
|------|----------------|-------------------|
| State | Accuracy / MAE | Precision, Recall |
| Prediction | Accuracy / RMSE | Calibration |
| Causal | Accuracy | Explanation quality (human eval) |
| Counterfactual | Accuracy | Consistency score |
| Procedural | BLEU / ROUGE | Step accuracy |
| Diagnostic | F1 / AUC | Ranking quality |

### 6.2 Hierarchical Metrics

**Hierarchical Accuracy:** Credit for partially correct taxonomy predictions:

```
HA(pred, true) = depth(LCA(pred, true)) / depth(true)

Example:
- True: S.flt.mec.wea.bea.inn (inner race wear)
- Pred: S.flt.mec.wea.bea.out (outer race wear)
- HA = 4/5 = 0.80 (correct to bearing level)
```

### 6.3 Aggregate Metrics

**FactoryNet Score (FNS):** Weighted average across question types:

```
FNS = Σ_i w_i × Accuracy_i

Default weights: State=0.15, Prediction=0.20, Causal=0.20,
                Counterfactual=0.20, Procedural=0.10, Diagnostic=0.15
```

### 6.4 Criticality-Weighted Metrics

**Safety-Weighted Accuracy (SWA):** Penalizes failures on critical questions:

```
SWA = Σ_c w_c × Accuracy_c × N_c / Σ_c w_c × N_c

Default weights: safety_critical=3.0, operational=1.5, informational=1.0
```

**Safety Failure Rate (SFR):** Critical deployment metric:

```
SFR = (Incorrect safety-critical answers) / (Total safety-critical questions)
```

| Metric | Description | Use Case |
|--------|-------------|----------|
| SWA | Criticality-weighted accuracy | Deployment readiness |
| SFR | Safety-critical failure rate | Risk assessment |
| Acc@Difficulty | Accuracy stratified by difficulty | Model capability analysis |
| Acc@Expertise | Accuracy stratified by required expertise | Target user evaluation |

### 6.6 Transfer Metrics

| Transfer Type | Metric |
|---------------|--------|
| Cross-machine | FNS on held-out machine type |
| Cross-fault | Accuracy on unseen fault categories |
| Zero-shot | Performance with no task-specific training |
| Few-shot | Performance with k={1,5,10} examples |
| Safety-critical transfer | SWA on unseen machine types |

---

## 7. Experiments

### 7.1 Baselines

We evaluate four categories of approaches:

**Category 1: Classical Methods (Multiple-Choice Setting)**
- Random baseline
- SVM + handcrafted features (spectral, statistical)
- XGBoost + feature engineering

*Note:* Classical methods do not generate natural language. We evaluate them in a **multiple-choice setting** where each question is presented with 4-5 candidate answers. The classifier selects among options based on extracted sensor features. This applies to question types with categorical/structured answers (State, Prediction yes/no, Diagnostic). For free-form questions (Procedural explanations, detailed Causal reasoning), classical methods are marked N/A.

**Category 2: Deep Learning (Sensor-Only)**
- TCN (Temporal Convolutional Network) [21]
- Transformer encoder [22]
- TimeSformer (video) [23]

*Evaluated in both multiple-choice and classification-to-template modes.*

**Category 3: Multimodal Deep Learning**
- CLIP-style sensor-text alignment
- Late fusion (sensor encoder + text encoder)
- Cross-attention multimodal transformer

**Category 4: LLM-Based**
- GPT-4 zero-shot (text description of sensors)
- GPT-4 + RAG (manual retrieval)
- Claude + RAG
- Fine-tuned LLaMA-3 on FactoryNet

*LLM-based methods are evaluated on all question types with free-form generation.*

[TODO: Add results table after experiments]

### 7.2 Main Results

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                              MAIN RESULTS (PLACEHOLDER)                               │
├──────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  Model                    State  Pred  Causal  Counter  Proc  Diag   FNS    SWA     │
│  ──────────────────────────────────────────────────────────────────────────────────  │
│  Random                   XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  SVM + Features           XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  XGBoost                  XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  ──────────────────────────────────────────────────────────────────────────────────  │
│  TCN                      XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  Transformer              XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  TimeSformer              XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  ──────────────────────────────────────────────────────────────────────────────────  │
│  CLIP-Industrial          XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  Multimodal Fusion        XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  ──────────────────────────────────────────────────────────────────────────────────  │
│  GPT-4 Zero-shot          XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  GPT-4 + RAG              XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  Claude + RAG             XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  LLaMA-3 Fine-tuned       XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│  ──────────────────────────────────────────────────────────────────────────────────  │
│  Human Expert             XX.X   XX.X   XX.X    XX.X    XX.X  XX.X   XX.X   XX.X    │
│                                                                                      │
│  Table 1: Main results on FactoryNet test set. FNS=FactoryNet Score,                │
│  SWA=Safety-Weighted Accuracy. Best per-category bolded.                            │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

### 7.3 Criticality Analysis

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                         CRITICALITY BREAKDOWN (PLACEHOLDER)                          │
├──────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  Model                    Safety-Crit  Operational  Informational   SFR (↓)         │
│  ──────────────────────────────────────────────────────────────────────────────────  │
│  GPT-4 + RAG              XX.X         XX.X         XX.X            XX.X            │
│  Claude + RAG             XX.X         XX.X         XX.X            XX.X            │
│  LLaMA-3 Fine-tuned       XX.X         XX.X         XX.X            XX.X            │
│  Multimodal Fusion        XX.X         XX.X         XX.X            XX.X            │
│  ──────────────────────────────────────────────────────────────────────────────────  │
│  Human Expert             XX.X         XX.X         XX.X            XX.X            │
│                                                                                      │
│  Table 2: Accuracy by question criticality. SFR = Safety Failure Rate (lower        │
│  is better). Models may have high overall accuracy but poor safety-critical         │
│  performance.                                                                        │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

### 7.4 Transfer Learning Results

[TODO: Cross-machine transfer table]

### 7.5 Ablation Studies

**Impact of Semantic Priors:**

| Configuration | FNS | Δ vs. Full |
|---------------|-----|------------|
| Full (sensors + URDF + manual) | XX.X | - |
| No manual | XX.X | -X.X |
| No URDF | XX.X | -X.X |
| Sensors only | XX.X | -X.X |

**Impact of Question Type Distribution:**

[TODO: Results varying question type weights]

### 7.6 Analysis

**What Makes Questions Hard?**

[TODO: Difficulty analysis by:
- Fault rarity
- Causal chain depth
- Required reasoning steps
- Cross-machine transfer
- Criticality level correlation]

**Safety-Critical Failure Analysis:**

[TODO: Analyze which types of safety-critical questions models fail most:
- E-stop/emergency procedures
- Collision prediction
- Failure consequence reasoning
- Counterfactual safety scenarios]

**Error Analysis:**

[TODO: Common failure modes for each model category]

---

## 8. Discussion

### 8.1 Key Findings

[TODO after experiments:
1. Finding about semantic priors
2. Finding about cross-machine transfer
3. Finding about counterfactual reasoning
4. Gap between LLMs and specialized models
5. Finding about safety-critical performance vs overall accuracy
6. Which model categories perform best on safety-critical questions]

### 8.2 Limitations

1. **Machine Diversity:** Currently limited to 7 machine types; industrial settings have thousands.
2. **Simulated Faults:** Synthetic data may not capture all real-world fault characteristics.
3. **Q&A Coverage:** Questions generated from templates may miss edge cases.
4. **Language Bias:** Questions in English only; industrial settings are multilingual.
5. **Static Dataset:** Machines and faults evolve; dataset requires updates.

### 8.3 Broader Impact

**Positive:** FactoryNet could accelerate development of AI systems that help technicians diagnose and repair equipment, reducing downtime and improving safety.

**Risks:** Overreliance on AI diagnostics without human verification could lead to missed faults or incorrect repairs. We recommend FactoryNet models be used as decision support, not autonomous decision-makers.

---

## 9. Conclusion

We introduced FactoryNet, the first large-scale benchmark for evaluating machine understanding in industrial AI. By framing evaluation as question-answering rather than classification, FactoryNet tests whether models genuinely understand machine physics. Our hierarchical taxonomy, multimodal data, and Q&A framework establish a foundation for developing and evaluating industrial world models.

**Future Work:**
- Extend to more machine types and real-world deployments
- Add multilingual questions
- Develop interactive benchmark with FactoryCell hardware
- Create FactoryNet-Lite for efficient development

---

## 10. Reproducibility and Data Access

**Dataset:** Available at https://huggingface.co/datasets/forgis/factorynet [TODO: create]

**Code:** Evaluation toolkit at https://github.com/forgis-ai/factorynet [TODO: create]

**Leaderboard:** https://factorynet.forgis.com [TODO: create]

**License:** CC-BY-4.0 (data), Apache-2.0 (code)

**Compute:** Experiments run on [TODO: specify cluster/GPUs]

**Datasheet:** See Appendix A for full datasheet per [24].

---

## References

[1] Deloitte. "The future of maintenance." 2022.
[2] Wang et al. "GLUE: A multi-task benchmark for NLU." EMNLP 2018.
[3] Wang et al. "SuperGLUE: A stickier benchmark for NLU." NeurIPS 2019.
[4] Yi*, Gan* et al. "CLEVRER: CoLlision Events for Video REpresentation and Reasoning." ICLR 2020.
[5] Saxena, Goebel, Simon, Eklund. "Damage propagation modeling for aircraft engine run-to-failure simulation." PHM 2008.
[6] Case Western Reserve University Bearing Data Center. Available: https://engineering.case.edu/bearingdatacenter
[7] Ribeiro et al. "Rotating machinery fault diagnosis using similarity-based models." SBrT 2017.
[8] PHM Society. "2010 PHM Society Conference Data Challenge: CNC Milling Machine Cutter RUL Estimation." 2010.
[9] Open X-Embodiment Collaboration. "Open X-Embodiment: Robotic learning datasets and RT-X models." CoRL 2023.
[10] Khazatsky et al. "DROID: A large-scale in-the-wild robot manipulation dataset." RSS 2024.
[11] Dasari et al. "RoboNet: Large-scale multi-robot learning." CoRL 2019.
[12] Bakhtin et al. "PHYRE: A new benchmark for physical reasoning." NeurIPS 2019.
[13] Riochet et al. "IntPhys: A Framework and Benchmark for Visual Intuitive Physics Reasoning." IEEE TPAMI 2022 (arXiv 2018).
[14] Hafner et al. "Mastering diverse domains through world models." arXiv:2301.04104, 2023.
[15] Brohan et al. "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control." CoRL 2023.
[16] Driess et al. "PaLM-E: An embodied multimodal language model." ICML 2023.
[17] Miller. "WordNet: A lexical database for English." CACM 1995.
[18] Ashburner et al. "Gene Ontology." Nature Genetics 2000.
[19] Lessmeier et al. "Condition Monitoring of Bearing Damage in Electromechanical Drive Systems by Using Motor Current Signals." PHM Europe 2016.
[20] Qiu et al. "Wavelet filter-based weak signature detection method and its application on rolling element bearing prognostics." Journal of Sound and Vibration 2006.
[21] Bai et al. "An empirical evaluation of generic convolutional and recurrent networks for sequence modeling." 2018.
[22] Vaswani et al. "Attention is all you need." NeurIPS 2017.
[23] Bertasius et al. "Is space-time attention all you need for video understanding?" ICML 2021.
[24] Gebru et al. "Datasheets for datasets." CACM 2021.
[25] Lei et al. "XJTU-SY Rolling Element Bearing Accelerated Life Test Datasets: A Tutorial." Journal of Mechanical Engineering 2019.
[26] Downs, Vogel. "A plant-wide industrial process control problem (Tennessee Eastman)." Computers & Chemical Engineering 1993.
[27] Veloso et al. "The MetroPT dataset for predictive maintenance." Scientific Data 2022.

---

## Appendix A: Datasheet for FactoryNet

[TODO: Complete datasheet following Gebru et al. template]

### A.1 Motivation
- **Purpose:** Evaluate machine understanding in industrial AI systems
- **Creators:** Forgis AG, ETH Zurich, Imperial College London
- **Funding:** Forgis internal research

### A.2 Composition
- **Instances:** 50,000+ episodes with multimodal sensor data
- **Sampling:** Balanced across machine types and fault categories
- **Missing data:** <2% of timesteps have sensor dropouts (labeled)

### A.3 Collection Process
[TODO: Details on annotation, quality control]

### A.4 Preprocessing
[TODO: Feature extraction, normalization procedures]

### A.5 Uses
- Intended: Research on industrial AI, world models, multimodal learning
- Not intended: Safety-critical deployment without human oversight

### A.6 Distribution
- Platform: Hugging Face Datasets
- License: CC-BY-4.0
- Access: Open

### A.7 Maintenance
- Updates: Quarterly with new episodes
- Contact: factorynet@forgis.com

---

## Appendix B: Full Taxonomy

[TODO: Complete 499-concept taxonomy in structured format]

---

## Appendix C: Question Templates

[TODO: All templates for each question type]

---

## Appendix D: Baseline Implementation Details

[TODO: Hyperparameters, training procedures]

---

## Appendix E: Additional Results

[TODO: Extended results tables, visualizations]

---

# OPEN TODOs FOR COMPLETION

## Data Collection
- [ ] Collect remaining episodes from FactoryCell (target: 10,000 real)
- [ ] Complete adaptation of open datasets (target: 10,000 adapted)
- [ ] Generate synthetic episodes (target: 30,000)
- [ ] Expert review of Q&A annotations

## Experiments
- [ ] Train and evaluate all baselines
- [ ] Complete ablation studies
- [ ] Cross-machine transfer experiments
- [ ] Human expert evaluation

## Paper
- [ ] Insert actual photos/figures
- [ ] Fill in results tables
- [ ] Complete error analysis
- [ ] Finalize datasheet

## Infrastructure
- [ ] Set up HuggingFace dataset
- [ ] Create GitHub repository
- [ ] Build leaderboard website
- [ ] Prepare submission package

## Timeline
- [ ] April 2026: Data collection complete
- [ ] May 2026: Baselines complete
- [ ] May 15, 2026: Paper draft complete
- [ ] May 19, 2026: NeurIPS D&B submission

---

*This draft is a working document. All placeholder values (XX.X) and [TODO] items to be completed before submission.*
