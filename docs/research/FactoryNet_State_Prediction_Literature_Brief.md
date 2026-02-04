# FactoryNet State Prediction - Literature Research Brief

*Created: 2026-02-02*

## Research Vision

**Core Idea:** Learn to predict the physical state (3D model / CAD / URDF / STL / image) of a machine from sensor data combined with semantic priors (manuals, CAD, URDF).

**Why This Matters:** This moves FactoryNet closer to the "World Model" vision - understanding and predicting the physical state of machines, not just classifying faults.

---

## Hardware Testbed

### Cobots (Primary Focus)
| Robot | Type | Key Specs |
|-------|------|-----------|
| ABB IRB 2600 | Industrial 6-axis | 20kg payload, 1.65m reach |
| ABB YUMI | Dual-arm collaborative | Precision assembly |
| Universal Robots UR3 | Collaborative 6-axis | 3kg payload, 500mm reach |
| Kuka KR10 | Industrial 6-axis | 10kg payload |

### Other Equipment (Generalization Targets)
- 2x Labelling machines (Herma, SPR)
- Conveyor belt

---

## Literature Research Topics

### 1. Robot State Estimation from Sensors

**Key Questions:**
- How do existing methods estimate robot joint states from proprioceptive sensors?
- What external sensing modalities (vision, force/torque) improve state estimation?
- How is sensor fusion done for redundant state estimation?

**Search Terms:**
- Robot state estimation
- Proprioceptive sensing robotics
- Joint angle estimation from sensors
- Sensor fusion robot manipulation

**Key Venues:** ICRA, IROS, CoRL, RSS, RA-L

---

### 2. URDF/CAD as Structural Priors for Learning

**Key Questions:**
- How have URDF models been used as priors in robot learning?
- Can CAD/mesh representations be embedded for learning?
- Differentiable simulation with URDF (MuJoCo, Isaac Gym, etc.)

**Search Terms:**
- URDF robot learning
- CAD-informed machine learning
- Differentiable robot simulation
- Structure-aware robot representations
- Mesh neural networks robotics

**Key Papers to Find:**
- Neural mesh representations
- Differentiable physics simulators
- Graph neural networks on robot kinematics

---

### 3. Foundation Models for Robotics / World Models

**Key Questions:**
- What are the current approaches to "world models" for robotics?
- How do video prediction models (Sora, Genie, etc.) relate to physical state prediction?
- Can language-grounded world models transfer across robot embodiments?

**Search Terms:**
- World models robotics
- Video prediction robot manipulation
- Foundation models robotics
- Embodiment-agnostic robot learning
- Cross-robot transfer learning

**Key Works:**
- Dreamer / DreamerV3 (Hafner et al.)
- RT-2, RT-X (Google DeepMind)
- UniSim / GAIA-1 (world simulation)
- RoboCat / Gato (generalist agents)

---

### 4. Semantic Priors from Manuals/Documentation

**Key Questions:**
- How have textual specifications been used to guide robot learning?
- Can LLMs provide useful priors for physical system modeling?
- Grounding language in robot state spaces

**Search Terms:**
- Language-conditioned robot learning
- Specification-guided learning
- LLM robot planning
- Technical documentation machine learning
- Language grounding robotics

---

### 5. Generalization Across Machine Families

**Key Questions:**
- How to achieve zero-shot or few-shot transfer between different robot morphologies?
- What representations enable cross-embodiment generalization?
- Domain adaptation in industrial robotics

**Search Terms:**
- Cross-embodiment transfer learning
- Zero-shot robot transfer
- Morphology-agnostic robot learning
- Domain adaptation industrial robots
- Universal robot representations

---

### 6. Industrial / Manufacturing Specific

**Key Questions:**
- Digital twin state estimation methods in manufacturing
- Existing benchmarks for industrial robot state estimation
- Industrial sensor fusion architectures

**Search Terms:**
- Digital twin state estimation
- Industry 4.0 machine learning
- Manufacturing robot perception
- Industrial IoT state prediction
- Predictive maintenance state estimation

---

### 7. Physical Reasoning & QA Benchmarks (NEW)

**Key Questions:**
- How are physical reasoning capabilities evaluated in AI?
- What question types test genuine physical understanding vs. pattern matching?
- How to generate diverse, high-quality questions automatically?

**Search Terms:**
- Physical reasoning benchmark
- PHYRE benchmark
- IntPhys intuitive physics
- Embodied question answering (EQA)
- Visual question answering physical
- Counterfactual reasoning robotics
- Action-conditioned prediction benchmark

**Key Benchmarks to Study:**
- **PHYRE** - Physical reasoning puzzles
- **IntPhys** - Intuitive physics benchmark
- **CLEVRER** - Compositional language and reasoning on video
- **EQA** - Embodied Question Answering
- **RoboVQA** - Robot manipulation VQA (if exists)
- **BabyAI** - Instruction following grid world

**Question Taxonomy to Develop:**
1. **State queries:** "What is the current position of joint 3?"
2. **Prediction:** "If command X, what will state Y be?"
3. **Counterfactual:** "What would have happened if I had done Z instead?"
4. **Causal:** "Why did the error occur?"
5. **Intervention:** "What action fixes problem P?"
6. **Constraint:** "Is action A safe given current state?"

---

## Potential Publication Venues

| Venue | Type | Deadline (typical) | Notes |
|-------|------|-------------------|-------|
| **NeurIPS** | ML Conference | May | World models, representation learning |
| **ICLR** | ML Conference | Oct | Foundation models |
| **ICRA** | Robotics Conference | Sep | Robot state estimation, manipulation |
| **RSS** | Robotics Conference | Feb | High-impact robotics |
| **CoRL** | Robot Learning | Jun | Learning for robotics |
| **RA-L** | Robotics Journal | Rolling | Technical contributions |

---

## Research Hypotheses to Validate

1. **Hypothesis 1:** Semantic priors (URDF + manuals) significantly reduce sample complexity for state prediction compared to learning from sensor data alone.

2. **Hypothesis 2:** A model trained on multiple cobots (ABB, UR, Kuka) generalizes better to unseen robots than single-robot training.

3. **Hypothesis 3:** State prediction enables better fault diagnosis than direct fault classification (intermediate representation helps).

4. **Hypothesis 4:** The learned state representation transfers to non-robot machines (labelling machines, conveyors) with minimal fine-tuning.

5. **Hypothesis 5 (NEW - Q&A):** A Q&A evaluation framework more accurately measures world model understanding than image generation quality metrics.

6. **Hypothesis 6 (NEW - Q&A):** Question diversity (state/prediction/causal/intervention) correlates with downstream task performance better than single question types.

---

## Next Steps

1. [ ] Deep dive into world models literature (Dreamer, video prediction)
2. [ ] Survey URDF/CAD-informed learning methods
3. [ ] Identify benchmark datasets for robot state estimation
4. [ ] Map out available sensor modalities for our 4 cobots
5. [ ] Design initial experimental protocol
6. [ ] **Survey physical reasoning benchmarks (PHYRE, IntPhys, CLEVRER, EQA)**
7. [ ] **Develop question taxonomy for industrial world models**
8. [ ] **Investigate automatic question generation from manuals/URDF**

---

## Notes from Initial Discussion

- Karim introduced fault taxonomy: time, space, dynamic vs dropout, bias, variance
- Big pivot: from fault classification to **state prediction** (more aligned with world models)
- Start narrow (4 cobots) → demonstrate within-family generalization → extend beyond (labelling, conveyors)
- Semantic priors are key differentiator from pure sensor-based approaches

---

## Key Insight: Q&A Instead of Image Generation (Philipp, 2026-02-03)

**Problem with image generation approach:**
- Generating images of predicted states is a "detour"
- Image quality evaluation via checklist is indirect and noisy
- Computationally expensive, harder to scale

**Proposed alternative: Question-Answering Benchmark**

| Input | Output |
|-------|--------|
| Manual + CAD model + current state + list_of_questions | Answers to questions |

**Example questions (commands embedded in questions):**
- "If I press the red button for 5 seconds, how high is the arm?"
- "What must I do to turn off the red warning light?"
- "How far does the arm rotate if I send the following command to the API: `move_joint(2, 45)`?"
- "After executing program X, which sensors will show values above threshold Y?"
- "Given the current error code, what is the most likely root cause?"

**Why this is better:**
1. **Direct evaluation** - answers are easier to score than images
2. **More practical** - operators ask questions, they don't request renders
3. **Harder to game** - requires genuine physical understanding, not just plausible visuals
4. **Novel contribution** - designing good questions for industrial world models is the differentiator

**Challenge:** Designing a comprehensive, diverse question set that truly tests world model understanding. This is where we can excel.

**Literature to explore:**
- VQA (Visual Question Answering) benchmarks
- Physical reasoning benchmarks (PHYRE, IntPhys, etc.)
- Embodied QA (EQA)
- Robotics instruction following benchmarks
