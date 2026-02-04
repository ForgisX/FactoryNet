# FactoryNet Literature Review: State Prediction from Sensor Data + Semantic Priors

*Compiled: 2026-02-04*
*For: Karim's Master Thesis at Forgis*

---

## Executive Summary

This review synthesizes literature across 7 research areas to support the FactoryNet thesis direction: **learning to predict machine state (3D/CAD/URDF) from sensor data combined with semantic priors (manuals)**. The key insight from Philipp: evaluate understanding through **Q&A** rather than image generation.

**Core Research Questions:**
1. Can semantic priors (URDF + manuals) reduce sample complexity for state prediction?
2. Does multi-robot training enable generalization to unseen robots and machine types?
3. Is Q&A evaluation more effective than image generation for testing world model understanding?

---

## 1. Robot State Estimation from Sensors

### Key Techniques

| Method | Best For | Your Cobots |
|--------|----------|-------------|
| EKF/UKF | Real-time fusion with known dynamics | KUKA KR10 |
| LSTM/GRU | Temporal patterns from sequences | UR3 (well-documented) |
| GNN on kinematic graph | Multi-link, coupled dynamics | ABB YUMI (dual-arm) |
| Motor current sensing | Sensorless torque estimation | All cobots |
| Momentum observer | External force detection | ABB IRB 2600 |

### Recommended Architecture for Your Fleet
```
[Joint Encoders] ──┬──> [EKF/UKF] ──> [Proprioceptive Estimate]
[Motor Currents] ──┘                          │
                                              ▼
[External Vision] ──> [CNN Keypoints] ──> [Attention Fusion] ──> [State]
                                              ▲
[F/T Sensor] ──> [Momentum Observer] ──> [Contact State]
```

### Key Papers
- Kim et al. (2021) - "Multi-Sensor Fusion Survey" - Taxonomy of fusion approaches
- Florence et al. (2022) - "RoboPose" - Vision-based state estimation
- Kim & Lee (2023) - "GNN for Robot State" - Graph-based methods

### Gap Identified
**No benchmark for ABB/UR/KUKA cobots under industrial conditions** → Opportunity for FactoryBench

---

## 2. URDF/CAD as Structural Priors

### Key Insight
Known robot structure provides powerful inductive bias that significantly reduces sample complexity.

### Techniques

**URDF to Graph Conversion:**
```
URDF Structure → Graph G = (V, E)
- Nodes V: Links with features [mass, inertia, geometry]
- Edges E: Joints with features [type, axis, limits, damping]
```

**Architecture for Multi-Robot State Prediction:**
```
URDF/CAD + Sensors
        ↓
┌─────────────────────────────────────┐
│ Per-Robot GNN Encoder (structure)   │
│ - Parse URDF → kinematic graph      │
│ - Message passing on structure      │
│ - CAD geometry features             │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ Multi-Robot Cross-Attention         │
└─────────────────────────────────────┘
        ↓
┌─────────────────────────────────────┐
│ Structure-Constrained Decoder       │
│ - Per-joint state prediction        │
│ - FK layer enforces constraints     │
└─────────────────────────────────────┘
```

### Key Papers
- **MetaMorph** (ICLR 2022) - Universal controllers with morphology tokens
- **Dojo** (RSS 2022) - Differentiable dynamics with contact
- **Neural Descriptor Fields** (ICRA 2022) - SE(3)-equivariant representations
- **Brax** (NeurIPS 2021) - Differentiable simulator with URDF

### Libraries
- `yourdfpy` / `urdfpy` - URDF parsing
- `PyTorch Geometric` - GNN implementation
- `e3nn` - SE(3)-equivariant networks
- `Drake` / `MuJoCo` - Differentiable dynamics

---

## 3. World Models & Foundation Models for Robotics

### What "World Model" Means

| Context | Definition |
|---------|------------|
| **Dreamer lineage** | Learned latent dynamics for imagination-based planning |
| **Video prediction** | Next-frame predictor as implicit physics (UniSim, GAIA-1) |
| **RT-2/RT-X** | Generalist policy with implicit world understanding |
| **Industrial (your target)** | State estimation + fault prediction with semantic grounding |

### Key Architecture: Latent World Model with Semantic Conditioning
```
                ┌─────────────────────────────────────────┐
                │     Semantic Foundation Model           │
                │  (VLM: understands manuals, symptoms)   │
                └──────────────────┬──────────────────────┘
                                   │ conditioning
                ┌──────────────────▼──────────────────────┐
 Sensors ──────>│        Latent World Model               │
                │  (Dreamer-style RSSM or Transformer)    │──> Machine State
                │  z_t → Dynamics → z_{t+1}               │    + Fault Prob
                └─────────────────────────────────────────┘
                                   │
                ┌──────────────────▼──────────────────────┐
                │      ManualsGraph (symptom→cause→fix)   │
                └─────────────────────────────────────────┘
```

### Key Papers
- **DreamerV3** (2023) - Unified world model architecture, symlog predictions
- **RT-2** (CoRL 2023) - VLM to robot actions, web knowledge transfer
- **RT-X / Open X-Embodiment** (CoRL 2023) - Cross-embodiment transfer works
- **UniSim** (2023) - Video prediction as world simulation
- **TD-MPC2** (2024) - Scalable world models for continuous control

### Your Novelty
No one has built an industrial world model combining:
- Factory-specific sensors (vibration, current, PLCs)
- Semantic priors from manuals (ManualsGraph)
- Hardware-in-the-loop validation (FactoryCell)
- Open benchmark (FactoryBench)

**Position: "Open X-Embodiment for industrial machines"**

---

## 4. Semantic Priors from Manuals/Documentation

### What Manuals Provide

| Information Type | Use for State Prediction |
|-----------------|-------------------------|
| Kinematic parameters | Prior for forward kinematics |
| Dynamic parameters | Prior for dynamics model |
| Joint limits | State validity constraints |
| Error codes | Discrete state classification |
| Operating procedures | Expected state sequences |
| Safety interlocks | Transition constraints |

### Integration Methods

1. **Dynamics Model Priors**: Manual provides mass, inertia → prior mean for Bayesian learning
2. **State Space Structuring**: Named states (IDLE, MOVING, ERROR) → discrete latent states
3. **Transition Constraints**: Safety interlocks → hard constraints on learned transitions
4. **Anomaly Detection**: Error codes, fault symptoms → prior for anomaly detection

### Pipeline for Using Manuals
```
Phase 1: Knowledge Extraction (ManualsGraph)
├── Parse PDFs (ABB, UR, Kuka manuals)
├── Extract specs, procedures, errors
├── Build knowledge graph
└── Generate constraint specifications

Phase 2: Prior Construction
├── Kinematic/dynamic parameters → Physics prior
├── State descriptions → State space definition
├── Procedures → Transition prior
└── Error codes → Anomaly classifier

Phase 3: Model Integration
├── Initialize dynamics with manual parameters
├── Constrain state space with manual states
├── Regularize transitions with procedural knowledge
└── Validate predictions against specifications
```

### Key Papers
- **RT-2** (2023) - Language models encode physical commonsense
- **SayCan** (2022) - Ground LLM planning in robot affordances
- **Code as Policies** (2022) - LLMs generate control code
- **Language to Rewards** (2023) - Specifications → reward functions

---

## 5. Cross-Robot / Cross-Machine Generalization

### Key Insight
**Task-centric representations** (what to achieve) generalize better than **embodiment-centric** (how robot moves).

### Hierarchy of Transferable Representations

| Level | Example | Transfers To |
|-------|---------|--------------|
| Task semantics | "Pick up red cube" | Any manipulator |
| End-effector space | (x, y, z, rpy) | Similar workspaces |
| Joint-normalized | Normalized positions | Similar kinematics |
| Raw proprioception | Joint angles | Same robot only |

### For Non-Robot Machines (Conveyors, Labelling)

**Challenge:** Different control interfaces, state spaces, failure modes.

**Solutions:**
1. **Functional state abstraction**: Map all machines to (current_operation, progress, health_indicators)
2. **Skill-based abstraction**: Define by operations, not kinematics
3. **Graph-based factory representation**: Machines as nodes with standardized interfaces

### Key Papers
- **Open X-Embodiment** (CoRL 2023) - Multi-robot training yields positive transfer
- **MetaMorph** (ICLR 2022) - Transformers for variable morphologies
- **XIRL** (CoRL 2022) - Cross-embodiment reward learning

---

## 6. Industrial/Manufacturing ML

### Existing Benchmarks

| Dataset | Domain | Modalities |
|---------|--------|------------|
| NASA C-MAPSS | Turbofan engines | 21 sensors |
| CWRU Bearings | Bearing faults | Vibration |
| PHM 2010 | Tool wear | Force, vibration, AE |
| MAFAULDA | Rotating machinery | Vibration, current |

### Critical Gaps (Your Opportunity)

1. **No multi-machine cell benchmarks** → FactoryBench
2. **No troubleshooting graphs** → ManualsGraph
3. **No hardware-in-the-loop at scale** → FactoryCell
4. **No fault datasets with fix instructions** → FactoryNet
5. **No generative factory models** → FactoryGraph

### Manufacturing-Specific Challenges
- **Noise/drift**: Environmental variations cause distribution shift
- **Rare faults**: May occur once/year; class imbalance
- **Multi-domain**: Each machine has unique dynamics
- **Real-time**: <10ms latency for control loops
- **Interpretability**: Engineers need explainable decisions

---

## 7. Physical Reasoning & QA Benchmarks (Philipp's Insight)

### Key Insight
**Q&A evaluation tests genuine understanding better than image generation.**

### Question Taxonomy for Industrial QA

| Category | Example | Tests |
|----------|---------|-------|
| **State Recognition** | "What position is valve V3 in?" | Perception |
| **Causal (Forward)** | "If pressure exceeds 10 bar, what happens?" | Physical causation |
| **Causal (Backward)** | "What caused the conveyor jam?" | Fault diagnosis |
| **Counterfactual** | "If sensor S2 hadn't triggered, would E-stop activate?" | Causal models |
| **Predictive** | "Will the part clear the obstacle next cycle?" | Dynamics |
| **Procedural** | "What's the correct restart order after E-stop?" | Process knowledge |
| **Diagnostic** | "Is this sensor reading physically possible?" | Anomaly detection |

### Anti-Shortcut Measures (Critical)
1. **Compositional splits**: Test on novel component + fault combinations
2. **Counterfactual probing**: Same scene, opposite answers required
3. **Contrastive pairs**: Minimally different scenes, different answers
4. **Reasoning chain requirements**: Model must explain, not just answer
5. **Adversarial filtering**: Remove questions solvable by shortcuts

### Key Benchmarks to Study
- **CLEVRER** (ICLR 2020) - 4-way taxonomy: descriptive, explanatory, predictive, counterfactual
- **PHYRE** (NeurIPS 2019) - Action-conditioned physical reasoning
- **IntPhys** (ICLR 2019) - Violation of expectation paradigm
- **CoPhy** (2020) - Counterfactual physical reasoning

### Proposed Evaluation Format
```
Input:
{
  "manual": "Technical documentation",
  "cad": "3D CAD model",
  "state": {sensors, cameras, actuators, alarms, history},
  "question": "Natural language question"
}

Output:
{
  "answer": "Response",
  "reasoning": "Step-by-step explanation",
  "grounding": {manual_refs, cad_regions, sensor_sources}
}
```

---

## 8. Synthesis: Proposed Architecture for FactoryNet

```
┌─────────────────────────────────────────────────────────────────┐
│                    SEMANTIC FOUNDATION LAYER                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│  │  Manuals    │  │    CAD/     │  │   Error Code            │ │
│  │  (parsed)   │  │   URDF      │  │   Database              │ │
│  └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘ │
│         └────────────────┼─────────────────────┘               │
│                          ▼                                      │
│              ┌───────────────────────┐                         │
│              │   ManualsGraph KG     │                         │
│              │ (symptom→cause→fix)   │                         │
│              └───────────┬───────────┘                         │
└──────────────────────────┼──────────────────────────────────────┘
                           │ semantic conditioning
┌──────────────────────────▼──────────────────────────────────────┐
│                    PERCEPTION LAYER                              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │Vibration│ │ Current │ │ Vision  │ │ F/T     │ │ Encoders│   │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘   │
│       └───────────┴───────────┼───────────┴───────────┘         │
│                               ▼                                  │
│              ┌────────────────────────────┐                     │
│              │   Attention-Based Fusion   │                     │
│              └────────────┬───────────────┘                     │
└───────────────────────────┼─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    STRUCTURAL LAYER                              │
│              ┌────────────────────────────┐                     │
│              │   Per-Robot GNN Encoder    │                     │
│              │   (URDF → kinematic graph) │                     │
│              └────────────┬───────────────┘                     │
│                           ▼                                      │
│              ┌────────────────────────────┐                     │
│              │  Multi-Robot Attention     │                     │
│              │  (cross-machine relations) │                     │
│              └────────────┬───────────────┘                     │
└───────────────────────────┼─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    WORLD MODEL LAYER                             │
│              ┌────────────────────────────┐                     │
│              │  Latent Dynamics Model     │                     │
│              │  (Dreamer-style RSSM)      │                     │
│              │  z_t → p(z_{t+1}|a_t)     │                     │
│              └────────────┬───────────────┘                     │
└───────────────────────────┼─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│                    OUTPUT LAYER                                  │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐ │
│  │  State Pred     │  │  Fault Prob     │  │  Q&A Module     │ │
│  │  (joint angles, │  │  (anomaly       │  │  (answer        │ │
│  │   poses, etc.)  │  │   detection)    │  │   questions)    │ │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Research Hypotheses

1. **H1:** Semantic priors (URDF + manuals) reduce sample complexity by >50% compared to sensor-only learning.

2. **H2:** Multi-cobot training (ABB, UR, Kuka) enables positive transfer to unseen robots.

3. **H3:** State prediction as intermediate representation improves fault diagnosis vs direct classification.

4. **H4:** Learned representations transfer to non-robot machines (labelling, conveyors) with <100 samples.

5. **H5:** Q&A evaluation correlates better with downstream task performance than image generation metrics.

6. **H6:** Counterfactual questions are the best discriminator between genuine understanding and pattern matching.

---

## 10. Recommended Reading List (Priority Order)

### Must-Read (Week 1-2)
1. **DreamerV3** - Core world model architecture
2. **RT-X / Open X-Embodiment** - Cross-embodiment transfer
3. **MetaMorph** - Transformers for variable morphologies
4. **CLEVRER** - Question taxonomy for physical reasoning

### Deep Dive (Week 3-4)
5. **Neural Descriptor Fields** - SE(3)-equivariant representations
6. **TD-MPC2** - Scalable world models for control
7. **Language to Rewards** - Specifications → rewards
8. **Kim et al.** - Multi-sensor fusion survey

### Industrial Context (Week 5-6)
9. **Tao et al.** - Digital twin foundations
10. **Lei et al.** - Machinery prognostics taxonomy
11. **NASA C-MAPSS** documentation - Baseline benchmark

### Advanced (Week 7+)
12. **CoPhy** - Counterfactual physical reasoning
13. **SayCan** - Grounded LLM planning
14. **Physics-Informed Neural Networks** for state estimation

---

## 11. Next Steps for Karim

### Immediate (This Week)
- [ ] Read DreamerV3 and CLEVRER papers
- [ ] Inventory sensor modalities on all 4 cobots
- [ ] Collect sample manuals for ABB IRB 2600, YUMI, UR3, Kuka KR10

### Short-term (Month 1)
- [ ] Implement URDF parser → GNN encoder prototype
- [ ] Design question taxonomy for cobot state reasoning
- [ ] Create small pilot dataset (1 robot, manual sensor readings, 50 questions)

### Medium-term (Month 2-3)
- [ ] Train baseline state predictor (sensor-only)
- [ ] Add semantic conditioning from manual parameters
- [ ] Compare sample complexity with/without priors

### Thesis Deliverables
- [ ] FactoryNet dataset: Multi-robot state + fault data
- [ ] Q&A benchmark: Question set with taxonomy
- [ ] Model: State predictor with semantic priors
- [ ] Paper: Submit to CoRL or ICRA by deadline

---

## 12. Publication Strategy

| Venue | Deadline | Focus | Fit |
|-------|----------|-------|-----|
| **CoRL 2026** | ~June | Robot learning | High - world models, cross-robot |
| **ICRA 2027** | ~Sep 2026 | Robotics | High - state estimation, industrial |
| **NeurIPS 2026** | ~May | ML | Medium - needs strong ML contribution |
| **IEEE TII** | Rolling | Industrial | High - practical industrial focus |

**Recommended:** Target CoRL 2026 with state prediction + Q&A evaluation; extend to ICRA 2027 with generalization results.

---

*This literature review synthesizes findings from 7 parallel research agents covering: robot state estimation, URDF/CAD priors, world models, semantic priors from documentation, cross-robot generalization, industrial ML, and physical reasoning benchmarks.*
