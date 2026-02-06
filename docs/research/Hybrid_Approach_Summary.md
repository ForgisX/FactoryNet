# FactoryNet Hybrid Approach - Executive Summary (Revised)

## The Merged Vision

**Paper Title**: FactoryNet: Causally-Structured Data and Evaluation for Transferable Industrial Machine Understanding

**One-Sentence Pitch**: We introduce a data schema that separates machine commands (Intent) from responses (Outcome), enabling physics-based fault detection that transfers across machines without labeled training data.

---

## What NeurIPS D&B Reviewers Will Ask

| Question | Our Answer |
|----------|------------|
| **Scale?** | 500+ UR3e + 320 Paderborn + extensible to CWRU/MAFAULDA |
| **Diversity?** | 2 machine types (robot + bearing rig), 4 trajectory types |
| **Transfer?** | Cross-domain: UR3e → Paderborn fault detection |
| **Novelty?** | ICO structure enables transfer without target labels |

**Hysteresis** answers none of these well. It's been demoted to a 1-paragraph case study.

---

## The Hero Result

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│   "A physics model trained ONLY on healthy UR3e robot data     │
│    detects bearing faults in Paderborn test rig data           │
│    WITHOUT any Paderborn-specific training."                   │
│                                                                 │
│   This proves:                                                  │
│   1. ICO structure captures transferable physics                │
│   2. Cross-machine generalization is possible                   │
│   3. Fault detection works without fault labels                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

Even a modest improvement over baseline is publishable. We need the experiment run.

---

## What We're Merging

| Element | From Karim | From Jonas | Hybrid |
|---------|------------|------------|--------|
| **Core Schema** | Intent/Context/Outcome | Episode with taxonomy | ICO + Taxonomy |
| **Data: Real** | 500+ UR3e episodes | - | Karim collects |
| **Data: Adapted** | - | 320 Paderborn, 8 adapters | Jonas provides |
| **Evaluation** | Residual-based detection | Q&A framework | Both levels |
| **Key Experiment** | ~~Hysteresis~~ → **Transfer** | Cross-dataset transfer | UR3e → Paderborn |

---

## Current Status

### Already Complete (Jonas/Pipeline)
```
✅ 8 dataset adapters working
   - CWRU, Paderborn, MAFAULDA, XJTU-SY
   - PHM 2010, PHM 2021 SCARA, UR3e Pick-Place, AURSAD

✅ 320 real Paderborn episodes processed
   - 6 sensor channels
   - 18 features extracted per channel
   - 12 Q&A pairs per episode (3,840 total)
   - 100% validation pass rate

✅ Full pipeline operational
   - Adapter → Normalize → Validate → Features → Q&A → Store
   - Parquet storage, JSON metadata
```

### Needed From Karim (2-Week Sprint)

**Priority 1: SCALE**
```
🔲 500+ UR3e episodes with ICO structure
   - Week 1: 400+ episodes (3 trajectory types × 3 speeds × 3 loads)
   - Intent: target_q, target_qd from RTDE
   - Outcome: actual_q, actual_qd, actual_current
   - Context: load_state, speed_state
```

**Priority 2: TRANSFER EXPERIMENT**
```
🔲 Cross-domain transfer: UR3e → Paderborn
   - Train physics model on UR3e healthy data
   - Test on Paderborn faulty data
   - Report: Does ICO structure enable fault detection?
```

**Priority 3: Integration**
```
🔲 UR3e adapter integrated with pipeline
   - Map RTDE fields to unified schema
   - Run through Jonas's pipeline
```

**Deprioritized**
```
⬜ Hysteresis: 1-paragraph case study only (if time permits)
⬜ ABB data: Stretch goal (if available)
```

---

## Revised Sprint Plan Overview

### Week 1: Data Collection at SCALE

| Day | Focus | Deliverable |
|-----|-------|-------------|
| 1-2 | Setup + collection script | Working automation |
| 3 | Pick-and-place runs | 135 episodes |
| 4 | Circular motion runs | 135 episodes (270 total) |
| 5 | Linear sweeps + random | 140 episodes (410 total) |

**Week 1 Output**: 400+ UR3e episodes, diverse conditions

### Week 2: Transfer Experiments

| Day | Focus | Deliverable |
|-----|-------|-------------|
| 6-7 | Adapter integration | Data in unified format |
| 8 | Train physics model | UR3e baseline MAE |
| 9 | **HERO EXPERIMENT** | UR3e → Paderborn transfer |
| 10 | Final experiments + figures | Results table |

**Week 2 Output**: Cross-domain transfer result, all figures

---

## Paper Structure (Revised)

| Section | Owner | Status |
|---------|-------|--------|
| 1. Introduction | Shared | Draft exists |
| 2. Related Work | Karim | Draft exists |
| 3.1-3.2 ICO Schema | **Karim** | Needs writing |
| 3.3 Taxonomy | **Jonas** | Draft exists |
| 4.1 Real Robot Data (UR3e) | **Karim** | After collection |
| 4.2 Adapted Datasets | **Jonas** | Can write now |
| 5.1 Residual Evaluation | **Karim** | After experiments |
| 5.2 Q&A Evaluation | **Jonas** | Draft exists |
| 6.1 Transfer Results | **Karim** | After experiments |
| 6.2 Q&A Baselines | **Jonas** | After Karim's data |
| 7. Discussion | Shared | End |

**Removed**: Dedicated hysteresis section. Mention in 1 paragraph under 6.1.

---

## Key Figures for Paper

### Figure 1: ICO Schema + Transfer Concept
```
              UR3e Robot                    Paderborn Bearing
         ┌───────────────────┐          ┌───────────────────┐
         │ Intent: target_q  │          │ Intent: motor_rpm │
         │ Context: load     │──────────│ Context: force    │
         │ Outcome: actual_q │          │ Outcome: vibration│
         └───────────────────┘          └───────────────────┘
                   │                              │
                   ▼                              ▼
            ┌─────────────┐                ┌─────────────┐
            │ Physics     │───TRANSFER───▶│ Apply model │
            │ Model       │                │ (no retrain)│
            └─────────────┘                └─────────────┘
```
**Owner**: Shared

### Figure 2: Transfer Results (THE KEY FIGURE)
| Train → Test | Residual MAE | Fault F1 |
|--------------|--------------|----------|
| UR3e → UR3e (held-out) | X.XX | - |
| UR3e → Paderborn healthy | X.XX | - |
| UR3e → Paderborn faulty | X.XX | X.XX |

**Owner**: Karim (experiments)

### Figure 3: Q&A Results
Accuracy by question type for different models.
**Owner**: Jonas (after integration)

---

## Minimum Viable Paper

**Must Have**:
- [ ] ICO schema specification - can write now
- [ ] 500+ UR3e episodes - Karim Week 1
- [ ] Transfer experiment result - Karim Week 2
- [ ] Paderborn adapted data description - done

**Nice to Have**:
- [ ] ABB data for cross-robot transfer
- [ ] Full Q&A baselines
- [ ] Hysteresis case study figure

**Cut**:
- [ ] Deep hysteresis analysis
- [ ] Synthetic data
- [ ] Semantic priors

---

## Risks (Updated)

| Risk | Mitigation |
|------|------------|
| Robot unavailable | Day 1-2 catches early; can pivot to adapted-only paper |
| Transfer doesn't work | Report honestly; ICO schema still valuable contribution |
| Not enough scale | 400 UR3e + 320 Paderborn = 720 episodes minimum |
| Behind schedule | Cut linear sweeps (Day 5); prioritize transfer experiment |

---

## Decision Points for Meeting

### 1. Confirm Revised Priorities
**Agree that**:
- Scale > Hysteresis
- Transfer experiment = Hero result
- Hysteresis = 1-paragraph case study only

### 2. Data Scale Commitment
**Proposal**: 500+ UR3e + 320 Paderborn + optional CWRU/MAFAULDA
- Conservative but achievable
- Can add more adapted datasets easily

### 3. ABB Access
**Question**: Can Karim collect ABB data?
- If yes: Add to stretch goals
- If no: Paper works with UR3e + Paderborn only

### 4. Timeline
- Karim's sprint: 2 weeks
- Paper writing: 2 weeks after
- Target: NeurIPS D&B 2026

---

## Action Items

### Before Sprint Starts
- [ ] Karim: Confirm robot access
- [ ] Jonas: Share Paderborn data in Parquet format
- [ ] Both: Agree on exact ICO field mappings
- [ ] Both: Set up shared data folder

### Karim's Sprint
- [ ] Week 1: Collect 400+ diverse episodes
- [ ] Week 2: Run transfer experiment, create figures
- [ ] Daily: Async updates with episode count

### Jonas Parallel Work
- [ ] Write Section 4.2 (Adapted Datasets)
- [ ] Prepare Paderborn data for transfer experiment
- [ ] Set up Q&A baseline infrastructure

---

## Files

1. `docs/research/FactoryNet_Hybrid_Paper_Outline.md` - Paper structure
2. `docs/research/Karim_2_Week_Sprint_Plan.md` - Detailed sprint (REVISED)
3. `docs/research/Hybrid_Approach_Summary.md` - This document (REVISED)
