# 🔀 FFN 与混合专家（FFN & Mixture-of-Experts）

> 模型的另一半算力花在哪：门控激活与稀疏专家。

注意力负责"信息怎么流动"，FFN 负责"信息怎么加工"——通常占模型三分之二的参数。
这条赛道收录 FFN 侧的演进：GLU/SwiGLU 门控激活、以及把稠密 FFN 换成稀疏路由专家的
MoE 路线（GShard/Switch/Mixtral）。MoE 让"参数规模"与"单 token 算力"解耦，
是 DeepSeek-V3、Mixtral、Qwen 系列放大模型的关键杠杆。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer | [1701.06538](https://arxiv.org/abs/1701.06538) | 2017 | MoE 的源头：稀疏门控专家层 |
| GLU Variants Improve Transformer | [2002.05202](https://arxiv.org/abs/2002.05202) | 2020 | 系统对比门控激活，SwiGLU 后来成为 LLM 标配 |
| GShard: Scaling Giant Models with Conditional Computation and Automatic Sharding | [2006.16668](https://arxiv.org/abs/2006.16668) | 2020 | MoE 首次在机器翻译上规模化落地 |
| Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity | [2101.03961](https://arxiv.org/abs/2101.03961) | 2021 | top-1 路由 + 负载均衡损失，MoE 实用化 |
| ST-MoE: Designing Stable and Transferable Sparse Expert Models | [2202.08906](https://arxiv.org/abs/2202.08906) | 2022 | 路由器设计的系统经验（z-loss、稳定性） |
| Mixtral of Experts | [2401.04088](https://arxiv.org/abs/2401.04088) | 2024 | 稀疏 MoE 开放权重的标杆，8×7B top-2 路由 |
| DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | [2405.04434](https://arxiv.org/abs/2405.04434) | 2024 | 细粒度专家 + 共享专家，DeepSeekMoE 架构 |

## 相关实现

- [mistralai/mistral-inference](https://github.com/mistralai/mistral-inference) — Mixtral 稀疏 MoE 参考实现。
- [deepseek-ai/DeepSeek-V3](https://github.com/deepseek-ai/DeepSeek-V3) — 细粒度 MoE + 无辅助损失负载均衡。

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-06 | [Rethinking MoE Load Balancing as Feedback Control](https://arxiv.org/abs/2611.09252v1) | 2611.09252v1 | 16 |
| 2026-11-06 | [ISER-MoE: Dynamic In-Switch Replication of Hot Experts for Load Balancing in Expert-Parallel](https://arxiv.org/abs/2611.09008v1) | 2611.09008v1 | 10 |
| 2026-11-05 | [Multimodal Hierarchical Mixture-of-Experts for 3D Medical Vision-Language Modeling](https://arxiv.org/abs/2611.08185v1) | 2611.08185v1 | 6 |
| 2026-11-05 | [SAE Interprets MoE: Sparse AutoEncoders Reveal That MoE Experts Exhibit Human-Interpretable Fine-Grained Specialization](https://arxiv.org/abs/2611.08089v1) | 2611.08089v1 | 0 |
| 2026-11-05 | [English Calibration Erodes Lithuanian in Expert-Pruned Mixture-of-Experts Language Models](https://arxiv.org/abs/2611.07654v1) | 2611.07654v1 | 6 |
| 2026-11-05 | [LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation](https://arxiv.org/abs/2611.07515v1) | 2611.07515v1 | 0 |
| 2026-11-05 | [AlterNet: Adaptive-Depth Mixture-of-Experts with Learned Halting for Elastic Inference](https://arxiv.org/abs/2611.08741v1) | 2611.08741v1 | 6 |
| 2026-11-04 | [Server-Side Sparse Assignment for Federated Mixture-of-Experts](https://arxiv.org/abs/2611.07093v1) | 2611.07093v1 | 6 |
| 2026-11-04 | [Rules, Traces and Routing Statistics: Training and Calibration Data for Open Models on ARC-AGI-2](https://arxiv.org/abs/2611.06827v1) | 2611.06827v1 | 0 |
| 2026-11-04 | [vExpert: Virtualizing Expert Storage for Adaptive Load Balancing in Distributed MoE Inference](https://arxiv.org/abs/2611.06057v1) | 2611.06057v1 | 6 |
| 2026-11-04 | [Routes of Reasoning: Reading and Reshaping Test-Time Compute in MoE Models](https://arxiv.org/abs/2611.05919v1) | 2611.05919v1 | 0 |
| 2026-11-03 | [Relevance Propagation as Entropic Optimal Transport on Filippov Neural Networks: Sinkhorn Propagation and Region Relevance in Image Classifiers](https://arxiv.org/abs/2611.05594v1) | 2611.05594v1 | 0 |
| 2026-11-03 | [Wonder 4: A Mixture-of-Experts Recipe for Image Quality Enhancement](https://arxiv.org/abs/2611.05294v1) | 2611.05294v1 | 6 |
| 2026-11-03 | [Aligning Training and Rollout Policies for End-to-End FP4 RL on Mixture-of-Experts LLMs](https://arxiv.org/abs/2611.04376v2) | 2611.04376v2 | 6 |
| 2026-11-03 | [GC-MoE: Overlapping Expert-Parallel Token Dispatch with FP8/FP4 Grouped GEMM via CUDA Green Contexts](https://arxiv.org/abs/2611.04222v1) | 2611.04222v1 | 0 |
| 2026-11-02 | [HybridSpec: Throughput-Aware Speculative Decoding for Hybrid GDN-MoE Models](https://arxiv.org/abs/2611.04055v1) | 2611.04055v1 | 0 |
| 2026-11-02 | [Sonar-MoE: In-Backward Expert Updates for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/abs/2611.03577v2) | 2611.03577v2 | 6 |
| 2026-11-02 | [Library of Layers (LoL): Adaptively Ordering Transformer Layers at Runtime](https://arxiv.org/abs/2611.03526v1) | 2611.03526v1 | 0 |
| 2026-11-02 | [RASP: Read-All, Sparse-Plasticity Continual Learning in a Stationary-Size LoRA](https://arxiv.org/abs/2611.03513v1) | 2611.03513v1 | 0 |
| 2026-11-02 | [NormMoX: A Normative Mixture of Experts for Explainable Autism Classification from Structural and Functional MRI](https://arxiv.org/abs/2611.03349v1) | 2611.03349v1 | 6 |
| 2026-11-02 | [VideoEditor-MoE: Scaling Complex Video Editing with Mixture of Experts](https://arxiv.org/abs/2611.03043v1) | 2611.03043v1 | 7 |
| 2026-11-02 | [VioTech: Frame-Level Violin Playing Technique Detection with Multi-Scale Mixture-of-Experts](https://arxiv.org/abs/2611.02680v1) | 2611.02680v1 | 6 |
| 2026-11-02 | [MAPO: Mixture of Experts with Alternating Policy Optimization for Universal Humanoid Motion Tracking](https://arxiv.org/abs/2611.02613v1) | 2611.02613v1 | 6 |
| 2026-11-01 | [MatMoE: Matryoshka Mixture-of-Experts with Dynamic Mixed-Precision Quantization for Efficient Inference](https://arxiv.org/abs/2611.01704v1) | 2611.01704v1 | 6 |
| 2026-11-01 | [When Does Sparse Routing Help? The Geometry of Expert Separation in Mixture of Experts](https://arxiv.org/abs/2611.01602v1) | 2611.01602v1 | 6 |
| 2026-10-30 | [PRISM-Net: Dynamic Routing Network with VLM-Guided Disentangled Attribute Distillation for Explainable Fine-Grained Product Retrieval](https://arxiv.org/abs/2611.00458v1) | 2611.00458v1 | 0 |
| 2026-10-30 | [Decomposing Irregular Time Series into Interpretable Temporal Patterns with Mixture-of-Experts](https://arxiv.org/abs/2611.00337v1) | 2611.00337v1 | 6 |
| 2026-10-29 | [Characterizing Recoverable Expert-Utilization Signatures in Fine-Tuned Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.41039v1) | 2610.41039v1 | 6 |
| 2026-10-29 | [Multi-View Latent MoE: Letting Every Router Shape Expert Computation](https://arxiv.org/abs/2610.40577v2) | 2610.40577v2 | 3 |
| 2026-10-29 | [Softmax Routing Dynamics in Mixture-of-Experts Models: Collapse and Recovery](https://arxiv.org/abs/2610.39442v1) | 2610.39442v1 | 6 |
| 2026-10-28 | [CalibCause: A Quality-Gated, Interpretable and Calibrated Deep Learning Framework for Diabetic Retinopathy Grading](https://arxiv.org/abs/2610.40699v1) | 2610.40699v1 | 0 |
| 2026-10-28 | [Nemotron 3.5 Super and Lightning: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Models for Agentic AI](https://arxiv.org/abs/2610.38095v1) | 2610.38095v1 | 6 |
| 2026-10-27 | [Muon Makes the First Mixture-of-Experts Layer Harder to Balance](https://arxiv.org/abs/2610.37914v1) | 2610.37914v1 | 6 |
| 2026-10-27 | [Channel Selection for Mixture-of-Experts Decoding Needs No Calibration Data](https://arxiv.org/abs/2610.37386v1) | 2610.37386v1 | 6 |
| 2026-10-27 | [Agent-Conditioned Routing: Diverse Reasoning Paths Within One Frozen Model](https://arxiv.org/abs/2610.37375v1) | 2610.37375v1 | 0 |
| 2026-10-26 | [INC-MoE: Overlapping In-Network Collectives and Expert Computation for Expert-Parallel Mixture-of-Experts Inference](https://arxiv.org/abs/2610.36339v1) | 2610.36339v1 | 6 |
| 2026-10-26 | [DuplexTune: Coupled-State Replay for Memory-Efficient Mixture-of-Experts Adaptation](https://arxiv.org/abs/2610.36009v1) | 2610.36009v1 | 6 |
| 2026-10-26 | [Prefetch-Steered Routing: Deterministic Cache-Aware Expert Selection for Offloaded Mixture-of-Experts Decoding](https://arxiv.org/abs/2610.34721v1) | 2610.34721v1 | 6 |
| 2026-10-25 | [HobbyLM: A Sparse Mixture-of-Experts Model Family on a Hobby Budget](https://arxiv.org/abs/2610.34582v1) | 2610.34582v1 | 6 |
| 2026-10-25 | [Speculative Decoding for Mixture-of-Experts Models: Expert Bytes, Kernel Bandwidth and the Best Draft Length](https://arxiv.org/abs/2610.34440v1) | 2610.34440v1 | 6 |
| 2026-10-24 | [FedSEAM: Federated Continual Learning of LLMs via Subspace Expert Agreement Merging](https://arxiv.org/abs/2610.33496v1) | 2610.33496v1 | 0 |
| 2026-10-24 | [COPE: Composable Performance Emulation for Mixture-of-Experts Offloading Policies](https://arxiv.org/abs/2610.33404v1) | 2610.33404v1 | 6 |
| 2026-10-23 | [EDWARD-NMT: Elastic Dimensions With Adaptive Routing and Dual-consistency for Neural Machine Translation](https://arxiv.org/abs/2610.32115v1) | 2610.32115v1 | 0 |
| 2026-10-22 | [F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation](https://arxiv.org/abs/2610.31623v1) | 2610.31623v1 | 0 |
| 2026-10-22 | [ProQuant: Preserving Expert Quality over Quantity in Ultra-Low-Bit Quantization of Mixture-of-Experts Models](https://arxiv.org/abs/2610.30779v1) | 2610.30779v1 | 6 |
| 2026-10-22 | [SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation](https://arxiv.org/abs/2610.30732v1) | 2610.30732v1 | 6 |
| 2026-10-21 | [MoEZip: Routing-Aware KV Cache Compression for Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.30206v1) | 2610.30206v1 | 6 |
| 2026-10-21 | [A Strong MoE Is All You Need for Process Supervision](https://arxiv.org/abs/2610.29498v1) | 2610.29498v1 | 0 |
| 2026-10-21 | [CertMoE: Robustness Certification for Mixture-of-Experts LLMs via Routing-Aware Smoothing](https://arxiv.org/abs/2610.29395v1) | 2610.29395v1 | 6 |
| 2026-10-21 | [GaP-MoE : Explicit Expert Specialization in Mixture-of-Experts via Orthogonal Gradient Accumulation and Projection](https://arxiv.org/abs/2610.29355v1) | 2610.29355v1 | 6 |
| 2026-10-20 | [The Router Already Knows](https://arxiv.org/abs/2610.27421v1) | 2610.27421v1 | 3 |
| 2026-10-19 | [Reconstruction-Optimized Expert Pruning for Mixture-of-Experts Language Models](https://arxiv.org/abs/2610.27123v1) | 2610.27123v1 | 6 |
| 2026-10-19 | [An Empirical Study of Parameter-Efficient Fine-Tuning for Mixture-of-Experts LLMs](https://arxiv.org/abs/2610.26370v1) | 2610.26370v1 | 6 |
| 2026-10-19 | [Map-Distribution Mixture-of-Experts for Multi-Agent Pathfinding](https://arxiv.org/abs/2610.25991v1) | 2610.25991v1 | 6 |
| 2026-10-19 | [3D-MoE: Complementarity-Guided Hardware-Software Co-Design for MoE Decode on 3D-Stacked NMP](https://arxiv.org/abs/2610.26991v1) | 2610.26991v1 | 0 |
| 2026-10-19 | [Towards Architectural-Level Safety Control: Relocating Hazardous Knowledge into Removable Experts in Mixture-of-Experts Models](https://arxiv.org/abs/2610.25791v1) | 2610.25791v1 | 6 |
| 2026-10-19 | [Fine-Grained Units, Flat Decisions: Hierarchical Micro-Expert Pruning for Mixture-of-Experts Models](https://arxiv.org/abs/2610.25717v1) | 2610.25717v1 | 6 |
| 2026-10-16 | [TileDRAM: Compiler-Controlled Tile-to-DRAM Layouts for 3D DRAM GPGPUs](https://arxiv.org/abs/2610.23767v1) | 2610.23767v1 | 0 |
| 2026-10-16 | [ScoutRoute: Efficient Mixture-of-Experts Routing Using Internal Language Model Signals](https://arxiv.org/abs/2610.23443v1) | 2610.23443v1 | 6 |
| 2026-10-16 | [Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design](https://arxiv.org/abs/2610.23036v1) | 2610.23036v1 | 0 |
| 2026-10-16 | [Efficient CPU-GPU collaborative MoE inference via Adaptive Expert Assignment](https://arxiv.org/abs/2610.23006v1) | 2610.23006v1 | 0 |
| 2026-10-16 | [COMET: Decoupled Distillation, Routing, and Capacity Control for Task-Agnostic Continual Vision--Language Learning](https://arxiv.org/abs/2610.22907v1) | 2610.22907v1 | 0 |
| 2026-10-15 | [Rethinking Routing Exploration in Modern Mixture-of-Experts](https://arxiv.org/abs/2610.22353v1) | 2610.22353v1 | 6 |
| 2026-10-15 | [Explaining the Roles of Experts in Mixture-of-Experts LLMs for Personalization](https://arxiv.org/abs/2610.22127v1) | 2610.22127v1 | 6 |
| 2026-10-15 | [Router Drift Control: Mitigating Off-Policy Degradation in Mixture-of-Experts Reinforcement Learning](https://arxiv.org/abs/2610.21682v2) | 2610.21682v2 | 9 |
| 2026-10-15 | [DPA-MoE: A Runtime Precision Control Framework for MoE Inference](https://arxiv.org/abs/2610.21378v1) | 2610.21378v1 | 0 |
| 2026-10-14 | [A Mixture-of-Experts Framework for Multi-Stream Quickest Change Detection](https://arxiv.org/abs/2610.20876v1) | 2610.20876v1 | 6 |
| 2026-10-14 | [Task-Phase-Conditioned Expert Routing Is Not a Reliable Proxy for Quantization Sensitivity in MoE FFN Tensors](https://arxiv.org/abs/2610.20826v1) | 2610.20826v1 | 6 |
| 2026-10-14 | [OrionMoE-v1.0: A Mixture-of-Experts Foundation Model for Tabular In-Context Learning](https://arxiv.org/abs/2610.20418v2) | 2610.20418v2 | 6 |
| 2026-10-14 | [Cortex: Consolidating Context into Parametric Memory](https://arxiv.org/abs/2610.20399v1) | 2610.20399v1 | 0 |
| 2026-10-14 | [Scaling Multilingual Mixture-of-Experts: How Language Coverage Changes Capacity and Compute Allocation](https://arxiv.org/abs/2610.20247v3) | 2610.20247v3 | 7 |
| 2026-10-14 | [MAEM: Mitigating Recency Bias via a Replay-Free, Capacity-Controlled Dynamic Mixture of Experts for Class-Incremental Graph Learning](https://arxiv.org/abs/2610.20238v1) | 2610.20238v1 | 6 |
| 2026-10-13 | [Spectral-MoE: Heterogeneous Per-Layer Expert Utilization in Dense-to-MoE Conversion](https://arxiv.org/abs/2610.19232v1) | 2610.19232v1 | 0 |
| 2026-10-13 | [How Many Ranks Does a Token Need? A Noise-Floor Squelch for Rank-One LoRA Experts](https://arxiv.org/abs/2610.19033v1) | 2610.19033v1 | 0 |
| 2026-10-13 | [PixelMoE: Scaling Pixel-Space Diffusion with LLM-Style Mixture-of-Experts](https://arxiv.org/abs/2610.18857v3) | 2610.18857v3 | 7 |
| 2026-10-13 | [UniW(A)M: A Unified Mixture-of-Experts Framework for World and World-Action Models](https://arxiv.org/abs/2610.18697v2) | 2610.18697v2 | 6 |
| 2026-10-13 | [Revisiting Cauchy-Schwarz Norm Bounds for SDC Detection in LLM Inference](https://arxiv.org/abs/2610.18557v3) | 2610.18557v3 | 0 |
| 2026-10-11 | [Towards Robust Calibration Dataset for Domain-General Mixture of Experts Pruning](https://arxiv.org/abs/2610.15578v1) | 2610.15578v1 | 11 |
| 2026-10-10 | [Sparsity Saves Compute, Not Samples: Oracle Inequalities for Dense and Sparse Mixture of Experts](https://arxiv.org/abs/2610.15039v1) | 2610.15039v1 | 10 |
| 2026-10-10 | [Shaping Latent Mixture-of-Experts: From Expert Geometry to Layerwise Capacity Allocation](https://arxiv.org/abs/2610.14644v1) | 2610.14644v1 | 6 |
| 2026-10-09 | [DuoRate: Two-Rate Per-Expert Precision Allocation for Mixture-of-Experts Serving](https://arxiv.org/abs/2610.13328v1) | 2610.13328v1 | 8 |
| 2026-10-09 | [TAME-Nav: Temporal Asymmetric Mixture-of-Experts Distillation for Agile and Versatile Robot Navigation](https://arxiv.org/abs/2610.12877v1) | 2610.12877v1 | 14 |
| 2026-10-08 | [Cost-Aware Mixture-of-Experts Coordination for Model Markets](https://arxiv.org/abs/2610.11908v1) | 2610.11908v1 | 6 |
| 2026-10-08 | [RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing](https://arxiv.org/abs/2610.11775v1) | 2610.11775v1 | 13 |
| 2026-10-08 | [Smoothing the Top-k Exposure Boundary for Sparse Mixture-of-Experts](https://arxiv.org/abs/2610.11575v3) | 2610.11575v3 | 10 |
| 2026-10-08 | [WARP-VLA: Wrist-Camera Adaptation for View-Robust Policy Execution in Vision-Language-Action Models](https://arxiv.org/abs/2610.11508v2) | 2610.11508v2 | 6 |
| 2026-10-08 | [Zepp: Accelerating Distributed MoE Serving under Relaxed Balance Constraints](https://arxiv.org/abs/2610.11158v2) | 2610.11158v2 | 8 |
| 2026-10-07 | [When Routing Reveals Membership: Privacy Leakage from MoE Router Telemetry](https://arxiv.org/abs/2610.10616v1) | 2610.10616v1 | 7 |
| 2026-10-07 | [Expert Coupling in MoE Pretraining: Reducing All-to-All Overhead with Correlated Placement and Token Shuffling](https://arxiv.org/abs/2610.09372v1) | 2610.09372v1 | 8 |
| 2026-10-07 | [Shared Low-rank Basis Factorization for Data-free Mixture-of-Experts Compression](https://arxiv.org/abs/2610.09342v1) | 2610.09342v1 | 6 |
| 2026-10-06 | [Beyond the Leaderboard: Multi-Dimensional Evaluation of Dense and Mixture-of-Experts Models for Automated Program Repair](https://arxiv.org/abs/2610.08173v1) | 2610.08173v1 | 6 |
| 2026-10-06 | [MASKerade: Token-Routed Mask Experts for Dense-to-MoE Upcycling](https://arxiv.org/abs/2610.07809v1) | 2610.07809v1 | 8 |
| 2026-10-06 | [Adaptive Mean Estimation by In-Context Learning: A Gradient-Flow Analysis](https://arxiv.org/abs/2610.07804v1) | 2610.07804v1 | 6 |
| 2026-10-06 | [Reading, Not Manipulating: Leveraging Router Logits for Multimodal Safety in MoE Vision-Language Models](https://arxiv.org/abs/2610.07774v1) | 2610.07774v1 | 11 |
| 2026-10-06 | [Anchor-driven Multi-modal Multi-scale Expert Selection for Survival Prediction](https://arxiv.org/abs/2610.07694v1) | 2610.07694v1 | 8 |
| 2026-10-05 | [Memory-Efficient Expert Routing for Distributed MoE Training](https://arxiv.org/abs/2610.07333v1) | 2610.07333v1 | 12 |
| 2026-10-05 | [Structuring MoE Expert Selection for Agentic Reinforcement Learning](https://arxiv.org/abs/2610.07332v1) | 2610.07332v1 | 8 |
| 2026-10-05 | [Cascadia: Resident 975B MoE Inference on Eleven AI PCs](https://arxiv.org/abs/2610.07219v1) | 2610.07219v1 | 7 |
| 2026-10-05 | [Distributionally Robust Mixture-of-Experts Training](https://arxiv.org/abs/2610.07207v1) | 2610.07207v1 | 7 |
| 2026-10-05 | [BRANCH-MoE: Balance-Aware Tree Routing for Large Embedding Models](https://arxiv.org/abs/2610.06725v1) | 2610.06725v1 | 6 |
| 2026-10-05 | [How Sparse Probability Maps Shape Mixture-of-Experts Routing](https://arxiv.org/abs/2610.06677v1) | 2610.06677v1 | 8 |
| 2026-10-05 | [The Arbitrary-Placement Problem in Entropy-Minimizing Selection, and a Residual-Entropy Formulation](https://arxiv.org/abs/2610.05925v1) | 2610.05925v1 | 6 |
| 2026-10-05 | [CIPHER-MoE: Balancing Efficiency and Routing Fidelity in Trillion-Scale MoE Training](https://arxiv.org/abs/2610.05744v1) | 2610.05744v1 | 7 |
| 2026-10-04 | [RoMod: Temporal Routing Modulation via Mixture-of-Experts for Video Anomaly Detection](https://arxiv.org/abs/2610.05131v1) | 2610.05131v1 | 6 |
| 2026-10-04 | [HiNa-MoE: High-Performance, Non-Intrusive MoE Inference on CPUs with Matrix Engines](https://arxiv.org/abs/2610.05123v1) | 2610.05123v1 | 6 |
| 2026-10-04 | [LoopMoEVR: Loop-Based Degradation-Aware Mixture-of-Experts for Unified UHD Video Restoration](https://arxiv.org/abs/2610.05109v1) | 2610.05109v1 | 6 |
| 2026-10-03 | [Principled Top-$k$ Selection for Language Models with Hybrid Gradients](https://arxiv.org/abs/2610.04162v1) | 2610.04162v1 | 8 |
| 2026-10-02 | [ExpertMuon-Compass: Alignment-Guided Step Sizes for Mixture-of-Experts Training](https://arxiv.org/abs/2610.04140v1) | 2610.04140v1 | 8 |
| 2026-10-02 | [RailWave: Adaptive Spatial and Temporal Scheduling for Expert-Parallel Communication](https://arxiv.org/abs/2610.03415v1) | 2610.03415v1 | 8 |
| 2026-10-02 | [AFORE: Attention-FFN Disaggregation with Overlapped Reconfiguration of Experts](https://arxiv.org/abs/2610.03203v1) | 2610.03203v1 | 6 |
| 2026-10-02 | [Frequency Is Not Sensitivity Identifying Safety-Sensitive Experts in Sparse MoE LLM](https://arxiv.org/abs/2610.02910v1) | 2610.02910v1 | 6 |
| 2026-10-02 | [Conditional Capacity and Routing in Mixture-of-Experts Particle Transformers](https://arxiv.org/abs/2610.02701v2) | 2610.02701v2 | 10 |
| 2026-10-01 | [Dense Mixture-of-Experts as a Reparameterized Wide FFN: A Granularity Sweep at Fixed Compute](https://arxiv.org/abs/2610.02584v1) | 2610.02584v1 | 9 |
| 2026-10-01 | [Harnessing Domain Specialists in Multimodal Mixture-of-Experts for Efficient Adaptation](https://arxiv.org/abs/2610.02123v1) | 2610.02123v1 | 8 |
| 2026-10-01 | [Cross-Lingual Alignment for Decoder-Only Models using MoE Routers](https://arxiv.org/abs/2610.01921v2) | 2610.01921v2 | 7 |
| 2026-10-01 | [SpikeMoE: Brain-Inspired Competitive Routing for Flexible Spiking Mixture-of-Experts](https://arxiv.org/abs/2610.01418v2) | 2610.01418v2 | 12 |
| 2026-09-30 | [MegaFlux: Skew-Resilient MoE Megakernels via Pipelined Expert Replication](https://arxiv.org/abs/2610.00671v1) | 2610.00671v1 | 6 |
| 2026-09-30 | [Scaling Laws for Looped Mixture of Experts](https://arxiv.org/abs/2609.40316v1) | 2609.40316v1 | 11 |
| 2026-09-30 | [Raw-Routed Mixture of Adapters: A Causal Intervention for Routing Collapse in Time Series Foundation Models](https://arxiv.org/abs/2609.39445v1) | 2609.39445v1 | 6 |
| 2026-09-30 | [HAPMoE: Heterogeneity-Aware Automatic Parallelism Planning for Mixture-of-Experts Models Training](https://arxiv.org/abs/2609.39350v1) | 2609.39350v1 | 6 |
| 2026-09-30 | [UniAE-MoE: A Unified Audio Encoder via Mixture of Experts](https://arxiv.org/abs/2609.39199v2) | 2609.39199v2 | 13 |
| 2026-09-30 | [MoRA: MoE Pruning via Router Bias Learning and Expert Approximation](https://arxiv.org/abs/2610.00367v1) | 2610.00367v1 | 8 |
| 2026-09-30 | [RouteRec: Behavior-Guided Sparse Routing for Sequential Recommendation](https://arxiv.org/abs/2609.39007v1) | 2609.39007v1 | 7 |
| 2026-09-30 | [DecoMoE: Decoupling Visual Propagation and Expert Computation for Efficient Multimodal MoE Inference](https://arxiv.org/abs/2609.38823v1) | 2609.38823v1 | 8 |
| 2026-09-29 | [Mira: Memory-Efficient MoE Inference Using Adaptive Caching and Predictive Expert Staging](https://arxiv.org/abs/2609.38090v1) | 2609.38090v1 | 7 |
| 2026-09-29 | [DIET: Deletion-response Expert Trimming for Video Diffusion Transformers](https://arxiv.org/abs/2609.37829v1) | 2609.37829v1 | 6 |
| 2026-09-29 | [Cross-Entropy Guided Routing in Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2609.37751v1) | 2609.37751v1 | 12 |
| 2026-09-29 | [E-MoE: Enhanced Mixture-of-Experts for Non-Factorized Diffusion Language Models](https://arxiv.org/abs/2609.37533v1) | 2609.37533v1 | 6 |
| 2026-09-29 | [Hardware-Native Joint Sparse-Quantization for Trillion-Scale Mixture-of-Experts](https://arxiv.org/abs/2610.02241v1) | 2610.02241v1 | 8 |
| 2026-09-29 | [Routing in Gradient Space: Balanced Usage Is Not Expert Specialization](https://arxiv.org/abs/2609.36724v1) | 2609.36724v1 | 8 |
| 2026-09-28 | [MoRE: Scaling mixture of experts with hardware-aware low-rank routing](https://arxiv.org/abs/2609.36301v1) | 2609.36301v1 | 13 |
| 2026-09-28 | [BASE: Batch-Aware Selection of Experts Using Predicted Removal Error for Efficient MoE Decoding](https://arxiv.org/abs/2609.36222v1) | 2609.36222v1 | 6 |
| 2026-09-28 | [How to Loop MoE: Flatten the Experts, Untie the Attention](https://arxiv.org/abs/2609.35751v1) | 2609.35751v1 | 6 |
| 2026-09-28 | [TopoEP: Topology-Aware Load Balancing for Expert-Parallel MoE Training](https://arxiv.org/abs/2609.35481v1) | 2609.35481v1 | 10 |
| 2026-09-28 | [Role-Guided MOE for Encoder-Level Pathology Representation Learning in WSI Classification](https://arxiv.org/abs/2609.34897v1) | 2609.34897v1 | 6 |
| 2026-09-28 | [A Persistent State for Auditable Mixture-of-Experts Routing](https://arxiv.org/abs/2609.34634v1) | 2609.34634v1 | 8 |
| 2026-09-28 | [SAGE: Subspace Alignment for Classifier-Free Guidance in Mixture-of-Experts Diffusion Models](https://arxiv.org/abs/2609.34525v1) | 2609.34525v1 | 7 |
| 2026-09-28 | [MaskCoFT: Masked Co-Adaptive Fine-Tuning for Memory-Efficient MoE Inference](https://arxiv.org/abs/2609.34077v2) | 2609.34077v2 | 8 |
| 2026-09-27 | [Domain-Adaptive Dual-Gating Mixture of Experts for Generalizable Speech Deepfake Detection](https://arxiv.org/abs/2609.33709v1) | 2609.33709v1 | 10 |
| 2026-09-27 | [OLED-MoE: Accelerating MoE-Based dLLM Inference via Inter-Iteration Locality-Aware Expert Offloading](https://arxiv.org/abs/2609.33385v1) | 2609.33385v1 | 9 |
| 2026-09-27 | [CascadeEP: Asynchronous Expert Execution for MoE Prefill under Attention Imbalance](https://arxiv.org/abs/2609.33252v1) | 2609.33252v1 | 6 |
| 2026-09-27 | [OneSign: Unifying Sign Language Understanding Tasks with One Model](https://arxiv.org/abs/2609.33090v1) | 2609.33090v1 | 6 |
| 2026-09-27 | [CipherGenome: Homomorphic Inference for Genomic Mixture-of-Experts](https://arxiv.org/abs/2609.35883v2) | 2609.35883v2 | 10 |
| 2026-09-27 | [GenomeOcean Anywhere: Private WebGPU Inference for Genome MoEs](https://arxiv.org/abs/2609.35882v2) | 2609.35882v2 | 6 |
| 2026-09-26 | [Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs](https://arxiv.org/abs/2609.32821v1) | 2609.32821v1 | 10 |
| 2026-09-26 | [OmniMoE-VL: A Sparse Vision-Language Model with Coupled Visual-Depth Routing](https://arxiv.org/abs/2609.32780v1) | 2609.32780v1 | 8 |
| 2026-09-26 | [Kairos: Toward a Byte-Level Foundation Model for Every Modality](https://arxiv.org/abs/2610.12495v1) | 2610.12495v1 | 6 |
| 2026-09-26 | [HERO-MoE: Historical Expert Routing with Scale-Preserving Fusion](https://arxiv.org/abs/2609.32581v1) | 2609.32581v1 | 12 |
| 2026-09-25 | [Resource-Aware Federated Mixture-of-Experts with Adaptive Pruning for Onboard Learning in LEO Satellite Constellations](https://arxiv.org/abs/2609.31932v1) | 2609.31932v1 | 10 |
| 2026-09-25 | [EviDETR: Preserving Query-Relevant Temporal Evidence for Moment Retrieval and Highlight Detection](https://arxiv.org/abs/2609.30724v1) | 2609.30724v1 | 12 |
| 2026-09-24 | [RAZOR: Pruning Replaceable Experts in LLMs](https://arxiv.org/abs/2609.30465v4) | 2609.30465v4 | 6 |
| 2026-09-23 | [Exact Quantile Balancing and Load-Error Injection for Mixture-of-Experts](https://arxiv.org/abs/2609.28053v1) | 2609.28053v1 | 8 |
| 2026-09-22 | [Logit-Aware MIMO AirComp for Distributed Mixture-of-Experts LLM Inference over Wireless Edge Networks](https://arxiv.org/abs/2610.03741v1) | 2610.03741v1 | 10 |
| 2026-09-22 | [Unlocking Cross-Scenario Physical Layer Security: A Mixture-of-Experts Framework with Generative Diffusion Models](https://arxiv.org/abs/2609.26598v1) | 2609.26598v1 | 6 |
| 2026-09-22 | [C2FXNet: Coarse-to-Fine Scene Expert for Unified Object Detection across Adverse Weather](https://arxiv.org/abs/2609.25693v1) | 2609.25693v1 | 6 |
| 2026-09-21 | [MECT: Mixture of Experts with CNN-Transformer Network for Speaker verification](https://arxiv.org/abs/2609.24061v1) | 2609.24061v1 | 10 |
| 2026-09-21 | [All-in-One Multilingual Scene Text Recognition with Script-aware Mixture-of-Experts](https://arxiv.org/abs/2609.24058v1) | 2609.24058v1 | 8 |
| 2026-09-18 | [Efficient Mixture-of-Experts with Speculative Decoding via Expert Coactivation](https://arxiv.org/abs/2609.22471v1) | 2609.22471v1 | 8 |
| 2026-09-18 | [Accelerating Dense LLMs via L0-regularized Mixture-of-Experts](https://arxiv.org/abs/2609.21672v1) | 2609.21672v1 | 6 |
| 2026-09-18 | [IntBMoE: Integrating Block-Level Conditioning into Expert Composition for Full-Participation Mixture-of-Experts](https://arxiv.org/abs/2609.21346v1) | 2609.21346v1 | 8 |
| 2026-09-17 | [Attention-Aware Routing: Coupling Routing and Attention in MoEs](https://arxiv.org/abs/2609.20974v1) | 2609.20974v1 | 6 |
| 2026-09-17 | [OceanMoE: Structured Conditional Sparse Computation for Long-Horizon Multivariate Ocean Forecasting](https://arxiv.org/abs/2609.19768v1) | 2609.19768v1 | 6 |
| 2026-09-16 | [Higher-order pruning of experts in mixture-of-experts language models](https://arxiv.org/abs/2609.18916v3) | 2609.18916v3 | 6 |
| 2026-09-16 | [Infinite-Parameter LLMs: Generating and Adapting Weights from Live Data](https://arxiv.org/abs/2609.18842v2) | 2609.18842v2 | 7 |
| 2026-09-16 | [Generalist-Specialist Mixture-of-Experts for Rare Pathology Detection in Multimodal Imaging](https://arxiv.org/abs/2609.18688v1) | 2609.18688v1 | 6 |
| 2026-09-16 | [Occluded Gait Recognition with Mixture of Experts: An Action Detection Perspective](https://arxiv.org/abs/2609.18432v1) | 2609.18432v1 | 6 |
| 2026-09-16 | [MoRE: Mixture of Reused Experts](https://arxiv.org/abs/2609.18176v2) | 2609.18176v2 | 6 |
| 2026-09-16 | [Multi-View Mixture-of-Experts with Vision-Language Reranking for Cross-View Object Geo-Localization](https://arxiv.org/abs/2609.18139v1) | 2609.18139v1 | 6 |
| 2026-09-16 | [The Other Half of the Memory Wall: Serving 35B MoEs from SSD with Trained Routing Prediction](https://arxiv.org/abs/2609.18063v2) | 2609.18063v2 | 6 |
| 2026-09-16 | [CoAtNet-DeepMoE: A Convolution-Attention Hybrid with DeepSeek Mixture-of-Experts for Parameter-Efficient Tomato Disease Classification](https://arxiv.org/abs/2609.18038v1) | 2609.18038v1 | 10 |
| 2026-09-15 | [Beyond the Previous Layer: Residual Predictive Structure in Sparse MoE Routing](https://arxiv.org/abs/2609.17940v1) | 2609.17940v1 | 6 |
| 2026-09-15 | [Unifying Semantic Priors and High-Frequency Traces: Enhancing V-JEPA with Mixture-of-Experts for Robust Synthetic Image Forensics](https://arxiv.org/abs/2609.16778v2) | 2609.16778v2 | 6 |
| 2026-09-15 | [Dense to MoE Adaptation for Compact Vision Language Action Policies](https://arxiv.org/abs/2609.16503v2) | 2609.16503v2 | 6 |
| 2026-09-14 | [STHMoE: Hypergraph-Enhanced Heterogeneous Dependency Coordination for LLM-Based Urban Traffic Data Forecasting](https://arxiv.org/abs/2609.15172v1) | 2609.15172v1 | 10 |
| 2026-09-12 | [Multi-Modal Tumor Survival Prediction via Graph-Guided Mixture of Experts](https://arxiv.org/abs/2609.14072v1) | 2609.14072v1 | 6 |
| 2026-09-11 | [Mixture-of-Experts Language Models Can Be Strong and Efficient Retrievers](https://arxiv.org/abs/2609.13486v1) | 2609.13486v1 | 6 |
| 2026-09-11 | [Task-Aware Federated Fine-Tuning for MoE-based Large Language Models](https://arxiv.org/abs/2609.13395v1) | 2609.13395v1 | 8 |
| 2026-09-11 | [Expert-Space Exploration in MoE Reinforcement Learning](https://arxiv.org/abs/2609.13058v1) | 2609.13058v1 | 10 |
| 2026-09-11 | [ExpertHTR: Unified Handwritten Text Recognition with Multi-Task Learning and Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.12705v1) | 2609.12705v1 | 10 |
| 2026-09-11 | [Quality-Constrained Routing over a Fixed Pool of Quantized Mixture-of-Experts Instances](https://arxiv.org/abs/2609.12550v1) | 2609.12550v1 | 6 |
| 2026-09-09 | [OMP-MoE: Efficient Expert Pruning for Mixture-of-Experts LLMs via Orthogonal Matching Pursuit](https://arxiv.org/abs/2609.31631v2) | 2609.31631v2 | 7 |
| 2026-09-08 | [HDA-MoE: Hybrid Parallelism and Dynamic, Adaptive Scheduling for Mixture-of-Experts with 3D Near-Memory Processing](https://arxiv.org/abs/2609.08682v1) | 2609.08682v1 | 7 |
| 2026-09-08 | [MoEMB: Scaling Universal Multimodal Embeddings with Efficient Mixture-of-Experts Models](https://arxiv.org/abs/2609.08663v2) | 2609.08663v2 | 7 |
| 2026-09-08 | [Distribution-Consistent Inference for Dynamic Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.09241v1) | 2609.09241v1 | 7 |
| 2026-09-08 | [Router Prior Bias: Preserving Base Routing Structure in MoE Post-Training](https://arxiv.org/abs/2609.08115v1) | 2609.08115v1 | 7 |
| 2026-09-07 | [MI-PEFT: Mixture-of-Experts Integrated Parameter-Efficient Fine-Tuning Protein Language Models Improves Acidophilic Proteins Classification](https://arxiv.org/abs/2609.08059v1) | 2609.08059v1 | 6 |
| 2026-09-07 | [Latent-MoE: Domain-Aware Mixture-of-Experts for PDEs with Multi-Regime Physics](https://arxiv.org/abs/2609.07814v1) | 2609.07814v1 | 8 |
| 2026-09-07 | [Analytical Resource Management for Fine-grained MoE Computation-Communication Overlap](https://arxiv.org/abs/2609.07536v1) | 2609.07536v1 | 6 |
| 2026-09-07 | [Distance-Aware Attention and Wall-Distance Expert Routing for Transformer-Based 3D Flow Prediction](https://arxiv.org/abs/2609.07222v1) | 2609.07222v1 | 12 |
| 2026-09-05 | [ExpertLens: Visualizing Embedding Spaces for Post-Hoc Explainability in MoE Enhanced Retrievers](https://arxiv.org/abs/2609.06155v1) | 2609.06155v1 | 8 |
| 2026-09-04 | [RAPTOR: Role-Aware Private Training for Mixture-of-Experts](https://arxiv.org/abs/2609.05770v1) | 2609.05770v1 | 10 |
| 2026-09-04 | [ACE: Adaptive Calibration-Free Expert Skipping for MoE-based LLMs](https://arxiv.org/abs/2609.05228v1) | 2609.05228v1 | 9 |
| 2026-09-04 | [Cache-Aware Joint Router Adaptation for Memory-Efficient MoE Inference](https://arxiv.org/abs/2609.04895v2) | 2609.04895v2 | 7 |
| 2026-09-04 | [ProtLingo: Efficient Protein Language Modeling via Conditional Memory and Expert Routing](https://arxiv.org/abs/2609.04793v1) | 2609.04793v1 | 16 |
| 2026-09-04 | [Training-Free Halving of Activated Experts in Fine-Grained Mixture-of-Experts Models](https://arxiv.org/abs/2609.04575v1) | 2609.04575v1 | 8 |
| 2026-09-03 | [When Load-Balancing Goes Too Far: Expert Pruning in Over-Dispersed Mixture-of-Experts Models](https://arxiv.org/abs/2609.04453v1) | 2609.04453v1 | 8 |
| 2026-09-03 | [Towards a Statistical Understanding of Mixture-of-Experts](https://arxiv.org/abs/2609.03501v1) | 2609.03501v1 | 10 |
| 2026-09-02 | [Evidence for Shared Routing Geometry and Dynamics in Sparse Mixture-of-Experts](https://arxiv.org/abs/2609.02404v1) | 2609.02404v1 | 8 |
| 2026-09-02 | [SEAL: Reinforcing Global Safety in Mixture-of-Experts through Shared Expert ALignment](https://arxiv.org/abs/2609.02293v1) | 2609.02293v1 | 9 |
| 2026-09-02 | [TAME: Temporal-Aware Mixture-of-Experts for Text-Video Retrieval](https://arxiv.org/abs/2609.02204v1) | 2609.02204v1 | 6 |
| 2026-09-01 | [Beyond Magnitude: Contrastive Routing for Modular Mixture-of-Experts](https://arxiv.org/abs/2609.01100v1) | 2609.01100v1 | 6 |
| 2026-09-01 | [Residual Sparsification via Output Importance for Compressing Mixture-of-Experts LLMs](https://arxiv.org/abs/2609.00575v2) | 2609.00575v2 | 6 |
| 2026-08-31 | [WiSDoM: Wireless Sparse Decision Transformer with Mixture-of-Experts for Multi-Task Mobile Network Optimization](https://arxiv.org/abs/2609.00284v1) | 2609.00284v1 | 10 |
| 2026-08-31 | [Q-Strata: Hierarchical Bit Allocation for Mixed-Precision Quantization of Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.30564v1) | 2608.30564v1 | 6 |
| 2026-08-30 | [Evolutionary Soups: Evolving Mixture-of-Experts for Multi-Objective LLM Alignment](https://arxiv.org/abs/2608.29978v1) | 2608.29978v1 | 6 |
| 2026-08-30 | [Structure Aware Neural Architecture Search for Mixture of Experts](https://arxiv.org/abs/2608.29817v1) | 2608.29817v1 | 10 |
| 2026-08-30 | [HiVe: Beyond Static Prompts for Multitask Learning via Hierarchy-based Vertical Mixture-of-Experts](https://arxiv.org/abs/2608.29790v2) | 2608.29790v2 | 6 |
| 2026-08-30 | [IMEX-FND: A Traceable Interaction-Aware Mixture-of-Experts Framework for Multimodal Fake News Detection](https://arxiv.org/abs/2609.29610v1) | 2609.29610v1 | 6 |
| 2026-08-29 | [WoE Wrote It? Watermarking Mixture-of-Experts LLMs for Black-Box Text Provenance](https://arxiv.org/abs/2608.29151v1) | 2608.29151v1 | 6 |
| 2026-08-28 | [Training Communication-Efficient Mixture-of-Experts Language Models with Layer Re-Configuration](https://arxiv.org/abs/2608.28511v1) | 2608.28511v1 | 7 |
| 2026-08-28 | [FUSED: Forensic-Semantic Mixture-of-Experts for AI Inpainting Detection and Localization](https://arxiv.org/abs/2608.28302v1) | 2608.28302v1 | 6 |
| 2026-08-28 | [HARTS: A Prefix-Sharing Training System for Agentic RL with Hybrid-Attention Models](https://arxiv.org/abs/2608.28158v2) | 2608.28158v2 | 6 |
| 2026-08-27 | [MM-Spectrum: Multimodal Multi-spectral Molecular Structural Elucidation with a Stable MoE Framework](https://arxiv.org/abs/2608.27286v1) | 2608.27286v1 | 6 |
| 2026-08-27 | [Meta-Learning Where to Allocate Experts: Task-Conditioned Layer-Wise Compression for MoEs](https://arxiv.org/abs/2608.26650v1) | 2608.26650v1 | 6 |
| 2026-08-27 | [Launch-Bound and Substitutable: Why Three Inference Optimizations Fail to Pay Off in Mixture-of-Experts Models](https://arxiv.org/abs/2608.26612v2) | 2608.26612v2 | 8 |
| 2026-08-26 | [Robust CurveMoE: Multi-Norm Adversarial Defense for Mixture-of-Experts Models via Mode Connectivity](https://arxiv.org/abs/2608.26043v1) | 2608.26043v1 | 6 |
| 2026-08-26 | [Drift-Aware Multimodal User Representation Learning via Multi-Scale Temporal Modeling and Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.25773v1) | 2608.25773v1 | 6 |
| 2026-08-26 | [Mixture of Wide Experts: Sparse Routing for Interpretable Native Coordinates](https://arxiv.org/abs/2611.03655v1) | 2611.03655v1 | 6 |
| 2026-08-26 | [The Limits of Speculation: Bounding Speculative Decoding in Mixture-of-Experts](https://arxiv.org/abs/2609.22156v1) | 2609.22156v1 | 6 |
| 2026-08-26 | [Groundhog Bit-Flip Attack: Seeding Infinite Generation Loops in Mixture-of-Experts LLMs through Bit Flips](https://arxiv.org/abs/2608.25276v1) | 2608.25276v1 | 6 |
| 2026-08-25 | [The Von-Neumann State-Space Transformer for neural decoding](https://arxiv.org/abs/2608.25088v1) | 2608.25088v1 | 6 |
| 2026-08-25 | [MoTE: Mixture of Task Experts for Multi-Task Video Understanding](https://arxiv.org/abs/2608.24763v1) | 2608.24763v1 | 6 |
| 2026-08-25 | [A Heterogeneous Mixture of Experts Framework for Interpretable Machine Learning](https://arxiv.org/abs/2608.24195v1) | 2608.24195v1 | 10 |
| 2026-08-25 | [TransPhy: Visual In-Context Learning for Physically Grounded Image Editing](https://arxiv.org/abs/2608.24119v1) | 2608.24119v1 | 8 |
| 2026-08-24 | [Giga-Embeddings: Mixture-of-Experts Encoders for High-Throughput Text Embeddings](https://arxiv.org/abs/2608.23806v1) | 2608.23806v1 | 6 |
| 2026-08-24 | [DF-MoE: Generalizable Deepfake Detection via Multimodal Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.23363v1) | 2608.23363v1 | 6 |
| 2026-08-24 | [ExFold: Unified Expert Folding for Training-Free MoE Prefill-Decode Acceleration](https://arxiv.org/abs/2608.24938v1) | 2608.24938v1 | 8 |
| 2026-08-24 | [Optimize Surgical Triplet Recognition: A Knowledge-Driven Mixture-of-Experts Solution](https://arxiv.org/abs/2608.22972v1) | 2608.22972v1 | 6 |
| 2026-08-24 | [AirMoE: Realizing Over-the-Air Distributed Mixture-of-Experts Inference at the Wireless Edge](https://arxiv.org/abs/2608.22932v2) | 2608.22932v2 | 6 |
| 2026-08-24 | [Fairness-Aware Mixture-of-Experts via Subgroup Reweighting and Gate Regularization](https://arxiv.org/abs/2608.22820v1) | 2608.22820v1 | 6 |
| 2026-08-22 | [ViSMoE: Visual-Aware Sparse Mixture-of-Experts for Embodied Referring Expression Grounding](https://arxiv.org/abs/2608.21878v1) | 2608.21878v1 | 6 |
| 2026-08-22 | [More Experts, Worse Dynamics: Inverse Scaling and Spectral Bias in Mixture-of-Experts State-Space Models](https://arxiv.org/abs/2608.21840v1) | 2608.21840v1 | 7 |
| 2026-08-21 | [SAEM: Stage-Aware Expert Management for Memory-Efficient MoE Inference in Chain-of-Thought Reasoning](https://arxiv.org/abs/2608.21614v1) | 2608.21614v1 | 8 |
| 2026-08-21 | [RARE: Decoupling Representation Steering from Expert Routing in Mixture-of-Experts Language Models](https://arxiv.org/abs/2608.21236v1) | 2608.21236v1 | 14 |
| 2026-08-21 | [Fuzzy-MoE: Interpretable Regime-Conditioned Expert Routing for Non-Stationary Multivariate Time Series Forecasting](https://arxiv.org/abs/2608.20761v1) | 2608.20761v1 | 12 |
| 2026-08-20 | [From Urban Mobility to Epidemic Dynamics: A Mixture-of-Experts Framework with Preference Alignment for Policy Scenario Simulation](https://arxiv.org/abs/2608.20512v1) | 2608.20512v1 | 6 |
| 2026-08-19 | [MonoMoE: An Efficient Fused Mega-kernel for Quantized MoE Decoding](https://arxiv.org/abs/2609.04244v1) | 2609.04244v1 | 8 |
| 2026-08-18 | [Cacheable by Design? Training Mixture-of-Experts Routers for Locality Against the Edge Memory-Bandwidth Wall: A Pre-Registered Negative Result with a Systems Measurement Study](https://arxiv.org/abs/2608.18261v1) | 2608.18261v1 | 9 |
| 2026-08-18 | [Mixture-of-Expert Blocks Contain Strong Hallucination Detection Signals](https://arxiv.org/abs/2608.17687v1) | 2608.17687v1 | 6 |
| 2026-08-18 | [Beyond the Trace: Coupling an Interpretable Reasoning-State Readout to Native MoE Routing](https://arxiv.org/abs/2608.17638v2) | 2608.17638v2 | 6 |
| 2026-08-18 | [MoE-ViE: Mixture of Experts Vision Encoder for Efficient Image and Video Understanding](https://arxiv.org/abs/2608.17402v1) | 2608.17402v1 | 11 |
| 2026-08-18 | [MoFE: A Novel Mixture-of-Experts Framework with Fourier Neural Operators for Cryptocurrency Forecasting](https://arxiv.org/abs/2608.17342v1) | 2608.17342v1 | 6 |
| 2026-08-17 | [AdaSprite: Resource-efficient Online Co-Adaptation for V2I Systems Under Large-scale Data Drifts](https://arxiv.org/abs/2608.16188v1) | 2608.16188v1 | 13 |
| 2026-08-16 | [Routing Divergence Is Not Evidence of Behavioral Influence in Same-Weight MoE Self-Distillation](https://arxiv.org/abs/2608.15787v1) | 2608.15787v1 | 7 |
| 2026-08-16 | [THESIS-MoE: Trainable Hierarchical Extraction and SteerIng of Sycophancy in Mixture-of-Experts](https://arxiv.org/abs/2608.15687v1) | 2608.15687v1 | 6 |
| 2026-08-15 | [Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference](https://arxiv.org/abs/2608.15383v1) | 2608.15383v1 | 8 |
| 2026-08-15 | [MoE Router-Guided Clustering for Heterogeneous Federated Instruction Tuning](https://arxiv.org/abs/2608.15311v1) | 2608.15311v1 | 8 |
| 2026-08-15 | [A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models](https://arxiv.org/abs/2608.15102v2) | 2608.15102v2 | 12 |
| 2026-08-15 | [S2-MoE: Enabling Efficient Self-Speculative Decoding for Mixture-of-Experts on Edge Devices](https://arxiv.org/abs/2608.15018v2) | 2608.15018v2 | 6 |
| 2026-08-15 | [A Deterministic Constant-Competitive Algorithm for Dynamic Mixture-of-Experts Serving](https://arxiv.org/abs/2608.16947v2) | 2608.16947v2 | 6 |
| 2026-08-14 | [Mixture of experts surrogate model for the homogenization of open-porous materials](https://arxiv.org/abs/2608.14809v1) | 2608.14809v1 | 6 |
| 2026-08-14 | [FreeBalance: Pre-Routing Online Moe Load Balancing via Residual Workload Prediction](https://arxiv.org/abs/2608.14205v1) | 2608.14205v1 | 12 |
| 2026-08-13 | [Fine-Grained Action Recognition with Cross-Attentive Latent Sparse Experts](https://arxiv.org/abs/2608.13458v2) | 2608.13458v2 | 10 |
| 2026-08-12 | [Regime-Gated Residual Mixture-of-Experts for Cross-Sectional Volatility Forecasting](https://arxiv.org/abs/2608.12251v1) | 2608.12251v1 | 10 |
| 2026-08-12 | [RoutePack: Replay-Guided Expert Placement and Rollout Trajectory Scheduling for MoE Reinforcement Learning](https://arxiv.org/abs/2608.12146v2) | 2608.12146v2 | 6 |
| 2026-08-12 | [Who Should Own the Expert Cache? Kernel-Managed Tiering for Trillion-Parameter MoE Inference](https://arxiv.org/abs/2608.12103v2) | 2608.12103v2 | 6 |
| 2026-08-12 | [TradingMoE: Routing the Right Experts in Evolving Markets](https://arxiv.org/abs/2608.11785v1) | 2608.11785v1 | 10 |
| 2026-08-12 | [STAR: A Spatial-Topology Aware Routing Framework for Generalizable 3D Scene Understanding](https://arxiv.org/abs/2608.11699v1) | 2608.11699v1 | 6 |
| 2026-08-12 | [APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference](https://arxiv.org/abs/2608.11688v1) | 2608.11688v1 | 6 |
| 2026-08-12 | [FM-LLM: A frequency-enhanced mixture-of-experts framework for adapting LLMs to time series forecasting](https://arxiv.org/abs/2608.11623v1) | 2608.11623v1 | 6 |
| 2026-08-11 | [Mixture-of-Experts-based Entropy Model for Learned Image Compression](https://arxiv.org/abs/2608.10947v1) | 2608.10947v1 | 10 |
| 2026-08-11 | [Trigger the Straggler: Load Hijack on Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.10614v1) | 2608.10614v1 | 8 |
| 2026-08-11 | [Compute-Optimal Is Not Cluster-Optimal: Systems-Aware Scaling for Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.10605v1) | 2608.10605v1 | 7 |
| 2026-08-11 | [MammoMix: Leveraging Mixture of Experts for Robust Mammogram Breast Detection](https://arxiv.org/abs/2608.10437v1) | 2608.10437v1 | 10 |
| 2026-08-11 | [Share First, Route What Remains: A Unified Framework for Token-Adaptive MoE Computation](https://arxiv.org/abs/2608.10392v1) | 2608.10392v1 | 12 |
| 2026-08-10 | [Deep Analog: Open-Set Film Emulation with Reference-Conditioned 3D LUTs](https://arxiv.org/abs/2608.14702v1) | 2608.14702v1 | 12 |
| 2026-08-10 | [DistMoE: Private-data Rehearsal-free Routing in Mixture-of-Experts for Distributed Instruction Tuning](https://arxiv.org/abs/2608.09907v1) | 2608.09907v1 | 8 |
| 2026-08-10 | [Disentangling Co-Occurring Retinal Pathologies with Saliency-Guided Sparse Expert Routing](https://arxiv.org/abs/2608.09752v1) | 2608.09752v1 | 16 |
| 2026-08-10 | [SonicWeave: Chunk-Routed Mixture-of-Experts for Unified Audio Scene Generation](https://arxiv.org/abs/2608.09571v1) | 2608.09571v1 | 6 |
| 2026-08-09 | [Tied Trit-Planes: Constraining PTQTP to a Uniform Nine-Level Quantizer, with a Persistent Folded Format for Disk-Streamed Mixture-of-Experts Serving](https://arxiv.org/abs/2608.08910v1) | 2608.08910v1 | 6 |
| 2026-08-09 | [Beyond Routing: Decoupling Expert Dispatch and Aggregation in Sparse Mixture-of-Experts](https://arxiv.org/abs/2608.08853v1) | 2608.08853v1 | 8 |
| 2026-08-09 | [AdapterMoE: A Two-Stage Hard-Routing Mixture-of-Experts Architecture for Multi-Crop Disease Recognition with Calibrated Rejection and Incremental Learning](https://arxiv.org/abs/2608.08808v1) | 2608.08808v1 | 9 |
| 2026-08-09 | [The Evolution of Mixture-of-Experts Architectures in Large Language Models: Routing, Topology, Load Balancing, and Expert Parallelism](https://arxiv.org/abs/2608.08650v1) | 2608.08650v1 | 14 |
| 2026-08-08 | [EasyBalance: Cross-Layer Load Balancing in Distributed MoE Inference](https://arxiv.org/abs/2608.07964v1) | 2608.07964v1 | 10 |
| 2026-08-08 | [Router Sensitivity Under Lightweight Fine-Tuning Identifies Prunable Experts in Mixture-of-Experts Models](https://arxiv.org/abs/2608.07890v3) | 2608.07890v3 | 9 |
| 2026-08-07 | [Shape Mutating Expert Compression:LorExperts and BTExperts](https://arxiv.org/abs/2608.07814v1) | 2608.07814v1 | 6 |
| 2026-08-07 | [Multi-Level Modeling of Large Language Model Inference Latency and Energy via Hybrid Analytical--Machine-Learning Predictors](https://arxiv.org/abs/2608.06723v1) | 2608.06723v1 | 7 |
| 2026-08-07 | [Policy-Masked Private Experts: Auditable and Reversible Capability Access Control in Sparse MoE Models](https://arxiv.org/abs/2608.06690v2) | 2608.06690v2 | 6 |
| 2026-08-06 | [DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation](https://arxiv.org/abs/2608.06374v1) | 2608.06374v1 | 6 |
| 2026-08-05 | [EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding](https://arxiv.org/abs/2608.05303v1) | 2608.05303v1 | 12 |
| 2026-08-05 | [An Emerging Retail Portfolio Management Application: Personalized, Tax-Aware Reinforcement Learning with Natural Language Goals](https://arxiv.org/abs/2608.05255v1) | 2608.05255v1 | 6 |
| 2026-08-05 | [Personalized Federated Sparse Adaptation of Time-Series Foundation Models](https://arxiv.org/abs/2608.04695v1) | 2608.04695v1 | 6 |
| 2026-08-05 | [Semiparametric robust mixture of experts based on nonparametric maximum likelihood](https://arxiv.org/abs/2608.04561v1) | 2608.04561v1 | 6 |
| 2026-08-05 | [AFD-Ledger: Deployment Provisioning for Attention--FFN Disaggregation](https://arxiv.org/abs/2608.04502v1) | 2608.04502v1 | 6 |
| 2026-08-05 | [Beyond Global Routing Aggregation: Phase-Aware Expert Merging for MoE Vision-Language Models](https://arxiv.org/abs/2608.04454v1) | 2608.04454v1 | 10 |
| 2026-08-05 | [MESH: Memory-Efficient Sinkhorn Optimization for Mixture-of-Experts Training](https://arxiv.org/abs/2608.04407v1) | 2608.04407v1 | 6 |
| 2026-08-05 | [Elbow-Based MoE Routing: A Training-Free Inference Time Plugin for Expert Selection](https://arxiv.org/abs/2608.04401v1) | 2608.04401v1 | 7 |
| 2026-08-04 | [SpecDrop: Parameter-Free Category-Conditioned Routing for Modular Specialization](https://arxiv.org/abs/2608.04084v2) | 2608.04084v2 | 6 |
| 2026-08-04 | [LLaDA MoE v2: Scaling Mixture-of-Experts Diffusion Language Models](https://arxiv.org/abs/2608.03457v1) | 2608.03457v1 | 7 |
| 2026-08-04 | [AcceptMoE: Commitment-Weighted Self-Sizing Verifier Expert Sets for Efficient MoE Speculative Decoding](https://arxiv.org/abs/2608.02989v1) | 2608.02989v1 | 6 |
| 2026-08-03 | [Broadcast Rate Limits in Wi-Fi: A Forgotten Bottleneck for Collaborative Edge LLM Inference](https://arxiv.org/abs/2608.02341v1) | 2608.02341v1 | 8 |
| 2026-08-03 | [STEAM: A Spatio-TEmporal Alignment Mixture-of-Experts Model with Hierarchical Pre-training for EEG Decoding](https://arxiv.org/abs/2608.02070v2) | 2608.02070v2 | 6 |
| 2026-08-03 | [REFLEX: Rethinking MoE Inference as Refinement-Aware Compute Allocation in Diffusion Language Models](https://arxiv.org/abs/2608.01784v1) | 2608.01784v1 | 10 |
| 2026-08-02 | [M3-Former: Multimodal Transformer with Mixture-of-Experts for Long-Term Vessel Trajectory Prediction](https://arxiv.org/abs/2609.10559v1) | 2609.10559v1 | 6 |
| 2026-08-02 | [One Query, Many Scales: Sparse Mixture-of-Experts for Efficient Hierarchical Cross-View Geo-Localization](https://arxiv.org/abs/2608.01060v2) | 2608.01060v2 | 6 |
| 2026-08-01 | [LooperMuscle: Fast and Stable Learning of Humanoid Whole-Body Tracking via Structured Mixture-of-Experts](https://arxiv.org/abs/2608.00820v1) | 2608.00820v1 | 6 |
| 2026-07-31 | [Beyond Routing Weights: Faithful Response-Level Interpretation of Mixture-of-Experts Reward Models via Contribution Contrast](https://arxiv.org/abs/2608.06400v1) | 2608.06400v1 | 8 |
| 2026-07-31 | [EntropyMoE: Entropy-Aware Sparse Expert Routing for Tokenizer-Free LLMs](https://arxiv.org/abs/2608.06398v1) | 2608.06398v1 | 20 |
| 2026-07-31 | [Weight-Space Mixture-of-Experts for Implicit Neural Representation Classification](https://arxiv.org/abs/2607.29463v1) | 2607.29463v1 | 6 |
| 2026-07-31 | [MoPET: Parameter-Efficient Mixture-of-Experts for Unified Medical Image Classification](https://arxiv.org/abs/2607.29462v2) | 2607.29462v2 | 8 |
| 2026-07-31 | [TEXAS: Task-Expert-Aware Supervision for Downstream Mixture-of-Experts LLM Adaptation](https://arxiv.org/abs/2608.06396v1) | 2608.06396v1 | 6 |
| 2026-07-31 | [ReMoE: Report-Guided Mixture-of-Experts for Multimodal OCT/OCTA Anomaly Detection](https://arxiv.org/abs/2607.29039v1) | 2607.29039v1 | 6 |
| 2026-07-31 | [Z-Loss Backward Geometry in Dense Output Heads and Sparse Routers](https://arxiv.org/abs/2609.16179v1) | 2609.16179v1 | 7 |
| 2026-07-30 | [Beyond Geometric Complementarity: Coherent Overlap in Sparse Mixture-of-Experts Routing](https://arxiv.org/abs/2607.28308v1) | 2607.28308v1 | 6 |
| 2026-07-29 | [TIER-MoE: Trust-Informed Expert Routing via Conditional Modality Risk for Multimodal Fusion in Biomedical Classification](https://arxiv.org/abs/2607.27289v1) | 2607.27289v1 | 10 |
| 2026-07-29 | [Mixture-of-experts for handwriting trajectory reconstruction from IMU sensors](https://arxiv.org/abs/2607.26708v1) | 2607.26708v1 | 6 |
| 2026-07-28 | [Spend Experts Where You Are Unsure: Confidence-Adaptive Routing for Mixture-of-Experts LoRA](https://arxiv.org/abs/2607.26052v2) | 2607.26052v2 | 8 |
| 2026-07-27 | [DraftExpert: Expansion-Aware Self-Speculative Decoding for End-Device MoE Inference](https://arxiv.org/abs/2607.24434v1) | 2607.24434v1 | 6 |
| 2026-07-25 | [Context-Adaptive Inference: A Unified Statistical and Foundation-Model View](https://arxiv.org/abs/2607.23304v1) | 2607.23304v1 | 8 |
| 2026-07-25 | [Hierarchical Copula-Gumbel-Top-K Routing: Two-Sided Dependence Control for Frozen Mixture-of-Experts at Fixed Per-Token Routing Laws](https://arxiv.org/abs/2607.28670v3) | 2607.28670v3 | 11 |
| 2026-07-25 | [Decoding the Skew: Distribution-Aware MoE Inference with Adaptive Kernel Dispatch](https://arxiv.org/abs/2607.23099v3) | 2607.23099v3 | 12 |
| 2026-07-25 | [DishSeg24k: A Large-Scale Benchmark for Food Segmentation with Stochastic Expert Decoding](https://arxiv.org/abs/2607.23070v2) | 2607.23070v2 | 8 |
| 2026-07-24 | [MoE$^2$-LoRA: When MoE Models Meet MoE-style Low-Rank Adaptation](https://arxiv.org/abs/2607.21978v1) | 2607.21978v1 | 6 |
| 2026-07-23 | [Beyond Independent Optimization: Compression, MoE Routing, and Quantization Interactions in Multimodal Edge Intelligence](https://arxiv.org/abs/2607.20981v1) | 2607.20981v1 | 6 |
| 2026-07-22 | [Emergent Compositional Skills in Mixture-of-Experts VLAs](https://arxiv.org/abs/2607.20771v2) | 2607.20771v2 | 8 |
| 2026-07-22 | [An Isotropy-Preserving Spectral Cap for Muon: Theory and Three Case Studies](https://arxiv.org/abs/2607.19771v1) | 2607.19771v1 | 9 |
| 2026-07-21 | [Fine-grained Computation-Communication Overlap via Tile-level Signaling and Scheduling for Mixture-of-Experts](https://arxiv.org/abs/2607.19539v1) | 2607.19539v1 | 9 |
| 2026-07-21 | [Where Should Optimizer State Live? Tiered State Allocation for Memory-Efficient Mixture-of-Experts Training](https://arxiv.org/abs/2607.19058v2) | 2607.19058v2 | 8 |
| 2026-07-20 | [Mixture-of-Experts Serving](https://arxiv.org/abs/2607.17880v1) | 2607.17880v1 | 6 |
| 2026-07-19 | [OrderMoE: An expert similarity driven distributed edge MoE inference](https://arxiv.org/abs/2607.17154v2) | 2607.17154v2 | 6 |
| 2026-07-19 | [ThAME: 3D Memory-Enabled Heterogeneous Accelerator for LLM Mixture of Experts](https://arxiv.org/abs/2607.17074v2) | 2607.17074v2 | 11 |
| 2026-07-18 | [Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding](https://arxiv.org/abs/2607.16721v1) | 2607.16721v1 | 6 |
| 2026-07-17 | [Multi-level context Modeling for consistent expert selection in Mixture-of-Experts](https://arxiv.org/abs/2607.16427v2) | 2607.16427v2 | 13 |
| 2026-07-17 | [MGDT: MLLM-Guided Diffusion Transformer with Relation-Adaptive Mixture-of-Experts for Multimodal Knowledge Graph Completion](https://arxiv.org/abs/2607.15592v1) | 2607.15592v1 | 6 |
| 2026-07-15 | [MixCompress: Mixture of Experts for Variable Rate Learned Image Compression](https://arxiv.org/abs/2607.14334v1) | 2607.14334v1 | 10 |
| 2026-07-14 | [Less Experts, Faster Decoding: Cost-Aware Speculative Decoding for Mixture-of-Experts](https://arxiv.org/abs/2607.12696v1) | 2607.12696v1 | 7 |
| 2026-07-14 | [WaterMoE: Expert-Routing-based Watermarking for High Fidelity and Efficiency](https://arxiv.org/abs/2607.13099v1) | 2607.13099v1 | 6 |
| 2026-07-14 | [Full-Pipeline Inference Optimization for MiMo-V2.5 Series: Pushing Hybrid SWA Efficiency to the Limit](https://arxiv.org/abs/2607.13095v1) | 2607.13095v1 | 10 |
| 2026-07-14 | [Understanding Structured Health Data through Interaction-Aware Mixture-of-Experts](https://arxiv.org/abs/2607.12255v1) | 2607.12255v1 | 6 |
| 2026-07-14 | [Risk-Aware Decision-Making for Autonomous Overtaking: A World Model-Based Mixture-of-Experts Framework](https://arxiv.org/abs/2609.00385v1) | 2609.00385v1 | 6 |
| 2026-07-14 | [Detecting a Route Flip Is Easier Than Knowing Whether to Fix It: Causal Route-Mediated Damage in Quantized Mixture-of-Experts](https://arxiv.org/abs/2608.11212v1) | 2608.11212v1 | 8 |
| 2026-07-09 | [On the Design of Mixture-of-Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2607.08250v2) | 2607.08250v2 | 10 |
| 2026-07-09 | [MORES: Mobile Reasoning-as-a-Service via Distributed LLM Inference-Time Scaling](https://arxiv.org/abs/2607.08116v1) | 2607.08116v1 | 7 |
| 2026-07-08 | [Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence](https://arxiv.org/abs/2607.07675v1) | 2607.07675v1 | 7 |
| 2026-07-08 | [Image classification via a quantum-inspired strategy involving a mixture of experts](https://arxiv.org/abs/2607.07754v2) | 2607.07754v2 | 6 |
| 2026-07-07 | [ProMoE-FL: Prototype-conditioned Mixture of Experts for Multimodal Federated Learning with Missing Modalities](https://arxiv.org/abs/2607.06633v1) | 2607.06633v1 | 14 |
| 2026-07-07 | [Mixture-of-Experts Deep Reinforcement Learning for Reliability-Constrained Energy-Efficient PDCCH Monitoring in Internet of Thing Device](https://arxiv.org/abs/2607.06084v2) | 2607.06084v2 | 6 |
| 2026-07-07 | [SpaR3D-MoE: Adaptive 3D Spatial Reasoning from Sparse Views Meets Geometry-Inductive Mixture-of-Experts](https://arxiv.org/abs/2607.06620v1) | 2607.06620v1 | 8 |
| 2026-07-07 | [SpecTrack: Spectral Prompt Guided Adaptive Experts for Multispectral Object Tracking](https://arxiv.org/abs/2607.05988v1) | 2607.05988v1 | 6 |
| 2026-07-07 | [Knowledge-Constrained Shape Optimization with a Mixture-of-Experts Neural Operator for High-Confidence Design](https://arxiv.org/abs/2607.09763v1) | 2607.09763v1 | 6 |
| 2026-07-05 | [Optimal Mixture-of-Experts Model Averaging for Conditional Generative Models](https://arxiv.org/abs/2607.04360v1) | 2607.04360v1 | 6 |
| 2026-07-05 | [WPG-MoE: Weak-Prior-Guided Dense Mixture-of-Experts for User-Level Social Media Depression Detection](https://arxiv.org/abs/2607.04350v1) | 2607.04350v1 | 6 |
| 2026-07-05 | [BrownoutMoE: Structure-Aware Expert Grouping for Efficient and Accurate LLM Web-based Services](https://arxiv.org/abs/2607.04164v1) | 2607.04164v1 | 8 |
| 2026-07-04 | [Worldscape-MoE: A Unified Mixture-of-Experts World Model for Scalable Heterogeneous Action Control](https://arxiv.org/abs/2607.03964v1) | 2607.03964v1 | 7 |
| 2026-07-02 | [Mixture-of-Parallelisms: Towards Memory-Efficient Training Stack for Mixture-of-Experts Models](https://arxiv.org/abs/2607.01844v1) | 2607.01844v1 | 6 |
| 2026-07-02 | [EPnG: Adaptive Expert Prune-and-Grow for Parameter-Efficient MoE Fine-tuning](https://arxiv.org/abs/2607.01789v1) | 2607.01789v1 | 6 |
| 2026-07-02 | [Generic Expert Coverage for Pruning SparseMixture-of-Experts Language Models](https://arxiv.org/abs/2607.01710v1) | 2607.01710v1 | 6 |
| 2026-07-01 | [On the Utility and Factual Reliability of Pruned Mixture-of-Experts Models in the Biomedical Domain](https://arxiv.org/abs/2607.01444v1) | 2607.01444v1 | 6 |
| 2026-07-01 | [ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving](https://arxiv.org/abs/2607.00466v2) | 2607.00466v2 | 6 |
| 2026-07-01 | [Multi-scale Mixture of World Models for Embodied Agents in Evolving Environments](https://arxiv.org/abs/2607.00457v1) | 2607.00457v1 | 6 |
| 2026-07-01 | [MEPA: Multi-Scale Representation Alignment for Visual Autoregressive Modeling with Mixture of Experts](https://arxiv.org/abs/2607.00371v1) | 2607.00371v1 | 6 |
| 2026-06-30 | [FRAME: Learning the Adaptation Domain with a Mixture of Fractional-Fourier Experts](https://arxiv.org/abs/2607.00162v1) | 2607.00162v1 | 8 |
| 2026-06-30 | [FaceMoE: Mixture of Experts for Low-Resolution Face Recognition](https://arxiv.org/abs/2606.32040v1) | 2606.32040v1 | 18 |
| 2026-06-30 | [Dual-Adaptive SAM3: Hierarchical Routing over Low-Rank Expert Layers for Parameter-Efficient Medical Image Segmentation](https://arxiv.org/abs/2607.02571v1) | 2607.02571v1 | 6 |
| 2026-06-30 | [ExPLoRe: Expert Patch-Level Loss Routing for Multi-Objective Masked Image Modeling](https://arxiv.org/abs/2606.31201v1) | 2606.31201v1 | 6 |
| 2026-06-30 | [A Three-Phase Foundation Model for Tax-Aware Personalized Portfolio Management](https://arxiv.org/abs/2606.30997v3) | 2606.30997v3 | 6 |
| 2026-06-29 | [A Multi-task Mixture of Experts Framework for Malware Classification, Packing Detection, and Family Attribution](https://arxiv.org/abs/2606.30572v1) | 2606.30572v1 | 6 |
| 2026-06-29 | [Residual-Guided Expert Specialization for Incomplete Multimodal Learning](https://arxiv.org/abs/2606.30355v1) | 2606.30355v1 | 6 |
| 2026-06-29 | [Towards Continual Motion-Language Agents: LoRA Variants for Incremental Motion Understanding and Generation](https://arxiv.org/abs/2606.30266v2) | 2606.30266v2 | 6 |
| 2026-06-28 | [Does Role Specialization Matter for Explanation Faithfulness in Mixture-of-Experts?](https://arxiv.org/abs/2606.29613v1) | 2606.29613v1 | 6 |
| 2026-06-28 | [TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation](https://arxiv.org/abs/2606.29575v3) | 2606.29575v3 | 6 |
| 2026-06-26 | [CLEAR-MoE: Shared-Basis Expert Extraction from Frozen Vision Transformers via Calibration-Driven Layer Selection](https://arxiv.org/abs/2606.28516v1) | 2606.28516v1 | 8 |
| 2026-06-25 | [PAMAE: Phase-Aware-MoE Action Experts Towards Reliable Flow-Matching Vision-Language-Action Policies](https://arxiv.org/abs/2606.27144v1) | 2606.27144v1 | 10 |
| 2026-06-25 | [Focusing on What Matters: Saliency-Harnessing Accurate Routing for Diffusion MoE](https://arxiv.org/abs/2606.26938v1) | 2606.26938v1 | 7 |
| 2026-06-25 | [Depth-Aware Sensitivity Analysis of Mixture-of-Experts Models via Magnitude-Based Expert Masking](https://arxiv.org/abs/2608.13565v1) | 2608.13565v1 | 8 |
| 2026-06-24 | [SARA: Unlocking Multilingual Knowledge in Mixture-of-Experts via Semantically Anchored Routing Alignment](https://arxiv.org/abs/2606.25821v1) | 2606.25821v1 | 6 |
| 2026-06-24 | [Learning Subset-Shared Invariances for Domain Generalization with Mixture-of-Experts](https://arxiv.org/abs/2606.25665v1) | 2606.25665v1 | 6 |
| 2026-06-24 | [SpecPrefetch: Parameter-Efficient Expert Prefetching for Sparse MoE Foundation Models](https://arxiv.org/abs/2607.24787v2) | 2607.24787v2 | 6 |
| 2026-06-23 | [How Modular Is a Frontier Mixture-of-Experts? A Pre-registered Causal Test in Which Apparent Expert Modularity Mostly Dissolves](https://arxiv.org/abs/2606.25092v1) | 2606.25092v1 | 6 |
| 2026-06-23 | [A 35B Hybrid-Attention Mixture-of-Experts Model on a 6GB 2011 GPU: Hand-Written 4-bit CUDA Inference for Fermi](https://arxiv.org/abs/2606.24031v1) | 2606.24031v1 | 6 |
| 2026-06-22 | [Cross-Architectural Mixture-of-Experts with Adaptive Soft Routing for Plant Leaf Disease Classification](https://arxiv.org/abs/2606.23441v1) | 2606.23441v1 | 6 |
| 2026-06-22 | [Does the Same Token Mean the Same State? MoE Routing as Signal for Reasoning Control](https://arxiv.org/abs/2606.22798v1) | 2606.22798v1 | 6 |
| 2026-06-21 | [Systematic Exploration of 4-Expert Heterogeneous Mixture-of-Experts via Automated Pipeline Search](https://arxiv.org/abs/2606.23739v1) | 2606.23739v1 | 7 |
| 2026-06-20 | [WiSP: A Working-Set View of Mixture-of-Experts Serving on Extremely Low-Resource Hardware](https://arxiv.org/abs/2606.21868v2) | 2606.21868v2 | 6 |
| 2026-06-19 | [Does Mixture-of-Experts Actually Help Inference on Consumer and Edge Hardware? An Empirical Study](https://arxiv.org/abs/2606.21428v3) | 2606.21428v3 | 6 |
| 2026-06-19 | [Speaker Identity in Non-Verbal Vocalizations: Conditional Distillation and Mixture of Experts Approach](https://arxiv.org/abs/2606.21215v1) | 2606.21215v1 | 6 |
| 2026-06-19 | [Factor-Aware Mixture-of-Experts with Pretrained Encoder for Combinatorial Generalization](https://arxiv.org/abs/2606.21100v1) | 2606.21100v1 | 8 |
| 2026-06-19 | [MoECodec: Image Compression for joint human and machine perception via Mixture-of-Experts](https://arxiv.org/abs/2606.21033v1) | 2606.21033v1 | 6 |
| 2026-06-18 | [Toward Calibrated Mixture-of-Experts Under Distribution Shift](https://arxiv.org/abs/2606.20544v1) | 2606.20544v1 | 6 |
| 2026-06-17 | [Geometric and Stochastic Analysis of Discontinuities in Sparse Mixture-of-Experts](https://arxiv.org/abs/2606.19036v1) | 2606.19036v1 | 7 |
| 2026-06-17 | [FoMoE: Breaking the Full-Replica Barrier with a Federation of MoEs](https://arxiv.org/abs/2606.19025v2) | 2606.19025v2 | 8 |
| 2026-06-17 | [MawForge: Memory-Bounded Expert Materialization for Local Mixture-of-Experts Inference](https://arxiv.org/abs/2607.09686v1) | 2607.09686v1 | 6 |
| 2026-06-16 | [Predicting Immune Biomarkers with MultiModal Mixture-of-Expert Pathology Foundation Models Empowers Precision Oncology](https://arxiv.org/abs/2606.18123v2) | 2606.18123v2 | 6 |
| 2026-06-16 | [SoftMoE: Soft Differentiable Routing for Mixture-of-Experts in LLMs](https://arxiv.org/abs/2606.17952v1) | 2606.17952v1 | 11 |
| 2026-06-16 | [Conservation Laws for Modern Neural Architectures](https://arxiv.org/abs/2606.17816v1) | 2606.17816v1 | 6 |
| 2026-06-16 | [SkillMoV: Mixture-of-View Routing with Prototype-Conditioned Gating for Unified Multi-View Proficiency Estimation](https://arxiv.org/abs/2606.17615v1) | 2606.17615v1 | 6 |
| 2026-06-15 | [Tying the Loop -- Tied Expert Layers in Mixture-of-Experts Language Models](https://arxiv.org/abs/2606.16825v1) | 2606.16825v1 | 7 |
| 2026-06-15 | [Multi-Modal Spatio-Temporal Graph Neural Network with Mixture of Experts for Soil Organic Carbon Prediction](https://arxiv.org/abs/2606.16580v1) | 2606.16580v1 | 10 |
| 2026-06-15 | [SPRI: SVD-Partitioned Residual Initialization for Data-Constrained MoE Upcycling](https://arxiv.org/abs/2606.16456v1) | 2606.16456v1 | 7 |
| 2026-06-15 | [DynFS-MoE: Dynamic Functional-Structural Mixture-of-Experts for Post-Traumatic Epilepsy Diagnosis](https://arxiv.org/abs/2606.16203v4) | 2606.16203v4 | 10 |
| 2026-06-14 | [How to Score Experts for One-Shot MoE Expert Pruning: A Systematic Formulation and Selection Principle](https://arxiv.org/abs/2606.15716v2) | 2606.15716v2 | 8 |
| 2026-06-14 | [Conflict-Aware Federated Fine-Tuning of Large Language Models with Mixture-of-Experts](https://arxiv.org/abs/2606.15625v1) | 2606.15625v1 | 7 |
| 2026-06-13 | [A Spatio-Temporal Expert Prefetching Framework for Efficient MoE-based LLM Inference](https://arxiv.org/abs/2606.15453v1) | 2606.15453v1 | 6 |
| 2026-06-13 | [Coordinated Scheduling for MoE LLM Serving](https://arxiv.org/abs/2606.15177v1) | 2606.15177v1 | 16 |
| 2026-06-12 | [Sticky Routing: Training MoE Models for Memory-Efficient Inference](https://arxiv.org/abs/2607.08780v1) | 2607.08780v1 | 6 |
| 2026-06-12 | [A Transformer-Based Mixture-of-Experts Framework for False Data Injection Attack Detection and Localization](https://arxiv.org/abs/2606.15005v1) | 2606.15005v1 | 6 |
| 2026-06-12 | [iLENS: Interpretable LLM-Guided Mixture-of-Experts for Neuroimaging Survival Analysis](https://arxiv.org/abs/2607.08778v1) | 2607.08778v1 | 10 |
| 2026-06-12 | [From Self-Supervised Speech Models to Mixture-of-Experts for Robust Anti-Spoofing](https://arxiv.org/abs/2606.14639v1) | 2606.14639v1 | 8 |
| 2026-06-12 | [Decoupled Mixture-of-Experts for Parametric Knowledge Injection](https://arxiv.org/abs/2606.14243v1) | 2606.14243v1 | 10 |
| 2026-06-11 | [See Selectively, Act Adaptively: Dual-Level Structural Decomposition for Bimanual Robot Manipulation](https://arxiv.org/abs/2606.13279v2) | 2606.13279v2 | 6 |
| 2026-06-10 | [Redesign Mixture-of-Experts Routers with Manifold Power Iteration](https://arxiv.org/abs/2606.12397v1) | 2606.12397v1 | 9 |
| 2026-06-10 | [Multi-Rate Mixture of Experts for Accelerating Liquid Neural Network Training](https://arxiv.org/abs/2606.12240v1) | 2606.12240v1 | 10 |
| 2026-06-10 | [The Brain That Goes Quiet: Serving a Large Model's Knowledge at 131 Tokens per Second on an 8 GB Laptop by Removing the Large Model from the Runtime Path](https://arxiv.org/abs/2606.12154v1) | 2606.12154v1 | 6 |
| 2026-06-10 | [Harnessing Routing Foresight for Micro-step-level MoE load balancing in RL Post-training](https://arxiv.org/abs/2606.11867v1) | 2606.11867v1 | 10 |
| 2026-06-09 | [From Observation to Intervention: A Causal Audit of Expert Importance in Mixture-of-Experts Models](https://arxiv.org/abs/2606.10703v2) | 2606.10703v2 | 6 |
| 2026-06-09 | [Achieving Cloud-Grade SLOs for Local Mixture-of-Experts Inference through CPU-GPU Hybrid Design](https://arxiv.org/abs/2606.10493v1) | 2606.10493v1 | 6 |
| 2026-06-09 | [Entropy-Aware Domain-Routed Mixture-of-Experts Speech-LLM Framework: A Case Study of Multi-Domain Child-Adult ASR](https://arxiv.org/abs/2606.10454v1) | 2606.10454v1 | 8 |
| 2026-06-09 | [Enhancing Multilingual LLM-based ASR with Mixture of Experts and Dynamic Downsampling](https://arxiv.org/abs/2606.10439v1) | 2606.10439v1 | 6 |
| 2026-06-09 | [PADD: Path-Aligned Decompression Distillation for Non-Router Teacher to Guide MoE Student Learning](https://arxiv.org/abs/2606.10369v1) | 2606.10369v1 | 11 |
| 2026-06-09 | [Routing-Aware Expert Calibration for Machine Unlearning in Mixture-of-Experts Language Models](https://arxiv.org/abs/2606.10338v2) | 2606.10338v2 | 8 |
| 2026-06-08 | [MosaicIMU: Composing Carrier Experts for Generalizable Neural Inertial Odometry](https://arxiv.org/abs/2606.09355v1) | 2606.09355v1 | 6 |
| 2026-06-08 | [FAME: Forecastability-Aware Mixture of Experts for Heterogeneous Time Series Forecasting](https://arxiv.org/abs/2606.08896v1) | 2606.08896v1 | 16 |
| 2026-06-07 | [STAR: Rethinking MoE Routing as Structure-Aware Subspace Learning](https://arxiv.org/abs/2606.08814v1) | 2606.08814v1 | 6 |
| 2026-06-07 | [NGram-MoSE: Efficient Remote Sensing Super-Resolution via N-Gram Context and Mixture-of-Experts](https://arxiv.org/abs/2606.08535v1) | 2606.08535v1 | 8 |
| 2026-06-06 | [LongMoE: Longitudinal Multimodal Learning via Trajectory-Aware Mixture-of-Experts](https://arxiv.org/abs/2606.09907v2) | 2606.09907v2 | 6 |
| 2026-06-04 | [Value-and-Structure Alignment for Routing-Consistent Quantization of Mixture-of-Experts Models](https://arxiv.org/abs/2606.05688v1) | 2606.05688v1 | 8 |
| 2026-06-04 | [Less is MoE: Trimming Experts in Domain-Specialist Language Models](https://arxiv.org/abs/2606.05538v2) | 2606.05538v2 | 6 |
| 2026-06-03 | [AlphaQ: Calibration-Free Bit Allocation for Mixture-of-Experts Quantization](https://arxiv.org/abs/2606.04980v1) | 2606.04980v1 | 10 |
| 2026-06-03 | [HD-DinoMoE: A Class-Aware Hierarchical Dual Mixture-of-Experts Network for Scleral Anomaly Segmentation in Complex Acquisition Scenarios](https://arxiv.org/abs/2606.04888v1) | 2606.04888v1 | 6 |
| 2026-06-03 | [D$^3$-MoE:Dual Disentangled Diffusion Mixture-of-Experts for Style-Controllable End-to-End Autonomous Driving](https://arxiv.org/abs/2606.04884v1) | 2606.04884v1 | 8 |
| 2026-06-03 | [Physics-Informed Video Generation via Mixture-of-Experts Latent Alignment](https://arxiv.org/abs/2606.04737v1) | 2606.04737v1 | 10 |
| 2026-06-03 | [CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation](https://arxiv.org/abs/2606.04718v3) | 2606.04718v3 | 10 |
| 2026-06-03 | [SHAPE: Coalition-Aware Expert Pruning for Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2606.09886v1) | 2606.09886v1 | 6 |
| 2026-06-03 | [TENP: Trapezoidal Expert Neuron Pruning For Mixture-of-Experts](https://arxiv.org/abs/2606.09885v1) | 2606.09885v1 | 6 |
| 2026-06-03 | [LoopMoE: Unifying Iterative Computation with Mixture-of-Experts for Language Modeling](https://arxiv.org/abs/2606.04438v2) | 2606.04438v2 | 6 |
| 2026-06-03 | [Argus-Retriever: Vision-LLM Late-Interaction Retrieval with Region-Aware Query-Conditioned MoE for Visual Document Retrieval](https://arxiv.org/abs/2606.04300v1) | 2606.04300v1 | 6 |
| 2026-06-02 | [Interpretability Is Not Just a Tax: Sparsity and Diversity Yield Legible and Composable Reward Experts for Personalization](https://arxiv.org/abs/2606.04284v2) | 2606.04284v2 | 6 |
| 2026-06-02 | [Decomposing Refusal Steering in Mixture-of-Experts Models](https://arxiv.org/abs/2606.04160v3) | 2606.04160v3 | 10 |
| 2026-06-02 | [PRISM: Synergizing Vision Foundation Models via Self-organized Expert Specialization](https://arxiv.org/abs/2606.03444v1) | 2606.03444v1 | 6 |
| 2026-06-02 | [When Model Merging Breaks Routing: Training-Free Calibration for MoE](https://arxiv.org/abs/2606.03391v1) | 2606.03391v1 | 8 |
| 2026-06-01 | [GC-MoE: Genomics-Guided Cell-Type-Specific Mixture of Experts for Histology-Based Single-Cell Spatial Transcriptomics](https://arxiv.org/abs/2606.02424v1) | 2606.02424v1 | 10 |
| 2026-06-01 | [Hierarchically Decoupled Mixture-of-Experts for Robust Traffic Sign Recognition in Complex Driving Scenarios](https://arxiv.org/abs/2606.01822v2) | 2606.01822v2 | 6 |
| 2026-06-01 | [MoRE: A Mixture-of-Experts-Based Task-Adaptive End-to-End Network for Multimodal MRI Reconstruction](https://arxiv.org/abs/2606.01784v1) | 2606.01784v1 | 7 |
| 2026-06-01 | [DOT-MoE: Differentiable Optimal Transport for MoEfication](https://arxiv.org/abs/2606.01666v1) | 2606.01666v1 | 11 |
| 2026-06-01 | [ProbMoE: Differentiable Probabilistic Routing for Mixture-of-Experts](https://arxiv.org/abs/2606.01509v1) | 2606.01509v1 | 6 |
| 2026-05-31 | [Deft Scheduling of Dynamic Cloud Workflows with Varying Deadlines via Mixture-of-Experts](https://arxiv.org/abs/2606.01162v2) | 2606.01162v2 | 10 |
| 2026-05-31 | [DAG-MoE: From Simple Mixture to Structural Aggregation in Mixture-of-Experts](https://arxiv.org/abs/2606.01062v1) | 2606.01062v1 | 9 |
| 2026-05-31 | [Learning Multi-Modal Trajectory Policies for Data-Efficient Robotic Manipulation](https://arxiv.org/abs/2606.01047v1) | 2606.01047v1 | 6 |
| 2026-05-30 | [MoEIoU: Rethinking Bounding-Box Regression as a Mixture of Experts](https://arxiv.org/abs/2606.00844v1) | 2606.00844v1 | 10 |
| 2026-05-30 | [Confidence-Adaptive SwiGLU for Mixture-of-Experts](https://arxiv.org/abs/2606.00761v1) | 2606.00761v1 | 11 |
| 2026-05-30 | [Dialectics of Alignment: Harnessing Unsafe Knowledge for Dynamic Safety Routing](https://arxiv.org/abs/2606.00686v3) | 2606.00686v3 | 6 |
| 2026-05-30 | [MESA: Improving MoE Safety Alignment via Decentralized Expertise](https://arxiv.org/abs/2606.00651v1) | 2606.00651v1 | 6 |
| 2026-05-29 | [PR2: Predictive Routing Replay for MoE-Based LLM Reinforcement Learning](https://arxiv.org/abs/2606.00395v2) | 2606.00395v2 | 6 |
| 2026-05-29 | [MoE-dqINR: A Unified Mixture-of-Experts Implicit Neural Representation Framework for Scan-Specific Dynamic and Quantitative MRI Reconstruction](https://arxiv.org/abs/2605.31302v1) | 2605.31302v1 | 6 |
| 2026-05-29 | [MoG: Mixture of Experts for Graph-based Retrieval-Augmented Generation](https://arxiv.org/abs/2605.31010v1) | 2605.31010v1 | 8 |
| 2026-05-29 | [Eigenvectors of Experts are Training-free Non-collapsing Routers](https://arxiv.org/abs/2605.30992v1) | 2605.30992v1 | 7 |
| 2026-05-29 | [dMoE: dLLMs with Learnable Block Experts](https://arxiv.org/abs/2605.30876v2) | 2605.30876v2 | 8 |
| 2026-05-28 | [Graph-Conditioned Mixture of Graph Neural Network Experts for Traffic Forecasting](https://arxiv.org/abs/2605.30486v1) | 2605.30486v1 | 6 |
| 2026-05-28 | [Leveraging Routing Dynamics in Mixture-of-Experts Models for Efficient Language Adaptation](https://arxiv.org/abs/2605.29714v1) | 2605.29714v1 | 10 |
| 2026-05-28 | [RASET: Router-Agnostic Safety-Critical Expert Tuning Exposes Localized Safety Enforcement Failures in Mixture-of-Experts LLMs](https://arxiv.org/abs/2605.29708v2) | 2605.29708v2 | 9 |
| 2026-05-28 | [ConMoE: MoE Compression as Expert Selection and Functional Assignment](https://arxiv.org/abs/2605.29350v2) | 2605.29350v2 | 6 |
| 2026-05-27 | [Rotary GPU: Exploring Local Execution Paths for Large Mixture-of-Experts Models Under Limited GPU Memory](https://arxiv.org/abs/2605.29135v1) | 2605.29135v1 | 7 |
| 2026-05-27 | [A Minimal Bifurcation Model of Load Imbalance in a Softmax Mixture-of-Experts Router](https://arxiv.org/abs/2605.29121v1) | 2605.29121v1 | 9 |
| 2026-05-27 | [RA-MoE: Routing-Aligned Fine-Tuning for Multilingual Adaptation of Mixture-of-Experts Models](https://arxiv.org/abs/2605.28306v2) | 2605.28306v2 | 7 |
| 2026-05-27 | [VidPrism: Heterogeneous Mixture of Experts for Image-to-Video Transfer](https://arxiv.org/abs/2605.28229v1) | 2605.28229v1 | 10 |
| 2026-05-27 | [Pruning and Distilling Mixture-of-Experts into Dense Language Models](https://arxiv.org/abs/2605.28207v2) | 2605.28207v2 | 7 |
| 2026-05-27 | [Mixture-of-Experts Knowledge Graph Retrieval-Augmented Generation for Multi-Agent LLM-based Recommendation](https://arxiv.org/abs/2605.28175v2) | 2605.28175v2 | 6 |
| 2026-05-27 | [FPMoE: A Sparse Mixture-of-Experts Approach to Functional Code Generation](https://arxiv.org/abs/2605.27849v1) | 2605.27849v1 | 6 |
| 2026-05-26 | [NUCLEUS-MoE: Unified Model of Pool Boiling for Liquid Cooling](https://arxiv.org/abs/2605.27722v1) | 2605.27722v1 | 8 |
| 2026-05-26 | [MobileMoE: Scaling On-Device Mixture of Experts](https://arxiv.org/abs/2605.27358v1) | 2605.27358v1 | 11 |
| 2026-05-26 | [ReMoE: Boosting Expert Reuse through Router Fine-Tuning in Memory-Constrained MoE LLM Inference](https://arxiv.org/abs/2605.27081v1) | 2605.27081v1 | 7 |
| 2026-05-25 | [BioFact-MoE: Biologically Factorized Mixture of Experts for Vision-Language Prognostic Modeling in Hepatocellular Carcinoma](https://arxiv.org/abs/2605.26376v1) | 2605.26376v1 | 6 |
| 2026-05-25 | [Cross-Stage Attention Multi-Expert Network for Radiologist-Inspired Breast Ultrasound Diagnosis](https://arxiv.org/abs/2605.25518v1) | 2605.25518v1 | 8 |
| 2026-05-24 | [AME-TS: Anchored Mixture-of-Experts for Time Series Forecasting](https://arxiv.org/abs/2605.25166v1) | 2605.25166v1 | 14 |
| 2026-05-24 | [RouteScan: A Non-Intrusive Approach to Auditing MoE LLMs Safety via Expert Routing Telemetry](https://arxiv.org/abs/2605.24817v2) | 2605.24817v2 | 17 |
| 2026-05-23 | [ConceptM$^3$oE: Concept-Guided Multimodal Mixture of Experts for Interpretable Computational Pathology](https://arxiv.org/abs/2605.24399v2) | 2605.24399v2 | 10 |
| 2026-05-22 | [Safety-Oriented Routing Analysis of Mixtral MoE Under Benign and Harmful Prompts](https://arxiv.org/abs/2605.24270v1) | 2605.24270v1 | 6 |
| 2026-05-22 | [Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models](https://arxiv.org/abs/2605.23893v2) | 2605.23893v2 | 7 |
| 2026-05-22 | [Semantically Structured Mixture-of-Experts for Compositional Robotic Manipulation](https://arxiv.org/abs/2605.23477v1) | 2605.23477v1 | 6 |
| 2026-05-22 | [Learning Individual Dynamics from Sparse Cross-Sectional Snapshots](https://arxiv.org/abs/2605.23470v1) | 2605.23470v1 | 6 |
| 2026-05-22 | [NASiC: 3D NAND-based CAM-Selected Multibit CIM Architecture for Efficient On-Device Mixture-of-Experts LLM Inference](https://arxiv.org/abs/2605.23294v1) | 2605.23294v1 | 11 |
| 2026-05-22 | [SpikingMoE: SDPrompt-Guided Dynamic Expert Fusion in Spiking Neural Networks](https://arxiv.org/abs/2605.23188v1) | 2605.23188v1 | 8 |
| 2026-05-22 | [GMENet: Generative Mixture of Experts Network for Multi-Center Glioma Diagnosis with Incomplete Imaging Sequences](https://arxiv.org/abs/2605.23183v1) | 2605.23183v1 | 10 |
| 2026-05-21 | [The Attribution Contract for Generative Language Models](https://arxiv.org/abs/2605.23080v3) | 2605.23080v3 | 8 |
| 2026-05-21 | [GEMQ: Global Expert-Level Mixed-Precision Quantization for MoE LLMs](https://arxiv.org/abs/2605.23078v1) | 2605.23078v1 | 6 |
| 2026-05-21 | [FAME: Failure-Aware Mixture-of-Experts for Message-Level Log Anomaly Detection](https://arxiv.org/abs/2605.22779v2) | 2605.22779v2 | 8 |
| 2026-05-21 | [Dynamic Mixture of Latent Memories for Self-Evolving Agents](https://arxiv.org/abs/2605.21951v1) | 2605.21951v1 | 6 |
| 2026-05-20 | [PALS: Power-Aware LLM Serving for Mixture-of-Experts Models](https://arxiv.org/abs/2605.21427v1) | 2605.21427v1 | 6 |
| 2026-05-20 | [Task-Routed Mixture-of-Experts with Cognitive Appraisal for Implicit Sentiment Analysis](https://arxiv.org/abs/2605.20916v1) | 2605.20916v1 | 12 |
| 2026-05-20 | [Dynamic TMoE: A Drift-Aware Dynamic Mixture of Experts Framework for Non-Stationary Time Series Forecasting](https://arxiv.org/abs/2605.20678v1) | 2605.20678v1 | 12 |
| 2026-05-20 | [LER-YOLO: Reliability-Aware Expert Routing for Misaligned RGB-Infrared UAV Detection](https://arxiv.org/abs/2605.20667v1) | 2605.20667v1 | 10 |
| 2026-05-20 | [Beyond Routing: Characterising Expert Tuning and Representation in Vision Mixture-of-Experts](https://arxiv.org/abs/2605.20610v1) | 2605.20610v1 | 6 |
| 2026-05-19 | [CAT-MoEformer: Context-Aware Temporal MoE Transformer for Beam Prediction](https://arxiv.org/abs/2605.19997v1) | 2605.19997v1 | 6 |
| 2026-05-19 | [UAV-Assisted Cooperative Edge Inference for Low-Altitude Economy via MoE-based Hierarchical Deep Reinforcement Learning](https://arxiv.org/abs/2605.19290v1) | 2605.19290v1 | 6 |
| 2026-05-19 | [FPED: A Functional-Network Prior-Guided Mixture-of-Experts Framework for Interpretable Brain Decoding](https://arxiv.org/abs/2605.19279v1) | 2605.19279v1 | 10 |
| 2026-05-18 | [Post-Trained MoE Can Skip Half Experts via Self-Distillation](https://arxiv.org/abs/2605.18643v2) | 2605.18643v2 | 8 |
| 2026-05-18 | [Mixture-of-Experts Diffusion Models for Adaptive Massive MIMO Channel Estimation via Variational Bayesian Inference](https://arxiv.org/abs/2605.18325v1) | 2605.18325v1 | 6 |
| 2026-05-18 | [CP-MoE: Consistency-Preserving Mixture-of-Experts for Continual Learning](https://arxiv.org/abs/2605.20247v2) | 2605.20247v2 | 7 |
| 2026-05-18 | [CoX-MoE: Coalesced Expert Execution for High-Throughput MoE Inference with AMX-Enabled CPU-GPU Co-Execution](https://arxiv.org/abs/2605.17889v2) | 2605.17889v2 | 8 |
| 2026-05-18 | [MoASE++: Mixture of Activation Sparsity Experts with Domain-Adaptive On-policy Distillation for Continual Test Time Adaptation](https://arxiv.org/abs/2605.17743v1) | 2605.17743v1 | 6 |
| 2026-05-17 | [Mixture of Experts for Low-Resource LLMs](https://arxiv.org/abs/2605.17598v1) | 2605.17598v1 | 15 |
| 2026-05-17 | [TAME: Test-Time Adversarial Prompt Tuning via Mixture-of-Experts for Vision-Language Models](https://arxiv.org/abs/2605.17577v1) | 2605.17577v1 | 6 |
| 2026-05-17 | [Stable Routing for Mixture-of-Experts in Class-Incremental Learning](https://arxiv.org/abs/2605.17571v1) | 2605.17571v1 | 8 |
| 2026-05-16 | [GoodServe: Globally-coordinated Routing of Agentic LLM Inferences for High Goodput](https://arxiv.org/abs/2605.16867v2) | 2605.16867v2 | 6 |
| 2026-05-16 | [SpaceMoE: Towards Orbital General Intelligence with Distributed Mixture-of-Experts Inference](https://arxiv.org/abs/2605.16849v1) | 2605.16849v1 | 10 |
| 2026-05-15 | [UB-SMoE: Universally Balanced Sparse Mixture-of-Experts for Resource-adaptive Federated Fine-tuning of Foundation Models](https://arxiv.org/abs/2605.16690v1) | 2605.16690v1 | 10 |
| 2026-05-15 | [Scalable Knowledge Editing for Mixture-of-Experts LLMs via Tensor-Structured Updates](https://arxiv.org/abs/2605.16686v1) | 2605.16686v1 | 8 |
| 2026-05-15 | [When Does Sparse MoE Help in Vision? The Role of Backbone Compute Leverage in Sparse Routing](https://arxiv.org/abs/2605.15484v1) | 2605.15484v1 | 8 |
| 2026-05-14 | [$φ$-Balancing for Mixture-of-Experts Training](https://arxiv.org/abs/2605.15403v1) | 2605.15403v1 | 6 |
| 2026-05-14 | [Deep Mixture of Experts Network for Resource Optimization in Aerial-Terrestrial CF-mMIMO Systems under URLLC](https://arxiv.org/abs/2605.15135v1) | 2605.15135v1 | 6 |
| 2026-05-14 | [An Interpretable Latency Model for Speculative Decoding in LLM Serving](https://arxiv.org/abs/2605.15051v1) | 2605.15051v1 | 8 |
| 2026-05-14 | [BEAM: Binary Expert Activation Masking for Dynamic Routing in MoE](https://arxiv.org/abs/2605.14438v1) | 2605.14438v1 | 6 |
| 2026-05-14 | [RQ-MoE: Residual Quantization via Mixture of Experts for Efficient Input-Dependent Vector Compression](https://arxiv.org/abs/2605.14359v1) | 2605.14359v1 | 6 |
| 2026-05-14 | [MetaMoE: Diversity-Aware Proxy Selection for Privacy-Preserving Mixture-of-Experts Unification](https://arxiv.org/abs/2605.14289v1) | 2605.14289v1 | 8 |
| 2026-05-13 | [How to Scale Mixture-of-Experts: From muP to the Maximally Scale-Stable Parameterization](https://arxiv.org/abs/2605.14200v1) | 2605.14200v1 | 7 |
| 2026-05-13 | [HodgeCover: Higher-Order Topological Coverage Drives Compression of Sparse Mixture-of-Experts](https://arxiv.org/abs/2605.13997v1) | 2605.13997v1 | 6 |
| 2026-05-13 | [Dense vs Sparse Pretraining at Tiny Scale: Active-Parameter vs Total-Parameter Matching](https://arxiv.org/abs/2605.13769v1) | 2605.13769v1 | 13 |
| 2026-05-13 | [A$_3$B$_2$: Adaptive Asymmetric Adapter for Alleviating Branch Bias in Vision-Language Image Classification with Few-Shot Learning](https://arxiv.org/abs/2605.13161v2) | 2605.13161v2 | 8 |
| 2026-05-12 | [Sparse Mixture-of-Experts Routing in Visual Diffusion Transformers:Diagnosis, Boundary Calibration and Evolutionary Roadmap from Routing Collapse to Selective Deadlock](https://arxiv.org/abs/2605.19378v1) | 2605.19378v1 | 8 |
| 2026-05-12 | [Routers Learn the Geometry of Their Experts: Geometric Coupling in Sparse Mixture-of-Experts](https://arxiv.org/abs/2605.12476v1) | 2605.12476v1 | 14 |
| 2026-05-12 | [ROMER: Expert Replacement and Router Calibration for Robust MoE LLMs on Analog Compute-in-Memory Systems](https://arxiv.org/abs/2605.11800v1) | 2605.11800v1 | 7 |
| 2026-05-12 | [M$^4$-SAM: Multi-Modal Mixture-of-Experts with Memory-Augmented SAM for RGB-D Video Salient Object Detection](https://arxiv.org/abs/2605.11760v1) | 2605.11760v1 | 6 |
| 2026-05-12 | [Slicing and Dicing: Configuring Optimal Mixtures of Experts](https://arxiv.org/abs/2605.11689v1) | 2605.11689v1 | 8 |
| 2026-05-11 | [Sieve: Dynamic Expert-Aware PIM Acceleration for Evolving Mixture-of-Experts Models](https://arxiv.org/abs/2605.11277v1) | 2605.11277v1 | 7 |
| 2026-05-11 | [HEBATRON: A Hebrew-Specialized Open-Weight Mixture-of-Experts Language Model](https://arxiv.org/abs/2605.11255v1) | 2605.11255v1 | 6 |
| 2026-05-11 | [DECO: Sparse Mixture-of-Experts with Dense-Comparable Performance on End-Side Devices](https://arxiv.org/abs/2605.10933v3) | 2605.10933v3 | 7 |
| 2026-05-11 | [CMKL: Modality-Aware Continual Learning for Evolving Biomedical Knowledge Graphs](https://arxiv.org/abs/2605.10510v1) | 2605.10510v1 | 6 |
| 2026-05-11 | [Fast Training of Mixture-of-Experts for Time Series Forecasting via Expert Loss Integration](https://arxiv.org/abs/2605.10330v3) | 2605.10330v3 | 6 |
| 2026-05-11 | [HELLoRA: Hot Experts Layer-Level Low-Rank Adaptation for Mixture-of-Experts Models](https://arxiv.org/abs/2605.18795v1) | 2605.18795v1 | 7 |
| 2026-05-10 | [Sparsity Moves Computation: How FFN Architecture Reshapes Attention in Small Transformers](https://arxiv.org/abs/2605.09403v2) | 2605.09403v2 | 9 |
| 2026-05-10 | [FLAME: Adaptive Mixture-of-Experts for Continual Multimodal Multi-Task Learning](https://arxiv.org/abs/2605.09355v2) | 2605.09355v2 | 8 |
| 2026-05-10 | [DisagMoE: Computation-Communication overlapped MoE Training via Disaggregated AF-Pipe Parallelism](https://arxiv.org/abs/2605.11005v1) | 2605.11005v1 | 6 |
| 2026-05-10 | [TileQ: Efficient Low-Rank Quantization of Mixture-of-Experts with 2D Tiling](https://arxiv.org/abs/2605.09281v1) | 2605.09281v1 | 6 |
| 2026-05-09 | [MicroFuse: Protein-to-Genome Expert Fusion for Microbial Operon Reasoning](https://arxiv.org/abs/2605.08815v1) | 2605.08815v1 | 6 |
| 2026-05-09 | [FLUX: Geometry-Aware Longitudinal Flow Matching with Mixture of Experts](https://arxiv.org/abs/2605.08648v1) | 2605.08648v1 | 16 |
| 2026-05-09 | [ReLibra: Routing-Replay-Guided Load Balancing for MoE Training in Reinforcement Learning](https://arxiv.org/abs/2605.08639v1) | 2605.08639v1 | 14 |
| 2026-05-09 | [Uncovering Intra-expert Activation Sparsity for Efficient Mixture-of-Expert Model Execution](https://arxiv.org/abs/2605.08575v1) | 2605.08575v1 | 8 |
| 2026-05-08 | [Is MoE Routing a Huffman Code? Discovering the Frequency-Diversity Law in Chain-of-Thought](https://arxiv.org/abs/2607.20427v1) | 2607.20427v1 | 9 |
| 2026-05-08 | [SDG-MoE: Signed Debate Graph Mixture-of-Experts](https://arxiv.org/abs/2605.08322v2) | 2605.08322v2 | 6 |
| 2026-05-08 | [DIMoE-Adapters: Dynamic Expert Evolution for Continual Learning in Vision-Language Models](https://arxiv.org/abs/2605.07494v1) | 2605.07494v1 | 8 |
| 2026-05-08 | [Hierarchical Mixture-of-Experts with Two-Stage Optimization](https://arxiv.org/abs/2605.08292v1) | 2605.08292v1 | 13 |
| 2026-05-08 | [When Are Experts Misrouted? Counterfactual Routing Analysis in Mixture-of-Experts Language Models](https://arxiv.org/abs/2605.07260v1) | 2605.07260v1 | 12 |
| 2026-05-08 | [Geometric Asymmetry in MoE Specialization: Functional Decorrelation and Representational Overlap](https://arxiv.org/abs/2605.16349v1) | 2605.16349v1 | 6 |
| 2026-05-08 | [Star Elastic: Many-in-One Reasoning LLMs with Efficient Budget Control](https://arxiv.org/abs/2605.07182v1) | 2605.07182v1 | 6 |
| 2026-05-07 | [UniPool: Learning Expert-to-Layer Ownership from Brief Global Access](https://arxiv.org/abs/2605.06665v2) | 2605.06665v2 | 6 |
| 2026-05-07 | [EMO: Pretraining Mixture of Experts for Emergent Modularity](https://arxiv.org/abs/2605.06663v2) | 2605.06663v2 | 11 |
| 2026-05-07 | [Scene-Adaptive Continual Learning for CSI-based Human Activity Recognition with Mixture of Experts](https://arxiv.org/abs/2605.06447v1) | 2605.06447v1 | 12 |
| 2026-05-07 | [E = T*H/(O+B): A Dimensionless Control Parameter for Mixture-of-Experts Ecology](https://arxiv.org/abs/2605.06415v2) | 2605.06415v2 | 8 |
| 2026-05-07 | [Dynamic Pondering Sparsity-aware Mixture-of-Experts Transformer for Event Stream based Visual Object Tracking](https://arxiv.org/abs/2605.06112v1) | 2605.06112v1 | 6 |
| 2026-05-06 | [Expert Routing for Communication-Efficient MoE via Finite Expert Banks](https://arxiv.org/abs/2605.05278v1) | 2605.05278v1 | 10 |
| 2026-05-06 | [Multi-Turn Distributed Inference with Mixture of Experts for 6G Edge--Cloud Networks](https://arxiv.org/abs/2607.02522v1) | 2607.02522v1 | 10 |
| 2026-05-06 | [You Snooze, You Lose: Automatic Safety Alignment Restoration through Neural Weight Translation](https://arxiv.org/abs/2605.04992v2) | 2605.04992v2 | 6 |
| 2026-05-06 | [Adaptive Inverted-Index Routing for Granular Mixtures-of-Experts](https://arxiv.org/abs/2605.04952v2) | 2605.04952v2 | 8 |
| 2026-05-06 | [AxMoE: Characterizing the Impact of Approximate Multipliers on Mixture-of-Experts DNN Architectures](https://arxiv.org/abs/2605.04754v1) | 2605.04754v1 | 6 |
| 2026-05-06 | [SPHERE: Mitigating the Loss of Spectral Plasticity in Mixture-of-Experts for Deep Reinforcement Learning](https://arxiv.org/abs/2605.04712v2) | 2605.04712v2 | 7 |
| 2026-05-06 | [GEM: Graph-Enhanced Mixture-of-Experts with ReAct Agents for Dialogue State Tracking](https://arxiv.org/abs/2605.04449v1) | 2605.04449v1 | 12 |
| 2026-05-06 | [Misrouter: Exploiting Routing Mechanisms for Input-Only Attacks on Mixture-of-Experts LLMs](https://arxiv.org/abs/2605.04446v1) | 2605.04446v1 | 10 |
| 2026-05-05 | [RD-ViT: Recurrent-Depth Vision Transformer for Semantic Segmentation with Reduced Data Dependence Extending the Recurrent-Depth Transformer Architecture to Dense Prediction](https://arxiv.org/abs/2605.03999v1) | 2605.03999v1 | 6 |
| 2026-05-05 | [Unified Multimodal Visual Tracking with Dual Mixture-of-Experts](https://arxiv.org/abs/2605.03716v1) | 2605.03716v1 | 6 |
| 2026-05-05 | [Ortho-Hydra: Orthogonalized Experts for DiT LoRA](https://arxiv.org/abs/2605.03252v1) | 2605.03252v1 | 6 |
| 2026-05-04 | [Soft-to-Hard Routing in Sparse Mixture-of-Experts Models](https://arxiv.org/abs/2605.02124v2) | 2605.02124v2 | 8 |
| 2026-05-01 | [PRISM: Exposing and Resolving Spurious Isolation in Federated Multimodal Continual Learning](https://arxiv.org/abs/2605.01061v1) | 2605.01061v1 | 8 |
| 2026-05-01 | [RouteHijack: Routing-Aware Attack on Mixture-of-Experts LLMs](https://arxiv.org/abs/2605.02946v1) | 2605.02946v1 | 10 |
| 2026-05-01 | [SpaceMoE: Realizing Distributed Mixture-of-Experts Inference over Space Networks](https://arxiv.org/abs/2605.00515v2) | 2605.00515v2 | 6 |
| 2026-05-01 | [PrefMoE: Robust Preference Modeling with Mixture-of-Experts Reward Learning](https://arxiv.org/abs/2605.00384v3) | 2605.00384v3 | 6 |
| 2026-04-30 | [Rethinking Network Topologies for Cost-Effective Mixture-of-Experts LLM Serving](https://arxiv.org/abs/2605.00254v1) | 2605.00254v1 | 6 |
| 2026-04-30 | [Prediction-powered Inference by Mixture of Experts](https://arxiv.org/abs/2604.27892v1) | 2604.27892v1 | 6 |
| 2026-04-30 | [MASCing: Configurable Mixture-of-Experts Behavior via Activation Steering Masks](https://arxiv.org/abs/2604.27818v1) | 2604.27818v1 | 6 |
| 2026-04-29 | [FaaSMoE: A Serverless Framework for Multi-Tenant Mixture-of-Experts Serving](https://arxiv.org/abs/2604.26881v1) | 2604.26881v1 | 6 |
| 2026-04-29 | [Advancing multi-site emission control: A physics-informed transfer learning framework with mixture of experts for carbon-pollutant synergy](https://arxiv.org/abs/2604.26571v2) | 2604.26571v2 | 10 |
| 2026-04-29 | [Adaptive and Fine-grained Module-wise Expert Pruning for Efficient LoRA-MoE Fine-Tuning](https://arxiv.org/abs/2604.26340v1) | 2604.26340v1 | 8 |
| 2026-04-29 | [Optimizing Tracking Accuracy in Energy-Constrained Multimodal ISAC via Lyapunov-Driven Heterogeneous Mixture-of-Experts](https://arxiv.org/abs/2604.26330v1) | 2604.26330v1 | 6 |
| 2026-04-28 | [Mixture of Experts Framework in Machine Learning Interatomic Potentials for Atomistic Simulations](https://arxiv.org/abs/2604.26143v1) | 2604.26143v1 | 10 |
| 2026-04-28 | [RaMP: Runtime-Aware Megakernel Polymorphism for Mixture-of-Experts](https://arxiv.org/abs/2604.26039v2) | 2604.26039v2 | 8 |
| 2026-04-27 | [SMoES: Soft Modality-Guided Expert Specialization in MoE-VLMs](https://arxiv.org/abs/2604.23996v2) | 2604.23996v2 | 8 |
| 2026-04-25 | [Scaling Multi-Node Mixture-of-Experts Inference Using Expert Activation Patterns](https://arxiv.org/abs/2604.23150v1) | 2604.23150v1 | 7 |
| 2026-04-25 | [Mixture of Heterogeneous Grouped Experts for Language Modeling](https://arxiv.org/abs/2604.23108v2) | 2604.23108v2 | 8 |
| 2026-04-23 | [Rethinking Cross-Domain Evaluation for Face Forgery Detection with Semantic Fine-grained Alignment and Mixture-of-Experts](https://arxiv.org/abs/2604.21478v1) | 2604.21478v1 | 6 |
| 2026-04-23 | [Teacher-Guided Routing for Sparse Vision Mixture-of-Experts](https://arxiv.org/abs/2604.21330v1) | 2604.21330v1 | 12 |
| 2026-04-22 | [On Bayesian Softmax-Gated Mixture-of-Experts Models](https://arxiv.org/abs/2604.20551v1) | 2604.20551v1 | 6 |
| 2026-04-22 | [C$^2$MOE: Consistency and Complementarity-guided Mixture of Experts for Incomplete Multimodal Emotion Learning](https://arxiv.org/abs/2608.04013v1) | 2608.04013v1 | 6 |
| 2026-04-22 | [Temporally Extended Mixture-of-Experts Models](https://arxiv.org/abs/2604.20156v1) | 2604.20156v1 | 7 |
| 2026-04-21 | [FEPLB: Exploiting Copy Engines for Nearly Free MoE Load Balancing in Distributed Training](https://arxiv.org/abs/2604.19654v1) | 2604.19654v1 | 10 |
| 2026-04-21 | [ReaLB: Real-Time Load Balancing for Multimodal MoE Inference](https://arxiv.org/abs/2604.19503v3) | 2604.19503v3 | 10 |
| 2026-04-21 | [Quadruped Parkour Learning: Sparsely Gated Mixture of Experts with Visual Input](https://arxiv.org/abs/2604.19344v1) | 2604.19344v1 | 11 |
| 2026-04-21 | [Expert Upcycling: Shifting the Compute-Efficient Frontier of Mixture-of-Experts](https://arxiv.org/abs/2604.19835v2) | 2604.19835v2 | 19 |
| 2026-04-21 | [SAMoRA: Semantic-Aware Mixture of LoRA Experts for Task-Adaptive Learning](https://arxiv.org/abs/2604.19048v1) | 2604.19048v1 | 7 |
| 2026-04-20 | [Multi-Domain Learning with Global Expert Mapping](https://arxiv.org/abs/2604.18842v1) | 2604.18842v1 | 6 |
| 2026-04-20 | [Efficient Mixture-of-Experts LLM Inference with Apple Silicon NPUs](https://arxiv.org/abs/2604.18788v1) | 2604.18788v1 | 10 |
| 2026-04-20 | [Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts](https://arxiv.org/abs/2604.18473v2) | 2604.18473v2 | 9 |
| 2026-04-20 | [Polysemantic Experts, Monosemantic Paths: Routing as Control in MoEs](https://arxiv.org/abs/2604.17837v1) | 2604.17837v1 | 6 |
| 2026-04-20 | [MoE-nD: Per-Layer Mixture-of-Experts Routing for Multi-Axis KV Cache Compression](https://arxiv.org/abs/2604.17695v1) | 2604.17695v1 | 6 |
| 2026-04-19 | [MACS: Modality-Aware Capacity Scaling for Efficient Multimodal MoE Inference](https://arxiv.org/abs/2605.05225v3) | 2605.05225v3 | 9 |
| 2026-04-19 | [Layer-wise MoE Routing Locality under Shared-Prefix Code Generation: Token-Identity Decomposition and Compile-Equivalent Fork Redundancy](https://arxiv.org/abs/2604.17182v1) | 2604.17182v1 | 8 |
| 2026-04-18 | [IMA-MoE: An Interpretable Modality-Aware Mixture-of-Experts Framework for Characterizing the Neurobiological Signatures of Binge Eating Disorder](https://arxiv.org/abs/2604.17028v1) | 2604.17028v1 | 6 |
| 2026-04-18 | [CoGR-MoE: Concept-Guided Expert Routing with Consistent Selection and Flexible Reasoning for Visual Question Answering](https://arxiv.org/abs/2604.16930v1) | 2604.16930v1 | 10 |
| 2026-04-17 | [Application of a Mixture of Experts-based Foundation Model to the GlueX DIRC Detector](https://arxiv.org/abs/2604.24775v1) | 2604.24775v1 | 10 |
| 2026-04-17 | [MOMENTA: Mixture-of-Experts Over Multimodal Embeddings with Neural Temporal Aggregation for Misinformation Detection](https://arxiv.org/abs/2604.16172v1) | 2604.16172v1 | 6 |
| 2026-04-16 | [Towards Faster Language Model Inference Using Mixture-of-Experts Flow Matching](https://arxiv.org/abs/2604.15009v1) | 2604.15009v1 | 6 |
| 2026-04-16 | [Geometric Metrics for MoE Specialization: From Fisher Information to Early Failure Detection](https://arxiv.org/abs/2604.14500v1) | 2604.14500v1 | 9 |
| 2026-04-15 | [Geometric Routing Enables Causal Expert Control in Mixture of Experts](https://arxiv.org/abs/2604.14434v1) | 2604.14434v1 | 12 |
| 2026-04-15 | [Equifinality in Mixture of Experts: Routing Topology Does Not Determine Language Modeling Quality](https://arxiv.org/abs/2604.14419v1) | 2604.14419v1 | 12 |
| 2026-04-15 | [Design and Behavior of Sparse Mixture-of-Experts Layers in CNN-based Semantic Segmentation](https://arxiv.org/abs/2604.13761v1) | 2604.13761v1 | 8 |
| 2026-04-15 | [Awakening Dormant Experts:Counterfactual Routing to Mitigate MoE Hallucinations](https://arxiv.org/abs/2604.14246v2) | 2604.14246v2 | 7 |
| 2026-04-15 | [Enhancing Mixture-of-Experts Specialization via Cluster-Aware Upcycling](https://arxiv.org/abs/2604.13508v2) | 2604.13508v2 | 8 |
| 2026-04-14 | [Efficient Handwriting-Based Alzheimer,s Disease Diagnosis Using a Low-Rank Mixture of Experts Deep Learning Framework](https://arxiv.org/abs/2605.04079v1) | 2605.04079v1 | 6 |
| 2026-04-13 | [TriFit: Trimodal Fusion with Protein Dynamics for Mutation Fitness Prediction](https://arxiv.org/abs/2604.12026v1) | 2604.12026v1 | 6 |
| 2026-04-13 | [Hyper-FEOD: Sparse Hypergraph-Enhanced Frame-Event Object Detection with Fine-Grained MoE](https://arxiv.org/abs/2604.11140v2) | 2604.11140v2 | 6 |
| 2026-04-12 | [WaveMoE: A Wavelet-Enhanced Mixture-of-Experts Foundation Model for Time Series Forecasting](https://arxiv.org/abs/2604.10544v1) | 2604.10544v1 | 11 |
| 2026-04-12 | [CodeQuant: Unified Clustering and Quantization for Enhanced Outlier Smoothing in Low-Precision Mixture-of-Experts](https://arxiv.org/abs/2604.10496v2) | 2604.10496v2 | 6 |
| 2026-04-11 | [SpecMoE: A Fast and Efficient Mixture-of-Experts Inference via Self-Assisted Speculative Decoding](https://arxiv.org/abs/2604.10152v1) | 2604.10152v1 | 6 |
| 2026-04-10 | [The Myth of Expert Specialization in MoEs: Why Routing Reflects Geometry, Not Necessarily Domain Expertise](https://arxiv.org/abs/2604.09780v1) | 2604.09780v1 | 6 |
| 2026-04-10 | [Compositional-Degradation UAV Image Restoration: Conditional Decoupled MoE Network and A Benchmark](https://arxiv.org/abs/2604.09313v1) | 2604.09313v1 | 8 |
| 2026-04-10 | [Generalization and Scaling Laws for Mixture-of-Experts Transformers](https://arxiv.org/abs/2604.09175v2) | 2604.09175v2 | 7 |
| 2026-04-10 | [MP-ISMoE: Mixed-Precision Interactive Side Mixture-of-Experts for Efficient Transfer Learning](https://arxiv.org/abs/2605.04058v1) | 2605.04058v1 | 7 |
| 2026-04-10 | [Plasticity-Enhanced Multi-Agent Mixture of Experts for Dynamic Objective Adaptation in UAVs-Assisted Emergency Communication Networks](https://arxiv.org/abs/2604.09028v1) | 2604.09028v1 | 8 |
| 2026-04-09 | [Seeing but Not Thinking: Routing Distraction in Multimodal Mixture-of-Experts](https://arxiv.org/abs/2604.08541v1) | 2604.08541v1 | 6 |
| 2026-04-09 | [Alloc-MoE: Budget-Aware Expert Activation Allocation for Efficient Mixture-of-Experts Inference](https://arxiv.org/abs/2604.08133v1) | 2604.08133v1 | 7 |
| 2026-04-08 | [Region-Graph Optimal Transport Routing for Mixture-of-Experts Whole-Slide Image Classification](https://arxiv.org/abs/2604.07298v1) | 2604.07298v1 | 6 |
| 2026-04-08 | [MoE Routing Testbed: Studying Expert Specialization and Routing Behavior at Small Scale](https://arxiv.org/abs/2604.07030v1) | 2604.07030v1 | 6 |
| 2026-04-08 | [Heterogeneous Mixture-of-Experts for Energy-Efficient Multimodal ISAC in Highly Mobile Networks](https://arxiv.org/abs/2604.06697v1) | 2604.06697v1 | 6 |
| 2026-04-07 | [Efficient Quantization of Mixture-of-Experts with Theoretical Generalization Guarantees](https://arxiv.org/abs/2604.06515v1) | 2604.06515v1 | 9 |
| 2026-04-07 | [Agentic AI-Based Joint Computing and Networking via Mixture of Experts and Large Language Models](https://arxiv.org/abs/2605.02911v1) | 2605.02911v1 | 6 |
| 2026-04-07 | [Cross-Platform Fused MoE Dispatch in Triton: Portable Expert Routing Without CUDA](https://arxiv.org/abs/2605.23911v1) | 2605.23911v1 | 14 |
| 2026-04-07 | [TalkLoRA: Communication-Aware Mixture of Low-Rank Adaptation for Large Language Models](https://arxiv.org/abs/2604.06291v1) | 2604.06291v1 | 8 |
| 2026-04-07 | [QA-MoE: Towards a Continuous Reliability Spectrum with Quality-Aware Mixture of Experts for Robust Multimodal Sentiment Analysis](https://arxiv.org/abs/2604.05704v2) | 2604.05704v2 | 14 |
| 2026-04-06 | [HI-MoE: Hierarchical Instance-Conditioned Mixture-of-Experts for Object Detection](https://arxiv.org/abs/2604.04908v1) | 2604.04908v1 | 8 |
| 2026-04-06 | [REAM: Merging Improves Pruning of Experts in LLMs](https://arxiv.org/abs/2604.04356v1) | 2604.04356v1 | 6 |
| 2026-04-05 | [Three Phases of Expert Routing: How Load Balance Evolves During Mixture-of-Experts Training](https://arxiv.org/abs/2604.04230v1) | 2604.04230v1 | 14 |
| 2026-04-05 | [SARES-DEIM: Sparse Mixture-of-Experts Meets DETR for Clutter-Aware SAR Ship Detection](https://arxiv.org/abs/2604.04127v2) | 2604.04127v2 | 6 |
| 2026-04-04 | [Unveiling Language Routing Isolation in Multilingual MoE Models for Interpretable Subnetwork Adaptation](https://arxiv.org/abs/2604.03592v2) | 2604.03592v2 | 8 |
| 2026-04-03 | [Mixture-of-Experts in Remote Sensing: A Survey](https://arxiv.org/abs/2604.03342v1) | 2604.03342v1 | 6 |
| 2026-04-03 | [FluxMoE: Decoupling Expert Residency for High-Performance MoE Serving](https://arxiv.org/abs/2604.02715v3) | 2604.02715v3 | 9 |
| 2026-04-02 | [The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expert Level](https://arxiv.org/abs/2604.02178v2) | 2604.02178v2 | 9 |
| 2026-04-02 | [FourierMoE: Fourier Mixture-of-Experts Adaptation of Large Language Models](https://arxiv.org/abs/2604.01762v1) | 2604.01762v1 | 8 |
| 2026-04-02 | [Expert-Choice Routing Enables Adaptive Computation in Diffusion Language Models](https://arxiv.org/abs/2604.01622v2) | 2604.01622v2 | 10 |
| 2026-04-01 | [StanceMoE: Mixture-of-Experts Architecture for Stance Detection](https://arxiv.org/abs/2604.00878v2) | 2604.00878v2 | 6 |
| 2026-04-01 | [Cost-Penalized Fitness in FMA-Orchestrated Mixture of Experts: Experimental Evidence for Molecular Memory in Domain Adaptation](https://arxiv.org/abs/2604.00812v1) | 2604.00812v1 | 10 |
| 2026-04-01 | [Routing-Free Mixture-of-Experts](https://arxiv.org/abs/2604.00801v1) | 2604.00801v1 | 12 |
| 2026-04-01 | [Scalable Pretraining of Large Mixture of Experts Language Models on Aurora Super Computer](https://arxiv.org/abs/2604.00785v1) | 2604.00785v1 | 7 |
| 2026-04-01 | [Self-Routing: Parameter-Free Expert Routing from Hidden States](https://arxiv.org/abs/2604.00421v3) | 2604.00421v3 | 12 |
| 2026-03-31 | [PASM: Population Adaptive Symbolic Mixture-of-Experts Model for Cross-location Hurricane Evacuation Decision Prediction](https://arxiv.org/abs/2604.00074v1) | 2604.00074v1 | 6 |
| 2026-03-31 | [TrafficMoE: Heterogeneity-aware Mixture of Experts for Encrypted Traffic Classification](https://arxiv.org/abs/2603.29520v1) | 2603.29520v1 | 10 |
| 2026-03-31 | [Route-Induced Density and Stability (RIDE): Controlled Intervention and Mechanism Analysis of Routing-Style Meta Prompts on LLM Internal States](https://arxiv.org/abs/2603.29206v1) | 2603.29206v1 | 6 |
| 2026-03-30 | [ExFusion: Efficient Transformer Training via Multi-Experts Fusion](https://arxiv.org/abs/2603.27965v2) | 2603.27965v2 | 6 |
| 2026-03-29 | [On Token's Dilemma: Dynamic MoE with Drift-Aware Token Assignment for Continual Learning of Large Vision Language Models](https://arxiv.org/abs/2603.27481v1) | 2603.27481v1 | 6 |
| 2026-03-28 | [Persistent Memory Through Triple-Loop Consolidation Under Stochastic Unit Turnover](https://arxiv.org/abs/2603.27188v3) | 2603.27188v3 | 8 |
| 2026-03-26 | [MP-MoE: Matrix Profile-Guided Mixture of Experts for Precipitation Forecasting](https://arxiv.org/abs/2603.25046v1) | 2603.25046v1 | 6 |
| 2026-03-26 | [MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](https://arxiv.org/abs/2603.24984v2) | 2603.24984v2 | 14 |
| 2026-03-26 | [CROSS: A Mixture-of-Experts Reinforcement Learning Framework for Generalizable Large-Scale Traffic Signal Control](https://arxiv.org/abs/2603.24930v1) | 2603.24930v1 | 6 |
| 2026-03-25 | [B-MoE: A Body-Part-Aware Mixture-of-Experts "All Parts Matter" Approach to Micro-Action Recognition](https://arxiv.org/abs/2603.24245v3) | 2603.24245v3 | 6 |
| 2026-03-25 | [LGEST: Dynamic Spatial-Spectral Expert Routing for Hyperspectral Image Classification](https://arxiv.org/abs/2603.24045v1) | 2603.24045v1 | 10 |
| 2026-03-25 | [MoE-Sieve: Routing-Guided LoRA for Efficient MoE Fine-Tuning](https://arxiv.org/abs/2603.24044v1) | 2603.24044v1 | 8 |
| 2026-03-25 | [SiftMoE: Similarity-Aware Energy-Efficient Expert Selection for Wireless Distributed MoE Inference](https://arxiv.org/abs/2603.23888v2) | 2603.23888v2 | 6 |
| 2026-03-24 | [Similarity-Aware Mixture-of-Experts for Data-Efficient Continual Learning](https://arxiv.org/abs/2603.23436v1) | 2603.23436v1 | 6 |
| 2026-03-23 | [Holistic Scaling Laws for Optimal Mixture-of-Experts Architecture Optimization](https://arxiv.org/abs/2603.21862v2) | 2603.21862v2 | 7 |
| 2026-03-22 | [Federated Mixture-of-Experts Alignment on Mobile Edge Networks under Data Heterogeneity](https://arxiv.org/abs/2603.21276v2) | 2603.21276v2 | 6 |
| 2026-03-22 | [QMoP: Query Guided Mixture-of-Projector for Efficient Visual Token Compression](https://arxiv.org/abs/2603.21232v1) | 2603.21232v1 | 6 |
| 2026-03-22 | [Mixture of Chapters: Scaling Learnt Memory in Transformers](https://arxiv.org/abs/2603.21096v1) | 2603.21096v1 | 7 |
| 2026-03-21 | [Distilled Large Language Model-Driven Dynamic Sparse Expert Activation Mechanism](https://arxiv.org/abs/2603.26735v1) | 2603.26735v1 | 10 |
| 2026-03-20 | [Mixture of Experts with Soft Nearest Neighbor Loss: Resolving Expert Collapse via Representation Disentanglement](https://arxiv.org/abs/2603.26734v1) | 2603.26734v1 | 10 |
| 2026-03-20 | [Geometric Mixture-of-Experts with Curvature-Guided Adaptive Routing for Graph Representation Learning](https://arxiv.org/abs/2603.22317v1) | 2603.22317v1 | 6 |
| 2026-03-19 | [Scalable Prompt Routing via Fine-Grained Latent Task Discovery](https://arxiv.org/abs/2603.19415v2) | 2603.19415v2 | 6 |
| 2026-03-19 | [ATG-MoE: Autoregressive trajectory generation with mixture-of-experts for assembly skill learning](https://arxiv.org/abs/2603.19029v1) | 2603.19029v1 | 10 |
| 2026-03-18 | [Path-Constrained Mixture-of-Experts](https://arxiv.org/abs/2603.18297v2) | 2603.18297v2 | 8 |
| 2026-03-17 | [Knowledge Localization in Mixture-of-Experts LLMs Using Cross-Lingual Inconsistency](https://arxiv.org/abs/2603.17102v1) | 2603.17102v1 | 8 |
| 2026-03-17 | [SpecMoE: Spectral Mixture-of-Experts Foundation Model for Cross-Species EEG Decoding](https://arxiv.org/abs/2603.16739v2) | 2603.16739v2 | 10 |
| 2026-03-17 | [AW-MoE: All-Weather Mixture of Experts for Robust Multi-Modal 3D Object Detection](https://arxiv.org/abs/2603.16261v1) | 2603.16261v1 | 6 |
| 2026-03-16 | [Bridging Local and Global Knowledge: Cascaded Mixture-of-Experts Learning for Near-Shortest Path Routing](https://arxiv.org/abs/2603.15541v1) | 2603.15541v1 | 10 |
| 2026-03-16 | [MoE-ACT: Scaling Multi-Task Bimanual Manipulation with Sparse Task-Conditioned Mixture-of-Experts Transformers](https://arxiv.org/abs/2603.15265v2) | 2603.15265v2 | 7 |
| 2026-03-14 | [Sparse-Dense Mixture of Experts Adapter for Multi-Modal Tracking](https://arxiv.org/abs/2603.13719v1) | 2603.13719v1 | 6 |
| 2026-03-13 | [MoEKD: Mixture-of-Experts Knowledge Distillation for Robust and High-Performing Compressed Code Models](https://arxiv.org/abs/2603.13213v1) | 2603.13213v1 | 12 |
| 2026-03-13 | [LightMoE: Reducing Mixture-of-Experts Redundancy through Expert Replacing](https://arxiv.org/abs/2603.12645v1) | 2603.12645v1 | 6 |
| 2026-03-13 | [Expert Pyramid Tuning: Efficient Parameter Fine-Tuning for Expertise-Driven Task Allocation](https://arxiv.org/abs/2603.12577v1) | 2603.12577v1 | 6 |
| 2026-03-12 | [Expert Threshold Routing for Autoregressive Language Modeling with Dynamic Computation Allocation and Load Balancing](https://arxiv.org/abs/2603.11535v1) | 2603.11535v1 | 11 |
| 2026-03-11 | [Task-Conditioned Routing Signatures in Sparse Mixture-of-Experts Transformers](https://arxiv.org/abs/2603.11114v1) | 2603.11114v1 | 7 |
| 2026-03-11 | [Optimal Expert-Attention Allocation in Mixture-of-Experts: A Scalable Law for Dynamic Model Design](https://arxiv.org/abs/2603.10379v1) | 2603.10379v1 | 7 |
| 2026-03-10 | [Variational Routing: A Scalable Bayesian Framework for Calibrated Mixture-of-Experts Transformers](https://arxiv.org/abs/2603.09453v3) | 2603.09453v3 | 6 |
| 2026-03-09 | [LAR-MoE: Latent-Aligned Routing for Mixture of Experts in Robotic Imitation Learning](https://arxiv.org/abs/2603.08476v1) | 2603.08476v1 | 14 |
| 2026-03-09 | [Speculating Experts Accelerates Inference for Mixture-of-Experts](https://arxiv.org/abs/2603.19289v1) | 2603.19289v1 | 9 |
| 2026-03-09 | [Mixture of experts architectures for machine learning interatomic potentials](https://arxiv.org/abs/2603.07977v3) | 2603.07977v3 | 10 |
| 2026-03-08 | [Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685v2) | 2603.07685v2 | 7 |
| 2026-03-08 | [Mixed Effects Mixture of Experts: Modeling Double Heterogeneous Trajectories](https://arxiv.org/abs/2603.07479v1) | 2603.07479v1 | 6 |
| 2026-03-08 | [Local Precise Refinement: A Dual-Gated Mixture-of-Experts for Enhancing Foundation Model Generalization against Spectral Shifts](https://arxiv.org/abs/2603.13352v3) | 2603.13352v3 | 6 |
| 2026-03-06 | [A Mixture-of-Experts Framework for Practical Hybrid-Quantum Models in Credit Card Fraud Detection](https://arxiv.org/abs/2603.06473v2) | 2603.06473v2 | 6 |
| 2026-03-06 | [WMoE-CLIP: Wavelet-Enhanced Mixture-of-Experts Prompt Learning for Zero-Shot Anomaly Detection](https://arxiv.org/abs/2603.06313v1) | 2603.06313v1 | 6 |
| 2026-03-06 | [GazeMoE: Perception of Gaze Target with Mixture-of-Experts](https://arxiv.org/abs/2603.06256v1) | 2603.06256v1 | 6 |
| 2026-03-06 | [MoE Lens -- An Expert Is All You Need](https://arxiv.org/abs/2603.05806v1) | 2603.05806v1 | 9 |
| 2026-03-06 | [Sparse Crosscoders for diffing MoEs and Dense models](https://arxiv.org/abs/2603.05805v1) | 2603.05805v1 | 13 |
| 2026-03-05 | [NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046v1) | 2603.05046v1 | 6 |
| 2026-03-05 | [Mixture of Universal Experts: Scaling Virtual Width via Depth-Width Transformation](https://arxiv.org/abs/2603.04971v1) | 2603.04971v1 | 7 |
| 2026-03-05 | [TSEmbed: Unlocking Task Scaling in Universal Multimodal Embeddings](https://arxiv.org/abs/2603.04772v1) | 2603.04772v1 | 9 |
| 2026-03-04 | [RANGER: Sparsely-Gated Mixture-of-Experts with Adaptive Retrieval Re-ranking for Pathology Report Generation](https://arxiv.org/abs/2603.04348v1) | 2603.04348v1 | 10 |
| 2026-03-04 | [CAMMSR: Category-Guided Attentive Mixture of Experts for Multimodal Sequential Recommendation](https://arxiv.org/abs/2603.04320v1) | 2603.04320v1 | 6 |
| 2026-03-03 | [Modeling Cross-vision Synergy for Unified Large Vision Model](https://arxiv.org/abs/2603.03564v1) | 2603.03564v1 | 6 |
| 2026-03-03 | [CMoE: Contrastive Mixture of Experts for Motion Control and Terrain Adaptation of Humanoid Robots](https://arxiv.org/abs/2603.03067v2) | 2603.03067v2 | 6 |
| 2026-03-03 | [Robust Heterogeneous Analog-Digital Computing for Mixture-of-Experts Models with Theoretical Generalization Guarantees](https://arxiv.org/abs/2603.02633v1) | 2603.02633v1 | 6 |
| 2026-03-02 | [DynaMoE: Dynamic Token-Level Expert Activation with Layer-Wise Adaptive Capacity for Mixture-of-Experts Neural Networks](https://arxiv.org/abs/2603.01697v1) | 2603.01697v1 | 9 |
| 2026-03-02 | [Multimodal Mixture-of-Experts with Retrieval Augmentation for Protein Active Site Identification](https://arxiv.org/abs/2603.01511v2) | 2603.01511v2 | 6 |
| 2026-03-02 | [Fed-GAME: Personalized Federated Learning with Graph Attention Mixture-of-Experts For Time-Series Forecasting](https://arxiv.org/abs/2603.01363v1) | 2603.01363v1 | 6 |
| 2026-02-27 | [Quant Experts: Token-aware Adaptive Error Reconstruction with Mixture of Experts for Large Vision-Language Models Quantization](https://arxiv.org/abs/2602.24059v1) | 2602.24059v1 | 10 |
| 2026-02-26 | [A Mixture-of-Experts Model for Multimodal Emotion Recognition in Conversations](https://arxiv.org/abs/2602.23300v1) | 2602.23300v1 | 6 |
| 2026-02-26 | [Switch-Hurdle: A MoE Encoder with AR Hurdle Decoder for Intermittent Demand Forecasting](https://arxiv.org/abs/2602.22685v1) | 2602.22685v1 | 8 |
| 2026-02-25 | [TiMi: Empower Time Series Transformers with Multimodal Mixture of Experts](https://arxiv.org/abs/2602.21693v2) | 2602.21693v2 | 10 |
| 2026-02-23 | [A Replicate-and-Quantize Strategy for Plug-and-Play Load Balancing of Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2602.19938v2) | 2602.19938v2 | 18 |
| 2026-02-23 | [Towards Dexterous Embodied Manipulation via Deep Multi-Sensory Fusion and Sparse Expert Scaling](https://arxiv.org/abs/2602.19764v1) | 2602.19764v1 | 11 |
| 2026-02-23 | [EMS-FL: Federated Tuning of Mixture-of-Experts in Satellite-Terrestrial Networks via Expert-Driven Model Splitting](https://arxiv.org/abs/2602.19485v1) | 2602.19485v1 | 6 |
| 2026-02-22 | [Robust Exploration in Directed Controller Synthesis via Reinforcement Learning with Soft Mixture-of-Experts](https://arxiv.org/abs/2602.19244v1) | 2602.19244v1 | 6 |
| 2026-02-22 | [Grouter: Decoupling Routing from Representation for Accelerated MoE Training](https://arxiv.org/abs/2603.06626v2) | 2603.06626v2 | 7 |
| 2026-02-22 | [Routing-Aware Explanations for Mixture of Experts Graph Models in Malware Detection](https://arxiv.org/abs/2602.19025v1) | 2602.19025v1 | 12 |
| 2026-02-19 | [Grassmannian Mixture-of-Experts: Concentration-Controlled Routing on Subspace Manifolds](https://arxiv.org/abs/2602.17798v1) | 2602.17798v1 | 8 |
| 2026-02-19 | [Phase-Aware Mixture of Experts for Agentic Reinforcement Learning](https://arxiv.org/abs/2602.17038v3) | 2602.17038v3 | 12 |
| 2026-02-19 | [Arcee Trinity Large Technical Report](https://arxiv.org/abs/2602.17004v1) | 2602.17004v1 | 8 |
| 2026-02-17 | [ExpertWeaver: Unlocking the Inherent MoE in Dense LLMs with GLU Activation Patterns](https://arxiv.org/abs/2602.15521v1) | 2602.15521v1 | 10 |
| 2026-02-16 | [Mixture-of-Experts under Finite-Rate Gating: Communication--Generalization Trade-offs](https://arxiv.org/abs/2602.15091v2) | 2602.15091v2 | 6 |
| 2026-02-15 | [Synergistic Intra- and Cross-Layer Regularization Losses for MoE Expert Specialization](https://arxiv.org/abs/2602.14159v1) | 2602.14159v1 | 8 |
| 2026-02-15 | [Geometry-Preserving Aggregation for Mixture-of-Experts Embedding Models](https://arxiv.org/abs/2602.14039v1) | 2602.14039v1 | 6 |
| 2026-02-14 | [Mixture-of-experts Wishart model for covariance matrices with an application to Cancer drug screening](https://arxiv.org/abs/2602.13888v1) | 2602.13888v1 | 6 |
| 2026-02-13 | [Multi-Head Attention as a Source of Catastrophic Forgetting in MoE Transformers](https://arxiv.org/abs/2602.12587v1) | 2602.12587v1 | 6 |
| 2026-02-12 | [LAER-MoE: Load-Adaptive Expert Re-layout for Efficient Mixture-of-Experts Training](https://arxiv.org/abs/2602.11686v1) | 2602.11686v1 | 10 |
| 2026-02-12 | [Evolutionary Router Feature Generation for Zero-Shot Graph Anomaly Detection with Mixture-of-Experts](https://arxiv.org/abs/2602.11622v1) | 2602.11622v1 | 9 |
| 2026-02-12 | [Pretraining A Large Language Model using Distributed GPUs: A Memory-Efficient Decentralized Paradigm](https://arxiv.org/abs/2602.11543v3) | 2602.11543v3 | 8 |
| 2026-02-11 | [MoEEdit: Efficient and Routing-Stable Knowledge Editing for Mixture-of-Experts LLMs](https://arxiv.org/abs/2602.10965v1) | 2602.10965v1 | 9 |
| 2026-02-10 | [Area-Efficient In-Memory Computing for Mixture-of-Experts via Multiplexing and Caching](https://arxiv.org/abs/2602.10254v1) | 2602.10254v1 | 8 |
| 2026-02-10 | [Is Retraining-Free Enough? The Necessity of Router Calibration for Efficient MoE Compression](https://arxiv.org/abs/2603.02217v1) | 2603.02217v1 | 7 |
| 2026-02-10 | [Expert Divergence Learning for MoE-based Language Models](https://arxiv.org/abs/2603.00054v1) | 2603.00054v1 | 9 |
| 2026-02-10 | [SMES: Towards Scalable Multi-Task Recommendation via Expert Sparsity](https://arxiv.org/abs/2602.09386v1) | 2602.09386v1 | 9 |
| 2026-02-10 | [MalMoE: Mixture-of-Experts Enhanced Encrypted Malicious Traffic Detection Under Graph Drift](https://arxiv.org/abs/2602.10157v1) | 2602.10157v1 | 10 |
| 2026-02-09 | [Generalizing GNNs with Tokenized Mixture of Experts](https://arxiv.org/abs/2602.09258v2) | 2602.09258v2 | 10 |
| 2026-02-09 | [DirMoE: Dirichlet-routed Mixture of Experts](https://arxiv.org/abs/2602.09001v1) | 2602.09001v1 | 12 |
| 2026-02-09 | [Align and Adapt: Multimodal Multiview Human Activity Recognition under Arbitrary View Combinations](https://arxiv.org/abs/2602.08755v3) | 2602.08755v3 | 8 |
| 2026-02-09 | [Large Language Lobotomy: Jailbreaking Mixture-of-Experts via Expert Silencing](https://arxiv.org/abs/2602.08741v1) | 2602.08741v1 | 11 |
| 2026-02-09 | [Sparse Models, Sparse Safety: Unsafe Routes in Mixture-of-Experts LLMs](https://arxiv.org/abs/2602.08621v1) | 2602.08621v1 | 9 |
| 2026-02-09 | [TEAM: Temporal-Spatial Consistency Guided Expert Activation for MoE Diffusion Language Model Acceleration](https://arxiv.org/abs/2602.08404v3) | 2602.08404v3 | 8 |
| 2026-02-09 | [Tighnari v2: Mitigating Label Noise and Distribution Shift in Multimodal Plant Distribution Prediction via Mixture of Experts and Weakly Supervised Learning](https://arxiv.org/abs/2602.08282v1) | 2602.08282v1 | 10 |
| 2026-02-08 | [Efficient and Adaptable Detection of Malicious LLM Prompts via Bootstrap Aggregation](https://arxiv.org/abs/2602.08062v2) | 2602.08062v2 | 6 |
| 2026-02-08 | [The Rise of Sparse Mixture-of-Experts: A Survey from Algorithmic Foundations to Decentralized Architectures and Vertical Domain Applications](https://arxiv.org/abs/2602.08019v1) | 2602.08019v1 | 11 |
| 2026-02-08 | [Fast Model Selection and Stable Optimization for Softmax-Gated Multinomial-Logistic Mixture of Experts Models](https://arxiv.org/abs/2602.07997v1) | 2602.07997v1 | 10 |
| 2026-02-07 | [When the Model Said 'No Comment', We Knew Helpfulness Was Dead, Honesty Was Alive, and Safety Was Terrified](https://arxiv.org/abs/2602.07381v1) | 2602.07381v1 | 8 |
| 2026-02-05 | [MoSE: Mixture of Slimmable Experts for Efficient and Adaptive Language Models](https://arxiv.org/abs/2602.06154v2) | 2602.06154v2 | 6 |
| 2026-02-05 | [OmniMoE: An Efficient MoE by Orchestrating Atomic Experts at Scale](https://arxiv.org/abs/2602.05711v2) | 2602.05711v2 | 6 |
| 2026-02-04 | [Rule-Based Spatial Mixture-of-Experts U-Net for Explainable Edge Detection](https://arxiv.org/abs/2602.05100v2) | 2602.05100v2 | 6 |
| 2026-02-04 | [ERNIE 5.0 Technical Report](https://arxiv.org/abs/2602.04705v1) | 2602.04705v1 | 9 |
| 2026-02-04 | [Routing-Aware Safety Alignment for Mixture-of-Experts Models](https://arxiv.org/abs/2602.04448v4) | 2602.04448v4 | 6 |
| 2026-02-03 | [SpecMD: A Comprehensive Study On Speculative Expert Prefetching](https://arxiv.org/abs/2602.03921v1) | 2602.03921v1 | 8 |
| 2026-02-02 | [Edge-Aligned Initialization of Kernels for Steered Mixture-of-Experts](https://arxiv.org/abs/2602.02031v1) | 2602.02031v1 | 6 |
| 2026-02-02 | [SAME: Stabilized Mixture-of-Experts for Multimodal Continual Instruction Tuning](https://arxiv.org/abs/2602.01990v3) | 2602.01990v3 | 17 |
| 2026-02-02 | [Mixture-of-Experts with Intermediate CTC Supervision for Accented Speech Recognition](https://arxiv.org/abs/2602.01967v1) | 2602.01967v1 | 6 |
| 2026-02-01 | [A Statistical Theory of Gated Attention through the Lens of Hierarchical Mixture of Experts](https://arxiv.org/abs/2602.01468v1) | 2602.01468v1 | 6 |
| 2026-02-01 | [Rethinking Multinomial Logistic Mixture of Experts with Sigmoid Gating Function](https://arxiv.org/abs/2602.01466v1) | 2602.01466v1 | 12 |
| 2026-02-01 | [Exposing and Defending the Achilles' Heel of Video Mixture-of-Experts](https://arxiv.org/abs/2602.01369v1) | 2602.01369v1 | 8 |
| 2026-02-01 | [Attention Sink Forges Native MoE in Attention Layers: Sink-Aware Training to Address Head Collapse](https://arxiv.org/abs/2602.01203v3) | 2602.01203v3 | 8 |
| 2026-02-01 | [LiME: Lightweight Mixture of Experts for Efficient Multimodal Multi-task Learning](https://arxiv.org/abs/2604.02338v1) | 2604.02338v1 | 8 |
| 2026-01-31 | [Dynamic Expert Sharing: Decoupling Memory from Parallelism in Mixture-of-Experts Diffusion LLMs](https://arxiv.org/abs/2602.00879v2) | 2602.00879v2 | 8 |
| 2026-01-31 | [PROBE: Co-Balancing Computation and Communication in MoE Inference via Real-Time Predictive Prefetching](https://arxiv.org/abs/2602.00509v2) | 2602.00509v2 | 7 |
| 2026-01-30 | [MELINOE: Fine-Tuning Enables Memory-Efficient Inference for Mixture-of-Experts Models](https://arxiv.org/abs/2602.11192v1) | 2602.11192v1 | 6 |
| 2026-01-30 | [UrbanMoE: A Sparse Multi-Modal Mixture-of-Experts Framework for Multi-Task Urban Region Profiling](https://arxiv.org/abs/2601.22746v1) | 2601.22746v1 | 6 |
| 2026-01-30 | [KBVQ-MoE: KLT-guided SVD with Bias-Corrected Vector Quantization for MoE Large Language Models](https://arxiv.org/abs/2602.11184v2) | 2602.11184v2 | 8 |
| 2026-01-29 | [Supervised Mixture-of-Experts for Surgical Grasping and Retraction](https://arxiv.org/abs/2601.21971v2) | 2601.21971v2 | 6 |
| 2026-01-29 | [Seg-MoE: Multi-Resolution Segment-wise Mixture-of-Experts for Time Series Forecasting Transformers](https://arxiv.org/abs/2601.21641v2) | 2601.21641v2 | 7 |
| 2026-01-29 | [L2R: Low-Rank and Lipschitz-Controlled Routing for Mixture-of-Experts](https://arxiv.org/abs/2601.21349v3) | 2601.21349v3 | 8 |
| 2026-01-29 | [Abstracting Robot Manipulation Skills via Mixture-of-Experts Diffusion Policies](https://arxiv.org/abs/2601.21251v1) | 2601.21251v1 | 7 |
| 2026-01-29 | [BrainStack: Neuro-MoE with Functionally Guided Expert Routing for EEG-Based Language Decoding](https://arxiv.org/abs/2601.21148v1) | 2601.21148v1 | 10 |
| 2026-01-28 | [Toward Effective Multi-Domain Rumor Detection in Social Networks Using Domain-Gated Mixture-of-Experts](https://arxiv.org/abs/2602.21214v1) | 2602.21214v1 | 6 |
| 2026-01-28 | [Hyperparameter Transfer with Mixture-of-Expert Layers](https://arxiv.org/abs/2601.20205v3) | 2601.20205v3 | 7 |
| 2026-01-27 | [Revisiting Incremental Stochastic Majorization-Minimization Algorithms with Applications to Mixture of Experts](https://arxiv.org/abs/2601.19811v1) | 2601.19811v1 | 6 |
| 2026-01-27 | [Dynamic Multi-Expert Projectors with Stabilized Routing for Multilingual Speech Recognition](https://arxiv.org/abs/2601.19451v1) | 2601.19451v1 | 8 |
| 2026-01-26 | [Mechanistic Analysis of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning](https://arxiv.org/abs/2601.18699v2) | 2601.18699v2 | 10 |
| 2026-01-26 | [LatentMoE: Toward Optimal Accuracy per FLOP and Parameter in Mixture of Experts](https://arxiv.org/abs/2601.18089v1) | 2601.18089v1 | 6 |
| 2026-01-25 | [Domain-Expert-Guided Hybrid Mixture-of-Experts for Medical AI: Integrating Data-Driven Learning with Clinical Priors](https://arxiv.org/abs/2601.17977v1) | 2601.17977v1 | 6 |
| 2026-01-25 | [$\infty$-MoE: Generalizing Mixture of Experts to Infinite Experts](https://arxiv.org/abs/2601.17680v1) | 2601.17680v1 | 8 |
| 2026-01-23 | [Least-Loaded Expert Parallelism: Load Balancing An Imbalanced Mixture-of-Experts](https://arxiv.org/abs/2601.17111v1) | 2601.17111v1 | 16 |
| 2026-01-23 | [GRIP: Algorithm-Agnostic Machine Unlearning for Mixture-of-Experts via Geometric Router Constraints](https://arxiv.org/abs/2601.16905v3) | 2601.16905v3 | 9 |
| 2026-01-22 | [FlashMoE: Reducing SSD I/O Bottlenecks via ML-Based Cache Replacement for Mixture-of-Experts Inference on Edge Devices](https://arxiv.org/abs/2601.17063v2) | 2601.17063v2 | 7 |
| 2026-01-21 | [Improving MoE Compute Efficiency by Composing Weight and Data Sparsity](https://arxiv.org/abs/2601.15370v1) | 2601.15370v1 | 8 |
| 2026-01-21 | [Mixture-of-Experts Models in Vision: Routing, Optimization, and Generalization](https://arxiv.org/abs/2601.15021v1) | 2601.15021v1 | 7 |
| 2026-01-21 | [Robustness of Mixtures of Experts to Feature Noise](https://arxiv.org/abs/2601.14792v2) | 2601.14792v2 | 9 |
| 2026-01-20 | [Understanding Multilingualism in Mixture-of-Experts LLMs: Routing Mechanism, Expert Specialization, and Layerwise Steering](https://arxiv.org/abs/2601.14050v1) | 2601.14050v1 | 6 |
| 2026-01-19 | [PASs-MoE: Mitigating Misaligned Co-drift among Router and Experts via Pathway Activation Subspaces for Continual Learning](https://arxiv.org/abs/2601.13020v2) | 2601.13020v2 | 7 |
| 2026-01-19 | [OFA-MAS: One-for-All Multi-Agent System Topology Design based on Mixture-of-Experts Graph Generative Models](https://arxiv.org/abs/2601.12996v1) | 2601.12996v1 | 6 |
| 2026-01-19 | [PhyG-MoE: A Physics-Guided Mixture-of-Experts Framework for Energy-Efficient GNSS Interference Recognition](https://arxiv.org/abs/2601.12798v1) | 2601.12798v1 | 6 |
| 2026-01-19 | [Topology-Aware Multiscale Mixture of Experts for Efficient Molecular Property Prediction](https://arxiv.org/abs/2601.12637v1) | 2601.12637v1 | 6 |
| 2026-01-18 | [A Mixture of Experts Vision Transformer for High-Fidelity Surface Code Decoding](https://arxiv.org/abs/2601.12483v2) | 2601.12483v2 | 6 |
| 2026-01-18 | [Learning Diverse Skills for Behavior Models with Mixture of Experts](https://arxiv.org/abs/2601.12397v1) | 2601.12397v1 | 6 |
| 2026-01-18 | [Facet-Aware Multi-Head Mixture-of-Experts Model with Text-Enhanced Pre-training for Sequential Recommendation](https://arxiv.org/abs/2601.12301v1) | 2601.12301v1 | 8 |
| 2026-01-17 | [EMoE: Eigenbasis-Guided Routing for Mixture-of-Experts](https://arxiv.org/abs/2601.12137v1) | 2601.12137v1 | 7 |
| 2026-01-16 | [Self-Augmented Mixture-of-Experts for QoS Prediction](https://arxiv.org/abs/2601.11036v3) | 2601.11036v3 | 6 |
| 2026-01-15 | [MoST: Mixing Speech and Text with Modality-Aware Mixture of Experts](https://arxiv.org/abs/2601.10272v1) | 2601.10272v1 | 6 |
| 2026-01-14 | [Progressive Mixture-of-Experts with autoencoder routing for continual RANS turbulence modelling](https://arxiv.org/abs/2601.09305v2) | 2601.09305v2 | 8 |
| 2026-01-14 | [Horseshoe Mixtures-of-Experts (HS-MoE)](https://arxiv.org/abs/2601.09043v1) | 2601.09043v1 | 8 |
| 2026-01-13 | [M$^2$FMoE: Multi-Resolution Multi-View Frequency Mixture-of-Experts for Extreme-Adaptive Time Series Forecasting](https://arxiv.org/abs/2601.08631v1) | 2601.08631v1 | 6 |
| 2026-01-13 | [Towards Principled Design of Mixture-of-Experts Language Models under Memory and Inference Constraints](https://arxiv.org/abs/2601.08215v1) | 2601.08215v1 | 6 |
| 2026-01-12 | [CRAFT: Fine-Grained Cost-Aware Expert Replication For Efficient Mixture-of-Experts Serving](https://arxiv.org/abs/2603.28768v2) | 2603.28768v2 | 7 |
| 2026-01-12 | [TAG-MoE: Task-Aware Gating for Unified Generative Mixture-of-Experts](https://arxiv.org/abs/2601.08881v2) | 2601.08881v2 | 6 |
| 2026-01-12 | [Conditional Memory via Scalable Lookup: A New Axis of Sparsity for Large Language Models](https://arxiv.org/abs/2601.07372v2) | 2601.07372v2 | 6 |
| 2026-01-11 | [MoE-DisCo:Low Economy Cost Training Mixture-of-Experts Models](https://arxiv.org/abs/2601.06857v1) | 2601.06857v1 | 6 |
| 2026-01-11 | [MoEScore: Mixture-of-Experts-Based Text-Audio Relevance Score Prediction for Text-to-Audio System Evaluation](https://arxiv.org/abs/2601.06829v1) | 2601.06829v1 | 10 |
| 2026-01-09 | [Monkey Jump : MoE-Style PEFT for Efficient Multi-Task Learning](https://arxiv.org/abs/2601.06356v1) | 2601.06356v1 | 6 |
| 2026-01-09 | [Mixture-of-Experts as Soft Clustering: A Dual Jacobian-PCA Spectral Geometry Perspective](https://arxiv.org/abs/2601.11616v2) | 2601.11616v2 | 9 |
| 2026-01-08 | [MoE3D: A Mixture-of-Experts Module for 3D Reconstruction](https://arxiv.org/abs/2601.05208v3) | 2601.05208v3 | 8 |
| 2026-01-08 | [FaST: Efficient and Effective Long-Horizon Forecasting for Large-Scale Spatial-Temporal Graphs via Mixture-of-Experts](https://arxiv.org/abs/2601.05174v1) | 2601.05174v1 | 11 |
| 2026-01-08 | [DR-LoRA: Dynamic Rank LoRA for Fine-Tuning Mixture-of-Experts Models](https://arxiv.org/abs/2601.04823v6) | 2601.04823v6 | 7 |
| 2026-01-07 | [Variational Inference, Entropy, and Orthogonality: A Unified Theory of Mixture-of-Experts](https://arxiv.org/abs/2601.03577v1) | 2601.03577v1 | 12 |
| 2026-01-06 | [The Illusion of Specialization: Unveiling the Domain-Invariant "Standing Committee" in Mixture-of-Experts Models](https://arxiv.org/abs/2601.03425v2) | 2601.03425v2 | 10 |
| 2026-01-06 | [MixTTE: Multi-Level Mixture-of-Experts for Scalable and Adaptive Travel Time Estimation](https://arxiv.org/abs/2601.02943v1) | 2601.02943v1 | 6 |
| 2026-01-05 | [Routing by Analogy: kNN-Augmented Expert Assignment for Mixture-of-Experts](https://arxiv.org/abs/2601.02144v2) | 2601.02144v2 | 8 |
| 2026-01-05 | [Varying-coefficient mixture of experts model for dynamic heterogeneous populations: application to mouse cortical development](https://arxiv.org/abs/2601.01699v2) | 2601.01699v2 | 10 |
| 2026-01-04 | [Multi-Subspace Multi-Modal Modeling for Diffusion Models: Estimation, Convergence and Mixture of Experts](https://arxiv.org/abs/2601.01475v1) | 2601.01475v1 | 6 |
| 2026-01-02 | [HFedMoE: Resource-aware Heterogeneous Federated Learning with Mixture-of-Experts](https://arxiv.org/abs/2601.00583v1) | 2601.00583v1 | 6 |
| 2026-01-01 | [Geometric Regularization in Mixture-of-Experts: The Disconnect Between Weights and Activations](https://arxiv.org/abs/2601.00457v1) | 2601.00457v1 | 6 |
| 2026-01-01 | [Identification and Estimation under Multiple Versions of Treatment: Mixture-of-Experts Approach](https://arxiv.org/abs/2601.00287v2) | 2601.00287v2 | 6 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-30 | [RepetitionCurse: Measuring and Understanding Router Imbalance in Mixture-of-Experts LLMs under DoS Stress](https://arxiv.org/abs/2512.23995v2) | 2512.23995v2 | 14 |
| 2025-12-29 | [Coupling Experts and Routers in Mixture-of-Experts via an Auxiliary Loss](https://arxiv.org/abs/2512.23447v2) | 2512.23447v2 | 9 |
| 2025-12-28 | [FLEX-MoE: Federated Mixture-of-Experts with Load-balanced Expert Assignment for Edge Computing](https://arxiv.org/abs/2512.23070v2) | 2512.23070v2 | 10 |
| 2025-12-28 | [Text-Routed Sparse Mixture-of-Experts Model with Explanation and Temporal Alignment for Multi-Modal Sentiment Analysis](https://arxiv.org/abs/2512.22741v1) | 2512.22741v1 | 6 |
| 2025-12-26 | [MMCTOP: A Multimodal Textualization and Mixture-of-Experts Framework for Clinical Trial Outcome Prediction](https://arxiv.org/abs/2512.21897v1) | 2512.21897v1 | 13 |
| 2025-12-25 | [Hybrid Quantum-Classical Mixture of Experts: Unlocking Topological Advantage via Interference-Based Routing](https://arxiv.org/abs/2512.22296v1) | 2512.22296v1 | 13 |
| 2025-12-25 | [Spatiotemporal-Untrammelled Mixture of Experts for Multi-Person Motion Prediction](https://arxiv.org/abs/2512.21707v1) | 2512.21707v1 | 6 |
| 2025-12-25 | [Efficient MoE Inference with Fine-Grained Scheduling of Disaggregated Expert Parallelism](https://arxiv.org/abs/2512.21487v1) | 2512.21487v1 | 8 |
| 2025-12-24 | [RevFFN: Memory-Efficient Full-Parameter Fine-Tuning of Mixture-of-Experts LLMs with Reversible Blocks](https://arxiv.org/abs/2512.20920v1) | 2512.20920v1 | 10 |
| 2025-12-23 | [Divided We Fall: Defending Against Adversarial Attacks via Soft-Gated Fractional Mixture-of-Experts with Randomized Adversarial Training](https://arxiv.org/abs/2512.20821v3) | 2512.20821v3 | 6 |
| 2025-12-23 | [Branch Learning in MRI: More Data, More Models, More Training](https://arxiv.org/abs/2512.20330v1) | 2512.20330v1 | 9 |
| 2025-12-23 | [Mixture-of-Experts with Gradient Conflict-Driven Subspace Topology Pruning for Emergent Modularity](https://arxiv.org/abs/2512.20291v4) | 2512.20291v4 | 6 |
| 2025-12-23 | [Degradation-Aware Metric Prompting for Hyperspectral Image Restoration](https://arxiv.org/abs/2512.20251v3) | 2512.20251v3 | 6 |
| 2025-12-21 | [Remoe: Towards Efficient and Low-Cost MoE Inference in Serverless Computing](https://arxiv.org/abs/2512.18674v1) | 2512.18674v1 | 8 |
| 2025-12-21 | [How Many Experts Are Enough? Towards Optimal Semantic Specialization for Mixture-of-Experts](https://arxiv.org/abs/2512.19765v1) | 2512.19765v1 | 6 |
| 2025-12-20 | [Secret mixtures of experts inside your LLM](https://arxiv.org/abs/2512.18452v1) | 2512.18452v1 | 6 |
| 2025-12-19 | [RUL-QMoE: Multiple Non-crossing Quantile Mixture-of-Experts for Probabilistic Remaining Useful Life Predictions of Varying Battery Materials](https://arxiv.org/abs/2512.23725v1) | 2512.23725v1 | 6 |
| 2025-12-18 | [Bandwidth-Efficient Adaptive Mixture-of-Experts via Low-Rank Compensation](https://arxiv.org/abs/2512.17073v1) | 2512.17073v1 | 8 |
| 2025-12-18 | [PoseMoE: Mixture-of-Experts Network for Monocular 3D Human Pose Estimation](https://arxiv.org/abs/2512.16494v1) | 2512.16494v1 | 6 |
| 2025-12-18 | [Sigma-MoE-Tiny Technical Report](https://arxiv.org/abs/2512.16248v2) | 2512.16248v2 | 8 |
| 2025-12-16 | [Let the Barbarians In: How AI Can Accelerate Systems Performance Research](https://arxiv.org/abs/2512.14806v4) | 2512.14806v4 | 8 |
| 2025-12-16 | [VersatileFFN: Achieving Parameter Efficiency in LLMs via Adaptive Wide-and-Deep Reuse](https://arxiv.org/abs/2512.14531v2) | 2512.14531v2 | 11 |
| 2025-12-16 | [SonicMoE: Accelerating MoE with IO and Tile-aware Optimizations](https://arxiv.org/abs/2512.14080v2) | 2512.14080v2 | 7 |
| 2025-12-15 | [SocialNav-MoE: A Mixture-of-Experts Vision Language Model for Socially Compliant Navigation with Reinforcement Fine-Tuning](https://arxiv.org/abs/2512.14757v1) | 2512.14757v1 | 6 |
| 2025-12-13 | [MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models](https://arxiv.org/abs/2512.12121v1) | 2512.12121v1 | 8 |
| 2025-12-10 | [M3Net: A Multi-Metric Mixture of Experts Network Digital Twin with Graph Neural Networks](https://arxiv.org/abs/2512.09797v1) | 2512.09797v1 | 10 |
| 2025-12-09 | [Ask, Answer, and Detect: Role-Playing LLMs for Personality Detection with Question-Conditioned Mixture-of-Experts](https://arxiv.org/abs/2512.08814v2) | 2512.08814v2 | 6 |
| 2025-12-09 | [What really matters for person re-identification? A Mixture-of-Experts Framework for Semantic Attribute Importance](https://arxiv.org/abs/2512.08697v1) | 2512.08697v1 | 8 |
| 2025-12-07 | [Stable-MoE: Lyapunov-based Token Routing for Distributed Mixture-of-Experts Training over Edge Networks](https://arxiv.org/abs/2512.06784v3) | 2512.06784v3 | 10 |
| 2025-12-07 | [Statistic-Augmented, Decoupled MoE Routing and Aggregating in Autonomous Driving](https://arxiv.org/abs/2512.06664v1) | 2512.06664v1 | 8 |
| 2025-12-06 | [Enhancing Medical Cross-Modal Hashing Retrieval using Dropout-Voting Mixture-of-Experts Fusion](https://arxiv.org/abs/2512.06449v1) | 2512.06449v1 | 6 |
| 2025-12-05 | [HiMoE-VLA: Hierarchical Mixture-of-Experts for Generalist Vision-Language-Action Policies](https://arxiv.org/abs/2512.05693v2) | 2512.05693v2 | 6 |
| 2025-12-04 | [Context-Aware Mixture-of-Experts Inference on CXL-Enabled GPU-NDP Systems](https://arxiv.org/abs/2512.04476v1) | 2512.04476v1 | 6 |
| 2025-12-03 | [A Theoretical Framework for Auxiliary-Loss-Free Load Balancing of Sparse Mixture-of-Experts in Large-Scale AI Models](https://arxiv.org/abs/2512.03915v3) | 2512.03915v3 | 13 |
| 2025-12-02 | [SkyMoE: A Vision-Language Foundation Model for Enhancing Geospatial Interpretation with Mixture of Experts](https://arxiv.org/abs/2512.02517v1) | 2512.02517v1 | 12 |
| 2025-12-01 | [StructuredDNA: A Bio-Physical Framework for Energy-Aware Transformer Routing](https://arxiv.org/abs/2512.08968v1) | 2512.08968v1 | 13 |
| 2025-12-01 | [Multimodal Mixture-of-Experts for ISAC in Low-Altitude Wireless Networks](https://arxiv.org/abs/2512.01750v1) | 2512.01750v1 | 6 |
| 2025-12-01 | [Efficient Training of Diffusion Mixture-of-Experts Models: A Practical Recipe](https://arxiv.org/abs/2512.01252v1) | 2512.01252v1 | 6 |
| 2025-11-30 | [MoB: Mixture of Bidders](https://arxiv.org/abs/2512.10969v1) | 2512.10969v1 | 9 |
| 2025-11-28 | [Chart2Code-MoLA: Efficient Multi-Modal Code Generation via Adaptive Expert Routing](https://arxiv.org/abs/2511.23321v1) | 2511.23321v1 | 10 |
| 2025-11-28 | [Distillation-based Scenario-Adaptive Mixture-of-Experts for the Matching Stage of Multi-scenario Recommendation](https://arxiv.org/abs/2601.02368v1) | 2601.02368v1 | 6 |
| 2025-11-28 | [Experts are all you need: A Composable Framework for Large Language Model Inference](https://arxiv.org/abs/2511.22955v1) | 2511.22955v1 | 6 |
| 2025-11-27 | [MoE3D: Mixture of Experts meets Multi-Modal 3D Understanding](https://arxiv.org/abs/2511.22103v1) | 2511.22103v1 | 6 |
| 2025-11-26 | [MemFine: Memory-Aware Fine-Grained Scheduling for MoE Training](https://arxiv.org/abs/2511.21431v4) | 2511.21431v4 | 8 |
| 2025-11-26 | [MLPMoE: Zero-Shot Architectural Metamorphosis of Dense LLM MLPs into Static Mixture-of-Experts](https://arxiv.org/abs/2511.21089v1) | 2511.21089v1 | 14 |
| 2025-11-25 | [History-Augmented Contrastive Learning With Soft Mixture of Experts for Blind Super-Resolution of Planetary Remote Sensing Images](https://arxiv.org/abs/2511.20045v2) | 2511.20045v2 | 10 |
| 2025-11-25 | [Mosaic Pruning: A Hierarchical Framework for Generalizable Pruning of Mixture-of-Experts Models](https://arxiv.org/abs/2511.19822v1) | 2511.19822v1 | 7 |
| 2025-11-24 | [OrdMoE: Preference Alignment via Hierarchical Expert Group Ranking in Multimodal Mixture-of-Experts LLMs](https://arxiv.org/abs/2511.19023v1) | 2511.19023v1 | 8 |
| 2025-11-24 | [Dynamic Mixture of Experts Against Severe Distribution Shifts](https://arxiv.org/abs/2511.18987v1) | 2511.18987v1 | 10 |
| 2025-11-21 | [Unified Class and Domain Incremental Learning with Mixture of Experts for Indoor Localization](https://arxiv.org/abs/2511.17829v1) | 2511.17829v1 | 10 |
| 2025-11-21 | [Sparse Mixture-of-Experts for Multi-Channel Imaging: Are All Channel Interactions Required?](https://arxiv.org/abs/2511.17400v1) | 2511.17400v1 | 8 |
| 2025-11-21 | [MCMoE: Completing Missing Modalities with Mixture of Experts for Incomplete Multimodal Action Quality Assessment](https://arxiv.org/abs/2511.17397v2) | 2511.17397v2 | 6 |
| 2025-11-21 | [RadioKMoE: Knowledge-Guided Radiomap Estimation with Kolmogorov-Arnold Networks and Mixture-of-Experts](https://arxiv.org/abs/2511.16986v1) | 2511.16986v1 | 6 |
| 2025-11-21 | [Fine-grained MoE Load Balancing with Linear Programming](https://arxiv.org/abs/2511.16947v2) | 2511.16947v2 | 10 |
| 2025-11-19 | [MoDES: Accelerating Mixture-of-Experts Multimodal Large Language Models via Dynamic Expert Skipping](https://arxiv.org/abs/2511.15690v2) | 2511.15690v2 | 6 |
| 2025-11-19 | [Dynamic Expert Quantization for Scalable Mixture-of-Experts Inference](https://arxiv.org/abs/2511.15015v4) | 2511.15015v4 | 9 |
| 2025-11-18 | [Generalizable and Efficient Automated Scoring with a Knowledge-Distilled Multi-Task Mixture-of-Experts](https://arxiv.org/abs/2511.17601v1) | 2511.17601v1 | 6 |
| 2025-11-18 | [SMGeo: Cross-View Object Geo-Localization with Grid-Level Mixture-of-Experts](https://arxiv.org/abs/2511.14093v1) | 2511.14093v1 | 6 |
| 2025-11-17 | [MoMoE: A Mixture of Expert Agent Model for Financial Sentiment Analysis](https://arxiv.org/abs/2511.13983v1) | 2511.13983v1 | 8 |
| 2025-11-17 | [YOLO Meets Mixture-of-Experts: Adaptive Expert Routing for Robust Object Detection](https://arxiv.org/abs/2511.13344v4) | 2511.13344v4 | 12 |
| 2025-11-16 | [SEMC: Structure-Enhanced Mixture-of-Experts Contrastive Learning for Ultrasound Standard Plane Recognition](https://arxiv.org/abs/2511.12559v1) | 2511.12559v1 | 6 |
| 2025-11-16 | [MdaIF: Robust One-Stop Multi-Degradation-Aware Image Fusion with Language-Driven Semantics](https://arxiv.org/abs/2511.12525v1) | 2511.12525v1 | 8 |
| 2025-11-16 | [47B Mixture-of-Experts Beats 671B Dense Models on Chinese Medical Examinations](https://arxiv.org/abs/2511.21701v2) | 2511.21701v2 | 6 |
| 2025-11-15 | [SAC-MoE: Reinforcement Learning with Mixture-of-Experts for Control of Hybrid Dynamical Systems with Uncertainty](https://arxiv.org/abs/2511.12361v1) | 2511.12361v1 | 8 |
| 2025-11-15 | [AMR-MoEGA: Antimicrobial Resistance Prediction using Mixture of Experts and Genetic Algorithms](https://arxiv.org/abs/2511.12223v1) | 2511.12223v1 | 6 |
| 2025-11-15 | [ViTE: Virtual Graph Trajectory Expert Router for Pedestrian Trajectory Prediction](https://arxiv.org/abs/2511.12214v1) | 2511.12214v1 | 7 |
| 2025-11-14 | [Rethinking Efficient Mixture-of-Experts for Remote Sensing Modality-Missing Classification](https://arxiv.org/abs/2511.11460v3) | 2511.11460v3 | 6 |
| 2025-11-14 | [DoReMi: Bridging 3D Domains via Topology-Aware Domain-Representation Mixture of Experts](https://arxiv.org/abs/2511.11232v2) | 2511.11232v2 | 10 |
| 2025-11-14 | [ERMoE: Eigen-Reparameterized Mixture-of-Experts for Stable Routing and Interpretable Specialization](https://arxiv.org/abs/2511.10971v2) | 2511.10971v2 | 12 |
| 2025-11-13 | [Uncertainty Makes It Stable: Curiosity-Driven Quantized Mixture-of-Experts](https://arxiv.org/abs/2511.11743v4) | 2511.11743v4 | 6 |
| 2025-11-13 | [Generalizable Slum Detection from Satellite Imagery with Mixture-of-Experts](https://arxiv.org/abs/2511.10300v1) | 2511.10300v1 | 6 |
| 2025-11-13 | [ExpertAD: Enhancing Autonomous Driving Systems with Mixture of Experts](https://arxiv.org/abs/2511.11740v1) | 2511.11740v1 | 10 |
| 2025-11-13 | [BuddyMoE: Exploiting Expert Redundancy to Accelerate Memory-Constrained Mixture-of-Experts Inference](https://arxiv.org/abs/2511.10054v1) | 2511.10054v1 | 6 |
| 2025-11-12 | [Selective Sinkhorn Routing for Improved Sparse Mixture of Experts](https://arxiv.org/abs/2511.08972v2) | 2511.08972v2 | 10 |
| 2025-11-12 | [Bayesian Mixture of Experts For Large Language Models](https://arxiv.org/abs/2511.08968v1) | 2511.08968v1 | 10 |
| 2025-11-11 | [Let the Experts Speak: Improving Survival Prediction & Calibration via Mixture-of-Experts Heads](https://arxiv.org/abs/2511.09567v2) | 2511.09567v2 | 6 |
| 2025-11-10 | [One Router to Route Them All: Homogeneous Expert Routing for Heterogeneous Graph Transformers](https://arxiv.org/abs/2511.07603v2) | 2511.07603v2 | 13 |
| 2025-11-10 | [Routing Manifold Alignment Improves Generalization of Mixture-of-Experts LLMs](https://arxiv.org/abs/2511.07419v2) | 2511.07419v2 | 8 |
| 2025-11-10 | [Pre-Attention Expert Prediction and Prefetching for Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2511.10676v1) | 2511.10676v1 | 8 |
| 2025-11-09 | [HyMoERec: Hybrid Mixture-of-Experts for Sequential Recommendation](https://arxiv.org/abs/2511.06388v1) | 2511.06388v1 | 8 |
| 2025-11-09 | [Towards Fine-Grained Code-Switch Speech Translation with Semantic Space Alignment](https://arxiv.org/abs/2511.10670v2) | 2511.10670v2 | 8 |
| 2025-11-08 | [In-depth Analysis on Caching and Pre-fetching in Mixture of Experts Offloading](https://arxiv.org/abs/2511.05814v1) | 2511.05814v1 | 6 |
| 2025-11-06 | [PuzzleMoE: Efficient Compression of Large Mixture-of-Experts Models via Sparse Expert Merging and Bit-packed inference](https://arxiv.org/abs/2511.04805v2) | 2511.04805v2 | 13 |
| 2025-11-06 | [GNN-MoE: Context-Aware Patch Routing using GNNs for Parameter-Efficient Domain Generalization](https://arxiv.org/abs/2511.04008v1) | 2511.04008v1 | 6 |
| 2025-11-04 | [RoME: Domain-Robust Mixture-of-Experts for MILP Solution Prediction across Domains](https://arxiv.org/abs/2511.02331v1) | 2511.02331v1 | 6 |
| 2025-11-04 | [Opportunistic Expert Activation: Batch-Aware Expert Routing for Faster Decode Without Retraining](https://arxiv.org/abs/2511.02237v1) | 2511.02237v1 | 12 |
| 2025-11-03 | [Towards Efficient Federated Learning of Networked Mixture-of-Experts for Mobile Edge Computing](https://arxiv.org/abs/2511.01743v2) | 2511.01743v2 | 6 |
| 2025-11-03 | [CryptoMoE: Privacy-Preserving and Scalable Mixture of Experts Inference via Balanced Expert Routing](https://arxiv.org/abs/2511.01197v3) | 2511.01197v3 | 16 |
| 2025-11-03 | [DEER: Disentangled Mixture of Experts with Instance-Adaptive Routing for Generalizable Machine-Generated Text Detection](https://arxiv.org/abs/2511.01192v2) | 2511.01192v2 | 12 |
| 2025-10-31 | [MoRE: 3D Visual Geometry Reconstruction Meets Mixture-of-Experts](https://arxiv.org/abs/2510.27234v1) | 2510.27234v1 | 7 |
| 2025-10-31 | [Hierarchical Fusion of Local and Global Visual Features with Mixture-of-Experts for Remote Sensing Image Scene Classification](https://arxiv.org/abs/2510.27155v2) | 2510.27155v2 | 6 |
| 2025-10-30 | [Mixture-of-Transformers Learn Faster: A Theoretical Study on Classification Problems](https://arxiv.org/abs/2510.27004v1) | 2510.27004v1 | 6 |
| 2025-10-29 | [Dual Mixture-of-Experts Framework for Discrete-Time Survival Analysis](https://arxiv.org/abs/2510.26014v1) | 2510.26014v1 | 6 |
| 2025-10-29 | [Revisiting scalable sequential recommendation with Multi-Embedding Approach and Mixture-of-Experts](https://arxiv.org/abs/2510.25285v1) | 2510.25285v1 | 6 |
| 2025-10-29 | [Mixture-of-Experts Operator Transformer for Large-Scale PDE Pre-Training](https://arxiv.org/abs/2510.25803v2) | 2510.25803v2 | 8 |
| 2025-10-29 | [H3M-SSMoEs: Hypergraph-based Multimodal Learning with LLM Reasoning and Style-Structured Mixture of Experts](https://arxiv.org/abs/2510.25091v1) | 2510.25091v1 | 6 |
| 2025-10-28 | [Routing Matters in MoE: Scaling Diffusion Transformers with Explicit Routing Guidance](https://arxiv.org/abs/2510.24711v2) | 2510.24711v2 | 7 |
| 2025-10-27 | [Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts](https://arxiv.org/abs/2510.23027v2) | 2510.23027v2 | 9 |
| 2025-10-27 | [MoEMeta: Mixture-of-Experts Meta Learning for Few-Shot Relational Learning](https://arxiv.org/abs/2510.23013v4) | 2510.23013v4 | 6 |
| 2025-10-26 | [Sparsity and Superposition in Mixture of Experts](https://arxiv.org/abs/2510.23671v2) | 2510.23671v2 | 11 |
| 2025-10-23 | [Bayesian Jammer Localization with a Hybrid CNN and Path-Loss Mixture of Experts](https://arxiv.org/abs/2510.20666v1) | 2510.20666v1 | 10 |
| 2025-10-23 | [Metis-HOME: Hybrid Optimized Mixture-of-Experts for Multimodal Reasoning](https://arxiv.org/abs/2510.20519v2) | 2510.20519v2 | 8 |
| 2025-10-23 | [Addressing Corner Cases in Autonomous Driving: A World Model-based Approach with Mixture of Experts and LLMs](https://arxiv.org/abs/2510.21867v1) | 2510.21867v1 | 12 |
| 2025-10-23 | [A Parameter-Efficient Mixture-of-Experts Framework for Cross-Modal Geo-Localization](https://arxiv.org/abs/2510.20291v1) | 2510.20291v1 | 6 |
| 2025-10-22 | [RailS: Load Balancing for All-to-All Communication in Distributed Mixture-of-Experts Training](https://arxiv.org/abs/2510.19262v2) | 2510.19262v2 | 12 |
| 2025-10-22 | [MoE-GS: Mixture of Experts for Dynamic Gaussian Splatting](https://arxiv.org/abs/2510.19210v2) | 2510.19210v2 | 12 |
| 2025-10-21 | [Unifying and Enhancing Graph Transformers via a Hierarchical Mask Framework](https://arxiv.org/abs/2510.18825v1) | 2510.18825v1 | 8 |
| 2025-10-20 | [Intelligent Communication Mixture-of-Experts Boosted-Medical Image Segmentation Foundation Model](https://arxiv.org/abs/2510.17684v1) | 2510.17684v1 | 10 |
| 2025-10-20 | [MoE-Based Learned Inertial Odometry for Bicycle Localization](https://arxiv.org/abs/2510.17604v2) | 2510.17604v2 | 6 |
| 2025-10-20 | [ReXMoE: Reusing Experts with Minimal Overhead in Mixture-of-Experts](https://arxiv.org/abs/2510.17483v1) | 2510.17483v1 | 9 |
| 2025-10-19 | [Online Mixture of Experts: No-Regret Learning for Optimal Collective Decision-Making](https://arxiv.org/abs/2510.21788v2) | 2510.21788v2 | 10 |
| 2025-10-19 | [L-MoE: End-to-End Training of a Lightweight Mixture of Low-Rank Adaptation Experts](https://arxiv.org/abs/2510.17898v2) | 2510.17898v2 | 7 |
| 2025-10-18 | [Input Domain Aware MoE: Decoupling Routing Decisions from Task Optimization in Mixture of Experts](https://arxiv.org/abs/2510.16448v1) | 2510.16448v1 | 7 |
| 2025-10-18 | [Modeling Expert Interactions in Sparse Mixture of Experts via Graph Structures](https://arxiv.org/abs/2510.16411v1) | 2510.16411v1 | 6 |
| 2025-10-17 | [Expert Merging in Sparse Mixture of Experts with Nash Bargaining](https://arxiv.org/abs/2510.16138v2) | 2510.16138v2 | 6 |
| 2025-10-17 | [Mixture of Experts Approaches in Dense Retrieval Tasks](https://arxiv.org/abs/2510.15683v1) | 2510.15683v1 | 10 |
| 2025-10-17 | [Backdoor or Manipulation? Graph Mixture of Experts Can Defend Against Various Graph Adversarial Attacks](https://arxiv.org/abs/2510.15333v1) | 2510.15333v1 | 8 |
| 2025-10-17 | [MTmixAtt: Integrating Mixture-of-Experts with Multi-Mix Attention for Large-Scale Recommendation](https://arxiv.org/abs/2510.15286v1) | 2510.15286v1 | 11 |
| 2025-10-16 | [Rewiring Experts on the Fly:Continuous Rerouting for Better Online Adaptation in Mixture-of-Expert models](https://arxiv.org/abs/2510.14853v1) | 2510.14853v1 | 11 |
| 2025-10-16 | [Expertise need not monopolize: Action-Specialized Mixture of Experts for Vision-Language-Action Learning](https://arxiv.org/abs/2510.14300v1) | 2510.14300v1 | 13 |
| 2025-10-15 | [REAP the Experts: Why Pruning Prevails for One-Shot MoE compression](https://arxiv.org/abs/2510.13999v3) | 2510.13999v3 | 6 |
| 2025-10-15 | [Steer-MoE: Efficient Audio-Language Alignment with a Mixture-of-Experts Steering Module](https://arxiv.org/abs/2510.13558v1) | 2510.13558v1 | 8 |
| 2025-10-15 | [Who Speaks for the Trigger? Dynamic Expert Routing in Backdoored Mixture-of-Experts Transformers](https://arxiv.org/abs/2510.13462v1) | 2510.13462v1 | 12 |
| 2025-10-15 | [Toward Efficient Inference Attacks: Shadow Model Sharing via Mixture-of-Experts](https://arxiv.org/abs/2510.13451v1) | 2510.13451v1 | 6 |
| 2025-10-15 | [GatePro: Parameter-Free Expert Selection Optimization for Mixture-of-Experts Models](https://arxiv.org/abs/2510.13079v1) | 2510.13079v1 | 7 |
| 2025-10-14 | [Dendrograms of Mixing Measures for Softmax-Gated Gaussian Mixture of Experts: Consistency Without Model Sweeps](https://arxiv.org/abs/2510.12744v2) | 2510.12744v2 | 6 |
| 2025-10-14 | [MoBiLE: Efficient Mixture-of-Experts Inference on Consumer GPU with Mixture of Big Little Experts](https://arxiv.org/abs/2510.12357v1) | 2510.12357v1 | 6 |
| 2025-10-13 | [Stabilizing MoE Reinforcement Learning by Aligning Training and Inference Routers](https://arxiv.org/abs/2510.11370v2) | 2510.11370v2 | 7 |
| 2025-10-13 | [MC#: Mixture Compressor for Mixture-of-Experts Large Models](https://arxiv.org/abs/2510.10962v1) | 2510.10962v1 | 6 |
| 2025-10-10 | [Dense2MoE: Restructuring Diffusion Transformer to MoE for Efficient Text-to-Image Generation](https://arxiv.org/abs/2510.09094v1) | 2510.09094v1 | 10 |
| 2025-10-09 | [FlyLoRA: Boosting Task Decoupling and Parameter Efficiency via Implicit Rank-Wise Mixture-of-Experts](https://arxiv.org/abs/2510.08396v2) | 2510.08396v2 | 12 |
| 2025-10-09 | [Beyond Sunk Costs: Boosting LLM Pre-training Efficiency via Orthogonal Growth of Mixture-of-Experts](https://arxiv.org/abs/2510.08008v2) | 2510.08008v2 | 7 |
| 2025-10-08 | [Guided by the Experts: Provable Feature Learning Dynamic of Soft-Routed Mixture-of-Experts](https://arxiv.org/abs/2510.07205v1) | 2510.07205v1 | 8 |
| 2025-10-08 | [Dynamic Mixture-of-Experts for Visual Autoregressive Model](https://arxiv.org/abs/2510.08629v2) | 2510.08629v2 | 8 |
| 2025-10-07 | [Barbarians at the Gate: How AI is Upending Systems Research](https://arxiv.org/abs/2510.06189v3) | 2510.06189v3 | 8 |
| 2025-10-07 | [Rasterized Steered Mixture of Experts for Efficient 2D Image Regression](https://arxiv.org/abs/2510.05814v2) | 2510.05814v2 | 6 |
| 2025-10-06 | [REN: Anatomically-Informed Mixture-of-Experts for Interstitial Lung Disease Diagnosis](https://arxiv.org/abs/2510.04923v3) | 2510.04923v3 | 6 |
| 2025-10-06 | [Multilingual Routing in Mixture-of-Experts](https://arxiv.org/abs/2510.04694v2) | 2510.04694v2 | 13 |
| 2025-10-05 | [SliceMoE: Routing Embedding Slices Instead of Tokens for Fine-Grained and Balanced Transformer Scaling](https://arxiv.org/abs/2510.04286v1) | 2510.04286v1 | 9 |
| 2025-10-05 | [MoME: Mixture of Matryoshka Experts for Audio-Visual Speech Recognition](https://arxiv.org/abs/2510.04136v1) | 2510.04136v1 | 6 |
| 2025-10-02 | [ElasticMoE: An Efficient Auto Scaling Method for Mixture-of-Experts Models](https://arxiv.org/abs/2510.02613v1) | 2510.02613v1 | 7 |
| 2025-10-02 | [UpSafe$^\circ$C: Upcycling for Controllable Safety in Large Language Models](https://arxiv.org/abs/2510.02194v2) | 2510.02194v2 | 6 |
| 2025-10-01 | [Dirichlet-Prior Shaping: Guiding Expert Specialization in Upcycled MoEs](https://arxiv.org/abs/2510.01185v1) | 2510.01185v1 | 6 |
| 2025-10-01 | [FAME: Adaptive Functional Attention with Expert Routing for Function-on-Function Regression](https://arxiv.org/abs/2510.00621v1) | 2510.00621v1 | 10 |
| 2025-10-01 | [Adaptive Shared Experts with LoRA-Based Mixture of Experts for Multi-Task Learning](https://arxiv.org/abs/2510.00570v1) | 2510.00570v1 | 16 |
| 2025-09-30 | [FlowMoE: A Scalable Pipeline Scheduling Framework for Distributed Mixture-of-Experts Training](https://arxiv.org/abs/2510.00207v2) | 2510.00207v2 | 6 |
| 2025-09-30 | [Training Matryoshka Mixture-of-Experts for Elastic Inference-Time Expert Utilization](https://arxiv.org/abs/2509.26520v2) | 2509.26520v2 | 9 |
| 2025-09-30 | [Understanding the Mixture-of-Experts with Nadaraya-Watson Kernel](https://arxiv.org/abs/2509.25913v2) | 2509.25913v2 | 10 |
| 2025-09-30 | [Multimodal LLM With Hierarchical Mixture-of-Experts for VQA on 3D Brain MRI](https://arxiv.org/abs/2509.25889v3) | 2509.25889v3 | 6 |
| 2025-09-30 | [Massively Multimodal Foundation Models: A Framework for Capturing Interactions with Specialized Mixture-of-Experts](https://arxiv.org/abs/2509.25678v4) | 2509.25678v4 | 9 |
| 2025-09-29 | [From Score Distributions to Balance: Plug-and-Play Mixture-of-Experts Routing](https://arxiv.org/abs/2510.03293v1) | 2510.03293v1 | 10 |
| 2025-09-29 | [One-Prompt Strikes Back: Sparse Mixture of Experts for Prompt-based Continual Learning](https://arxiv.org/abs/2509.24483v3) | 2509.24483v3 | 6 |
| 2025-09-28 | [Beyond Benchmarks: Understanding Mixture-of-Experts Models through Internal Mechanisms](https://arxiv.org/abs/2509.23933v1) | 2509.23933v1 | 6 |
| 2025-09-28 | [Bayesian Mixture-of-Experts: Towards Making LLMs Know What They Don't Know](https://arxiv.org/abs/2509.23830v1) | 2509.23830v1 | 6 |
| 2025-09-28 | [Towards a Comprehensive Scaling Law of Mixture-of-Experts](https://arxiv.org/abs/2509.23678v1) | 2509.23678v1 | 7 |
| 2025-09-27 | [Breaking the MoE LLM Trilemma: Dynamic Expert Clustering with Structured Compression](https://arxiv.org/abs/2510.02345v4) | 2510.02345v4 | 6 |
| 2025-09-26 | [Dynamic Experts Search: Enhancing Reasoning in Mixture-of-Experts LLMs at Test Time](https://arxiv.org/abs/2509.22572v1) | 2509.22572v1 | 7 |
| 2025-09-26 | [Learning to Ball: Composing Policies for Long-Horizon Basketball Moves](https://arxiv.org/abs/2509.22442v1) | 2509.22442v1 | 6 |
| 2025-09-26 | [Task-Aware Mixture-of-Experts for Time Series Analysis](https://arxiv.org/abs/2509.22279v3) | 2509.22279v3 | 12 |
| 2025-09-26 | [Elastic MoE: Unlocking the Inference-Time Scalability of Mixture-of-Experts](https://arxiv.org/abs/2509.21892v2) | 2509.21892v2 | 9 |
| 2025-09-25 | [DiaMoE-TTS: A Unified IPA-Based Dialect TTS Framework with Mixture-of-Experts and Parameter-Efficient Zero-Shot Adaptation](https://arxiv.org/abs/2509.22727v1) | 2509.22727v1 | 6 |
| 2025-09-24 | [Dynamic Reasoning Chains through Depth-Specialized Mixture-of-Experts in Transformer Architectures](https://arxiv.org/abs/2509.20577v1) | 2509.20577v1 | 10 |
| 2025-09-24 | [SHMoAReg: Spark Deformable Image Registration via Spatial Heterogeneous Mixture of Experts and Attention Heads](https://arxiv.org/abs/2509.20073v2) | 2509.20073v2 | 6 |
| 2025-09-24 | [Faster, Smaller, and Smarter: Task-Aware Expert Merging for Online MoE Inference](https://arxiv.org/abs/2509.19781v2) | 2509.19781v2 | 11 |
| 2025-09-24 | [MIXRAG : Mixture-of-Experts Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering](https://arxiv.org/abs/2509.21391v2) | 2509.21391v2 | 6 |
| 2025-09-23 | [Frequency-Domain Decomposition and Recomposition for Robust Audio-Visual Segmentation](https://arxiv.org/abs/2509.18912v2) | 2509.18912v2 | 8 |
| 2025-09-23 | [Symphony-MoE: Harmonizing Disparate Pre-trained Models into a Coherent Mixture-of-Experts](https://arxiv.org/abs/2509.18542v2) | 2509.18542v2 | 8 |
| 2025-09-22 | [Expert-as-a-Service: Towards Efficient, Scalable, and Robust Large-scale MoE Serving](https://arxiv.org/abs/2509.17863v1) | 2509.17863v1 | 9 |
| 2025-09-22 | [Attention-based Mixture of Experts for Robust Speech Deepfake Detection](https://arxiv.org/abs/2509.17585v1) | 2509.17585v1 | 6 |
| 2025-09-21 | [MoEs Are Stronger than You Think: Hyper-Parallel Inference Scaling with RoE](https://arxiv.org/abs/2509.17238v2) | 2509.17238v2 | 9 |
| 2025-09-21 | [A Statistical Mixture-of-Experts Framework for EMG Artifact Removal in EEG: Empirical Insights and a Proof-of-Concept Application](https://arxiv.org/abs/2509.19385v1) | 2509.19385v1 | 7 |
| 2025-09-21 | [CoBEVMoE: Heterogeneity-aware Feature Fusion with Dynamic Mixture-of-Experts for Collaborative Perception](https://arxiv.org/abs/2509.17107v2) | 2509.17107v2 | 6 |
| 2025-09-21 | [Dynamic Expert Specialization: Towards Catastrophic Forgetting-Free Multi-Domain MoE Adaptation](https://arxiv.org/abs/2509.16882v1) | 2509.16882v1 | 6 |
| 2025-09-19 | [DiEP: Adaptive Mixture-of-Experts Compression through Differentiable Expert Pruning](https://arxiv.org/abs/2509.16105v1) | 2509.16105v1 | 6 |
| 2025-09-19 | [MoE-CE: Enhancing Generalization for Deep Learning based Channel Estimation via a Mixture-of-Experts Framework](https://arxiv.org/abs/2509.15964v1) | 2509.15964v1 | 8 |
| 2025-09-18 | [Beyond Spurious Signals: Debiasing Multimodal Large Language Models via Counterfactual Inference and Adaptive Expert Routing](https://arxiv.org/abs/2509.15361v1) | 2509.15361v1 | 10 |
| 2025-09-18 | [EchoVLM: Dynamic Mixture-of-Experts Vision-Language Model for Universal Ultrasound Intelligence](https://arxiv.org/abs/2509.14977v3) | 2509.14977v3 | 6 |
| 2025-09-18 | [FURINA: Free from Unmergeable Router via LINear Aggregation of mixed experts](https://arxiv.org/abs/2509.14900v2) | 2509.14900v2 | 8 |
| 2025-09-17 | [CSMoE: An Efficient Remote Sensing Foundation Model with Soft Mixture-of-Experts](https://arxiv.org/abs/2509.14104v2) | 2509.14104v2 | 6 |
| 2025-09-17 | [Semi-MoE: Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation](https://arxiv.org/abs/2509.13834v1) | 2509.13834v1 | 6 |
| 2025-09-16 | [Mixture-of-Experts Framework for Field-of-View Enhanced Signal-Dependent Binauralization of Moving Talkers](https://arxiv.org/abs/2509.13548v3) | 2509.13548v3 | 10 |
| 2025-09-16 | [GLAD: Global-Local Aware Dynamic Mixture-of-Experts for Multi-Talker ASR](https://arxiv.org/abs/2509.13093v4) | 2509.13093v4 | 6 |
| 2025-09-16 | [NavMoE: Hybrid Model- and Learning-based Traversability Estimation for Local Navigation via Mixture of Experts](https://arxiv.org/abs/2509.12747v2) | 2509.12747v2 | 6 |
| 2025-09-15 | [SparseDoctor: Towards Efficient Chat Doctor with Mixture of Experts Enhanced Large Language Models](https://arxiv.org/abs/2509.14269v2) | 2509.14269v2 | 6 |
| 2025-09-14 | [Knowledge-Guided Adaptive Mixture of Experts for Precipitation Prediction](https://arxiv.org/abs/2509.11459v1) | 2509.11459v1 | 8 |
| 2025-09-14 | [On Linear Mode Connectivity of Mixture-of-Experts Architectures](https://arxiv.org/abs/2509.11348v2) | 2509.11348v2 | 6 |
| 2025-09-13 | [Lightweight Metadata-Aware Mixture-of-Experts Masked Autoencoder for Earth Observation](https://arxiv.org/abs/2509.10919v1) | 2509.10919v1 | 14 |
| 2025-09-12 | [Dropping Experts, Recombining Neurons: Retraining-Free Pruning for Sparse Mixture-of-Experts LLMs](https://arxiv.org/abs/2509.10377v1) | 2509.10377v1 | 8 |
| 2025-09-12 | [Cosine-Similarity Routing with Semantic Anchors for Interpretable Mixture-of-Experts Language Models](https://arxiv.org/abs/2509.14255v2) | 2509.14255v2 | 8 |
| 2025-09-12 | [Exploring Expert Specialization through Unsupervised Training in Sparse Mixture of Experts](https://arxiv.org/abs/2509.10025v1) | 2509.10025v1 | 10 |
| 2025-09-11 | [Steering MoE LLMs via Expert (De)Activation](https://arxiv.org/abs/2509.09660v2) | 2509.09660v2 | 6 |
| 2025-09-11 | [MoLEx: Mixture of LoRA Experts in Speech Self-Supervised Models for Audio Deepfake Detection](https://arxiv.org/abs/2509.09175v1) | 2509.09175v1 | 6 |
| 2025-09-10 | [Joint Learning using Mixture-of-Expert-Based Representation for Speech Enhancement and Robust Emotion Recognition](https://arxiv.org/abs/2509.08470v2) | 2509.08470v2 | 8 |
| 2025-09-09 | [DuoServe-MoE: Dual-Phase Expert Prefetch and Caching for LLM Inference QoS Assurance](https://arxiv.org/abs/2509.07379v2) | 2509.07379v2 | 8 |
| 2025-09-08 | [Flexible Multimodal Neuroimaging Fusion for Alzheimer's Disease Progression Prediction](https://arxiv.org/abs/2509.12234v1) | 2509.12234v1 | 6 |
| 2025-09-08 | [CAME-AB: Cross-Modality Attention with Mixture-of-Experts for Antibody Binding Site Prediction](https://arxiv.org/abs/2509.06465v4) | 2509.06465v4 | 6 |
| 2025-09-08 | [Ban&Pick: Enhancing Performance and Efficiency of MoE-LLMs via Smarter Routing](https://arxiv.org/abs/2509.06346v3) | 2509.06346v3 | 7 |
| 2025-09-05 | [Robust Experts: the Effect of Adversarial Training on CNNs with Sparse Mixture-of-Experts Layers](https://arxiv.org/abs/2509.05086v1) | 2509.05086v1 | 6 |
| 2025-09-05 | [A Knowledge-Driven Diffusion Policy for End-to-End Autonomous Driving Based on Expert Routing](https://arxiv.org/abs/2509.04853v2) | 2509.04853v2 | 14 |
| 2025-09-05 | [REMOTE: A Unified Multimodal Relation Extraction Framework with Multilevel Optimal Transport and Mixture-of-Experts](https://arxiv.org/abs/2509.04844v1) | 2509.04844v1 | 6 |
| 2025-09-05 | [Dynamic Adaptive Shared Experts with Grouped Multi-Head Attention Mixture of Experts](https://arxiv.org/abs/2509.10530v1) | 2509.10530v1 | 6 |
| 2025-09-02 | [Cache Management for Mixture-of-Experts LLMs -- extended version](https://arxiv.org/abs/2509.02408v1) | 2509.02408v1 | 6 |
| 2025-09-01 | [SimulMEGA: MoE Routers are Advanced Policy Makers for Simultaneous Speech Translation](https://arxiv.org/abs/2509.01200v2) | 2509.01200v2 | 7 |
| 2025-09-01 | [Joint Information Extraction Across Classical and Modern Chinese with Tea-MOELoRA](https://arxiv.org/abs/2509.01158v3) | 2509.01158v3 | 6 |
| 2025-08-31 | [Router Upcycling: Leveraging Mixture-of-Routers in Mixture-of-Experts Upcycling](https://arxiv.org/abs/2509.00679v1) | 2509.00679v1 | 9 |
| 2025-08-29 | [MoE-Health: A Mixture of Experts Framework for Robust Multimodal Healthcare Prediction](https://arxiv.org/abs/2508.21793v1) | 2508.21793v1 | 6 |
| 2025-08-29 | [Accelerating Mixture-of-Experts Inference by Hiding Offloading Latency with Speculative Decoding](https://arxiv.org/abs/2508.21706v2) | 2508.21706v2 | 10 |
| 2025-08-28 | [A Mixture of Experts Gating Network for Enhanced Surrogate Modeling in External Aerodynamics](https://arxiv.org/abs/2508.21249v1) | 2508.21249v1 | 6 |
| 2025-08-27 | [FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control](https://arxiv.org/abs/2508.19926v1) | 2508.19926v1 | 6 |
| 2025-08-27 | [FakeSV-VLM: Taming VLM for Detecting Fake Short-Video News via Progressive Mixture-Of-Experts Adapter](https://arxiv.org/abs/2508.19639v1) | 2508.19639v1 | 10 |
| 2025-08-27 | [Divide, Weight, and Route: Difficulty-Aware Optimization with Dynamic Expert Fusion for Long-tailed Recognition](https://arxiv.org/abs/2508.19630v1) | 2508.19630v1 | 10 |
| 2025-08-27 | [Understanding and Leveraging the Expert Specialization of Context Faithfulness in Mixture-of-Experts LLMs](https://arxiv.org/abs/2508.19594v3) | 2508.19594v3 | 8 |
| 2025-08-27 | [A Self-Supervised Mixture-of-Experts Framework for Multi-behavior Recommendation](https://arxiv.org/abs/2508.19507v2) | 2508.19507v2 | 6 |
| 2025-08-26 | [HAP: Hybrid Adaptive Parallelism for Efficient Mixture-of-Experts Inference](https://arxiv.org/abs/2508.19373v1) | 2508.19373v1 | 6 |
| 2025-08-26 | [Optimal Sparsity of Mixture-of-Experts Language Models for Reasoning Tasks](https://arxiv.org/abs/2508.18672v3) | 2508.18672v3 | 7 |
| 2025-08-25 | [DualSparse-MoE: Coordinating Tensor/Neuron-Level Sparsity with Expert Partition and Reconstruction](https://arxiv.org/abs/2508.18376v1) | 2508.18376v1 | 7 |
| 2025-08-25 | [ISALux: Illumination and Segmentation Aware Transformer Employing Mixture of Experts for Low Light Image Enhancement](https://arxiv.org/abs/2508.17885v1) | 2508.17885v1 | 8 |
| 2025-08-24 | [GateTS: Versatile and Efficient Forecasting via Attention-Inspired routed Mixture-of-Experts](https://arxiv.org/abs/2508.17515v2) | 2508.17515v2 | 8 |
| 2025-08-22 | [Anchor-MoE: A Mean-Anchored Mixture of Experts For Probabilistic Regression](https://arxiv.org/abs/2508.16802v1) | 2508.16802v1 | 9 |
| 2025-08-22 | [Closer to Reality: Practical Semi-Supervised Federated Learning for Foundation Model Adaptation](https://arxiv.org/abs/2508.16568v1) | 2508.16568v1 | 10 |
| 2025-08-22 | [MultiPL-MoE: Multi-Programming-Lingual Extension of Large Language Models through Hybrid Mixture-of-Experts](https://arxiv.org/abs/2508.19268v2) | 2508.19268v2 | 10 |
| 2025-08-22 | [GPT-OSS-20B: A Comprehensive Deployment-Centric Analysis of OpenAI's Open-Weight Mixture of Experts Model](https://arxiv.org/abs/2508.16700v2) | 2508.16700v2 | 10 |
| 2025-08-20 | [MoEcho: Exploiting Side-Channel Attacks to Compromise User Privacy in Mixture-of-Experts LLMs](https://arxiv.org/abs/2508.15036v1) | 2508.15036v1 | 10 |
| 2025-08-19 | [DIME-Net: A Dual-Illumination Adaptive Enhancement Network Based on Retinex and Mixture-of-Experts](https://arxiv.org/abs/2508.13921v1) | 2508.13921v1 | 6 |
| 2025-08-18 | [X-MoE: Enabling Scalable Training for Emerging Mixture-of-Experts Architectures on HPC Platforms](https://arxiv.org/abs/2508.13337v1) | 2508.13337v1 | 8 |
| 2025-08-18 | [Maximum Score Routing For Mixture-of-Experts](https://arxiv.org/abs/2508.12801v1) | 2508.12801v1 | 10 |
| 2025-08-16 | [FNH-TTS: Mixture-of-Experts Duration Modeling for Robust Neural Speech Synthesis](https://arxiv.org/abs/2508.12001v4) | 2508.12001v4 | 6 |
| 2025-08-15 | [MoE-TTS: Enhancing Out-of-Domain Text Understanding for Description-based TTS via Mixture-of-Experts](https://arxiv.org/abs/2508.11326v1) | 2508.11326v1 | 6 |
| 2025-08-13 | [Dynamic Mixture-of-Experts for Incremental Graph Learning](https://arxiv.org/abs/2508.09974v1) | 2508.09974v1 | 6 |
| 2025-08-13 | [MoIIE: Mixture of Intra- and Inter-Modality Experts for Large Vision Language Models](https://arxiv.org/abs/2508.09779v2) | 2508.09779v2 | 9 |
| 2025-08-13 | [TriForecaster: A Mixture of Experts Framework for Multi-Region Electric Load Forecasting with Tri-dimensional Specialization](https://arxiv.org/abs/2508.09753v1) | 2508.09753v1 | 6 |
| 2025-08-13 | [$μ$-Parametrization for Mixture of Experts](https://arxiv.org/abs/2508.09752v2) | 2508.09752v2 | 10 |
| 2025-08-12 | [Wavelet Mixture of Experts for Time Series Forecasting](https://arxiv.org/abs/2508.08825v1) | 2508.08825v1 | 6 |
| 2025-08-11 | [Multi-modal Adaptive Mixture of Experts for Cold-start Recommendation](https://arxiv.org/abs/2508.08042v1) | 2508.08042v1 | 6 |
| 2025-08-11 | [CBDES MoE: Hierarchically Decoupled Mixture-of-Experts for Functional Modules in Autonomous Driving](https://arxiv.org/abs/2508.07838v1) | 2508.07838v1 | 8 |
| 2025-08-11 | [Separation and Collaboration: Two-Level Routing Grouped Mixture-of-Experts for Multi-Domain Continual Learning](https://arxiv.org/abs/2508.07738v1) | 2508.07738v1 | 8 |
| 2025-08-10 | [N-BEATS-MOE: N-BEATS with a Mixture-of-Experts Layer for Heterogeneous Time Series Forecasting](https://arxiv.org/abs/2508.07490v1) | 2508.07490v1 | 6 |
| 2025-08-09 | [A Stage-Aware Mixture of Experts Framework for Neurodegenerative Disease Progression Modelling](https://arxiv.org/abs/2508.07032v1) | 2508.07032v1 | 6 |
| 2025-08-09 | [SSD Offloading for LLM Mixture-of-Experts Weights Considered Harmful in Energy Efficiency](https://arxiv.org/abs/2508.06978v1) | 2508.06978v1 | 7 |
| 2025-08-08 | [Mixture of Experts Guided by Gaussian Splatters Matters: A new Approach to Weakly-Supervised Video Anomaly Detection](https://arxiv.org/abs/2508.06318v1) | 2508.06318v1 | 10 |
| 2025-08-08 | [Towards Unified Image Deblurring using a Mixture-of-Experts Decoder](https://arxiv.org/abs/2508.06228v2) | 2508.06228v2 | 6 |
| 2025-08-08 | [EC2MoE: Adaptive End-Cloud Pipeline Collaboration Enabling Scalable Mixture-of-Experts Inference](https://arxiv.org/abs/2508.06024v1) | 2508.06024v1 | 10 |
| 2025-08-08 | [Efficient Multimodal Streaming Recommendation via Expandable Side Mixture-of-Experts](https://arxiv.org/abs/2508.05993v3) | 2508.05993v3 | 8 |
| 2025-08-05 | [Beyond Hard Sharing: Efficient Multi-Task Speech-to-Text Modeling with Supervised Mixture of Experts](https://arxiv.org/abs/2508.10009v1) | 2508.10009v1 | 6 |
| 2025-08-05 | [Frontier: Simulating the Next Generation of LLM Inference Systems](https://arxiv.org/abs/2508.03148v1) | 2508.03148v1 | 9 |
| 2025-08-04 | [Parameter-Efficient Routed Fine-Tuning: Mixture-of-Experts Demands Mixture of Adaptation Modules](https://arxiv.org/abs/2508.02587v1) | 2508.02587v1 | 6 |
| 2025-08-04 | [FedVLA: Federated Vision-Language-Action Learning with Dual Gating Mixture-of-Experts for Robotic Manipulation](https://arxiv.org/abs/2508.02190v1) | 2508.02190v1 | 6 |
| 2025-08-03 | [RouteMark: A Fingerprint for Intellectual Property Attribution in Routing-based Model Merging](https://arxiv.org/abs/2508.01784v1) | 2508.01784v1 | 8 |
| 2025-08-03 | [Shape Distribution Matters: Shape-Specific Mixture-of-Experts for Amodal Segmentation Under Diverse Occlusions](https://arxiv.org/abs/2508.01664v2) | 2508.01664v2 | 8 |
| 2025-08-03 | [EAC-MoE: Expert-Selection Aware Compressor for Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2508.01625v1) | 2508.01625v1 | 9 |
| 2025-08-01 | [MMBERT: Scaled Mixture-of-Experts Multimodal BERT for Robust Chinese Hate Speech Detection under Cloaking Perturbations](https://arxiv.org/abs/2508.00760v1) | 2508.00760v1 | 8 |
| 2025-08-01 | [GeoMoE: Divide-and-Conquer Motion Field Modeling with Mixture-of-Experts for Two-View Geometry](https://arxiv.org/abs/2508.00592v1) | 2508.00592v1 | 6 |
| 2025-07-30 | [SAEL: Leveraging Large Language Models with Adaptive Mixture-of-Experts for Smart Contract Vulnerability Detection](https://arxiv.org/abs/2507.22371v1) | 2507.22371v1 | 6 |
| 2025-07-28 | [Learning Explainable Stock Predictions with Tweets Using Mixture of Experts](https://arxiv.org/abs/2507.20535v1) | 2507.20535v1 | 6 |
| 2025-07-25 | [A3D-MoE: Acceleration of Large Language Models with Mixture of Experts via 3D Heterogeneous Integration](https://arxiv.org/abs/2507.19142v1) | 2507.19142v1 | 10 |
| 2025-07-24 | [DriftMoE: A Mixture of Experts Approach to Handle Concept Drifts](https://arxiv.org/abs/2507.18464v1) | 2507.18464v1 | 12 |
| 2025-07-23 | [Towards Greater Leverage: Scaling Laws for Efficient Mixture-of-Experts Language Models](https://arxiv.org/abs/2507.17702v4) | 2507.17702v4 | 7 |
| 2025-07-23 | [Dynamic-DINO: Fine-Grained Mixture of Experts Tuning for Real-time Open-Vocabulary Object Detection](https://arxiv.org/abs/2507.17436v1) | 2507.17436v1 | 10 |
| 2025-07-22 | [Adaptive Market Intelligence: A Mixture of Experts Framework for Volatility-Sensitive Stock Forecasting](https://arxiv.org/abs/2508.02686v1) | 2508.02686v1 | 6 |
| 2025-07-21 | [Universal crystal material property prediction via multi-view geometric fusion in graph transformers](https://arxiv.org/abs/2507.15303v1) | 2507.15303v1 | 6 |
| 2025-07-19 | [GEMINUS: Dual-aware Global and Scene-Adaptive Mixture-of-Experts for End-to-End Autonomous Driving](https://arxiv.org/abs/2507.14456v4) | 2507.14456v4 | 8 |
| 2025-07-17 | [R^2MoE: Redundancy-Removal Mixture of Experts for Lifelong Concept Learning](https://arxiv.org/abs/2507.13107v1) | 2507.13107v1 | 10 |
| 2025-07-16 | [Astro-MoE: Mixture of Experts for Multiband Astronomical Time Series](https://arxiv.org/abs/2507.12611v1) | 2507.12611v1 | 6 |
| 2025-07-16 | [CorrMoE: Mixture of Experts with De-stylization Learning for Cross-Scene and Cross-Domain Correspondence Pruning](https://arxiv.org/abs/2507.11834v1) | 2507.11834v1 | 10 |
| 2025-07-15 | [Mixture of Experts in Large Language Models](https://arxiv.org/abs/2507.11181v2) | 2507.11181v2 | 10 |
| 2025-07-14 | [Multi-residual Mixture of Experts Learning for Cooperative Control in Multi-vehicle Systems](https://arxiv.org/abs/2507.09836v1) | 2507.09836v1 | 6 |
| 2025-07-13 | [Explainable AI in Genomics: Transcription Factor Binding Site Prediction with Mixture of Experts](https://arxiv.org/abs/2507.09754v2) | 2507.09754v2 | 6 |
| 2025-07-11 | [BlockFFN: Towards End-Side Acceleration-Friendly Mixture-of-Experts with Chunk-Level Activation Sparsity](https://arxiv.org/abs/2507.08771v2) | 2507.08771v2 | 8 |
| 2025-07-10 | [MoSE: Skill-by-Skill Mixture-of-Experts Learning for Embodied Autonomous Machines](https://arxiv.org/abs/2507.07818v2) | 2507.07818v2 | 8 |
| 2025-07-09 | [SlimCaching: Edge Caching of Mixture-of-Experts for Distributed Inference](https://arxiv.org/abs/2507.06567v3) | 2507.06567v3 | 6 |
| 2025-07-08 | [Speech Quality Assessment Model Based on Mixture of Experts: System-Level Performance Enhancement and Utterance-Level Challenge Analysis](https://arxiv.org/abs/2507.06116v1) | 2507.06116v1 | 6 |
| 2025-07-08 | [Omni-Router: Sharing Routing Decisions in Sparse Mixture-of-Experts for Speech Recognition](https://arxiv.org/abs/2507.05724v3) | 2507.05724v3 | 9 |
| 2025-07-08 | [Efficient Training of Large-Scale AI Models Through Federated Mixture-of-Experts: A System-Level Approach](https://arxiv.org/abs/2507.05685v1) | 2507.05685v1 | 10 |
| 2025-07-07 | [QMoE: A Quantum Mixture of Experts Framework for Scalable Quantum Neural Networks](https://arxiv.org/abs/2507.05190v1) | 2507.05190v1 | 6 |
| 2025-07-07 | [Learning Robust Stereo Matching in the Wild with Selective Mixture-of-Experts](https://arxiv.org/abs/2507.04631v1) | 2507.04631v1 | 6 |
| 2025-07-05 | [Towards Accurate and Efficient 3D Object Detection for Autonomous Driving: A Mixture of Experts Computing System on Edge](https://arxiv.org/abs/2507.04123v2) | 2507.04123v2 | 6 |
| 2025-07-03 | [Neural Inhibition Improves Dynamic Routing and Mixture of Experts](https://arxiv.org/abs/2507.03221v1) | 2507.03221v1 | 10 |
| 2025-07-02 | [MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics](https://arxiv.org/abs/2507.01843v2) | 2507.01843v2 | 6 |
| 2025-07-02 | [Long-Tailed Distribution-Aware Router For Mixture-of-Experts in Large Vision-Language Model](https://arxiv.org/abs/2507.01351v2) | 2507.01351v2 | 17 |
| 2025-07-02 | [Dynamical Multimodal Fusion with Mixture-of-Experts for Localizations](https://arxiv.org/abs/2507.01337v1) | 2507.01337v1 | 8 |
| 2025-06-30 | [Towards Building Private LLMs: Exploring Multi-Node Expert Parallelism on Apple Silicon for Mixture-of-Experts Large Language Model](https://arxiv.org/abs/2506.23635v1) | 2506.23635v1 | 6 |
| 2025-06-29 | [Masked Gated Linear Unit](https://arxiv.org/abs/2506.23225v1) | 2506.23225v1 | 7 |
| 2025-06-29 | [External Data-Enhanced Meta-Representation for Adaptive Probabilistic Load Forecasting](https://arxiv.org/abs/2506.23201v1) | 2506.23201v1 | 8 |
| 2025-06-28 | [Hecto: Modular Sparse Experts for Adaptive and Interpretable Reasoning](https://arxiv.org/abs/2506.22919v2) | 2506.22919v2 | 10 |
| 2025-06-27 | [Towards Distributed Neural Architectures](https://arxiv.org/abs/2506.22389v1) | 2506.22389v1 | 10 |
| 2025-06-26 | [Latent Prototype Routing: Achieving Near-Perfect Load Balancing in Mixture-of-Experts](https://arxiv.org/abs/2506.21328v1) | 2506.21328v1 | 17 |
| 2025-06-26 | [Little by Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts](https://arxiv.org/abs/2506.21035v6) | 2506.21035v6 | 6 |
| 2025-06-26 | [EVA: Mixture-of-Experts Semantic Variant Alignment for Compositional Zero-Shot Learning](https://arxiv.org/abs/2506.20986v1) | 2506.20986v1 | 6 |
| 2025-06-25 | [Opportunistic Osteoporosis Diagnosis via Texture-Preserving Self-Supervision, Mixture of Experts and Multi-Task Integration](https://arxiv.org/abs/2506.20282v1) | 2506.20282v1 | 6 |
| 2025-06-23 | [Multimodal Anomaly Detection with a Mixture-of-Experts](https://arxiv.org/abs/2506.19077v1) | 2506.19077v1 | 6 |
| 2025-06-23 | [Shift Happens: Mixture of Experts based Continual Adaptation in Federated Learning](https://arxiv.org/abs/2506.18789v2) | 2506.18789v2 | 6 |
| 2025-06-23 | [Chain-of-Experts: Unlocking the Communication Power of Mixture-of-Experts Models](https://arxiv.org/abs/2506.18945v1) | 2506.18945v1 | 9 |
| 2025-06-21 | [Physics-informed mixture of experts network for interpretable battery degradation trajectory computation amid second-life complexities](https://arxiv.org/abs/2506.17755v1) | 2506.17755v1 | 6 |
| 2025-06-19 | [Optimizing MoE Routers: Design, Implementation, and Evaluation in Transformer Models](https://arxiv.org/abs/2506.16419v1) | 2506.16419v1 | 7 |
| 2025-06-17 | [NeuroMoE: A Transformer-Based Mixture-of-Experts Framework for Multi-Modal Neurological Disorder Classification](https://arxiv.org/abs/2506.14970v1) | 2506.14970v1 | 6 |
| 2025-06-17 | [Utility-Driven Speculative Decoding for Mixture-of-Experts](https://arxiv.org/abs/2506.20675v1) | 2506.20675v1 | 10 |
| 2025-06-17 | [Exploring Speaker Diarization with Mixture of Experts](https://arxiv.org/abs/2506.14750v1) | 2506.14750v1 | 6 |
| 2025-06-17 | [LoRA-Mixer: Coordinate Modular LoRA Experts Through Serial Attention Routing](https://arxiv.org/abs/2507.00029v2) | 2507.00029v2 | 8 |
| 2025-06-16 | [Load Balancing Mixture of Experts with Similarity Preserving Routers](https://arxiv.org/abs/2506.14038v2) | 2506.14038v2 | 15 |
| 2025-06-16 | [EAQuant: Enhancing Post-Training Quantization for MoE Models via Expert-Aware Optimization](https://arxiv.org/abs/2506.13329v3) | 2506.13329v3 | 8 |
| 2025-06-14 | [Automatic Expert Discovery in LLM Upcycling via Sparse Interpolated Mixture-of-Experts](https://arxiv.org/abs/2506.12597v1) | 2506.12597v1 | 8 |
| 2025-06-14 | [Group then Scale: Dynamic Mixture-of-Experts Multilingual Language Model](https://arxiv.org/abs/2506.12388v1) | 2506.12388v1 | 6 |
| 2025-06-13 | [Mixture-of-Experts Can Surpass Dense LLMs Under Strictly Equal Resource](https://arxiv.org/abs/2506.12119v2) | 2506.12119v2 | 6 |
| 2025-06-11 | [DIVE into MoE: Diversity-Enhanced Reconstruction of Large Language Models from Dense into Mixture-of-Experts](https://arxiv.org/abs/2506.09351v1) | 2506.09351v1 | 10 |
| 2025-06-10 | [CoQMoE: Co-Designed Quantization and Computation Orchestration for Mixture-of-Experts Vision Transformer on FPGA](https://arxiv.org/abs/2506.08496v1) | 2506.08496v1 | 6 |
| 2025-06-10 | [MedMoE: Modality-Specialized Mixture of Experts for Medical Vision-Language Understanding](https://arxiv.org/abs/2506.08356v2) | 2506.08356v2 | 10 |
| 2025-06-09 | [MoQAE: Mixed-Precision Quantization for Long-Context LLM Inference via Mixture of Quantization-Aware Experts](https://arxiv.org/abs/2506.07533v1) | 2506.07533v1 | 6 |
| 2025-06-09 | [MoE-GPS: Guidlines for Prediction Strategy for Dynamic Expert Duplication in MoE Load Balancing](https://arxiv.org/abs/2506.07366v1) | 2506.07366v1 | 10 |
| 2025-06-05 | [Mixture-of-Experts Meets In-Context Reinforcement Learning](https://arxiv.org/abs/2506.05426v3) | 2506.05426v3 | 8 |
| 2025-06-04 | [Mitigating Task Objective Conflicts for Continual Learning in Unified Multimodal Models](https://arxiv.org/abs/2506.03591v3) | 2506.03591v3 | 6 |
| 2025-06-03 | [PC-MoE: Memory-Efficient and Privacy-Preserving Collaborative Training for Mixture-of-Experts LLMs](https://arxiv.org/abs/2506.02965v2) | 2506.02965v2 | 6 |
| 2025-06-03 | [Multi-level Mixture of Experts for Multimodal Entity Linking](https://arxiv.org/abs/2507.07108v1) | 2507.07108v1 | 6 |
| 2025-06-02 | [Mixture of Experts Provably Detect and Learn the Latent Cluster Structure in Gradient-Based Learning](https://arxiv.org/abs/2506.01656v2) | 2506.01656v2 | 8 |
| 2025-06-01 | [FLEx: Personalized Federated Learning for Mixture-of-Experts LLMs via Expert Grafting](https://arxiv.org/abs/2506.00965v2) | 2506.00965v2 | 10 |
| 2025-05-31 | [Enhancing Multimodal Continual Instruction Tuning with BranchLoRA](https://arxiv.org/abs/2506.02041v1) | 2506.02041v1 | 6 |
| 2025-05-30 | [Mixture-of-Experts for Personalized and Semantic-Aware Next Location Prediction](https://arxiv.org/abs/2505.24597v1) | 2505.24597v1 | 6 |
| 2025-05-30 | [Decoding Knowledge Attribution in Mixture-of-Experts: A Framework of Basic-Refinement Collaboration and Efficiency Analysis](https://arxiv.org/abs/2505.24593v2) | 2505.24593v2 | 6 |
| 2025-05-30 | [On the Expressive Power of Mixture-of-Experts for Structured Complex Tasks](https://arxiv.org/abs/2505.24205v2) | 2505.24205v2 | 6 |
| 2025-05-29 | [Point-MoE: Large-Scale Multi-Dataset Training with Mixture-of-Experts for 3D Semantic Segmentation](https://arxiv.org/abs/2505.23926v2) | 2505.23926v2 | 9 |
| 2025-05-28 | [Less, but Better: Efficient Multilingual Expansion for LLMs via Layer-wise Mixture-of-Experts](https://arxiv.org/abs/2505.22582v1) | 2505.22582v1 | 8 |
| 2025-05-28 | [Advancing Expert Specialization for Better MoE](https://arxiv.org/abs/2505.22323v5) | 2505.22323v5 | 9 |
| 2025-05-28 | [EvoMoE: Expert Evolution in Mixture of Experts for Multimodal Large Language Models](https://arxiv.org/abs/2505.23830v1) | 2505.23830v1 | 8 |
| 2025-05-27 | [Pangu Pro MoE: Mixture of Grouped Experts for Efficient Sparsity](https://arxiv.org/abs/2505.21411v2) | 2505.21411v2 | 9 |
| 2025-05-27 | [Uni3D-MoE: Scalable Multimodal 3D Scene Understanding via Mixture of Experts](https://arxiv.org/abs/2505.21079v1) | 2505.21079v1 | 10 |
| 2025-05-27 | [Multi-objective Large Language Model Alignment with Hierarchical Experts](https://arxiv.org/abs/2505.20925v1) | 2505.20925v1 | 6 |
| 2025-05-26 | [FLAME-MoE: A Transparent End-to-End Research Platform for Mixture-of-Experts Language Models](https://arxiv.org/abs/2505.20225v1) | 2505.20225v1 | 7 |
| 2025-05-26 | [NEXT: Multi-Grained Mixture of Experts via Text-Modulation for Multi-Modal Object Re-Identification](https://arxiv.org/abs/2505.20001v5) | 2505.20001v5 | 6 |
| 2025-05-26 | [Mosaic: Data-Free Knowledge Distillation via Mixture-of-Experts for Heterogeneous Distributed Environments](https://arxiv.org/abs/2505.19699v2) | 2505.19699v2 | 6 |
| 2025-05-25 | [I2MoE: Interpretable Multimodal Interaction-aware Mixture-of-Experts](https://arxiv.org/abs/2505.19190v1) | 2505.19190v1 | 10 |
| 2025-05-24 | [MoveGPT: Scaling Mobility Foundation Models with Spatially-Aware Mixture of Experts](https://arxiv.org/abs/2505.18670v3) | 2505.18670v3 | 11 |
| 2025-05-24 | [Guiding the Experts: Semantic Priors for Efficient and Focused MoE Routing](https://arxiv.org/abs/2505.18586v1) | 2505.18586v1 | 9 |
| 2025-05-24 | [On Minimax Estimation of Parameters in Softmax-Contaminated Mixture of Experts](https://arxiv.org/abs/2505.18455v2) | 2505.18455v2 | 6 |
| 2025-05-23 | [EvidenceMoE: A Physics-Guided Mixture-of-Experts with Evidential Critics for Advancing Fluorescence Light Detection and Ranging in Scattering Media](https://arxiv.org/abs/2505.21532v1) | 2505.21532v1 | 6 |
| 2025-05-23 | [PreMoE: Proactive Inference for Efficient Mixture-of-Experts](https://arxiv.org/abs/2505.17639v4) | 2505.17639v4 | 8 |
| 2025-05-23 | [CoMoE: Contrastive Representation for Mixture-of-Experts in Parameter-Efficient Fine-tuning](https://arxiv.org/abs/2505.17553v2) | 2505.17553v2 | 8 |
| 2025-05-23 | [MEGADance: Mixture-of-Experts Architecture for Genre-Aware 3D Dance Generation](https://arxiv.org/abs/2505.17543v3) | 2505.17543v3 | 6 |
| 2025-05-22 | [DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving](https://arxiv.org/abs/2505.16278v2) | 2505.16278v2 | 8 |
| 2025-05-21 | [MoRE-Brain: Routed Mixture of Experts for Interpretable and Generalizable Cross-Subject fMRI Visual Decoding](https://arxiv.org/abs/2505.15946v3) | 2505.15946v3 | 12 |
| 2025-05-21 | [Time Tracker: Mixture-of-Experts-Enhanced Foundation Time Series Forecasting Model with Decoupled Training Pipelines](https://arxiv.org/abs/2505.15151v2) | 2505.15151v2 | 10 |
| 2025-05-20 | [Balanced and Elastic End-to-end Training of Dynamic LLMs](https://arxiv.org/abs/2505.14864v2) | 2505.14864v2 | 8 |
| 2025-05-20 | [Scaling and Enhancing LLM-based AVSR: A Sparse Mixture of Projectors Approach](https://arxiv.org/abs/2505.14336v2) | 2505.14336v2 | 7 |
| 2025-05-19 | [CompeteSMoE -- Statistically Guaranteed Mixture of Experts Training via Competition](https://arxiv.org/abs/2505.13380v1) | 2505.13380v1 | 8 |
| 2025-05-19 | [EMoE: Training-Free Expert Disagreement for Uncertainty-Aware Text-to-Image Diffusion](https://arxiv.org/abs/2505.13273v2) | 2505.13273v2 | 6 |
| 2025-05-19 | [Model Selection for Gaussian-gated Gaussian Mixture of Experts Using Dendrograms of Mixing Measures](https://arxiv.org/abs/2505.13052v2) | 2505.13052v2 | 6 |
| 2025-05-18 | [Scene-Adaptive Motion Planning with Explicit Mixture of Experts and Interaction-Oriented Optimization](https://arxiv.org/abs/2505.12311v3) | 2505.12311v3 | 8 |
| 2025-05-16 | [MegaScale-MoE: Large-Scale Communication-Efficient Training of Mixture-of-Experts Models in Production](https://arxiv.org/abs/2505.11432v3) | 2505.11432v3 | 6 |
| 2025-05-16 | [MoE-CAP: Benchmarking Cost, Accuracy and Performance of Sparse Mixture-of-Experts Systems](https://arxiv.org/abs/2505.11415v2) | 2505.11415v2 | 8 |
| 2025-05-16 | [On DeepSeekMoE: Statistical Benefits of Shared Experts and Normalized Sigmoid Gating](https://arxiv.org/abs/2505.10860v2) | 2505.10860v2 | 6 |
| 2025-05-14 | [PT-MoE: An Efficient Finetuning Framework for Integrating Mixture-of-Experts into Prompt Tuning](https://arxiv.org/abs/2505.09519v1) | 2505.09519v1 | 8 |
| 2025-05-13 | [Toward Cost-Efficient Serving of Mixture-of-Experts with Asynchrony](https://arxiv.org/abs/2505.08944v2) | 2505.08944v2 | 6 |
| 2025-05-13 | [PWC-MoE: Privacy-Aware Wireless Collaborative Mixture of Experts](https://arxiv.org/abs/2505.08719v1) | 2505.08719v1 | 6 |
| 2025-05-12 | [UMoE: Unifying Attention and FFN with Shared Experts](https://arxiv.org/abs/2505.07260v2) | 2505.07260v2 | 7 |
| 2025-05-11 | [The power of fine-grained experts: Granularity boosts expressivity in Mixture of Experts](https://arxiv.org/abs/2505.06839v1) | 2505.06839v1 | 11 |
| 2025-05-10 | [PRIME: Physics-Related Intelligent Mixture of Experts for Transistor Characteristics Prediction](https://arxiv.org/abs/2505.11523v1) | 2505.11523v1 | 6 |
| 2025-05-03 | [BadPatches: Routing-Aware Backdoor Attacks on Vision Mixture-of-Experts](https://arxiv.org/abs/2505.01811v4) | 2505.01811v4 | 7 |
| 2025-05-02 | [MoEQuant: Enhancing Quantization for Mixture-of-Experts Large Language Models via Expert-Balanced Sampling and Affinity Guidance](https://arxiv.org/abs/2505.03804v1) | 2505.03804v1 | 6 |
| 2025-05-01 | [Improving Routing in Sparse Mixture of Experts with Graph of Tokens](https://arxiv.org/abs/2505.00792v1) | 2505.00792v1 | 6 |
| 2025-04-29 | [TT-LoRA MoE: Unifying Parameter-Efficient Fine-Tuning and Sparse Mixture-of-Experts](https://arxiv.org/abs/2504.21190v1) | 2504.21190v1 | 12 |
| 2025-04-29 | [Token-Level Prompt Mixture with Parameter-Free Routing for Federated Domain Generalization](https://arxiv.org/abs/2504.21063v1) | 2504.21063v1 | 6 |
| 2025-04-29 | [FT-MoE: Sustainable-learning Mixture of Experts for Fault-Tolerant Computing](https://arxiv.org/abs/2504.20446v2) | 2504.20446v2 | 10 |
| 2025-04-29 | [MicarVLMoE: A Modern Gated Cross-Aligned Vision-Language Mixture of Experts Model for Medical Image Captioning and Report Generation](https://arxiv.org/abs/2504.20343v1) | 2504.20343v1 | 10 |
| 2025-04-28 | [SYMI: Efficient Mixture-of-Experts Training via Model and Optimizer State Decoupling](https://arxiv.org/abs/2504.19925v2) | 2504.19925v2 | 9 |
| 2025-04-28 | [Mixture of Experts for Decentralized Generative AI and Reinforcement Learning in Wireless Networks: A Comprehensive Survey](https://arxiv.org/abs/2504.19660v2) | 2504.19660v2 | 7 |
| 2025-04-28 | [ARTEMIS: Autoregressive End-to-End Trajectory Planning with Mixture of Experts for Autonomous Driving](https://arxiv.org/abs/2504.19580v2) | 2504.19580v2 | 10 |
| 2025-04-24 | [BadMoE: Backdooring Mixture-of-Experts LLMs via Optimizing Routing Triggers and Infecting Dormant Experts](https://arxiv.org/abs/2504.18598v2) | 2504.18598v2 | 7 |
| 2025-04-18 | [Multi-Type Context-Aware Conversational Recommender Systems via Mixture-of-Experts](https://arxiv.org/abs/2504.13655v2) | 2504.13655v2 | 6 |
| 2025-04-16 | [Dense Backpropagation Improves Training for Sparse Mixture-of-Experts](https://arxiv.org/abs/2504.12463v3) | 2504.12463v3 | 12 |
| 2025-04-16 | [Trend Filtered Mixture of Experts for Automated Gating of High-Frequency Flow Cytometry Data](https://arxiv.org/abs/2504.12287v1) | 2504.12287v1 | 10 |
| 2025-04-16 | [MOS: Towards Effective Smart Contract Vulnerability Detection through Mixture-of-Experts Tuning of Large Language Models](https://arxiv.org/abs/2504.12234v1) | 2504.12234v1 | 8 |
| 2025-04-16 | [Unveiling Hidden Collaboration within Mixture-of-Experts in Large Language Models](https://arxiv.org/abs/2504.12359v1) | 2504.12359v1 | 6 |
| 2025-04-14 | [Plasticity-Aware Mixture of Experts for Learning Under QoE Shifts in Adaptive Video Streaming](https://arxiv.org/abs/2504.09906v2) | 2504.09906v2 | 6 |
| 2025-04-11 | [RouterKT: Mixture-of-Experts for Knowledge Tracing](https://arxiv.org/abs/2504.08989v3) | 2504.08989v3 | 9 |
| 2025-04-10 | [Cluster-Driven Expert Pruning for Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2504.07807v1) | 2504.07807v1 | 7 |
| 2025-04-10 | [Adaptive Detection of Fast Moving Celestial Objects Using a Mixture of Experts and Physical-Inspired Neural Network](https://arxiv.org/abs/2504.07777v1) | 2504.07777v1 | 6 |
| 2025-04-09 | [MoEDiff-SR: Mixture of Experts-Guided Diffusion Model for Region-Adaptive MRI Super-Resolution](https://arxiv.org/abs/2504.07308v1) | 2504.07308v1 | 6 |
| 2025-04-09 | [Domain-Specific Pruning of Large Mixture-of-Experts Models with Few-shot Demonstrations](https://arxiv.org/abs/2504.06792v2) | 2504.06792v2 | 6 |
| 2025-04-04 | [HeterMoE: Efficient Training of Mixture-of-Experts Models on Heterogeneous GPUs](https://arxiv.org/abs/2504.03871v1) | 2504.03871v1 | 10 |
| 2025-04-03 | [MegaScale-Infer: Serving Mixture-of-Experts at Scale with Disaggregated Expert Parallelism](https://arxiv.org/abs/2504.02263v4) | 2504.02263v4 | 9 |
| 2025-04-02 | [Advancing MoE Efficiency: A Collaboration-Constrained Routing (C2R) Strategy for Better Expert Parallelism Design](https://arxiv.org/abs/2504.01337v2) | 2504.01337v2 | 8 |
| 2025-04-01 | [Mixture-of-Experts for Distributed Edge Computing with Channel-Aware Gating Function](https://arxiv.org/abs/2504.00819v1) | 2504.00819v1 | 6 |
| 2025-04-01 | [A Unified Virtual Mixture-of-Experts Framework:Enhanced Inference and Hallucination Mitigation in Single-Model System](https://arxiv.org/abs/2504.03739v1) | 2504.03739v1 | 6 |
| 2025-04-01 | [DynMoLE: Boosting Mixture of LoRA Experts Fine-Tuning with a Hybrid Routing Mechanism](https://arxiv.org/abs/2504.00661v1) | 2504.00661v1 | 6 |
| 2025-03-30 | [Mixture of Routers](https://arxiv.org/abs/2503.23362v3) | 2503.23362v3 | 11 |
| 2025-03-29 | [S2MoE: Robust Sparse Mixture of Experts via Stochastic Learning](https://arxiv.org/abs/2503.23007v1) | 2503.23007v1 | 8 |
| 2025-03-29 | [Rethinking Sparse Mixture of Experts from a Unified Perspective](https://arxiv.org/abs/2503.22996v3) | 2503.22996v3 | 6 |
| 2025-03-28 | [Exploiting Mixture-of-Experts Redundancy Unlocks Multimodal Generative Abilities](https://arxiv.org/abs/2503.22517v2) | 2503.22517v2 | 6 |
| 2025-03-27 | [RocketPPA: Code-Level Power, Performance, and Area Prediction via LLM and Mixture of Experts](https://arxiv.org/abs/2503.21971v3) | 2503.21971v3 | 10 |
| 2025-03-27 | [LLaVA-CMoE: Towards Continual Mixture of Experts for Large Vision-Language Models](https://arxiv.org/abs/2503.21227v3) | 2503.21227v3 | 8 |
| 2025-03-26 | [A multi-scale lithium-ion battery capacity prediction using mixture of experts and patch-based MLP](https://arxiv.org/abs/2504.03706v1) | 2504.03706v1 | 6 |
| 2025-03-26 | [MoLe-VLA: Dynamic Layer-skipping Vision Language Action Model via Mixture-of-Layers for Efficient Robot Manipulation](https://arxiv.org/abs/2503.20384v2) | 2503.20384v2 | 6 |
| 2025-03-25 | [Resilient Sensor Fusion under Adverse Sensor Failures via Multi-Modal Expert Fusion](https://arxiv.org/abs/2503.19776v2) | 2503.19776v2 | 6 |
| 2025-03-25 | [M$^2$CD: A Unified MultiModal Framework for Optical-SAR Change Detection with Mixture of Experts and Self-Distillation](https://arxiv.org/abs/2503.19406v1) | 2503.19406v1 | 6 |
| 2025-03-24 | [SPMTrack: Spatio-Temporal Parameter-Efficient Fine-Tuning with Mixture of Experts for Scalable Visual Tracking](https://arxiv.org/abs/2503.18338v2) | 2503.18338v2 | 10 |
| 2025-03-23 | [ExpertRAG: Efficient RAG with Mixture of Experts -- Optimizing Context Retrieval for Adaptive LLM Responses](https://arxiv.org/abs/2504.08744v1) | 2504.08744v1 | 19 |
| 2025-03-23 | [Challenging Dataset and Multi-modal Gated Mixture of Experts Model for Remote Sensing Copy-Move Forgery Understanding](https://arxiv.org/abs/2503.18104v3) | 2503.18104v3 | 6 |
| 2025-03-22 | [Every Sample Matters: Leveraging Mixture-of-Experts and High-Quality Data for Efficient and Accurate Code LLM](https://arxiv.org/abs/2503.17793v1) | 2503.17793v1 | 6 |
| 2025-03-20 | [Expert Race: A Flexible Routing Strategy for Scaling Diffusion Transformer with Mixture of Experts](https://arxiv.org/abs/2503.16057v3) | 2503.16057v3 | 9 |
| 2025-03-20 | [Mixture of Lookup Experts](https://arxiv.org/abs/2503.15798v2) | 2503.15798v2 | 6 |
| 2025-03-18 | [MAST-Pro: Dynamic Mixture-of-Experts for Adaptive Segmentation of Pan-Tumors with Knowledge-Driven Prompts](https://arxiv.org/abs/2503.14355v1) | 2503.14355v1 | 6 |
| 2025-03-18 | [SNAKE: A Sustainable and Multi-functional Traffic Analysis System utilizing Specialized Large-Scale Models with a Mixture of Experts Architecture](https://arxiv.org/abs/2503.13808v1) | 2503.13808v1 | 6 |
| 2025-03-17 | [Optimal Expert Selection for Distributed Mixture-of-Experts at the Wireless Edge](https://arxiv.org/abs/2503.13421v1) | 2503.13421v1 | 6 |
| 2025-03-16 | [MoECollab: Democratizing LLM Development Through Collaborative Mixture of Experts](https://arxiv.org/abs/2503.12592v1) | 2503.12592v1 | 6 |
| 2025-03-13 | [dFLMoE: Decentralized Federated Learning via Mixture of Experts for Medical Data Analysis](https://arxiv.org/abs/2503.10412v4) | 2503.10412v4 | 6 |
| 2025-03-12 | [Double-Stage Feature-Level Clustering-Based Mixture of Experts Framework](https://arxiv.org/abs/2503.09504v1) | 2503.09504v1 | 10 |
| 2025-03-12 | [Astrea: A MOE-based Visual Understanding Model with Progressive Alignment](https://arxiv.org/abs/2503.09445v2) | 2503.09445v2 | 8 |
| 2025-03-11 | [MoE-Loco: Mixture of Experts for Multitask Locomotion](https://arxiv.org/abs/2503.08564v2) | 2503.08564v2 | 6 |
| 2025-03-11 | [Accelerating MoE Model Inference with Expert Sharding](https://arxiv.org/abs/2503.08467v1) | 2503.08467v1 | 8 |
| 2025-03-10 | [MELON: Multimodal Mixture-of-Experts with Spectral-Temporal Fusion for Long-Term Mobility Estimation in Critical Care](https://arxiv.org/abs/2503.11695v1) | 2503.11695v1 | 6 |
| 2025-03-10 | [GM-MoE: Low-Light Enhancement with Gated-Mechanism Mixture-of-Experts](https://arxiv.org/abs/2503.07417v5) | 2503.07417v5 | 6 |
| 2025-03-10 | [A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications](https://arxiv.org/abs/2503.07137v4) | 2503.07137v4 | 10 |
| 2025-03-10 | [ResMoE: Space-efficient Compression of Mixture of Experts LLMs via Residual Restoration](https://arxiv.org/abs/2503.06881v1) | 2503.06881v1 | 10 |
| 2025-03-10 | [eMoE: Task-aware Memory Efficient Mixture-of-Experts-Based (MoE) Model Inference](https://arxiv.org/abs/2503.06823v1) | 2503.06823v1 | 10 |
| 2025-03-08 | [MANDARIN: Mixture-of-Experts Framework for Dynamic Delirium and Coma Prediction in ICU Patients: Development and Validation of an Acute Brain Dysfunction Prediction Model](https://arxiv.org/abs/2503.06059v1) | 2503.06059v1 | 6 |
| 2025-03-07 | [Skill-Based Mixture-of-Experts: Adaptive Routing for Heterogeneous Reasoning via Inferred Skills](https://arxiv.org/abs/2503.05641v4) | 2503.05641v4 | 6 |
| 2025-03-07 | [Every FLOP Counts: Scaling a 300B Mixture-of-Experts LING LLM without Premium GPUs](https://arxiv.org/abs/2503.05139v2) | 2503.05139v2 | 11 |
| 2025-03-07 | [Capacity-Aware Inference: Mitigating the Straggler Effect in Mixture of Experts](https://arxiv.org/abs/2503.05066v5) | 2503.05066v5 | 11 |
| 2025-03-06 | [Continual Pre-training of MoEs: How robust is your router?](https://arxiv.org/abs/2503.05029v2) | 2503.05029v2 | 7 |
| 2025-03-06 | [DM-Adapter: Domain-Aware Mixture-of-Adapters for Text-Based Person Retrieval](https://arxiv.org/abs/2503.04144v1) | 2503.04144v1 | 6 |
| 2025-03-05 | [Mixture of Experts Made Intrinsically Interpretable](https://arxiv.org/abs/2503.07639v1) | 2503.07639v1 | 11 |
| 2025-03-05 | [Convergence Rates for Softmax Gating Mixture of Experts](https://arxiv.org/abs/2503.03213v1) | 2503.03213v1 | 8 |
| 2025-03-03 | [How Do Consumers Really Choose: Exposing Hidden Preferences with the Mixture of Experts Model](https://arxiv.org/abs/2503.05800v1) | 2503.05800v1 | 6 |
| 2025-03-03 | [DeRS: Towards Extremely Efficient Upcycled Mixture-of-Experts Models](https://arxiv.org/abs/2503.01359v1) | 2503.01359v1 | 8 |
| 2025-03-03 | [PROPER: A Progressive Learning Framework for Personalized Large Language Models with Group-Level Adaptation](https://arxiv.org/abs/2503.01303v1) | 2503.01303v1 | 6 |
| 2025-03-01 | [Efficiently Editing Mixture-of-Experts Models with Compressed Experts](https://arxiv.org/abs/2503.00634v2) | 2503.00634v2 | 7 |
| 2025-03-01 | [CL-MoE: Enhancing Multimodal Large Language Model with Dual Momentum Mixture-of-Experts for Continual Visual Question Answering](https://arxiv.org/abs/2503.00413v1) | 2503.00413v1 | 8 |
| 2025-02-28 | [CoSMoEs: Compact Sparse Mixture of Experts](https://arxiv.org/abs/2503.00245v1) | 2503.00245v1 | 6 |
| 2025-02-27 | [R2-T2: Re-Routing in Test-Time for Multimodal Mixture-of-Experts](https://arxiv.org/abs/2502.20395v2) | 2502.20395v2 | 8 |
| 2025-02-27 | [Mixture of Experts for Recognizing Depression from Interview and Reading Tasks](https://arxiv.org/abs/2502.20213v2) | 2502.20213v2 | 6 |
| 2025-02-27 | [Mixture of Experts-augmented Deep Unfolding for Activity Detection in IRS-aided Systems](https://arxiv.org/abs/2502.20183v2) | 2502.20183v2 | 6 |
| 2025-02-27 | [Comet: Fine-grained Computation-communication Overlapping for Mixture-of-Experts](https://arxiv.org/abs/2502.19811v3) | 2502.19811v3 | 6 |
| 2025-02-26 | [Drop-Upcycling: Training Sparse Mixture of Experts with Partial Re-initialization](https://arxiv.org/abs/2502.19261v2) | 2502.19261v2 | 6 |
| 2025-02-24 | [BigMac: A Communication-Efficient Mixture-of-Experts Model Structure for Fast Training and Inference](https://arxiv.org/abs/2502.16927v2) | 2502.16927v2 | 6 |
| 2025-02-24 | [Make LoRA Great Again: Boosting LoRA with Adaptive Singular Values and Mixture-of-Experts Optimization Alignment](https://arxiv.org/abs/2502.16894v4) | 2502.16894v4 | 7 |
| 2025-02-21 | [Binary-Integer-Programming Based Algorithm for Expert Load Balancing in Mixture-of-Experts Models](https://arxiv.org/abs/2502.15451v2) | 2502.15451v2 | 12 |
| 2025-02-21 | [Tight Clusters Make Specialized Experts](https://arxiv.org/abs/2502.15315v3) | 2502.15315v3 | 10 |
| 2025-02-21 | [Multimodal Graph-Based Variational Mixture of Experts Network for Zero-Shot Multimodal Information Extraction](https://arxiv.org/abs/2502.15290v1) | 2502.15290v1 | 6 |
| 2025-02-19 | [Unraveling the Localized Latents: Learning Stratified Manifold Structures in LLM Embedding Space with Sparse Mixture-of-Experts](https://arxiv.org/abs/2502.13577v1) | 2502.13577v1 | 6 |
| 2025-02-18 | [Every Expert Matters: Towards Effective Knowledge Distillation for Mixture-of-Experts Language Models](https://arxiv.org/abs/2502.12947v1) | 2502.12947v1 | 9 |
| 2025-02-18 | [DSMoE: Matrix-Partitioned Experts with Dynamic Routing for Computation-Efficient Dense LLMs](https://arxiv.org/abs/2502.12455v3) | 2502.12455v3 | 8 |
| 2025-02-17 | [From Dense to Dynamic: Token-Difficulty Driven MoEfication of Pre-Trained LLMs](https://arxiv.org/abs/2502.12325v1) | 2502.12325v1 | 6 |
| 2025-02-17 | [How to Upscale Neural Networks with Scaling Law? A Survey and Practical Guidelines](https://arxiv.org/abs/2502.12051v3) | 2502.12051v3 | 6 |
| 2025-02-17 | [Fate: Fast Edge Inference of Mixture-of-Experts Models via Cross-Layer Gate](https://arxiv.org/abs/2502.12224v2) | 2502.12224v2 | 6 |
| 2025-02-12 | [Heterogeneous Mixture of Experts for Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2502.09654v2) | 2502.09654v2 | 6 |
| 2025-02-11 | [Training Sparse Mixture Of Experts Text Embedding Models](https://arxiv.org/abs/2502.07972v3) | 2502.07972v3 | 7 |
| 2025-02-11 | [MoENAS: Mixture-of-Expert based Neural Architecture Search for jointly Accurate, Fair, and Robust Edge Deep Neural Networks](https://arxiv.org/abs/2502.07422v1) | 2502.07422v1 | 8 |
| 2025-02-10 | [Fair-MoE: Fairness-Oriented Mixture of Experts in Vision-Language Models](https://arxiv.org/abs/2502.06094v1) | 2502.06094v1 | 6 |
| 2025-02-08 | [Mol-MoE: Training Preference-Guided Routers for Molecule Generation](https://arxiv.org/abs/2502.05633v1) | 2502.05633v1 | 7 |
| 2025-02-08 | [UbiMoE: A Ubiquitous Mixture-of-Experts Vision Transformer Accelerator With Hybrid Computation Pattern on FPGA](https://arxiv.org/abs/2502.05602v3) | 2502.05602v3 | 6 |
| 2025-02-07 | [Towards Foundational Models for Dynamical System Reconstruction: Hierarchical Meta-Learning via Mixture of Experts](https://arxiv.org/abs/2502.05335v2) | 2502.05335v2 | 6 |
| 2025-02-07 | [Joint MoE Scaling Laws: Mixture of Experts Can Be Memory Efficient](https://arxiv.org/abs/2502.05172v2) | 2502.05172v2 | 7 |
| 2025-02-06 | [Analytical FFN-to-MoE Restructuring via Activation Pattern Analysis](https://arxiv.org/abs/2502.04416v3) | 2502.04416v3 | 9 |
| 2025-02-05 | [Optimizing Robustness and Accuracy in Mixture of Experts: A Dual-Model Approach](https://arxiv.org/abs/2502.06832v3) | 2502.06832v3 | 8 |
| 2025-02-05 | [RepLoRA: Reparameterizing Low-Rank Adaptation via the Perspective of Mixture of Experts](https://arxiv.org/abs/2502.03044v2) | 2502.03044v2 | 6 |
| 2025-02-05 | [Scaling Laws for Upcycling Mixture-of-Experts Language Models](https://arxiv.org/abs/2502.03009v2) | 2502.03009v2 | 7 |
| 2025-02-04 | [Themis: Efficient Sparse Model Training Through Fully Sharded Sparse Data Parallelism](https://arxiv.org/abs/2502.02581v2) | 2502.02581v2 | 9 |
| 2025-02-03 | [CLIP-UP: A Simple and Efficient Mixture-of-Experts CLIP Training Recipe with Sparse Upcycling](https://arxiv.org/abs/2502.00965v2) | 2502.00965v2 | 7 |
| 2025-02-01 | [Sigmoid Self-Attention has Lower Sample Complexity than Softmax Self-Attention: A Mixture-of-Experts Perspective](https://arxiv.org/abs/2502.00281v2) | 2502.00281v2 | 10 |
| 2025-01-30 | [MolGraph-xLSTM: A graph-based dual-level xLSTM framework with multi-head mixture-of-experts for enhanced molecular representation and interpretability](https://arxiv.org/abs/2501.18439v1) | 2501.18439v1 | 10 |
| 2025-01-29 | [Free Agent in Agent-Based Mixture-of-Experts Generative AI Framework](https://arxiv.org/abs/2501.17903v2) | 2501.17903v2 | 6 |
| 2025-01-29 | [Heuristic-Informed Mixture of Experts for Link Prediction in Multilayer Networks](https://arxiv.org/abs/2501.17557v1) | 2501.17557v1 | 10 |
| 2025-01-28 | [3D-MoE: Towards Spatial Intelligence with Mixture-of-Experts for 3D Reasoning and Action Generation](https://arxiv.org/abs/2501.16698v2) | 2501.16698v2 | 7 |
| 2025-01-27 | [One-for-All Does Not Work! Enhancing Vulnerability Detection by Mixture-of-Experts (MoE)](https://arxiv.org/abs/2501.16454v2) | 2501.16454v2 | 6 |
| 2025-01-25 | [ToMoE: Converting Dense Large Language Models to Mixture-of-Experts through Dynamic Structural Pruning](https://arxiv.org/abs/2501.15316v2) | 2501.15316v2 | 10 |
| 2025-01-25 | [FreqMoE: Enhancing Time Series Forecasting through Frequency Decomposition Mixture of Experts](https://arxiv.org/abs/2501.15125v2) | 2501.15125v2 | 10 |
| 2025-01-25 | [Each Rank Could be an Expert: Single-Ranked Mixture of Experts LoRA for Multi-Task Learning](https://arxiv.org/abs/2501.15103v2) | 2501.15103v2 | 6 |
| 2025-01-24 | [Hierarchical Time-Aware Mixture of Experts for Multi-Modal Sequential Recommendation](https://arxiv.org/abs/2501.14269v2) | 2501.14269v2 | 6 |
| 2025-01-24 | [Sparse Mixture-of-Experts for Non-Uniform Noise Reduction in MRI Images](https://arxiv.org/abs/2501.14198v3) | 2501.14198v3 | 6 |
| 2025-01-22 | [Autonomy-of-Experts Models](https://arxiv.org/abs/2501.13074v2) | 2501.13074v2 | 6 |
| 2025-01-22 | [BLR-MoE: Boosted Language-Routing Mixture of Experts for Domain-Robust Multilingual E2E ASR](https://arxiv.org/abs/2501.12602v1) | 2501.12602v1 | 10 |
| 2025-01-21 | [Parameters vs FLOPs: Scaling Laws for Optimal Sparsity for Mixture-of-Experts Language Models](https://arxiv.org/abs/2501.12370v3) | 2501.12370v3 | 7 |
| 2025-01-21 | [Modality Interactive Mixture-of-Experts for Fake News Detection](https://arxiv.org/abs/2501.12431v2) | 2501.12431v2 | 6 |
| 2025-01-21 | [Demons in the Detail: On Implementing Load Balancing Loss for Training Specialized Mixture-of-Expert Models](https://arxiv.org/abs/2501.11873v2) | 2501.11873v2 | 12 |
| 2025-01-18 | [Mixture of Experts (MoE): A Big Data Perspective](https://arxiv.org/abs/2501.16352v1) | 2501.16352v1 | 6 |
| 2025-01-18 | [FSMoE: A Flexible and Scalable Training System for Sparse Mixture-of-Experts Models](https://arxiv.org/abs/2501.10714v1) | 2501.10714v1 | 6 |
| 2025-01-16 | [LLM-Based Routing in Mixture of Experts: A Novel Framework for Trading](https://arxiv.org/abs/2501.09636v2) | 2501.09636v2 | 12 |
| 2025-01-14 | [GRAPHMOE: Amplifying Cognitive Depth of Mixture-of-Experts Network via Introducing Self-Rethinking Mechanism](https://arxiv.org/abs/2501.07890v4) | 2501.07890v4 | 6 |
| 2025-01-12 | [Transforming Vision Transformer: Towards Efficient Multi-Task Asynchronous Learning](https://arxiv.org/abs/2501.06884v1) | 2501.06884v1 | 6 |
| 2025-01-09 | [Optimizing Distributed Deployment of Mixture-of-Experts Model Inference in Serverless Computing](https://arxiv.org/abs/2501.05313v1) | 2501.05313v1 | 6 |
| 2025-01-07 | [MixNet: A Runtime Reconfigurable Optical-Electrical Fabric for Distributed Mixture-of-Experts Training](https://arxiv.org/abs/2501.03905v4) | 2501.03905v4 | 6 |
| 2025-01-06 | [Mixture-of-Experts Graph Transformers for Interpretable Particle Collision Detection](https://arxiv.org/abs/2501.03432v3) | 2501.03432v3 | 6 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-26 | [Graph Mixture of Experts and Memory-augmented Routers for Multivariate Time Series Anomaly Detection](https://arxiv.org/abs/2412.19108v2) | 2412.19108v2 | 9 |
| 2024-12-23 | [UME: Upcycling Mixture-of-Experts for Scalable and Efficient Automatic Speech Recognition](https://arxiv.org/abs/2412.17507v1) | 2412.17507v1 | 9 |
| 2024-12-22 | [Part-Of-Speech Sensitivity of Routers in Mixture of Experts Models](https://arxiv.org/abs/2412.16971v1) | 2412.16971v1 | 9 |
| 2024-12-20 | [Theory of Mixture-of-Experts for Mobile Edge Computing](https://arxiv.org/abs/2412.15690v2) | 2412.15690v2 | 6 |
| 2024-12-19 | [ReMoE: Fully Differentiable Mixture-of-Experts with ReLU Routing](https://arxiv.org/abs/2412.14711v2) | 2412.14711v2 | 8 |
| 2024-12-18 | [A Survey on Inference Optimization Techniques for Mixture of Experts Models](https://arxiv.org/abs/2412.14219v2) | 2412.14219v2 | 10 |
| 2024-12-18 | [GMoE: Empowering LLMs Fine-Tuning via MoE Graph Collaboration](https://arxiv.org/abs/2412.16216v4) | 2412.16216v4 | 6 |
| 2024-12-17 | [SMOSE: Sparse Mixture of Shallow Experts for Interpretable Reinforcement Learning in Continuous Control Tasks](https://arxiv.org/abs/2412.13053v1) | 2412.13053v1 | 6 |
| 2024-12-17 | [CAMEL: Cross-Attention Enhanced Mixture-of-Experts and Language Bias for Code-Switching Speech Recognition](https://arxiv.org/abs/2412.12760v2) | 2412.12760v2 | 6 |
| 2024-12-16 | [Investigating Mixture of Experts in Dense Retrieval](https://arxiv.org/abs/2412.11864v1) | 2412.11864v1 | 10 |
| 2024-12-16 | [Towards Adversarial Robustness of Model-Level Mixture-of-Experts Architectures for Semantic Segmentation](https://arxiv.org/abs/2412.11608v1) | 2412.11608v1 | 10 |
| 2024-12-14 | [DeMo: Decoupled Feature-Based Mixture of Experts for Multi-Modal Object Re-Identification](https://arxiv.org/abs/2412.10650v1) | 2412.10650v1 | 6 |
| 2024-12-13 | [Mr. DETR++: Instructive Multi-Route Training for Detection Transformers with Mixture-of-Experts](https://arxiv.org/abs/2412.10028v4) | 2412.10028v4 | 8 |
| 2024-12-11 | [Mixture of Experts Meets Decoupled Message Passing: Towards General and Adaptive Node Classification](https://arxiv.org/abs/2412.08193v2) | 2412.08193v2 | 10 |
| 2024-12-10 | [MoE-CAP: Benchmarking Cost, Accuracy and Performance of Sparse Mixture-of-Experts Systems](https://arxiv.org/abs/2412.07067v6) | 2412.07067v6 | 8 |
| 2024-12-09 | [UniPaint: Unified Space-time Video Inpainting via Mixture-of-Experts](https://arxiv.org/abs/2412.06340v2) | 2412.06340v2 | 10 |
| 2024-12-08 | [An Entailment Tree Generation Approach for Multimodal Multi-Hop Question Answering with Mixture-of-Experts and Iterative Feedback Mechanism](https://arxiv.org/abs/2412.05821v2) | 2412.05821v2 | 10 |
| 2024-12-07 | [RSUniVLM: A Unified Vision Language Model for Remote Sensing via Granularity-oriented Mixture of Experts](https://arxiv.org/abs/2412.05679v2) | 2412.05679v2 | 6 |
| 2024-12-07 | [SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts](https://arxiv.org/abs/2412.05552v1) | 2412.05552v1 | 6 |
| 2024-12-07 | [Towards 3D Acceleration for low-power Mixture-of-Experts and Multi-Head Attention Spiking Transformers](https://arxiv.org/abs/2412.05540v1) | 2412.05540v1 | 7 |
| 2024-12-05 | [Meta-Reinforcement Learning With Mixture of Experts for Generalizable Multi Access in Heterogeneous Wireless Networks](https://arxiv.org/abs/2412.03850v1) | 2412.03850v1 | 6 |
| 2024-12-04 | [Convolutional Neural Networks and Mixture of Experts for Intrusion Detection in 5G Networks and beyond](https://arxiv.org/abs/2412.03483v2) | 2412.03483v2 | 8 |
| 2024-12-03 | [VA-MoE: Variables-Adaptive Mixture of Experts for Incremental Weather Forecasting](https://arxiv.org/abs/2412.02503v2) | 2412.02503v2 | 6 |
| 2024-11-30 | [Mixture of Experts for Node Classification](https://arxiv.org/abs/2412.00418v3) | 2412.00418v3 | 6 |
| 2024-11-30 | [HiMoE: Heterogeneity-Informed Mixture-of-Experts for Fair Spatial-Temporal Forecasting](https://arxiv.org/abs/2412.00316v3) | 2412.00316v3 | 6 |
| 2024-11-28 | [On the Role of Discrete Representation in Sparse Mixture of Experts](https://arxiv.org/abs/2411.19402v2) | 2411.19402v2 | 9 |
| 2024-11-27 | [SEUF: Is Unlearning One Expert Enough for Mixture-of-Experts LLMs?](https://arxiv.org/abs/2411.18797v2) | 2411.18797v2 | 8 |
| 2024-11-27 | [Mixture of Experts in Image Classification: What's the Sweet Spot?](https://arxiv.org/abs/2411.18322v2) | 2411.18322v2 | 13 |
| 2024-11-26 | [Condense, Don't Just Prune: Enhancing Efficiency and Performance in MoE Layer Pruning](https://arxiv.org/abs/2412.00069v3) | 2412.00069v3 | 6 |
| 2024-11-25 | [MH-MoE: Multi-Head Mixture-of-Experts](https://arxiv.org/abs/2411.16205v3) | 2411.16205v3 | 10 |
| 2024-11-24 | [LLaMA-MoE v2: Exploring Sparsity of LLaMA from Perspective of Mixture-of-Experts with Post-Training](https://arxiv.org/abs/2411.15708v1) | 2411.15708v1 | 7 |
| 2024-11-20 | [MERLOT: A Distilled LLM-based Mixture-of-Experts Framework for Scalable Encrypted Traffic Classification](https://arxiv.org/abs/2411.13004v1) | 2411.13004v1 | 6 |
| 2024-11-20 | [NumCoKE: Ordinal-Aware Numerical Reasoning over Knowledge Graphs with Mixture-of-Experts and Contrastive Learning](https://arxiv.org/abs/2411.12950v4) | 2411.12950v4 | 6 |
| 2024-11-16 | [Awaker2.5-VL: Stably Scaling MLLMs with Parameter-Efficient Mixture of Experts](https://arxiv.org/abs/2411.10669v1) | 2411.10669v1 | 7 |
| 2024-11-15 | [Pro-Prophet: A Systematic Load Balancing Method for Efficient Parallel Training of Large-scale MoE Models](https://arxiv.org/abs/2411.10003v2) | 2411.10003v2 | 6 |
| 2024-11-12 | [Imitation Learning from Observations: An Autoregressive Mixture of Experts Approach](https://arxiv.org/abs/2411.08232v1) | 2411.08232v1 | 6 |
| 2024-11-11 | [WDMoE: Wireless Distributed Mixture of Experts for Large Language Models](https://arxiv.org/abs/2411.06681v1) | 2411.06681v1 | 6 |
| 2024-11-08 | [NeKo: Cross-Modality Post-Recognition Error Correction with Tasks-Guided Mixture-of-Experts Language Model](https://arxiv.org/abs/2411.05945v2) | 2411.05945v2 | 6 |
| 2024-11-05 | [DA-MoE: Addressing Depth-Sensitivity in Graph-Level Analysis through Mixture of Experts](https://arxiv.org/abs/2411.03025v1) | 2411.03025v1 | 6 |
| 2024-11-04 | [Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent](https://arxiv.org/abs/2411.02265v3) | 2411.02265v3 | 9 |
| 2024-11-04 | [FedMoE-DA: Federated Mixture of Experts via Domain Aware Fine-grained Aggregation](https://arxiv.org/abs/2411.02115v2) | 2411.02115v2 | 6 |
| 2024-11-03 | [RS-MoE: A Vision-Language Model with Mixture of Experts for Remote Sensing Image Captioning and Visual Question Answering](https://arxiv.org/abs/2411.01595v2) | 2411.01595v2 | 8 |
| 2024-11-03 | [Facet-Aware Multi-Head Mixture-of-Experts Model for Sequential Recommendation](https://arxiv.org/abs/2411.01457v2) | 2411.01457v2 | 8 |
| 2024-11-02 | [Hexa-MoE: Efficient and Heterogeneous-aware Training for Mixture-of-Experts](https://arxiv.org/abs/2411.01288v4) | 2411.01288v4 | 6 |
| 2024-11-01 | [MoE-I$^2$: Compressing Mixture of Experts Models through Inter-Expert Pruning and Intra-Expert Low-Rank Decomposition](https://arxiv.org/abs/2411.01016v1) | 2411.01016v1 | 6 |
| 2024-11-01 | [MoNTA: Accelerating Mixture-of-Experts Training with Network-Traffc-Aware Parallel Optimization](https://arxiv.org/abs/2411.00662v1) | 2411.00662v1 | 10 |
| 2024-11-01 | [LIBMoE: A Library for comprehensive benchmarking Mixture of Experts in Large Language Models](https://arxiv.org/abs/2411.00918v5) | 2411.00918v5 | 13 |
| 2024-10-31 | [Stereo-Talker: Audio-driven 3D Human Synthesis with Prior-Guided Mixture-of-Experts](https://arxiv.org/abs/2410.23836v1) | 2410.23836v1 | 6 |
| 2024-10-30 | [Efficient and Interpretable Grammatical Error Correction with Mixture of Experts](https://arxiv.org/abs/2410.23507v1) | 2410.23507v1 | 10 |
| 2024-10-30 | [Stealing User Prompts from Mixture of Experts](https://arxiv.org/abs/2410.22884v1) | 2410.22884v1 | 10 |
| 2024-10-29 | [Efficient and Effective Weight-Ensembling Mixture of Experts for Multi-Task Model Merging](https://arxiv.org/abs/2410.21804v1) | 2410.21804v1 | 10 |
| 2024-10-29 | [Neural Experts: Mixture of Experts for Implicit Neural Representations](https://arxiv.org/abs/2410.21643v1) | 2410.21643v1 | 6 |
| 2024-10-25 | [MoE-Enhanced Explainable Deep Manifold Transformation for Complex Data Embedding and Visualization](https://arxiv.org/abs/2410.19504v3) | 2410.19504v3 | 8 |
| 2024-10-25 | [Hierarchical Mixture of Experts: Generalizable Learning for High-Level Synthesis](https://arxiv.org/abs/2410.19225v4) | 2410.19225v4 | 6 |
| 2024-10-24 | [Read-ME: Refactorizing LLMs as Router-Decoupled Mixture of Experts with System Co-Design](https://arxiv.org/abs/2410.19123v1) | 2410.19123v1 | 13 |
| 2024-10-24 | [MoMQ: Mixture-of-Experts Enhances Multi-Dialect Query Generation across Relational and Non-Relational Databases](https://arxiv.org/abs/2410.18406v1) | 2410.18406v1 | 6 |
| 2024-10-23 | [Robust and Explainable Depression Identification from Speech Using Vowel-Based Ensemble Learning Approaches](https://arxiv.org/abs/2410.18298v1) | 2410.18298v1 | 6 |
| 2024-10-23 | [MiLoRA: Efficient Mixture of Low-Rank Adaptation for Large Language Models Fine-tuning](https://arxiv.org/abs/2410.18035v1) | 2410.18035v1 | 10 |
| 2024-10-23 | [ExpertFlow: Efficient Mixture-of-Experts Inference via Predictive Expert Caching and Token Scheduling](https://arxiv.org/abs/2410.17954v2) | 2410.17954v2 | 6 |
| 2024-10-22 | [Optimizing Mixture-of-Experts Inference Time Combining Model Deployment and Communication Scheduling](https://arxiv.org/abs/2410.17043v1) | 2410.17043v1 | 6 |
| 2024-10-21 | [CartesianMoE: Boosting Knowledge Sharing among Experts via Cartesian Product Routing in Mixture-of-Experts](https://arxiv.org/abs/2410.16077v3) | 2410.16077v3 | 11 |
| 2024-10-21 | [Generalizing Motion Planners with Mixture of Experts for Autonomous Driving](https://arxiv.org/abs/2410.15774v2) | 2410.15774v2 | 14 |
| 2024-10-21 | [ViMoE: An Empirical Study of Designing Vision Mixture-of-Experts](https://arxiv.org/abs/2410.15732v2) | 2410.15732v2 | 10 |
| 2024-10-20 | [LoRA-IR: Taming Low-Rank Experts for Efficient All-in-One Image Restoration](https://arxiv.org/abs/2410.15385v2) | 2410.15385v2 | 6 |
| 2024-10-19 | [MENTOR: Mixture-of-Experts Network with Task-Oriented Perturbation for Visual Reinforcement Learning](https://arxiv.org/abs/2410.14972v3) | 2410.14972v3 | 6 |
| 2024-10-18 | [MomentumSMoE: Integrating Momentum into Sparse Mixture of Experts](https://arxiv.org/abs/2410.14574v1) | 2410.14574v1 | 6 |
| 2024-10-18 | [ST-MoE-BERT: A Spatial-Temporal Mixture-of-Experts Framework for Long-Term Cross-City Mobility Prediction](https://arxiv.org/abs/2410.14099v1) | 2410.14099v1 | 6 |
| 2024-10-17 | [Sparse Mixture-of-Experts for Compositional Generalization: Empirical Evidence and Theoretical Foundations of Optimal Sparsity](https://arxiv.org/abs/2410.13964v2) | 2410.13964v2 | 7 |
| 2024-10-16 | [Understanding Expert Structures on Minimax Parameter Estimation in Contaminated Mixture of Experts](https://arxiv.org/abs/2410.12258v2) | 2410.12258v2 | 6 |
| 2024-10-15 | [MoE-Pruner: Pruning Mixture-of-Experts Large Language Model using the Hints from Its Router](https://arxiv.org/abs/2410.12013v1) | 2410.12013v1 | 9 |
| 2024-10-15 | [GaVaMoE: Gaussian-Variational Gated Mixture of Experts for Explainable Recommendation](https://arxiv.org/abs/2410.11841v2) | 2410.11841v2 | 6 |
| 2024-10-15 | [Quadratic Gating Mixture of Experts: Statistical Insights into Self-Attention](https://arxiv.org/abs/2410.11222v3) | 2410.11222v3 | 7 |
| 2024-10-14 | [Your Mixture-of-Experts LLM Is Secretly an Embedding Model For Free](https://arxiv.org/abs/2410.10814v2) | 2410.10814v2 | 8 |
| 2024-10-14 | [Moirai-MoE: Empowering Time Series Foundation Models with Sparse Mixture of Experts](https://arxiv.org/abs/2410.10469v1) | 2410.10469v1 | 6 |
| 2024-10-14 | [Ada-K Routing: Boosting the Efficiency of MoE-based LLMs](https://arxiv.org/abs/2410.10456v2) | 2410.10456v2 | 7 |
| 2024-10-14 | [Mixture of Experts Made Personalized: Federated Prompt Learning for Vision-Language Models](https://arxiv.org/abs/2410.10114v4) | 2410.10114v4 | 6 |
| 2024-10-13 | [ContextWIN: Whittle Index Based Mixture-of-Experts Neural Model For Restless Bandits Via Deep RL](https://arxiv.org/abs/2410.09781v1) | 2410.09781v1 | 10 |
| 2024-10-12 | [AT-MoE: Adaptive Task-planning Mixture of Experts via LoRA Approach](https://arxiv.org/abs/2410.10896v2) | 2410.10896v2 | 6 |
| 2024-10-11 | [Semi-Supervised Learning of Noisy Mixture of Experts Models](https://arxiv.org/abs/2410.09039v1) | 2410.09039v1 | 6 |
| 2024-10-11 | [Retraining-Free Merging of Sparse MoE via Hierarchical Clustering](https://arxiv.org/abs/2410.08589v4) | 2410.08589v4 | 8 |
| 2024-10-10 | [Flex-MoE: Modeling Arbitrary Modality Combination via the Flexible Mixture-of-Experts](https://arxiv.org/abs/2410.08245v2) | 2410.08245v2 | 8 |
| 2024-10-10 | [Upcycling Large Language Models into Mixture of Experts](https://arxiv.org/abs/2410.07524v2) | 2410.07524v2 | 15 |
| 2024-10-09 | [MoE++: Accelerating Mixture-of-Experts Methods with Zero-Computation Experts](https://arxiv.org/abs/2410.07348v1) | 2410.07348v1 | 8 |
| 2024-10-08 | [Mixture Compressor for Mixture-of-Experts LLMs Gains More](https://arxiv.org/abs/2410.06270v2) | 2410.06270v2 | 6 |
| 2024-10-08 | [Aria: An Open Multimodal Native Mixture-of-Experts Model](https://arxiv.org/abs/2410.05993v4) | 2410.05993v4 | 6 |
| 2024-10-04 | [A Dynamic Approach to Stock Price Prediction: Comparing RNN and Mixture of Experts Models Across Different Volatility Profiles](https://arxiv.org/abs/2410.07234v1) | 2410.07234v1 | 6 |
| 2024-10-03 | [On Expert Estimation in Hierarchical Mixture of Experts: Beyond Softmax Gating Functions](https://arxiv.org/abs/2410.02935v2) | 2410.02935v2 | 6 |
| 2024-10-03 | [Efficient Residual Learning with Mixture-of-Experts for Universal Dexterous Grasping](https://arxiv.org/abs/2410.02475v1) | 2410.02475v1 | 6 |
| 2024-10-03 | [MIGA: Mixture-of-Experts with Group Aggregation for Stock Market Prediction](https://arxiv.org/abs/2410.02241v1) | 2410.02241v1 | 10 |
| 2024-10-03 | [Searching for Efficient Linear Layers over a Continuous Space of Structured Matrices](https://arxiv.org/abs/2410.02117v2) | 2410.02117v2 | 7 |
| 2024-10-02 | [Upcycling Instruction Tuning from Dense to Mixture-of-Experts via Parameter Merging](https://arxiv.org/abs/2410.01610v1) | 2410.01610v1 | 9 |
| 2024-10-01 | [UniAdapt: A Universal Adapter for Knowledge Calibration](https://arxiv.org/abs/2410.00454v1) | 2410.00454v1 | 6 |
| 2024-09-27 | [SciDFM: A Large Language Model with Mixture-of-Experts for Science](https://arxiv.org/abs/2409.18412v3) | 2409.18412v3 | 6 |
| 2024-09-26 | [Uni-Med: A Unified Medical Generalist Foundation Model For Multi-Task Learning Via Connector-MoE](https://arxiv.org/abs/2409.17508v2) | 2409.17508v2 | 6 |
| 2024-09-26 | [A Time Series is Worth Five Experts: Heterogeneous Mixture of Experts for Traffic Flow Prediction](https://arxiv.org/abs/2409.17440v1) | 2409.17440v1 | 6 |
| 2024-09-24 | [Leveraging Mixture of Experts for Improved Speech Deepfake Detection](https://arxiv.org/abs/2409.16077v1) | 2409.16077v1 | 6 |
| 2024-09-24 | [Time-MoE: Billion-Scale Time Series Foundation Models with Mixture of Experts](https://arxiv.org/abs/2409.16040v4) | 2409.16040v4 | 11 |
| 2024-09-24 | [Boosting Code-Switching ASR with Mixture of Experts Enhanced Speech-Conditioned LLM](https://arxiv.org/abs/2409.15905v2) | 2409.15905v2 | 6 |
| 2024-09-24 | [Toward Mixture-of-Experts Enabled Trustworthy Semantic Communication for 6G Networks](https://arxiv.org/abs/2409.15695v1) | 2409.15695v1 | 6 |
| 2024-09-21 | [Routing in Sparsely-gated Language Models responds to Context](https://arxiv.org/abs/2409.14107v1) | 2409.14107v1 | 6 |
| 2024-09-20 | [On-Device Collaborative Language Modeling via a Mixture of Generalists and Specialists](https://arxiv.org/abs/2409.13931v4) | 2409.13931v4 | 6 |
| 2024-09-19 | [Robust Audiovisual Speech Recognition Models with Mixture-of-Experts](https://arxiv.org/abs/2409.12370v1) | 2409.12370v1 | 6 |
| 2024-09-18 | [GRIN: GRadient-INformed MoE](https://arxiv.org/abs/2409.12136v1) | 2409.12136v1 | 9 |
| 2024-09-18 | [Mixture of Experts Fusion for Fake Audio Detection Using Frozen wav2vec 2.0](https://arxiv.org/abs/2409.11909v1) | 2409.11909v1 | 6 |
| 2024-09-16 | [Adaptive Segmentation-Based Initialization for Steered Mixture of Experts Image Regression](https://arxiv.org/abs/2409.10101v1) | 2409.10101v1 | 6 |
| 2024-09-10 | [DA-MoE: Towards Dynamic Expert Allocation for Mixture-of-Experts Models](https://arxiv.org/abs/2409.06669v1) | 2409.06669v1 | 8 |
| 2024-09-05 | [Interpretable mixture of experts for time series prediction under recurrent and non-recurrent conditions](https://arxiv.org/abs/2409.03282v1) | 2409.03282v1 | 6 |
| 2024-09-03 | [OLMoE: Open Mixture-of-Experts Language Models](https://arxiv.org/abs/2409.02060v2) | 2409.02060v2 | 6 |
| 2024-09-03 | [Enhancing Code-Switching Speech Recognition with LID-Based Collaborative Mixture of Experts Model](https://arxiv.org/abs/2409.02050v2) | 2409.02050v2 | 6 |
| 2024-09-02 | [Duplex: A Device for Large Language Models with Mixture of Experts, Grouped Query Attention, and Continuous Batching](https://arxiv.org/abs/2409.01141v1) | 2409.01141v1 | 6 |
| 2024-09-02 | [Beyond Parameter Count: Implicit Bias in Soft Mixture of Experts](https://arxiv.org/abs/2409.00879v1) | 2409.00879v1 | 6 |
| 2024-08-28 | [Nexus: Specialization meets Adaptability for Efficiently Training Mixture of Experts](https://arxiv.org/abs/2408.15901v1) | 2408.15901v1 | 6 |
| 2024-08-28 | [Auxiliary-Loss-Free Load Balancing Strategy for Mixture-of-Experts](https://arxiv.org/abs/2408.15664v1) | 2408.15664v1 | 14 |
| 2024-08-21 | [MoE-LPR: Multilingual Extension of Large Language Models through Mixture-of-Experts with Language Priors Routing](https://arxiv.org/abs/2408.11396v1) | 2408.11396v1 | 6 |
| 2024-08-21 | [FedMoE: Personalized Federated Learning via Heterogeneous Mixture of Experts](https://arxiv.org/abs/2408.11304v1) | 2408.11304v1 | 12 |
| 2024-08-20 | [AnyGraph: Graph Foundation Model in the Wild](https://arxiv.org/abs/2408.10700v1) | 2408.10700v1 | 9 |
| 2024-08-20 | [HMoE: Heterogeneous Mixture of Experts for Language Modeling](https://arxiv.org/abs/2408.10681v1) | 2408.10681v1 | 6 |
| 2024-08-15 | [BAM! Just Like That: Simple and Efficient Parameter Upcycling for Mixture of Experts](https://arxiv.org/abs/2408.08274v2) | 2408.08274v2 | 8 |
| 2024-08-15 | [FactorLLM: Factorizing Knowledge via Mixture of Experts for Large Language Models](https://arxiv.org/abs/2408.11855v1) | 2408.11855v1 | 14 |
| 2024-08-13 | [A Survey on Model MoErging: Recycling and Routing Among Specialized Experts for Collaborative Learning](https://arxiv.org/abs/2408.07057v2) | 2408.07057v2 | 6 |
| 2024-08-13 | [Layerwise Recurrent Router for Mixture-of-Experts](https://arxiv.org/abs/2408.06793v2) | 2408.06793v2 | 10 |
| 2024-08-08 | [MoC-System: Efficient Fault Tolerance for Sparse Mixture-of-Experts Model Training](https://arxiv.org/abs/2408.04307v3) | 2408.04307v3 | 6 |
| 2024-08-08 | [LaDiMo: Layer-wise Distillation Inspired MoEfier](https://arxiv.org/abs/2408.04278v1) | 2408.04278v1 | 6 |
| 2024-07-31 | [MoMa: Efficient Early-Fusion Pre-training with Mixture of Modality-Aware Experts](https://arxiv.org/abs/2407.21770v3) | 2407.21770v3 | 6 |
| 2024-07-31 | [PMoE: Progressive Mixture of Experts with Asymmetric Transformer for Continual Learning](https://arxiv.org/abs/2407.21571v1) | 2407.21571v1 | 8 |
| 2024-07-28 | [Mixture of Modular Experts: Distilling Knowledge from a Multilingual Teacher into Specialized Modular Language Models](https://arxiv.org/abs/2407.19610v1) | 2407.19610v1 | 6 |
| 2024-07-26 | [Dynamic Language Group-Based MoE: Enhancing Code-Switching Speech Recognition with Hierarchical Routing](https://arxiv.org/abs/2407.18581v4) | 2407.18581v4 | 11 |
| 2024-07-25 | [How Lightweight Can A Vision Transformer Be](https://arxiv.org/abs/2407.17783v1) | 2407.17783v1 | 7 |
| 2024-07-24 | [Exploring Domain Robust Lightweight Reward Models based on Router Mechanism](https://arxiv.org/abs/2407.17546v1) | 2407.17546v1 | 7 |
| 2024-07-24 | [M4: Multi-Proxy Multi-Gate Mixture of Experts Network for Multiple Instance Learning in Histopathology Image Analysis](https://arxiv.org/abs/2407.17267v1) | 2407.17267v1 | 10 |
| 2024-07-19 | [Mixture of Experts with Mixture of Precisions for Tuning Quality of Service](https://arxiv.org/abs/2407.14417v2) | 2407.14417v2 | 10 |
| 2024-07-18 | [Mixture of Experts based Multi-task Supervise Learning from Crowds](https://arxiv.org/abs/2407.13268v2) | 2407.13268v2 | 6 |
| 2024-07-15 | [Boost Your NeRF: A Model-Agnostic Mixture of Experts Framework for High Quality and Efficient Rendering](https://arxiv.org/abs/2407.10389v3) | 2407.10389v3 | 6 |
| 2024-07-13 | [MaskMoE: Boosting Token-Level Learning via Routing Mask in Mixture-of-Experts](https://arxiv.org/abs/2407.09816v4) | 2407.09816v4 | 9 |
| 2024-07-12 | [Diversifying the Expert Knowledge for Task-Agnostic Pruning in Sparse Mixture-of-Experts](https://arxiv.org/abs/2407.09590v4) | 2407.09590v4 | 6 |
| 2024-07-09 | [A Simple Architecture for Enterprise Large Language Model Applications based on Role based security and Clearance Levels using Retrieval-Augmented Generation or Mixture of Experts](https://arxiv.org/abs/2407.06718v1) | 2407.06718v1 | 6 |
| 2024-07-05 | [Lazarus: Resilient and Elastic Training of Mixture-of-Experts Models](https://arxiv.org/abs/2407.04656v2) | 2407.04656v2 | 6 |
| 2024-07-01 | [Efficient Expert Pruning for Sparse Mixture-of-Experts Language Models: Enhancing Performance and Reducing Inference Costs](https://arxiv.org/abs/2407.00945v1) | 2407.00945v1 | 6 |
| 2024-06-28 | [LEMoE: Advanced Mixture of Experts Adaptor for Lifelong Model Editing of Large Language Models](https://arxiv.org/abs/2406.20030v1) | 2406.20030v1 | 6 |
| 2024-06-28 | [Solving Token Gradient Conflict in Mixture-of-Experts for Large Vision-Language Model](https://arxiv.org/abs/2406.19905v3) | 2406.19905v3 | 9 |
| 2024-06-26 | [A Survey on Mixture of Experts in Large Language Models](https://arxiv.org/abs/2407.06204v3) | 2407.06204v3 | 11 |
| 2024-06-26 | [Mixture of Experts in a Mixture of RL settings](https://arxiv.org/abs/2406.18420v1) | 2406.18420v1 | 6 |
| 2024-06-26 | [A Closer Look into Mixture-of-Experts in Large Language Models](https://arxiv.org/abs/2406.18219v3) | 2406.18219v3 | 8 |
| 2024-06-25 | [A New Benchmark Dataset and Mixture-of-Experts Language Models for Adversarial Natural Language Inference in Vietnamese](https://arxiv.org/abs/2406.17716v3) | 2406.17716v3 | 6 |
| 2024-06-25 | [MoESD: Mixture of Experts Stable Diffusion to Mitigate Gender Bias](https://arxiv.org/abs/2407.11002v2) | 2407.11002v2 | 10 |
| 2024-06-24 | [Peirce in the Machine: How Mixture of Experts Models Perform Hypothesis Construction](https://arxiv.org/abs/2406.17150v1) | 2406.17150v1 | 6 |
| 2024-06-24 | [LLaMA-MoE: Building Mixture-of-Experts from LLaMA with Continual Pre-training](https://arxiv.org/abs/2406.16554v1) | 2406.16554v1 | 9 |
| 2024-06-24 | [Theory on Mixture-of-Experts in Continual Learning](https://arxiv.org/abs/2406.16437v3) | 2406.16437v3 | 8 |
| 2024-06-19 | [Low-Rank Mixture-of-Experts for Continual Medical Image Segmentation](https://arxiv.org/abs/2406.13583v1) | 2406.13583v1 | 10 |
| 2024-06-19 | [AdaMoE: Token-Adaptive Routing with Null Experts for Mixture-of-Experts Language Models](https://arxiv.org/abs/2406.13233v2) | 2406.13233v2 | 12 |
| 2024-06-18 | [Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts](https://arxiv.org/abs/2406.12845v1) | 2406.12845v1 | 6 |
| 2024-06-18 | [Variational Distillation of Diffusion Policies into Mixture of Experts](https://arxiv.org/abs/2406.12538v2) | 2406.12538v2 | 6 |
| 2024-06-18 | [GW-MoE: Resolving Uncertainty in MoE Router with Global Workspace Theory](https://arxiv.org/abs/2406.12375v1) | 2406.12375v1 | 7 |
| 2024-06-17 | [Not Eliminate but Aggregate: Post-Hoc Control over Mixture-of-Experts to Address Shortcut Shifts in Natural Language Understanding](https://arxiv.org/abs/2406.12060v3) | 2406.12060v3 | 6 |
| 2024-06-17 | [$\texttt{MoE-RBench}$: Towards Building Reliable Language Models with Sparse Mixture-of-Experts](https://arxiv.org/abs/2406.11353v1) | 2406.11353v1 | 7 |
| 2024-06-17 | [Dynamic Data Mixing Maximizes Instruction Tuning for Mixture-of-Experts](https://arxiv.org/abs/2406.11256v1) | 2406.11256v1 | 6 |
| 2024-06-17 | [Graph Knowledge Distillation to Mixture of Experts](https://arxiv.org/abs/2406.11919v2) | 2406.11919v2 | 10 |
| 2024-06-14 | [Interpretable Cascading Mixture-of-Experts for Urban Traffic Congestion Prediction](https://arxiv.org/abs/2406.12923v1) | 2406.12923v1 | 6 |
| 2024-06-14 | [Towards Efficient Pareto Set Approximation via Mixture of Experts Based Model Fusion](https://arxiv.org/abs/2406.09770v2) | 2406.09770v2 | 8 |
| 2024-06-13 | [DeepUnifiedMom: Unified Time-series Momentum Portfolio Construction via Multi-Task Learning with Multi-Gate Mixture of Experts](https://arxiv.org/abs/2406.08742v1) | 2406.08742v1 | 6 |
| 2024-06-12 | [QuantMoE-Bench: Examining Post-Training Quantization for Mixture-of-Experts](https://arxiv.org/abs/2406.08155v2) | 2406.08155v2 | 6 |
| 2024-06-10 | [Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters](https://arxiv.org/abs/2406.05955v2) | 2406.05955v2 | 8 |
| 2024-06-07 | [MEFT: Memory-Efficient Fine-Tuning through Sparse Adapter](https://arxiv.org/abs/2406.04984v1) | 2406.04984v1 | 6 |
| 2024-06-07 | [MoE Jetpack: From Dense Checkpoints to Adaptive Mixture of Experts for Vision Tasks](https://arxiv.org/abs/2406.04801v1) | 2406.04801v1 | 6 |
| 2024-06-05 | [Style Mixture of Experts for Expressive Text-To-Speech Synthesis](https://arxiv.org/abs/2406.03637v2) | 2406.03637v2 | 6 |
| 2024-06-05 | [Node-wise Filtering in Graph Neural Networks: A Mixture of Experts Approach](https://arxiv.org/abs/2406.03464v1) | 2406.03464v1 | 6 |
| 2024-06-05 | [Continual Traffic Forecasting via Mixture of Experts](https://arxiv.org/abs/2406.03140v1) | 2406.03140v1 | 6 |
| 2024-06-04 | [Towards Efficient Mixture of Experts: A Holistic Study of Compression Techniques](https://arxiv.org/abs/2406.02500v3) | 2406.02500v3 | 7 |
| 2024-06-03 | [Skywork-MoE: A Deep Dive into Training Techniques for Mixture-of-Experts Language Models](https://arxiv.org/abs/2406.06563v1) | 2406.06563v1 | 6 |
| 2024-06-02 | [Reservoir History Matching of the Norne field with generative exotic priors and a coupled Mixture of Experts -- Physics Informed Neural Operator Forward Model](https://arxiv.org/abs/2406.00889v1) | 2406.00889v1 | 6 |
| 2024-05-29 | [MEMoE: Enhancing Model Editing with Mixture of Experts Adaptors](https://arxiv.org/abs/2405.19086v2) | 2405.19086v2 | 6 |
| 2024-05-29 | [MEGO: Learning Mixture-of-Experts for General-Purpose Binary Optimization](https://arxiv.org/abs/2405.18884v2) | 2405.18884v2 | 6 |
| 2024-05-28 | [Yuan 2.0-M32: Mixture of Experts with Attention Router](https://arxiv.org/abs/2405.17976v2) | 2405.17976v2 | 13 |
| 2024-05-27 | [Enhancing Fast Feed Forward Networks with Load Balancing and a Master Leaf Node](https://arxiv.org/abs/2405.16836v1) | 2405.16836v1 | 10 |
| 2024-05-26 | [A Provably Effective Method for Pruning Experts in Fine-tuned Sparse Mixture-of-Experts](https://arxiv.org/abs/2405.16646v3) | 2405.16646v3 | 12 |
| 2024-05-25 | [MoEUT: Mixture-of-Experts Universal Transformers](https://arxiv.org/abs/2405.16039v2) | 2405.16039v2 | 7 |
| 2024-05-24 | [Wasserstein Distances, Neuronal Entanglement, and Sparsity](https://arxiv.org/abs/2405.15756v4) | 2405.15756v4 | 8 |
| 2024-05-24 | [Expert-Token Resonance MoE: Bidirectional Routing with Efficiency Affinity-Driven Active Selection](https://arxiv.org/abs/2406.00023v4) | 2406.00023v4 | 9 |
| 2024-05-23 | [Dynamic Mixture of Experts: An Auto-Tuning Approach for Efficient Transformer Models](https://arxiv.org/abs/2405.14297v4) | 2405.14297v4 | 6 |
| 2024-05-23 | [Statistical Advantages of Perturbing Cosine Router in Mixture of Experts](https://arxiv.org/abs/2405.14131v3) | 2405.14131v3 | 9 |
| 2024-05-23 | [Mixture of Experts Meets Prompt-Based Continual Learning](https://arxiv.org/abs/2405.14124v4) | 2405.14124v4 | 6 |
| 2024-05-22 | [Sigmoid Gating is More Sample Efficient than Softmax Gating in Mixture of Experts](https://arxiv.org/abs/2405.13997v3) | 2405.13997v3 | 8 |
| 2024-05-21 | [Optimizing Generative AI Networking: A Dual Perspective with Multi-Agent Systems and Mixture of Experts](https://arxiv.org/abs/2405.12472v1) | 2405.12472v1 | 6 |
| 2024-05-20 | [Ensemble and Mixture-of-Experts DeepONets For Operator Learning](https://arxiv.org/abs/2405.11907v5) | 2405.11907v5 | 6 |
| 2024-05-19 | [Learning More Generalized Experts by Merging Experts in Mixture-of-Experts](https://arxiv.org/abs/2405.11530v1) | 2405.11530v1 | 8 |
| 2024-05-18 | [Uni-MoE: Scaling Unified Multimodal LLMs with Mixture of Experts](https://arxiv.org/abs/2405.11273v1) | 2405.11273v1 | 7 |
| 2024-05-16 | [Many Hands Make Light Work: Task-Oriented Dialogue System with Module-Based Mixture-of-Experts](https://arxiv.org/abs/2405.09744v1) | 2405.09744v1 | 7 |
| 2024-05-15 | [M$^4$oE: A Foundation Model for Medical Multimodal Image Segmentation with Mixture of Experts](https://arxiv.org/abs/2405.09446v1) | 2405.09446v1 | 6 |
| 2024-05-15 | [A Mixture of Experts (MoE) model to improve AI-based computational pathology prediction performance under variable levels of histopathology image blur](https://arxiv.org/abs/2405.09298v5) | 2405.09298v5 | 6 |
| 2024-05-09 | [A Mixture of Experts Approach to 3D Human Motion Prediction](https://arxiv.org/abs/2405.06088v1) | 2405.06088v1 | 6 |
| 2024-05-09 | [A Mixture-of-Experts Approach to Few-Shot Task Transfer in Open-Ended Text Worlds](https://arxiv.org/abs/2405.06059v1) | 2405.06059v1 | 6 |
| 2024-05-09 | [CuMo: Scaling Multimodal LLM with Co-Upcycled Mixture-of-Experts](https://arxiv.org/abs/2405.05949v1) | 2405.05949v1 | 7 |
| 2024-05-09 | [EWMoE: An effective model for global weather forecasting with mixture-of-experts](https://arxiv.org/abs/2405.06004v2) | 2405.06004v2 | 6 |
| 2024-05-07 | [Enhancing Physical Layer Communication Security through Generative AI with Mixture of Experts](https://arxiv.org/abs/2405.04198v1) | 2405.04198v1 | 6 |
| 2024-05-06 | [MEET: Mixture of Experts Extra Tree-Based sEMG Hand Gesture Identification](https://arxiv.org/abs/2405.09562v1) | 2405.09562v1 | 6 |
| 2024-05-06 | [Lory: Fully Differentiable Mixture-of-Experts for Autoregressive Language Model Pre-training](https://arxiv.org/abs/2405.03133v2) | 2405.03133v2 | 9 |
| 2024-05-06 | [WDMoE: Wireless Distributed Large Language Models with Mixture of Experts](https://arxiv.org/abs/2405.03131v1) | 2405.03131v1 | 6 |
| 2024-05-02 | [MVMoE: Multi-Task Vehicle Routing Solver with Mixture-of-Experts](https://arxiv.org/abs/2405.01029v2) | 2405.01029v2 | 6 |
| 2024-04-30 | [Lancet: Accelerating Mixture-of-Experts Training via Whole Graph Computation-Communication Overlapping](https://arxiv.org/abs/2404.19429v1) | 2404.19429v1 | 6 |
| 2024-04-29 | [Swin2-MoSE: A New Single Image Super-Resolution Model for Remote Sensing](https://arxiv.org/abs/2404.18924v2) | 2404.18924v2 | 7 |
| 2024-04-25 | [U2++ MoE: Scaling 4.7x parameters with minimal impact on RTF](https://arxiv.org/abs/2404.16407v2) | 2404.16407v2 | 11 |
| 2024-04-25 | [Integration of Mixture of Experts and Multimodal Generative AI in Internet of Vehicles: A Survey](https://arxiv.org/abs/2404.16356v1) | 2404.16356v1 | 6 |
| 2024-04-23 | [XFT: Unlocking the Power of Code Instruction Tuning by Simply Merging Upcycled Mixture-of-Experts](https://arxiv.org/abs/2404.15247v2) | 2404.15247v2 | 6 |
| 2024-04-23 | [Multi-Head Mixture-of-Experts](https://arxiv.org/abs/2404.15045v1) | 2404.15045v1 | 6 |
| 2024-04-22 | [MixLoRA: Enhancing Large Language Models Fine-Tuning with LoRA-based Mixture of Experts](https://arxiv.org/abs/2404.15159v3) | 2404.15159v3 | 10 |
| 2024-04-16 | [Med-MoE: Mixture of Domain-Specific Experts for Lightweight Medical Vision-Language Models](https://arxiv.org/abs/2404.10237v3) | 2404.10237v3 | 6 |
| 2024-04-14 | [Generative AI Agents with Large Language Model for Satellite Networks via a Mixture of Experts Transmission](https://arxiv.org/abs/2404.09134v2) | 2404.09134v2 | 6 |
| 2024-04-13 | [T-REX: Mixture-of-Rank-One-Experts with Semantic-aware Intuition for Multi-task Large Language Model Finetuning](https://arxiv.org/abs/2404.08985v2) | 2404.08985v2 | 7 |
| 2024-04-12 | [MoE-FFD: Mixture of Experts for Generalized and Parameter-Efficient Face Forgery Detection](https://arxiv.org/abs/2404.08452v3) | 2404.08452v3 | 10 |
| 2024-04-08 | [Dense Training, Sparse Inference: Rethinking Training of Mixture-of-Experts Language Models](https://arxiv.org/abs/2404.05567v1) | 2404.05567v1 | 6 |
| 2024-04-07 | [SEER-MoE: Sparse Expert Efficiency through Regularization for Mixture-of-Experts](https://arxiv.org/abs/2404.05089v1) | 2404.05089v1 | 12 |
| 2024-04-07 | [Shortcut-connected Expert Parallelism for Accelerating Mixture-of-Experts](https://arxiv.org/abs/2404.05019v3) | 2404.05019v3 | 6 |
| 2024-04-04 | [Fusion of Mixture of Experts and Generative Artificial Intelligence in Mobile Edge Metaverse](https://arxiv.org/abs/2404.03321v1) | 2404.03321v1 | 6 |
| 2024-03-29 | [Revolutionizing Disease Diagnosis with simultaneous functional PET/MR and Deeply Integrated Brain Metabolic, Hemodynamic, and Perfusion Networks](https://arxiv.org/abs/2403.20058v3) | 2403.20058v3 | 8 |
| 2024-03-26 | [Generalization Error Analysis for Sparse Mixture-of-Experts: A Preliminary Study](https://arxiv.org/abs/2403.17404v1) | 2403.17404v1 | 8 |
| 2024-03-20 | [DESIRE-ME: Domain-Enhanced Supervised Information REtrieval using Mixture-of-Experts](https://arxiv.org/abs/2403.13468v1) | 2403.13468v1 | 6 |
| 2024-03-20 | [GeRM: A Generalist Robotic Model with Mixture-of-experts for Quadruped Robot](https://arxiv.org/abs/2403.13358v2) | 2403.13358v2 | 6 |
| 2024-03-18 | [Boosting Continual Learning of Vision-Language Models via Mixture-of-Experts Adapters](https://arxiv.org/abs/2403.11549v2) | 2403.11549v2 | 6 |
| 2024-03-14 | [Switch Diffusion Transformer: Synergizing Denoising Tasks with Sparse Mixture-of-Experts](https://arxiv.org/abs/2403.09176v2) | 2403.09176v2 | 6 |
| 2024-03-13 | [Unleashing the Power of Meta-tuning for Few-shot Generalization Through Sparse Interpolated Experts](https://arxiv.org/abs/2403.08477v3) | 2403.08477v3 | 8 |
| 2024-03-13 | [Scattered Mixture-of-Experts Implementation](https://arxiv.org/abs/2403.08245v2) | 2403.08245v2 | 6 |
| 2024-03-12 | [Branch-Train-MiX: Mixing Expert LLMs into a Mixture-of-Experts LLM](https://arxiv.org/abs/2403.07816v1) | 2403.07816v1 | 6 |
| 2024-03-12 | [Harder Tasks Need More Experts: Dynamic Routing in MoE Models](https://arxiv.org/abs/2403.07652v1) | 2403.07652v1 | 6 |
| 2024-03-11 | [Acquiring Diverse Skills using Curriculum Reinforcement Learning with Mixture of Experts](https://arxiv.org/abs/2403.06966v2) | 2403.06966v2 | 6 |
| 2024-03-08 | [MMoE: Robust Spoiler Detection with Multi-modal Information and Domain-aware Mixture-of-Experts](https://arxiv.org/abs/2403.05265v3) | 2403.05265v3 | 6 |
| 2024-03-06 | [Video Relationship Detection Using Mixture of Experts](https://arxiv.org/abs/2403.03994v1) | 2403.03994v1 | 10 |
| 2024-03-05 | [TESTAM: A Time-Enhanced Spatio-Temporal Attention Model with Mixture of Experts](https://arxiv.org/abs/2403.02600v1) | 2403.02600v1 | 10 |
| 2024-03-04 | [Improving the Downstream Performance of Mixture-of-Experts Transformers via Weak Vanilla Transformers](https://arxiv.org/abs/2403.01994v2) | 2403.01994v2 | 10 |
| 2024-03-02 | [DMoERM: Recipes of Mixture-of-Experts for Effective Reward Modeling](https://arxiv.org/abs/2403.01197v2) | 2403.01197v2 | 7 |
| 2024-02-29 | [Enhancing the "Immunity" of Mixture-of-Experts Networks for Adversarial Defense](https://arxiv.org/abs/2402.18787v1) | 2402.18787v1 | 6 |
| 2024-02-27 | [XMoE: Sparse Models with Fine-grained and Adaptive Expert Selection](https://arxiv.org/abs/2403.18926v2) | 2403.18926v2 | 8 |
| 2024-02-27 | [An Effective Mixture-Of-Experts Approach For Code-Switching Speech Recognition Leveraging Encoder Disentanglement](https://arxiv.org/abs/2402.17189v1) | 2402.17189v1 | 6 |
| 2024-02-23 | [Co-Supervised Learning: Improving Weak-to-Strong Generalization with Hierarchical Mixture of Experts](https://arxiv.org/abs/2402.15505v1) | 2402.15505v1 | 6 |
| 2024-02-23 | [PEMT: Multi-Task Correlation Guided Mixture-of-Experts Enables Parameter-Efficient Transfer Learning](https://arxiv.org/abs/2402.15082v2) | 2402.15082v2 | 6 |
| 2024-02-22 | [Not All Experts are Equal: Efficient Expert Pruning and Skipping for Mixture-of-Experts Large Language Models](https://arxiv.org/abs/2402.14800v2) | 2402.14800v2 | 6 |
| 2024-02-20 | [Scaling physics-informed hard constraints with mixture-of-experts](https://arxiv.org/abs/2402.13412v1) | 2402.13412v1 | 7 |
| 2024-02-20 | [BiMediX: Bilingual Medical Mixture of Experts LLM](https://arxiv.org/abs/2402.13253v2) | 2402.13253v2 | 6 |
| 2024-02-20 | [Towards an empirical understanding of MoE design choices](https://arxiv.org/abs/2402.13089v1) | 2402.13089v1 | 6 |
| 2024-02-20 | [MoELoRA: Contrastive Learning Guided Mixture of Experts on Parameter-Efficient Fine-Tuning for Large Language Models](https://arxiv.org/abs/2402.12851v1) | 2402.12851v1 | 6 |
| 2024-02-20 | [Denoising OCT Images Using Steered Mixture of Experts with Multi-Model Inference](https://arxiv.org/abs/2402.12735v2) | 2402.12735v2 | 6 |
| 2024-02-20 | [HyperMoE: Towards Better Mixture of Experts via Transferring Among Experts](https://arxiv.org/abs/2402.12656v4) | 2402.12656v4 | 6 |
| 2024-02-19 | [Multilinear Mixture of Experts: Scalable Expert Specialization through Factorization](https://arxiv.org/abs/2402.12550v4) | 2402.12550v4 | 11 |
| 2024-02-19 | [Unraveling Complex Data Diversity in Underwater Acoustic Target Recognition through Convolution-based Mixture of Experts](https://arxiv.org/abs/2402.11919v2) | 2402.11919v2 | 6 |
| 2024-02-17 | [Turn Waste into Worth: Rectifying Top-$k$ Router of MoE](https://arxiv.org/abs/2402.12399v2) | 2402.12399v2 | 7 |
| 2024-02-15 | [Mixture of Experts for Network Optimization: A Large Language Model-enabled Approach](https://arxiv.org/abs/2402.09756v1) | 2402.09756v1 | 6 |
| 2024-02-13 | [AMEND: A Mixture of Experts Framework for Long-tailed Trajectory Prediction](https://arxiv.org/abs/2402.08698v2) | 2402.08698v2 | 8 |
| 2024-02-12 | [Scaling Laws for Fine-Grained Mixture of Experts](https://arxiv.org/abs/2402.07871v1) | 2402.07871v1 | 9 |
| 2024-02-11 | [Differentially Private Training of Mixture of Experts Models](https://arxiv.org/abs/2402.07334v1) | 2402.07334v1 | 6 |
| 2024-02-10 | [Fiddler: CPU-GPU Orchestration for Fast Inference of Mixture-of-Experts Models](https://arxiv.org/abs/2402.07033v3) | 2402.07033v3 | 6 |
| 2024-02-10 | [Toward Scalable Generative AI via Mixture of Experts in Mobile Edge Networks](https://arxiv.org/abs/2402.06942v1) | 2402.06942v1 | 6 |
| 2024-02-08 | [Buffer Overflow in Mixture of Experts](https://arxiv.org/abs/2402.05526v1) | 2402.05526v1 | 11 |
| 2024-02-07 | [On Parameter Estimation in Deviated Gaussian Mixture of Experts](https://arxiv.org/abs/2402.05220v2) | 2402.05220v2 | 6 |
| 2024-02-05 | [Approximation Rates and VC-Dimension Bounds for (P)ReLU MLP Mixture of Experts](https://arxiv.org/abs/2402.03460v2) | 2402.03460v2 | 10 |
| 2024-02-05 | [FuseMoE: Mixture-of-Experts Transformers for Fleximodal Fusion](https://arxiv.org/abs/2402.03226v4) | 2402.03226v4 | 6 |
| 2024-02-05 | [On Least Square Estimation in Softmax Gating Mixture of Experts](https://arxiv.org/abs/2402.02952v2) | 2402.02952v2 | 8 |
| 2024-02-05 | [Intrinsic User-Centric Interpretability through Global Mixture of Experts](https://arxiv.org/abs/2402.02933v4) | 2402.02933v4 | 10 |
| 2024-02-04 | [CompeteSMoE -- Effective Training of Sparse Mixture of Experts via Competition](https://arxiv.org/abs/2402.02526v1) | 2402.02526v1 | 8 |
| 2024-02-02 | [pFedMoE: Data-Level Personalization with Mixture of Experts for Model-Heterogeneous Personalized Federated Learning](https://arxiv.org/abs/2402.01350v3) | 2402.01350v3 | 6 |
| 2024-02-01 | [Merging Multi-Task Models via Weight-Ensembling Mixture of Experts](https://arxiv.org/abs/2402.00433v2) | 2402.00433v2 | 7 |
| 2024-01-31 | [MoDE: A Mixture-of-Experts Model with Mutual Distillation among the Experts](https://arxiv.org/abs/2402.00893v1) | 2402.00893v1 | 6 |
| 2024-01-30 | [Explainable data-driven modeling via mixture of experts: towards effective blending of grey and black-box models](https://arxiv.org/abs/2401.17118v1) | 2401.17118v1 | 6 |
| 2024-01-30 | [Checkmating One, by Using Many: Combining Mixture of Experts with MCTS to Improve in Chess](https://arxiv.org/abs/2401.16852v3) | 2401.16852v3 | 6 |
| 2024-01-29 | [OpenMoE: An Early Effort on Open Mixture-of-Experts Language Models](https://arxiv.org/abs/2402.01739v2) | 2402.01739v2 | 6 |
| 2024-01-29 | [Routers in Vision Mixture of Experts: An Empirical Study](https://arxiv.org/abs/2401.15969v2) | 2401.15969v2 | 13 |
| 2024-01-28 | [Contrastive Learning and Mixture of Experts Enables Precise Vector Embeddings](https://arxiv.org/abs/2401.15713v3) | 2401.15713v3 | 6 |
| 2024-01-25 | [Is Temperature Sample Efficient for Softmax Gaussian Mixture of Experts?](https://arxiv.org/abs/2401.13875v2) | 2401.13875v2 | 6 |
| 2024-01-24 | [M$^3$TN: Multi-gate Mixture-of-Experts based Multi-valued Treatment Network for Uplift Modeling](https://arxiv.org/abs/2401.14426v1) | 2401.14426v1 | 6 |
| 2024-01-16 | [Exploiting Inter-Layer Expert Affinity for Accelerating Mixture-of-Experts Model Inference](https://arxiv.org/abs/2401.08383v2) | 2401.08383v2 | 14 |
| 2024-01-11 | [DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models](https://arxiv.org/abs/2401.06066v1) | 2401.06066v1 | 7 |
| 2024-01-08 | [Mixtral of Experts](https://arxiv.org/abs/2401.04088v1) | 2401.04088v1 | 6 |
| 2024-01-05 | [Parameter-Efficient Sparsity Crafting from Dense to Mixture-of-Experts for Instruction Tuning on General Tasks](https://arxiv.org/abs/2401.02731v4) | 2401.02731v4 | 7 |
| 2024-01-04 | [Frequency-Adaptive Pan-Sharpening with Mixture of Experts](https://arxiv.org/abs/2401.02151v1) | 2401.02151v1 | 6 |
| 2024-01-04 | [k-Winners-Take-All Ensemble Neural Network](https://arxiv.org/abs/2401.02092v1) | 2401.02092v1 | 6 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-28 | [Fast Inference of Mixture-of-Experts Language Models with Offloading](https://arxiv.org/abs/2312.17238v1) | 2312.17238v1 | 6 |
| 2023-12-27 | [Efficient Deweather Mixture-of-Experts with Uncertainty-aware Feature-wise Linear Modulation](https://arxiv.org/abs/2312.16610v1) | 2312.16610v1 | 8 |
| 2023-12-22 | [Aurora:Activating Chinese chat capability for Mixtral-8x7B sparse Mixture-of-Experts through Instruction-Tuning](https://arxiv.org/abs/2312.14557v2) | 2312.14557v2 | 10 |
| 2023-12-19 | [Generator Assisted Mixture of Experts For Feature Acquisition in Batch](https://arxiv.org/abs/2312.12574v1) | 2312.12574v1 | 6 |
| 2023-12-15 | [LoRAMoE: Alleviate World Knowledge Forgetting in Large Language Models via MoE-Style Plugin](https://arxiv.org/abs/2312.09979v4) | 2312.09979v4 | 6 |
| 2023-12-15 | [Optimal Transport Aggregation for Distributed Mixture-of-Experts](https://arxiv.org/abs/2312.09877v3) | 2312.09877v3 | 6 |
| 2023-12-13 | [Training of Neural Networks with Uncertain Data: A Mixture of Experts Approach](https://arxiv.org/abs/2312.08083v4) | 2312.08083v4 | 6 |
| 2023-12-13 | [SwitchHead: Accelerating Transformers with Mixture-of-Experts Attention](https://arxiv.org/abs/2312.07987v3) | 2312.07987v3 | 10 |
| 2023-12-12 | [Parameter Efficient Adaptation for Image Restoration with Heterogeneous Mixture-of-Experts](https://arxiv.org/abs/2312.08881v2) | 2312.08881v2 | 6 |
| 2023-12-12 | [HyperRouter: Towards Efficient Training and Inference of Sparse Mixture of Experts](https://arxiv.org/abs/2312.07035v1) | 2312.07035v1 | 13 |
| 2023-12-11 | [Mixture-of-Linear-Experts for Long-term Time Series Forecasting](https://arxiv.org/abs/2312.06786v3) | 2312.06786v3 | 6 |
| 2023-12-11 | [Uncovering high-dimensional phase space and the application of Mixture of Experts (MoE) on building the Large CALPHAD Model (LCM)](https://arxiv.org/abs/2312.06429v1) | 2312.06429v1 | 6 |
| 2023-12-04 | [MoE-AMC: Enhancing Automatic Modulation Classification Performance Using Mixture-of-Experts](https://arxiv.org/abs/2312.02298v1) | 2312.02298v1 | 6 |
| 2023-12-03 | [MoEC: Mixture of Experts Implicit Neural Compression](https://arxiv.org/abs/2312.01361v1) | 2312.01361v1 | 6 |
| 2023-11-23 | [HOPE: A Memory-Based and Composition-Aware Framework for Zero-Shot Learning with Hopfield Network and Soft Mixture of Experts](https://arxiv.org/abs/2311.14747v2) | 2311.14747v2 | 6 |
| 2023-11-08 | [DAMEX: Dataset-aware Mixture-of-Experts for visual understanding of mixture-of-datasets](https://arxiv.org/abs/2311.04894v1) | 2311.04894v1 | 6 |
| 2023-11-06 | [CAME: Competitively Learning a Mixture-of-Experts Model for First-stage Retrieval](https://arxiv.org/abs/2311.02834v1) | 2311.02834v1 | 6 |
| 2023-11-01 | [Mixture-of-Experts for Open Set Domain Adaptation: A Dual-Space Detection Approach](https://arxiv.org/abs/2311.00285v2) | 2311.00285v2 | 12 |
| 2023-10-29 | [SiDA-MoE: Sparsity-Inspired Data-Aware Serving for Efficient and Scalable Large Mixture-of-Experts Models](https://arxiv.org/abs/2310.18859v2) | 2310.18859v2 | 6 |
| 2023-10-22 | [A General Theory for Softmax Gating Multinomial Logistic Mixture of Experts](https://arxiv.org/abs/2310.14188v2) | 2310.14188v2 | 10 |
| 2023-10-18 | [Direct Neural Machine Translation with Task-level Mixture of Experts models](https://arxiv.org/abs/2310.12236v2) | 2310.12236v2 | 6 |
| 2023-10-18 | [Image Super-resolution Via Latent Diffusion: A Sampling-space Mixture Of Experts And Frequency-augmented Decoder Approach](https://arxiv.org/abs/2310.12004v3) | 2310.12004v3 | 6 |
| 2023-10-15 | [Merging Experts into One: Improving Computational Efficiency of Mixture of Experts](https://arxiv.org/abs/2310.09832v3) | 2310.09832v3 | 7 |
| 2023-10-15 | [Diversifying the Mixture-of-Experts Representation for Language Models with Orthogonal Optimizer](https://arxiv.org/abs/2310.09762v2) | 2310.09762v2 | 10 |
| 2023-10-11 | [Adaptive Gating in Mixture-of-Experts based Language Models](https://arxiv.org/abs/2310.07188v1) | 2310.07188v1 | 7 |
| 2023-10-06 | [Exploiting Activation Sparsity with Dense to Dynamic-k Mixture-of-Experts Conversion](https://arxiv.org/abs/2310.04361v4) | 2310.04361v4 | 6 |
| 2023-10-04 | [Reinforcement Learning-based Mixture of Vision Transformers for Video Violence Recognition](https://arxiv.org/abs/2310.03108v1) | 2310.03108v1 | 6 |
| 2023-10-04 | [BA-MoE: Boundary-Aware Mixture-of-Experts Adapter for Code-Switching Speech Recognition](https://arxiv.org/abs/2310.02629v2) | 2310.02629v2 | 6 |
| 2023-10-01 | [Sparse Backpropagation for MoE Training](https://arxiv.org/abs/2310.00811v1) | 2310.00811v1 | 8 |
| 2023-09-25 | [Statistical Perspective of Top-K Sparse Softmax Gating Mixture of Experts](https://arxiv.org/abs/2309.13850v2) | 2309.13850v2 | 7 |
| 2023-09-11 | [Pushing Mixture of Experts to the Limit: Extremely Parameter Efficient MoE for Instruction Tuning](https://arxiv.org/abs/2309.05444v1) | 2309.05444v1 | 6 |
| 2023-09-08 | [Mobile V-MoEs: Scaling Down Vision Transformers via Sparse Mixture-of-Experts](https://arxiv.org/abs/2309.04354v1) | 2309.04354v1 | 9 |
| 2023-09-07 | [Exploring Sparse MoE in GANs for Text-conditioned Image Synthesis](https://arxiv.org/abs/2309.03904v1) | 2309.03904v1 | 7 |
| 2023-08-23 | [Pre-gated MoE: An Algorithm-System Co-Design for Fast and Scalable Mixture-of-Expert Inference](https://arxiv.org/abs/2308.12066v3) | 2308.12066v3 | 9 |
| 2023-08-22 | [Enhancing NeRF akin to Enhancing LLMs: Generalizable NeRF Transformer with Mixture-of-View-Experts](https://arxiv.org/abs/2308.11793v1) | 2308.11793v1 | 6 |
| 2023-08-12 | [HyperFormer: Enhancing Entity and Relation Interaction for Hyper-Relational Knowledge Graph Completion](https://arxiv.org/abs/2308.06512v1) | 2308.06512v1 | 6 |
| 2023-08-11 | [Experts Weights Averaging: A New General Training Scheme for Vision Transformers](https://arxiv.org/abs/2308.06093v2) | 2308.06093v2 | 6 |
| 2023-08-01 | [A Novel Temporal Multi-Gate Mixture-of-Experts Approach for Vehicle Trajectory and Driving Intention Prediction](https://arxiv.org/abs/2308.00533v1) | 2308.00533v1 | 6 |
| 2023-07-28 | [TaskExpert: Dynamically Assembling Multi-Task Representations with Memorial Mixture-of-Experts](https://arxiv.org/abs/2307.15324v1) | 2307.15324v1 | 6 |
| 2023-07-18 | [MLP Fusion: Towards Efficient Fine-tuning of Dense and Mixture-of-Experts Language Models](https://arxiv.org/abs/2307.08941v3) | 2307.08941v3 | 6 |
| 2023-07-12 | [Language-Routing Mixture of Experts for Multilingual and Code-Switching Speech Recognition](https://arxiv.org/abs/2307.05956v2) | 2307.05956v2 | 8 |
| 2023-06-28 | [Chatlaw: A Multi-Agent Legal Assistant based on a Role-Aligned Mixture-of-Experts Architecture](https://arxiv.org/abs/2306.16092v3) | 2306.16092v3 | 6 |
| 2023-06-10 | [ShiftAddViT: Mixture of Multiplication Primitives Towards Efficient Vision Transformer](https://arxiv.org/abs/2306.06446v6) | 2306.06446v6 | 6 |
| 2023-06-08 | [Attention Weighted Mixture of Experts with Contrastive Learning for Personalized Ranking in E-commerce](https://arxiv.org/abs/2306.05011v1) | 2306.05011v1 | 8 |
| 2023-06-08 | [Mixture-of-Supernets: Improving Weight-Sharing Supernet Training with Architecture-Routed Mixture-of-Experts](https://arxiv.org/abs/2306.04845v2) | 2306.04845v2 | 6 |
| 2023-06-07 | [ModuleFormer: Modularity Emerges from Mixture-of-Experts](https://arxiv.org/abs/2306.04640v2) | 2306.04640v2 | 14 |
| 2023-06-07 | [Patch-level Routing in Mixture-of-Experts is Provably Sample-efficient for Convolutional Neural Networks](https://arxiv.org/abs/2306.04073v1) | 2306.04073v1 | 8 |
| 2023-06-05 | [COMET: Learning Cardinality Constrained Mixture of Experts with Trees and Local Search](https://arxiv.org/abs/2306.02824v1) | 2306.02824v1 | 14 |
| 2023-05-30 | [Edge-MoE: Memory-Efficient Multi-Task Vision Transformer Architecture with Task-level Sparsity via Mixture-of-Experts](https://arxiv.org/abs/2305.18691v2) | 2305.18691v2 | 6 |
| 2023-05-25 | [Modeling Task Relationships in Multi-variate Soft Sensor with Balanced Mixture-of-Experts](https://arxiv.org/abs/2305.16360v1) | 2305.16360v1 | 10 |
| 2023-05-24 | [Mixture-of-Experts Meets Instruction Tuning:A Winning Combination for Large Language Models](https://arxiv.org/abs/2305.14705v2) | 2305.14705v2 | 6 |
| 2023-05-23 | [Towards A Unified View of Sparse Feed-Forward Network in Pretraining Large Language Model](https://arxiv.org/abs/2305.13999v3) | 2305.13999v3 | 8 |
| 2023-05-23 | [LightCurve MoE: A Dynamic Sparse Routing Mixture-of-Experts Architecture for Efficient Stellar Light Curve Classification](https://arxiv.org/abs/2305.13745v3) | 2305.13745v3 | 8 |
| 2023-05-12 | [Towards Convergence Rates for Parameter Estimation in Gaussian-gated Mixture of Experts](https://arxiv.org/abs/2305.07572v2) | 2305.07572v2 | 6 |
| 2023-05-10 | [Alternating Gradient Descent and Mixture-of-Experts for Integrated Multimodal Perception](https://arxiv.org/abs/2305.06324v2) | 2305.06324v2 | 7 |
| 2023-05-05 | [Steered Mixture-of-Experts Autoencoder Design for Real-Time Image Modelling and Denoising](https://arxiv.org/abs/2305.03485v1) | 2305.03485v1 | 6 |
| 2023-05-05 | [Demystifying Softmax Gating Function in Gaussian Mixture of Experts](https://arxiv.org/abs/2305.03288v2) | 2305.03288v2 | 6 |
| 2023-05-03 | [Towards Being Parameter-Efficient: A Stratified Sparsely Activated Transformer with Dynamic Capacity](https://arxiv.org/abs/2305.02176v2) | 2305.02176v2 | 8 |
| 2023-04-11 | [Revisiting Single-gated Mixtures of Experts](https://arxiv.org/abs/2304.05497v1) | 2304.05497v1 | 6 |
| 2023-04-06 | [Graph Mixture of Experts: Learning on Large-Scale Graphs with Explicit Diversity Modeling](https://arxiv.org/abs/2304.02806v2) | 2304.02806v2 | 10 |
| 2023-03-30 | [Steered Mixture of Experts Regression for Image Denoising with Multi-Model-Inference](https://arxiv.org/abs/2303.17409v2) | 2303.17409v2 | 10 |
| 2023-03-24 | [WM-MoE: Weather-aware Multi-scale Mixture-of-Experts for Blind Adverse Weather Removal](https://arxiv.org/abs/2303.13739v2) | 2303.13739v2 | 8 |
| 2023-03-22 | [Improving Transformer Performance for French Clinical Notes Classification Using Mixture of Experts on a Limited Dataset](https://arxiv.org/abs/2303.12892v3) | 2303.12892v3 | 6 |
| 2023-03-21 | [Learning A Sparse Transformer Network for Effective Image Deraining](https://arxiv.org/abs/2303.11950v1) | 2303.11950v1 | 6 |
| 2023-03-13 | [Scaling Vision-Language Models with Sparse Mixture of Experts](https://arxiv.org/abs/2303.07226v1) | 2303.07226v1 | 11 |
| 2023-03-11 | [A Hybrid Tensor-Expert-Data Parallelism Approach to Optimize Mixture-of-Experts Training](https://arxiv.org/abs/2303.06318v2) | 2303.06318v2 | 6 |
| 2023-03-10 | [Towards MoE Deployment: Mitigating Inefficiencies in Mixture-of-Expert (MoE) Inference](https://arxiv.org/abs/2303.06182v2) | 2303.06182v2 | 8 |
| 2023-03-02 | [Sparse MoE as the New Dropout: Scaling Dense and Self-Slimmable Transformers](https://arxiv.org/abs/2303.01610v1) | 2303.01610v1 | 7 |
| 2023-02-28 | [Improving Expert Specialization in Mixture of Experts](https://arxiv.org/abs/2302.14703v1) | 2302.14703v1 | 6 |
| 2023-02-23 | [Improved Training of Mixture-of-Experts Language GANs](https://arxiv.org/abs/2302.11875v1) | 2302.11875v1 | 6 |
| 2023-02-04 | [mixdistreg: An R Package for Fitting Mixture of Experts Distributional Regression with Adaptive First-order Methods](https://arxiv.org/abs/2302.02043v1) | 2302.02043v1 | 6 |
| 2023-02-02 | [Fast, Differentiable and Sparse Top-k: a Convex Analysis Perspective](https://arxiv.org/abs/2302.01425v3) | 2302.01425v3 | 6 |

### 2022
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2022-12-15 | [Mod-Squad: Designing Mixture of Experts As Modular Multi-Task Learners](https://arxiv.org/abs/2212.08066v1) | 2212.08066v1 | 6 |
| 2022-12-10 | [SMILE: Scaling Mixture-of-Experts with Efficient Bi-level Routing](https://arxiv.org/abs/2212.05191v1) | 2212.05191v1 | 7 |
| 2022-12-09 | [Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints](https://arxiv.org/abs/2212.05055v2) | 2212.05055v2 | 7 |
| 2022-11-29 | [MegaBlocks: Efficient Sparse Training with Mixture-of-Experts](https://arxiv.org/abs/2211.15841v1) | 2211.15841v1 | 6 |
| 2022-11-24 | [Spatial Mixture-of-Experts](https://arxiv.org/abs/2211.13491v1) | 2211.13491v1 | 6 |
| 2022-11-17 | [Mixture of Experts Distributional Regression: Implementation Using Robust Estimation with Adaptive First-order Methods](https://arxiv.org/abs/2211.09875v1) | 2211.09875v1 | 6 |
| 2022-11-15 | [HMOE: Hypernetwork-based Mixture of Experts for Domain Generalization](https://arxiv.org/abs/2211.08253v3) | 2211.08253v3 | 6 |
| 2022-11-11 | [Handling Trade-Offs in Speech Separation with Sparsely-Gated Mixture of Experts](https://arxiv.org/abs/2211.06493v2) | 2211.06493v2 | 10 |
| 2022-11-07 | [Using Deep Mixture-of-Experts to Detect Word Meaning Shift for TempoWiC](https://arxiv.org/abs/2211.03466v1) | 2211.03466v1 | 6 |
| 2022-11-01 | [Contextual Mixture of Experts: Integrating Knowledge into Predictive Modeling](https://arxiv.org/abs/2211.00558v1) | 2211.00558v1 | 6 |
| 2022-10-30 | [Prediction Sets for High-Dimensional Mixture of Experts Models](https://arxiv.org/abs/2210.16710v1) | 2210.16710v1 | 6 |
| 2022-10-28 | [Knowledge-in-Context: Towards Knowledgeable Semi-Parametric Language Models](https://arxiv.org/abs/2210.16433v3) | 2210.16433v3 | 6 |
| 2022-10-26 | [M$^3$ViT: Mixture-of-Experts Vision Transformer for Efficient Multi-task Learning with Model-Accelerator Co-design](https://arxiv.org/abs/2210.14793v1) | 2210.14793v1 | 10 |
| 2022-10-19 | [On the Adversarial Robustness of Mixture of Experts](https://arxiv.org/abs/2210.10253v1) | 2210.10253v1 | 6 |
| 2022-10-18 | [Tiny-Attention Adapter: Contexts Are More Important Than the Number of Parameters](https://arxiv.org/abs/2211.01979v1) | 2211.01979v1 | 6 |
| 2022-10-14 | [AutoMoE: Heterogeneous Mixture-of-Experts with Adaptive Computation for Efficient Neural Machine Translation](https://arxiv.org/abs/2210.07535v2) | 2210.07535v2 | 6 |
| 2022-10-11 | [Mixture of Attention Heads: Selecting Attention Heads Per Token](https://arxiv.org/abs/2210.05144v1) | 2210.05144v1 | 6 |
| 2022-10-10 | [FEAMOE: Fair, Explainable and Adaptive Mixture of Experts](https://arxiv.org/abs/2210.04995v1) | 2210.04995v1 | 10 |
| 2022-10-08 | [Meta-DMoE: Adapting to Domain Shift by Meta-Distillation from Mixture-of-Experts](https://arxiv.org/abs/2210.03885v2) | 2210.03885v2 | 6 |
| 2022-09-30 | [Mixture of experts models for multilevel data: modelling framework and approximation theory](https://arxiv.org/abs/2209.15207v1) | 2209.15207v1 | 6 |
| 2022-09-29 | [Tuning of Mixture-of-Experts Mixed-Precision Neural Networks](https://arxiv.org/abs/2209.15427v1) | 2209.15427v1 | 6 |
| 2022-09-17 | [Parameter-Efficient Conformers via Sharing Sparsely-Gated Experts for End-to-End Speech Recognition](https://arxiv.org/abs/2209.08326v1) | 2209.08326v1 | 6 |
| 2022-09-13 | [Sparse Video Representation Using Steered Mixture-of-Experts With Global Motion Compensation](https://arxiv.org/abs/2209.05993v1) | 2209.05993v1 | 6 |
| 2022-09-04 | [A Review of Sparse Expert Models in Deep Learning](https://arxiv.org/abs/2209.01667v1) | 2209.01667v1 | 10 |
| 2022-08-24 | [ADMoE: Anomaly Detection with Mixture-of-Experts from Noisy Labels](https://arxiv.org/abs/2208.11290v2) | 2208.11290v2 | 6 |
| 2022-08-15 | [Context-aware Mixture-of-Experts for Unbiased Scene Graph Generation](https://arxiv.org/abs/2208.07109v3) | 2208.07109v3 | 10 |
| 2022-08-04 | [Towards Understanding Mixture of Experts in Deep Learning](https://arxiv.org/abs/2208.02813v1) | 2208.02813v1 | 12 |
| 2022-07-28 | [Towards overcoming data scarcity in materials science: unifying models and datasets with a mixture of experts framework](https://arxiv.org/abs/2207.13880v1) | 2207.13880v1 | 6 |
| 2022-07-27 | [BotBuster: Multi-platform Bot Detection Using A Mixture of Experts](https://arxiv.org/abs/2207.13658v1) | 2207.13658v1 | 6 |
| 2022-07-25 | [Edge-Aware Autoencoder Design for Real-Time Mixture-of-Experts Image Compression](https://arxiv.org/abs/2207.12348v1) | 2207.12348v1 | 6 |
| 2022-07-20 | [Adaptive Mixture of Experts Learning for Generalizable Face Anti-Spoofing](https://arxiv.org/abs/2207.09868v1) | 2207.09868v1 | 6 |
| 2022-07-19 | [MoEC: Mixture of Expert Clusters](https://arxiv.org/abs/2207.09094v1) | 2207.09094v1 | 9 |
| 2022-06-08 | [Sparse Mixture-of-Experts are Domain Generalizable Learners](https://arxiv.org/abs/2206.04046v6) | 2206.04046v6 | 6 |
| 2022-06-07 | [Tutel: Adaptive Mixture-of-Experts at Scale](https://arxiv.org/abs/2206.03382v2) | 2206.03382v2 | 6 |
| 2022-06-07 | [Quantitative Stock Investment by Routing Uncertainty-Aware Trading Experts: A Multi-Task Learning Approach](https://arxiv.org/abs/2207.07578v1) | 2207.07578v1 | 6 |
| 2022-06-06 | [Multimodal Contrastive Learning with LIMoE: the Language-Image Mixture of Experts](https://arxiv.org/abs/2206.02770v1) | 2206.02770v1 | 6 |
| 2022-06-05 | [Interpretable Mixture of Experts](https://arxiv.org/abs/2206.02107v2) | 2206.02107v2 | 6 |
| 2022-06-03 | [Patcher: Patch Transformers with Mixture of Experts for Precise Medical Image Segmentation](https://arxiv.org/abs/2206.01741v2) | 2206.01741v2 | 10 |
| 2022-06-01 | [Task-Specific Expert Pruning for Sparse Mixture-of-Experts](https://arxiv.org/abs/2206.00277v2) | 2206.00277v2 | 6 |
| 2022-05-31 | [Text2Human: Text-Driven Controllable Human Image Generation](https://arxiv.org/abs/2205.15996v1) | 2205.15996v1 | 8 |
| 2022-05-28 | [Gating Dropout: Communication-efficient Regularization for Sparsely Activated Transformers](https://arxiv.org/abs/2205.14336v2) | 2205.14336v2 | 9 |
| 2022-05-25 | [Eliciting and Understanding Cross-Task Skills with Task-Level Mixture-of-Experts](https://arxiv.org/abs/2205.12701v2) | 2205.12701v2 | 8 |
| 2022-05-20 | [MoESys: A Distributed and Efficient Mixture-of-Experts Training and Inference System for Internet Services](https://arxiv.org/abs/2205.10034v3) | 2205.10034v3 | 10 |
| 2022-05-04 | [Optimizing Mixture of Experts using Dynamic Recompilations](https://arxiv.org/abs/2205.01848v2) | 2205.01848v2 | 7 |
| 2022-04-20 | [Residual Mixture of Experts](https://arxiv.org/abs/2204.09636v3) | 2204.09636v3 | 6 |
| 2022-04-20 | [On the Representation Collapse of Sparse Mixture of Experts](https://arxiv.org/abs/2204.09179v3) | 2204.09179v3 | 10 |
| 2022-04-19 | [Table-based Fact Verification with Self-adaptive Mixture of Experts](https://arxiv.org/abs/2204.08753v1) | 2204.08753v1 | 10 |
| 2022-04-18 | [StableMoE: Stable Routing Strategy for Mixture of Experts](https://arxiv.org/abs/2204.08396v1) | 2204.08396v1 | 12 |
| 2022-04-16 | [Sparsely Activated Mixture-of-Experts are Robust Multi-Task Learners](https://arxiv.org/abs/2204.07689v1) | 2204.07689v1 | 6 |
| 2022-04-15 | [MoEBERT: from BERT to Mixture-of-Experts via Importance-Guided Adaptation](https://arxiv.org/abs/2204.07675v2) | 2204.07675v2 | 8 |
| 2022-04-15 | [Mixture of Experts for Biomedical Question Answering](https://arxiv.org/abs/2204.07469v1) | 2204.07469v1 | 6 |
| 2022-04-11 | [Mixture-of-experts VAEs can disregard variation in surjective multimodal data](https://arxiv.org/abs/2204.05229v1) | 2204.05229v1 | 10 |
| 2022-04-06 | [Learning to Adapt Clinical Sequences with Residual Mixture of Experts](https://arxiv.org/abs/2204.02687v1) | 2204.02687v1 | 10 |
| 2022-03-20 | [Build a Robust QA System with Transformer-based Mixture of Experts](https://arxiv.org/abs/2204.09598v1) | 2204.09598v1 | 12 |
| 2022-03-13 | [SummaReranker: A Multi-Task Mixture-of-Experts Re-ranking Framework for Abstractive Summarization](https://arxiv.org/abs/2203.06569v2) | 2203.06569v2 | 6 |
| 2022-03-02 | [Parameter-Efficient Mixture-of-Experts Architecture for Pre-trained Language Models](https://arxiv.org/abs/2203.01104v4) | 2203.01104v4 | 6 |
| 2022-02-28 | [Functional mixture-of-experts for classification](https://arxiv.org/abs/2202.13934v1) | 2202.13934v1 | 6 |
| 2022-02-18 | [Mixture-of-Experts with Expert Choice Routing](https://arxiv.org/abs/2202.09368v2) | 2202.09368v2 | 10 |
| 2022-02-17 | [ST-MoE: Designing Stable and Transferable Sparse Expert Models](https://arxiv.org/abs/2202.08906v2) | 2202.08906v2 | 12 |
| 2022-01-14 | [DeepSpeed-MoE: Advancing Mixture-of-Experts Inference and Training to Power Next-Generation AI Scale](https://arxiv.org/abs/2201.05596v2) | 2201.05596v2 | 6 |
| 2022-01-11 | [Towards Lightweight Neural Animation : Exploration of Neural Network Pruning in Mixture of Experts-based Animation Models](https://arxiv.org/abs/2201.04042v2) | 2201.04042v2 | 10 |

### 2021
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2021-12-29 | [EvoMoE: An Evolutional Mixture-of-Experts Training Framework via Dense-To-Sparse Gate](https://arxiv.org/abs/2112.14397v2) | 2112.14397v2 | 6 |
| 2021-12-13 | [GLaM: Efficient Scaling of Language Models with Mixture-of-Experts](https://arxiv.org/abs/2112.06905v2) | 2112.06905v2 | 7 |
| 2021-12-10 | [Building a great multi-lingual teacher with sparsely-gated mixture of experts for speech recognition](https://arxiv.org/abs/2112.05820v3) | 2112.05820v3 | 6 |
| 2021-12-08 | [Specializing Versatile Skill Libraries using Local Mixture of Experts](https://arxiv.org/abs/2112.04216v2) | 2112.04216v2 | 6 |
| 2021-11-23 | [SpeechMoE2: Mixture-of-Experts Model with Improved Routing](https://arxiv.org/abs/2111.11831v1) | 2111.11831v1 | 8 |
| 2021-10-31 | [Phase-type mixture-of-experts regression for loss severities](https://arxiv.org/abs/2111.00581v2) | 2111.00581v2 | 6 |
| 2021-10-13 | [Simple or Complex? Complexity-Controllable Question Generation with Soft Templates and Deep Mixture of Experts Model](https://arxiv.org/abs/2110.06560v1) | 2110.06560v1 | 6 |
| 2021-09-24 | [Beyond Distillation: Task-level Mixture-of-Experts for Efficient Inference](https://arxiv.org/abs/2110.03742v1) | 2110.03742v1 | 8 |
| 2021-09-23 | [Dynamic Mixture of Experts Models for Online Prediction](https://arxiv.org/abs/2109.11449v2) | 2109.11449v2 | 6 |
| 2021-09-11 | [Universal Simultaneous Machine Translation with Mixture-of-Experts Wait-k Policy](https://arxiv.org/abs/2109.05238v3) | 2109.05238v3 | 10 |
| 2021-09-05 | [Cross-token Modeling with Conditional Computation](https://arxiv.org/abs/2109.02008v3) | 2109.02008v3 | 7 |
| 2021-08-17 | [SPMoE: Generate Multiple Pattern-Aware Outputs with Sparse Pattern Mixture of Experts](https://arxiv.org/abs/2108.07535v2) | 2108.07535v2 | 6 |
| 2021-07-25 | [Go Wider Instead of Deeper](https://arxiv.org/abs/2107.11817v3) | 2107.11817v3 | 6 |
| 2021-07-14 | [Federated Mixture of Experts](https://arxiv.org/abs/2107.06724v1) | 2107.06724v1 | 6 |
| 2021-06-23 | [Mixtures of Deep Neural Experts for Automated Speech Scoring](https://arxiv.org/abs/2106.12475v1) | 2106.12475v1 | 6 |
| 2021-06-10 | [Scaling Vision with Sparse Mixture of Experts](https://arxiv.org/abs/2106.05974v1) | 2106.05974v1 | 7 |
| 2021-06-07 | [DSelect-k: Differentiable Selection in the Mixture of Experts with Applications to Multi-Task Learning](https://arxiv.org/abs/2106.03760v3) | 2106.03760v3 | 11 |
| 2021-05-31 | [M6-T: Exploring Sparse Expert Models and Beyond](https://arxiv.org/abs/2105.15082v5) | 2105.15082v5 | 11 |
| 2021-05-19 | [Generalizable Person Re-identification with Relevance-aware Mixture of Experts](https://arxiv.org/abs/2105.09156v1) | 2105.09156v1 | 6 |
| 2021-05-07 | [SpeechMoE: Scaling to Large Acoustic Models with Dynamic Routing Mixture of Experts](https://arxiv.org/abs/2105.03036v1) | 2105.03036v1 | 9 |
| 2021-04-23 | [Robust Federated Learning by Mixture of Experts](https://arxiv.org/abs/2104.11700v1) | 2104.11700v1 | 6 |
| 2021-04-19 | [Probabilistic Mixture-of-Experts for Efficient Deep Reinforcement Learning](https://arxiv.org/abs/2104.09122v1) | 2104.09122v1 | 6 |
| 2021-04-06 | [A non-asymptotic approach for model selection via penalization in high-dimensional mixture of experts models](https://arxiv.org/abs/2104.02640v3) | 2104.02640v3 | 6 |
| 2021-01-13 | [Preferential Mixture-of-Experts: Interpretable Models that Rely on Human Expertise as much as Possible](https://arxiv.org/abs/2101.05360v1) | 2101.05360v1 | 6 |
| 2021-01-11 | [Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](https://arxiv.org/abs/2101.03961v3) | 2101.03961v3 | 6 |

### 2020
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2020-12-31 | [Gated Ensemble of Spatio-temporal Mixture of Experts for Multi-task Learning in Ride-hailing System](https://arxiv.org/abs/2012.15408v6) | 2012.15408v6 | 6 |
| 2020-12-08 | [Channel Gain Cartography via Mixture of Experts](https://arxiv.org/abs/2012.04290v1) | 2012.04290v1 | 10 |
| 2020-12-04 | [Approximations of conditional probability density functions in Lebesgue spaces via mixture of experts models](https://arxiv.org/abs/2012.02385v2) | 2012.02385v2 | 6 |
| 2020-12-03 | [A similarity-based Bayesian mixture-of-experts model](https://arxiv.org/abs/2012.02130v4) | 2012.02130v4 | 6 |
| 2020-11-20 | [Nested Mixture of Experts: Cooperative and Competitive Learning of Hybrid Dynamical System](https://arxiv.org/abs/2011.10605v2) | 2011.10605v2 | 6 |
| 2020-10-05 | [Specialized federated learning using a mixture of experts](https://arxiv.org/abs/2010.02056v3) | 2010.02056v3 | 6 |
| 2020-09-30 | [Restoring Spatially-Heterogeneous Distortions using Mixture of Experts Network](https://arxiv.org/abs/2009.14563v1) | 2009.14563v1 | 6 |
| 2020-09-22 | [Non-asymptotic oracle inequalities for the Lasso in high-dimensional mixture of experts](https://arxiv.org/abs/2009.10622v7) | 2009.10622v7 | 6 |
| 2020-09-14 | [Double-Wing Mixture of Experts for Streaming Recommendations](https://arxiv.org/abs/2009.06327v1) | 2009.06327v1 | 6 |
| 2020-08-13 | [MIXCAPS: A Capsule Network-based Mixture of Experts for Lung Nodule Malignancy Prediction](https://arxiv.org/abs/2008.06072v1) | 2008.06072v1 | 6 |
| 2020-07-28 | [Team Deep Mixture of Experts for Distributed Power Control](https://arxiv.org/abs/2007.14147v1) | 2007.14147v1 | 6 |
| 2020-07-24 | [Adversarial Mixture Of Experts with Category Hierarchy Soft Constraint](https://arxiv.org/abs/2007.12349v3) | 2007.12349v3 | 6 |
| 2020-07-05 | [Extending Mixture of Experts Model to Investigate Heterogeneity of Trajectories: When, Where and How to Add Which Covariates](https://arxiv.org/abs/2007.02432v8) | 2007.02432v8 | 10 |

### 2019
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2019-12-27 | [MoEVC: A Mixture-of-experts Voice Conversion System with Sparse Gating Mechanism for Accelerating Online Computation](https://arxiv.org/abs/1912.11984v1) | 1912.11984v1 | 6 |
| 2019-11-08 | [Variational Mixture-of-Experts Autoencoders for Multi-Modal Deep Generative Models](https://arxiv.org/abs/1911.03393v1) | 1911.03393v1 | 6 |
| 2019-10-23 | [Efficient bifurcation and parameterization of multi-dimensional combustion manifolds using deep mixture of experts: an a priori study](https://arxiv.org/abs/1910.10765v2) | 1910.10765v2 | 6 |
| 2019-10-21 | [Tree-gated Deep Mixture-of-Experts For Pose-robust Face Alignment](https://arxiv.org/abs/1910.09450v1) | 1910.09450v1 | 10 |
| 2019-10-17 | [Mixture-of-Experts Variational Autoencoder for Clustering and Generating from Similarity-Based Representations on Single Cell Data](https://arxiv.org/abs/1910.07763v3) | 1910.07763v3 | 6 |
| 2019-07-10 | [A Modular Task-oriented Dialogue System Using a Neural Mixture-of-Experts](https://arxiv.org/abs/1907.05346v1) | 1907.05346v1 | 6 |
| 2019-04-22 | [PLUME: Polyhedral Learning Using Mixture of Experts](https://arxiv.org/abs/1904.09948v1) | 1904.09948v1 | 6 |
| 2019-04-09 | [Bivariate Gamma Mixture of Experts Models for Joint Insurance Claims Modeling](https://arxiv.org/abs/1904.04699v1) | 1904.04699v1 | 6 |
| 2019-03-25 | [On the Functional Equivalence of TSK Fuzzy Systems to Neural Networks, Mixture of Experts, CART, and Stacking Ensemble Regression](https://arxiv.org/abs/1903.10572v2) | 1903.10572v2 | 6 |
| 2019-03-24 | [A mixture of experts model for predicting persistent weather patterns](https://arxiv.org/abs/1903.10012v1) | 1903.10012v1 | 6 |
| 2019-03-18 | [Hierarchical Routing Mixture of Experts](https://arxiv.org/abs/1903.07756v1) | 1903.07756v1 | 6 |
| 2019-02-28 | [Tensor-variate Mixture of Experts for Proportional Myographic Control of a Robotic Hand](https://arxiv.org/abs/1902.11104v3) | 1902.11104v3 | 10 |

### 2018
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2018-12-25 | [Dropout Regularization in Hierarchical Mixture of Experts](https://arxiv.org/abs/1812.10158v1) | 1812.10158v1 | 6 |
| 2018-11-07 | [Learning to Compose Topic-Aware Mixture of Experts for Zero-Shot Video Captioning](https://arxiv.org/abs/1811.02765v2) | 1811.02765v2 | 6 |
| 2018-09-13 | [Bayesian shrinkage in mixture of experts models: Identifying robust determinants of class membership](https://arxiv.org/abs/1809.04853v2) | 1809.04853v2 | 6 |
| 2018-09-07 | [Multi-Source Domain Adaptation with Mixture of Experts](https://arxiv.org/abs/1809.02256v2) | 1809.02256v2 | 10 |
| 2018-06-19 | [MoE-SPNet: A Mixture-of-Experts Scene Parsing Network](https://arxiv.org/abs/1806.07049v1) | 1806.07049v1 | 6 |
| 2018-06-05 | [Deep Mixture of Experts via Shallow Embedding](https://arxiv.org/abs/1806.01531v3) | 1806.01531v3 | 7 |
| 2018-05-07 | [MEGAN: Mixture of Experts of Generative Adversarial Networks for Multimodal Image Generation](https://arxiv.org/abs/1805.02481v2) | 1805.02481v2 | 6 |
| 2018-03-07 | [Discontinuity-Sensitive Optimal Control Learning by Mixture of Experts](https://arxiv.org/abs/1803.02493v2) | 1803.02493v2 | 6 |
| 2018-02-21 | [Breaking the gridlock in Mixture-of-Experts: Consistent and Efficient Algorithms](https://arxiv.org/abs/1802.07417v3) | 1802.07417v3 | 6 |

### 2017
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2017-10-02 | [Improving Spark Application Throughput Via Memory Aware Task Co-location: A Mixture of Experts Approach](https://arxiv.org/abs/1710.00610v1) | 1710.00610v1 | 10 |
| 2017-07-12 | [An Introduction to the Practical and Theoretical Aspects of Mixture-of-Experts Modeling](https://arxiv.org/abs/1707.03538v1) | 1707.03538v1 | 6 |
| 2017-03-27 | [Speech Enhancement using a Deep Mixture of Experts](https://arxiv.org/abs/1703.09302v1) | 1703.09302v1 | 6 |
| 2017-01-23 | [Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538v1) | 1701.06538v1 | 8 |

### 2016
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2016-12-09 | [Robust mixture of experts modeling using the skew $t$ distribution](https://arxiv.org/abs/1612.06879v1) | 1612.06879v1 | 6 |
| 2016-12-09 | [Robust mixture of experts modeling using the $t$ distribution](https://arxiv.org/abs/1701.07429v1) | 1701.07429v1 | 6 |
| 2016-05-05 | [LSTM-based Mixture-of-Experts for Knowledge-Aware Dialogues](https://arxiv.org/abs/1605.01652v1) | 1605.01652v1 | 6 |
| 2016-02-11 | [A Universal Approximation Theorem for Mixture of Experts Models](https://arxiv.org/abs/1602.03683v1) | 1602.03683v1 | 6 |

### 2014
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2014-12-09 | [Hierarchical Mixture-of-Experts Model for Large-Scale Gaussian Process Regression](https://arxiv.org/abs/1412.3078v1) | 1412.3078v1 | 6 |
| 2014-05-29 | [Simultaneous Feature and Expert Selection within Mixture of Experts](https://arxiv.org/abs/1405.7624v1) | 1405.7624v1 | 6 |

<!-- table:end papers -->
