# FactoryNet: Hybrid Paper Outline

## Merged Vision

**Title**: FactoryNet: Causally-Structured Data and Evaluation for Transferable Industrial Machine Understanding

**Core Thesis**: The Intent/Context/Outcome (ICO) schema enables physics-based fault detection that transfers across machines, validated through both residual metrics and a Q&A evaluation framework.

**Key Insight**: The schema structure (Karim's contribution) is what makes the evaluation framework (our contribution) meaningful. ICO grounds questions in physics rather than pattern matching.

---

## Paper Structure (8 pages + appendix)

### 1. Introduction (1 page)
- $50B downtime problem (shared)
- Why transfer fails: models learn sensor statistics, not physics
- **Key contribution**: Data structure that encodes causality
  - Intent (command) vs Outcome (response) separation
  - Residual = physics violation = fault (without labels)
- **Secondary contribution**: Evaluation framework grounded in ICO
  - Q&A tests whether models understand the physics relationship
- Contributions list:
  1. ICO Schema with Adapter Pattern
  2. Cross-Robot Dataset (real + adapted)
  3. Two-Level Evaluation (residual + Q&A)
  4. Hysteresis Validation Experiment

### 2. Related Work (1 page)
- Industrial fault datasets (Table 1 from Karim - CWRU, PHM, etc.)
- Robot dynamics datasets (MESSII, Open X-Embodiment)
- Hysteresis modeling (Bouc-Wen, LuGre, neural approaches)
- Physical reasoning benchmarks (CLEVRER, PHYRE)
- World models (DreamerV3, RT-2)
- **Gap**: No dataset with causal structure + cross-machine scope + grounded evaluation

### 3. The FactoryNet Schema (1.5 pages)

#### 3.1 Intent/Context/Outcome Structure (Karim's core)
```
┌─────────────────────────────────────────────────────────────┐
│                    FACTORYNET SCHEMA                        │
├─────────────────────────────────────────────────────────────┤
│  INTENT (Command)     │  CONTEXT (Conditions)  │  OUTCOME   │
│  ─────────────────    │  ────────────────────  │  ───────── │
│  • target_position    │  • load_state          │  • actual_ │
│  • target_velocity    │  • thermal_state       │    position│
│  • target_torque      │  • direction           │  • actual_ │
│  • gripper_command    │  • motor_temperature   │    velocity│
│                       │  • wear_state          │  • current │
│                       │                        │  • force   │
├─────────────────────────────────────────────────────────────┤
│  FAULT DETECTION: residual(t) = outcome(t) - f(intent, ctx) │
│  • Healthy: residual ≈ 0                                    │
│  • Fault: residual shows systematic pattern                 │
└─────────────────────────────────────────────────────────────┘
```

#### 3.2 Adapter Pattern (Karim's contribution)
- Maps robot-specific signals → universal schema columns
- Enables cross-robot research without schema redesign
- Example: UR3e RTDE vs ABB EGM mappings

#### 3.3 Hierarchical Taxonomy (Our contribution)
- 5 dimensions: Machine, State, Symptom, Cause, Action
- Synset IDs for hierarchical evaluation
- Enables "partial credit" for close-but-wrong predictions

#### 3.4 Episode Schema (Merged)
```python
FactoryNetEpisode = {
    # ICO Structure (Karim)
    "intent": {...},      # Commands at each timestep
    "context": {...},     # Conditions (load, temp, direction)
    "outcome": {...},     # Actual responses

    # Taxonomy Labels (Ours)
    "machine_synset": "M.rob.col.ur.ur3e",
    "state_synset": "S.nom.run",

    # Evaluation Annotations (Merged)
    "residual_labels": {...},  # For residual-based eval
    "qa_pairs": [...],         # For Q&A eval
}
```

### 4. Dataset Construction (1.5 pages)

#### 4.1 Real Robot Data (Karim's collection)
| Platform | Episodes | Signals | Collection Protocol |
|----------|----------|---------|---------------------|
| UR3e | 200+ | RTDE @ 500Hz | Hysteresis + load + thermal |
| ABB IRB 2600 | 100+ | EGM @ 250Hz | Same protocol |

**Systematic Context Variation**:
- Load: Empty / Light / Heavy
- Thermal: Cold start / Warm
- Direction: Forward / Backward (for hysteresis)

#### 4.2 Adapted Open Datasets (Our pipeline)
| Source | Episodes | Signals | Adaptation |
|--------|----------|---------|------------|
| Paderborn | 320 | Force, current, vibration | ICO mapping + taxonomy |
| CWRU | 500+ | Vibration | ICO mapping + taxonomy |
| MAFAULDA | 500+ | Vibration, audio | ICO mapping + taxonomy |
| XJTU-SY | 500+ | Vibration | ICO mapping + taxonomy |
| PHM 2010 | 300+ | Force, vibration, AE | ICO mapping + taxonomy |

**Total: 2,500+ episodes** (scalable to 10,000+)

#### 4.3 Data Format
- Parquet for timeseries (efficient columnar storage)
- JSON for metadata and Q&A
- Standardized directory structure per episode

### 5. Evaluation Framework (1 page)

#### 5.1 Level 1: Residual-Based Metrics (Karim's approach)
**Physics Model Fit**:
- Train: outcome = f(intent, context) on healthy data
- Metric: MAE of prediction on held-out healthy data

**Fault Detection**:
- Compute residual on test data
- Detect faults as residual anomalies
- Metrics: Precision, Recall, F1 for fault detection

**Transfer Metrics**:
- Train on Robot A, test on Robot B
- Residual correlation with ground-truth faults

#### 5.2 Level 2: Q&A Evaluation (Our approach)
**Question Types** (grounded in ICO):
| Type | Example | ICO Grounding |
|------|---------|---------------|
| State | "What is joint 3 position?" | Direct Outcome query |
| Prediction | "If load increases, will current exceed 2A?" | f(Intent, Context) |
| Causal | "What caused the position lag?" | Residual interpretation |
| Counterfactual | "If direction were reversed, would error persist?" | Context variation |

**Metrics**:
- Accuracy per question type
- Safety-Weighted Accuracy (SWA)
- FactoryNet Score (FNS) - weighted average

#### 5.3 Relationship Between Levels
```
Level 1 (Residual) → "Can the model learn physics?"
Level 2 (Q&A)      → "Can the model explain physics?"

A model that passes Level 1 but fails Level 2 learns correlations.
A model that passes both genuinely understands.
```

### 6. Experiments (1.5 pages)

#### 6.1 Experiment 1: Hysteresis Visibility (Karim's validation)
**Setup**: Direction-reversal trajectory on UR3e and ABB
**Result**: Hysteresis loop visible in ICO structure, invisible without Intent

```
[Figure: Hysteresis loops - cold vs warm, UR3e vs ABB]
```

#### 6.2 Experiment 2: Cross-Robot Transfer
**Setup**: Train physics model on UR3e, test on ABB (and vice versa)
**Baselines**:
- Raw transfer (no adaptation)
- Context-conditioned (robot_type as feature)
- Per-robot (upper bound)

**Metrics**: Residual MAE, fault detection F1

#### 6.3 Experiment 3: Adapted Dataset Transfer
**Setup**: Train on Paderborn bearings, test on CWRU/MAFAULDA
**Question**: Does ICO structure help transfer across bearing datasets?

#### 6.4 Experiment 4: Q&A Baselines
**Models**:
- Classical: SVM + features (multiple choice)
- Deep: Transformer encoder
- LLM: GPT-4 + RAG, fine-tuned LLaMA

**Results Table**: Accuracy by question type

### 7. Discussion (0.5 pages)
- ICO as foundation for industrial world models
- Limitation: 2 robot types (future: more diversity)
- Limitation: Adapted datasets have simpler ICO (no Intent)
- Future: Semantic priors (manuals, URDF)

### 8. Conclusion (0.25 pages)
- ICO schema enables physics-based transfer
- Two-level evaluation tests both learning and understanding
- Released: dataset, adapters, evaluation toolkit

---

## Appendices

### A. Full Schema Specification
- Complete ICO field definitions
- Adapter implementations for UR3e, ABB, Paderborn

### B. Taxonomy (Condensed)
- Machine, State, Symptom hierarchies
- Synset encoding scheme

### C. Q&A Templates
- Templates for each question type
- Grounding in ICO fields

### D. Baseline Details
- Hyperparameters, training procedures

---

## What Each Person Contributes

| Section | Karim | Jonas/Pipeline | Shared |
|---------|-------|----------------|--------|
| 1. Introduction | Core thesis | Q&A motivation | Write together |
| 3.1-3.2 Schema ICO | **Primary** | Review | |
| 3.3 Taxonomy | | **Primary** | |
| 4.1 Real Robot Data | **Primary** | | |
| 4.2 Adapted Datasets | | **Primary** | |
| 5.1 Residual Eval | **Primary** | | |
| 5.2 Q&A Eval | | **Primary** | |
| 6.1 Hysteresis | **Primary** | | |
| 6.2 Cross-Robot | **Primary** | Support | |
| 6.3 Adapted Transfer | | **Primary** | |
| 6.4 Q&A Baselines | | **Primary** | |

---

## Minimum Viable Paper (MVP)

If time is tight, we can ship with:
- ✅ ICO schema specification
- ✅ 320 Paderborn episodes (already done)
- ✅ UR3e hysteresis data (Karim's 2 weeks)
- ✅ Residual-based transfer experiment
- ⚪ Simplified Q&A (1-2 question types only)

This is still a strong NeurIPS D&B submission.
