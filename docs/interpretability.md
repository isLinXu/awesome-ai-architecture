# 🔬 可解释性与模块分析（Interpretability）

> 拆开看：每个头、每层、每个神经元到底在干什么。

架构设计不该是炼丹。这条赛道收录把 Transformer 模块"打开来看"的工作：
注意力头的功能分类、induction heads 与上下文学习的关系、circuits 视角的机械可解释性。
理解了模块为什么有效，才知道下一步该改哪里。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| A Mathematical Framework for Transformer Circuits | [transformer-circuits.pub](https://transformer-circuits.pub/2021/framework/index.html) | 2021 | 用 circuit 视角分解注意力的奠基性长文 |
| In-context Learning and Induction Heads | [2209.11895](https://arxiv.org/abs/2209.11895) | 2022 | induction heads：上下文学习能力的关键回路 |
| Toy Models of Superposition | [2209.10652](https://arxiv.org/abs/2209.10652) | 2022 | 叠加假说的玩具模型验证：特征为何会挤在同一个神经元里 |

## 相关工具

- [jessevig/bertviz](https://github.com/jessevig/bertviz) — 注意力头可视化工具。
- [TransformerLensOrg/TransformerLens](https://github.com/TransformerLensOrg/TransformerLens) — 机械可解释性标准库（原 Neel Nanda 项目），按模块 hook 一切中间量。

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-05 | [Understanding AI from the Inside: The State of Mechanistic Interpretability for AI Safety](https://arxiv.org/abs/2611.08438v1) | 2611.08438v1 | 9 |
| 2026-10-30 | [A Framework for Task-Agnostic Counterfactual Fairness in Transformers through Activation Steering](https://arxiv.org/abs/2611.00298v1) | 2611.00298v1 | 0 |
| 2026-10-26 | [Mechanistic Insights into LoRA: Layer Sparsity for Adaptive Fine-Tuning via Path Patching](https://arxiv.org/abs/2610.34756v1) | 2610.34756v1 | 0 |
| 2026-10-19 | [Shaped SAEs: Expanding the Toolkit for Mechanistic Interpretability](https://arxiv.org/abs/2610.27375v1) | 2610.27375v1 | 9 |
| 2026-10-18 | [Formally Verified Autoresearch for Analyzing the Expressivity of Multi-Head Attention](https://arxiv.org/abs/2610.25341v1) | 2610.25341v1 | 0 |
| 2026-10-15 | [Spurious Attention Heads in Vision Transformers: Mechanistic Identification of Annotation-Driven Bias in Medical Chest X-Ray Analysis](https://arxiv.org/abs/2610.21638v1) | 2610.21638v1 | 1 |
| 2026-10-14 | [Sparse Transformer: a Controlled Testbed for Mechanistic Interpretability](https://arxiv.org/abs/2610.19907v1) | 2610.19907v1 | 9 |
| 2026-10-13 | [Monitoring latent reasoning in looped language models](https://arxiv.org/abs/2610.18127v1) | 2610.18127v1 | 0 |
| 2026-10-06 | [How High Is 0.6? Floors, Ceilings, and Headroom in Interpretability Probing](https://arxiv.org/abs/2610.08544v1) | 2610.08544v1 | 9 |
| 2026-10-03 | [Beyond the Linear Representation Hypothesis: Non-Linear Activation Steering in Text-to-Image Models](https://arxiv.org/abs/2610.06945v1) | 2610.06945v1 | 6 |
| 2026-09-21 | [Comparing Latent Concept Formation in State Space Models and Transformers via Sparse Autoencoders](https://arxiv.org/abs/2609.24440v1) | 2609.24440v1 | 7 |
| 2026-09-21 | [Topographic Training Concentrates Causal Circuits Without Improving Neuron Monosemanticity](https://arxiv.org/abs/2609.24379v1) | 2609.24379v1 | 6 |
| 2026-09-03 | [Lost in Reordering: Structural Sensitivity of Multilingual LLMs under Semantics-Preserving Perturbations](https://arxiv.org/abs/2609.03511v1) | 2609.03511v1 | 7 |
| 2026-08-30 | [Dissecting Hierarchical Reasoning Models: A Mechanistic Study](https://arxiv.org/abs/2609.22197v1) | 2609.22197v1 | 8 |
| 2026-08-26 | [MechaTerp-TRACE: A Novel Approach for Component Ablation Analysis in Language Models](https://arxiv.org/abs/2609.22163v1) | 2609.22163v1 | 7 |
| 2026-08-25 | [RACE: Scalable Statistical Estimation of Functional Consistency in LLM Neurons](https://arxiv.org/abs/2608.24758v2) | 2608.24758v2 | 7 |
| 2026-08-24 | [Grounding Isn't Knowing: Do VLMs Need Object Localization for Spatial Reasoning?](https://arxiv.org/abs/2608.23074v1) | 2608.23074v1 | 9 |
| 2026-08-23 | [What AstroPT knows about galaxies, and what that can teach us about LLMs](https://arxiv.org/abs/2608.22614v1) | 2608.22614v1 | 10 |
| 2026-08-22 | [Align, Unify, Suppress, Route: A Coherentist View of Transformer Computation](https://arxiv.org/abs/2608.22034v1) | 2608.22034v1 | 10 |
| 2026-08-22 | [The Communication Map of a Transformer](https://arxiv.org/abs/2608.22007v2) | 2608.22007v2 | 6 |
| 2026-08-17 | [Certified Mechanistic Interpretability: Lifting Single-Input Findings to Bounded Neighbourhoods](https://arxiv.org/abs/2609.26112v1) | 2609.26112v1 | 13 |
| 2026-08-14 | [SpIn-ViT: Designing a Sparsity-Induced Vision Transformer That Is Mechanistically Interpretable](https://arxiv.org/abs/2608.14922v1) | 2608.14922v1 | 6 |
| 2026-08-13 | [Perturbation-based Regional Interpretability through Subtraction Mapping (PRISM): naming-error dissociations in language models and post-stroke aphasia](https://arxiv.org/abs/2608.12717v1) | 2608.12717v1 | 8 |
| 2026-08-10 | [Label-Free Parkinson's Disease Screening from Face and Voice through Mechanistic Interpretability](https://arxiv.org/abs/2608.08976v1) | 2608.08976v1 | 10 |
| 2026-08-09 | [Can Graph Learning Learn Circuits?](https://arxiv.org/abs/2608.08536v2) | 2608.08536v2 | 6 |
| 2026-08-04 | [Sparse Weight Decomposition for Efficient Circuit Extraction](https://arxiv.org/abs/2608.03913v1) | 2608.03913v1 | 7 |
| 2026-07-28 | [Emergent Latent-State Computation under Stochastic Volatility](https://arxiv.org/abs/2607.25459v1) | 2607.25459v1 | 6 |
| 2026-07-15 | [Tracing LLM Behavior to the Training Data with Empirical Next-Token Distributions](https://arxiv.org/abs/2607.14306v2) | 2607.14306v2 | 6 |
| 2026-07-14 | [From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery](https://arxiv.org/abs/2607.12474v2) | 2607.12474v2 | 6 |
| 2026-07-10 | [MLPs are Hebbians: Constructing Efficient Fact-Storing MLPs for Transformers](https://arxiv.org/abs/2607.10034v1) | 2607.10034v1 | 6 |
| 2026-07-09 | [When Structured Sparse Autoencoders Learn Consistent Concepts Across Modalities](https://arxiv.org/abs/2607.08605v1) | 2607.08605v1 | 7 |
| 2026-07-08 | [Mechanistic Interpretability for Neural Networks: Circuits, Sparse Features and Symbolic Reasoning](https://arxiv.org/abs/2607.07316v1) | 2607.07316v1 | 18 |
| 2026-07-03 | [Individual Parameters in Weight-Sparse Transformers Appear Interpretable](https://arxiv.org/abs/2607.02964v1) | 2607.02964v1 | 6 |
| 2026-07-02 | [Induction Heads Interpolate N-Grams](https://arxiv.org/abs/2607.02800v1) | 2607.02800v1 | 13 |
| 2026-07-02 | [Towards Robustness against Typographic Attack with Training-free Concept Localization](https://arxiv.org/abs/2607.02494v1) | 2607.02494v1 | 7 |
| 2026-07-02 | [Conditional Co-Ablation: Recovering Self-Repair Backups in Transformer Circuits](https://arxiv.org/abs/2607.01940v3) | 2607.01940v3 | 12 |
| 2026-06-30 | [Representation as a Bottleneck for Mechanistic Interpretability: The Manifestation Unit Protocol](https://arxiv.org/abs/2607.00089v1) | 2607.00089v1 | 9 |
| 2026-06-30 | [Resolving superposition in AI for interpretability and cross-modal alignment in patient-neuronal images](https://arxiv.org/abs/2606.31394v2) | 2606.31394v2 | 6 |
| 2026-06-25 | [PairSAE: Mechanistic Interpretability from Pair Representations in Protein Co-Folding](https://arxiv.org/abs/2606.27440v1) | 2606.27440v1 | 9 |
| 2026-06-23 | [Can Language Model Agents be Helpful Circuit Explainers in Mechanistic Interpretability?](https://arxiv.org/abs/2606.24026v2) | 2606.24026v2 | 14 |
| 2026-06-18 | [From Texts to Scores: Tracing the Emergence of Essay Quality Representations in Large Language Models](https://arxiv.org/abs/2606.20152v1) | 2606.20152v1 | 6 |
| 2026-06-17 | [Closing the Loop: PID Feedback Control for Interpretable Activation Steering in Symbolic Music Generation](https://arxiv.org/abs/2606.18790v1) | 2606.18790v1 | 6 |
| 2026-06-13 | [Transformers Learn the Mestre-Nagao Heuristic](https://arxiv.org/abs/2606.15036v1) | 2606.15036v1 | 11 |
| 2026-06-12 | [Beyond Importance: Interchange-Sobol Sensitivity Reveals Task-Specific Content Channels in Transformer Components](https://arxiv.org/abs/2606.20678v1) | 2606.20678v1 | 6 |
| 2026-06-08 | [VFUSE: Virulent Feature Understanding with Sparse autoEncoders](https://arxiv.org/abs/2606.10080v1) | 2606.10080v1 | 8 |
| 2026-06-08 | [Trajectory Geometry of Transformer Representations Across Layers](https://arxiv.org/abs/2606.09287v2) | 2606.09287v2 | 10 |
| 2026-06-07 | [One Lens, Many Worlds : A Capability-Typed Interface for World-Model Interpretability](https://arxiv.org/abs/2606.09936v1) | 2606.09936v1 | 6 |
| 2026-06-04 | [Inside the Visual Mind: Neuroscience-Motivated Concept Circuits for Interpreting and Steering Vision Transformers](https://arxiv.org/abs/2606.06664v1) | 2606.06664v1 | 8 |
| 2026-06-01 | [When Do Attention Circuits Form? Developmental Trajectories of Capability and Attention-Sink Emergence Across Three 1B-ClassArchitectures](https://arxiv.org/abs/2606.02378v2) | 2606.02378v2 | 6 |
| 2026-05-30 | [A Circuit, Not The Circuit: Non-Unique Causal Localisation of the Mamba-2 State Sink](https://arxiv.org/abs/2606.00930v2) | 2606.00930v2 | 8 |
| 2026-05-29 | [Latent Space Disentanglement via Activation Steering for Interpretable Attribute Control in Symbolic Music Generation](https://arxiv.org/abs/2605.31295v1) | 2605.31295v1 | 6 |
| 2026-05-28 | [Discovering a Zeta Map Algorithm on Dyck Paths via Mechanistic Interpretability](https://arxiv.org/abs/2605.30482v1) | 2605.30482v1 | 12 |
| 2026-05-27 | [Feature Geometry of LoRA Adapters: A Sparse Autoencoder Analysis of Representational Divergence in Fine-Tuned Language Models](https://arxiv.org/abs/2605.28896v1) | 2605.28896v1 | 7 |
| 2026-05-26 | [The Ignition Index: Measuring Global Workspace Dynamics in Language Models](https://arxiv.org/abs/2608.05160v1) | 2608.05160v1 | 8 |
| 2026-05-24 | [Transformer Field Theory: A Response-Theoretic Approach to Mechanistic Interpretability](https://arxiv.org/abs/2605.25225v2) | 2605.25225v2 | 9 |
| 2026-05-21 | [Towards Verifiable Transformers: Solver-Checkable Circuit Explanations](https://arxiv.org/abs/2605.24033v2) | 2605.24033v2 | 6 |
| 2026-05-20 | [Post-Hoc Understanding of Metaphor Processing in Decoder-Only Language Models via Conditional Scale Entropy](https://arxiv.org/abs/2605.21391v1) | 2605.21391v1 | 7 |
| 2026-05-20 | [A Sharper Picture of Generalization in Transformers](https://arxiv.org/abs/2605.20988v2) | 2605.20988v2 | 6 |
| 2026-05-20 | [Markovian Circuit Tracing: Ground-Truth Tests of Transformer State Abstractions](https://arxiv.org/abs/2605.20824v2) | 2605.20824v2 | 8 |
| 2026-05-20 | [Mechanistic Interpretability for Learning Assurance of a Vision-Based Landing System](https://arxiv.org/abs/2605.20607v1) | 2605.20607v1 | 9 |
| 2026-05-17 | [Beyond Linear Superposition: Discovering Climate Features in AI Weather Models with KAN-SAE](https://arxiv.org/abs/2605.17493v1) | 2605.17493v1 | 6 |
| 2026-05-13 | [Rethinking Layer Relevance in Large Language Models Beyond Cosine Similarity](https://arxiv.org/abs/2605.14075v1) | 2605.14075v1 | 7 |
| 2026-05-13 | [Mechanistic Interpretability of EEG Foundation Models via Sparse Autoencoders](https://arxiv.org/abs/2605.13930v3) | 2605.13930v3 | 11 |
| 2026-05-13 | [Transformers Linearly Represent Highly Structured World Models](https://arxiv.org/abs/2605.18847v1) | 2605.18847v1 | 7 |
| 2026-05-12 | [Metaphor Is Not All Attention Needs](https://arxiv.org/abs/2605.12128v1) | 2605.12128v1 | 6 |
| 2026-05-11 | [Dissecting Jet-Tagger Through Mechanistic Interpretability](https://arxiv.org/abs/2605.09881v1) | 2605.09881v1 | 14 |
| 2026-05-09 | [Investigating Anisotropy in Visual Grounding under Controlled Counterfactual Perturbations](https://arxiv.org/abs/2605.09090v1) | 2605.09090v1 | 7 |
| 2026-05-08 | [Activation Differences Reveal Backdoors: A Comparison of SAE Architectures](https://arxiv.org/abs/2605.07324v1) | 2605.07324v1 | 6 |
| 2026-05-07 | [SoftSAE: Dynamic Top-K Selection for Adaptive Sparse Autoencoders](https://arxiv.org/abs/2605.06610v2) | 2605.06610v2 | 6 |
| 2026-05-07 | [From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of Sparse Autoencoder Features](https://arxiv.org/abs/2605.06494v1) | 2605.06494v1 | 9 |
| 2026-05-07 | [Patch-Effect Graph Kernels for LLM Interpretability](https://arxiv.org/abs/2605.06480v1) | 2605.06480v1 | 8 |
| 2026-05-07 | [Playing the network backward: A Game Theoretic Attribution Framework](https://arxiv.org/abs/2605.06212v2) | 2605.06212v2 | 6 |
| 2026-05-07 | [Navigating by Old Maps: The Pitfalls of Static Mechanistic Localization in LLM Post-Training](https://arxiv.org/abs/2605.06076v1) | 2605.06076v1 | 10 |
| 2026-05-06 | [Superposition Is Not Necessary: A Mechanistic Interpretability Analysis of Transformer Representations for Time Series Forecasting](https://arxiv.org/abs/2605.05151v1) | 2605.05151v1 | 12 |
| 2026-05-02 | [Automated Interpretability and Feature Discovery in Language Models with Agents](https://arxiv.org/abs/2605.01555v1) | 2605.01555v1 | 7 |
| 2026-05-01 | [From Local to Global to Mechanistic: An iERF-Centered Unified Framework for Interpreting Vision Models](https://arxiv.org/abs/2605.00474v1) | 2605.00474v1 | 7 |
| 2026-04-28 | [From Insight to Action: A Novel Framework for Interpretability-Guided Data Selection in Large Language Models](https://arxiv.org/abs/2604.25167v1) | 2604.25167v1 | 8 |
| 2026-04-26 | [AIPsy-Affect: A Keyword-Free Clinical Stimulus Battery for Mechanistic Interpretability of Emotion in Language Models](https://arxiv.org/abs/2604.23719v2) | 2604.23719v2 | 14 |
| 2026-04-24 | [Preference Heads in Large Language Models: A Mechanistic Framework for Interpretable Personalization](https://arxiv.org/abs/2604.22345v1) | 2604.22345v1 | 7 |
| 2026-04-20 | [The Topological Dual of a Dataset: A Logic-to-Topology Encoding for AlphaGeometry-Style Data](https://arxiv.org/abs/2604.18050v2) | 2604.18050v2 | 6 |
| 2026-04-15 | [Seeing Through Circuits: Faithful Mechanistic Interpretability for Vision Transformers](https://arxiv.org/abs/2604.14477v1) | 2604.14477v1 | 9 |
| 2026-04-15 | [Causal Drawbridges: Characterizing Gradient Blocking of Syntactic Islands in Transformer LMs](https://arxiv.org/abs/2604.13950v1) | 2604.13950v1 | 6 |
| 2026-04-09 | [Revisiting Anisotropy in Language Transformers: The Geometry of Learning Dynamics](https://arxiv.org/abs/2604.08764v1) | 2604.08764v1 | 6 |
| 2026-04-07 | [LAG-XAI: A Lie-Inspired Affine Geometric Framework for Interpretable Paraphrasing in Transformer Latent Spaces](https://arxiv.org/abs/2604.06086v1) | 2604.06086v1 | 6 |
| 2026-04-04 | [Automated Attention Pattern Discovery at Scale in Large Language Models](https://arxiv.org/abs/2604.03764v1) | 2604.03764v1 | 8 |
| 2026-04-03 | [Finding Belief Geometries with Sparse Autoencoders](https://arxiv.org/abs/2604.02685v1) | 2604.02685v1 | 6 |
| 2026-03-31 | [Tracking Equivalent Mechanistic Interpretations Across Neural Networks](https://arxiv.org/abs/2603.30002v1) | 2603.30002v1 | 6 |
| 2026-03-23 | [Steering Sparse Autoencoder Latents to Control Dynamic Head Pruning in Vision Transformers (Student Abstract)](https://arxiv.org/abs/2603.26743v1) | 2603.26743v1 | 6 |
| 2026-03-23 | [What Do World Models Learn in RL? Probing Latent Representations in Learned Environment Simulators](https://arxiv.org/abs/2603.21546v1) | 2603.21546v1 | 8 |
| 2026-03-19 | [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](https://arxiv.org/abs/2603.18505v1) | 2603.18505v1 | 7 |
| 2026-03-16 | [Mechanistic Foundations of Goal-Directed Control](https://arxiv.org/abs/2603.15248v2) | 2603.15248v2 | 11 |
| 2026-03-16 | [Directional Routing in Transformers](https://arxiv.org/abs/2603.14923v1) | 2603.14923v1 | 10 |
| 2026-03-12 | [Exhaustive Circuit Mapping of a Single-Cell Foundation Model Reveals Massive Redundancy, Heavy-Tailed Hub Architecture, and Layer-Dependent Differentiation Control](https://arxiv.org/abs/2603.11940v1) | 2603.11940v1 | 7 |
| 2026-03-12 | [Locating Demographic Bias at the Attention-Head Level in CLIP's Vision Encoder](https://arxiv.org/abs/2603.11793v1) | 2603.11793v1 | 7 |
| 2026-03-11 | [Attention Gathers, MLPs Compose: A Causal Analysis of an Action-Outcome Circuit in VideoViT](https://arxiv.org/abs/2603.11142v1) | 2603.11142v1 | 7 |
| 2026-03-11 | [Backdoor Directions in Vision Transformers](https://arxiv.org/abs/2603.10806v1) | 2603.10806v1 | 7 |
| 2026-03-11 | [Implicit Statistical Inference in Transformers: Approximating Likelihood-Ratio Tests In-Context](https://arxiv.org/abs/2603.10573v1) | 2603.10573v1 | 7 |
| 2026-03-05 | [Observing and Controlling Features in Vision-Language-Action Models](https://arxiv.org/abs/2603.05487v2) | 2603.05487v2 | 6 |
| 2026-03-05 | [The Geometric Inductive Bias of Grokking: Bypassing Phase Transitions via Architectural Topology](https://arxiv.org/abs/2603.05228v3) | 2603.05228v3 | 7 |
| 2026-03-05 | [Stochastic Optimal Feedforward-Feedback Control for Partially Observable Sensorimotor Systems](https://arxiv.org/abs/2603.04994v1) | 2603.04994v1 | 6 |
| 2026-02-26 | [MetaOthello: A Controlled Study of Multiple World Models in Transformers](https://arxiv.org/abs/2602.23164v2) | 2602.23164v2 | 8 |
| 2026-02-26 | [Interpreting and Steering State-Space Models via Activation Subspace Bottlenecks](https://arxiv.org/abs/2602.22719v2) | 2602.22719v2 | 6 |
| 2026-02-22 | [Beyond Behavioural Trade-Offs: Mechanistic Tracing of Pain-Pleasure Decisions in an LLM](https://arxiv.org/abs/2602.19159v1) | 2602.19159v1 | 8 |
| 2026-02-17 | [Quantifying LLM Attention-Head Stability: Implications for Circuit Universality](https://arxiv.org/abs/2602.16740v1) | 2602.16740v1 | 6 |
| 2026-02-16 | [Seeing to Generalize: How Visual Data Corrects Binding Shortcuts](https://arxiv.org/abs/2602.15183v1) | 2602.15183v1 | 6 |
| 2026-02-16 | [Inner Loop Inference for Pretrained Transformers: Unlocking Latent Capabilities Without Training](https://arxiv.org/abs/2602.14759v2) | 2602.14759v2 | 6 |
| 2026-02-13 | [NAST: Improving Negation Handling in Medical Vision-Language Models through Negation-Aware Selective Training](https://arxiv.org/abs/2602.12498v2) | 2602.12498v2 | 6 |
| 2026-02-11 | [Learning Glioblastoma Tumor Heterogeneity Using Brain Inspired Topological Neural Networks](https://arxiv.org/abs/2602.11234v1) | 2602.11234v1 | 7 |
| 2026-02-10 | [Circuit Fingerprints: How Answer Tokens Encode Their Geometrical Path](https://arxiv.org/abs/2602.09784v1) | 2602.09784v1 | 6 |
| 2026-02-05 | [The Story is Not the Science: Execution-Grounded Evaluation of Mechanistic Interpretability Research](https://arxiv.org/abs/2602.18458v1) | 2602.18458v1 | 9 |
| 2026-02-04 | [Hierarchical Latent Structures in Data Generation Process Unify Mechanistic Phenomena across Scale](https://arxiv.org/abs/2603.06592v2) | 2603.06592v2 | 10 |
| 2026-02-03 | [Momentum Attention: The Physics of In-Context Learning and Spectral Forensics for Mechanistic Interpretability](https://arxiv.org/abs/2602.04902v2) | 2602.04902v2 | 13 |
| 2026-02-03 | [Explaining the Explainer: Understanding the Inner Workings of Transformer-based Symbolic Regression Models](https://arxiv.org/abs/2602.03506v1) | 2602.03506v1 | 9 |
| 2026-02-02 | [Universal Redundancies in Time Series Foundation Models](https://arxiv.org/abs/2602.01605v2) | 2602.01605v2 | 6 |
| 2026-01-30 | [Sparse or Dense? A Mechanistic Estimation of Computation Density in Transformer-based LLMs](https://arxiv.org/abs/2601.22795v2) | 2601.22795v2 | 6 |
| 2026-01-29 | [Putting a Face to Forgetting: Continual Learning meets Mechanistic Interpretability](https://arxiv.org/abs/2601.22012v3) | 2601.22012v3 | 10 |
| 2026-01-27 | [How Do Transformers Learn to Associate Tokens: Gradient Leading Terms Bring Mechanistic Interpretability](https://arxiv.org/abs/2601.19208v2) | 2601.19208v2 | 10 |
| 2026-01-25 | [A Monosemantic Attribution Framework for Stable Interpretability in Clinical Neuroscience Transformer-Based Language Models](https://arxiv.org/abs/2601.17952v2) | 2601.17952v2 | 7 |
| 2026-01-16 | [From Interpretability to Performance: Optimizing Retrieval Heads for Long-Context Language Models](https://arxiv.org/abs/2601.11020v3) | 2601.11020v3 | 7 |
| 2026-01-09 | [Circuit Mechanisms for Spatial Relation Generation in Diffusion Transformers](https://arxiv.org/abs/2601.06338v2) | 2601.06338v2 | 6 |
| 2026-01-07 | [Interpreting Transformers Through Attention Head Intervention](https://arxiv.org/abs/2601.04398v4) | 2601.04398v4 | 6 |
| 2026-01-03 | [Central Dogma Transformer: Towards Mechanism-Oriented AI for Cellular Understanding](https://arxiv.org/abs/2601.01089v2) | 2601.01089v2 | 7 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-31 | [Triangulation as an Acceptance Rule for Multilingual Mechanistic Interpretability](https://arxiv.org/abs/2512.24842v1) | 2512.24842v1 | 9 |
| 2025-12-17 | [SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks](https://arxiv.org/abs/2512.15938v2) | 2512.15938v2 | 6 |
| 2025-12-07 | [Mechanistic Interpretability of GPT-2: Lexical and Contextual Layers in Sentiment Analysis](https://arxiv.org/abs/2512.06681v1) | 2512.06681v1 | 10 |
| 2025-12-03 | [Minuet: A Diffusion Autoencoder for Compact Semantic Compression of Multi-Band Galaxy Images](https://arxiv.org/abs/2512.04145v1) | 2512.04145v1 | 8 |
| 2025-11-26 | [Start Making Sense(s): A Developmental Probe of Attention Specialization Using Lexical Ambiguity](https://arxiv.org/abs/2511.21974v1) | 2511.21974v1 | 7 |
| 2025-11-26 | [Mechanistic Interpretability for Transformer-based Time Series Classification](https://arxiv.org/abs/2511.21514v1) | 2511.21514v1 | 11 |
| 2025-11-25 | [Beyond Components: Singular Vector-Based Interpretability of Transformer Circuits](https://arxiv.org/abs/2511.20273v1) | 2511.20273v1 | 13 |
| 2025-11-20 | [BlockCert: Certified Blockwise Extraction of Transformer Mechanisms](https://arxiv.org/abs/2511.17645v1) | 2511.17645v1 | 6 |
| 2025-11-18 | [nnterp: A Standardized Interface for Mechanistic Interpretability of Transformers](https://arxiv.org/abs/2511.14465v2) | 2511.14465v2 | 10 |
| 2025-11-12 | [Decomposition of Small Transformer Models](https://arxiv.org/abs/2511.08854v2) | 2511.08854v2 | 7 |
| 2025-11-10 | [SCALAR: Benchmarking SAE Interaction Sparsity in Toy LLMs](https://arxiv.org/abs/2511.07572v1) | 2511.07572v1 | 6 |
| 2025-11-10 | [Learning Biomolecular Motion: The Physics-Informed Machine Learning Paradigm](https://arxiv.org/abs/2511.06585v1) | 2511.06585v1 | 6 |
| 2025-11-02 | [On the Emergence of Induction Heads for In-Context Learning](https://arxiv.org/abs/2511.01033v2) | 2511.01033v2 | 6 |
| 2025-10-28 | [Emergence of Minimal Circuits for Indirect Object Identification in Attention-Only Transformers](https://arxiv.org/abs/2510.25013v2) | 2510.25013v2 | 9 |
| 2025-10-24 | [Mechanistic Interpretability for Neural TSP Solvers](https://arxiv.org/abs/2510.21693v1) | 2510.21693v1 | 10 |
| 2025-10-21 | [DePass: Unified Feature Attributing by Simple Decomposed Forward Pass](https://arxiv.org/abs/2510.18462v2) | 2510.18462v2 | 8 |
| 2025-10-20 | [Extracting Rule-based Descriptions of Attention Features in Transformers](https://arxiv.org/abs/2510.18148v1) | 2510.18148v1 | 6 |
| 2025-10-20 | [Explainability of Large Language Models: Opportunities and Challenges toward Generating Trustworthy Explanations](https://arxiv.org/abs/2510.17256v2) | 2510.17256v2 | 6 |
| 2025-10-20 | [Fighter: Unveiling the Graph Convolutional Nature of Transformers in Time Series Modeling](https://arxiv.org/abs/2510.17106v1) | 2510.17106v1 | 6 |
| 2025-10-16 | [CAST: Compositional Analysis via Spectral Tracking for Understanding Transformer Layer Functions](https://arxiv.org/abs/2510.14262v1) | 2510.14262v1 | 7 |
| 2025-10-15 | [Unlocking Out-of-Distribution Generalization in Transformers via Recursive Latent Space Reasoning](https://arxiv.org/abs/2510.14095v1) | 2510.14095v1 | 7 |
| 2025-10-10 | [Causality $\neq$ Decodability, and Vice Versa: Lessons from Interpreting Counting ViTs](https://arxiv.org/abs/2510.09794v1) | 2510.09794v1 | 8 |
| 2025-10-10 | [Deductive Logic in Language Models: Horizontal vs Vertical Reasoning](https://arxiv.org/abs/2510.09340v2) | 2510.09340v2 | 6 |
| 2025-10-06 | [Causal Abstractions, Categorically Unified](https://arxiv.org/abs/2510.05033v1) | 2510.05033v1 | 7 |
| 2025-10-06 | [Visual Representations inside the Language Model](https://arxiv.org/abs/2510.04819v1) | 2510.04819v1 | 6 |
| 2025-10-03 | [Disentangling Recall and Reasoning in Transformer Models through Layer-wise Attention and Activation Analysis](https://arxiv.org/abs/2510.03366v2) | 2510.03366v2 | 9 |
| 2025-10-01 | [Feature Identification via the Empirical NTK](https://arxiv.org/abs/2510.00468v4) | 2510.00468v4 | 7 |
| 2025-09-25 | [CLUE: Conflict-guided Localization for LLM Unlearning Framework](https://arxiv.org/abs/2509.20977v1) | 2509.20977v1 | 6 |
| 2025-09-18 | [Modeling Transformers as complex networks to analyze learning dynamics](https://arxiv.org/abs/2509.15269v1) | 2509.15269v1 | 6 |
| 2025-09-09 | [Selective Induction Heads: How Transformers Select Causal Structures In Context](https://arxiv.org/abs/2509.08184v1) | 2509.08184v1 | 9 |
| 2025-09-08 | [Measuring Uncertainty in Transformer Circuits with Effective Information Consistency](https://arxiv.org/abs/2509.07149v1) | 2509.07149v1 | 13 |
| 2025-08-30 | [Mechanistic interpretability for steering vision-language-action models](https://arxiv.org/abs/2509.00328v1) | 2509.00328v1 | 9 |
| 2025-08-22 | [From Indirect Object Identification to Syllogisms: Exploring Binary Mechanisms in Transformer Circuits](https://arxiv.org/abs/2508.16109v1) | 2508.16109v1 | 13 |
| 2025-08-19 | [Mechanistic Exploration of Backdoored Large Language Model Attention Patterns](https://arxiv.org/abs/2508.15847v1) | 2508.15847v1 | 7 |
| 2025-07-21 | [Probing Information Distribution in Transformer Architectures through Entropy Analysis](https://arxiv.org/abs/2507.15347v2) | 2507.15347v2 | 6 |
| 2025-07-17 | [Insights into a radiology-specialised multimodal large language model with sparse autoencoders](https://arxiv.org/abs/2507.12950v2) | 2507.12950v2 | 6 |
| 2025-07-16 | [CytoSAE: Interpretable Cell Embeddings for Hematology](https://arxiv.org/abs/2507.12464v1) | 2507.12464v1 | 6 |
| 2025-07-12 | [Adversarial Activation Patching: A Framework for Detecting and Mitigating Emergent Deception in Safety-Aligned Transformers](https://arxiv.org/abs/2507.09406v1) | 2507.09406v1 | 6 |
| 2025-07-04 | [TRACE: Training and Inference-Time Interpretability Analysis for Language Models](https://arxiv.org/abs/2507.03668v1) | 2507.03668v1 | 6 |
| 2025-07-03 | [Transformers Don't Need LayerNorm at Inference Time: Scaling LayerNorm Removal to GPT-2 XL and the Implications for Mechanistic Interpretability](https://arxiv.org/abs/2507.02559v1) | 2507.02559v1 | 9 |
| 2025-06-30 | [Learning Modular Exponentiation with Transformers](https://arxiv.org/abs/2506.23679v2) | 2506.23679v2 | 7 |
| 2025-06-23 | [Transformer Circuits Can Realize Clustering Algorithms](https://arxiv.org/abs/2506.19125v2) | 2506.19125v2 | 6 |
| 2025-06-22 | [Mechanistic Interpretability in the Presence of Architectural Obfuscation](https://arxiv.org/abs/2506.18053v1) | 2506.18053v1 | 9 |
| 2025-06-20 | [Latent Concept Disentanglement in Transformer-based Language Models](https://arxiv.org/abs/2506.16975v2) | 2506.16975v2 | 6 |
| 2025-06-17 | [Understanding Verbatim Memorization in LLMs Through Circuit Discovery](https://arxiv.org/abs/2506.21588v2) | 2506.21588v2 | 10 |
| 2025-06-04 | [Mechanistic Decomposition of Sentence Representations](https://arxiv.org/abs/2506.04373v2) | 2506.04373v2 | 7 |
| 2025-05-26 | [From What to How: Attributing CLIP's Latent Components Reveals Unexpected Semantic Reliance](https://arxiv.org/abs/2505.20229v1) | 2505.20229v1 | 8 |
| 2025-05-26 | [The Birth of Knowledge: Emergent Features across Time, Space, and Scale in Large Language Models](https://arxiv.org/abs/2505.19440v1) | 2505.19440v1 | 7 |
| 2025-05-24 | [DB-KSVD: Scalable Alternating Optimization for Disentangling High-Dimensional Embedding Spaces](https://arxiv.org/abs/2505.18441v2) | 2505.18441v2 | 6 |
| 2025-05-20 | [Mechanistic Interpretability of GPT-like Models on Summarization Tasks](https://arxiv.org/abs/2505.17073v1) | 2505.17073v1 | 11 |
| 2025-05-19 | [Causal Head Gating: A Framework for Interpreting Roles of Attention Heads in Transformers](https://arxiv.org/abs/2505.13737v2) | 2505.13737v2 | 6 |
| 2025-05-16 | [Illusion or Algorithm? Investigating Memorization, Emergence, and Symbolic Processing in In-Context Learning](https://arxiv.org/abs/2505.11004v3) | 2505.11004v3 | 7 |
| 2025-05-16 | [Distilled Circuits: A Mechanistic Study of Internal Restructuring in Knowledge Distillation](https://arxiv.org/abs/2505.10822v2) | 2505.10822v2 | 6 |
| 2025-05-08 | [Safety by Measurement: A Systematic Literature Review of AI Safety Evaluation Methods](https://arxiv.org/abs/2505.05541v1) | 2505.05541v1 | 7 |
| 2025-05-06 | [A Multi-Level Causal Intervention Framework for Mechanistic Interpretability in Variational Autoencoders](https://arxiv.org/abs/2505.03530v3) | 2505.03530v3 | 10 |
| 2025-04-29 | [Towards Understanding the Nature of Attention with Low-Rank Sparse Decomposition](https://arxiv.org/abs/2504.20938v1) | 2504.20938v1 | 7 |
| 2025-04-28 | [Prisma: An Open Source Toolkit for Mechanistic Interpretability in Vision and Video](https://arxiv.org/abs/2504.19475v3) | 2504.19475v3 | 10 |
| 2025-04-25 | [Structural Inference: Interpreting Small Language Models with Susceptibilities](https://arxiv.org/abs/2504.18274v3) | 2504.18274v3 | 6 |
| 2025-04-18 | [Signatures of human-like processing in Transformer forward passes](https://arxiv.org/abs/2504.14107v2) | 2504.14107v2 | 6 |
| 2025-04-18 | [Decoding Vision Transformers: the Diffusion Steering Lens](https://arxiv.org/abs/2504.13763v2) | 2504.13763v2 | 7 |
| 2025-04-06 | [Activation Patching for Interpretable Steering in Music Generation](https://arxiv.org/abs/2504.04479v1) | 2504.04479v1 | 7 |
| 2025-03-31 | [Identifying Sparsely Active Circuits Through Local Loss Landscape Decomposition](https://arxiv.org/abs/2504.00194v1) | 2504.00194v1 | 6 |
| 2025-03-30 | [Embedding Shift Dissection on CLIP: Effects of Augmentations on VLM's Representation Learning](https://arxiv.org/abs/2503.23495v3) | 2503.23495v3 | 7 |
| 2025-03-25 | [Reverse-Engineering the Retrieval Process in GenIR Models](https://arxiv.org/abs/2503.19715v2) | 2503.19715v2 | 6 |
| 2025-03-24 | [Mechanistic Interpretability of Fine-Tuned Vision Transformers on Distorted Images: Decoding Attention Head Behavior for Transparent and Trustworthy AI](https://arxiv.org/abs/2503.18762v1) | 2503.18762v1 | 9 |
| 2025-03-13 | [HyperDAS: Towards Automating Mechanistic Interpretability with Hypernetworks](https://arxiv.org/abs/2503.10894v3) | 2503.10894v3 | 9 |
| 2025-03-07 | [A Survey on Sparse Autoencoders: Interpreting the Internal Mechanisms of Large Language Models](https://arxiv.org/abs/2503.05613v3) | 2503.05613v3 | 6 |
| 2025-03-03 | [Linear Representations of Political Perspective Emerge in Large Language Models](https://arxiv.org/abs/2503.02080v2) | 2503.02080v2 | 8 |
| 2025-02-22 | [A Survey on Mechanistic Interpretability for Multi-Modal Foundation Models](https://arxiv.org/abs/2502.17516v1) | 2502.17516v1 | 10 |
| 2025-02-19 | [An explainable transformer circuit for compositional generalization](https://arxiv.org/abs/2502.15801v1) | 2502.15801v1 | 8 |
| 2025-02-17 | [Towards Mechanistic Interpretability of Graph Transformers via Attention Graphs](https://arxiv.org/abs/2502.12352v2) | 2502.12352v2 | 9 |
| 2025-02-17 | [Transformer Dynamics: A neuroscientific approach to interpretability of large language models](https://arxiv.org/abs/2502.12131v1) | 2502.12131v1 | 8 |
| 2025-02-13 | [Interpreting and Steering Protein Language Models through Sparse Autoencoders](https://arxiv.org/abs/2502.09135v1) | 2502.09135v1 | 7 |
| 2025-02-13 | [Mechanistic Unveiling of Transformer Circuits: Self-Influence as a Key to Model Reasoning](https://arxiv.org/abs/2502.09022v2) | 2502.09022v2 | 13 |
| 2025-02-10 | [Do Attention Heads Compete or Cooperate during Counting?](https://arxiv.org/abs/2502.06923v1) | 2502.06923v1 | 7 |
| 2025-02-07 | [EAP-GP: Mitigating Saturation Effect in Gradient-based Automated Circuit Identification](https://arxiv.org/abs/2502.06852v1) | 2502.06852v1 | 6 |
| 2025-02-05 | [The Logical Implication Steering Method for Conditional Interventions on Transformer Generation](https://arxiv.org/abs/2502.03618v2) | 2502.03618v2 | 6 |
| 2025-02-04 | [Constrained belief updates explain geometric structures in transformer representations](https://arxiv.org/abs/2502.01954v2) | 2502.01954v2 | 8 |
| 2025-01-29 | [Automated Interpretability Metrics Do Not Distinguish Trained and Random Transformers](https://arxiv.org/abs/2501.17727v2) | 2501.17727v2 | 7 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-17 | [Benchmarking and Understanding Compositional Relational Reasoning of LLMs](https://arxiv.org/abs/2412.12841v1) | 2412.12841v1 | 6 |
| 2024-12-06 | [Transformers Struggle to Learn to Search](https://arxiv.org/abs/2412.04703v2) | 2412.04703v2 | 6 |
| 2024-12-05 | [Monet: Mixture of Monosemantic Experts for Transformers](https://arxiv.org/abs/2412.04139v4) | 2412.04139v4 | 6 |
| 2024-12-04 | [Modular addition without black-boxes: Compressing explanations of MLPs that compute numerical integration](https://arxiv.org/abs/2412.03773v1) | 2412.03773v1 | 6 |
| 2024-10-31 | [Group Crosscoders for Mechanistic Analysis of Symmetry](https://arxiv.org/abs/2410.24184v2) | 2410.24184v2 | 7 |
| 2024-10-31 | [Dynamical similarity analysis can identify compositional dynamics developing in RNNs](https://arxiv.org/abs/2410.24070v4) | 2410.24070v4 | 9 |
| 2024-10-31 | [Interpretable Next-token Prediction via the Generalized Induction Head](https://arxiv.org/abs/2411.00066v2) | 2411.00066v2 | 8 |
| 2024-10-24 | [Probing Ranking LLMs: A Mechanistic Analysis for Information Retrieval](https://arxiv.org/abs/2410.18527v3) | 2410.18527v3 | 6 |
| 2024-10-22 | [Interpreting Affine Recurrence Learning in GPT-style Transformers](https://arxiv.org/abs/2410.17438v1) | 2410.17438v1 | 6 |
| 2024-10-16 | [Interpreting token compositionality in LLMs: A robustness analysis](https://arxiv.org/abs/2410.12924v3) | 2410.12924v3 | 7 |
| 2024-10-12 | [ReLU's Revival: On the Entropic Overload in Normalization-Free Large Language Models](https://arxiv.org/abs/2410.09637v3) | 2410.09637v3 | 6 |
| 2024-10-09 | [Quantifying Feature Space Universality Across Large Language Models via Sparse Autoencoders](https://arxiv.org/abs/2410.06981v4) | 2410.06981v4 | 6 |
| 2024-10-08 | [Interpretability for Time Series Transformers using A Concept Bottleneck Framework](https://arxiv.org/abs/2410.06070v2) | 2410.06070v2 | 8 |
| 2024-10-04 | [An X-Ray Is Worth 15 Features: Sparse Autoencoders for Interpretable Radiology Report Generation](https://arxiv.org/abs/2410.03334v1) | 2410.03334v1 | 7 |
| 2024-10-02 | [Circuit Compositions: Exploring Modular Structures in Transformer-Based Language Models](https://arxiv.org/abs/2410.01434v3) | 2410.01434v3 | 6 |
| 2024-09-16 | [Self-Attention Limits Working Memory Capacity of Transformer-Based Models](https://arxiv.org/abs/2409.10715v2) | 2409.10715v2 | 6 |
| 2024-09-06 | [You can remove GPT2's LayerNorm by fine-tuning](https://arxiv.org/abs/2409.13710v2) | 2409.13710v2 | 6 |
| 2024-08-26 | [Enhancing Neural Network Interpretability Through Conductance-Based Information Plane Analysis](https://arxiv.org/abs/2408.14681v1) | 2408.14681v1 | 6 |
| 2024-08-05 | [Bridging Linguistic Structure and Mechanistic Interpretability for Conceptual Interpretation in Language Models](https://arxiv.org/abs/2408.11827v2) | 2408.11827v2 | 10 |
| 2024-07-19 | [InterpBench: Semi-Synthetic Transformers for Evaluating Mechanistic Interpretability Techniques](https://arxiv.org/abs/2407.14494v3) | 2407.14494v3 | 9 |
| 2024-07-19 | [Investigating the Indirect Object Identification circuit in Mamba](https://arxiv.org/abs/2407.14008v2) | 2407.14008v2 | 6 |
| 2024-07-18 | [Validating Mechanistic Interpretations: An Axiomatic Approach](https://arxiv.org/abs/2407.13594v2) | 2407.13594v2 | 7 |
| 2024-07-15 | [Mechanistic interpretability of large language models with applications to the financial services industry](https://arxiv.org/abs/2407.11215v2) | 2407.11215v2 | 10 |
| 2024-07-02 | [A Practical Review of Mechanistic Interpretability for Transformer-Based Language Models](https://arxiv.org/abs/2407.02646v4) | 2407.02646v4 | 9 |
| 2024-07-01 | [Efficient Automated Circuit Discovery in Transformers using Contextual Decomposition](https://arxiv.org/abs/2407.00886v3) | 2407.00886v3 | 6 |
| 2024-06-25 | [Interpreting Attention Layer Outputs with Sparse Autoencoders](https://arxiv.org/abs/2406.17759v1) | 2406.17759v1 | 11 |
| 2024-06-22 | [Beyond the Doors of Perception: Vision Transformers Represent Relations Between Objects](https://arxiv.org/abs/2406.15955v3) | 2406.15955v3 | 6 |
| 2024-06-20 | [From Transformer to Biology: A Hierarchical Model for Attention in Complex Problem-Solving](https://arxiv.org/abs/2406.14100v2) | 2406.14100v2 | 7 |
| 2024-06-17 | [Transcoders Find Interpretable LLM Feature Circuits](https://arxiv.org/abs/2406.11944v2) | 2406.11944v2 | 7 |
| 2024-06-17 | [Compact Proofs of Model Performance via Mechanistic Interpretability](https://arxiv.org/abs/2406.11779v14) | 2406.11779v14 | 9 |
| 2024-05-27 | [Mechanistic Interpretability of Binary and Ternary Transformers](https://arxiv.org/abs/2405.17703v1) | 2405.17703v1 | 9 |
| 2024-05-17 | [The Local Interaction Basis: Identifying Computationally-Relevant and Sparsely Interacting Features in Neural Networks](https://arxiv.org/abs/2405.10928v2) | 2405.10928v2 | 7 |
| 2024-05-07 | [How does GPT-2 Predict Acronyms? Extracting and Understanding a Circuit via Mechanistic Interpretability](https://arxiv.org/abs/2405.04156v1) | 2405.04156v1 | 9 |
| 2024-04-10 | [What needs to go right for an induction head? A mechanistic study of in-context learning circuits and their formation](https://arxiv.org/abs/2404.07129v1) | 2404.07129v1 | 12 |
| 2024-02-19 | [Dictionary Learning Improves Patch-Free Circuit Discovery in Mechanistic Interpretability: A Case Study on Othello-GPT](https://arxiv.org/abs/2402.12201v1) | 2402.12201v1 | 9 |
| 2024-02-02 | [An introduction to graphical tensor notation for mechanistic interpretability](https://arxiv.org/abs/2402.01790v1) | 2402.01790v1 | 17 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-26 | [Observable Propagation: Uncovering Feature Vectors in Transformers](https://arxiv.org/abs/2312.16291v2) | 2312.16291v2 | 7 |
| 2023-11-21 | [Mechanistically analyzing the effects of fine-tuning on procedurally defined tasks](https://arxiv.org/abs/2311.12786v2) | 2311.12786v2 | 9 |
| 2023-11-14 | [The Transient Nature of Emergent In-Context Learning in Transformers](https://arxiv.org/abs/2311.08360v3) | 2311.08360v3 | 6 |
| 2023-10-29 | [Analyzing Vision Transformers for Image Classification in Class Embedding Space](https://arxiv.org/abs/2310.18969v1) | 2310.18969v1 | 8 |
| 2023-07-05 | [Harmonizing Feature Attributions Across Deep Learning Architectures: Enhancing Interpretability and Consistency](https://arxiv.org/abs/2307.02150v3) | 2307.02150v3 | 6 |
| 2023-06-16 | [Beyond Geometry: Comparing the Temporal Structure of Computation in Neural Circuits with Dynamical Similarity Analysis](https://arxiv.org/abs/2306.10168v3) | 2306.10168v3 | 7 |
| 2023-06-01 | [Learning Transformer Programs](https://arxiv.org/abs/2306.01128v2) | 2306.01128v2 | 7 |
| 2023-05-24 | [Can Transformers Learn to Solve Problems Recursively?](https://arxiv.org/abs/2305.14699v2) | 2305.14699v2 | 6 |
| 2023-05-05 | [A technical note on bilinear layers for interpretability](https://arxiv.org/abs/2305.03452v1) | 2305.03452v1 | 11 |
| 2023-04-28 | [Towards Automated Circuit Discovery for Mechanistic Interpretability](https://arxiv.org/abs/2304.14997v4) | 2304.14997v4 | 9 |
| 2023-01-12 | [Progress measures for grokking via mechanistic interpretability](https://arxiv.org/abs/2301.05217v3) | 2301.05217v3 | 9 |
| 2023-01-11 | [Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability](https://arxiv.org/abs/2301.04709v4) | 2301.04709v4 | 10 |

### 2018
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2018-01-15 | [Predictive Systems Toxicology](https://arxiv.org/abs/1801.05058v1) | 1801.05058v1 | 7 |

<!-- table:end papers -->
