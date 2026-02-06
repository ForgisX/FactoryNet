# Karim's 2-Week Sprint Plan (Revised)

## Objective
Collect robot data at SCALE and run TRANSFER experiments that prove the ICO schema enables cross-machine generalization.

**Primary Goal**: Demonstrate that a physics model trained on UR3e healthy data can detect anomalies in Paderborn bearing data WITHOUT any Paderborn-specific training.

---

## What We Already Have (Jonas/Pipeline)
- 8 working dataset adapters (CWRU, Paderborn, MAFAULDA, XJTU-SY, PHM2010, PHM2021, UR3e, AURSAD)
- 320 real Paderborn episodes processed through full pipeline
- Feature extraction (RMS, kurtosis, spectral, bearing frequencies)
- Q&A generation templates
- Parquet storage with unified schema
- Validation framework (100% pass rate on Paderborn)

## What We Need From Karim (Priority Order)
1. **500+ UR3e episodes** with ICO structure (SCALE)
2. **Cross-domain transfer experiment**: UR3e → Paderborn (HERO RESULT)
3. **UR3e RTDE adapter** integrated with pipeline
4. _(Stretch)_ ABB data for cross-robot transfer

**Explicitly Deprioritized**: Hysteresis deep-dive. Include as 1-paragraph case study only.

---

## Week 1: Data Collection at Scale

### Day 1-2: Setup & Collection Infrastructure

**Day 1 (Monday)**
- [ ] Review hybrid paper outline and this sprint plan
- [ ] Finalize ICO schema fields for UR3e RTDE:
  ```python
  UR3E_ADAPTER = {
      # INTENT - What we commanded
      "intent_position": "target_q",           # rad, 6 joints
      "intent_velocity": "target_qd",          # rad/s
      "intent_acceleration": "target_qdd",     # rad/s²
      "intent_current": "target_current",      # A

      # CONTEXT - Operating conditions
      "context_temperature": "joint_temperatures",  # °C
      "context_voltage": "actual_main_voltage",     # V
      "context_load": "INJECTED_TAG",               # 0/1/2 (empty/light/heavy)
      "context_speed": "INJECTED_TAG",              # 0/1/2 (slow/med/fast)

      # OUTCOME - What actually happened
      "outcome_position": "actual_q",          # rad
      "outcome_velocity": "actual_qd",         # rad/s
      "outcome_current": "actual_current",     # A
  }
  ```
- [ ] Set up data collection environment (RTDE connection, logging)
- [ ] Define 3-4 diverse trajectory types

**Day 2 (Tuesday)**
- [ ] Write UR3e data collection script with RTDE
- [ ] Implement automated context tag injection
- [ ] Test data logging at 500 Hz
- [ ] Verify all ICO fields are captured
- [ ] **Deliverable**: Working automated collection script

### Day 3-5: Mass Data Collection

**Goal: 400+ episodes across diverse conditions**

**Day 3 (Wednesday)** - Trajectory 1: Pick-and-Place
| Speed | Empty (0kg) | Light (1kg) | Heavy (3kg) |
|-------|-------------|-------------|-------------|
| 25%   | 15 runs     | 15 runs     | 15 runs     |
| 50%   | 15 runs     | 15 runs     | 15 runs     |
| 100%  | 15 runs     | 15 runs     | 15 runs     |
- [ ] **Deliverable**: 135 episodes

**Day 4 (Thursday)** - Trajectory 2: Circular Motion
| Speed | Empty | Light | Heavy |
|-------|-------|-------|-------|
| 25%   | 15    | 15    | 15    |
| 50%   | 15    | 15    | 15    |
| 100%  | 15    | 15    | 15    |
- [ ] **Deliverable**: 135 episodes (270 cumulative)

**Day 5 (Friday)** - Trajectory 3: Linear Sweeps + Random
| Type | Conditions | Runs |
|------|------------|------|
| X-axis sweep | All loads × 50% speed | 30 |
| Y-axis sweep | All loads × 50% speed | 30 |
| Z-axis sweep | All loads × 50% speed | 30 |
| Random waypoints | Mixed | 50 |
- [ ] **Deliverable**: 140 episodes (410 cumulative)

**Hysteresis (Low Priority)**: If time permits Friday afternoon, collect 20 direction-reversal episodes for a case study paragraph. This is NOT a primary deliverable.

---

## Week 1 Checkpoint (End of Friday)

**Required Deliverables**:
- [ ] Working UR3e RTDE collection script
- [ ] **400+ UR3e episodes collected** (varied trajectories, loads, speeds)
- [ ] ICO schema validated on real data
- [ ] Data exported as Parquet + metadata JSON

**Data to Share with Jonas**:
- Raw RTDE logs (Parquet format)
- Metadata JSON per run
- Collection script (for reproducibility)

---

## Week 2: Transfer Experiments & Integration

### Day 6-7: Adapter Integration

**Day 6 (Monday)**
- [ ] Integrate UR3e adapter with Jonas's pipeline
- [ ] Convert all collected data to FactoryNet schema
- [ ] Run through validation pipeline
- [ ] Fix any schema mismatches
- [ ] **Deliverable**: 400+ UR3e episodes in unified format

**Day 7 (Tuesday)**
- [ ] Generate features for UR3e data
- [ ] Generate Q&A pairs for UR3e episodes
- [ ] Verify feature extraction works correctly
- [ ] Collect 100 more episodes if needed (reach 500 total)
- [ ] **Deliverable**: UR3e data with features + Q&A

### Day 8-9: Physics Model & THE TRANSFER EXPERIMENT

**Day 8 (Wednesday)** - Train Physics Model on UR3e
- [ ] Implement physics model:
  ```python
  # Model: outcome = f(intent, context)
  # Option 1: Linear baseline
  outcome_pos = A @ intent_pos + B @ context + bias

  # Option 2: MLP
  outcome_pos = MLP(concat(intent, context))
  ```
- [ ] Train on 80% of healthy UR3e data
- [ ] Evaluate on held-out 20% UR3e data
- [ ] Compute baseline MAE for within-domain
- [ ] **Deliverable**: Trained physics model, UR3e MAE baseline

**Day 9 (Thursday)** - THE HERO EXPERIMENT: Cross-Domain Transfer
- [ ] Map UR3e ICO fields to Paderborn ICO fields:
  ```
  UR3e intent_velocity → Paderborn motor_speed (normalized)
  UR3e outcome_position → Paderborn bearing_position (via velocity integral)
  UR3e context_load → Paderborn radial_force (mapped)
  ```
- [ ] Apply UR3e-trained model to Paderborn healthy data
- [ ] Compute residuals on Paderborn faulty data
- [ ] **KEY RESULT**: Do residuals discriminate healthy vs faulty on Paderborn?
- [ ] **Deliverable**: Transfer results table + figure

### Day 10: Final Experiments & Documentation

**Day 10 (Friday)** - Consolidation
- [ ] Run additional transfer experiments:
  | Experiment | Train | Test | Metric |
  |------------|-------|------|--------|
  | Within-UR3e | UR3e healthy | UR3e (held-out) | MAE |
  | Within-Paderborn | Paderborn healthy | Paderborn faulty | Residual |
  | **Cross-domain** | UR3e healthy | Paderborn faulty | Residual + F1 |

- [ ] (If ABB available) Collect 50 ABB episodes, run UR3e → ABB transfer
- [ ] Create all paper figures
- [ ] Document negative results honestly
- [ ] **Deliverable**: Complete experimental results

---

## Week 2 Checkpoint (End of Friday)

**Required Deliverables**:
- [ ] 500+ UR3e episodes in unified format
- [ ] Physics model trained and evaluated
- [ ] **Cross-domain transfer result** (UR3e → Paderborn)
- [ ] All figures for paper
- [ ] Experimental results table

**Stretch Deliverables**:
- [ ] ABB data + cross-robot transfer
- [ ] Hysteresis case study figure

---

## THE HERO RESULT WE NEED

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

Even a modest improvement over random baseline is publishable. We need the experiment run, not perfection.

---

## Data Format Specification

### Directory Structure
```
ur3e_data/
├── pick_place/
│   ├── run_001_empty_slow/
│   │   ├── metadata.json
│   │   └── timeseries.parquet
│   ├── run_002_empty_slow/
│   └── ...
├── circular/
│   └── ...
├── linear_sweep/
│   └── ...
└── random/
    └── ...
```

### metadata.json
```json
{
  "run_id": "run_001",
  "robot": "ur3e",
  "trajectory_type": "pick_place",
  "load_state": 0,
  "load_kg": 0.0,
  "speed_state": 0,
  "speed_percent": 25,
  "duration_sec": 12.5,
  "sample_rate_hz": 500,
  "timestamp_start": "2026-02-10T09:00:00Z"
}
```

---

## Daily Communication

**Daily Standup (async)**:
- What I did yesterday
- What I'm doing today
- Episode count (running total)
- Any blockers

**Mid-week Sync (Wednesday)**:
- 30-min call
- Review episode count
- Adjust if behind

**End-of-week Demo (Friday)**:
- Show data + preliminary results
- Plan next week

---

## Key Success Metrics

### Week 1 Success = SCALE
- [ ] 400+ diverse UR3e episodes
- [ ] Multiple trajectory types
- [ ] Full load/speed coverage
- [ ] Clean Parquet export

### Week 2 Success = TRANSFER
- [ ] Physics model trains successfully
- [ ] Cross-domain experiment runs
- [ ] Results are interpretable (positive or negative)
- [ ] All figures created

### Paper-Ready Success
- [ ] **Figure**: Transfer results (UR3e → Paderborn)
- [ ] **Table**: MAE/F1 across domains
- [ ] **500+ episodes** in unified format
- [ ] Clear story: ICO enables transfer

---

## What We're NOT Doing (Explicit Scope Cuts)

1. **Deep hysteresis analysis** - One paragraph case study max
2. **Perfect physics model** - Simple MLP is fine
3. **Many baseline comparisons** - One transfer experiment is the priority
4. **Synthetic data** - Real data only
5. **Full Q&A evaluation** - Jonas handles this in parallel

---

## Risk Mitigation (Revised)

| Risk | Mitigation |
|------|------------|
| Robot unavailable | Day 1-2 setup catches this early |
| RTDE issues | Lower to 125 Hz if needed |
| Transfer doesn't work | Report honestly; ICO structure still valuable |
| Behind on episodes | Cut trajectory 3 (linear sweeps) |
| ABB not available | Paper works without it |

---

## Files Reference

- Paper outline: `docs/research/FactoryNet_Hybrid_Paper_Outline.md`
- This sprint plan: `docs/research/Karim_2_Week_Sprint_Plan.md`
- Summary: `docs/research/Hybrid_Approach_Summary.md`
- Existing adapters: `core/adapters/` (reference for UR3e adapter)
