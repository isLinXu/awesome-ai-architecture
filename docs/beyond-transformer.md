# 🌊 超越 Transformer / 混合架构（Beyond Transformer）

> 当二次复杂度成为天花板：SSM、线性注意力与新循环。

无论怎么优化，softmax 注意力都要为每个 token 维护随上下文增长的 KV cache。
这条赛道收录"换掉注意力"或"只用一点点注意力"的路线：
状态空间模型（Mamba 一脉）、可并行化的 RNN（RWKV/RetNet）、门控线性注意力（Gated DeltaNet），
以及 2025 年后主流的混合栈——大部分层用线性复杂度模块，少数层保留全注意力保精度。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Efficiently Modeling Long Sequences with Structured State Spaces (S4) | [2111.00396](https://arxiv.org/abs/2111.00396) | 2021 | SSM 路线的奠基之作，Mamba 的理论前身 |
| Hyena Hierarchy: Towards Larger Convolutional Language Models | [2302.10866](https://arxiv.org/abs/2302.10866) | 2023 | 长卷积替代注意力的代表路线 |
| RWKV: Reinventing RNNs for the Transformer Era | [2305.13048](https://arxiv.org/abs/2305.13048) | 2023 | 线性注意力的 RNN 化，训练像 Transformer、推理像 RNN |
| Retentive Network: A Successor to Transformer for Large Language Models | [2307.08621](https://arxiv.org/abs/2307.08621) | 2023 | RetNet：保留并行训练的线性复杂度序列建模 |
| Mamba: Linear-Time Sequence Modeling with Selective State Spaces | [2312.00752](https://arxiv.org/abs/2312.00752) | 2023 | 选择性 SSM，让状态随输入变化，线性时间序列建模 |
| Jamba: A Hybrid Transformer-Mamba Language Model | [2403.19887](https://arxiv.org/abs/2403.19887) | 2024 | Transformer-Mamba-MoE 三层混合的早期规模化验证 |
| xLSTM: Extended Long Short-Term Memory | [2405.04517](https://arxiv.org/abs/2405.04517) | 2024 | LSTM 的现代化改造：矩阵记忆 + 指数门控 |
| Transformers are SSMs (Mamba-2) | [2405.21060](https://arxiv.org/abs/2405.21060) | 2024 | SSD 理论：注意力与 SSM 是同一族半可分矩阵的两端 |
| Learning to (Learn at Test Time): RNNs with Expressive Hidden States (TTT) | [2407.04620](https://arxiv.org/abs/2407.04620) | 2024 | 把隐状态本身变成一个小模型，测试时继续训练 |
| Gated Delta Networks: Improving Mamba2 with Delta Rule | [2412.06464](https://arxiv.org/abs/2412.06464) | 2024 | 门控 + delta 规则，线性注意力接近全注意力质量 |
| MiniMax-01: Scaling Foundation Models with Lightning Attention | [2501.08313](https://arxiv.org/abs/2501.08313) | 2025 | Lightning Attention 7:1 混合栈，456B 规模验证 |
| Titans: Learning to Memorize at Test Time | [2501.00663](https://arxiv.org/abs/2501.00663) | 2025 | 神经长期记忆模块，在测试时更新记忆 |
| Kimi Linear: An Expressive, Efficient Attention Architecture | [2510.26692](https://arxiv.org/abs/2510.26692) | 2025 | KDA + MLA 3:1 混合，KV cache 砍掉 75% 还反超全注意力 |

## 相关实现

- [state-spaces/mamba](https://github.com/state-spaces/mamba) — Mamba / Mamba-2 官方实现。
- [BlinkDL/RWKV-LM](https://github.com/BlinkDL/RWKV-LM) — RWKV 官方训练仓库。
- [fla-org/flash-linear-attention](https://github.com/fla-org/flash-linear-attention) — Gated DeltaNet、KDA 等线性注意力 kernel。

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-06 | [MIRA: Mitigating Pole Geometry Bias in Recurrent Language Models](https://arxiv.org/abs/2611.09412v1) | 2611.09412v1 | 12 |
| 2026-11-06 | [RegNC-Mamba3: Shared Structural Feature Learning Using Non-Causal State Space Principles for Multi-Modal Image Registration](https://arxiv.org/abs/2611.09336v1) | 2611.09336v1 | 10 |
| 2026-11-05 | [First-Token Attraction in Mamba Dynamics](https://arxiv.org/abs/2611.08303v1) | 2611.08303v1 | 6 |
| 2026-11-05 | [Identifying Neural Dynamics Using Nonlinear Interventional State Space Models](https://arxiv.org/abs/2611.08113v1) | 2611.08113v1 | 6 |
| 2026-11-05 | [OcTreeMamba: Topology-Aware Mamba for 3D Medical Segmentation via Octree Sparsification](https://arxiv.org/abs/2611.07865v1) | 2611.07865v1 | 6 |
| 2026-11-05 | [MambaTG: Candidate-Aware State Space Modeling for Future Link Prediction on Temporal Graphs](https://arxiv.org/abs/2611.07569v1) | 2611.07569v1 | 12 |
| 2026-11-04 | [Shallow Encoding Emits Deep Memories](https://arxiv.org/abs/2611.06084v1) | 2611.06084v1 | 0 |
| 2026-11-03 | [MambaHand: Local Identity and Behavioral Sequence Learning with Mamba for Dynamic Hand Gesture Authentication](https://arxiv.org/abs/2611.04626v1) | 2611.04626v1 | 6 |
| 2026-11-03 | [Multi-Path Mamba Diffusion for 3D Point Cloud Semantic Scene Completion](https://arxiv.org/abs/2611.04583v1) | 2611.04583v1 | 6 |
| 2026-11-03 | [Near-Zero Token Embeddings Silently Stall Training in Gated Sequence Models](https://arxiv.org/abs/2611.04449v1) | 2611.04449v1 | 0 |
| 2026-11-03 | [LCM-UNet: Scale-Selective Mamba with Reparameterizable Multi-Basis Local Modeling for Lightweight Skin Lesion Segmentation](https://arxiv.org/abs/2611.04409v1) | 2611.04409v1 | 6 |
| 2026-11-03 | [Toward Generalized LEO Channel Prediction: A Rapid Adaptation Time-Frequency Mamba Framework](https://arxiv.org/abs/2611.04224v1) | 2611.04224v1 | 6 |
| 2026-11-02 | [Diagonal Equivalence in State Space Models: Characterization, Retrieval Rank, and Selective Extensions](https://arxiv.org/abs/2611.03101v1) | 2611.03101v1 | 6 |
| 2026-11-01 | [FlyWheel: Attention Kernels Built for the TPU](https://arxiv.org/abs/2611.01426v1) | 2611.01426v1 | 0 |
| 2026-10-31 | [ResMamba: A Dual-Path Convolution-Mamba Model for Music Genre Classification](https://arxiv.org/abs/2611.00746v1) | 2611.00746v1 | 6 |
| 2026-10-30 | [PAM-Mamba - Efficient Dense Action Detection using Mamba](https://arxiv.org/abs/2611.00423v1) | 2611.00423v1 | 6 |
| 2026-10-30 | [Fuzzy selective state model for forecasting the dynamics of consumer preferences](https://arxiv.org/abs/2610.41879v1) | 2610.41879v1 | 0 |
| 2026-10-30 | [Dynamical Memory Transformer: Selective Recurrent Memories with Constant Cost Attention](https://arxiv.org/abs/2610.41850v1) | 2610.41850v1 | 3 |
| 2026-10-29 | [Morphology-Aware Channel-Decoupled Mamba Network for Medical Image Segmentation](https://arxiv.org/abs/2610.40085v2) | 2610.40085v2 | 6 |
| 2026-10-29 | [Segment Anything Model Based Context Guided Mamba Unet for Medical Image Segmentation](https://arxiv.org/abs/2610.40029v2) | 2610.40029v2 | 6 |
| 2026-10-29 | [LinQuant: Functional Invariances for Low-Precision Linear Recurrences](https://arxiv.org/abs/2610.39418v1) | 2610.39418v1 | 0 |
| 2026-10-29 | [Zonal-Aware Prostate Cancer Detection and Classification via Hadamard-Fused Mamba-UNet](https://arxiv.org/abs/2610.40720v1) | 2610.40720v1 | 6 |
| 2026-10-28 | [UnMixMamba: Unmixing Guided State Space Subpixel Mapping of Crops from MODIS Time Series](https://arxiv.org/abs/2610.38507v1) | 2610.38507v1 | 6 |
| 2026-10-28 | [ParaTTT: Parallelizing Test-Time Training Layers with Deep Memories](https://arxiv.org/abs/2610.38255v1) | 2610.38255v1 | 0 |
| 2026-10-27 | [Multi-task Disentangling Fusion Mamba-CNN for MODIS Spectral-Temporal Unmixing with Endmember Variability Modeling](https://arxiv.org/abs/2610.36750v1) | 2610.36750v1 | 6 |
| 2026-10-27 | [Balanced State Subspaces for Mamba-2 State Compression](https://arxiv.org/abs/2610.36617v1) | 2610.36617v1 | 6 |
| 2026-10-26 | [LayoutMamba: Efficient Document Layout Analysis with Hybrid Mamba-Transformer Networks](https://arxiv.org/abs/2610.34879v1) | 2610.34879v1 | 6 |
| 2026-10-25 | [Higher-Order Marginal Likelihood Approximation for Nonlinear State Space Models](https://arxiv.org/abs/2610.34629v1) | 2610.34629v1 | 6 |
| 2026-10-25 | [CORMA: Constraint-Routed Decision Mamba for Generalizable Multi-Constraint Offline Safe Reinforcement Learning](https://arxiv.org/abs/2610.34208v1) | 2610.34208v1 | 6 |
| 2026-10-25 | [Hybrid Mamba-Transformer Network for Single-Shot 3D Reconstruction from Fringe Patterns](https://arxiv.org/abs/2610.33988v1) | 2610.33988v1 | 6 |
| 2026-10-24 | [Real-Time Human Trajectory Prediction from RGB-D for Mobile Robots Using Bi-Mamba](https://arxiv.org/abs/2610.33916v1) | 2610.33916v1 | 6 |
| 2026-10-23 | [FOCUS: A Lightweight Mamba-2 Model for EEG-Based Cognitive Workload Classification](https://arxiv.org/abs/2610.32361v1) | 2610.32361v1 | 6 |
| 2026-10-21 | [Mamba Quantum Eigensolver (MQE): A Selective State Space Model for Scalable Ground State Simulations in Quantum Chemistry](https://arxiv.org/abs/2610.29779v1) | 2610.29779v1 | 15 |
| 2026-10-21 | [LEAF-Mamba: Feature Adaptation and Fusion for Whole Slide Image Analysis](https://arxiv.org/abs/2610.29746v1) | 2610.29746v1 | 6 |
| 2026-10-21 | [PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States](https://arxiv.org/abs/2610.29545v1) | 2610.29545v1 | 3 |
| 2026-10-20 | [GraphCast-Mamba: Learning Non-Markovian Corrections for Weather Forecasting](https://arxiv.org/abs/2610.28512v1) | 2610.28512v1 | 6 |
| 2026-10-20 | [AGGR-Mamba: Mamba-based Network with Attention-Guided Gated Residual Refinement for Undersampled MRI Reconstruction](https://arxiv.org/abs/2610.28291v1) | 2610.28291v1 | 6 |
| 2026-10-20 | [AD-Mamba: Architecture-Complementary Knowledge Distillation for Efficient and Robust Audio Classification](https://arxiv.org/abs/2610.27713v1) | 2610.27713v1 | 6 |
| 2026-10-19 | [Competing Learning in Hybrid Architectures](https://arxiv.org/abs/2610.26830v1) | 2610.26830v1 | 6 |
| 2026-10-19 | [PolMamba: Long-wave Infrared Polarimetric Remote Sensing Image Fusion for Vehicle Detection](https://arxiv.org/abs/2610.27018v2) | 2610.27018v2 | 6 |
| 2026-10-19 | [Multi-scale Fusion of Fast Vision Mamba and Foundation Model Features for Patch-Level Gleason Grading in Computational Pathology](https://arxiv.org/abs/2610.25904v1) | 2610.25904v1 | 6 |
| 2026-10-18 | [State Space Modeling of the Ornstein-Uhlenbeck Process with Measurement Error: An Application to Microbiome Data](https://arxiv.org/abs/2610.25266v2) | 2610.25266v2 | 6 |
| 2026-10-16 | [MambaAct: Efficient Mamba Action Experts for Flow-Matching Vision-Language-Action Models](https://arxiv.org/abs/2610.22951v1) | 2610.22951v1 | 6 |
| 2026-10-14 | [TurboMamba: Faster Inference, Faster Training, and Better Prediction with Lexical Memory](https://arxiv.org/abs/2610.20682v1) | 2610.20682v1 | 6 |
| 2026-10-14 | [Beyond State Capacity: Why Retrieval Breaks in Mamba](https://arxiv.org/abs/2610.19709v1) | 2610.19709v1 | 6 |
| 2026-10-13 | [The Effect of Layer Ordering in Hybrid Architectures](https://arxiv.org/abs/2610.18104v1) | 2610.18104v1 | 6 |
| 2026-10-12 | [SSM-Attack: Learning Where to Perturb for Black-Box Face Privacy](https://arxiv.org/abs/2610.17323v1) | 2610.17323v1 | 0 |
| 2026-10-12 | [FreeSolo: Linear-time Sparse Attention with Zero-Shot Length Extrapolation](https://arxiv.org/abs/2610.17191v1) | 2610.17191v1 | 1 |
| 2026-10-12 | [SuPER-Mamba: Surprisal Prioritization for Extended-Context Routing in Mamba](https://arxiv.org/abs/2610.16636v1) | 2610.16636v1 | 6 |
| 2026-10-12 | [AeroChem: Closed-loop Physics-Informed State Space Modeling for Long-term Chemically-Reactive Air Quality Forecasting--Extended Version](https://arxiv.org/abs/2610.16630v1) | 2610.16630v1 | 6 |
| 2026-10-12 | [Hardware-Friendly Token-Group Activation Quantization for Low-Bit Mamba Super-Resolution](https://arxiv.org/abs/2610.16261v1) | 2610.16261v1 | 6 |
| 2026-10-11 | [History Replays Itself: Unleashing Long-Context Capability in Linear Attention](https://arxiv.org/abs/2610.15715v1) | 2610.15715v1 | 3 |
| 2026-10-11 | [Preserving Updates in Low-Bit Recurrent State Quantization](https://arxiv.org/abs/2610.15709v1) | 2610.15709v1 | 3 |
| 2026-10-10 | [scHFBiMamba: a bidirectional Mamba autoencoder for cardiac disease-state classification from single-nucleus RNA-seq data](https://arxiv.org/abs/2610.15117v1) | 2610.15117v1 | 6 |
| 2026-10-09 | [Deep learning from a control vantage point](https://arxiv.org/abs/2610.14385v1) | 2610.14385v1 | 0 |
| 2026-10-09 | [The RNN Homunculus: Learning to Gate Long-Term Memory](https://arxiv.org/abs/2610.14279v1) | 2610.14279v1 | 0 |
| 2026-10-09 | [ReplaySSM: Cache SSM Inputs, Not State](https://arxiv.org/abs/2610.13778v1) | 2610.13778v1 | 0 |
| 2026-10-09 | [State-Isolated Vision Mamba via Update-Tendency Routing for Underwater Image Enhancement](https://arxiv.org/abs/2610.13720v1) | 2610.13720v1 | 6 |
| 2026-10-09 | [Understanding Mamba-3 Through Oscillatory Dynamics](https://arxiv.org/abs/2610.13341v1) | 2610.13341v1 | 6 |
| 2026-10-09 | [Selective Spatio-Temporal Fruit Inspector (S$^2$FI): A Mamba-based Framework for Rotational Fruit Quality Assessment](https://arxiv.org/abs/2610.12868v1) | 2610.12868v1 | 6 |
| 2026-10-09 | [Time Delay System for Sequence Modeling](https://arxiv.org/abs/2610.12864v1) | 2610.12864v1 | 3 |
| 2026-10-08 | [Bridging Human and Model Attention: Explainability Analysis of CNN, Mamba, and ViT Architectures with Gaze-Based Validation](https://arxiv.org/abs/2610.12703v1) | 2610.12703v1 | 6 |
| 2026-10-08 | [V-CoLA: Vision Token Compression with Linear Attention](https://arxiv.org/abs/2610.11251v2) | 2610.11251v2 | 3 |
| 2026-10-07 | [HAN-Mamba: Hierarchical Selective State Space Networks for Multi-Scale Financial Volatility Forecasting](https://arxiv.org/abs/2610.10323v1) | 2610.10323v1 | 9 |
| 2026-10-07 | [GeoPrior-Mamba: Structured Process Priors with Mamba for Fine-Resolution XCO2 Reconstruction](https://arxiv.org/abs/2610.09456v1) | 2610.09456v1 | 6 |
| 2026-10-06 | [Lyapunov-Inspired LyRIC Activation and GLARE Attention in Chaos-Guided State Space Modeling for EMG-To-Speech (ETS) Synthesis](https://arxiv.org/abs/2610.09225v1) | 2610.09225v1 | 6 |
| 2026-10-06 | [MaRK: Markov-adapted Recurrent Kernels for Dynamic Operator Conditioning in State Space Models](https://arxiv.org/abs/2610.09092v3) | 2610.09092v3 | 9 |
| 2026-10-05 | [WaveGSSM: Graph Wave State Space Models for Propagating Spatio-Temporal Patterns](https://arxiv.org/abs/2610.06540v1) | 2610.06540v1 | 6 |
| 2026-10-05 | [Weave Mamba Fusion: Global Cross-Scale Interaction for Lightweight Face Detection](https://arxiv.org/abs/2610.05865v1) | 2610.05865v1 | 10 |
| 2026-10-05 | [LocAttMamba: A Low-Complexity Mamba Framework with Attention-Based Multi-AP Fusion for Indoor Localization](https://arxiv.org/abs/2610.05673v1) | 2610.05673v1 | 8 |
| 2026-10-04 | [TIRMamba: A Thermal-Prior-Modulated State-Space Network for Sub-Million-Parameter Infrared Image Super-Resolution](https://arxiv.org/abs/2610.05182v1) | 2610.05182v1 | 6 |
| 2026-10-04 | [LogSig-SSM: Time-Series Modelling with Multi-Scale Log-Signature Compression for State-Space Models](https://arxiv.org/abs/2610.05051v1) | 2610.05051v1 | 6 |
| 2026-10-02 | [PhysMamba: Selective State Space Models as Learned Articulated Body Simulators](https://arxiv.org/abs/2610.04014v1) | 2610.04014v1 | 15 |
| 2026-10-02 | [Bounded Reachability & Jailbreak Detection via Contraction-Constrained State Space Models](https://arxiv.org/abs/2610.02853v1) | 2610.02853v1 | 10 |
| 2026-10-02 | [Distributed Learning with Selective State Space Models: Architecture-Aware Convergence Analysis](https://arxiv.org/abs/2610.02659v2) | 2610.02659v2 | 18 |
| 2026-10-01 | [Learning Rate Transfer for Hybrid Transformer-SSM Architectures](https://arxiv.org/abs/2610.01172v2) | 2610.01172v2 | 8 |
| 2026-09-30 | [MEG-Mamba: A Scalable State-Space Foundation Model for Magnetoencephalography](https://arxiv.org/abs/2610.00746v1) | 2610.00746v1 | 6 |
| 2026-09-30 | [State-Space Unlearning for Non-Stationary Bias in Land Surface Forecasting](https://arxiv.org/abs/2610.02248v1) | 2610.02248v1 | 8 |
| 2026-09-30 | [Low-Discrepancy Dither for Quantized Recurrent State Caches](https://arxiv.org/abs/2609.39185v1) | 2609.39185v1 | 7 |
| 2026-09-29 | [Sequence Models for Layer-3 Protocol Emulation](https://arxiv.org/abs/2609.37697v1) | 2609.37697v1 | 8 |
| 2026-09-29 | [Physics-Informed State Space Models for Day-Ahead Photovoltaic Power Forecasting](https://arxiv.org/abs/2610.14014v1) | 2610.14014v1 | 12 |
| 2026-09-29 | [Channel-Dependent State Space Model for Multivariate Time Series Forecasting](https://arxiv.org/abs/2609.36453v2) | 2609.36453v2 | 6 |
| 2026-09-28 | [Fractional State Space Transition for Long Sequence Modeling](https://arxiv.org/abs/2609.36314v1) | 2609.36314v1 | 9 |
| 2026-09-28 | [CyFA: Linear Sequence Modeling with Relative-Time-Partitioned Memory](https://arxiv.org/abs/2609.36259v1) | 2609.36259v1 | 8 |
| 2026-09-28 | [DR-net-Mamba: Selective State-Space Modeling for Long-Range ECG Time-Series Denoising](https://arxiv.org/abs/2609.35634v1) | 2609.35634v1 | 6 |
| 2026-09-28 | [Riccati State Space Models: Non-iterative Parallelization for Nonlinear Sequence Modeling](https://arxiv.org/abs/2609.35441v1) | 2609.35441v1 | 11 |
| 2026-09-28 | [ReCAT: Remember, Count, and Time: Structured Recurrent Memory for Robot Manipulation](https://arxiv.org/abs/2609.35200v1) | 2609.35200v1 | 9 |
| 2026-09-28 | [Coordinated Lane-Level Variable Speed Limits and Ramp Metering for Successive Weaving Segments Considering Merging/Diverging Risks: A Hybrid Model Predictive Control and Multi-Agent Reinforcement Learning Approach](https://arxiv.org/abs/2609.35152v1) | 2609.35152v1 | 6 |
| 2026-09-28 | [MASCIT: A Mask-Aware State Space Classifier for Naturally Irregular Time Series](https://arxiv.org/abs/2609.34409v2) | 2609.34409v2 | 6 |
| 2026-09-27 | [3D Point Tracking with State Space Models](https://arxiv.org/abs/2609.34035v1) | 2609.34035v1 | 12 |
| 2026-09-27 | [ADPTNet: Adaptive with Prescriptive Timescales Non-Linear SSM for Sequence Modelling](https://arxiv.org/abs/2609.34034v1) | 2609.34034v1 | 8 |
| 2026-09-27 | [TopoMamba: A Load-Support Relation-Guided Multi-Directional State-Space Model for Topology Optimization](https://arxiv.org/abs/2609.33688v1) | 2609.33688v1 | 6 |
| 2026-09-27 | [SchemaMem: Schema-Indexed Recurrent Memory for Delayed State Retrieval](https://arxiv.org/abs/2609.33436v1) | 2609.33436v1 | 11 |
| 2026-09-27 | [StarBOA: Real-Time Mamba State-Space Unrolling for Sparse Radar Micro-Doppler in ISAC Networks](https://arxiv.org/abs/2609.33408v1) | 2609.33408v1 | 6 |
| 2026-09-27 | [SketchSSM: Write to the Full State, Read from a Compact Sketch](https://arxiv.org/abs/2609.33051v2) | 2609.33051v2 | 8 |
| 2026-09-26 | [RIPE-MambaSpike: Resolution-Independent Spiking-State-Space Interfaces for Parameter-Efficient Event-Based Vision](https://arxiv.org/abs/2609.32537v2) | 2609.32537v2 | 10 |
| 2026-09-26 | [Elastic Selective Spectral Hybrids for Train-Once, Export-Many Budgeted Inference](https://arxiv.org/abs/2609.32486v1) | 2609.32486v1 | 10 |
| 2026-09-26 | [DRAM: Delta-rule Recurrent Associative Memory for Robot Manipulation Policies](https://arxiv.org/abs/2609.32453v2) | 2609.32453v2 | 9 |
| 2026-09-26 | [Length-Independent State Tracking Under a Parallel Scan](https://arxiv.org/abs/2609.32447v1) | 2609.32447v1 | 8 |
| 2026-09-26 | [Residual Streams Read, Recurrent States Remember: The Global Workspace in Mamba Models](https://arxiv.org/abs/2609.32102v1) | 2609.32102v1 | 9 |
| 2026-09-25 | [Quantizing Looped Transformers: Feedback Exposure and Calibration Blindness](https://arxiv.org/abs/2609.30820v1) | 2609.30820v1 | 6 |
| 2026-09-24 | [Selective state space model for photon energy estimation in microwave kinetic inductance detectors](https://arxiv.org/abs/2609.30382v2) | 2609.30382v2 | 13 |
| 2026-09-24 | [Physics and Data Driven Transformer-Mamba Framework for Flow Field](https://arxiv.org/abs/2609.29087v2) | 2609.29087v2 | 6 |
| 2026-09-23 | [BiMamba2 Masked Discrete-Unit Prediction for Multilingual Speech Representation for Unsupervised Speech in the Wild Challenge](https://arxiv.org/abs/2609.28758v1) | 2609.28758v1 | 6 |
| 2026-09-23 | [Token Clustering and Semantic Sequence Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2609.28580v1) | 2609.28580v1 | 10 |
| 2026-09-23 | [Non-Commutative State Tracking with Input-Dependent Low-Rank Updates in Mamba-3](https://arxiv.org/abs/2609.28273v2) | 2609.28273v2 | 6 |
| 2026-09-23 | [Mamba-Family State-Space Model Kernels on a Programmable CGLA](https://arxiv.org/abs/2609.27437v1) | 2609.27437v1 | 8 |
| 2026-09-23 | [When Labels Are Scarce: An Oscillatory State Space Model for Vibration Diagnosis](https://arxiv.org/abs/2609.27411v1) | 2609.27411v1 | 6 |
| 2026-09-22 | [Temporally Ordered Region-Token Mamba with Logit-Space Diffusion for Remote Sensing Change Detection](https://arxiv.org/abs/2609.27149v1) | 2609.27149v1 | 6 |
| 2026-09-22 | [AI-Enabled Wireless Propagation Modeling and Radio Environment Maps for 5G Aerial Wireless Networks](https://arxiv.org/abs/2609.27083v1) | 2609.27083v1 | 6 |
| 2026-09-22 | [MambaVoice: Lightweight Audiovisual Singing Voice Separation Via A Hybrid Mamba-Transformer Model](https://arxiv.org/abs/2609.26635v1) | 2609.26635v1 | 12 |
| 2026-09-22 | [SE-MSB: End-to-End Unpaired Speech Enhancement using Mamba Schrödinger Bridges](https://arxiv.org/abs/2609.26000v1) | 2609.26000v1 | 6 |
| 2026-09-22 | [Point Diffusion Mamba: Unified Diffusion-State-Space Modeling for Single-View 3D Reconstruction under Data Scarcity](https://arxiv.org/abs/2609.25538v1) | 2609.25538v1 | 6 |
| 2026-09-21 | [CMAMBADEPTH: Self-supervised Monocular Depth Estimation with Channel Mamba and Hybrid Attention](https://arxiv.org/abs/2609.24494v1) | 2609.24494v1 | 6 |
| 2026-09-21 | [Pharmacokinetic State Space Models for Unbiased Prediction of Haemodynamic Collapse](https://arxiv.org/abs/2609.24338v1) | 2609.24338v1 | 10 |
| 2026-09-21 | [LiAuto-MindViT: A Hybrid Vision Backbone with Adaptive Bidirectional Mamba](https://arxiv.org/abs/2609.24337v2) | 2609.24337v2 | 8 |
| 2026-09-21 | [H-Spec: Parallel Speculative Decoding Without a Drafter-Side KV Cache](https://arxiv.org/abs/2609.24197v1) | 2609.24197v1 | 6 |
| 2026-09-21 | [U-PEN Mamba: Progressive Expansion with Selective State-Space Modeling for Efficient Retinal Vessel Segmentation](https://arxiv.org/abs/2609.24049v1) | 2609.24049v1 | 6 |
| 2026-09-19 | [HDMamba-YOLO: Efficient State-Space Perception and Local Spatial Reconstruction for UAV Small Object](https://arxiv.org/abs/2609.23061v1) | 2609.23061v1 | 6 |
| 2026-09-18 | [PointLAM: Local Attentive Mamba for Efficient Point-based 3D Object Detection](https://arxiv.org/abs/2609.21780v1) | 2609.21780v1 | 8 |
| 2026-09-18 | [Dual-Interest Sequential Product Recommendation With Multi-Granular SSM](https://arxiv.org/abs/2609.21548v1) | 2609.21548v1 | 8 |
| 2026-09-18 | [WS-NeRF: A Mamba-Driven World-State-Aware Adaptive Deblurring Neural Radiance Field](https://arxiv.org/abs/2609.21391v1) | 2609.21391v1 | 6 |
| 2026-09-18 | [S3VD: Semantic-Guidance Spatio-Temporal Scanning for Video Deraining](https://arxiv.org/abs/2609.21322v1) | 2609.21322v1 | 8 |
| 2026-09-16 | [Conditionally linear, matrix normal state space models](https://arxiv.org/abs/2609.18734v1) | 2609.18734v1 | 6 |
| 2026-09-16 | [SG-Mamba: Sparse Graph-Guided Mamba for Audio-Visual Speech Enhancement](https://arxiv.org/abs/2609.18009v2) | 2609.18009v2 | 6 |
| 2026-09-16 | [The Attention Within: Consensus Dynamics in Selective State Space Models](https://arxiv.org/abs/2609.17997v1) | 2609.17997v1 | 15 |
| 2026-09-15 | [Long-Context Demonstration Selection Using State Space Models](https://arxiv.org/abs/2609.17888v1) | 2609.17888v1 | 6 |
| 2026-09-15 | [QART: A Quantum-Classical Hybrid Architecture for Long-Horizon Reasoning -- Exploring a Conditional Path toward Quantum Scaling](https://arxiv.org/abs/2609.16887v1) | 2609.16887v1 | 6 |
| 2026-09-15 | [Channel-Wise and Token-Aware Post-Training Quantization for Visual State Space Duality](https://arxiv.org/abs/2609.16656v1) | 2609.16656v1 | 8 |
| 2026-09-15 | [On the Importance of Gating: Memorization vs. In-Context Learning in State Space Models](https://arxiv.org/abs/2609.16540v1) | 2609.16540v1 | 11 |
| 2026-09-14 | [Anatomy of Associative Recall in Fixed-State Recurrences: A Matched-State Decomposition, an Interference Wall, and a Curriculum That Breaks It](https://arxiv.org/abs/2609.16183v1) | 2609.16183v1 | 8 |
| 2026-09-14 | [MambaMPD: A Mamba-Driven Segmentation Framework for Marine Pollution Detection from Remote Sensing Imagery](https://arxiv.org/abs/2609.15676v1) | 2609.15676v1 | 6 |
| 2026-09-12 | [YOLO12-MambaScan: An Efficient Object Detector with High-Frequency Enhancement and State-Space Modeling](https://arxiv.org/abs/2609.13647v1) | 2609.13647v1 | 6 |
| 2026-09-11 | [SCDM: Spatial-Contextual Disentanglement Mamba via Differential Inference for Efficient Image Classification](https://arxiv.org/abs/2609.12825v2) | 2609.12825v2 | 10 |
| 2026-09-11 | [An Ultra-Widefield Swept-Source OCTA Dataset and a Polar-Gated Mamba Network for Retinal Vessel Segmentation](https://arxiv.org/abs/2609.12574v1) | 2609.12574v1 | 10 |
| 2026-09-10 | [SSEMG-Net: A Spectrogram-Based Mamba Network for Surface Electromyography Denoising](https://arxiv.org/abs/2609.11663v1) | 2609.11663v1 | 6 |
| 2026-09-10 | [A Dataset and Model for Imputing Water Surface Elevation on a Large and Extremely Sparse Spatiotemporal Graph](https://arxiv.org/abs/2609.11580v2) | 2609.11580v2 | 6 |
| 2026-09-10 | [RAMamba-Net: A Reliability-Aware and Mamba-Based Multimodal Fusion Network for Auditory Attention Detection](https://arxiv.org/abs/2609.11372v1) | 2609.11372v1 | 6 |
| 2026-09-08 | [Global Divergence, Local Convergence: Representation Geometry in SSMs and Transformers](https://arxiv.org/abs/2609.08692v1) | 2609.08692v1 | 8 |
| 2026-09-08 | [Online Signature Verification Using Augmented Path Signature and T-Mamba](https://arxiv.org/abs/2609.08276v1) | 2609.08276v1 | 10 |
| 2026-09-07 | [MamMA: A Mamba-Based Pedestrian Trajectory Prediction Algorithm Considering Occupancy Map and Pedestrian Awareness States](https://arxiv.org/abs/2609.08041v1) | 2609.08041v1 | 6 |
| 2026-09-07 | [On the Recall Scaling Laws in Mamba: A Theoretical and Mechanistic Study via Hashing](https://arxiv.org/abs/2609.07681v1) | 2609.07681v1 | 6 |
| 2026-09-07 | [AF-Mamba: Efficient Long-Term Signal Modeling for Early Prediction of Atrial Fibrillation Onset](https://arxiv.org/abs/2609.06984v1) | 2609.06984v1 | 10 |
| 2026-09-06 | [PPIM: Pennes Physics-Informed Mamba for Heat-Source-Conditioned 3D Bioheat Simulation](https://arxiv.org/abs/2609.06869v1) | 2609.06869v1 | 6 |
| 2026-09-04 | [BEAM3R: Beam's-eye-view architecture with Mamba-3 for implicit dose reconstruction](https://arxiv.org/abs/2609.04747v1) | 2609.04747v1 | 6 |
| 2026-09-03 | [Why Gated DeltaNet Survives 4-Bit Quantization: NVFP4 W4A4 for the Recurrent Half of a Hybrid 27B LLM](https://arxiv.org/abs/2609.04098v1) | 2609.04098v1 | 9 |
| 2026-09-03 | [Semantic-Aware Subgraph State Space Model for WSI Classification in Histopathology](https://arxiv.org/abs/2609.03689v1) | 2609.03689v1 | 10 |
| 2026-09-01 | [A Dataset for Modeling Iterative Problem-Solving](https://arxiv.org/abs/2609.00940v2) | 2609.00940v2 | 6 |
| 2026-08-31 | [DASC: Decay-Aware State Compression for Hybrid Linear-Attention Serving](https://arxiv.org/abs/2608.30386v2) | 2608.30386v2 | 6 |
| 2026-08-30 | [A Hybrid State-Space Approach for Census-Tract Population Estimation](https://arxiv.org/abs/2608.30094v1) | 2608.30094v1 | 8 |
| 2026-08-30 | [GraM-Diff: A Unified Graph-Mamba Diffusion Framework for EEG-Based Alzheimer's Disease Data Generation and Diagnosis](https://arxiv.org/abs/2608.29755v1) | 2608.29755v1 | 6 |
| 2026-08-30 | [ButterMamba: Butterworth-Enhanced Spatial-Temporal Mamba for Efficient Traffic Flow Prediction](https://arxiv.org/abs/2608.29658v1) | 2608.29658v1 | 10 |
| 2026-08-30 | [SPLG-Mamba: Structure-Preserving Local-Global Mamba Network for Salient Object Detection in Optical Remote Sensing Images](https://arxiv.org/abs/2608.29626v1) | 2608.29626v1 | 6 |
| 2026-08-28 | [Multirate State Space Models for End-to-End Processing of Pulse Density Modulated Speech Signals](https://arxiv.org/abs/2608.28472v1) | 2608.28472v1 | 6 |
| 2026-08-28 | [Causal Non-causal State Space Models and the Modelling of Financial Bubbles](https://arxiv.org/abs/2608.28115v1) | 2608.28115v1 | 6 |
| 2026-08-28 | [PhyMamba: Physics-Modulated Mamba for Robust Battery Health Prognostics](https://arxiv.org/abs/2608.27978v1) | 2608.27978v1 | 6 |
| 2026-08-28 | [SOMTab: Set-Order Mamba for Efficient Tabular In-Context Learning](https://arxiv.org/abs/2608.27882v1) | 2608.27882v1 | 6 |
| 2026-08-27 | [Cross-Architecture Knowledge Distillation from a Vision Foundation Model to a Lightweight Visual State Space Model for Tea Leaf Disease Classification](https://arxiv.org/abs/2608.26771v1) | 2608.26771v1 | 6 |
| 2026-08-27 | [FU-Mamba: A Frequency-Enhanced Dynamic Scanning Framework for Oralscan Image Segmentation](https://arxiv.org/abs/2608.26607v1) | 2608.26607v1 | 10 |
| 2026-08-26 | [Uncertainty and Business-Aware Remaining Useful Life Estimation for Semiconductor Manufacturing](https://arxiv.org/abs/2609.22160v2) | 2609.22160v2 | 6 |
| 2026-08-26 | [CrossMambaTuning: Synergistic Spatial and Cross-Layer Adaptation for Machine Vision Compression](https://arxiv.org/abs/2608.25568v1) | 2608.25568v1 | 10 |
| 2026-08-25 | [Multi-View Trust Evaluation for Collaborator Selection via Evidential Deep Learning](https://arxiv.org/abs/2608.25235v1) | 2608.25235v1 | 6 |
| 2026-08-25 | [Long-Term Behavioral Evaluation for Trusted Collaborator Selection via Bidirectional Mamba](https://arxiv.org/abs/2608.25232v1) | 2608.25232v1 | 6 |
| 2026-08-25 | [BanglaMamba: Exploring State Space Models for Bangla Fake News Detection](https://arxiv.org/abs/2608.25190v1) | 2608.25190v1 | 12 |
| 2026-08-25 | [Strictly Causal Streaming Video Anomaly Detection with a Theoretically-Grounded State-Space Core](https://arxiv.org/abs/2608.24810v1) | 2608.24810v1 | 8 |
| 2026-08-25 | [SeisMamba: Low-Latency Single-Station Seismic Magnitude Estimation for Spatially Distributed Earthquake Early Warning](https://arxiv.org/abs/2608.24561v1) | 2608.24561v1 | 6 |
| 2026-08-24 | [What a Cross-Model Fixed-Point Census Can and Cannot Arbitrate About Repetition](https://arxiv.org/abs/2609.29507v1) | 2609.29507v1 | 8 |
| 2026-08-24 | [Following Motion for Sequential Modeling in Video Frame Interpolation](https://arxiv.org/abs/2608.22861v1) | 2608.22861v1 | 12 |
| 2026-08-22 | [SSDi8: Accurate and Efficient 8-bit Quantization for State Space Duality](https://arxiv.org/abs/2608.21952v1) | 2608.21952v1 | 8 |
| 2026-08-21 | [Exact Rejection Sampling for Non-Gaussian State Space Models](https://arxiv.org/abs/2608.21619v1) | 2608.21619v1 | 6 |
| 2026-08-21 | [Tydra: An Efficient Hybrid Model for Tabular Data](https://arxiv.org/abs/2608.21199v1) | 2608.21199v1 | 8 |
| 2026-08-21 | [TreeWY: Speculative Verification for Gated DeltaNet Hybrids](https://arxiv.org/abs/2608.20961v2) | 2608.20961v2 | 8 |
| 2026-08-20 | [Keyed Provenance Watermarking with Complementary Lattice-Based Secure Aggregation for Federated Learning](https://arxiv.org/abs/2608.20580v1) | 2608.20580v1 | 6 |
| 2026-08-20 | [Energy-Mamba: A Physics-Constrained State-Space Model for Medical Image Classification](https://arxiv.org/abs/2608.19813v1) | 2608.19813v1 | 7 |
| 2026-08-20 | [DAVSS: Distilled Audio-Visual State Space Models](https://arxiv.org/abs/2608.19523v1) | 2608.19523v1 | 6 |
| 2026-08-18 | [RetiWave-Mamba: A Dual-Stream Network for Retinal Disease Detection based on Multi-scale Context and Feature-Adaptive Mamba Projection](https://arxiv.org/abs/2608.17623v2) | 2608.17623v2 | 10 |
| 2026-08-18 | [TEAMS: Text-prompted spatiotEmporal dual-heAd Mamba Snake](https://arxiv.org/abs/2608.17421v1) | 2608.17421v1 | 10 |
| 2026-08-17 | [SIGMA-Lane: Scale-pyramId Gated MAmba for Temporally Consistent Video Lane Detection](https://arxiv.org/abs/2608.16338v1) | 2608.16338v1 | 12 |
| 2026-08-16 | [CardiacMamba: Fair and Robust RGB-RF Fusion for Remote Heart Rate Estimation via State Space Modeling](https://arxiv.org/abs/2608.15831v1) | 2608.15831v1 | 12 |
| 2026-08-15 | [A Unified Mamba--MoE Surrogate for Closed-Loop Simulation and Measurement-Window Forecasting of Inverter Transients](https://arxiv.org/abs/2608.15051v1) | 2608.15051v1 | 6 |
| 2026-08-14 | [CSG-Mamba: A Convolutional Scoring Gating Vision State Space Network for Endoscopic Polyp Segmentation](https://arxiv.org/abs/2608.14146v1) | 2608.14146v1 | 10 |
| 2026-08-14 | [KHiM-Mamba: Injecting Pathology Knowledge into Mamba via Hidden-State Modulation for Whole Slide Image Analysis](https://arxiv.org/abs/2608.14757v1) | 2608.14757v1 | 8 |
| 2026-08-13 | [Graph-MambaNav: Spatial-Temporal Graph Mamba Leveraging Object-Relation Knowledge for Object-Goal Navigation](https://arxiv.org/abs/2608.13723v1) | 2608.13723v1 | 8 |
| 2026-08-12 | [Apnea Burden-Guided Framework: Enhancing Out-of-Distribution Generalization in PPG-Based Sleep Apnea Characterization](https://arxiv.org/abs/2608.12229v1) | 2608.12229v1 | 6 |
| 2026-08-12 | [RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation](https://arxiv.org/abs/2608.12099v2) | 2608.12099v2 | 8 |
| 2026-08-11 | [Social Graph Mamba: Forecasting Pedestrian Movements Based on Social Context](https://arxiv.org/abs/2608.21411v1) | 2608.21411v1 | 12 |
| 2026-08-11 | [Secure Cooperative THz ISAC via Mamba Empowered Graph Neural Network Precoding](https://arxiv.org/abs/2608.10467v1) | 2608.10467v1 | 10 |
| 2026-08-10 | [ChronoSSM: Training for Temporally Aware Representations in Autoregressive State Space Models](https://arxiv.org/abs/2608.10120v1) | 2608.10120v1 | 6 |
| 2026-08-10 | [Mamba-based Selective State Space Modeling Improves the Accuracy-Complexity Tradeoff of SmolVLA Vision-Language-Action Experts](https://arxiv.org/abs/2608.21407v1) | 2608.21407v1 | 15 |
| 2026-08-08 | [Causal State-Space Model for Causal Inference: Estimating Longitudinal Individual Treatment Effects](https://arxiv.org/abs/2608.08288v2) | 2608.08288v2 | 6 |
| 2026-08-08 | [AraSSM: A bidirectional state-space encoder for Arabic masked language modeling](https://arxiv.org/abs/2608.08256v1) | 2608.08256v1 | 7 |
| 2026-08-08 | [PE-Mamba: Bidirectional Selective Layer Aggregation for AI-Generated Image Detection](https://arxiv.org/abs/2608.07999v1) | 2608.07999v1 | 6 |
| 2026-08-07 | [Phase State Space Models: Parallel, Surrogate-Free Training of Spiking Networks](https://arxiv.org/abs/2608.07754v1) | 2608.07754v1 | 8 |
| 2026-08-06 | [Hybrid Machine Learning Framework for Herd-Level Cattle Growth Pattern and Weight Gain Forecasting in Grazing-Based Production Systems](https://arxiv.org/abs/2608.06001v1) | 2608.06001v1 | 6 |
| 2026-08-04 | [Muon Meets Mamba: Spectral Optimization for State Space Models](https://arxiv.org/abs/2608.03941v1) | 2608.03941v1 | 12 |
| 2026-08-04 | [Lightweight 3D Object Detection via Mamba-Based Knowledge Distillation](https://arxiv.org/abs/2608.03490v1) | 2608.03490v1 | 9 |
| 2026-08-04 | [State Propagation Also Satisfies: A Complex-Valued State-Space Model for Deterministic State Tracking](https://arxiv.org/abs/2608.03425v3) | 2608.03425v3 | 6 |
| 2026-08-03 | [LowRank-SSM: Hardware-Software Co-Design for Rank-Reduced Mamba Acceleration on FPGA](https://arxiv.org/abs/2608.02954v2) | 2608.02954v2 | 11 |
| 2026-08-03 | [USP-Mamba: Unmixing-Derived Spectral and Structural Prompting for Hyperspectral Image Super-Resolution](https://arxiv.org/abs/2608.02401v1) | 2608.02401v1 | 8 |
| 2026-08-03 | [Loop-Mamba: A Loop Mamba with Degradation-Aware and Shared Memory for Old Photo Restoration](https://arxiv.org/abs/2608.02346v3) | 2608.02346v3 | 8 |
| 2026-08-03 | [PNEC-Mamba: Prototype-Guided Positive-Negative Evidence Calibration for Hyperspectral Image Classification](https://arxiv.org/abs/2608.01910v1) | 2608.01910v1 | 6 |
| 2026-08-02 | [State space modeling of RLC ladder circuits](https://arxiv.org/abs/2608.01051v1) | 2608.01051v1 | 6 |
| 2026-07-31 | [CoDe-SSM: Context-Detail Decoupled State Space Model for Efficient UHD Image Restoration](https://arxiv.org/abs/2607.29595v1) | 2607.29595v1 | 6 |
| 2026-07-30 | [A Unified Benchmark of Deep Learning Models for Multi-task 3D Brain Tumor Segmentation from Magnetic Resonance Imaging](https://arxiv.org/abs/2607.28858v1) | 2607.28858v1 | 8 |
| 2026-07-30 | [MSCM-net: A hyperspectral image classiffcation method based on multi-scale convolution and Mamba](https://arxiv.org/abs/2607.28277v1) | 2607.28277v1 | 8 |
| 2026-07-30 | [SPFM-Net: Semantic-Prior-Guided Frequency-Constrained Mamba for Invisible Watermark Attack](https://arxiv.org/abs/2607.27811v1) | 2607.27811v1 | 6 |
| 2026-07-29 | [Phoneme- vs. Character-Level Targets and Selective State-Space Models for Intracortical Brain-to-Text](https://arxiv.org/abs/2607.26751v1) | 2607.26751v1 | 6 |
| 2026-07-28 | [Raven: High-Recall Sequence Modeling with Sparse Memory Routing](https://arxiv.org/abs/2607.25357v1) | 2607.25357v1 | 8 |
| 2026-07-27 | [LCMamNet: A Lightweight Cross-scale Mamba Network for Infrared Small Target Detection](https://arxiv.org/abs/2607.24184v1) | 2607.24184v1 | 6 |
| 2026-07-26 | [Direction-adaptive Mamba: Spatial-Frequency Dual-Domain Collaborative Learning for PolSAR Image Classification](https://arxiv.org/abs/2607.23464v1) | 2607.23464v1 | 6 |
| 2026-07-26 | [Multi-Modal Object Re-Identification with Prompt-S6 and Semantic-Aware Knowledge Guidance](https://arxiv.org/abs/2607.23451v1) | 2607.23451v1 | 6 |
| 2026-07-24 | [Disentangling Multi-View Scanning in Mamba for Network Traffic Anomaly Detection](https://arxiv.org/abs/2607.22829v1) | 2607.22829v1 | 9 |
| 2026-07-24 | [HEMERA: A Heterogeneous Memory-Centric Accelerator with Recursive Dataflow for Edge-Constrained State-Space-Duality Models Inference](https://arxiv.org/abs/2607.22022v1) | 2607.22022v1 | 10 |
| 2026-07-23 | [Naju: A Native Discrete State-Space Model with Independent Retention and Writing for Long-Sequence Memory](https://arxiv.org/abs/2607.21000v1) | 2607.21000v1 | 7 |
| 2026-07-22 | [User-Centric Modeling of Transactional Sequences with Explainable State Space Models](https://arxiv.org/abs/2607.20228v1) | 2607.20228v1 | 10 |
| 2026-07-22 | [Physics-Aware Complex-Valued State Space Model with Scattering-Prior Feature Modulation for PolSAR Image Classification](https://arxiv.org/abs/2607.19787v1) | 2607.19787v1 | 6 |
| 2026-07-21 | [Selective State-Space Adaptation and Retrieval for Language Model Reasoning](https://arxiv.org/abs/2607.19326v3) | 2607.19326v3 | 6 |
| 2026-07-21 | [DAMamba-UNet3D: A Parameter-Efficient Mamba State Space U-Net with Dynamic Adaptive Scan for 3D Medical Image Segmentation](https://arxiv.org/abs/2607.22718v1) | 2607.22718v1 | 6 |
| 2026-07-21 | [Black-Mamba: Biologically-Inspired Leaky Accumulation for Conceptual Knowledge under Distribution Drift](https://arxiv.org/abs/2607.18899v1) | 2607.18899v1 | 6 |
| 2026-07-21 | [Norm or Direction? Decoding Vision Mambas for High-Resolution Vision](https://arxiv.org/abs/2607.18625v1) | 2607.18625v1 | 12 |
| 2026-07-20 | [Adaptive Mamba Neural Operators](https://arxiv.org/abs/2607.18043v1) | 2607.18043v1 | 6 |
| 2026-07-20 | [MambaLSTM: A Spatio-Temporal Framework for Enhanced Traffic Accident Risk Prediction](https://arxiv.org/abs/2607.18353v1) | 2607.18353v1 | 6 |
| 2026-07-17 | [BCG-Former: Toward Pareto-Efficient Hyperspectral Image Classification via Band-Contextual Gating](https://arxiv.org/abs/2607.15639v1) | 2607.15639v1 | 6 |
| 2026-07-16 | [VideoSEMA: a scalable and efficient Mamba-like attention for video understanding](https://arxiv.org/abs/2607.14711v2) | 2607.14711v2 | 6 |
| 2026-07-15 | [DCVC-MB: Neural B-Frame Video Compression using State Space Models](https://arxiv.org/abs/2607.14305v1) | 2607.14305v1 | 10 |
| 2026-07-14 | [MambaPSA: A Mamba-based Replacement for C2PSA in YOLO26](https://arxiv.org/abs/2607.12681v1) | 2607.12681v1 | 10 |
| 2026-07-14 | [A Hybrid Mamba for Audio-Visual Navigation](https://arxiv.org/abs/2607.13110v1) | 2607.13110v1 | 8 |
| 2026-07-14 | [TSSM: Triaxial State Space Model for Global Station Weather Forecasting with Temporal-Variable-Historical Modeling](https://arxiv.org/abs/2607.13101v1) | 2607.13101v1 | 6 |
| 2026-07-14 | [StratMamba: Strategic and Reactive Stream Partitioning for Path-Efficient LiDAR-Based Obstacle Avoidance](https://arxiv.org/abs/2607.12370v1) | 2607.12370v1 | 6 |
| 2026-07-14 | [Motif-Mamba: network motif improved mamba for long-range sequence modeling](https://arxiv.org/abs/2608.00027v1) | 2608.00027v1 | 18 |
| 2026-07-13 | [Multi-Stage Mamba-Based Architecture for Fast and Scalable Superconducting Qubit Readout](https://arxiv.org/abs/2607.11668v1) | 2607.11668v1 | 8 |
| 2026-07-13 | [FAD-SA-GRU: Enhancing Hate Speech Detection in Algerian Dialect Through Feature-Augmented Self-Attention GRU Networks](https://arxiv.org/abs/2607.11279v1) | 2607.11279v1 | 8 |
| 2026-07-11 | [BAT-RM: A Boundary-Aware Transformer with Region-Aware Multi-Directional Mamba for Clinically Deployed Cervical Cancer Radiotherapy Auto-Contouring](https://arxiv.org/abs/2607.11949v1) | 2607.11949v1 | 11 |
| 2026-07-11 | [DSSMs: State Space Models with Explicit Memory via Delay Differential Equations](https://arxiv.org/abs/2607.10244v1) | 2607.10244v1 | 11 |
| 2026-07-11 | [CHASE: Cache-Hole-Adapted Skip Exit for Looped State-Space Language Models](https://arxiv.org/abs/2607.10110v2) | 2607.10110v2 | 6 |
| 2026-07-09 | [SCI-Mamba: Unsupervised Learning based Low-Light Image Enhancement for Non-Cooperative Spacecraft](https://arxiv.org/abs/2607.08033v4) | 2607.08033v4 | 6 |
| 2026-07-08 | [-8 dB SNR + 90% Packet Loss: MamVSC -- CSI-Guided Semantic Mamba for Extreme-Robust Video Semantic Communication](https://arxiv.org/abs/2607.07293v1) | 2607.07293v1 | 6 |
| 2026-07-08 | [FMMVCC: Fuzzy Mamba-based Multi-View Contrastive Clustering for Univariate Time Series](https://arxiv.org/abs/2607.07258v1) | 2607.07258v1 | 8 |
| 2026-07-06 | [Uncertainty-Aware Velocity Correction for Proprioceptive Vehicle Localization using Evidential Mamba](https://arxiv.org/abs/2607.05669v1) | 2607.05669v1 | 12 |
| 2026-07-06 | [RUFNet: Query-Guided Support Mask Refinement and Uncertainty Fusion based on Hybrid Mamba for Few-Shot Brain Tumor Segmentation](https://arxiv.org/abs/2607.05035v1) | 2607.05035v1 | 6 |
| 2026-07-06 | [Lightweight ML-Based Automatic Sleep Staging Framework with Constrained CNN and Mamba for Small-Sample EEG Datasets](https://arxiv.org/abs/2607.04934v1) | 2607.04934v1 | 6 |
| 2026-07-05 | [UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization](https://arxiv.org/abs/2607.04498v2) | 2607.04498v2 | 12 |
| 2026-07-03 | [Vision Non-Causal Trapezoidal Mamba: Eliminating Directional Scanning in Vision SSMs with Second-Order Dynamics](https://arxiv.org/abs/2607.03589v2) | 2607.03589v2 | 12 |
| 2026-07-03 | [DistillH-Mamba: A Hypergraph-Mamba-Based Knowledge Distillation Model for Efficient Impact Fall Detection](https://arxiv.org/abs/2607.03156v1) | 2607.03156v1 | 6 |
| 2026-07-03 | [MambaLIE: Scene Light Intensity-Boosted Low-Light Image Enhancement with State Space Model](https://arxiv.org/abs/2607.03013v2) | 2607.03013v2 | 12 |
| 2026-07-03 | [E-TraMamba: A New Paradigm for Efficient Long-Term 3D Feature Tracking with Event Cameras](https://arxiv.org/abs/2607.02866v1) | 2607.02866v1 | 6 |
| 2026-07-02 | [Dual-Selective Network for Domain-Incremental Change Detection](https://arxiv.org/abs/2607.02299v1) | 2607.02299v1 | 8 |
| 2026-07-02 | [QuantFlow: A Federated Mamba-Based Post-Transformer Foundation Model for Time-Series Forecasting](https://arxiv.org/abs/2607.02632v2) | 2607.02632v2 | 6 |
| 2026-07-01 | [From Monolingual to Multilingual: Evaluating Mamba for ASR in South African Languages](https://arxiv.org/abs/2607.01502v1) | 2607.01502v1 | 10 |
| 2026-07-01 | [Slope-Guided Mamba and Angular-Refined Transformer for Light Field Super-Resolution](https://arxiv.org/abs/2607.00965v1) | 2607.00965v1 | 8 |
| 2026-07-01 | [From Objectives to Applications: Aligning Architectural Biases in Audio Self-Supervised Learning](https://arxiv.org/abs/2607.00387v1) | 2607.00387v1 | 10 |
| 2026-06-30 | [Temporal Multi-Signal Fusion for Token-Level Hallucination Detection](https://arxiv.org/abs/2608.18115v1) | 2608.18115v1 | 6 |
| 2026-06-30 | [SAMBA: A Scatter-Guided Masked Bidirectional Mamba Foundation Model for SAR Target Recognition](https://arxiv.org/abs/2606.31668v2) | 2606.31668v2 | 6 |
| 2026-06-30 | [RCL-Mamba: A Dual-domain State Space Model for Measurement-oriented Image Restoration in Rotational Sparse-View Scanning Computed Laminography](https://arxiv.org/abs/2606.31353v2) | 2606.31353v2 | 12 |
| 2026-06-29 | [MuonSSM: Orthogonalizing State Space Models for Sequence Modeling](https://arxiv.org/abs/2606.30461v1) | 2606.30461v1 | 12 |
| 2026-06-29 | [Chronos: A Physics-Informed Full-History Framework for Non-Markovian Long-Horizon Manipulation](https://arxiv.org/abs/2606.30318v1) | 2606.30318v1 | 6 |
| 2026-06-29 | [Timesteps of Mamba Align with Human Reading Times](https://arxiv.org/abs/2606.29904v1) | 2606.29904v1 | 8 |
| 2026-06-29 | [SUMO: Segment and Track Any Motion with Nonlinear State Space Models](https://arxiv.org/abs/2606.29861v1) | 2606.29861v1 | 6 |
| 2026-06-28 | [AdaSurvMamba: Dynamic Fusion and Semantic Scanning for Multimodal Survival Analysis](https://arxiv.org/abs/2607.16260v1) | 2607.16260v1 | 8 |
| 2026-06-26 | [Improving Patient Subtyping on Longitudinal Data using Representations from Mamba-based Architecture](https://arxiv.org/abs/2606.28623v1) | 2606.28623v1 | 6 |
| 2026-06-26 | [MASS: Motion-Aligned Selective Scan for Refinement in Flow-Based Video Frame Interpolation](https://arxiv.org/abs/2606.27718v1) | 2606.27718v1 | 6 |
| 2026-06-25 | [Liquid Fusion of Heterogeneous Representations Towards General Salient Object Detection](https://arxiv.org/abs/2606.26849v1) | 2606.26849v1 | 8 |
| 2026-06-24 | [SSM Adapters via Hankel Reduced-order Modeling: Injection Site Determines Task Suitability in Long-Context Fine-Tuning](https://arxiv.org/abs/2606.26290v1) | 2606.26290v1 | 6 |
| 2026-06-24 | [Tracking the Turn: Mamba-Powered Human Orientation Detection using UWB](https://arxiv.org/abs/2606.26187v1) | 2606.26187v1 | 8 |
| 2026-06-24 | [State Space Models Meet Remote Sensing: A Survey](https://arxiv.org/abs/2606.25329v1) | 2606.25329v1 | 6 |
| 2026-06-24 | [Efficient Remote Sensing Instance Segmentation with Linear-Time State Space Distilled Visual Foundation Models](https://arxiv.org/abs/2606.25324v1) | 2606.25324v1 | 7 |
| 2026-06-23 | [MambaRaw: Selective State Space Modeling for Efficient 4K Raw Image Reconstruction](https://arxiv.org/abs/2606.24479v1) | 2606.24479v1 | 15 |
| 2026-06-22 | [Scaling State-Space Models from Lines to Paragraphs: An Ablation of Mamba-based OCR](https://arxiv.org/abs/2606.23524v1) | 2606.23524v1 | 9 |
| 2026-06-22 | [MambaADv2: Evolving Duality-enhanced State Space Model for Unsupervised Anomaly Detection](https://arxiv.org/abs/2606.23126v1) | 2606.23126v1 | 12 |
| 2026-06-22 | [Physics-Guided Spatiotemporal State Space Modeling for Lookahead Molten Pool Segmentation in Laser Wire-Feed Welding](https://arxiv.org/abs/2606.23028v1) | 2606.23028v1 | 10 |
| 2026-06-22 | [Learning Adaptive Dynamical Features via Multi-$τ$ Liquid-Mamba for All-in-one Image Restoration](https://arxiv.org/abs/2606.22801v1) | 2606.22801v1 | 12 |
| 2026-06-21 | [DR-Mamba: Automatic Inference-Time Domain Adaptation for Document Image Binarization via Sample-Conditioned Detail-Background Suppression](https://arxiv.org/abs/2606.22625v1) | 2606.22625v1 | 6 |
| 2026-06-19 | [MS-rPPG: Multi-spectral State Space Model for Remote Photoplethysmography in Driver Monitoring Systems](https://arxiv.org/abs/2606.21115v1) | 2606.21115v1 | 10 |
| 2026-06-19 | [Diffusion-Driven State Space Models](https://arxiv.org/abs/2606.21036v2) | 2606.21036v2 | 6 |
| 2026-06-18 | [Comparing Transformers and Hybrid Models at the Token Level](https://arxiv.org/abs/2606.20936v1) | 2606.20936v1 | 6 |
| 2026-06-18 | [U$^2$Mamba: A Two-level Nested U-structure Mamba for Salient Object Detection](https://arxiv.org/abs/2606.20282v1) | 2606.20282v1 | 6 |
| 2026-06-18 | [Spatial-Aware Reduction Framework: Towards Efficient and Faithful Visual State Space Models](https://arxiv.org/abs/2606.19932v1) | 2606.19932v1 | 10 |
| 2026-06-18 | [SL-S4Wave: Self-Supervised Learning of Physiological Waveforms with Structured State Space Models](https://arxiv.org/abs/2606.19888v2) | 2606.19888v2 | 8 |
| 2026-06-17 | [ITNet: A Learnable Integral Transform That Subsumes Convolution, Attention, and Recurrence](https://arxiv.org/abs/2606.19538v3) | 2606.19538v3 | 6 |
| 2026-06-17 | [An approach with Visual and Tabular Mamba to multimodal medical data using Mixed Fusion](https://arxiv.org/abs/2606.20738v1) | 2606.20738v1 | 10 |
| 2026-06-17 | [Leveraging Energy Features for Surface Classification with Deep Learning: A Comparative Analysis Across Three Independent Datasets](https://arxiv.org/abs/2606.18698v1) | 2606.18698v1 | 6 |
| 2026-06-17 | [MIDS: Detecting Stealthy Masquerade and Tampering Attacks on CAN Bus via Bidirectional Mamba](https://arxiv.org/abs/2606.18599v1) | 2606.18599v1 | 6 |
| 2026-06-16 | [Ternary Mamba: Grouped Quantization-Aware Training of W1.58A16 State Space Models](https://arxiv.org/abs/2606.18114v1) | 2606.18114v1 | 13 |
| 2026-06-16 | [S4oP: Operator-level Pruning of Structured State Space Models for Resource-Constrained Devices](https://arxiv.org/abs/2606.18096v2) | 2606.18096v2 | 6 |
| 2026-06-16 | [Reload-Mamba: Hierarchical Anti-Dilution State-Space Modeling for Multi-Class Semantic Segmentation](https://arxiv.org/abs/2606.17966v1) | 2606.17966v1 | 11 |
| 2026-06-16 | [MambaCount: Efficient Text-guided Open-vocabulary Object Counting with Spatial Sparse State Space Duality Block](https://arxiv.org/abs/2606.17650v1) | 2606.17650v1 | 6 |
| 2026-06-16 | [Memory-Efficient Meta-Reinforcement Learning for Adaptive Safety-Critical Control in Adversarial Spacecraft Proximity Operations](https://arxiv.org/abs/2606.17414v1) | 2606.17414v1 | 12 |
| 2026-06-15 | [Quantum Enchanced Multi-Scale CNN with Bi-directional Mamba for Crop Field Analysis](https://arxiv.org/abs/2606.17222v1) | 2606.17222v1 | 6 |
| 2026-06-15 | [Structure-aware Knowledge-guided Heterogeneous Mamba for Zygomaticomaxillary Suture Assessment](https://arxiv.org/abs/2606.16749v1) | 2606.16749v1 | 6 |
| 2026-06-15 | [Long-Context Modeling via GSS-Transformer Hybrid Architecture with Learnable Mixing](https://arxiv.org/abs/2606.16093v1) | 2606.16093v1 | 12 |
| 2026-06-14 | [MambAdapter: Lightweight Mamba-Based Adapters for Parameter-Efficient Transfer Learning in Speech and Audio](https://arxiv.org/abs/2606.15638v1) | 2606.15638v1 | 8 |
| 2026-06-13 | [Rethinking the Role of Efficient Attention in Hybrid Architectures](https://arxiv.org/abs/2606.15378v1) | 2606.15378v1 | 8 |
| 2026-06-12 | [Nemotron 3 Ultra: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2606.15007v1) | 2606.15007v1 | 6 |
| 2026-06-11 | [LongSpike: Fractional Order Spiking State Space Models for Efficient Long Sequence Learning](https://arxiv.org/abs/2606.12895v1) | 2606.12895v1 | 6 |
| 2026-06-10 | [On Subquadratic Architectures: From Applications to Principles](https://arxiv.org/abs/2606.12364v1) | 2606.12364v1 | 10 |
| 2026-06-10 | [Variational Deep Unfolding with Mamba-Based Nonlocal Modeling for Underwater Image Enhancement](https://arxiv.org/abs/2606.14781v1) | 2606.14781v1 | 6 |
| 2026-06-08 | [Graph Mamba Operator: A Latent Simulator for Interacting Particle Systems](https://arxiv.org/abs/2606.09432v1) | 2606.09432v1 | 6 |
| 2026-06-08 | [Vision-Language Guided Hyperspectral Object Tracking via Semantics Fusion and Contextual Template Updating](https://arxiv.org/abs/2606.09167v1) | 2606.09167v1 | 10 |
| 2026-06-07 | [Generalizing Geometry-Guided Mamba as a Plug-and-Play Context Module for CNN-based Semantic Segmentation](https://arxiv.org/abs/2606.08866v2) | 2606.08866v2 | 6 |
| 2026-06-07 | [DeepMine-Mamba: Mitigating Information Dilution in Mamba-Based State Space Models for Document Image Binarization](https://arxiv.org/abs/2606.08781v3) | 2606.08781v3 | 12 |
| 2026-06-06 | [SPDM: Geometry-Modulated State Space Modeling with Manifold Constraints for Time Series Forecasting](https://arxiv.org/abs/2606.09917v1) | 2606.09917v1 | 11 |
| 2026-06-06 | [A dual-system approach for epilepsy diagnosis: integrating mamba-Bi-LSTM architecture with SHAP-based verification](https://arxiv.org/abs/2606.08240v1) | 2606.08240v1 | 6 |
| 2026-06-06 | [CG-MambaNet: A spatiotemporal framework for cross-patient epileptic seizure prediction using CNN-GCN-Mamba-BiLSTM with event-level clinical evaluation](https://arxiv.org/abs/2606.08226v1) | 2606.08226v1 | 6 |
| 2026-06-05 | [C-MambaPose: Phase-Preserving Complex Mamba for Cross-Environment Wi-Fi Human Pose Estimation](https://arxiv.org/abs/2606.13700v2) | 2606.13700v2 | 6 |
| 2026-06-04 | [HoT-SSM:Higher-order Temporal Knowledge Graph Reasoning with State Space Models for Health Care](https://arxiv.org/abs/2606.05994v1) | 2606.05994v1 | 6 |
| 2026-06-03 | [Mamba-Assisted Non-Markovian Closure for Reduced-Order Modeling](https://arxiv.org/abs/2606.05371v2) | 2606.05371v2 | 10 |
| 2026-06-03 | [Coarse-to-fine Hierarchical Architecture with Sequential Mamba for Brain Reconstruction](https://arxiv.org/abs/2606.04772v1) | 2606.04772v1 | 6 |
| 2026-06-03 | [Query-based Cross-Modal Projector Bolstering Mamba Multimodal LLM](https://arxiv.org/abs/2606.04719v1) | 2606.04719v1 | 6 |
| 2026-06-03 | [Learning Long Range Spatio-Temporal Representations over Continuous Time Dynamic Graphs with State Space Models](https://arxiv.org/abs/2606.04672v2) | 2606.04672v2 | 6 |
| 2026-06-03 | [SinkRec: Mitigating Semantic State Sink in Long Sequence Recommendation with Memory-Conditioned Gated Delta Networks](https://arxiv.org/abs/2606.09888v1) | 2606.09888v1 | 11 |
| 2026-06-03 | [SFMambaNet: Spectral-Frequency Enhanced Selective State Space Model for Correspondence Pruning](https://arxiv.org/abs/2606.04493v1) | 2606.04493v1 | 17 |
| 2026-06-02 | [Dynamic Short Convolutions Improve Transformers](https://arxiv.org/abs/2606.03825v2) | 2606.03825v2 | 8 |
| 2026-06-02 | [Mamba-Enhanced Implicit Motion Learning for Audio-Driven Portrait Animation](https://arxiv.org/abs/2606.03402v2) | 2606.03402v2 | 6 |
| 2026-06-01 | [Physically-Constrained Mamba-SDE for Remaining Useful Life Prediction under Irregular Observations](https://arxiv.org/abs/2606.01894v1) | 2606.01894v1 | 6 |
| 2026-06-01 | [RPCASSM: Robust PCA State Space Model For Infrared Small Target Detection](https://arxiv.org/abs/2606.01689v1) | 2606.01689v1 | 6 |
| 2026-06-01 | [ForestMamba: Sparse Mamba with Geometry-guided Queries for 3D Forest Point Cloud Segmentation](https://arxiv.org/abs/2606.01549v2) | 2606.01549v2 | 7 |
| 2026-05-30 | [DINO-GFSA: Geo-Localization via Semantic Gated Fusion and Mamba-based Sequential Aggregation](https://arxiv.org/abs/2606.00784v1) | 2606.00784v1 | 6 |
| 2026-05-30 | [ScanWeaver: Compiler-Driven Parallelization of Affine Recurrences via Associative Scan Lowering](https://arxiv.org/abs/2606.00601v1) | 2606.00601v1 | 7 |
| 2026-05-30 | [EnergyMamba: An Uncertainty-Aware Graph-Enhanced Selective State Space Model for Energy Consumption Prediction](https://arxiv.org/abs/2606.00506v1) | 2606.00506v1 | 15 |
| 2026-05-30 | [3D Segment Anything Model with Visual Mamba for Diagnosing Placenta Accreta Spectrum](https://arxiv.org/abs/2606.00489v2) | 2606.00489v2 | 10 |
| 2026-05-29 | [Zamba2-VL Technical Report](https://arxiv.org/abs/2606.00390v1) | 2606.00390v1 | 6 |
| 2026-05-29 | [Rethinking Efficient Crack Segmentation with Task-Aligned Structural-Directional Modeling](https://arxiv.org/abs/2605.31048v1) | 2605.31048v1 | 8 |
| 2026-05-29 | [BiSegMamba: Efficient Bidirectional Tri-Oriented Mamba for 3D Medical Image Segmentation](https://arxiv.org/abs/2605.30972v3) | 2605.30972v3 | 8 |
| 2026-05-29 | [A Protocol-Language Model for Network Intrusion (Without Deep Packet Inspection)](https://arxiv.org/abs/2606.00155v1) | 2606.00155v1 | 6 |
| 2026-05-28 | [Chess-World-Model: A 10M-Game Benchmark for Exact State Tracking from Chess Move Sequences](https://arxiv.org/abs/2605.30100v2) | 2605.30100v2 | 10 |
| 2026-05-28 | [GeoMag: Geometric-Aware Video Motion Magnification via State Space Model](https://arxiv.org/abs/2605.29762v1) | 2605.29762v1 | 6 |
| 2026-05-27 | [CaMBRAIN: Real-time, Continuous EEG Inference with Causal State Space Models](https://arxiv.org/abs/2605.28792v1) | 2605.28792v1 | 11 |
| 2026-05-27 | [Modeling Vehicle-Type-Specific Pedestrian Crash Avoidance Behavior in Safety-Critical Interactions Using Smooth-Mamba Deep Reinforcement Learning](https://arxiv.org/abs/2605.28552v1) | 2605.28552v1 | 6 |
| 2026-05-26 | [DinoComplete: 3D Shape Completion with Distilled Semantic Priors and State Space Models](https://arxiv.org/abs/2605.26949v2) | 2605.26949v2 | 12 |
| 2026-05-25 | [NL-MambaXCT: Self-Supervised Nested-Learning Mamba for Nomex Honeycomb X-ray CT Defect Classification](https://arxiv.org/abs/2605.27454v2) | 2605.27454v2 | 6 |
| 2026-05-25 | [SP-MoMamba: Superpixel-driven Mixture of State Space Experts for Efficient Image Super-Resolution](https://arxiv.org/abs/2605.25892v2) | 2605.25892v2 | 12 |
| 2026-05-24 | [Multi-view Consistent 3D Gaussian Head Avatars 'without' Multi-view Generation](https://arxiv.org/abs/2605.25220v1) | 2605.25220v1 | 8 |
| 2026-05-24 | [MedMamba: Multi-View State Space Models with Adaptive Graph Learning for Medical Time Series Classification](https://arxiv.org/abs/2605.24961v1) | 2605.24961v1 | 12 |
| 2026-05-24 | [MambaDSF: Multi-Scale SSM with Dilated Feature Fusion for Sonar Small Target Detection](https://arxiv.org/abs/2605.24928v2) | 2605.24928v2 | 6 |
| 2026-05-23 | [Graph Mamba Survival Analysis Based on Topology-Aware ordering](https://arxiv.org/abs/2606.02602v1) | 2606.02602v1 | 6 |
| 2026-05-23 | [Interdomain Attention: Beyond Token-Level Key-Value Memory](https://arxiv.org/abs/2605.24330v2) | 2605.24330v2 | 10 |
| 2026-05-23 | [Cross-Modal Action Recognition in Egocentric Video Using Mamba: Integrating RGB and Hand Skeleton Streams via CLS Token Fusion Strategies](https://arxiv.org/abs/2605.24302v2) | 2605.24302v2 | 10 |
| 2026-05-21 | [MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data](https://arxiv.org/abs/2605.22775v3) | 2605.22775v3 | 6 |
| 2026-05-21 | [CLSP-REQA: A Real-Time Quality-Aware Closed-Loop Seizure Prediction Framework with Mamba-BiLSTM and Confidence-Gated Intervention](https://arxiv.org/abs/2606.00074v2) | 2606.00074v2 | 6 |
| 2026-05-21 | [Asymmetric Virtual Memory Paging for Hybrid Mamba-Transformer Inference](https://arxiv.org/abs/2605.22416v1) | 2605.22416v1 | 10 |
| 2026-05-21 | [GALAR-TemporalNet v2: Anatomy-Guided Dual-Branch Temporal Classification with Bidirectional Mamba and Dual-Graph GCN for Video Capsule Endoscopy -- after competition results](https://arxiv.org/abs/2605.22209v1) | 2605.22209v1 | 6 |
| 2026-05-21 | [SO-Mamba: State-Ownership Mamba for Unrolled MRI Reconstruction](https://arxiv.org/abs/2605.22031v1) | 2605.22031v1 | 8 |
| 2026-05-20 | [Deformba: Vision State Space Model with Adaptive State Fusion](https://arxiv.org/abs/2605.21308v1) | 2605.21308v1 | 9 |
| 2026-05-20 | [Efficient Learning of Deep State Space Models via Importance Smoothing](https://arxiv.org/abs/2605.21108v2) | 2605.21108v2 | 6 |
| 2026-05-20 | [Diagnosing Overhead in Dispatch Operations: Cross-architecture Observatory](https://arxiv.org/abs/2605.20982v2) | 2605.20982v2 | 8 |
| 2026-05-19 | [CogScale: Scalable Benchmark for Sequence Processing](https://arxiv.org/abs/2605.19758v1) | 2605.19758v1 | 6 |
| 2026-05-18 | [HexagonalWarriorMamba: Superior Threshold-Dependent Multi-label Classification of 12-Lead ECG Cardiac Abnormalities](https://arxiv.org/abs/2605.17875v1) | 2605.17875v1 | 6 |
| 2026-05-18 | [Patch-MoE Mamba: A Patch-Ordered Mixture-of-Experts State Space Architecture for Medical Image Segmentation](https://arxiv.org/abs/2605.17719v1) | 2605.17719v1 | 10 |
| 2026-05-17 | [Mamba-VGGT: Persistent Long-Sequence Video Geometry Grounded Transformer via External Sliding Window Mamba Memory](https://arxiv.org/abs/2605.17478v1) | 2605.17478v1 | 6 |
| 2026-05-17 | [Stability and Discretization Error of State Space Model Neural Operators](https://arxiv.org/abs/2605.18905v1) | 2605.18905v1 | 6 |
| 2026-05-16 | [Sparse Mamba Decoder for Quantum Error Correction: Efficient Defect-Centric Processing of Surface Code Syndromes](https://arxiv.org/abs/2605.17156v2) | 2605.17156v2 | 6 |
| 2026-05-16 | [HEED: Density-Weighted Residual Alignment for Hybrid Vision-Language Model Distillation](https://arxiv.org/abs/2605.17093v1) | 2605.17093v1 | 8 |
| 2026-05-16 | [Axial-Relation Guided Fusion State Space Model for Optical-Elevation Sensing Image Segmentation](https://arxiv.org/abs/2605.16768v1) | 2605.16768v1 | 10 |
| 2026-05-15 | [Public-Decay Homomorphic State Space Models for Private Sequence Inference](https://arxiv.org/abs/2605.16647v1) | 2605.16647v1 | 8 |
| 2026-05-15 | [Provably Shorter Scratchpads in Hybrid DeltaNet-Attention Decoders](https://arxiv.org/abs/2605.16640v1) | 2605.16640v1 | 10 |
| 2026-05-15 | [Reshape and Recur: Improving SSMs with Input Reshaping and Depth Recurrence](https://arxiv.org/abs/2605.16048v2) | 2605.16048v2 | 6 |
| 2026-05-15 | [MHMamba: Multi-Head Mamba for 3D Brain Tumor Segmentation](https://arxiv.org/abs/2605.16464v1) | 2605.16464v1 | 6 |
| 2026-05-15 | [3DTMDet: A Dual-Path Synergy Network of Transformer and SSM for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2605.15546v1) | 2605.15546v1 | 10 |
| 2026-05-14 | [Social-Mamba: Socially-Aware Trajectory Forecasting with State-Space Models](https://arxiv.org/abs/2605.15424v1) | 2605.15424v1 | 7 |
| 2026-05-14 | [Time-Varying Deep State Space Models for Sequences with Switching Dynamics](https://arxiv.org/abs/2605.15311v1) | 2605.15311v1 | 6 |
| 2026-05-14 | [QuChaTeR: A Hybrid Quantum-Chaotic Temporal Framework for Earthquake Prediction](https://arxiv.org/abs/2605.16454v1) | 2605.16454v1 | 6 |
| 2026-05-14 | [Can Visual Mamba Improve AI-Generated Image Detection? An In-Depth Investigation](https://arxiv.org/abs/2605.14799v2) | 2605.14799v2 | 6 |
| 2026-05-14 | [MambaRain: Multi-Scale Mamba-Attention Framework for 0-3 Hour Precipitation Nowcasting](https://arxiv.org/abs/2605.14606v1) | 2605.14606v1 | 8 |
| 2026-05-14 | [DSSP: Diffusion State Space Policy with Full-History Encoding](https://arxiv.org/abs/2605.14598v2) | 2605.14598v2 | 6 |
| 2026-05-13 | [FSCM: Frequency-Enhanced Spatial-Spectral Coupled Mamba for Infrared Hyperspectral Image Colorization](https://arxiv.org/abs/2605.15880v1) | 2605.15880v1 | 6 |
| 2026-05-13 | [Hybrid Quantum-MambaVision: A Quantum-enhanced State Space Model for Calibrated Mixed-type Wafer Defect Detection](https://arxiv.org/abs/2605.16404v1) | 2605.16404v1 | 12 |
| 2026-05-13 | [STAR: Semantic-Temporal Adaptive Representation Learning for Few-Shot Action Recognition](https://arxiv.org/abs/2605.13202v1) | 2605.13202v1 | 6 |
| 2026-05-12 | [WriteSAE: Sparse Autoencoders for Recurrent State](https://arxiv.org/abs/2605.12770v4) | 2605.12770v4 | 15 |
| 2026-05-12 | [Parallel-in-Time Training of Recurrent Neural Networks for Dynamical Systems Reconstruction](https://arxiv.org/abs/2605.12683v1) | 2605.12683v1 | 7 |
| 2026-05-12 | [MambaPanoptic: A Vision Mamba-based Structured State Space Framework for Panoptic Segmentation](https://arxiv.org/abs/2605.12640v2) | 2605.12640v2 | 6 |
| 2026-05-12 | [Train Short, Act Long: Multistability and the Horizon Independence of Recurrent Policies](https://arxiv.org/abs/2605.12206v2) | 2605.12206v2 | 7 |
| 2026-05-12 | [Interactive State Space Model with Cross-Modal Local Scanning for Depth Super-Resolution](https://arxiv.org/abs/2605.11934v1) | 2605.11934v1 | 10 |
| 2026-05-12 | [Selection, Not Fusion: Radar-Modulated State Space Models for Radar-Camera Depth Estimation](https://arxiv.org/abs/2605.11840v2) | 2605.11840v2 | 10 |
| 2026-05-12 | [TCP-SSM: Efficient Vision State Space Models with Token-Conditioned Poles](https://arxiv.org/abs/2605.11563v1) | 2605.11563v1 | 13 |
| 2026-05-11 | [Can Graphs Help Vision SSMs See Better?](https://arxiv.org/abs/2605.11300v1) | 2605.11300v1 | 8 |
| 2026-05-11 | [USEMA: a Scalable Efficient Mamba Like Attention for Medical Image Segmentation](https://arxiv.org/abs/2605.11131v1) | 2605.11131v1 | 6 |
| 2026-05-11 | [Scalable Mamba-Based Message-Passing Neural Decoder for Error-Correcting Codes](https://arxiv.org/abs/2605.10681v2) | 2605.10681v2 | 6 |
| 2026-05-11 | [A Single-Layer Model Can Do Language Modeling](https://arxiv.org/abs/2605.10643v1) | 2605.10643v1 | 14 |
| 2026-05-11 | [Polygon-mamba: Retinal vessel segmentation using polygon scanning mamba and space-frequency collaborative attention](https://arxiv.org/abs/2605.10581v2) | 2605.10581v2 | 10 |
| 2026-05-11 | [Increasing the Efficiency of DETR for Maritime High-Resolution Images](https://arxiv.org/abs/2605.10269v1) | 2605.10269v1 | 8 |
| 2026-05-11 | [CFSPMNet: Cross-subject Fourier-guided Spatial-Patch Mamba Network for EEG Motor Imagery Decoding in Stroke Patients](https://arxiv.org/abs/2605.10111v1) | 2605.10111v1 | 6 |
| 2026-05-11 | [ReTAMamba: Reliability-Aware Temporal Aggregation with Mamba for Irregular Clinical Time Series Prediction](https://arxiv.org/abs/2605.16380v1) | 2605.16380v1 | 6 |
| 2026-05-11 | [MambaNetBurst: Direct Byte-level Network Traffic Classification without Tokenization or Pretraining](https://arxiv.org/abs/2605.11034v1) | 2605.11034v1 | 14 |
| 2026-05-10 | [TIDES: Implicit Time-Awareness in Selective State Space Models](https://arxiv.org/abs/2605.09742v3) | 2605.09742v3 | 13 |
| 2026-05-10 | [Mixture of Layers with Hybrid Attention](https://arxiv.org/abs/2605.09516v1) | 2605.09516v1 | 6 |
| 2026-05-09 | [FRACTAL: SSM with Fractional Recurrent Architecture for Computational Temporal Analysis of Long Sequences](https://arxiv.org/abs/2605.08833v1) | 2605.08833v1 | 9 |
| 2026-05-08 | [EmambaIR: Efficient Visual State Space Model for Event-guided Image Reconstruction](https://arxiv.org/abs/2605.08073v1) | 2605.08073v1 | 12 |
| 2026-05-08 | [Spatiotemporal Trust Evaluation for Collaborator Selection via Customized GNN-Mamba](https://arxiv.org/abs/2605.07658v1) | 2605.07658v1 | 6 |
| 2026-05-08 | [Breaking Spatial Uniformity: Prior-Guided Mamba with Radial Serialization for Lens Flare Removal](https://arxiv.org/abs/2605.07650v1) | 2605.07650v1 | 10 |
| 2026-05-08 | [Priming: Hybrid State Space Models From Pre-trained Transformers](https://arxiv.org/abs/2605.08301v1) | 2605.08301v1 | 20 |
| 2026-05-08 | [VIMCAN: Visual-Inertial 3D Human Pose Estimation with Hybrid Mamba-Cross-Attention Network](https://arxiv.org/abs/2605.07552v2) | 2605.07552v2 | 12 |
| 2026-05-08 | [StreamPhy: Streaming Inference of High-Dimensional Physical Dynamics via State Space Models](https://arxiv.org/abs/2605.07384v3) | 2605.07384v3 | 6 |
| 2026-05-08 | [GEM: Generating LiDAR World Model via Deformable Mamba](https://arxiv.org/abs/2605.07326v2) | 2605.07326v2 | 6 |
| 2026-05-08 | [PALM: Physically-Anchored Latent-timescale Mamba for Stable Representations under Distribution Shift](https://arxiv.org/abs/2605.16351v2) | 2605.16351v2 | 6 |
| 2026-05-08 | [ImplantMamba: Long-range Sequential Modeling Mamba For Dental Implant Position Prediction](https://arxiv.org/abs/2605.07082v1) | 2605.07082v1 | 6 |
| 2026-05-07 | [Echo: KV-Cache-Free Associative Recall with Spectral Koopman Operators](https://arxiv.org/abs/2605.06997v1) | 2605.06997v1 | 6 |
| 2026-05-07 | [A Novel Geographic Graph-Regulated Disentangling Mamba Model with Sparse Tokens for Enhanced Tree Species Classification from MODIS Time Series](https://arxiv.org/abs/2605.05549v2) | 2605.05549v2 | 6 |
| 2026-05-07 | [A Simple State Space Model Excels at Multivariate Time Series Classification](https://arxiv.org/abs/2605.27406v2) | 2605.27406v2 | 12 |
| 2026-05-06 | [The Impossibility Triangle of Long-Context Modeling](https://arxiv.org/abs/2605.05066v2) | 2605.05066v2 | 10 |
| 2026-05-06 | [Bilinear Mamba-Koopman Neural MPC for Varying Dynamics](https://arxiv.org/abs/2605.04793v2) | 2605.04793v2 | 6 |
| 2026-05-06 | [ELVIS: Ensemble-Calibrated Latent Imagination for Long-Horizon Visual MPC](https://arxiv.org/abs/2605.04709v1) | 2605.04709v1 | 6 |
| 2026-05-06 | [SAMIC: A Lightweight Semantic-Aware Mamba for Efficient Perceptual Image Compression](https://arxiv.org/abs/2605.04560v1) | 2605.04560v1 | 10 |
| 2026-05-05 | [Mantis: Mamba-native Tuning is Efficient for 3D Point Cloud Foundation Models](https://arxiv.org/abs/2605.03438v4) | 2605.03438v4 | 6 |
| 2026-05-04 | [Edge-Efficient Image Restoration: Transformer Distillation into State-Space Models](https://arxiv.org/abs/2605.02794v1) | 2605.02794v1 | 6 |
| 2026-05-04 | [Learning Temporal Patterns in Financial Time Series: A Comparative Study of Quantum LSTM and Quantum Reservoir Computing](https://arxiv.org/abs/2605.02656v2) | 2605.02656v2 | 6 |
| 2026-05-03 | [ViM-Q: Scalable Algorithm-Hardware Co-Design for Vision Mamba Model Inference on FPGA](https://arxiv.org/abs/2605.01935v1) | 2605.01935v1 | 10 |
| 2026-05-03 | [QHyer: Q-conditioned Hybrid Attention-mamba Transformer for Offline Goal-conditioned RL](https://arxiv.org/abs/2605.01862v2) | 2605.01862v2 | 10 |
| 2026-05-02 | [Factor State Space Modelling of the Ornstein-Uhlenbeck Process with Measurement Error and its Application](https://arxiv.org/abs/2605.01262v1) | 2605.01262v1 | 6 |
| 2026-05-02 | [Rhamba: Region-Aware Hybrid Attention-Mamba Framework for Self-Supervised Learning in Resting-State fMRI](https://arxiv.org/abs/2605.01240v3) | 2605.01240v3 | 12 |
| 2026-04-30 | [Caracal: Causal Architecture via Spectral Mixing](https://arxiv.org/abs/2605.00292v2) | 2605.00292v2 | 6 |
| 2026-04-30 | [Lost in State Space: Probing Frozen Mamba Representations](https://arxiv.org/abs/2605.00253v1) | 2605.00253v1 | 8 |
| 2026-04-30 | [RopeDreamer: A Kinematic Recurrent State Space Model for Dynamics of Flexible Deformable Linear Objects](https://arxiv.org/abs/2604.28161v1) | 2604.28161v1 | 9 |
| 2026-04-29 | [SAMamba3D: adapting Segment Anything for generalizable 3D segmentation of multiphase pore-scale images](https://arxiv.org/abs/2605.00916v1) | 2605.00916v1 | 6 |
| 2026-04-29 | [Random Number Generators in Advanced Optical Experiments: A Comparative Analysis of Semiclassical, Quantum, and Hybrid Architectures](https://arxiv.org/abs/2604.26554v1) | 2604.26554v1 | 6 |
| 2026-04-29 | [$\text{PKS}^4$:Parallel Kinematic Selective State Space Scanners for Efficient Video Understanding](https://arxiv.org/abs/2604.26461v1) | 2604.26461v1 | 7 |
| 2026-04-28 | [PPG-Based Affect Recognition with Long-Range Deep Models: A Measurement-Driven Comparison of CNN, Transformer, and Mamba Architectures](https://arxiv.org/abs/2604.26078v1) | 2604.26078v1 | 6 |
| 2026-04-28 | [Density Field State Space Models: 1-Bit Distillation, Efficient Inference, and Knowledge Organization in Mamba-2](https://arxiv.org/abs/2606.10932v1) | 2606.10932v1 | 12 |
| 2026-04-28 | [Vision SmolMamba: Spike-Guided Token Pruning for Energy-Efficient Spiking State-Space Vision Models](https://arxiv.org/abs/2604.25570v1) | 2604.25570v1 | 7 |
| 2026-04-28 | [TopoMamba: Topology-Aware Scanning and Fusion for Segmenting Heterogeneous Medical Visual Media](https://arxiv.org/abs/2604.25545v2) | 2604.25545v2 | 6 |
| 2026-04-28 | [Biased Dreams: Limitations to Epistemic Uncertainty Quantification in Latent Dynamics Models](https://arxiv.org/abs/2604.25416v2) | 2604.25416v2 | 6 |
| 2026-04-28 | [CacheFlow: Efficient LLM Serving via Automated 3D-Parallel KV Cache Restoration](https://arxiv.org/abs/2604.25080v2) | 2604.25080v2 | 6 |
| 2026-04-26 | [On the Generalization Properties of Selective State-Space Models for Filtering Tasks for Unknown Systems](https://arxiv.org/abs/2604.23818v1) | 2604.23818v1 | 6 |
| 2026-04-26 | [BVI-Mamba: Video Enhancement Using a Visual State-Space Model for Low-Light and Underwater Environments](https://arxiv.org/abs/2604.23655v1) | 2604.23655v1 | 6 |
| 2026-04-25 | [Breaking the Resource Wall: Geometry-Guided Sequence Modeling for Efficient Semantic Segmentation](https://arxiv.org/abs/2604.23399v2) | 2604.23399v2 | 11 |
| 2026-04-25 | [AdaMamba: Adaptive Frequency-Gated Mamba for Long-Term Time Series Forecasting](https://arxiv.org/abs/2604.23239v2) | 2604.23239v2 | 6 |
| 2026-04-24 | [NAKUL-Med: Spectral-Graph State Space Models with Dynamics Kernels for Medical Signals](https://arxiv.org/abs/2605.00871v1) | 2605.00871v1 | 7 |
| 2026-04-24 | [Where Should LoRA Go? Component-Type Placement in Hybrid Language Models](https://arxiv.org/abs/2604.22127v1) | 2604.22127v1 | 10 |
| 2026-04-23 | [On a class of constrained particle filters for continuous-discrete state space models](https://arxiv.org/abs/2604.21538v1) | 2604.21538v1 | 6 |
| 2026-04-23 | [MambaCSP: Hybrid-Attention State Space Models for Hardware-Efficient Channel State Prediction](https://arxiv.org/abs/2604.21957v2) | 2604.21957v2 | 15 |
| 2026-04-23 | [Robust Cross-Domain WiFi Fall Detection via Physics-Driven Attention-Enhanced Transformers](https://arxiv.org/abs/2605.00869v1) | 2605.00869v1 | 6 |
| 2026-04-22 | [Beyond ZOH: Advanced Discretization Strategies for Vision Mamba](https://arxiv.org/abs/2604.20606v1) | 2604.20606v1 | 10 |
| 2026-04-22 | [LayerTracer: A Joint Task-Particle and Vulnerable-Layer Analysis framework for Arbitrary Large Language Model Architectures](https://arxiv.org/abs/2604.20556v1) | 2604.20556v1 | 8 |
| 2026-04-22 | [MambaLiteUNet: Cross-Gated Adaptive Feature Fusion for Robust Skin Lesion Segmentation](https://arxiv.org/abs/2604.20286v1) | 2604.20286v1 | 10 |
| 2026-04-21 | [M$^{2}$GRPO: Mamba-based Multi-Agent Group Relative Policy Optimization for Biomimetic Underwater Robots Pursuit](https://arxiv.org/abs/2604.19404v1) | 2604.19404v1 | 8 |
| 2026-04-20 | [ConvVitMamba: Efficient Multiscale Convolution, Transformer, and Mamba-Based Sequence modelling for Hyperspectral Image Classification](https://arxiv.org/abs/2604.18856v1) | 2604.18856v1 | 6 |
| 2026-04-20 | [Sessa: Selective State Space Attention](https://arxiv.org/abs/2604.18580v2) | 2604.18580v2 | 11 |
| 2026-04-19 | [DGSSM: Diffusion guided state-space models for multimodal salient object detection](https://arxiv.org/abs/2604.17585v1) | 2604.17585v1 | 8 |
| 2026-04-19 | [Bilinear Input Modulation for Mamba: Koopman Bilinear Forms for Memory Retention and Multiplicative Computation](https://arxiv.org/abs/2604.17221v2) | 2604.17221v2 | 12 |
| 2026-04-18 | [TSM-Pose: Topology-Aware Learning with Semantic Mamba for Category-Level Object Pose Estimation](https://arxiv.org/abs/2604.16954v2) | 2604.16954v2 | 6 |
| 2026-04-18 | [GAMMA-Net: Adaptive Long-Horizon Traffic Spatio-Temporal Forecasting Model based on Interleaved Graph Attention and Multi-Axis Mamba](https://arxiv.org/abs/2604.16859v1) | 2604.16859v1 | 14 |
| 2026-04-17 | [Hero-Mamba: Mamba-based Dual Domain Learning for Underwater Image Enhancement](https://arxiv.org/abs/2604.16266v1) | 2604.16266v1 | 6 |
| 2026-04-17 | [MambaKick: Early Penalty Direction Prediction from HAR Embeddings](https://arxiv.org/abs/2604.16588v1) | 2604.16588v1 | 6 |
| 2026-04-17 | [MambaBack: Bridging Local Features and Global Contexts in Whole Slide Image Analysis](https://arxiv.org/abs/2604.15729v2) | 2604.15729v2 | 10 |
| 2026-04-17 | [SSMamba: A Self-Supervised Hybrid State Space Model for Pathological Image Classification](https://arxiv.org/abs/2604.15711v2) | 2604.15711v2 | 12 |
| 2026-04-17 | [CLIMB: Controllable Longitudinal Brain Image Generation using Mamba-based Latent Diffusion Model and Gaussian-aligned Autoencoder](https://arxiv.org/abs/2604.15611v1) | 2604.15611v1 | 10 |
| 2026-04-17 | [MedMamba: Recasting Mamba for Medical Time Series Classification](https://arxiv.org/abs/2605.05214v1) | 2605.05214v1 | 12 |
| 2026-04-16 | [MambaSL: Exploring Single-Layer Mamba for Time Series Classification](https://arxiv.org/abs/2604.15174v3) | 2604.15174v3 | 10 |
| 2026-04-16 | [Learning Ad Hoc Network Dynamics via Graph-Structured World Models](https://arxiv.org/abs/2604.14811v1) | 2604.14811v1 | 6 |
| 2026-04-16 | [HAMSA: Scanning-Free Vision State Space Models via SpectralPulseNet](https://arxiv.org/abs/2604.14724v1) | 2604.14724v1 | 10 |
| 2026-04-15 | [Mamba-SSM with LLM Reasoning for Feature Selection: Faithfulness-Aware Biomarker Discovery](https://arxiv.org/abs/2604.14334v2) | 2604.14334v2 | 6 |
| 2026-04-15 | [Mamba Sequence Modeling meets Model Predictive Control](https://arxiv.org/abs/2604.13857v2) | 2604.13857v2 | 10 |
| 2026-04-15 | [Dynamic Heartbeat Modeling with Recurrent Neural Networks and Inverse Gaussian Point Process](https://arxiv.org/abs/2604.13815v3) | 2604.13815v3 | 7 |
| 2026-04-15 | [A KL Lens on Quantization: Fast, Forward-Only Sensitivity for Mixed-Precision SSM-Transformer Models](https://arxiv.org/abs/2604.13440v1) | 2604.13440v1 | 8 |
| 2026-04-15 | [Event-Adaptive State Transition and Gated Fusion for RGB-Event Object Tracking](https://arxiv.org/abs/2604.13426v1) | 2604.13426v1 | 8 |
| 2026-04-14 | [TCL: Enabling Fast and Efficient Cross-Hardware Tensor Program Optimization via Continual Learning](https://arxiv.org/abs/2604.12891v1) | 2604.12891v1 | 6 |
| 2026-04-14 | [A Hybrid Architecture for Benign-Malignant Classification of Mammography ROIs](https://arxiv.org/abs/2604.12437v1) | 2604.12437v1 | 14 |
| 2026-04-14 | [Nemotron 3 Super: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2604.12374v1) | 2604.12374v1 | 6 |
| 2026-04-14 | [RSGMamba: Reliability-Aware Self-Gated State Space Model for Multimodal Semantic Segmentation](https://arxiv.org/abs/2604.12319v2) | 2604.12319v2 | 12 |
| 2026-04-14 | [TokenSE: a Mamba-based discrete token speech enhancement framework for cochlear implants](https://arxiv.org/abs/2604.12246v1) | 2604.12246v1 | 6 |
| 2026-04-13 | [Physics-Informed State Space Models for Reliable Solar Irradiance Forecasting in Off-Grid Systems](https://arxiv.org/abs/2604.11807v3) | 2604.11807v3 | 6 |
| 2026-04-13 | [A Mamba-Based Multimodal Network for Multiscale Blast-Induced Rapid Structural Damage Assessment](https://arxiv.org/abs/2604.11709v1) | 2604.11709v1 | 6 |
| 2026-04-12 | [COREY: Entropy-Guided Runtime Chunk Scheduling for Selective Scan Kernels](https://arxiv.org/abs/2604.10597v3) | 2604.10597v3 | 13 |
| 2026-04-10 | [Unmixing-Guided Spatial-Spectral Mamba with Clustering Tokens for Hyperspectral Image Classification](https://arxiv.org/abs/2604.09948v1) | 2604.09948v1 | 6 |
| 2026-04-10 | [FaceLiVTv2: An Improved Hybrid Architecture for Efficient Mobile Face Recognition](https://arxiv.org/abs/2604.09127v1) | 2604.09127v1 | 6 |
| 2026-04-09 | [HST-HGN: Heterogeneous Spatial-Temporal Hypergraph Networks with Bidirectional State Space Models for Global Fatigue Assessment](https://arxiv.org/abs/2604.08435v2) | 2604.08435v2 | 12 |
| 2026-04-09 | [ABMAMBA: Multimodal Large Language Model with Aligned Hierarchical Bidirectional Scan for Efficient Video Captioning](https://arxiv.org/abs/2604.08050v1) | 2604.08050v1 | 10 |
| 2026-04-09 | [Beyond Mamba: Enhancing State-space Models with Deformable Dilated Convolutions for Multi-scale Traffic Object Detection](https://arxiv.org/abs/2604.08038v1) | 2604.08038v1 | 6 |
| 2026-04-09 | [Beyond the Autoregressive Horizon: A Comprehensive Survey of Diffusion Models, World Modelling, and State Space Models for Code](https://arxiv.org/abs/2606.23690v1) | 2606.23690v1 | 7 |
| 2026-04-09 | [Stochastic Thermodynamics for Autoregressive Generative Models: A Non-Markovian Perspective](https://arxiv.org/abs/2604.07867v5) | 2604.07867v5 | 10 |
| 2026-04-08 | [CloudMamba: An Uncertainty-Guided Dual-Scale Mamba Network for Cloud Detection in Remote Sensing Imagery](https://arxiv.org/abs/2604.06844v1) | 2604.06844v1 | 10 |
| 2026-04-08 | [Balancing Efficiency and Restoration: Lightweight Mamba-Based Model for CT Metal Artifact Reduction](https://arxiv.org/abs/2604.06622v1) | 2604.06622v1 | 6 |
| 2026-04-07 | [The UNDO Flip-Flop: A Controlled Probe for Reversible Semantic State Management in State Space Model](https://arxiv.org/abs/2604.05923v1) | 2604.05923v1 | 10 |
| 2026-04-07 | [Physics-Aligned Spectral Mamba: Decoupling Semantics and Dynamics for Few-Shot Hyperspectral Target Detection](https://arxiv.org/abs/2604.05562v1) | 2604.05562v1 | 6 |
| 2026-04-05 | [StateSMix: Online Lossless Compression via Mamba State Space Models and Sparse N-gram Context Mixing](https://arxiv.org/abs/2605.02904v1) | 2605.02904v1 | 12 |
| 2026-04-04 | [Mambalaya: Einsum-Based Fusion Optimizations on State-Space Models](https://arxiv.org/abs/2604.03829v2) | 2604.03829v2 | 6 |
| 2026-04-04 | [Safety, Security, and Cognitive Risks in State-Space Models: A Systematic Threat Analysis with Spectral, Stateful, and Capacity Attacks](https://arxiv.org/abs/2604.16424v1) | 2604.16424v1 | 11 |
| 2026-04-04 | [CAGMamba: Context-Aware Gated Cross-Modal Mamba Network for Multimodal Sentiment Analysis](https://arxiv.org/abs/2604.03650v1) | 2604.03650v1 | 6 |
| 2026-04-03 | [Adversarial Robustness of Deep State Space Models for Forecasting](https://arxiv.org/abs/2604.03427v1) | 2604.03427v1 | 6 |
| 2026-04-03 | [Learning the Signature of Memorization in Autoregressive Language Models](https://arxiv.org/abs/2604.03199v1) | 2604.03199v1 | 12 |
| 2026-04-03 | [RayMamba: Ray-Aligned Serialization for Long-Range 3D Object Detection](https://arxiv.org/abs/2604.02903v1) | 2604.02903v1 | 10 |
| 2026-04-02 | [AViS-Mamba: Adaptive Visual Steering of Audio State-Space Dynamics for Violence Detection](https://arxiv.org/abs/2604.03329v2) | 2604.03329v2 | 6 |
| 2026-04-02 | [AEGIS: Adversarial Entropy-Guided Immune System -- Thermodynamic State Space Models for Zero-Day Network Evasion Detection](https://arxiv.org/abs/2604.02149v1) | 2604.02149v1 | 11 |
| 2026-04-01 | [S0 Tuning: Zero-Overhead Adaptation of Hybrid Recurrent-Attention Models](https://arxiv.org/abs/2604.01168v2) | 2604.01168v2 | 7 |
| 2026-04-01 | [A Benchmark of State-Space Models vs. Transformers and BiLSTM-based Models for Historical Newspaper OCR](https://arxiv.org/abs/2604.00725v2) | 2604.00725v2 | 7 |
| 2026-04-01 | [Attention to Mamba: A Recipe for Cross-Architecture Distillation](https://arxiv.org/abs/2604.14191v2) | 2604.14191v2 | 10 |
| 2026-04-01 | [KG-CMI: Knowledge graph enhanced cross-Mamba interaction for medical visual question answering](https://arxiv.org/abs/2604.00601v1) | 2604.00601v1 | 6 |
| 2026-04-01 | [MATHENA: Mamba-based Architectural Tooth Hierarchical Estimator and Holistic Evaluation Network for Anatomy](https://arxiv.org/abs/2604.00537v1) | 2604.00537v1 | 10 |
| 2026-04-01 | [VADMamba++: Efficient Video Anomaly Detection via Hybrid Modeling in Grayscale Space](https://arxiv.org/abs/2604.00360v1) | 2604.00360v1 | 6 |
| 2026-03-31 | [MambaVoiceCloning: Efficient and Expressive Text-to-Speech via State-Space Modeling and Diffusion Control](https://arxiv.org/abs/2604.00292v1) | 2604.00292v1 | 7 |
| 2026-03-31 | [HCLSM: Hierarchical Causal Latent State Machines for Object-Centric World Modeling](https://arxiv.org/abs/2603.29090v1) | 2603.29090v1 | 6 |
| 2026-03-29 | [The Randomness Floor: Measuring Intrinsic Non-Randomness in Language Model Token Distributions](https://arxiv.org/abs/2604.22771v1) | 2604.22771v1 | 8 |
| 2026-03-28 | [TokenDance: Token-to-Token Music-to-Dance Generation with Bidirectional Mamba](https://arxiv.org/abs/2603.27314v1) | 2603.27314v1 | 6 |
| 2026-03-27 | [WiMamba: Linear-Scale Wireless Foundation Model](https://arxiv.org/abs/2603.26367v1) | 2603.26367v1 | 9 |
| 2026-03-26 | [A Mamba-based Perceptual Loss Function for Learning-based UGC Transcoding](https://arxiv.org/abs/2603.25566v1) | 2603.25566v1 | 6 |
| 2026-03-26 | [Towards Controllable Low-Light Image Enhancement: A Continuous Multi-illumination Dataset and Efficient State Space Framework](https://arxiv.org/abs/2603.25296v1) | 2603.25296v1 | 8 |
| 2026-03-26 | [Hyena Operator for Fast Sequential Recommendation](https://arxiv.org/abs/2603.25027v1) | 2603.25027v1 | 7 |
| 2026-03-25 | [RS-SSM: Refining Forgotten Specifics in State Space Model for Video Semantic Segmentation](https://arxiv.org/abs/2603.24295v2) | 2603.24295v2 | 6 |
| 2026-03-24 | [Mamba-driven MRI-to-CT Synthesis for MRI-only Radiotherapy Planning](https://arxiv.org/abs/2603.23295v2) | 2603.23295v2 | 6 |
| 2026-03-23 | [Multi-View Deformable Convolution Meets Visual Mamba for Coronary Artery Segmentation](https://arxiv.org/abs/2603.21829v1) | 2603.21829v1 | 12 |
| 2026-03-22 | [HELIX: Scaling Raw Audio Understanding with Hybrid Mamba-Attention Beyond the Quadratic Limit](https://arxiv.org/abs/2603.21316v1) | 2603.21316v1 | 6 |
| 2026-03-22 | [Fusing Memory and Attention: A study on LSTM, Transformer and Hybrid Architectures for Symbolic Music Generation](https://arxiv.org/abs/2603.21282v1) | 2603.21282v1 | 6 |
| 2026-03-22 | [When Does Content-Based Routing Work? Representation Requirements for Selective Attention in Hybrid Sequence Models](https://arxiv.org/abs/2603.20997v2) | 2603.20997v2 | 6 |
| 2026-03-21 | [Mamba Learns in Context: Structure-Aware Domain Generalization for Multi-Task Point Cloud Understanding](https://arxiv.org/abs/2603.20739v1) | 2603.20739v1 | 7 |
| 2026-03-20 | [Graph Signal Processing Meets Mamba2: Adaptive Filter Bank via Delta Modulation](https://arxiv.org/abs/2603.22333v1) | 2603.22333v1 | 9 |
| 2026-03-20 | [MFil-Mamba: Multi-Filter Scanning for Spatial Redundancy-Aware Visual State Space Models](https://arxiv.org/abs/2603.20074v1) | 2603.20074v1 | 14 |
| 2026-03-20 | [Hybrid Associative Memories](https://arxiv.org/abs/2603.22325v2) | 2603.22325v2 | 6 |
| 2026-03-20 | [ReconMIL: Synergizing Latent Space Reconstruction with Bi-Stream Mamba for Whole Slide Image Analysis](https://arxiv.org/abs/2603.19925v2) | 2603.19925v2 | 8 |
| 2026-03-20 | [CS-MUNet: A Channel-Spatial Dual-Stream Mamba Network for Multi-Organ Segmentation](https://arxiv.org/abs/2603.19659v1) | 2603.19659v1 | 6 |
| 2026-03-19 | [Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encoders](https://arxiv.org/abs/2603.19209v1) | 2603.19209v1 | 6 |
| 2026-03-19 | [LuMamba: Latent Unified Mamba for Electrode Topology-Invariant and Efficient EEG Modeling](https://arxiv.org/abs/2603.19100v2) | 2603.19100v2 | 6 |
| 2026-03-19 | [DA-Mamba: Learning Domain-Aware State Space Model for Global-Local Alignment in Domain Adaptive Object Detection](https://arxiv.org/abs/2603.18757v1) | 2603.18757v1 | 13 |
| 2026-03-19 | [AlignMamba-2: Enhancing Multimodal Fusion and Sentiment Analysis with Modality-Aware Mamba](https://arxiv.org/abs/2603.18462v1) | 2603.18462v1 | 6 |
| 2026-03-18 | [FEMBA on the Edge: Physiologically-Aware Pre-Training, Quantization, and Deployment of a Bidirectional Mamba EEG Foundation Model on an Ultra-low Power Microcontroller](https://arxiv.org/abs/2603.26716v1) | 2603.26716v1 | 6 |
| 2026-03-18 | [DSS-GAN: Directional State Space GAN with Mamba backbone for Class-Conditional Image Synthesis](https://arxiv.org/abs/2603.17637v1) | 2603.17637v1 | 6 |
| 2026-03-18 | [Atomic Trajectory Modeling with State Space Models for Biomolecular Dynamics](https://arxiv.org/abs/2603.17633v1) | 2603.17633v1 | 6 |
| 2026-03-17 | [PI-Mamba: Linear-Time Protein Backbone Generation via Spectrally Initialized Flow Matching](https://arxiv.org/abs/2603.26705v1) | 2603.26705v1 | 7 |
| 2026-03-17 | [SF-Mamba: Rethinking State Space Model for Vision](https://arxiv.org/abs/2603.16423v2) | 2603.16423v2 | 14 |
| 2026-03-17 | [HGP-Mamba: Integrating Histology and Generated Protein Features for Mamba-based Multimodal Survival Risk Prediction](https://arxiv.org/abs/2603.16421v2) | 2603.16421v2 | 6 |
| 2026-03-17 | [NeuronSpark: Selective Spiking State Space Models with Adaptive Computation for Language Modeling](https://arxiv.org/abs/2603.16148v2) | 2603.16148v2 | 12 |
| 2026-03-16 | [Mamba-3: Improved Sequence Modeling using State Space Principles](https://arxiv.org/abs/2603.15569v1) | 2603.15569v1 | 18 |
| 2026-03-16 | [DUET: Disaggregated Hybrid Mamba-Transformer LLMs with Prefill and Decode-Specific Packages](https://arxiv.org/abs/2603.15530v1) | 2603.15530v1 | 10 |
| 2026-03-16 | [AnolisVLA: Lightweight Vision-Language-Action Model with Deep State Space Models for Mobile Manipulation](https://arxiv.org/abs/2603.15046v2) | 2603.15046v2 | 6 |
| 2026-03-16 | [M2IR: Proactive All-in-One Image Restoration via Mamba-style Modulation and Mixture-of-Experts](https://arxiv.org/abs/2603.14816v1) | 2603.14816v1 | 6 |
| 2026-03-16 | [TrajMamba: An Ego-Motion-Guided Mamba Model for Pedestrian Trajectory Prediction from an Egocentric Perspective](https://arxiv.org/abs/2603.14739v1) | 2603.14739v1 | 6 |
| 2026-03-14 | [Enhancing Eye Feature Estimation from Event Data Streams through Adaptive Inference State Space Modeling](https://arxiv.org/abs/2603.14077v2) | 2603.14077v2 | 6 |
| 2026-03-14 | [Deep Learning for Virtual Reality User Identification: A Benchmark](https://arxiv.org/abs/2604.16341v1) | 2604.16341v1 | 6 |
| 2026-03-13 | [Decoding Matters: Efficient Mamba-Based Decoder with Distribution-Aware Deep Supervision for Medical Image Segmentation](https://arxiv.org/abs/2603.12547v1) | 2603.12547v1 | 6 |
| 2026-03-12 | [Probing Length Generalization in Mamba via Image Reconstruction](https://arxiv.org/abs/2603.12499v1) | 2603.12499v1 | 6 |
| 2026-03-12 | [SpectralGuard: Detecting Memory Collapse Attacks in State Space Models](https://arxiv.org/abs/2603.12414v1) | 2603.12414v1 | 13 |
| 2026-03-12 | [MamTra: A Hybrid Mamba-Transformer Backbone for Speech Synthesis](https://arxiv.org/abs/2603.12342v2) | 2603.12342v2 | 11 |
| 2026-03-12 | [CLASP: Defending Hybrid Large Language Models Against Hidden State Poisoning Attacks](https://arxiv.org/abs/2603.12206v2) | 2603.12206v2 | 12 |
| 2026-03-12 | [SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns](https://arxiv.org/abs/2603.11669v3) | 2603.11669v3 | 6 |
| 2026-03-11 | [Hierarchical Granularity Alignment and State Space Modeling for Robust Multimodal AU Detection in the Wild](https://arxiv.org/abs/2603.11306v1) | 2603.11306v1 | 10 |
| 2026-03-11 | [Single molecule localization microscopy challenge: a biologically inspired benchmark for long-sequence modeling](https://arxiv.org/abs/2603.11296v1) | 2603.11296v1 | 7 |
| 2026-03-10 | [Progressive Split Mamba: Effective State Space Modelling for Image Restoration](https://arxiv.org/abs/2603.09171v1) | 2603.09171v1 | 15 |
| 2026-03-10 | [Rotation Equivariant Mamba for Vision Tasks](https://arxiv.org/abs/2603.09138v3) | 2603.09138v3 | 6 |
| 2026-03-09 | [BuildMamba: A Visual State-Space Based Model for Multi-Task Building Segmentation and Height Estimation from Satellite Images](https://arxiv.org/abs/2603.08523v1) | 2603.08523v1 | 7 |
| 2026-03-09 | [Not Like Transformers: Drop the Beat Representation for Dance Generation with Mamba-Based Diffusion Model](https://arxiv.org/abs/2603.08023v1) | 2603.08023v1 | 6 |
| 2026-03-09 | [Geometric Transformation-Embedded Mamba for Learned Video Compression](https://arxiv.org/abs/2603.07912v1) | 2603.07912v1 | 6 |
| 2026-03-08 | [InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model](https://arxiv.org/abs/2603.18031v2) | 2603.18031v2 | 14 |
| 2026-03-07 | [Permutation-Equivariant 2D State Space Models: Theory and Canonical Architecture for Multivariate Time Series](https://arxiv.org/abs/2603.08753v1) | 2603.08753v1 | 10 |
| 2026-03-06 | [Swimba: Switch Mamba Model Scales State Space Models](https://arxiv.org/abs/2603.06938v1) | 2603.06938v1 | 14 |
| 2026-03-06 | [DLRMamba: Distilling Low-Rank Mamba for Edge Multispectral Fusion Object Detection](https://arxiv.org/abs/2603.06920v1) | 2603.06920v1 | 10 |
| 2026-03-06 | [MoEMambaMIL: Structure-Aware Selective State Space Modeling for Whole-Slide Image Analysis](https://arxiv.org/abs/2603.06378v1) | 2603.06378v1 | 17 |
| 2026-03-06 | [UniMamba: A Unified Spatial-Temporal Modeling Framework with State-Space and Attention Integration](https://arxiv.org/abs/2604.16325v3) | 2604.16325v3 | 6 |
| 2026-03-05 | [DeformTrace: A Deformable State Space Model with Relay Tokens for Temporal Forgery Localization](https://arxiv.org/abs/2603.04882v1) | 2603.04882v1 | 10 |
| 2026-03-04 | [Mask-aware inference with State-Space Models](https://arxiv.org/abs/2603.04568v2) | 2603.04568v2 | 8 |
| 2026-03-04 | [Architectural Proprioception in State Space Models: Thermodynamic Training Induces Anticipatory Halt Detection](https://arxiv.org/abs/2603.04180v1) | 2603.04180v1 | 8 |
| 2026-03-04 | [Harnessing Selective State Space Models to Enhance Semianalytical Design of Fabrication-Ready Multilayered Huygens' Metasurfaces: Part II - Generative Inverse Design (MetaMamba)](https://arxiv.org/abs/2603.03877v1) | 2603.03877v1 | 17 |
| 2026-03-04 | [Separators in Enhancing Autoregressive Pretraining for Vision Mamba](https://arxiv.org/abs/2603.03806v2) | 2603.03806v2 | 10 |
| 2026-03-03 | [mHC-HSI: Clustering-Guided Hyper-Connection Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2603.03418v1) | 2603.03418v1 | 6 |
| 2026-03-03 | [MaBERT:A Padding Safe Interleaved Transformer Mamba Hybrid Encoder for Efficient Extended Context Masked Language Modeling](https://arxiv.org/abs/2603.03001v1) | 2603.03001v1 | 10 |
| 2026-03-03 | [CAWM-Mamba: A unified model for infrared-visible image fusion and compound adverse weather restoration](https://arxiv.org/abs/2603.02560v1) | 2603.02560v1 | 6 |
| 2026-03-02 | [How do standard time series forecasting benchmarks translate to finance? A broad study of risk adjusted performance](https://arxiv.org/abs/2603.01820v2) | 2603.01820v2 | 6 |
| 2026-03-02 | [TacMamba: A Tactile History Compression Adapter Bridging Fast Reflexes and Slow VLA Reasoning](https://arxiv.org/abs/2603.01700v1) | 2603.01700v1 | 6 |
| 2026-03-02 | [MixerCSeg: An Efficient Mixer Architecture for Crack Segmentation via Decoupled Mamba Attention](https://arxiv.org/abs/2603.01361v1) | 2603.01361v1 | 6 |
| 2026-03-01 | [Efficient Extractive Summarization with MAMBA-Transformer Hybrids for Low-Resource Scenarios](https://arxiv.org/abs/2603.01288v1) | 2603.01288v1 | 11 |
| 2026-03-01 | [VP-Hype: A Hybrid Mamba-Transformer Framework with Visual-Textual Prompting for Hyperspectral Image Classification](https://arxiv.org/abs/2603.01174v1) | 2603.01174v1 | 13 |
| 2026-03-01 | [GRAD-Former: Gated Robust Attention-based Differential Transformer for Change Detection](https://arxiv.org/abs/2603.01161v1) | 2603.01161v1 | 6 |
| 2026-03-01 | [VEMamba: Efficient Isotropic Reconstruction of Volume Electron Microscopy with Axial-Lateral Consistent Mamba](https://arxiv.org/abs/2603.00887v2) | 2603.00887v2 | 6 |
| 2026-03-01 | [PPC-MT: Parallel Point Cloud Completion with Mamba-Transformer Hybrid Architecture](https://arxiv.org/abs/2603.00870v1) | 2603.00870v1 | 12 |
| 2026-02-28 | [Mamba-CAD: State Space Model For 3D Computer-Aided Design Generative Modeling](https://arxiv.org/abs/2603.00439v1) | 2603.00439v1 | 12 |
| 2026-02-27 | [Stateful Token Reduction for Long-Video Hybrid VLMs](https://arxiv.org/abs/2603.00198v2) | 2603.00198v2 | 6 |
| 2026-02-26 | [SpectralMamba-UNet: Frequency-Disentangled State Space Modeling for Texture-Structure Consistent Medical Image Segmentation](https://arxiv.org/abs/2602.23103v1) | 2602.23103v1 | 12 |
| 2026-02-26 | [SPMamba-YOLO: An Underwater Object Detection Network Based on Multi-Scale Feature Enhancement and Global Context Modeling](https://arxiv.org/abs/2602.22674v1) | 2602.22674v1 | 10 |
| 2026-02-25 | [Moving Speaker Separation via Parallel Spectral-Spatial Processing](https://arxiv.org/abs/2602.22487v1) | 2602.22487v1 | 6 |
| 2026-02-25 | [Scan Clusters, Not Pixels: A Cluster-Centric Paradigm for Efficient Ultra-high-definition Image Restoration](https://arxiv.org/abs/2602.21917v2) | 2602.21917v2 | 8 |
| 2026-02-25 | [Mamba Meets Scheduling: Learning to Solve Flexible Job Shop Scheduling with Efficient Sequence Modeling](https://arxiv.org/abs/2602.21546v1) | 2602.21546v1 | 9 |
| 2026-02-24 | [Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting](https://arxiv.org/abs/2602.21415v3) | 2602.21415v3 | 13 |
| 2026-02-24 | [HiPPO Zoo: Explicit Memory Mechanisms for Interpretable State Space Models](https://arxiv.org/abs/2602.21340v2) | 2602.21340v2 | 12 |
| 2026-02-24 | [Rethinking Efficiency in Neural Combinatorial Optimization: Batched Preference Optimization with Mamba](https://arxiv.org/abs/2602.20730v3) | 2602.20730v3 | 6 |
| 2026-02-24 | [PFGNet: A Fully Convolutional Frequency-Guided Peripheral Gating Network for Efficient Spatiotemporal Predictive Learning](https://arxiv.org/abs/2602.20537v3) | 2602.20537v3 | 6 |
| 2026-02-23 | [CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction](https://arxiv.org/abs/2602.22236v1) | 2602.22236v1 | 6 |
| 2026-02-23 | [Decision MetaMamba: Enhancing Selective SSM in Offline RL with Heterogeneous Sequence Mixing](https://arxiv.org/abs/2602.19805v2) | 2602.19805v2 | 6 |
| 2026-02-23 | [Fore-Mamba3D: Mamba-based Foreground-Enhanced Encoding for 3D Object Detection](https://arxiv.org/abs/2602.19536v1) | 2602.19536v1 | 6 |
| 2026-02-21 | [NeXt2Former-CD: Efficient Remote Sensing Change Detection with Modern Vision Architectures](https://arxiv.org/abs/2602.18717v1) | 2602.18717v1 | 8 |
| 2026-02-19 | [COMBA: Cross Batch Aggregation for Learning Large Graphs with Context Gating State Space Models](https://arxiv.org/abs/2602.17893v1) | 2602.17893v1 | 6 |
| 2026-02-19 | [Bayesian Optimality of In-Context Learning with Selective State Spaces](https://arxiv.org/abs/2602.17744v1) | 2602.17744v1 | 7 |
| 2026-02-18 | [StereoAdapter-2: Globally Structure-Consistent Underwater Stereo Depth Estimation](https://arxiv.org/abs/2602.16915v1) | 2602.16915v1 | 6 |
| 2026-02-16 | [Is Mamba Reliable for Medical Imaging?](https://arxiv.org/abs/2602.16723v1) | 2602.16723v1 | 7 |
| 2026-02-14 | [NeuroMambaLLM: Dynamic Graph Learning of fMRI Functional Connectivity in Autistic Brains Using Mamba and Language Model Reasoning](https://arxiv.org/abs/2602.13770v3) | 2602.13770v3 | 6 |
| 2026-02-13 | [Frequency-Enhanced Hilbert Scanning Mamba for Short-Term Arctic Sea Ice Concentration Prediction](https://arxiv.org/abs/2602.13522v1) | 2602.13522v1 | 8 |
| 2026-02-13 | [A Theoretical Analysis of Mamba's Training Dynamics: Filtering Relevant Features for Generalization in State Space Models](https://arxiv.org/abs/2602.12499v1) | 2602.12499v1 | 16 |
| 2026-02-12 | [Tiny Recursive Reasoning with Mamba-2 Attention Hybrid](https://arxiv.org/abs/2602.12078v2) | 2602.12078v2 | 6 |
| 2026-02-12 | [Improved state mixing in higher-order and block diagonal linear recurrent networks](https://arxiv.org/abs/2602.12021v2) | 2602.12021v2 | 13 |
| 2026-02-12 | [RAM-Net: Linear-Time Sequence Modeling with Sparsely Addressable State](https://arxiv.org/abs/2602.11958v2) | 2602.11958v2 | 12 |
| 2026-02-12 | [RI-Mamba: Rotation-Invariant Mamba for Robust Text-to-Shape Retrieval](https://arxiv.org/abs/2602.11673v1) | 2602.11673v1 | 6 |
| 2026-02-12 | [TC-BiMamba: Trans-Chunk bidirectionally within BiMamba for unified streaming and non-streaming ASR](https://arxiv.org/abs/2602.11546v2) | 2602.11546v2 | 6 |
| 2026-02-12 | [Real-Time Proactive Anomaly Detection via Forward and Backward Forecast Modeling](https://arxiv.org/abs/2602.11539v1) | 2602.11539v1 | 6 |
| 2026-02-11 | [LaSSM: Efficient Semantic-Spatial Query Decoding via Local Aggregation and State Space Models for 3D Instance Segmentation](https://arxiv.org/abs/2602.11007v1) | 2602.11007v1 | 6 |
| 2026-02-11 | [Bridging the Compression-Precision Paradox: A Hybrid Architecture for Clinical EEG Report Generation with Guaranteed Measurement Accuracy](https://arxiv.org/abs/2602.10544v1) | 2602.10544v1 | 6 |
| 2026-02-10 | [BabyMamba-HAR: Lightweight Selective State Space Models for Efficient Human Activity Recognition on Resource Constrained Devices](https://arxiv.org/abs/2602.09872v2) | 2602.09872v2 | 15 |
| 2026-02-10 | [Mag-Mamba: Modeling Coupled spatiotemporal Asymmetry for POI Recommendation](https://arxiv.org/abs/2603.00053v1) | 2603.00053v1 | 6 |
| 2026-02-09 | [DMamba: Decomposition-enhanced Mamba for Time Series Forecasting](https://arxiv.org/abs/2602.09081v1) | 2602.09081v1 | 10 |
| 2026-02-09 | [Learning to Remember, Learn, and Forget in Attention-Based Models](https://arxiv.org/abs/2602.09075v4) | 2602.09075v4 | 6 |
| 2026-02-09 | [Input-Adaptive Spectral Feature Compression by Sequence Modeling for Source Separation](https://arxiv.org/abs/2602.08671v1) | 2602.08671v1 | 7 |
| 2026-02-09 | [DriveMamba: Task-Centric Scalable State Space Model for Efficient End-to-End Autonomous Driving](https://arxiv.org/abs/2602.13301v2) | 2602.13301v2 | 12 |
| 2026-02-09 | [Physiologically Informed Deep Learning: A Multi-Scale Framework for Next-Generation PBPK Modeling](https://arxiv.org/abs/2602.18472v1) | 2602.18472v1 | 6 |
| 2026-02-08 | [MambaFusion: Adaptive State-Space Fusion for Multimodal 3D Object Detection](https://arxiv.org/abs/2602.08126v2) | 2602.08126v2 | 7 |
| 2026-02-07 | [On Sequence-to-Sequence Models for Automated Log Parsing](https://arxiv.org/abs/2602.07698v2) | 2602.07698v2 | 6 |
| 2026-02-06 | [Behavior Score Prediction in Resting-State Functional MRI by Deep State Space Modeling](https://arxiv.org/abs/2602.07131v2) | 2602.07131v2 | 6 |
| 2026-02-06 | [Towards Understanding What State Space Models Learn About Code](https://arxiv.org/abs/2602.06774v2) | 2602.06774v2 | 6 |
| 2026-02-06 | [AS-Mamba: Asymmetric Self-Guided Mamba Decoupled Iterative Network for Metal Artifact Reduction](https://arxiv.org/abs/2602.06350v1) | 2602.06350v1 | 10 |
| 2026-02-05 | [MambaVF: State Space Model for Efficient Video Fusion](https://arxiv.org/abs/2602.06017v2) | 2602.06017v2 | 12 |
| 2026-02-05 | [A Decomposition-based State Space Model for Multivariate Time-Series Forecasting](https://arxiv.org/abs/2602.05389v1) | 2602.05389v1 | 6 |
| 2026-02-05 | [HealthMamba: An Uncertainty-aware Spatiotemporal Graph State Space Model for Effective and Reliable Healthcare Facility Visit Prediction](https://arxiv.org/abs/2602.05286v4) | 2602.05286v4 | 12 |
| 2026-02-04 | [XtraLight-MedMamba for Classification of Neoplastic Tubular Adenomas](https://arxiv.org/abs/2602.04819v5) | 2602.04819v5 | 6 |
| 2026-02-04 | [Interactive Spatial-Frequency Fusion Mamba for Multi-Modal Image Fusion](https://arxiv.org/abs/2602.04405v1) | 2602.04405v1 | 6 |
| 2026-02-04 | [Partial Ring Scan: Revisiting Scan Order in Vision State Space Models](https://arxiv.org/abs/2602.04170v2) | 2602.04170v2 | 12 |
| 2026-02-04 | [DMS2F-HAD: A Dual-branch Mamba-based Spatial-Spectral Fusion Network for Hyperspectral Anomaly Detection](https://arxiv.org/abs/2602.04102v1) | 2602.04102v1 | 7 |
| 2026-02-02 | [A Multi-scale Linear-time Encoder for Whole-Slide Image Analysis](https://arxiv.org/abs/2602.02918v1) | 2602.02918v1 | 9 |
| 2026-02-02 | [A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention](https://arxiv.org/abs/2602.01763v1) | 2602.01763v1 | 6 |
| 2026-02-02 | [DenVisCoM: Dense Vision Correspondence Mamba for Efficient and Real-time Optical Flow and Stereo Estimation](https://arxiv.org/abs/2602.01724v1) | 2602.01724v1 | 10 |
| 2026-02-02 | [SMTrack: State-Aware Mamba for Efficient Temporal Modeling in Visual Tracking](https://arxiv.org/abs/2602.01677v1) | 2602.01677v1 | 10 |
| 2026-02-02 | [ASGMamba: Adaptive Spectral Gating Mamba for Multivariate Time Series Forecasting](https://arxiv.org/abs/2602.01668v1) | 2602.01668v1 | 10 |
| 2026-02-02 | [Samba+: General and Accurate Salient Object Detection via A More Unified Mamba-based Framework](https://arxiv.org/abs/2602.01593v1) | 2602.01593v1 | 6 |
| 2026-02-02 | [HandMCM: Multi-modal Point Cloud-based Correspondence State Space Model for 3D Hand Pose Estimation](https://arxiv.org/abs/2602.01586v2) | 2602.01586v2 | 10 |
| 2026-02-02 | [Rotation-free Online Handwritten Character Recognition Using Linear Recurrent Units](https://arxiv.org/abs/2602.01533v2) | 2602.01533v2 | 7 |
| 2026-02-01 | [BioTamperNet: Affinity-Guided State-Space Model Detecting Tampered Biomedical Images](https://arxiv.org/abs/2602.01435v2) | 2602.01435v2 | 6 |
| 2026-02-01 | [T2M Mamba: Motion Periodicity-Saliency Coupling Approach for Stable Text-Driven Motion Generation](https://arxiv.org/abs/2602.01352v2) | 2602.01352v2 | 6 |
| 2026-01-31 | [Physics-informed Diffusion Mamba Transformer for Real-world Driving](https://arxiv.org/abs/2602.00808v1) | 2602.00808v1 | 6 |
| 2026-01-31 | [A Hybrid Mamba-SAM Architecture for Efficient 3D Medical Image Segmentation](https://arxiv.org/abs/2602.00650v1) | 2602.00650v1 | 15 |
| 2026-01-31 | [AIRE-Prune: Asymptotic Impulse-Response Energy for State Pruning in State Space Models](https://arxiv.org/abs/2602.00534v1) | 2602.00534v1 | 6 |
| 2026-01-30 | [GaussianOcc3D: A Gaussian-Based Adaptive Multi-modal 3D Occupancy Prediction](https://arxiv.org/abs/2601.22729v1) | 2601.22729v1 | 10 |
| 2026-01-30 | [Elastic Spectral State Space Models for Train-Once Budgeted Inference](https://arxiv.org/abs/2601.22488v4) | 2601.22488v4 | 8 |
| 2026-01-29 | [NetMamba+: A Framework of Pre-trained Models for Efficient and Accurate Network Traffic Classification](https://arxiv.org/abs/2601.21792v1) | 2601.21792v1 | 6 |
| 2026-01-29 | [CAF-Mamba: Mamba-Based Cross-Modal Adaptive Attention Fusion for Multimodal Depression Detection](https://arxiv.org/abs/2601.21648v2) | 2601.21648v2 | 6 |
| 2026-01-29 | [MAR: Efficient Large Language Models via Module-aware Architecture Refinement](https://arxiv.org/abs/2601.21503v1) | 2601.21503v1 | 7 |
| 2026-01-29 | [Towards Geometry-Aware and Motion-Guided Video Human Mesh Recovery](https://arxiv.org/abs/2601.21376v1) | 2601.21376v1 | 8 |
| 2026-01-29 | [Mam-App: A Novel Parameter-Efficient Mamba Model for Apple Leaf Disease Classification](https://arxiv.org/abs/2601.21307v1) | 2601.21307v1 | 6 |
| 2026-01-29 | [Reliability-Calibrated Edge-IoT Early Fault Warning for Rotating Machinery with a Physics-Guided Tiny-Mamba Transformer](https://arxiv.org/abs/2601.21293v3) | 2601.21293v3 | 6 |
| 2026-01-29 | [Model-Free Neural Filtering: A Comparison with Classical Filters in Nonlinear Systems](https://arxiv.org/abs/2601.21266v3) | 2601.21266v3 | 6 |
| 2026-01-28 | [CLEAR-Mamba:Towards Accurate, Adaptive and Trustworthy Multi-Sequence Ophthalmic Angiography Classification](https://arxiv.org/abs/2601.20601v3) | 2601.20601v3 | 6 |
| 2026-01-28 | [CCMamba: Topologically-Informed Selective State-Space Networks on Combinatorial Complexes for Higher-Order Graph Learning](https://arxiv.org/abs/2601.20518v2) | 2601.20518v2 | 6 |
| 2026-01-27 | [Dual-Strategy-Enhanced ConBiMamba for Neural Speaker Diarization](https://arxiv.org/abs/2601.19472v1) | 2601.19472v1 | 6 |
| 2026-01-27 | [On the Expressiveness of State Space Models via Temporal Logics](https://arxiv.org/abs/2601.19467v1) | 2601.19467v1 | 6 |
| 2026-01-27 | [DREAMSTATE: Diffusing States and Parameters for Recurrent Large Language Models](https://arxiv.org/abs/2601.19221v1) | 2601.19221v1 | 11 |
| 2026-01-24 | [Fluxamba: Topology-Aware Anisotropic State Space Models for Geological Lineament Segmentation in Multi-Source Remote Sensing](https://arxiv.org/abs/2601.17288v1) | 2601.17288v1 | 6 |
| 2026-01-23 | [Hybrid Mamba-Attention Neural Architecture for Channel Estimation](https://arxiv.org/abs/2601.17108v3) | 2601.17108v3 | 6 |
| 2026-01-23 | [PENGUIN: General Vital Sign Reconstruction from PPG with Flow Matching State Space Model](https://arxiv.org/abs/2602.03858v1) | 2602.03858v1 | 6 |
| 2026-01-23 | [PanopMamba: Vision State Space Modeling for Nuclei Panoptic Segmentation](https://arxiv.org/abs/2601.16631v1) | 2601.16631v1 | 12 |
| 2026-01-23 | [Omni-directional attention mechanism based on Mamba for speech separation](https://arxiv.org/abs/2601.16603v1) | 2601.16603v1 | 6 |
| 2026-01-22 | [When to Think Fast and Slow? AMOR: Adaptive Entropy Gate for Hybrid Models](https://arxiv.org/abs/2602.13215v3) | 2602.13215v3 | 14 |
| 2026-01-22 | [Clustering-Guided Spatial-Spectral Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2601.16098v1) | 2601.16098v1 | 6 |
| 2026-01-22 | [NeuroMamba: Multi-Perspective Feature Interaction with Visual Mamba for Neuron Segmentation](https://arxiv.org/abs/2601.15929v1) | 2601.15929v1 | 6 |
| 2026-01-21 | [UBATrack: Spatio-Temporal State Space Model for General Multi-Modal Tracking](https://arxiv.org/abs/2601.14799v1) | 2601.14799v1 | 12 |
| 2026-01-21 | [M2I2HA: Multi-modal Object Detection Based on Intra- and Inter-Modal Hypergraph Attention](https://arxiv.org/abs/2601.14776v3) | 2601.14776v3 | 8 |
| 2026-01-20 | [PAS-Mamba: Phase-Amplitude-Spatial State Space Model for MRI Reconstruction](https://arxiv.org/abs/2601.14530v1) | 2601.14530v1 | 12 |
| 2026-01-20 | [Gaussian Based Adaptive Multi-Modal 3D Semantic Occupancy Prediction](https://arxiv.org/abs/2601.14448v1) | 2601.14448v1 | 10 |
| 2026-01-20 | [ASBA: A-line State Space Model and B-line Attention for Sparse Optical Doppler Tomography Reconstruction](https://arxiv.org/abs/2601.14165v1) | 2601.14165v1 | 6 |
| 2026-01-19 | [On the Relation of State Space Models and Hidden Markov Models](https://arxiv.org/abs/2601.13357v1) | 2601.13357v1 | 10 |
| 2026-01-19 | [ConvMambaNet: A Hybrid CNN-Mamba State Space Architecture for Accurate and Real-Time EEG Seizure Detection](https://arxiv.org/abs/2601.13234v1) | 2601.13234v1 | 12 |
| 2026-01-19 | [Analysis of Long Range Dependency Understanding in State Space Models](https://arxiv.org/abs/2601.13048v1) | 2601.13048v1 | 6 |
| 2026-01-19 | [StyMam: A Mamba-Based Generator for Artistic Style Transfer](https://arxiv.org/abs/2601.12954v3) | 2601.12954v3 | 6 |
| 2026-01-17 | [A method for detecting spatio-temporal correlation anomalies of WSN nodes based on topological information enhancement and time-frequency feature extraction](https://arxiv.org/abs/2601.11951v2) | 2601.11951v2 | 6 |
| 2026-01-16 | [FTDMamba: Frequency-Assisted Temporal Dilation Mamba for Unmanned Aerial Vehicle Video Anomaly Detection](https://arxiv.org/abs/2601.11254v1) | 2601.11254v1 | 8 |
| 2026-01-14 | [Late Breaking Results: Quamba-SE: Soft-edge Quantizer for Activations in State Space Models](https://arxiv.org/abs/2601.09451v1) | 2601.09451v1 | 10 |
| 2026-01-13 | [SfMamba: Efficient Source-Free Domain Adaptation via Selective Scan Modeling](https://arxiv.org/abs/2601.08608v1) | 2601.08608v1 | 6 |
| 2026-01-13 | [Scalable Sequential Recommendation under Latency and Memory Constraints](https://arxiv.org/abs/2601.08360v2) | 2601.08360v2 | 9 |
| 2026-01-13 | [M3SR: Multi-Scale Multi-Perceptual Mamba for Efficient Spectral Reconstruction](https://arxiv.org/abs/2601.08293v1) | 2601.08293v1 | 6 |
| 2026-01-09 | [DIFF-MF: A Difference-Driven Channel-Spatial State Space Model for Multi-Modal Image Fusion](https://arxiv.org/abs/2601.05538v1) | 2601.05538v1 | 6 |
| 2026-01-09 | [DeMa: Dual-Path Delay-Aware Mamba for Efficient Multivariate Time Series Analysis](https://arxiv.org/abs/2601.05527v2) | 2601.05527v2 | 9 |
| 2026-01-08 | [Akasha 2: Hamiltonian State Space Duality and Visual-Language Joint Embedding Predictive Architectur](https://arxiv.org/abs/2601.06212v2) | 2601.06212v2 | 10 |
| 2026-01-08 | [DB-MSMUNet:Dual Branch Multi-scale Mamba UNet for Pancreatic CT Scans Segmentation](https://arxiv.org/abs/2601.04676v1) | 2601.04676v1 | 10 |
| 2026-01-08 | [HUR-MACL: High-Uncertainty Region-Guided Multi-Architecture Collaborative Learning for Head and Neck Multi-Organ Segmentation](https://arxiv.org/abs/2601.04607v1) | 2601.04607v1 | 8 |
| 2026-01-06 | [Listen to Rhythm, Choose Movements: Autoregressive Multimodal Dance Generation via Diffusion and Mamba with Decoupled Dance Dataset](https://arxiv.org/abs/2601.03323v3) | 2601.03323v3 | 6 |
| 2026-01-06 | [XLSR-MamBo: Scaling the Hybrid Mamba-Attention Backbone for Audio Deepfake Detection](https://arxiv.org/abs/2601.02944v3) | 2601.02944v3 | 18 |
| 2026-01-05 | [Shallow- and Deep-fake Image Manipulation Localization Using Vision Mamba and Guided Graph Neural Network](https://arxiv.org/abs/2601.02566v1) | 2601.02566v1 | 6 |
| 2026-01-05 | [Scalable Gaussian Processes for Integrated and Overlapping Measurements Via Augmented State Space Models](https://arxiv.org/abs/2601.02527v2) | 2601.02527v2 | 6 |
| 2026-01-05 | [A Mamba-Based Model for Automatic Chord Recognition](https://arxiv.org/abs/2601.02101v1) | 2601.02101v1 | 6 |
| 2026-01-05 | [Hidden State Poisoning Attacks against Mamba-based Language Models](https://arxiv.org/abs/2601.01972v5) | 2601.01972v5 | 10 |
| 2026-01-04 | [Reliable Grid Forecasting: State Space Models for Safety-Critical Energy Systems](https://arxiv.org/abs/2601.01410v6) | 2601.01410v6 | 10 |
| 2026-01-03 | [MambaFormer: Token-Level Guided Routing Mixture-of-Experts for Accurate and Efficient Clinical Assistance](https://arxiv.org/abs/2601.01260v1) | 2601.01260v1 | 11 |
| 2026-01-03 | [Benchmarking the Computational and Representational Efficiency of State Space Models against Transformers on Long-Context Dyadic Sessions](https://arxiv.org/abs/2601.01237v1) | 2601.01237v1 | 12 |
| 2026-01-02 | [SpikySpace: A Spiking State Space Model for Energy-Efficient Time Series Forecasting](https://arxiv.org/abs/2601.02411v2) | 2601.02411v2 | 8 |
| 2026-01-01 | [Depth-Synergized Mamba Meets Memory Experts for All-Day Image Reflection Separation](https://arxiv.org/abs/2601.00322v1) | 2601.00322v1 | 6 |
| 2026-01-01 | [MODE: Efficient Time Series Prediction with Mamba Enhanced by Low-Rank Neural ODEs](https://arxiv.org/abs/2601.00920v2) | 2601.00920v2 | 8 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-30 | [MambaSeg: Harnessing Mamba for Accurate and Efficient Image-Event Semantic Segmentation](https://arxiv.org/abs/2512.24243v1) | 2512.24243v1 | 6 |
| 2025-12-30 | [Bridging the Perception-Cognition Gap:Re-engineering SAM2 with Hilbert-Mamba for Robust VLM-based Medical Diagnosis](https://arxiv.org/abs/2512.24013v1) | 2512.24013v1 | 10 |
| 2025-12-29 | [MS-SSM: A Multi-Scale State Space Model for Efficient Sequence Modeling](https://arxiv.org/abs/2512.23824v1) | 2512.23824v1 | 9 |
| 2025-12-29 | [Hierarchical Decision Mamba Meets Agentic AI: A Novel Approach for RAN Slicing in 6G](https://arxiv.org/abs/2512.23502v2) | 2512.23502v2 | 6 |
| 2025-12-28 | [Breaking the Memory Wall: Exact Analytical Differentiation via Tiled Operator-Space Evolution](https://arxiv.org/abs/2512.23068v1) | 2512.23068v1 | 7 |
| 2025-12-27 | [MEGA-PCC: A Mamba-based Efficient Approach for Joint Geometry and Attribute Point Cloud Compression](https://arxiv.org/abs/2512.22463v1) | 2512.22463v1 | 6 |
| 2025-12-25 | [CellMamba: Adaptive Mamba for Accurate and Efficient Cell Detection](https://arxiv.org/abs/2512.21803v1) | 2512.21803v1 | 6 |
| 2025-12-25 | [UltraLBM-UNet: Ultralight Bidirectional Mamba-based Model for Skin Lesion Segmentation](https://arxiv.org/abs/2512.21584v1) | 2512.21584v1 | 6 |
| 2025-12-24 | [FluencyVE: Marrying Temporal-Aware Mamba with Bypass Attention for Video Editing](https://arxiv.org/abs/2512.21015v2) | 2512.21015v2 | 6 |
| 2025-12-24 | [Self-supervised Multiplex Consensus Mamba for General Image Fusion](https://arxiv.org/abs/2512.20921v1) | 2512.20921v1 | 6 |
| 2025-12-23 | [Nemotron 3 Nano: Open, Efficient Mixture-of-Experts Hybrid Mamba-Transformer Model for Agentic Reasoning](https://arxiv.org/abs/2512.20848v1) | 2512.20848v1 | 6 |
| 2025-12-23 | [Distilling to Hybrid Attention Models via KL-Guided Layer Selection](https://arxiv.org/abs/2512.20569v1) | 2512.20569v1 | 6 |
| 2025-12-23 | [milliMamba: Specular-Aware Human Pose Estimation via Dual mmWave Radar with Multi-Frame Mamba Fusion](https://arxiv.org/abs/2512.20128v1) | 2512.20128v1 | 6 |
| 2025-12-22 | [Efficient Vision Mamba for MRI Super-Resolution via Hybrid Selective Scanning](https://arxiv.org/abs/2512.19676v3) | 2512.19676v3 | 6 |
| 2025-12-22 | [Interpretable Hybrid Deep Q-Learning Framework for IoT-Based Food Spoilage Prediction with Synthetic Data Generation and Hardware Validation](https://arxiv.org/abs/2512.19361v1) | 2512.19361v1 | 6 |
| 2025-12-22 | [Mamba-Based Modality Disentanglement Network for Multi-Contrast MRI Reconstruction](https://arxiv.org/abs/2512.19095v1) | 2512.19095v1 | 6 |
| 2025-12-22 | [Lag Operator SSMs: A Geometric Framework for Structured State Space Modeling](https://arxiv.org/abs/2512.18965v2) | 2512.18965v2 | 12 |
| 2025-12-21 | [Rectification Reimagined: A Unified Mamba Model for Image Correction and Rectangling with Prompts](https://arxiv.org/abs/2512.18718v3) | 2512.18718v3 | 6 |
| 2025-12-20 | [MACE-Dance: Motion-Appearance Cascaded Experts for Music-Driven Dance Video Generation](https://arxiv.org/abs/2512.18181v3) | 2512.18181v3 | 8 |
| 2025-12-19 | [MambaMIL+: Modeling Long-Term Contextual Patterns for Gigapixel Whole Slide Image](https://arxiv.org/abs/2512.17726v1) | 2512.17726v1 | 6 |
| 2025-12-19 | [Spatially-informed transformers: Injecting geostatistical covariance biases into self-attention for spatio-temporal forecasting](https://arxiv.org/abs/2512.17696v1) | 2512.17696v1 | 6 |
| 2025-12-19 | [Physics of Language Models: Part 4.1, Architecture Design and the Magic of Canon Layers](https://arxiv.org/abs/2512.17351v2) | 2512.17351v2 | 6 |
| 2025-12-19 | [WDFFU-Mamba: A Wavelet-guided Dual-attention Feature Fusion Mamba for Breast Tumor Segmentation in Ultrasound Images](https://arxiv.org/abs/2512.17278v1) | 2512.17278v1 | 6 |
| 2025-12-18 | [KineST: A Kinematics-guided Spatiotemporal State Space Model for Human Motion Tracking from Sparse Signals](https://arxiv.org/abs/2512.16791v1) | 2512.16791v1 | 6 |
| 2025-12-18 | [KOSS: Kalman-Optimal Selective State Spaces for Long-Term Sequence Modeling](https://arxiv.org/abs/2512.16723v1) | 2512.16723v1 | 14 |
| 2025-12-18 | [CPMamba: Selective State Space Models for MIMO Channel Prediction in High-Mobility Environments](https://arxiv.org/abs/2512.16315v1) | 2512.16315v1 | 15 |
| 2025-12-17 | [BarcodeMamba+: Advancing State-Space Models for Fungal Biodiversity Research](https://arxiv.org/abs/2512.15931v1) | 2512.15931v1 | 6 |
| 2025-12-17 | [Characterizing Mamba's Selective Memory using Auto-Encoders](https://arxiv.org/abs/2512.15653v1) | 2512.15653v1 | 10 |
| 2025-12-17 | [PaperNet: Efficient Temporal Convolutions and Channel Residual Attention for EEG Epilepsy Detection](https://arxiv.org/abs/2512.22172v1) | 2512.22172v1 | 6 |
| 2025-12-17 | [MMMamba: A Versatile Cross-Modal In Context Fusion Framework for Pan-Sharpening and Zero-Shot Image Enhancement](https://arxiv.org/abs/2512.15261v1) | 2512.15261v1 | 6 |
| 2025-12-17 | [How Many Heads Make an SSM? A Unified Framework for Attention and State Space Models](https://arxiv.org/abs/2512.15115v1) | 2512.15115v1 | 10 |
| 2025-12-16 | [Kinetic-Mamba: Mamba-Assisted Predictions of Stiff Chemical Kinetics](https://arxiv.org/abs/2512.14471v2) | 2512.14471v2 | 6 |
| 2025-12-16 | [PSMamba: Progressive Self-supervised Vision Mamba for Plant Disease Recognition](https://arxiv.org/abs/2512.14309v1) | 2512.14309v1 | 6 |
| 2025-12-13 | [HydroDiffusion: Diffusion-Based Probabilistic Streamflow Forecasting with a State Space Backbone](https://arxiv.org/abs/2512.12183v1) | 2512.12183v1 | 6 |
| 2025-12-12 | [TSkel-Mamba: Temporal Dynamic Modeling via State Space Model for Human Skeleton-based Action Recognition](https://arxiv.org/abs/2512.11503v1) | 2512.11503v1 | 12 |
| 2025-12-11 | [Hybrid Transformer-Mamba for Weakly Supervised Volumetric Medical Segmentation](https://arxiv.org/abs/2512.10353v2) | 2512.10353v2 | 7 |
| 2025-12-08 | [UltrasODM: A Dual Stream Optical Flow Mamba Network for 3D Freehand Ultrasound Reconstruction](https://arxiv.org/abs/2512.07756v1) | 2512.07756v1 | 6 |
| 2025-12-08 | [How Far are Modern Trackers from UAV-Anti-UAV? A Million-Scale Benchmark and New Baseline](https://arxiv.org/abs/2512.07385v1) | 2512.07385v1 | 10 |
| 2025-12-08 | [Dual Refinement Cycle Learning: Unsupervised Text Classification of Mamba and Community Detection on Text Attributed Graph](https://arxiv.org/abs/2512.07100v2) | 2512.07100v2 | 6 |
| 2025-12-07 | [TextMamba: Scene Text Detector with Mamba](https://arxiv.org/abs/2512.06657v1) | 2512.06657v1 | 10 |
| 2025-12-03 | [Traffic Image Restoration under Adverse Weather via Frequency-Aware Mamba](https://arxiv.org/abs/2512.03852v1) | 2512.03852v1 | 8 |
| 2025-12-03 | [State Space Models for Bioacoustics: A Comparative Evaluation with Transformers](https://arxiv.org/abs/2512.03563v2) | 2512.03563v2 | 10 |
| 2025-12-03 | [DM3D: Dynamic Mamba via Offset-Guided Feature Resampling for Point Cloud Understanding](https://arxiv.org/abs/2512.03424v4) | 2512.03424v4 | 10 |
| 2025-12-03 | [UniQL: Unified Quantization and Low-rank Compression for Adaptive Edge LLMs](https://arxiv.org/abs/2512.03383v3) | 2512.03383v3 | 8 |
| 2025-12-02 | [MICCAI STSR 2025 Challenge: Semi-Supervised Teeth and Pulp Segmentation and CBCT-IOS Registration](https://arxiv.org/abs/2512.02867v1) | 2512.02867v1 | 8 |
| 2025-12-02 | [DF-Mamba: Deformable State Space Modeling for 3D Hand Pose Estimation in Interactions](https://arxiv.org/abs/2512.02727v1) | 2512.02727v1 | 12 |
| 2025-12-01 | [ViT$^3$: Unlocking Test-Time Training in Vision](https://arxiv.org/abs/2512.01643v2) | 2512.01643v2 | 8 |
| 2025-12-01 | [MasHeNe: A Benchmark for Head and Neck CT Mass Segmentation using Window-Enhanced Mamba with Frequency-Domain Integration](https://arxiv.org/abs/2512.01563v2) | 2512.01563v2 | 6 |
| 2025-12-01 | [Language as a Wave Phenomenon: Semantic Phase Locking and Interference in Neural Networks](https://arxiv.org/abs/2512.01208v5) | 2512.01208v5 | 6 |
| 2025-11-30 | [A Hybrid Architecture for Options Wheel Strategy Decisions: LLM-Generated Bayesian Networks for Transparent Trading](https://arxiv.org/abs/2512.01123v1) | 2512.01123v1 | 6 |
| 2025-11-30 | [Sleep Apnea Detection on a Wireless Multimodal Wearable Device Without Oxygen Flow Using a Mamba-based Deep Learning Approach](https://arxiv.org/abs/2512.00989v1) | 2512.00989v1 | 6 |
| 2025-11-29 | [MambaScope: Coarse-to-Fine Scoping for Efficient Vision Mamba](https://arxiv.org/abs/2512.00647v2) | 2512.00647v2 | 6 |
| 2025-11-29 | [MM-DETR: An Efficient Multimodal Detection Transformer with Mamba-Driven Dual-Granularity Fusion and Frequency-Aware Modality Adapters](https://arxiv.org/abs/2512.00363v1) | 2512.00363v1 | 6 |
| 2025-11-29 | [SMamDiff: Spatial Mamba for Stochastic Human Motion Prediction](https://arxiv.org/abs/2512.00355v1) | 2512.00355v1 | 6 |
| 2025-11-28 | [ReactionMamba: Generating Short & Long Human Reaction Sequences](https://arxiv.org/abs/2512.00208v2) | 2512.00208v2 | 6 |
| 2025-11-28 | [SmallWorlds: Assessing Dynamics Understanding of World Models in Isolated Environments](https://arxiv.org/abs/2511.23465v1) | 2511.23465v1 | 6 |
| 2025-11-28 | [PerfMamba: Performance Analysis and Pruning of Selective State Space Models](https://arxiv.org/abs/2511.22849v1) | 2511.22849v1 | 17 |
| 2025-11-27 | [Adaptive Dueling Double Deep Q-networks in Uniswap V3 Replication and Extension with Mamba](https://arxiv.org/abs/2511.22101v1) | 2511.22101v1 | 6 |
| 2025-11-26 | [MMA: A Momentum Mamba Architecture for Human Activity Recognition with Inertial Sensors](https://arxiv.org/abs/2511.21550v1) | 2511.21550v1 | 10 |
| 2025-11-26 | [MobileI2V: Fast and High-Resolution Image-to-Video on Mobile Devices](https://arxiv.org/abs/2511.21475v1) | 2511.21475v1 | 6 |
| 2025-11-26 | [PathMamba: A Hybrid Mamba-Transformer for Topologically Coherent Road Segmentation in Satellite Imagery](https://arxiv.org/abs/2511.21298v1) | 2511.21298v1 | 15 |
| 2025-11-26 | [FAIM: Frequency-Aware Interactive Mamba for Time Series Classification](https://arxiv.org/abs/2512.07858v1) | 2512.07858v1 | 6 |
| 2025-11-26 | [Gated KalmaNet: A Fading Memory Layer Through Test-Time Ridge Regression](https://arxiv.org/abs/2511.21016v3) | 2511.21016v3 | 8 |
| 2025-11-25 | [DAPointMamba: Domain Adaptive Point Mamba for Point Cloud Completion](https://arxiv.org/abs/2511.20278v1) | 2511.20278v1 | 10 |
| 2025-11-25 | [MambaEye: A Size-Agnostic Visual Encoder with Causal Sequential Processing](https://arxiv.org/abs/2511.19963v1) | 2511.19963v1 | 10 |
| 2025-11-25 | [Towards Edge General Intelligence: Knowledge Distillation for Mobile Agentic AI](https://arxiv.org/abs/2511.19947v1) | 2511.19947v1 | 8 |
| 2025-11-25 | [ChessMamba: Structure-Aware Interleaving of State Spaces for Change Detection in Remote Sensing Images](https://arxiv.org/abs/2511.19882v1) | 2511.19882v1 | 6 |
| 2025-11-24 | [MambaRefine-YOLO: A Dual-Modality Small Object Detector for UAV Imagery](https://arxiv.org/abs/2511.19134v1) | 2511.19134v1 | 6 |
| 2025-11-24 | [MFmamba: A Multi-function Network for Panchromatic Image Resolution Restoration Based on State-Space Model](https://arxiv.org/abs/2511.18888v1) | 2511.18888v1 | 6 |
| 2025-11-23 | [SAMBA: Toward an EEG Foundation Model via Differential Mamba and Coordinate-Driven Spatial Embedding](https://arxiv.org/abs/2511.18571v2) | 2511.18571v2 | 6 |
| 2025-11-23 | [HiFi-MambaV2: Hierarchical Shared-Routed MoE for High-Fidelity MRI Reconstruction](https://arxiv.org/abs/2511.18534v1) | 2511.18534v1 | 6 |
| 2025-11-23 | [RNN as Linear Transformer: A Closer Investigation into Representational Potentials of Visual Mamba Models](https://arxiv.org/abs/2511.18380v1) | 2511.18380v1 | 8 |
| 2025-11-23 | [DiM-TS: Bridge the Gap between Selective State Space Models and Time Series for Generative Modeling](https://arxiv.org/abs/2511.18312v1) | 2511.18312v1 | 15 |
| 2025-11-22 | [MambaX: Image Super-Resolution with State Predictive Control](https://arxiv.org/abs/2511.18028v2) | 2511.18028v2 | 6 |
| 2025-11-22 | [HyM-UNet: Synergizing Local Texture and Global Context via Hybrid CNN-Mamba Architecture for Medical Image Segmentation](https://arxiv.org/abs/2511.17988v1) | 2511.17988v1 | 10 |
| 2025-11-22 | [Controllability Analysis of State Space-based Language Model](https://arxiv.org/abs/2511.17970v1) | 2511.17970v1 | 6 |
| 2025-11-22 | [CADTrack: Learning Contextual Aggregation with Deformable Alignment for Robust RGBT Tracking](https://arxiv.org/abs/2511.17967v1) | 2511.17967v1 | 8 |
| 2025-11-22 | [Hybrid LSTM and PPO Networks for Dynamic Portfolio Optimization](https://arxiv.org/abs/2511.17963v1) | 2511.17963v1 | 6 |
| 2025-11-22 | [MambaTAD: When State-Space Models Meet Long-Range Temporal Action Detection](https://arxiv.org/abs/2511.17929v2) | 2511.17929v2 | 6 |
| 2025-11-21 | [UAM: A Unified Attention-Mamba Backbone of Multimodal Framework for Tumor Cell Classification](https://arxiv.org/abs/2511.17355v3) | 2511.17355v3 | 6 |
| 2025-11-21 | [Parts-Mamba: Augmenting Joint Context with Part-Level Scanning for Occluded Human Skeleton](https://arxiv.org/abs/2511.16860v1) | 2511.16860v1 | 6 |
| 2025-11-20 | [TimeViper: A Hybrid Mamba-Transformer Vision-Language Model for Efficient Long Video Understanding](https://arxiv.org/abs/2511.16595v2) | 2511.16595v2 | 6 |
| 2025-11-20 | [CausalMamba: Interpretable State Space Modeling for Temporal Rumor Causality](https://arxiv.org/abs/2511.16191v1) | 2511.16191v1 | 14 |
| 2025-11-20 | [MamTiff-CAD: Multi-Scale Latent Diffusion with Mamba+ for Complex Parametric Sequence](https://arxiv.org/abs/2511.17647v1) | 2511.17647v1 | 6 |
| 2025-11-19 | [DiffuMamba: High-Throughput Diffusion LMs with Mamba Backbone](https://arxiv.org/abs/2511.15927v4) | 2511.15927v4 | 9 |
| 2025-11-19 | [Fourier-KAN-Mamba: A Novel State-Space Equation Approach for Time-Series Anomaly Detection](https://arxiv.org/abs/2511.15083v2) | 2511.15083v2 | 12 |
| 2025-11-19 | [MambaTrack3D: A State Space Model Framework for LiDAR-Based Object Tracking under High Temporal Variation](https://arxiv.org/abs/2511.15077v1) | 2511.15077v1 | 12 |
| 2025-11-18 | [Quality-Controlled Multimodal Emotion Recognition in Conversations with Identity-Based Transfer Learning and MAMBA Fusion](https://arxiv.org/abs/2511.14969v1) | 2511.14969v1 | 6 |
| 2025-11-18 | [When CNNs Outperform Transformers and Mambas: Revisiting Deep Architectures for Dental Caries Segmentation](https://arxiv.org/abs/2511.14860v1) | 2511.14860v1 | 6 |
| 2025-11-18 | [Parameter Aware Mamba Model for Multi-task Dense Prediction](https://arxiv.org/abs/2511.14503v1) | 2511.14503v1 | 10 |
| 2025-11-17 | [Compute-in-Memory Implementation of State Space Models for Event Sequence Processing](https://arxiv.org/abs/2511.13912v2) | 2511.13912v2 | 8 |
| 2025-11-17 | [Naga: Vedic Encoding for Deep State Space Models](https://arxiv.org/abs/2511.13510v2) | 2511.13510v2 | 8 |
| 2025-11-17 | [WinMamba: Multi-Scale Shifted Windows in State Space Model for 3D Object Detection](https://arxiv.org/abs/2511.13138v1) | 2511.13138v1 | 12 |
| 2025-11-17 | [Semantics and Content Matter: Towards Multi-Prior Hierarchical Mamba for Image Deraining](https://arxiv.org/abs/2511.13113v1) | 2511.13113v1 | 6 |
| 2025-11-16 | [X-VMamba: Explainable Vision Mamba](https://arxiv.org/abs/2511.12694v1) | 2511.12694v1 | 12 |
| 2025-11-16 | [DensePercept-NCSSD: Vision Mamba towards Real-time Dense Visual Perception with Non-Causal State Space Duality](https://arxiv.org/abs/2511.12671v1) | 2511.12671v1 | 8 |
| 2025-11-15 | [MMRINet: Efficient Mamba-Based Segmentation with Dual-Path Refinement for Low-Resource MRI Analysis](https://arxiv.org/abs/2511.12193v2) | 2511.12193v2 | 6 |
| 2025-11-14 | [BOA Constrictor: A Mamba-based lossless compressor for High Energy Physics data](https://arxiv.org/abs/2511.11337v1) | 2511.11337v1 | 10 |
| 2025-11-14 | [Arcee: Differentiable Recurrent State Chain for Generative Vision Modeling with Mamba SSMs](https://arxiv.org/abs/2511.11243v2) | 2511.11243v2 | 12 |
| 2025-11-13 | [Multitask GLocal OBIA-Mamba for Sentinel-2 Landcover Mapping](https://arxiv.org/abs/2511.10604v1) | 2511.10604v1 | 6 |
| 2025-11-12 | [State Space Modeling of Mortgage Default Rates under Natural Hazard Shocks](https://arxiv.org/abs/2511.09698v1) | 2511.09698v1 | 6 |
| 2025-11-12 | [MPCM-Net: Multi-scale network integrates partial attention convolution with Mamba for ground-based cloud image segmentation](https://arxiv.org/abs/2511.11681v2) | 2511.11681v2 | 6 |
| 2025-11-12 | [SasMamba: A Lightweight Structure-Aware Stride State Space Model for 3D Human Pose Estimation](https://arxiv.org/abs/2511.08872v1) | 2511.08872v1 | 12 |
| 2025-11-11 | [Hybrid Quantum-Classical Selective State Space Artificial Intelligence](https://arxiv.org/abs/2511.08349v1) | 2511.08349v1 | 7 |
| 2025-11-11 | [Filtering Jump Markov Systems with Partially Known Dynamics: A Model-Based Deep Learning Approach](https://arxiv.org/abs/2511.09569v1) | 2511.09569v1 | 6 |
| 2025-11-11 | [ReIDMamba: Learning Discriminative Features with Visual State Space Model for Person Re-Identification](https://arxiv.org/abs/2511.07948v1) | 2511.07948v1 | 12 |
| 2025-11-11 | [CloudMamba: Grouped Selective State Spaces for Point Cloud Analysis](https://arxiv.org/abs/2511.07823v1) | 2511.07823v1 | 13 |
| 2025-11-10 | [A Classical-Quantum Hybrid Architecture for Physics-Informed Neural Networks](https://arxiv.org/abs/2511.07216v1) | 2511.07216v1 | 6 |
| 2025-11-10 | [Mamba-driven multi-perspective structural understanding for molecular ground-state conformation prediction](https://arxiv.org/abs/2511.09564v1) | 2511.09564v1 | 12 |
| 2025-11-10 | [Dual Mamba for Node-Specific Representation Learning: Tackling Over-Smoothing with Selective State Space Modeling](https://arxiv.org/abs/2511.06756v3) | 2511.06756v3 | 15 |
| 2025-11-10 | [MRT: Learning Compact Representations with Mixed RWKV-Transformer for Extreme Image Compression](https://arxiv.org/abs/2511.06717v2) | 2511.06717v2 | 6 |
| 2025-11-10 | [MirrorMamba: Towards Scalable and Robust Mirror Detection in Videos](https://arxiv.org/abs/2511.06716v1) | 2511.06716v1 | 6 |
| 2025-11-10 | [Spatial-Frequency Enhanced Mamba for Multi-Modal Image Fusion](https://arxiv.org/abs/2511.06593v1) | 2511.06593v1 | 6 |
| 2025-11-09 | [MambaOVSR: Multiscale Fusion with Global Motion Modeling for Chinese Opera Video Super-Resolution](https://arxiv.org/abs/2511.06172v1) | 2511.06172v1 | 6 |
| 2025-11-05 | [Enhancing Medical Image Segmentation via Heat Conduction Equation](https://arxiv.org/abs/2511.03260v2) | 2511.03260v2 | 8 |
| 2025-11-05 | [Transformer-Progressive Mamba Network for Lightweight Image Super-Resolution](https://arxiv.org/abs/2511.03232v3) | 2511.03232v3 | 6 |
| 2025-11-04 | [Apriel-H1: Towards Efficient Enterprise Reasoning Models](https://arxiv.org/abs/2511.02651v1) | 2511.02651v1 | 10 |
| 2025-11-04 | [M2S2L: Mamba-based Multi-Scale Spatial-temporal Learning for Video Anomaly Detection](https://arxiv.org/abs/2511.05564v1) | 2511.05564v1 | 6 |
| 2025-11-04 | [MM-UNet: Morph Mamba U-shaped Convolutional Networks for Retinal Vessel Segmentation](https://arxiv.org/abs/2511.02193v2) | 2511.02193v2 | 6 |
| 2025-11-03 | [CMI-MTL: Cross-Mamba interaction based multi-task learning for medical visual question answering](https://arxiv.org/abs/2511.01357v1) | 2511.01357v1 | 6 |
| 2025-11-03 | [MVSMamba: Multi-View Stereo with State Space Model](https://arxiv.org/abs/2511.01315v1) | 2511.01315v1 | 12 |
| 2025-10-31 | [Language Modeling With Factorization Memory](https://arxiv.org/abs/2511.00315v1) | 2511.00315v1 | 6 |
| 2025-10-31 | [Context-Gated Cross-Modal Perception with Visual Mamba for PET-CT Lung Tumor Segmentation](https://arxiv.org/abs/2510.27508v1) | 2510.27508v1 | 6 |
| 2025-10-31 | [Versatile and Efficient Medical Image Super-Resolution Via Frequency-Gated Mamba](https://arxiv.org/abs/2510.27296v1) | 2510.27296v1 | 6 |
| 2025-10-30 | [Understanding and Enhancing Mamba-Transformer Hybrids for Memory Recall and Language Modeling](https://arxiv.org/abs/2510.26912v1) | 2510.26912v1 | 14 |
| 2025-10-29 | [Larger Hausdorff Dimension in Scanning Pattern Facilitates Mamba-Based Methods in Low-Light Image Enhancement](https://arxiv.org/abs/2510.26001v2) | 2510.26001v2 | 6 |
| 2025-10-29 | [MaGNet: A Mamba Dual-Hypergraph Network for Stock Prediction via Temporal-Causal and Global Relational Learning](https://arxiv.org/abs/2511.00085v1) | 2511.00085v1 | 6 |
| 2025-10-29 | [State Space and Self-Attention Collaborative Network with Feature Aggregation for DOA Estimation](https://arxiv.org/abs/2510.25193v1) | 2510.25193v1 | 6 |
| 2025-10-28 | [Language Model Behavioral Phases are Consistent Across Architecture, Training Data, and Scale](https://arxiv.org/abs/2510.24963v1) | 2510.24963v1 | 8 |
| 2025-10-28 | [DeshadowMamba: Deshadowing as 1D Sequential Similarity](https://arxiv.org/abs/2510.24260v1) | 2510.24260v1 | 14 |
| 2025-10-27 | [HieraMamba: Video Temporal Grounding via Hierarchical Anchor-Mamba Pooling](https://arxiv.org/abs/2510.23043v2) | 2510.23043v2 | 6 |
| 2025-10-27 | [Understanding In-Context Learning Beyond Transformers: An Investigation of State Space and Hybrid Architectures](https://arxiv.org/abs/2510.23006v2) | 2510.23006v2 | 10 |
| 2025-10-27 | [Hankel Singular Value Regularization for Highly Compressible State Space Models](https://arxiv.org/abs/2510.22951v2) | 2510.22951v2 | 6 |
| 2025-10-27 | [GTR-Mamba: Geometry-to-Tangent Routing Mamba for Hyperbolic POI Recommendation](https://arxiv.org/abs/2510.22942v2) | 2510.22942v2 | 6 |
| 2025-10-25 | [Multi-dataset Joint Pre-training of Emotional EEG Enables Generalizable Affective Computing](https://arxiv.org/abs/2510.22197v1) | 2510.22197v1 | 6 |
| 2025-10-24 | [ParaRNN: Unlocking Parallel Training of Nonlinear RNNs for Large Language Models](https://arxiv.org/abs/2510.21450v2) | 2510.21450v2 | 12 |
| 2025-10-24 | [WaveSeg: Enhancing Segmentation Precision via High-Frequency Prior and Mamba-Driven Spectrum Decomposition](https://arxiv.org/abs/2510.21079v1) | 2510.21079v1 | 6 |
| 2025-10-23 | [LLM-Integrated Bayesian State Space Models for Multimodal Time-Series Forecasting](https://arxiv.org/abs/2510.20952v1) | 2510.20952v1 | 6 |
| 2025-10-22 | [PRGCN: A Graph Memory Network for Cross-Sequence Pattern Reuse in 3D Human Pose Estimation](https://arxiv.org/abs/2510.19475v2) | 2510.19475v2 | 8 |
| 2025-10-22 | [Data Efficient Any Transformer-to-Mamba Distillation via Attention Bridge](https://arxiv.org/abs/2510.19266v4) | 2510.19266v4 | 8 |
| 2025-10-21 | [Some Attention is All You Need for Retrieval](https://arxiv.org/abs/2510.19861v1) | 2510.19861v1 | 6 |
| 2025-10-21 | [$Δ$t-Mamba3D: A Time-Aware Spatio-Temporal State-Space Model for Breast Cancer Risk Prediction](https://arxiv.org/abs/2510.19003v1) | 2510.19003v1 | 8 |
| 2025-10-21 | [MLMA: Towards Multilingual ASR With Mamba-based Architectures](https://arxiv.org/abs/2510.18684v2) | 2510.18684v2 | 8 |
| 2025-10-21 | [Condition-Invariant fMRI Decoding of Speech Intelligibility with Deep State Space Model](https://arxiv.org/abs/2511.01868v1) | 2511.01868v1 | 6 |
| 2025-10-20 | [TrajMamba: An Efficient and Semantic-rich Vehicle Trajectory Pre-training Model](https://arxiv.org/abs/2510.17545v2) | 2510.17545v2 | 6 |
| 2025-10-20 | [MambaX-Net: Dual-Input Mamba-Enhanced Cross-Attention Network for Longitudinal Prostate MRI Segmentation](https://arxiv.org/abs/2510.17529v3) | 2510.17529v3 | 6 |
| 2025-10-20 | [CausalMamba: Scalable Conditional State Space Models for Neural Causal Inference](https://arxiv.org/abs/2510.17318v1) | 2510.17318v1 | 12 |
| 2025-10-20 | [Mamba4Net: Distilled Hybrid Mamba Large Language Models For Networking](https://arxiv.org/abs/2510.17147v1) | 2510.17147v1 | 6 |
| 2025-10-19 | [Schrödinger Bridge Mamba for One-Step Speech Enhancement](https://arxiv.org/abs/2510.16834v3) | 2510.16834v3 | 6 |
| 2025-10-19 | [EMRRG: Efficient Fine-Tuning Pre-trained X-ray Mamba Networks for Radiology Report Generation](https://arxiv.org/abs/2510.16776v1) | 2510.16776v1 | 6 |
| 2025-10-19 | [WaMaIR: Image Restoration via Multiscale Wavelet Convolutions and Mamba-based Channel Modeling with Texture Enhancement](https://arxiv.org/abs/2510.16765v2) | 2510.16765v2 | 6 |
| 2025-10-19 | [Evaluating protein binding interfaces with PUMBA](https://arxiv.org/abs/2510.16674v1) | 2510.16674v1 | 6 |
| 2025-10-17 | [VM-BeautyNet: A Synergistic Ensemble of Vision Transformer and Mamba for Facial Beauty Prediction](https://arxiv.org/abs/2510.16220v1) | 2510.16220v1 | 6 |
| 2025-10-17 | [Hierarchical Mixing Architecture for Low-light RAW Image Enhancement](https://arxiv.org/abs/2510.15497v2) | 2510.15497v2 | 8 |
| 2025-10-17 | [Cortical-SSM: A Deep State Space Model for Motor Imagery Decoding from EEG Signals](https://arxiv.org/abs/2510.15371v2) | 2510.15371v2 | 6 |
| 2025-10-16 | [EdgeNavMamba: Mamba Optimized Object Detection for Energy Efficient Edge Devices](https://arxiv.org/abs/2510.14946v1) | 2510.14946v1 | 6 |
| 2025-10-16 | [To Infinity and Beyond: Tool-Use Unlocks Length Generalization in State Space Models](https://arxiv.org/abs/2510.14826v1) | 2510.14826v1 | 8 |
| 2025-10-16 | [Vision Mamba for Permeability Prediction of Porous Media](https://arxiv.org/abs/2510.14516v2) | 2510.14516v2 | 6 |
| 2025-10-16 | [DRBD-Mamba for Robust and Efficient Brain Tumor Segmentation with Analytical Insights](https://arxiv.org/abs/2510.14383v4) | 2510.14383v4 | 10 |
| 2025-10-15 | [Context-Selective State Space Models: Feedback is All You Need](https://arxiv.org/abs/2510.14027v2) | 2510.14027v2 | 13 |
| 2025-10-15 | [End-to-End Multi-Modal Diffusion Mamba](https://arxiv.org/abs/2510.13253v1) | 2510.13253v1 | 6 |
| 2025-10-14 | [ECG-Mamba-V2: Architectural Refinements to a Bidirectional State Space Model for Multi-Label 12-Lead ECG Classification](https://arxiv.org/abs/2510.13046v3) | 2510.13046v3 | 15 |
| 2025-10-14 | [Learning Human Motion with Temporally Conditional Mamba](https://arxiv.org/abs/2510.12573v1) | 2510.12573v1 | 8 |
| 2025-10-14 | [Chimera: State Space Models Beyond Sequences](https://arxiv.org/abs/2510.12111v1) | 2510.12111v1 | 7 |
| 2025-10-14 | [Mamba Can Learn Low-Dimensional Targets In-Context via Test-Time Feature Learning](https://arxiv.org/abs/2510.12026v3) | 2510.12026v3 | 7 |
| 2025-10-13 | [Robust Photoplethysmography Signal Denoising via Mamba Networks](https://arxiv.org/abs/2510.11058v2) | 2510.11058v2 | 6 |
| 2025-10-13 | [High-Resolution Spatiotemporal Modeling with Global-Local State Space Models for Video-Based Human Pose Estimation](https://arxiv.org/abs/2510.11017v1) | 2510.11017v1 | 10 |
| 2025-10-12 | [MSF-Mamba: Motion-aware State Fusion Mamba for Efficient Micro-Gesture Recognition](https://arxiv.org/abs/2510.10478v2) | 2510.10478v2 | 11 |
| 2025-10-11 | [SaFiRe: Saccade-Fixation Reiteration with Mamba for Referring Image Segmentation](https://arxiv.org/abs/2510.10160v2) | 2510.10160v2 | 6 |
| 2025-10-10 | [Dynamic Weight-based Temporal Aggregation for Low-light Video Enhancement Under Extreme Noise](https://arxiv.org/abs/2510.09450v2) | 2510.09450v2 | 6 |
| 2025-10-10 | [Design Principles for Sequence Models via Coefficient Dynamics](https://arxiv.org/abs/2510.09389v2) | 2510.09389v2 | 6 |
| 2025-10-10 | [Eigenvalues as a Metric for Memory Dynamics in Sequence Models](https://arxiv.org/abs/2510.09379v2) | 2510.09379v2 | 6 |
| 2025-10-10 | [Minkowski-MambaNet: A Point Cloud Framework with Selective State Space Models for Forest Biomass Quantification](https://arxiv.org/abs/2510.09367v1) | 2510.09367v1 | 15 |
| 2025-10-10 | [MambaH-Fit: Rethinking Hyper-surface Fitting-based Point Cloud Normal Estimation via State Space Modelling](https://arxiv.org/abs/2510.09088v2) | 2510.09088v2 | 12 |
| 2025-10-08 | [Knowledge-Aware Mamba for Joint Change Detection and Classification from MODIS Times Series](https://arxiv.org/abs/2510.09679v1) | 2510.09679v1 | 6 |
| 2025-10-08 | [DeRainMamba: A Frequency-Aware State Space Model with Detail Enhancement for Image Deraining](https://arxiv.org/abs/2510.06746v1) | 2510.06746v1 | 14 |
| 2025-10-08 | [Contextual Representation Flow Across Depth in State-Space and Transformer Architectures](https://arxiv.org/abs/2510.06640v3) | 2510.06640v3 | 7 |
| 2025-10-06 | [The End of Transformers? On Challenging Attention and the Rise of Sub-Quadratic Architectures](https://arxiv.org/abs/2510.05364v1) | 2510.05364v1 | 11 |
| 2025-10-06 | [MCMC for State Space models](https://arxiv.org/abs/2510.04932v1) | 2510.04932v1 | 6 |
| 2025-10-06 | [Hybrid Architectures for Language Models: Systematic Analysis and Design Insights](https://arxiv.org/abs/2510.04800v3) | 2510.04800v3 | 14 |
| 2025-10-06 | [Speak, Edit, Repeat: High-Fidelity Voice Editing and Zero-Shot TTS with Cross-Attentive Mamba](https://arxiv.org/abs/2510.04738v1) | 2510.04738v1 | 8 |
| 2025-10-06 | [SpikingMamba: Towards Energy-Efficient Large Language Models via Knowledge Distillation from Mamba](https://arxiv.org/abs/2510.04595v2) | 2510.04595v2 | 6 |
| 2025-10-04 | [MambaCAFU: Hybrid Multi-Scale and Multi-Attention Model with Mamba-Based Fusion for Medical Image Segmentation](https://arxiv.org/abs/2510.03786v2) | 2510.03786v2 | 6 |
| 2025-10-03 | [The Curious Case of In-Training Compression of State Space Models](https://arxiv.org/abs/2510.02823v4) | 2510.02823v4 | 10 |
| 2025-10-02 | [Poolformer: Recurrent Networks with Pooling for Long-Sequence Modeling](https://arxiv.org/abs/2510.02206v1) | 2510.02206v1 | 10 |
| 2025-10-02 | [Exploring Resolution-Wise Shared Attention in Hybrid Mamba-U-Nets for Improved Cross-Corpus Speech Enhancement](https://arxiv.org/abs/2510.01958v2) | 2510.01958v2 | 6 |
| 2025-10-01 | [Linear RNNs for autoregressive generation of long music samples](https://arxiv.org/abs/2510.02401v1) | 2510.02401v1 | 6 |
| 2025-10-01 | [Gather-Scatter Mamba: Accelerating Propagation with Efficient State Space Model](https://arxiv.org/abs/2510.00862v1) | 2510.00862v1 | 19 |
| 2025-10-01 | [Memory Determines Learning Direction: A Theory of Gradient-Based Optimization in State Space Models](https://arxiv.org/abs/2510.00563v1) | 2510.00563v1 | 8 |
| 2025-10-01 | [How Can Mamba Learn In Context with Outliers and Generalize Provably?](https://arxiv.org/abs/2510.00399v2) | 2510.00399v2 | 8 |
| 2025-09-29 | [An Enhanced Pyramid Feature Network Based on Long-Range Dependencies for Multi-Organ Medical Image Segmentation](https://arxiv.org/abs/2509.24358v1) | 2509.24358v1 | 6 |
| 2025-09-29 | [Wavelet-Assisted Mamba for Satellite-Derived Sea Surface Temperature Super-Resolution](https://arxiv.org/abs/2509.24334v1) | 2509.24334v1 | 10 |
| 2025-09-28 | [HyMaTE: A Hybrid Mamba and Transformer Model for EHR Representation Learning](https://arxiv.org/abs/2509.24118v2) | 2509.24118v2 | 13 |
| 2025-09-28 | [Hazy Pedestrian Trajectory Prediction via Physical Priors and Graph-Mamba](https://arxiv.org/abs/2509.24020v1) | 2509.24020v1 | 10 |
| 2025-09-28 | [MemMamba: Rethinking Memory Patterns in State Space Model](https://arxiv.org/abs/2510.03279v1) | 2510.03279v1 | 16 |
| 2025-09-28 | [Trained Mamba Emulates Online Gradient Descent in In-Context Linear Regression](https://arxiv.org/abs/2509.23779v1) | 2509.23779v1 | 8 |
| 2025-09-28 | [EfficientMIL: Efficient Linear-Complexity MIL Method for WSI Classification](https://arxiv.org/abs/2509.23640v2) | 2509.23640v2 | 8 |
| 2025-09-28 | [VAMamba: An Efficient Visual Adaptive Mamba for Image Restoration](https://arxiv.org/abs/2509.23601v1) | 2509.23601v1 | 6 |
| 2025-09-26 | [TRUST: Test-Time Refinement using Uncertainty-Guided SSM Traverses](https://arxiv.org/abs/2509.22813v2) | 2509.22813v2 | 8 |
| 2025-09-26 | [In-Context Learning can Perform Continual Learning Like Humans](https://arxiv.org/abs/2509.22764v1) | 2509.22764v1 | 8 |
| 2025-09-25 | [SlideMamba: Entropy-Based Adaptive Fusion of GNN and Mamba for Enhanced Representation Learning in Digital Pathology](https://arxiv.org/abs/2509.21239v1) | 2509.21239v1 | 6 |
| 2025-09-25 | [Hybrid Real- and Complex-Valued Neural Network Architecture for Speech Enhancement](https://arxiv.org/abs/2509.21185v2) | 2509.21185v2 | 6 |
| 2025-09-25 | [SwinMamba: A hybrid local-global mamba framework for enhancing semantic segmentation of remotely sensed images](https://arxiv.org/abs/2509.20918v1) | 2509.20918v1 | 6 |
| 2025-09-25 | [Aligning Inductive Bias for Data-Efficient Generalization in State Space Models](https://arxiv.org/abs/2509.20789v5) | 2509.20789v5 | 8 |
| 2025-09-24 | [SpecMamba: Accelerating Mamba Inference on FPGA with Speculative Decoding](https://arxiv.org/abs/2509.19873v1) | 2509.19873v1 | 12 |
| 2025-09-23 | [Mamba Modulation: On the Length Generalization of Mamba](https://arxiv.org/abs/2509.19633v3) | 2509.19633v3 | 7 |
| 2025-09-23 | [An overview of neural architectures for self-supervised audio representation learning from masked spectrograms](https://arxiv.org/abs/2509.18691v1) | 2509.18691v1 | 12 |
| 2025-09-23 | [LEAF-Mamba: Local Emphatic and Adaptive Fusion State Space Model for RGB-D Salient Object Detection](https://arxiv.org/abs/2509.18683v1) | 2509.18683v1 | 12 |
| 2025-09-23 | [LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA](https://arxiv.org/abs/2509.18576v1) | 2509.18576v1 | 10 |
| 2025-09-22 | [HuMam: Humanoid Motion Control via End-to-End Deep Reinforcement Learning with Mamba](https://arxiv.org/abs/2509.18046v2) | 2509.18046v2 | 6 |
| 2025-09-22 | [M3ET: Efficient Vision-Language Learning for Robotics based on Multimodal Mamba-Enhanced Transformer](https://arxiv.org/abs/2509.18005v1) | 2509.18005v1 | 6 |
| 2025-09-22 | [DA-Mamba: Dialogue-aware selective state-space model for multimodal engagement estimation](https://arxiv.org/abs/2509.17711v1) | 2509.17711v1 | 6 |
| 2025-09-22 | [SISMA: Semantic Face Image Synthesis with Mamba](https://arxiv.org/abs/2509.17651v1) | 2509.17651v1 | 6 |
| 2025-09-22 | [Achilles' Heel of Mamba: Essential difficulties of the Mamba architecture demonstrated by synthetic data](https://arxiv.org/abs/2509.17514v2) | 2509.17514v2 | 10 |
| 2025-09-21 | [SynergyNet: Fusing Generative Priors and State-Space Models for Facial Beauty Prediction](https://arxiv.org/abs/2509.17172v1) | 2509.17172v1 | 9 |
| 2025-09-21 | [ME-Mamba: Multi-Expert Mamba with Efficient Knowledge Capture and Fusion for Multimodal Survival Analysis](https://arxiv.org/abs/2509.16900v1) | 2509.16900v1 | 6 |
| 2025-09-19 | [Estimating Clinical Lab Test Result Trajectories from PPG using Physiological Foundation Model and Patient-Aware State Space Model -- a UNIPHY+ Approach](https://arxiv.org/abs/2509.16345v1) | 2509.16345v1 | 10 |
| 2025-09-19 | [SAM: A Mamba-2 State-Space Audio-Language Model](https://arxiv.org/abs/2509.15680v3) | 2509.15680v3 | 6 |
| 2025-09-19 | [DC-Mamba: Bi-temporal deformable alignment and scale-sparse enhancement for remote sensing change detection](https://arxiv.org/abs/2509.15563v1) | 2509.15563v1 | 10 |
| 2025-09-18 | [HybridMamba: A Dual-domain Mamba for 3D Medical Image Segmentation](https://arxiv.org/abs/2509.14609v1) | 2509.14609v1 | 6 |
| 2025-09-17 | [CETUS: Causal Event-Driven Temporal Modeling With Unified Variable-Rate Scheduling](https://arxiv.org/abs/2509.13784v1) | 2509.13784v1 | 8 |
| 2025-09-17 | [State Space Models over Directed Graphs](https://arxiv.org/abs/2509.13735v1) | 2509.13735v1 | 6 |
| 2025-09-16 | [CECT-Mamba: a Hierarchical Contrast-enhanced-aware Model for Pancreatic Tumor Subtyping from Multi-phase CECT](https://arxiv.org/abs/2509.12777v1) | 2509.12777v1 | 6 |
| 2025-09-15 | [U-Mamba2: Scaling State Space Models for Dental Anatomy Segmentation in CBCT](https://arxiv.org/abs/2509.12069v3) | 2509.12069v3 | 12 |
| 2025-09-15 | [FluentAvatar: Flicker-Free Talking-Head Animation via Phoneme-Guided Autoregressive Modeling](https://arxiv.org/abs/2509.12052v3) | 2509.12052v3 | 6 |
| 2025-09-15 | [Joint-octamamba:an octa joint segmentation network based on feature enhanced mamba](https://arxiv.org/abs/2509.11649v1) | 2509.11649v1 | 6 |
| 2025-09-14 | [MixANT: Observation-dependent Memory Propagation for Stochastic Dense Action Anticipation](https://arxiv.org/abs/2509.11394v1) | 2509.11394v1 | 8 |
| 2025-09-14 | [Mamba Outpaces Reformer in Stock Prediction with Sentiments from Top Ten LLMs](https://arxiv.org/abs/2510.01203v1) | 2510.01203v1 | 6 |
| 2025-09-12 | [FLARE-SSM: Deep State Space Models with Influence-Balanced Loss for 72-Hour Solar Flare Prediction](https://arxiv.org/abs/2509.09988v1) | 2509.09988v1 | 6 |
| 2025-09-10 | [First-order State Space Model for Lightweight Image Super-resolution](https://arxiv.org/abs/2509.08458v2) | 2509.08458v2 | 10 |
| 2025-09-10 | [Hyperspectral Mamba for Hyperspectral Object Tracking](https://arxiv.org/abs/2509.08265v1) | 2509.08265v1 | 6 |
| 2025-09-09 | [DEPFusion: Dual-Domain Enhancement and Priority-Guided Mamba Fusion for UAV Multispectral Object Detection](https://arxiv.org/abs/2509.07327v2) | 2509.07327v2 | 6 |
| 2025-09-08 | [Video-Based MPAA Rating Prediction: An Attention-Driven Hybrid Architecture Using Contrastive Learning](https://arxiv.org/abs/2509.06826v1) | 2509.06826v1 | 6 |
| 2025-09-05 | [MambaLite-Micro: Memory-Optimized Mamba Inference on MCUs](https://arxiv.org/abs/2509.05488v1) | 2509.05488v1 | 6 |
| 2025-09-05 | [Detecting Blinks in Healthy and Parkinson's EEG: A Deep Learning Perspective](https://arxiv.org/abs/2509.04951v1) | 2509.04951v1 | 6 |
| 2025-09-05 | [Exploring Non-Local Spatial-Angular Correlations with a Hybrid Mamba-Transformer Framework for Light Field Super-Resolution](https://arxiv.org/abs/2509.04824v1) | 2509.04824v1 | 6 |
| 2025-09-05 | [CD-Mamba: Cloud detection with long-range spatial dependency modeling](https://arxiv.org/abs/2509.04729v1) | 2509.04729v1 | 6 |
| 2025-09-04 | [VCMamba: Bridging Convolutions with Multi-Directional Mamba for Efficient Visual Representation](https://arxiv.org/abs/2509.04669v1) | 2509.04669v1 | 10 |
| 2025-09-04 | [LISM: Long-range Integrative State space Models via Input-Latent State Interactions](https://arxiv.org/abs/2509.04226v2) | 2509.04226v2 | 11 |
| 2025-09-03 | [S2M2ECG: Spatio-temporal bi-directional State Space Model Enabled Multi-branch Mamba for ECG](https://arxiv.org/abs/2509.03066v1) | 2509.03066v1 | 12 |
| 2025-09-02 | [Mentality: A Mamba-based Approach towards Foundation Models for EEG](https://arxiv.org/abs/2509.02746v1) | 2509.02746v1 | 14 |
| 2025-09-02 | [ESTM: An Enhanced Dual-Branch Spectral-Temporal Mamba for Anomalous Sound Detection](https://arxiv.org/abs/2509.02471v1) | 2509.02471v1 | 8 |
| 2025-09-02 | [AudioRWKV: Efficient and Stable Bidirectional RWKV for Audio Pattern Recognition](https://arxiv.org/abs/2509.02167v2) | 2509.02167v2 | 12 |
| 2025-09-01 | [Mamba-CNN: A Hybrid Architecture for Efficient and Accurate Facial Beauty Prediction](https://arxiv.org/abs/2509.01431v1) | 2509.01431v1 | 16 |
| 2025-09-01 | [StoxLSTM: A Stochastic Extended Long Short-Term Memory Network for Time Series Forecasting](https://arxiv.org/abs/2509.01187v2) | 2509.01187v2 | 6 |
| 2025-09-01 | [SpectMamba: Integrating Frequency and State Space Models for Enhanced Medical Image Detection](https://arxiv.org/abs/2509.01080v1) | 2509.01080v1 | 12 |
| 2025-08-31 | [SCOUT: Toward Sub-Quadratic Attention via Segment Compression for Optimized Utility in Transformers](https://arxiv.org/abs/2509.00935v1) | 2509.00935v1 | 13 |
| 2025-08-31 | [CSFMamba: Cross State Fusion Mamba Operator for Multimodal Remote Sensing Image Classification](https://arxiv.org/abs/2509.00677v1) | 2509.00677v1 | 10 |
| 2025-08-31 | [MV-SSM: Multi-View State Space Modeling for 3D Human Pose Estimation](https://arxiv.org/abs/2509.00649v1) | 2509.00649v1 | 10 |
| 2025-08-31 | [HADIS: A Hybrid Architecture for Query-Aware Diffusion Model Serving](https://arxiv.org/abs/2509.00642v3) | 2509.00642v3 | 6 |
| 2025-08-30 | [Gated Associative Memory: A Parallel O(N) Architecture for Efficient Sequence Modeling](https://arxiv.org/abs/2509.00605v1) | 2509.00605v1 | 8 |
| 2025-08-30 | [SemaMIL: Semantic-Aware Multiple Instance Learning with Retrieval-Guided State Space Modeling for Whole Slide Images](https://arxiv.org/abs/2509.00442v2) | 2509.00442v2 | 6 |
| 2025-08-29 | [Quantum-Optimized Selective State Space Model for Efficient Time Series Prediction](https://arxiv.org/abs/2509.00259v1) | 2509.00259v1 | 14 |
| 2025-08-29 | [Scaling Legal AI: Benchmarking Mamba and Transformers for Statutory Classification and Case Law Retrieval](https://arxiv.org/abs/2509.00141v2) | 2509.00141v2 | 9 |
| 2025-08-28 | [Mitosis detection in domain shift scenarios: a Mamba-based approach](https://arxiv.org/abs/2508.21033v2) | 2508.21033v2 | 6 |
| 2025-08-28 | [PointDGRWKV: Generalizing RWKV-like Architecture to Unseen Domains for Point Cloud Classification](https://arxiv.org/abs/2508.20835v2) | 2508.20835v2 | 10 |
| 2025-08-28 | [Uncovering the Spectral Bias in Diagonal State Space Models](https://arxiv.org/abs/2508.20441v1) | 2508.20441v1 | 6 |
| 2025-08-28 | [Enhancing Mamba Decoder with Bidirectional Interaction in Multi-Task Dense Prediction](https://arxiv.org/abs/2508.20376v1) | 2508.20376v1 | 6 |
| 2025-08-27 | [Beyond BEV: Optimizing Point-Level Tokens for Collaborative Perception](https://arxiv.org/abs/2508.19638v1) | 2508.19638v1 | 6 |
| 2025-08-26 | [Atrial Fibrillation Prediction Using a Lightweight Temporal Convolutional and Selective State Space Architecture](https://arxiv.org/abs/2508.19361v1) | 2508.19361v1 | 15 |
| 2025-08-26 | [Revisiting associative recall in modern recurrent models](https://arxiv.org/abs/2508.19029v2) | 2508.19029v2 | 7 |
| 2025-08-25 | [The Computational Complexity of Satisfiability in State Space Models](https://arxiv.org/abs/2508.18162v1) | 2508.18162v1 | 6 |
| 2025-08-25 | [Characterizing the Behavior of Training Mamba-based State Space Models on GPUs](https://arxiv.org/abs/2508.17679v1) | 2508.17679v1 | 12 |
| 2025-08-24 | [Bridging Graph and State-Space Modeling for Intensive Care Unit Length of Stay Prediction](https://arxiv.org/abs/2508.17554v2) | 2508.17554v2 | 6 |
| 2025-08-22 | [Predictability Enables Parallelization of Nonlinear State Space Models](https://arxiv.org/abs/2508.16817v4) | 2508.16817v4 | 6 |
| 2025-08-22 | [Learning Long-Range Action Representation by Two-Stream Mamba Pyramid Network for Figure Skating Assessment](https://arxiv.org/abs/2508.16291v1) | 2508.16291v1 | 6 |
| 2025-08-21 | [ASCMamba: Multimodal Time-Frequency Mamba for Acoustic Scene Classification](https://arxiv.org/abs/2508.15632v2) | 2508.15632v2 | 10 |
| 2025-08-20 | [UST-SSM: Unified Spatio-Temporal State Space Models for Point Cloud Video Modeling](https://arxiv.org/abs/2508.14604v1) | 2508.14604v1 | 10 |
| 2025-08-20 | [Mamba2 Meets Silence: Robust Vocal Source Separation for Sparse Regions](https://arxiv.org/abs/2508.14556v2) | 2508.14556v2 | 10 |
| 2025-08-20 | [NVIDIA Nemotron Nano 2: An Accurate and Efficient Hybrid Mamba-Transformer Reasoning Model](https://arxiv.org/abs/2508.14444v4) | 2508.14444v4 | 6 |
| 2025-08-19 | [Diversity-enhanced Collaborative Mamba for Semi-supervised Medical Image Segmentation](https://arxiv.org/abs/2508.13712v1) | 2508.13712v1 | 10 |
| 2025-08-19 | [Leveraging Mamba with Full-Face Vision for Audio-Visual Speech Enhancement](https://arxiv.org/abs/2508.13624v2) | 2508.13624v2 | 6 |
| 2025-08-19 | [Towards Efficient Vision State Space Models via Token Merging](https://arxiv.org/abs/2508.13599v1) | 2508.13599v1 | 6 |
| 2025-08-18 | [Point upsampling networks for single-photon sensing](https://arxiv.org/abs/2508.12986v1) | 2508.12986v1 | 8 |
| 2025-08-18 | [D2-Mamba: Dual-Scale Fusion and Dual-Path Scanning with SSMs for Shadow Removal](https://arxiv.org/abs/2508.12750v3) | 2508.12750v3 | 6 |
| 2025-08-17 | [SRMA-Mamba: Spatial Reverse Mamba Attention Network for Pathological Liver Segmentation in MRI Volumes](https://arxiv.org/abs/2508.12410v3) | 2508.12410v3 | 6 |
| 2025-08-17 | [MBMamba: When Memory Buffer Meets Mamba for Structure-Aware Image Deblurring](https://arxiv.org/abs/2508.12346v2) | 2508.12346v2 | 6 |
| 2025-08-17 | [STM3: Mixture of Multiscale Mamba for Long-Term Spatio-Temporal Time-Series Prediction](https://arxiv.org/abs/2508.12247v3) | 2508.12247v3 | 6 |
| 2025-08-16 | [HPD: Hybrid Projection Decomposition for Robust State Space Models on Analog CIM Hardware](https://arxiv.org/abs/2508.11935v1) | 2508.11935v1 | 10 |
| 2025-08-16 | [ENA: Efficient N-dimensional Attention](https://arxiv.org/abs/2508.11921v1) | 2508.11921v1 | 6 |
| 2025-08-16 | [LocoMamba: Vision-Driven Locomotion via End-to-End Deep Reinforcement Learning with Mamba](https://arxiv.org/abs/2508.11849v3) | 2508.11849v3 | 9 |
| 2025-08-15 | [Guiding WaveMamba with Frequency Maps for Image Debanding](https://arxiv.org/abs/2508.11331v2) | 2508.11331v2 | 10 |
| 2025-08-14 | [Beyond Global Scanning: Adaptive Visual State Space Modeling for Salient Object Detection in Optical Remote Sensing Images](https://arxiv.org/abs/2508.10542v5) | 2508.10542v5 | 6 |
| 2025-08-14 | [EgoMusic-driven Human Dance Motion Estimation with Skeleton Mamba](https://arxiv.org/abs/2508.10522v1) | 2508.10522v1 | 6 |
| 2025-08-14 | [Trajectory-aware Shifted State Space Models for Online Video Super-Resolution](https://arxiv.org/abs/2508.10453v2) | 2508.10453v2 | 10 |
| 2025-08-14 | [eMamba: Efficient Acceleration Framework for Mamba Models in Edge Computing](https://arxiv.org/abs/2508.10370v1) | 2508.10370v1 | 10 |
| 2025-08-13 | [CKFNet: Neural Network Aided Cubature Kalman filtering](https://arxiv.org/abs/2508.09727v1) | 2508.09727v1 | 6 |
| 2025-08-12 | [UltraLight Med-Vision Mamba for Classification of Neoplastic Progression in Tubular Adenomas](https://arxiv.org/abs/2508.09339v1) | 2508.09339v1 | 6 |
| 2025-08-12 | [Fake-Mamba: Real-Time Speech Deepfake Detection Using Bidirectional Mamba as Self-Attention's Alternative](https://arxiv.org/abs/2508.09294v1) | 2508.09294v1 | 6 |
| 2025-08-12 | [Text-conditioned State Space Model For Domain-generalized Change Detection Visual Question Answering](https://arxiv.org/abs/2508.08974v3) | 2508.08974v3 | 6 |
| 2025-08-11 | [Fast weight programming and linear transformers: from machine learning to neurobiology](https://arxiv.org/abs/2508.08435v6) | 2508.08435v6 | 6 |
| 2025-08-11 | [Mamba-FCS: Joint Spatio- Frequency Feature Fusion, Change-Guided Attention, and SeK Loss for Enhanced Semantic Change Detection in Remote Sensing](https://arxiv.org/abs/2508.08232v2) | 2508.08232v2 | 10 |
| 2025-08-11 | [ME-TST+: Micro-expression Analysis via Temporal State Transition with ROI Relationship Awareness](https://arxiv.org/abs/2508.08082v1) | 2508.08082v1 | 8 |
| 2025-08-10 | [Keyword Mamba: Spoken Keyword Spotting with State Space Models](https://arxiv.org/abs/2508.07363v1) | 2508.07363v1 | 12 |
| 2025-08-10 | [ASM-UNet: Adaptive Scan Mamba Integrating Group Commonalities and Individual Variations for Fine-Grained Segmentation](https://arxiv.org/abs/2508.07237v1) | 2508.07237v1 | 6 |
| 2025-08-08 | [Generative AI for Intent-Driven Network Management in 6G RAN: A Case Study on the Mamba Model](https://arxiv.org/abs/2508.06616v2) | 2508.06616v2 | 6 |
| 2025-08-08 | [Text Embedded Swin-UMamba for DeepLesion Segmentation](https://arxiv.org/abs/2508.06453v2) | 2508.06453v2 | 6 |
| 2025-08-08 | [GMF-Drive: Gated Mamba Fusion with Spatial-Aware BEV Representation for End-to-End Autonomous Driving](https://arxiv.org/abs/2508.06113v2) | 2508.06113v2 | 6 |
| 2025-08-08 | [ME$^3$-BEV: Mamba-Enhanced Deep Reinforcement Learning for End-to-End Autonomous Driving with BEV-Perception](https://arxiv.org/abs/2508.06074v1) | 2508.06074v1 | 6 |
| 2025-08-08 | [Hypergraph Neural Network with State Space Models for Node Classification](https://arxiv.org/abs/2508.06587v2) | 2508.06587v2 | 10 |
| 2025-08-07 | [MM2CT: MR-to-CT translation for multi-modal image fusion with mamba](https://arxiv.org/abs/2508.05476v1) | 2508.05476v1 | 6 |
| 2025-08-07 | [HiSTM: Hierarchical Spatiotemporal Mamba for Cellular Traffic Forecasting](https://arxiv.org/abs/2508.09184v1) | 2508.09184v1 | 8 |
| 2025-08-07 | [HiFi-Mamba: Dual-Stream W-Laplacian Enhanced Mamba for High-Fidelity MRI Reconstruction](https://arxiv.org/abs/2508.09179v3) | 2508.09179v3 | 7 |
| 2025-08-07 | [MedMambaLite: Hardware-Aware Mamba for Medical Image Classification](https://arxiv.org/abs/2508.05049v1) | 2508.05049v1 | 6 |
| 2025-08-06 | [MambaITD: An Efficient Cross-Modal Mamba Network for Insider Threat Detection](https://arxiv.org/abs/2508.05695v1) | 2508.05695v1 | 10 |
| 2025-08-05 | [Beyond Illumination: Fine-Grained Detail Preservation in Extreme Dark Image Restoration](https://arxiv.org/abs/2508.03336v1) | 2508.03336v1 | 8 |
| 2025-08-05 | [Rethinking Selectivity in State Space Models: A Minimal Predictive Sufficiency Approach](https://arxiv.org/abs/2508.03158v1) | 2508.03158v1 | 12 |
| 2025-08-05 | [SSFMamba: Learning Symmetry-driven Spatial-Frequency Modeling for Physically Consistent 3D Medical Image Segmentation](https://arxiv.org/abs/2508.03069v3) | 2508.03069v3 | 10 |
| 2025-08-05 | [ClinicalFMamba: Advancing Clinical Assessment using Mamba-based Multimodal Neuroimaging Fusion](https://arxiv.org/abs/2508.03008v1) | 2508.03008v1 | 14 |
| 2025-08-05 | [Mamba-X: An End-to-End Vision Mamba Accelerator for Edge Computing Devices](https://arxiv.org/abs/2508.02977v1) | 2508.02977v1 | 10 |
| 2025-08-04 | [AMD-Mamba: A Phenotype-Aware Multi-Modal Framework for Robust AMD Prognosis](https://arxiv.org/abs/2508.02957v1) | 2508.02957v1 | 6 |
| 2025-08-04 | [Content-Aware Mamba for Learned Image Compression](https://arxiv.org/abs/2508.02192v6) | 2508.02192v6 | 6 |
| 2025-08-04 | [DeflareMamba: Hierarchical Vision Mamba for Contextually Consistent Lens Flare Removal](https://arxiv.org/abs/2508.02113v1) | 2508.02113v1 | 12 |
| 2025-08-03 | [Self-Navigated Residual Mamba for Universal Industrial Anomaly Detection](https://arxiv.org/abs/2508.01591v2) | 2508.01591v2 | 6 |
| 2025-08-02 | [RoadMamba: A Dual Branch Visual State Space Model for Road Surface Classification](https://arxiv.org/abs/2508.01210v1) | 2508.01210v1 | 12 |
| 2025-08-01 | [Online Fine-Tuning of Carbon Emission Predictions using Real-Time Recurrent Learning for State Space Models](https://arxiv.org/abs/2508.00804v1) | 2508.00804v1 | 9 |
| 2025-08-01 | [Output-recurrent gated state space model for multiphase flows modeling and uncertainty quantification of exhaust vehicles](https://arxiv.org/abs/2508.00588v1) | 2508.00588v1 | 9 |
| 2025-08-01 | [PIF-Net: Ill-Posed Prior Guided Multispectral and Hyperspectral Image Fusion via Invertible Mamba and Fusion-Aware LoRA](https://arxiv.org/abs/2508.00453v2) | 2508.00453v2 | 6 |
| 2025-08-01 | [UIS-Mamba: Exploring Mamba for Underwater Instance Segmentation via Dynamic Tree Scan and Hidden State Weaken](https://arxiv.org/abs/2508.00421v1) | 2508.00421v1 | 10 |
| 2025-08-01 | [Mamba for Wireless Communications and Networking: Principles and Opportunities](https://arxiv.org/abs/2508.00403v1) | 2508.00403v1 | 6 |
| 2025-08-01 | [Guided Depth Map Super-Resolution via Multi-Scale Fusion U-shaped Mamba Network](https://arxiv.org/abs/2508.00248v1) | 2508.00248v1 | 10 |
| 2025-07-31 | [Mamba-based Spatio-Frequency Motion Perception for Video Camouflaged Object Detection](https://arxiv.org/abs/2507.23601v2) | 2507.23601v2 | 13 |
| 2025-07-31 | [MamV2XCalib: V2X-based Target-less Infrastructure Camera Calibration with State Space Model](https://arxiv.org/abs/2507.23595v1) | 2507.23595v1 | 10 |
| 2025-07-31 | [Hybrid CNN-Mamba Enhancement Network for Robust Multimodal Sentiment Analysis](https://arxiv.org/abs/2507.23444v1) | 2507.23444v1 | 6 |
| 2025-07-30 | [LIDAR: Lightweight Adaptive Cue-Aware Fusion Vision Mamba for Multimodal Segmentation of Structural Cracks](https://arxiv.org/abs/2507.22477v2) | 2507.22477v2 | 6 |
| 2025-07-30 | [Falcon-H1: A Family of Hybrid-Head Language Models Redefining Efficiency and Performance](https://arxiv.org/abs/2507.22448v1) | 2507.22448v1 | 12 |
| 2025-07-29 | [Spatial-Temporal-Spectral Mamba with Sparse Deformable Token Sequence for Enhanced MODIS Time Series Classification](https://arxiv.org/abs/2508.02839v1) | 2508.02839v1 | 6 |
| 2025-07-28 | [RadioMamba: Breaking the Accuracy-Efficiency Trade-off in Radio Map Construction via a Hybrid Mamba-UNet](https://arxiv.org/abs/2508.09140v1) | 2508.09140v1 | 6 |
| 2025-07-27 | [Diffusion-based Symbolic Music Generation with Structured State Space Models](https://arxiv.org/abs/2507.20128v2) | 2507.20128v2 | 12 |
| 2025-07-26 | [FaRMamba: Frequency-based learning and Reconstruction aided Mamba for Medical Segmentation](https://arxiv.org/abs/2507.20056v1) | 2507.20056v1 | 6 |
| 2025-07-26 | [MambaVesselNet++: A Hybrid CNN-Mamba Architecture for Medical Image Segmentation](https://arxiv.org/abs/2507.19931v1) | 2507.19931v1 | 12 |
| 2025-07-26 | [A Structure-aware and Motion-adaptive Framework for 3D Human Pose Estimation with Mamba](https://arxiv.org/abs/2507.19852v1) | 2507.19852v1 | 6 |
| 2025-07-26 | [HydraMamba: Multi-Head State Space Model for Global Point Cloud Learning](https://arxiv.org/abs/2507.19778v1) | 2507.19778v1 | 14 |
| 2025-07-25 | [SP-Mamba: Spatial-Perception State Space Model for Unsupervised Medical Anomaly Detection](https://arxiv.org/abs/2507.19076v1) | 2507.19076v1 | 14 |
| 2025-07-25 | [GPSMamba: A Global Phase and Spectral Prompt-guided Mamba for Infrared Image Super-Resolution](https://arxiv.org/abs/2507.18998v3) | 2507.18998v3 | 6 |
| 2025-07-24 | [Bridging Cloud Convenience and Protocol Transparency: A Hybrid Architecture for Ethereum Node Operations on Amazon Managed Blockchain](https://arxiv.org/abs/2507.18774v1) | 2507.18774v1 | 6 |
| 2025-07-24 | [HybridTM: Combining Transformer and Mamba for 3D Semantic Segmentation](https://arxiv.org/abs/2507.18575v1) | 2507.18575v1 | 10 |
| 2025-07-24 | [Differential-UMamba: Rethinking Tumor Segmentation Under Limited Data Scenarios](https://arxiv.org/abs/2507.18177v2) | 2507.18177v2 | 6 |
| 2025-07-24 | [WaveMamba: Wavelet-Driven Mamba Fusion for RGB-Infrared Object Detection](https://arxiv.org/abs/2507.18173v1) | 2507.18173v1 | 6 |
| 2025-07-24 | [A Multimodal Sequence-to-Sequence Model for Cross-Subject Prediction of Brain Responses to Naturalistic Stimuli](https://arxiv.org/abs/2507.18104v3) | 2507.18104v3 | 6 |
| 2025-07-24 | [Neural Architecture Discovery via Autonomous Evolution](https://arxiv.org/abs/2507.18074v2) | 2507.18074v2 | 6 |
| 2025-07-23 | [MCM: Mamba-based Cardiac Motion Tracking using Sequential Images in MRI](https://arxiv.org/abs/2507.17678v1) | 2507.17678v1 | 6 |
| 2025-07-23 | [Mammo-Mamba: A Hybrid State-Space and Transformer Architecture with Sequential Mixture of Experts for Multi-View Mammography](https://arxiv.org/abs/2507.17662v1) | 2507.17662v1 | 6 |
| 2025-07-23 | [DeMo++: Motion Decoupling for Autonomous Driving](https://arxiv.org/abs/2507.17342v2) | 2507.17342v2 | 6 |
| 2025-07-22 | [A2Mamba: Attention-augmented State Space Models for Visual Recognition](https://arxiv.org/abs/2507.16624v1) | 2507.16624v1 | 12 |
| 2025-07-22 | [Mamba-OTR: a Mamba-based Solution for Online Take and Release Detection from Untrimmed Egocentric Video](https://arxiv.org/abs/2507.16342v1) | 2507.16342v1 | 6 |
| 2025-07-22 | [AtrousMamaba: An Atrous-Window Scanning Visual State Space Model for Remote Sensing Change Detection](https://arxiv.org/abs/2507.16172v1) | 2507.16172v1 | 10 |
| 2025-07-21 | [MSGM: A Multi-Scale Spatiotemporal Graph Mamba for EEG Emotion Recognition](https://arxiv.org/abs/2507.15914v1) | 2507.15914v1 | 6 |
| 2025-07-21 | [Few-Shot Object Detection via Spatial-Channel State Space Model](https://arxiv.org/abs/2507.15308v1) | 2507.15308v1 | 10 |
| 2025-07-21 | [MeshMamba: State Space Models for Articulated 3D Mesh Generation and Reconstruction](https://arxiv.org/abs/2507.15212v1) | 2507.15212v1 | 12 |
| 2025-07-18 | [Training-free Token Reduction for Vision Mamba](https://arxiv.org/abs/2507.14042v1) | 2507.14042v1 | 6 |
| 2025-07-18 | [GRAM-MAMBA: Holistic Feature Alignment for Wireless Perception with Adaptive Low-Rank Compensation](https://arxiv.org/abs/2507.13803v1) | 2507.13803v1 | 6 |
| 2025-07-18 | [State Space Models Naturally Produce Time Cell and Oscillatory Behaviors and Scale to Abstract Cognitive Functions](https://arxiv.org/abs/2507.13638v4) | 2507.13638v4 | 6 |
| 2025-07-17 | [FLDmamba: Integrating Fourier and Laplace Transform Decomposition with Mamba for Enhanced Time Series Prediction](https://arxiv.org/abs/2507.12803v1) | 2507.12803v1 | 6 |
| 2025-07-17 | [Unified Medical Image Segmentation with State Space Modeling Snake](https://arxiv.org/abs/2507.12760v2) | 2507.12760v2 | 10 |
| 2025-07-16 | [Characterizing State Space Model and Hybrid Language Model Performance with Long Context](https://arxiv.org/abs/2507.12442v4) | 2507.12442v4 | 6 |
| 2025-07-16 | [MambaRate: Speech Quality Assessment Across Different Sampling Rates](https://arxiv.org/abs/2507.12090v1) | 2507.12090v1 | 12 |
| 2025-07-16 | [Foresight in Motion: Reinforcing Trajectory Prediction with Reward Heuristics](https://arxiv.org/abs/2507.12083v1) | 2507.12083v1 | 6 |
| 2025-07-15 | [Flatten Wisely: How Patch Order Shapes Mamba-Powered Vision for MRI Segmentation](https://arxiv.org/abs/2507.13384v1) | 2507.13384v1 | 6 |
| 2025-07-15 | [Precision Spatio-Temporal Feature Fusion for Robust Remote Sensing Change Detection](https://arxiv.org/abs/2507.11523v1) | 2507.11523v1 | 8 |
| 2025-07-14 | [A Generalizable Physics-Enhanced State Space Model for Long-Term Dynamics Forecasting in Complex Environments](https://arxiv.org/abs/2507.10792v1) | 2507.10792v1 | 6 |
| 2025-07-14 | [Bridging Robustness and Generalization Against Word Substitution Attacks in NLP via the Growth Bound Matrix Approach](https://arxiv.org/abs/2507.10330v1) | 2507.10330v1 | 6 |
| 2025-07-14 | [Recognizing Dementia from Neuropsychological Tests with State Space Models](https://arxiv.org/abs/2507.10311v1) | 2507.10311v1 | 6 |
| 2025-07-13 | [Enhancing Stereo Sound Event Detection with BiMamba and Pretrained PSELDnet](https://arxiv.org/abs/2507.09570v1) | 2507.09570v1 | 6 |
| 2025-07-13 | [QuarterMap: Efficient Post-Training Token Pruning for Visual State Space Models](https://arxiv.org/abs/2507.09514v1) | 2507.09514v1 | 10 |
| 2025-07-10 | [DARAS: Dynamic Audio-Room Acoustic Synthesis for Blind Room Impulse Response Estimation](https://arxiv.org/abs/2507.08135v2) | 2507.08135v2 | 8 |
| 2025-07-10 | [Space-Filling Regularization for Robust and Interpretable Nonlinear State Space Models](https://arxiv.org/abs/2507.07792v1) | 2507.07792v1 | 6 |
| 2025-07-10 | [Tree-Mamba: A Tree-Aware Mamba for Underwater Monocular Depth Estimation](https://arxiv.org/abs/2507.07687v1) | 2507.07687v1 | 6 |
| 2025-07-09 | [DIFFUMA: High-Fidelity Spatio-Temporal Video Prediction via Dual-Path Mamba and Diffusion Enhancement](https://arxiv.org/abs/2507.06738v1) | 2507.06738v1 | 6 |
| 2025-07-09 | [Spatial-Temporal Graph Mamba for Music-Guided Dance Video Synthesis](https://arxiv.org/abs/2507.06689v1) | 2507.06689v1 | 6 |
| 2025-07-09 | [Exploring State-Space-Model based Language Model in Music Generation](https://arxiv.org/abs/2507.06674v1) | 2507.06674v1 | 10 |
| 2025-07-09 | [Decoder-Hybrid-Decoder Architecture for Efficient Reasoning with Long Generation](https://arxiv.org/abs/2507.06607v3) | 2507.06607v3 | 10 |
| 2025-07-08 | [Mamba Goes HoME: Hierarchical Soft Mixture-of-Experts for 3D Medical Image Segmentation](https://arxiv.org/abs/2507.06363v4) | 2507.06363v4 | 12 |
| 2025-07-08 | [Differential Mamba](https://arxiv.org/abs/2507.06204v2) | 2507.06204v2 | 6 |
| 2025-07-08 | [LangMamba: A Language-driven Mamba Framework for Low-dose CT Denoising with Vision-language Models](https://arxiv.org/abs/2507.06140v1) | 2507.06140v1 | 6 |
| 2025-07-08 | [Non-Intrusive Binaural Speech Intelligibility Prediction Using Mamba for Hearing-Impaired Listeners](https://arxiv.org/abs/2507.05729v1) | 2507.05729v1 | 6 |
| 2025-07-07 | [Bridging Expressivity and Scalability with Adaptive Unitary SSMs](https://arxiv.org/abs/2507.05238v3) | 2507.05238v3 | 10 |
| 2025-07-07 | [Bridging KAN and MLP: MJKAN, a Hybrid Architecture with Both Efficiency and Expressiveness](https://arxiv.org/abs/2507.04690v1) | 2507.04690v1 | 6 |
| 2025-07-06 | [MambaVideo for Discrete Video Tokenization with Channel-Split Quantization](https://arxiv.org/abs/2507.04559v1) | 2507.04559v1 | 6 |
| 2025-07-06 | [RAT: Bridging RNN Efficiency and Attention Accuracy via Chunk-based Sequence Modeling](https://arxiv.org/abs/2507.04416v3) | 2507.04416v3 | 9 |
| 2025-07-06 | [MVNet: Hyperspectral Remote Sensing Image Classification Based on Hybrid Mamba-Transformer Vision Backbone Architecture](https://arxiv.org/abs/2507.04409v1) | 2507.04409v1 | 12 |
| 2025-07-06 | [Multi-Expert Learning Framework with the State Space Model for Optical and SAR Image Registration](https://arxiv.org/abs/2507.04397v2) | 2507.04397v2 | 10 |
| 2025-07-06 | [DC-Mamber: A Dual Channel Prediction Model based on Mamba and Linear Transformer for Multivariate Time Series Forecasting](https://arxiv.org/abs/2507.04381v1) | 2507.04381v1 | 10 |
| 2025-07-06 | [MambaFusion: Height-Fidelity Dense Global Fusion for Multi-modal 3D Object Detection](https://arxiv.org/abs/2507.04369v1) | 2507.04369v1 | 8 |
| 2025-07-05 | [MCST-Mamba: Multivariate Mamba-Based Model for Traffic Prediction](https://arxiv.org/abs/2507.03927v1) | 2507.03927v1 | 6 |
| 2025-07-04 | [Adaptive Gate-Aware Mamba Networks for Magnetic Resonance Fingerprinting](https://arxiv.org/abs/2507.03369v1) | 2507.03369v1 | 6 |
| 2025-07-03 | [Transformer-based EEG Decoding: A Survey](https://arxiv.org/abs/2507.02320v1) | 2507.02320v1 | 6 |
| 2025-07-03 | [FMOcc: TPV-Driven Flow Matching for 3D Occupancy Prediction with Selective State Space Model](https://arxiv.org/abs/2507.02250v1) | 2507.02250v1 | 9 |
| 2025-07-02 | [TrackingMiM: Efficient Mamba-in-Mamba Serialization for Real-time UAV Object Tracking](https://arxiv.org/abs/2507.01535v1) | 2507.01535v1 | 8 |
| 2025-07-02 | [Mamba Guided Boundary Prior Matters: A New Perspective for Generalized Polyp Segmentation](https://arxiv.org/abs/2507.01509v1) | 2507.01509v1 | 6 |
| 2025-07-02 | [MUG: Pseudo Labeling Augmented Audio-Visual Mamba Network for Audio-Visual Video Parsing](https://arxiv.org/abs/2507.01384v2) | 2507.01384v2 | 6 |
| 2025-07-02 | [SWinMamba: Serpentine Window State Space Model for Vascular Segmentation](https://arxiv.org/abs/2507.01323v1) | 2507.01323v1 | 12 |
| 2025-07-01 | [MambAttention: Mamba with Multi-Head Attention for Generalizable Single-Channel Speech Enhancement](https://arxiv.org/abs/2507.00966v4) | 2507.00966v4 | 10 |
| 2025-07-01 | [UAVD-Mamba: Deformable Token Fusion Vision Mamba for Multimodal UAV Detection](https://arxiv.org/abs/2507.00849v1) | 2507.00849v1 | 6 |
| 2025-07-01 | [BadViM: Backdoor Attack against Vision Mamba](https://arxiv.org/abs/2507.00577v1) | 2507.00577v1 | 10 |
| 2025-07-01 | [Laplace-Mamba: Laplace Frequency Prior-Guided Mamba-CNN Fusion Network for Image Dehazing](https://arxiv.org/abs/2507.00501v1) | 2507.00501v1 | 6 |
| 2025-06-30 | [Mamba-FETrack V2: Revisiting State Space Model for Frame-Event based Visual Object Tracking](https://arxiv.org/abs/2506.23783v1) | 2506.23783v1 | 12 |
| 2025-06-29 | [MoMa: Modulating Mamba for Adapting Image Foundation Models to Video Recognition](https://arxiv.org/abs/2506.23283v1) | 2506.23283v1 | 12 |
| 2025-06-28 | [VSRM: A Robust Mamba-Based Framework for Video Super-Resolution](https://arxiv.org/abs/2506.22762v3) | 2506.22762v3 | 8 |
| 2025-06-27 | [BrainMT: A Hybrid Mamba-Transformer Architecture for Modeling Long-Range Dependencies in Functional MRI Data](https://arxiv.org/abs/2506.22591v1) | 2506.22591v1 | 6 |
| 2025-06-27 | [EAMamba: Efficient All-Around Vision State Space Model for Image Restoration](https://arxiv.org/abs/2506.22246v1) | 2506.22246v1 | 12 |
| 2025-06-27 | [RAUM-Net: Regional Attention and Uncertainty-aware Mamba Network](https://arxiv.org/abs/2506.21905v1) | 2506.21905v1 | 6 |
| 2025-06-26 | [TUS-REC2024: A Challenge to Reconstruct 3D Freehand Ultrasound Without External Tracker](https://arxiv.org/abs/2506.21765v2) | 2506.21765v2 | 6 |
| 2025-06-26 | [StruMamba3D: Exploring Structural Mamba for Self-supervised Point Cloud Representation Learning](https://arxiv.org/abs/2506.21541v3) | 2506.21541v3 | 10 |
| 2025-06-26 | [Holistic Surgical Phase Recognition with Hierarchical Input Dependent State Space Models](https://arxiv.org/abs/2506.21330v1) | 2506.21330v1 | 6 |
| 2025-06-26 | [DKGCM: A Spatio-Temporal Prediction Model for Traffic Flow by Fusing Spatial Node Clustering Method and Fourier Bidirectional Mamba Mechanism](https://arxiv.org/abs/2507.01982v1) | 2507.01982v1 | 6 |
| 2025-06-25 | [EAGLE: An Efficient Global Attention Lesion Segmentation Model for Hepatic Echinococcosis](https://arxiv.org/abs/2506.20333v1) | 2506.20333v1 | 8 |
| 2025-06-25 | [Echo State Transformer: Attention Over Finite Memories](https://arxiv.org/abs/2507.02917v3) | 2507.02917v3 | 6 |
| 2025-06-24 | [ReCoGNet: Recurrent Context-Guided Network for 3D MRI Prostate Segmentation](https://arxiv.org/abs/2506.19687v1) | 2506.19687v1 | 7 |
| 2025-06-24 | [MambaOutRS: A Hybrid CNN-Fourier Architecture for Remote Sensing Image Classification](https://arxiv.org/abs/2506.19561v1) | 2506.19561v1 | 12 |
| 2025-06-24 | [JCAPT: A Joint Modeling Approach for CAPT](https://arxiv.org/abs/2506.19315v2) | 2506.19315v2 | 10 |
| 2025-06-23 | [Diffusion Transformer-to-Mamba Distillation for High-Resolution Image Generation](https://arxiv.org/abs/2506.18999v1) | 2506.18999v1 | 10 |
| 2025-06-23 | [MARL-MambaContour: Unleashing Multi-Agent Deep Reinforcement Learning for Active Contour Optimization in Medical Image Segmentation](https://arxiv.org/abs/2506.18679v2) | 2506.18679v2 | 10 |
| 2025-06-23 | [BSMamba: Brightness and Semantic Modeling for Long-Range Interaction in Low-Light Image Enhancement](https://arxiv.org/abs/2506.18346v2) | 2506.18346v2 | 6 |
| 2025-06-23 | [Jet Reconstruction with Mamba Networks in Collider Events](https://arxiv.org/abs/2506.18336v2) | 2506.18336v2 | 6 |
| 2025-06-22 | [Memba: Membrane-driven Parameter-Efficient Fine-Tuning for Mamba](https://arxiv.org/abs/2506.18184v2) | 2506.18184v2 | 10 |
| 2025-06-22 | [Routing Mamba: Scaling State Space Models with Mixture-of-Experts Projection](https://arxiv.org/abs/2506.18145v1) | 2506.18145v1 | 14 |
| 2025-06-22 | [Damba-ST: Domain-Adaptive Mamba for Efficient Urban Spatio-Temporal Prediction](https://arxiv.org/abs/2506.18939v3) | 2506.18939v3 | 10 |
| 2025-06-22 | [OSDMamba: Enhancing Oil Spill Detection from Remote Sensing Images Using Selective State Space Model](https://arxiv.org/abs/2506.18006v1) | 2506.18006v1 | 15 |
| 2025-06-22 | [Cross-modal State Space Modeling for Real-time RGB-thermal Wild Scene Semantic Segmentation](https://arxiv.org/abs/2506.17869v1) | 2506.17869v1 | 6 |
| 2025-06-20 | [A Quantile Regression Approach for Remaining Useful Life Estimation with State Space Models](https://arxiv.org/abs/2506.17018v1) | 2506.17018v1 | 8 |
| 2025-06-19 | [MambaHash: Visual State Space Deep Hashing Model for Large-Scale Image Retrieval](https://arxiv.org/abs/2506.16353v1) | 2506.16353v1 | 6 |
| 2025-06-19 | [EDNet: A Versatile Speech Enhancement Framework with Gating Mamba Mechanism and Phase Shift-Invariant Training](https://arxiv.org/abs/2506.16231v2) | 2506.16231v2 | 6 |
| 2025-06-19 | [FlowRAM: Grounding Flow Matching Policy with Region-Aware Mamba Framework for Robotic Manipulation](https://arxiv.org/abs/2506.16201v1) | 2506.16201v1 | 10 |
| 2025-06-19 | [LBMamba: Locally Bi-directional Mamba](https://arxiv.org/abs/2506.15976v2) | 2506.15976v2 | 10 |
| 2025-06-18 | [Emergence of Primacy and Recency Effect in Mamba: A Mechanistic Point of View](https://arxiv.org/abs/2506.15156v1) | 2506.15156v1 | 8 |
| 2025-06-16 | [Scaling Algorithm Distillation for Continuous Control with Mamba](https://arxiv.org/abs/2506.13892v1) | 2506.13892v1 | 8 |
| 2025-06-16 | [Stereo sound event localization and detection based on PSELDnet pretraining and BiMamba sequence modeling](https://arxiv.org/abs/2506.13455v1) | 2506.13455v1 | 9 |
| 2025-06-16 | [MT-PCR: Hybrid Mamba-Transformer Network with Spatial Serialization for Point Cloud Registration](https://arxiv.org/abs/2506.13183v2) | 2506.13183v2 | 8 |
| 2025-06-15 | [Unleashing Diffusion and State Space Models for Medical Image Segmentation](https://arxiv.org/abs/2506.12747v2) | 2506.12747v2 | 10 |
| 2025-06-14 | [An Exploration of Mamba for Speech Self-Supervised Models](https://arxiv.org/abs/2506.12606v2) | 2506.12606v2 | 11 |
| 2025-06-14 | [Generalizable Trajectory Prediction via Inverse Reinforcement Learning with Mamba-Graph Architecture](https://arxiv.org/abs/2506.12474v2) | 2506.12474v2 | 6 |
| 2025-06-14 | [MS-UMamba: An Improved Vision Mamba Unet for Fetal Abdominal Medical Image Segmentation](https://arxiv.org/abs/2506.12441v1) | 2506.12441v1 | 6 |
| 2025-06-13 | [InceptionMamba: Efficient Multi-Stage Feature Enhancement with Selective State Space Model for Microscopic Medical Image Segmentation](https://arxiv.org/abs/2506.12208v1) | 2506.12208v1 | 15 |
| 2025-06-13 | [Maximally-Informative Retrieval for State Space Model Generation](https://arxiv.org/abs/2506.12149v1) | 2506.12149v1 | 6 |
| 2025-06-13 | [pLSTM: parallelizable Linear Source Transition Mark networks](https://arxiv.org/abs/2506.11997v1) | 2506.11997v1 | 6 |
| 2025-06-13 | [Understanding Input Selectivity in Mamba: Impact on Approximation Power, Memorization, and Associative Recall Capacity](https://arxiv.org/abs/2506.11891v1) | 2506.11891v1 | 6 |
| 2025-06-13 | [MambaVSR: Content-Aware Scanning State Space Model for Video Super-Resolution](https://arxiv.org/abs/2506.11768v1) | 2506.11768v1 | 12 |
| 2025-06-12 | [Sequential-Parallel Duality in Prefix Scannable Models](https://arxiv.org/abs/2506.10918v2) | 2506.10918v2 | 11 |
| 2025-06-12 | [M4V: Multimodal Mamba for Efficient Text-to-Video Generation](https://arxiv.org/abs/2506.10915v2) | 2506.10915v2 | 9 |
| 2025-06-12 | [Med-URWKV†: Toward Enhanced Pretrained Pure VRWKV Models for Medical Image Segmentation](https://arxiv.org/abs/2506.10858v2) | 2506.10858v2 | 14 |
| 2025-06-12 | [Brain2Vec: A Deep Learning Framework for EEG-Based Stress Detection Using CNN-LSTM-Attention](https://arxiv.org/abs/2506.11179v1) | 2506.11179v1 | 6 |
| 2025-06-11 | [SparseSSM: Efficient Selective Structured State Space Models Can Be Pruned in One-Shot](https://arxiv.org/abs/2506.09613v1) | 2506.09613v1 | 10 |
| 2025-06-10 | [KARMA: A Multilevel Decomposition Hybrid Mamba Framework for Multivariate Long-Term Time Series Forecasting](https://arxiv.org/abs/2506.08939v1) | 2506.08939v1 | 6 |
| 2025-06-10 | [InceptionMamba: An Efficient Hybrid Network with Large Band Convolution and Bottleneck Mamba](https://arxiv.org/abs/2506.08735v3) | 2506.08735v3 | 6 |
| 2025-06-10 | [ECMNet:Lightweight Semantic Segmentation with Efficient CNN-Mamba Network](https://arxiv.org/abs/2506.08629v1) | 2506.08629v1 | 6 |
| 2025-06-10 | [MLVTG: Mamba-Based Feature Alignment and LLM-Driven Purification for Multi-Modal Video Temporal Grounding](https://arxiv.org/abs/2506.08512v2) | 2506.08512v2 | 6 |
| 2025-06-10 | [SEMA: a Scalable and Efficient Mamba like Attention via Token Localization and Averaging](https://arxiv.org/abs/2506.08297v2) | 2506.08297v2 | 8 |
| 2025-06-09 | [W4S4: WaLRUS Meets S4 for Long-Range Sequence Modeling](https://arxiv.org/abs/2506.07920v1) | 2506.07920v1 | 7 |
| 2025-06-09 | [Spatio-Temporal State Space Model For Efficient Event-Based Optical Flow](https://arxiv.org/abs/2506.07878v1) | 2506.07878v1 | 6 |
| 2025-06-09 | [M2Restore: Mixture-of-Experts-based Mamba-CNN Fusion Framework for All-in-One Image Restoration](https://arxiv.org/abs/2506.07814v1) | 2506.07814v1 | 6 |
| 2025-06-09 | [FMaMIL: Frequency-Driven Mamba Multi-Instance Learning for Weakly Supervised Lesion Segmentation in Medical Images](https://arxiv.org/abs/2506.07652v1) | 2506.07652v1 | 6 |
| 2025-06-09 | [FAMSeg: Fetal Femur and Cranial Ultrasound Segmentation Using Feature-Aware Attention and Mamba Enhancement](https://arxiv.org/abs/2506.07431v2) | 2506.07431v2 | 6 |
| 2025-06-07 | [Hybrid Vision Transformer-Mamba Framework for Autism Diagnosis via Eye-Tracking Analysis](https://arxiv.org/abs/2506.06886v1) | 2506.06886v1 | 6 |
| 2025-06-07 | [Flood-DamageSense: Multimodal Mamba with Multitask Learning for Building Flood Damage Assessment using SAR Remote Sensing Imagery](https://arxiv.org/abs/2506.06667v1) | 2506.06667v1 | 6 |
| 2025-06-05 | [Generalizable, real-time neural decoding with hybrid state-space models](https://arxiv.org/abs/2506.05320v2) | 2506.05320v2 | 6 |
| 2025-06-05 | [DM-SegNet: Dual-Mamba Architecture for 3D Medical Image Segmentation with Global Context Modeling](https://arxiv.org/abs/2506.05297v1) | 2506.05297v1 | 12 |
| 2025-06-05 | [Learning long range dependencies through time reversal symmetry breaking](https://arxiv.org/abs/2506.05259v1) | 2506.05259v1 | 6 |
| 2025-06-05 | [MesaNet: Sequence Modeling by Locally Optimal Test-Time Training](https://arxiv.org/abs/2506.05233v2) | 2506.05233v2 | 9 |
| 2025-06-05 | [UnHiPPO: Uncertainty-aware Initialization for State Space Models](https://arxiv.org/abs/2506.05065v1) | 2506.05065v1 | 6 |
| 2025-06-04 | [SiLIF: Structured State Space Model Dynamics and Parametrization for Spiking Neural Networks](https://arxiv.org/abs/2506.06374v4) | 2506.06374v4 | 8 |
| 2025-06-04 | [MambaNeXt-YOLO: A Hybrid State Space Model for Real-time Object Detection](https://arxiv.org/abs/2506.03654v3) | 2506.03654v3 | 14 |
| 2025-06-04 | [MamFusion: Multi-Mamba with Temporal Fusion for Partially Relevant Video Retrieval](https://arxiv.org/abs/2506.03473v1) | 2506.03473v1 | 10 |
| 2025-06-03 | [SportMamba: Adaptive Non-Linear Multi-Object Tracking with State Space Models for Team Sports](https://arxiv.org/abs/2506.03335v1) | 2506.03335v1 | 12 |
| 2025-06-03 | [InterMamba: Efficient Human-Human Interaction Generation with Adaptive Spatio-Temporal Mamba](https://arxiv.org/abs/2506.03084v1) | 2506.03084v1 | 6 |
| 2025-06-03 | [ControlMambaIR: Conditional Controls with State-Space Model for Image Restoration](https://arxiv.org/abs/2506.02633v1) | 2506.02633v1 | 6 |
| 2025-06-03 | [Comba: Improving Bilinear RNNs with Closed-loop Control](https://arxiv.org/abs/2506.02475v5) | 2506.02475v5 | 18 |
| 2025-06-03 | [ss-Mamba: Semantic-Spline Selective State-Space Model](https://arxiv.org/abs/2506.14802v1) | 2506.14802v1 | 12 |
| 2025-06-03 | [ConMamba: Contrastive Vision Mamba for Plant Disease Detection](https://arxiv.org/abs/2506.03213v2) | 2506.03213v2 | 10 |
| 2025-06-02 | [Are Mamba-based Audio Foundation Models the Best Fit for Non-Verbal Emotion Recognition?](https://arxiv.org/abs/2506.02258v1) | 2506.02258v1 | 6 |
| 2025-06-01 | [Mamba Drafters for Speculative Decoding](https://arxiv.org/abs/2506.01206v1) | 2506.01206v1 | 10 |
| 2025-06-01 | [PARROT: Synergizing Mamba and Attention-based SSL Pre-Trained Models via Parallel Branch Hadamard Optimal Transport for Speech Emotion Recognition](https://arxiv.org/abs/2506.01138v1) | 2506.01138v1 | 6 |
| 2025-06-01 | [ECP-Mamba: An Efficient Multi-scale Self-supervised Contrastive Learning Method with State Space Model for PolSAR Image Classification](https://arxiv.org/abs/2506.01040v1) | 2506.01040v1 | 12 |
| 2025-06-01 | [Self-supervised ControlNet with Spatio-Temporal Mamba for Real-world Video Super-resolution](https://arxiv.org/abs/2506.01037v1) | 2506.01037v1 | 6 |
| 2025-06-01 | [3D Skeleton-Based Action Recognition: A Review](https://arxiv.org/abs/2506.00915v1) | 2506.00915v1 | 8 |
| 2025-05-30 | [ACM-UNet: Adaptive Integration of CNNs and Mamba for Efficient Medical Image Segmentation](https://arxiv.org/abs/2505.24481v1) | 2505.24481v1 | 10 |
| 2025-05-30 | [Mamba Knockout for Unraveling Factual Information Flow](https://arxiv.org/abs/2505.24244v1) | 2505.24244v1 | 6 |
| 2025-05-29 | [Studying the Soupability of Documents in State Space Models](https://arxiv.org/abs/2505.24033v3) | 2505.24033v3 | 10 |
| 2025-05-29 | [TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning](https://arxiv.org/abs/2505.23719v2) | 2505.23719v2 | 6 |
| 2025-05-29 | [State Space Model Programming in Turing.jl](https://arxiv.org/abs/2505.23302v1) | 2505.23302v1 | 6 |
| 2025-05-29 | [PhyxMamba: Chaotic System Reconstruction from Short Context Observations with Generative State-Space Models](https://arxiv.org/abs/2505.23863v3) | 2505.23863v3 | 6 |
| 2025-05-29 | [SAMamba: Adaptive State Space Modeling with Hierarchical Vision for Infrared Small Target Detection](https://arxiv.org/abs/2505.23214v1) | 2505.23214v1 | 16 |
| 2025-05-28 | [RiverMamba: A State Space Model for Global River Discharge and Flood Forecasting](https://arxiv.org/abs/2505.22535v3) | 2505.22535v3 | 12 |
| 2025-05-28 | [Scaling Reasoning without Attention](https://arxiv.org/abs/2505.22425v1) | 2505.22425v1 | 8 |
| 2025-05-27 | [Revisiting Bi-Linear State Transitions in Recurrent Neural Networks](https://arxiv.org/abs/2505.21749v2) | 2505.21749v2 | 7 |
| 2025-05-27 | [Parallelization of Non-linear State-Space Models: Scaling Up Liquid-Resistance Liquid-Capacitance Networks for Efficient Sequence Modeling](https://arxiv.org/abs/2505.21717v6) | 2505.21717v6 | 9 |
| 2025-05-27 | [ZigzagPointMamba: Spatial-Semantic Mamba for Point Cloud Understanding](https://arxiv.org/abs/2505.21381v6) | 2505.21381v6 | 10 |
| 2025-05-27 | [Universal Speech Enhancement with Regression and Generative Mamba](https://arxiv.org/abs/2505.21198v2) | 2505.21198v2 | 8 |
| 2025-05-27 | [PMA: Towards Parameter-Efficient Point Cloud Understanding via Point Mamba Adapter](https://arxiv.org/abs/2505.20941v1) | 2505.20941v1 | 6 |
| 2025-05-27 | [HTMNet: A Hybrid Network with Transformer-Mamba Bottleneck Multimodal Fusion for Transparent and Reflective Objects Depth Completion](https://arxiv.org/abs/2505.20904v2) | 2505.20904v2 | 10 |
| 2025-05-27 | [HAD: Hybrid Architecture Distillation Outperforms Teacher in Genomic Sequence Modeling](https://arxiv.org/abs/2505.20836v1) | 2505.20836v1 | 9 |
| 2025-05-27 | [Sparsified State-Space Models are Efficient Highway Networks](https://arxiv.org/abs/2505.20698v1) | 2505.20698v1 | 8 |
| 2025-05-27 | [Mamba-Driven Topology Fusion for Monocular 3D Human Pose Estimation](https://arxiv.org/abs/2505.20611v2) | 2505.20611v2 | 10 |
| 2025-05-25 | [Latent Mamba Operator for Partial Differential Equations](https://arxiv.org/abs/2505.19105v2) | 2505.19105v2 | 6 |
| 2025-05-25 | [FastMamba: A High-Speed and Efficient Mamba Accelerator on FPGA with Accurate Quantization](https://arxiv.org/abs/2505.18975v4) | 2505.18975v4 | 10 |
| 2025-05-25 | [Hierarchical Mamba Meets Hyperbolic Geometry: A New Paradigm for Structured Language Embeddings](https://arxiv.org/abs/2505.18973v3) | 2505.18973v3 | 8 |
| 2025-05-24 | [Exemplar-Free Continual Learning for State Space Models](https://arxiv.org/abs/2505.18604v3) | 2505.18604v3 | 8 |
| 2025-05-24 | [TK-Mamba: Marrying KAN With Mamba for Text-Driven 3D Medical Image Segmentation](https://arxiv.org/abs/2505.18525v2) | 2505.18525v2 | 7 |
| 2025-05-23 | [Weakly-supervised Mamba-Based Mastoidectomy Shape Prediction for Cochlear Implant Surgery Using 3D T-Distribution Loss](https://arxiv.org/abs/2505.18368v1) | 2505.18368v1 | 6 |
| 2025-05-23 | [Geometric SSM: LTI State Space Models for Selective Tasks](https://arxiv.org/abs/2505.17932v2) | 2505.17932v2 | 12 |
| 2025-05-23 | [Hybrid Mamba-Transformer Decoder for Error-Correcting Codes](https://arxiv.org/abs/2505.17834v1) | 2505.17834v1 | 6 |
| 2025-05-23 | [Structured Linear CDEs: Maximally Expressive and Parallel-in-Time Sequence Models](https://arxiv.org/abs/2505.17761v2) | 2505.17761v2 | 6 |
| 2025-05-23 | [FuseMamba-VD: Dual Branch VideoMamba with Gated Class Token Fusion for Violence Detection](https://arxiv.org/abs/2506.03162v3) | 2506.03162v3 | 6 |
| 2025-05-23 | [Hypergraph Mamba for Efficient Whole Slide Image Understanding](https://arxiv.org/abs/2505.17457v2) | 2505.17457v2 | 11 |
| 2025-05-23 | [EVM-Fusion: An Explainable Vision Mamba Architecture with Neural Algorithmic Fusion](https://arxiv.org/abs/2505.17367v4) | 2505.17367v4 | 6 |
| 2025-05-22 | [PCMamba: Physics-Informed Cross-Modal State Space Model for Dual-Camera Compressive Hyperspectral Imaging](https://arxiv.org/abs/2505.16373v1) | 2505.16373v1 | 12 |
| 2025-05-22 | [SAMba-UNet: SAM2-Mamba UNet for Cardiac MRI in Medical Robotic Perception](https://arxiv.org/abs/2505.16304v2) | 2505.16304v2 | 6 |
| 2025-05-21 | [FR-Mamba: Time-Series Physical Field Reconstruction Based on State Space Model](https://arxiv.org/abs/2505.16083v1) | 2505.16083v1 | 12 |
| 2025-05-21 | [HAMF: A Hybrid Attention-Mamba Framework for Joint Scene Context Understanding and Future Motion Representation Learning](https://arxiv.org/abs/2505.15703v1) | 2505.15703v1 | 6 |
| 2025-05-21 | [UNet with Self-Adaptive Mamba-Like Attention and Causal-Resonance Learning for Medical Image Segmentation](https://arxiv.org/abs/2505.15234v2) | 2505.15234v2 | 6 |
| 2025-05-21 | [Mechanistic evaluation of Transformers and state space models](https://arxiv.org/abs/2505.15105v3) | 2505.15105v3 | 10 |
| 2025-05-21 | [RLBenchNet: The Right Network for the Right Reinforcement Learning Task](https://arxiv.org/abs/2505.15040v1) | 2505.15040v1 | 6 |
| 2025-05-20 | [TF-Mamba: Text-enhanced Fusion Mamba with Missing Modalities for Robust Multimodal Sentiment Analysis](https://arxiv.org/abs/2505.14329v2) | 2505.14329v2 | 6 |
| 2025-05-20 | [MATHDance: Mamba-Transformer Architecture with Uniform Tokenization for High-Quality 3D Dance Generation](https://arxiv.org/abs/2505.14222v3) | 2505.14222v3 | 10 |
| 2025-05-20 | [FractalMamba++: Scaling Vision Mamba Across Resolutions via Hilbert Fractal Geometry](https://arxiv.org/abs/2505.14062v4) | 2505.14062v4 | 6 |
| 2025-05-20 | [BiCrossMamba-ST: Speech Deepfake Detection with Bidirectional Mamba Spectro-Temporal Cross-Attention](https://arxiv.org/abs/2505.13930v1) | 2505.13930v1 | 6 |
| 2025-05-19 | [SourceDetMamba: A Graph-aware State Space Model for Source Detection in Sequential Hypergraphs](https://arxiv.org/abs/2505.12910v2) | 2505.12910v2 | 12 |
| 2025-05-19 | [Mamba-Adaptor: State Space Model Adaptor for Visual Recognition](https://arxiv.org/abs/2505.12685v1) | 2505.12685v1 | 12 |
| 2025-05-19 | [Safe-Sora: Safe Text-to-Video Generation via Graphical Watermarking](https://arxiv.org/abs/2505.12667v2) | 2505.12667v2 | 8 |
| 2025-05-18 | [MTIL: Encoding Full History with Mamba for Temporal Imitation Learning](https://arxiv.org/abs/2505.12410v3) | 2505.12410v3 | 13 |
| 2025-05-17 | [GeoMaNO: Geometric Mamba Neural Operator for Partial Differential Equations](https://arxiv.org/abs/2505.12020v1) | 2505.12020v1 | 6 |
| 2025-05-17 | [MedVKAN: Efficient Feature Extraction with Mamba and KAN for Medical Image Segmentation](https://arxiv.org/abs/2505.11797v2) | 2505.11797v2 | 6 |
| 2025-05-16 | [Regularity and Stability Properties of Selective SSMs with Discontinuous Gating](https://arxiv.org/abs/2505.11602v3) | 2505.11602v3 | 6 |
| 2025-05-16 | [Equal is Not Always Fair: A New Perspective on Hyperspectral Representation Non-Uniformity](https://arxiv.org/abs/2505.11267v1) | 2505.11267v1 | 8 |
| 2025-05-16 | [SM3D: Mitigating Spectral Bias and Semantic Dilution in Point Cloud State Space Models](https://arxiv.org/abs/2505.11099v3) | 2505.11099v3 | 10 |
| 2025-05-16 | [HSRMamba: Efficient Wavelet Stripe State Space Model for Hyperspectral Image Super-Resolution](https://arxiv.org/abs/2505.11062v1) | 2505.11062v1 | 12 |
| 2025-05-15 | [Seasonal Forecasting of Pan-Arctic Sea Ice with State Space Model](https://arxiv.org/abs/2505.10665v1) | 2505.10665v1 | 10 |
| 2025-05-15 | [SRMamba: Mamba for Super-Resolution of LiDAR Point Clouds](https://arxiv.org/abs/2505.10601v1) | 2505.10601v1 | 10 |
| 2025-05-15 | [MambaControl: Anatomy Graph-Enhanced Mamba ControlNet with Fourier Refinement for Diffusion-Based Disease Trajectory Prediction](https://arxiv.org/abs/2505.09965v1) | 2505.09965v1 | 6 |
| 2025-05-14 | [Dyadic Mamba: Long-term Dyadic Human Motion Synthesis](https://arxiv.org/abs/2505.09827v1) | 2505.09827v1 | 6 |
| 2025-05-14 | [Spec2VolCAMU-Net: A Spectrogram-to-Volume Model for EEG-to-fMRI Reconstruction based on Multi-directional Time-Frequency Convolutional Attention Encoder and Vision-Mamba U-Net](https://arxiv.org/abs/2505.09521v2) | 2505.09521v2 | 7 |
| 2025-05-14 | [Efficient Malicious UAV Detection Using Autoencoder-TSMamba Integration](https://arxiv.org/abs/2505.10585v1) | 2505.10585v1 | 6 |
| 2025-05-14 | [MrTrack: Register Mamba for Needle Tracking with Rapid Reciprocating Motion during Ultrasound-Guided Aspiration Biopsy](https://arxiv.org/abs/2505.09450v2) | 2505.09450v2 | 6 |
| 2025-05-14 | [HMamba: Hyperbolic Mamba for Sequential Recommendation](https://arxiv.org/abs/2505.09205v1) | 2505.09205v1 | 11 |
| 2025-05-13 | [Block-Biased Mamba for Long-Range Sequence Processing](https://arxiv.org/abs/2505.09022v1) | 2505.09022v1 | 10 |
| 2025-05-13 | [DyGSSM: Multi-view Dynamic Graph Embeddings with State Space Model Gradient Update](https://arxiv.org/abs/2505.09017v2) | 2505.09017v2 | 8 |
| 2025-05-13 | [A Mamba-based Network for Semi-supervised Singing Melody Extraction Using Confidence Binary Regularization](https://arxiv.org/abs/2505.08681v1) | 2505.08681v1 | 6 |
| 2025-05-13 | [Efficient Unstructured Pruning of Mamba State-Space Models for Resource-Constrained Environments](https://arxiv.org/abs/2505.08299v2) | 2505.08299v2 | 9 |
| 2025-05-12 | [Overflow Prevention Enhances Long-Context Recurrent LLMs](https://arxiv.org/abs/2505.07793v2) | 2505.07793v2 | 12 |
| 2025-05-12 | [FermatSyn: SAM2-Enhanced Bidirectional Mamba with Isotropic Spiral Scanning for Multi-Modal Medical Image Synthesis](https://arxiv.org/abs/2505.07687v5) | 2505.07687v5 | 6 |
| 2025-05-09 | [Topo-VM-UNetV2: Encoding Topology into Vision Mamba UNet for Polyp Segmentation](https://arxiv.org/abs/2505.06210v1) | 2505.06210v1 | 10 |
| 2025-05-08 | [PillarMamba: Learning Local-Global Context for Roadside Point Cloud via Hybrid State Space Model](https://arxiv.org/abs/2505.05397v1) | 2505.05397v1 | 12 |
| 2025-05-08 | [PRE-Mamba: A 4D State Space Model for Ultra-High-Frequent Event Camera Deraining](https://arxiv.org/abs/2505.05307v2) | 2505.05307v2 | 12 |
| 2025-05-07 | [M2Rec: Multi-scale Mamba for Efficient Sequential Recommendation](https://arxiv.org/abs/2505.04445v1) | 2505.04445v1 | 6 |
| 2025-05-07 | [WDMamba: When Wavelet Degradation Prior Meets Vision Mamba for Image Dehazing](https://arxiv.org/abs/2505.04369v1) | 2505.04369v1 | 6 |
| 2025-05-07 | [SMMT: Siamese Motion Mamba with Self-attention for Thermal Infrared Target Tracking](https://arxiv.org/abs/2505.04088v3) | 2505.04088v3 | 6 |
| 2025-05-06 | [MambaStyle: Efficient StyleGAN Inversion for Real Image Editing with State-Space Models](https://arxiv.org/abs/2505.15822v1) | 2505.15822v1 | 6 |
| 2025-05-06 | [Recall with Reasoning: Chain-of-Thought Distillation for Mamba's Long-Context Memory and Extrapolation](https://arxiv.org/abs/2505.03320v2) | 2505.03320v2 | 6 |
| 2025-05-06 | [Mamba-Diffusion Model with Learnable Wavelet for Controllable Symbolic Music Generation](https://arxiv.org/abs/2505.03314v1) | 2505.03314v1 | 6 |
| 2025-05-05 | [Robustly Invertible Nonlinear Dynamics and the BiLipREN: Contracting Neural Models with Contracting Inverses](https://arxiv.org/abs/2505.03069v1) | 2505.03069v1 | 6 |
| 2025-05-04 | [Learning Local Causal World Models with State Space Models and Attention](https://arxiv.org/abs/2505.02074v1) | 2505.02074v1 | 6 |
| 2025-05-02 | [CodeSSM: Towards State Space Models for Code Understanding](https://arxiv.org/abs/2505.01475v3) | 2505.01475v3 | 6 |
| 2025-05-02 | [VRS-UIE: Value-Driven Reordering Scanning for Underwater Image Enhancement](https://arxiv.org/abs/2505.01224v2) | 2505.01224v2 | 8 |
| 2025-05-02 | [LMDepth: Lightweight Mamba-based Monocular Depth Estimation for Real-World Deployment](https://arxiv.org/abs/2505.00980v1) | 2505.00980v1 | 6 |
| 2025-05-01 | [Vision Mamba in Remote Sensing: A Comprehensive Survey of Techniques, Applications and Outlook](https://arxiv.org/abs/2505.00630v2) | 2505.00630v2 | 10 |
| 2025-04-30 | [Mamba Based Feature Extraction And Adaptive Multilevel Feature Fusion For 3D Tumor Segmentation From Multi-modal Medical Image](https://arxiv.org/abs/2504.21281v1) | 2504.21281v1 | 6 |
| 2025-04-29 | [DYNAMAX: Dynamic computing for Transformers and Mamba based architectures](https://arxiv.org/abs/2504.20922v1) | 2504.20922v1 | 6 |
| 2025-04-29 | [Overcoming Quadratic Hardware Scaling for a Fully Connected Digital Oscillatory Neural Network](https://arxiv.org/abs/2504.20680v1) | 2504.20680v1 | 6 |
| 2025-04-29 | [MambaMoE: Mixture-of-Spectral-Spatial-Experts State Space Model for Hyperspectral Image Classification](https://arxiv.org/abs/2504.20509v2) | 2504.20509v2 | 12 |
| 2025-04-28 | [GPA-RAM: Grasp-Pretraining Augmented Robotic Attention Mamba for Spatial Task Learning](https://arxiv.org/abs/2504.19683v4) | 2504.19683v4 | 6 |
| 2025-04-25 | [S3MOT: Monocular 3D Object Tracking with Selective State Space Model](https://arxiv.org/abs/2504.18068v1) | 2504.18068v1 | 9 |
| 2025-04-24 | [DPMambaIR: All-in-One Image Restoration via Degradation-Aware Prompt State Space Model](https://arxiv.org/abs/2504.17732v3) | 2504.17732v3 | 12 |
| 2025-04-24 | [Mamba-Sea: A Mamba-based Framework with Global-to-Local Sequence Augmentation for Generalizable Medical Image Segmentation](https://arxiv.org/abs/2504.17515v1) | 2504.17515v1 | 10 |
| 2025-04-24 | [StereoMamba: Real-time and Robust Intraoperative Stereo Disparity Estimation via Long-range Spatial Dependencies](https://arxiv.org/abs/2504.17401v2) | 2504.17401v2 | 6 |
| 2025-04-24 | [Fine-Grained Fusion: The Missing Piece in Area-Efficient State Space Model Acceleration](https://arxiv.org/abs/2504.17333v1) | 2504.17333v1 | 6 |
| 2025-04-23 | [A Diff-Attention Aware State Space Fusion Model for Remote Sensing Classification](https://arxiv.org/abs/2504.16665v2) | 2504.16665v2 | 10 |
| 2025-04-22 | [GeneMamba: An Efficient and Effective Foundation Model on Single Cell Data](https://arxiv.org/abs/2504.16956v4) | 2504.16956v4 | 11 |
| 2025-04-22 | [MVQA: Mamba with Unified Sampling for Efficient Video Quality Assessment](https://arxiv.org/abs/2504.16003v1) | 2504.16003v1 | 6 |
| 2025-04-22 | [UINO-FSS: Unifying Representation Learning and Few-shot Segmentation via Hierarchical Distillation and Mamba-HyperCorrelation](https://arxiv.org/abs/2504.15669v5) | 2504.15669v5 | 6 |
| 2025-04-22 | [HS-Mamba: Full-Field Interaction Multi-Groups Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2504.15612v1) | 2504.15612v1 | 8 |
| 2025-04-20 | [VM-BHINet:Vision Mamba Bimanual Hand Interaction Network for 3D Interacting Hand Mesh Recovery From a Single RGB Image](https://arxiv.org/abs/2504.14618v1) | 2504.14618v1 | 10 |
| 2025-04-19 | [Efficient Spiking Point Mamba for Point Cloud Analysis](https://arxiv.org/abs/2504.14371v2) | 2504.14371v2 | 8 |
| 2025-04-19 | [Cross-attention for State-based model RWKV-7](https://arxiv.org/abs/2504.14260v1) | 2504.14260v1 | 6 |
| 2025-04-18 | [WeatherGen: A Unified Diverse Weather Generator for LiDAR Point Clouds via Spider Mamba Diffusion](https://arxiv.org/abs/2504.13561v1) | 2504.13561v1 | 6 |
| 2025-04-18 | [U-Shape Mamba: State Space Model for faster diffusion](https://arxiv.org/abs/2504.13499v2) | 2504.13499v2 | 12 |
| 2025-04-17 | [Hierarchical Feature Learning for Medical Point Clouds via State Space Model](https://arxiv.org/abs/2504.13015v3) | 2504.13015v3 | 6 |
| 2025-04-16 | [RadMamba: Efficient Human Activity Recognition through Radar-based Micro-Doppler-Oriented Mamba State-Space Model](https://arxiv.org/abs/2504.12039v3) | 2504.12039v3 | 12 |
| 2025-04-16 | [ACMamba: Fast Unsupervised Anomaly Detection via An Asymmetrical Consensus State Space Model](https://arxiv.org/abs/2504.11781v1) | 2504.11781v1 | 12 |
| 2025-04-15 | [Mamba-Based Ensemble learning for White Blood Cell Classification](https://arxiv.org/abs/2504.11438v1) | 2504.11438v1 | 6 |
| 2025-04-15 | [Minitron-SSM: Efficient Hybrid Language Model Compression through Group-Aware SSM Pruning](https://arxiv.org/abs/2504.11409v2) | 2504.11409v2 | 10 |
| 2025-04-15 | [Sensitivity Analysis of State Space Models for Scrap Composition Estimation in EAF and BOF](https://arxiv.org/abs/2504.11319v1) | 2504.11319v1 | 6 |
| 2025-04-15 | [Efficient Remote Sensing Change Detection with Change State Space Models](https://arxiv.org/abs/2504.11080v2) | 2504.11080v2 | 10 |
| 2025-04-14 | [M1: Towards Scalable Test-Time Compute with Mamba Reasoning Models](https://arxiv.org/abs/2504.10449v3) | 2504.10449v3 | 6 |
| 2025-04-14 | [Classifying Copy Number Variations Using State Space Modeling of Targeted Sequencing Data: A Case Study in Thalassemia](https://arxiv.org/abs/2504.10338v1) | 2504.10338v1 | 6 |
| 2025-04-14 | [Global and Local Mamba Network for Multi-Modality Medical Image Super-Resolution](https://arxiv.org/abs/2504.10105v1) | 2504.10105v1 | 10 |
| 2025-04-13 | [OmniMamba4D: Spatio-temporal Mamba for longitudinal CT lesion segmentation](https://arxiv.org/abs/2504.09655v2) | 2504.09655v2 | 6 |
| 2025-04-13 | [Sparse Deformable Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2504.09446v2) | 2504.09446v2 | 6 |
| 2025-04-13 | [Unified GARCH-Recurrent Neural Network in Financial Volatility Forecasting](https://arxiv.org/abs/2504.09380v2) | 2504.09380v2 | 7 |
| 2025-04-12 | [Stochastic Claims Reserving Using State Space Modeling](https://arxiv.org/abs/2504.09292v1) | 2504.09292v1 | 6 |
| 2025-04-12 | [Repetitive Contrastive Learning Enhances Mamba's Selectivity in Time Series Prediction](https://arxiv.org/abs/2504.09185v2) | 2504.09185v2 | 6 |
| 2025-04-10 | [DGFamba: Learning Flow Factorized State Space for Visual Domain Generalization](https://arxiv.org/abs/2504.08019v1) | 2504.08019v1 | 10 |
| 2025-04-10 | [ms-Mamba: Multi-scale Mamba for Time-Series Forecasting](https://arxiv.org/abs/2504.07654v2) | 2504.07654v2 | 8 |
| 2025-04-10 | [A Novel Mamba-based Sequential Recommendation Method](https://arxiv.org/abs/2504.07398v1) | 2504.07398v1 | 6 |
| 2025-04-09 | [HGMamba: Enhancing 3D Human Pose Estimation with a HyperGCN-Mamba Network](https://arxiv.org/abs/2504.06638v1) | 2504.06638v1 | 10 |
| 2025-04-08 | [Fusing Global and Local: Transformer-CNN Synergy for Next-Gen Current Estimation](https://arxiv.org/abs/2504.07996v2) | 2504.07996v2 | 6 |
| 2025-04-08 | [DefMamba: Deformable Visual State Space Model](https://arxiv.org/abs/2504.05794v1) | 2504.05794v1 | 12 |
| 2025-04-07 | [Leveraging State Space Models in Long Range Genomics](https://arxiv.org/abs/2504.06304v2) | 2504.06304v2 | 6 |
| 2025-04-07 | [One-Minute Video Generation with Test-Time Training](https://arxiv.org/abs/2504.05298v1) | 2504.05298v1 | 8 |
| 2025-04-07 | [State Tuning: State-based Test-Time Scaling on RWKV-7](https://arxiv.org/abs/2504.05097v1) | 2504.05097v1 | 6 |
| 2025-04-07 | [GAMDTP: Dynamic Trajectory Prediction with Graph Attention Mamba Network](https://arxiv.org/abs/2504.04862v1) | 2504.04862v1 | 6 |
| 2025-04-07 | [Dynamic Vision Mamba](https://arxiv.org/abs/2504.04787v1) | 2504.04787v1 | 6 |
| 2025-04-06 | [GAMBAS: Generalised-Hilbert Mamba for Super-resolution of Paediatric Ultra-Low-Field MRI](https://arxiv.org/abs/2504.04523v2) | 2504.04523v2 | 6 |
| 2025-04-04 | [Nemotron-H: A Family of Accurate and Efficient Hybrid Mamba-Transformer Models](https://arxiv.org/abs/2504.03624v4) | 2504.03624v4 | 6 |
| 2025-04-04 | [Pyramid-based Mamba Multi-class Unsupervised Anomaly Detection](https://arxiv.org/abs/2504.03442v1) | 2504.03442v1 | 10 |
| 2025-04-04 | [Mamba as a Bridge: Where Vision Foundation Models Meet Vision Language Models for Domain-Generalized Semantic Segmentation](https://arxiv.org/abs/2504.03193v2) | 2504.03193v2 | 8 |
| 2025-04-03 | [Learning Phase Distortion with Selective State Space Models for Video Turbulence Mitigation](https://arxiv.org/abs/2504.02697v2) | 2504.02697v2 | 15 |
| 2025-04-03 | [Audio-visual Controlled Video Diffusion with Masked Selective State Spaces Modeling for Natural Talking Head Generation](https://arxiv.org/abs/2504.02542v3) | 2504.02542v3 | 7 |
| 2025-04-03 | [Cognitive Memory in Large Language Models](https://arxiv.org/abs/2504.02441v2) | 2504.02441v2 | 6 |
| 2025-04-02 | [Mesh Mamba: A Unified State Space Model for Saliency Prediction in Non-Textured and Textured Meshes](https://arxiv.org/abs/2504.01466v2) | 2504.01466v2 | 12 |
| 2025-04-02 | [Attention Mamba: Time Series Modeling with Adaptive Pooling Acceleration and Receptive Field Enhancements](https://arxiv.org/abs/2504.02013v1) | 2504.02013v1 | 6 |
| 2025-04-01 | [Detecting Financial Fraud with Hybrid Deep Learning: A Mix-of-Experts Approach to Sequential and Anomalous Patterns](https://arxiv.org/abs/2504.03750v1) | 2504.03750v1 | 6 |
| 2025-04-01 | [Scaling Up Resonate-and-Fire Networks for Fast Deep Learning](https://arxiv.org/abs/2504.00719v1) | 2504.00719v1 | 6 |
| 2025-04-01 | [ParallelFlow: Parallelizing Linear Transformers via Flow Discretization](https://arxiv.org/abs/2504.00492v1) | 2504.00492v1 | 8 |
| 2025-03-31 | [TransMamba: A Sequence-Level Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2503.24067v2) | 2503.24067v2 | 10 |
| 2025-03-31 | [AMMSM: Adaptive Motion Magnification and Sparse Mamba for Micro-Expression Recognition](https://arxiv.org/abs/2503.24057v1) | 2503.24057v1 | 6 |
| 2025-03-31 | [L2RU: a Structured State Space Model with prescribed L2-bound](https://arxiv.org/abs/2503.23818v3) | 2503.23818v3 | 6 |
| 2025-03-30 | [ViT-Linearizer: Distilling Quadratic Knowledge into Linear-Time Vision Models](https://arxiv.org/abs/2504.00037v2) | 2504.00037v2 | 7 |
| 2025-03-29 | [Efficient Explicit Joint-level Interaction Modeling with Mamba for Text-guided HOI Generation](https://arxiv.org/abs/2503.23121v1) | 2503.23121v1 | 6 |
| 2025-03-28 | [Quamba2: A Robust and Scalable Post-training Quantization Framework for Selective State Space Models](https://arxiv.org/abs/2503.22879v4) | 2503.22879v4 | 13 |
| 2025-03-28 | [NetSSM: Multi-Flow and State-Aware Network Trace Generation using State Space Models](https://arxiv.org/abs/2503.22663v3) | 2503.22663v3 | 6 |
| 2025-03-27 | [Q-MambaIR: Accurate Quantized Mamba for Efficient Image Restoration](https://arxiv.org/abs/2503.21970v3) | 2503.21970v3 | 6 |
| 2025-03-27 | [VADMamba: Exploring State Space Models for Fast Video Anomaly Detection](https://arxiv.org/abs/2503.21169v1) | 2503.21169v1 | 12 |
| 2025-03-26 | [Adaptive State-Space Mamba for Real-Time Sensor Data Anomaly Detection](https://arxiv.org/abs/2503.22743v2) | 2503.22743v2 | 6 |
| 2025-03-26 | [ReverBERT: A State Space Model for Efficient Text-Driven Speech Style Transfer](https://arxiv.org/abs/2503.20992v2) | 2503.20992v2 | 10 |
| 2025-03-26 | [Reasoning Beyond Limits: Advances and Open Problems for LLMs](https://arxiv.org/abs/2503.22732v2) | 2503.22732v2 | 8 |
| 2025-03-26 | [Ancestral Mamba: Enhancing Selective Discriminant Space Model with Online Visual Prototype Learning for Efficient and Robust Discriminant Approach](https://arxiv.org/abs/2503.22729v1) | 2503.22729v1 | 6 |
| 2025-03-26 | [Mamba-3D as Masked Autoencoders for Accurate and Data-Efficient Analysis of Medical Ultrasound Videos](https://arxiv.org/abs/2503.20258v1) | 2503.20258v1 | 6 |
| 2025-03-26 | [Exploiting Temporal State Space Sharing for Video Semantic Segmentation](https://arxiv.org/abs/2503.20824v1) | 2503.20824v1 | 8 |
| 2025-03-25 | [EventMamba: Enhancing Spatio-Temporal Locality with State Space Models for Event-Based Video Reconstruction](https://arxiv.org/abs/2503.19721v3) | 2503.19721v3 | 12 |
| 2025-03-25 | [Prompt-Guided Dual-Path UNet with Mamba for Medical Image Segmentation](https://arxiv.org/abs/2503.19589v1) | 2503.19589v1 | 10 |
| 2025-03-25 | [ASP-VMUNet: Atrous Shifted Parallel Vision Mamba U-Net for Skin Lesion Segmentation](https://arxiv.org/abs/2503.19427v1) | 2503.19427v1 | 10 |
| 2025-03-25 | [A Comprehensive Analysis of Mamba for 3D Volumetric Medical Image Segmentation](https://arxiv.org/abs/2503.19308v1) | 2503.19308v1 | 12 |
| 2025-03-25 | [$L^2$FMamba: Lightweight Light Field Image Super-Resolution with State Space Model](https://arxiv.org/abs/2503.19253v1) | 2503.19253v1 | 12 |
| 2025-03-24 | [Distil-xLSTM: Learning Attention Mechanisms through Recurrent Structures](https://arxiv.org/abs/2503.18565v1) | 2503.18565v1 | 7 |
| 2025-03-24 | [Exploring State Space Model in Wavelet Domain: An Infrared and Visible Image Fusion Network via Wavelet Transform and State Space Model](https://arxiv.org/abs/2503.18378v1) | 2503.18378v1 | 10 |
| 2025-03-23 | [GLADMamba: Unsupervised Graph-Level Anomaly Detection Powered by Selective State Space Model](https://arxiv.org/abs/2503.17903v2) | 2503.17903v2 | 15 |
| 2025-03-22 | [MAMAT: 3D Mamba-Based Atmospheric Turbulence Removal and its Object Detection Capability](https://arxiv.org/abs/2503.17700v1) | 2503.17700v1 | 6 |
| 2025-03-22 | [Advancing Intelligent Sequence Modeling: Evolution, Trade-offs, and Applications of State-Space Architectures from S4 to Mamba](https://arxiv.org/abs/2503.18970v4) | 2503.18970v4 | 15 |
| 2025-03-21 | [MM-UNet: Meta Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2503.17540v1) | 2503.17540v1 | 12 |
| 2025-03-21 | [Cross-Modal Interactive Perception Network with Mamba for Lung Tumor Segmentation in PET-CT Images](https://arxiv.org/abs/2503.17261v1) | 2503.17261v1 | 6 |
| 2025-03-21 | [Enhancing Steering Estimation with Semantic-Aware GNNs](https://arxiv.org/abs/2503.17153v1) | 2503.17153v1 | 6 |
| 2025-03-20 | [Lyra: An Efficient and Expressive Subquadratic Architecture for Modeling Biological Sequences](https://arxiv.org/abs/2503.16351v1) | 2503.16351v1 | 6 |
| 2025-03-20 | [Binarized Mamba-Transformer for Lightweight Quad Bayer HybridEVS Demosaicing](https://arxiv.org/abs/2503.16134v1) | 2503.16134v1 | 6 |
| 2025-03-20 | [GazeSCRNN: Event-based Near-eye Gaze Tracking using a Spiking Neural Network](https://arxiv.org/abs/2503.16012v1) | 2503.16012v1 | 6 |
| 2025-03-20 | [SaMam: Style-aware State Space Model for Arbitrary Image Style Transfer](https://arxiv.org/abs/2503.15934v1) | 2503.15934v1 | 10 |
| 2025-03-18 | [Core-Periphery Principle Guided State Space Model for Functional Connectome Classification](https://arxiv.org/abs/2503.14655v1) | 2503.14655v1 | 12 |
| 2025-03-18 | [State Space Model Meets Transformer: A New Paradigm for 3D Object Detection](https://arxiv.org/abs/2503.14493v2) | 2503.14493v2 | 6 |
| 2025-03-18 | [MamBEV: Enabling State Space Models to Learn Birds-Eye-View Representations](https://arxiv.org/abs/2503.13858v2) | 2503.13858v2 | 10 |
| 2025-03-17 | [MaTVLM: Hybrid Mamba-Transformer for Efficient Vision-Language Modeling](https://arxiv.org/abs/2503.13440v2) | 2503.13440v2 | 6 |
| 2025-03-17 | [xLSTM 7B: A Recurrent LLM for Fast and Efficient Inference](https://arxiv.org/abs/2503.13427v1) | 2503.13427v1 | 7 |
| 2025-03-17 | [DynSTG-Mamba: Dynamic Spatio-Temporal Graph Mamba with Cross-Graph Knowledge Distillation for Gait Disorders Recognition](https://arxiv.org/abs/2503.13156v2) | 2503.13156v2 | 8 |
| 2025-03-17 | [TFDM: Time-Variant Frequency-Based Point Cloud Diffusion with Mamba](https://arxiv.org/abs/2503.13004v1) | 2503.13004v1 | 10 |
| 2025-03-16 | [BS-Mamba for Black-Soil Area Detection On the Qinghai-Tibetan Plateau](https://arxiv.org/abs/2503.12495v1) | 2503.12495v1 | 6 |
| 2025-03-16 | [MambaIC: State Space Models for High-Performance Learned Image Compression](https://arxiv.org/abs/2503.12461v3) | 2503.12461v3 | 12 |
| 2025-03-16 | [VideoMAP: Toward Scalable Mamba-based Video Autoregressive Pretraining](https://arxiv.org/abs/2503.12332v1) | 2503.12332v1 | 6 |
| 2025-03-15 | [Text-Driven Video Style Transfer with State-Space Models: Extending StyleMamba for Temporal Coherence](https://arxiv.org/abs/2503.12291v2) | 2503.12291v2 | 6 |
| 2025-03-15 | [UniMamba: Unified Spatial-Channel Representation Learning with Group-Efficient Mamba for LiDAR-based 3D Object Detection](https://arxiv.org/abs/2503.12009v3) | 2503.12009v3 | 10 |
| 2025-03-14 | [Vamba: Understanding Hour-Long Videos with Hybrid Mamba-Transformers](https://arxiv.org/abs/2503.11579v2) | 2503.11579v2 | 6 |
| 2025-03-14 | [BioMamba: Leveraging Spectro-Temporal Embedding in Bidirectional Mamba for Enhanced Biosignal Classification](https://arxiv.org/abs/2503.11741v3) | 2503.11741v3 | 6 |
| 2025-03-14 | [Hierarchical Information-Guided Spatio-Temporal Mamba for Stock Time Series Forecasting](https://arxiv.org/abs/2503.11387v1) | 2503.11387v1 | 6 |
| 2025-03-14 | [Technologies on Effectiveness and Efficiency: A Survey of State Spaces Models](https://arxiv.org/abs/2503.11224v1) | 2503.11224v1 | 8 |
| 2025-03-13 | [OuroMamba: A Data-Free Quantization Framework for Vision Mamba](https://arxiv.org/abs/2503.10959v2) | 2503.10959v2 | 8 |
| 2025-03-13 | [Trajectory Mamba: Efficient Attention-Mamba Forecasting Model Based on Selective SSM](https://arxiv.org/abs/2503.10898v1) | 2503.10898v1 | 6 |
| 2025-03-13 | [Mamba time series forecasting with uncertainty quantification](https://arxiv.org/abs/2503.10873v2) | 2503.10873v2 | 10 |
| 2025-03-13 | [Fixed-Point RNNs: Interpolating from Diagonal to Dense](https://arxiv.org/abs/2503.10799v3) | 2503.10799v3 | 6 |
| 2025-03-13 | [Category Prompt Mamba Network for Nuclei Segmentation and Classification](https://arxiv.org/abs/2503.10422v2) | 2503.10422v2 | 6 |
| 2025-03-13 | [RoMA: Scaling up Mamba-based Foundation Models for Remote Sensing](https://arxiv.org/abs/2503.10392v2) | 2503.10392v2 | 6 |
| 2025-03-13 | [Mamba-VA: A Mamba-based Approach for Continuous Emotion Recognition in Valence-Arousal Space](https://arxiv.org/abs/2503.10104v1) | 2503.10104v1 | 8 |
| 2025-03-13 | [Multi-Modal Mamba Modeling for Survival Prediction (M4Survive): Adapting Joint Foundation Model Representations](https://arxiv.org/abs/2503.10057v1) | 2503.10057v1 | 6 |
| 2025-03-13 | [HiCMamba: Enhancing Hi-C Resolution and Identifying 3D Genome Structures with State Space Modeling](https://arxiv.org/abs/2503.10713v1) | 2503.10713v1 | 12 |
| 2025-03-12 | [ViM-VQ: Efficient Post-Training Vector Quantization for Visual Mamba](https://arxiv.org/abs/2503.09509v2) | 2503.09509v2 | 12 |
| 2025-03-12 | [Dual-Domain Homogeneous Fusion with Cross-Modal Mamba and Progressive Decoder for 3D Object Detection](https://arxiv.org/abs/2503.08992v2) | 2503.08992v2 | 6 |
| 2025-03-11 | [OmniMamba: Efficient and Unified Multimodal Understanding and Generation via State Space Models](https://arxiv.org/abs/2503.08686v1) | 2503.08686v1 | 12 |
| 2025-03-11 | [MinGRU-Based Encoder for Turbo Autoencoder Frameworks](https://arxiv.org/abs/2503.08451v1) | 2503.08451v1 | 12 |
| 2025-03-10 | [SegResMamba: An Efficient Architecture for 3D Medical Image Segmentation](https://arxiv.org/abs/2503.07766v1) | 2503.07766v1 | 10 |
| 2025-03-10 | [MambaFlow: A Mamba-Centric Architecture for End-to-End Optical Flow Estimation](https://arxiv.org/abs/2503.07046v4) | 2503.07046v4 | 8 |
| 2025-03-09 | [Global-Aware Monocular Semantic Scene Completion with State Space Models](https://arxiv.org/abs/2503.06569v1) | 2503.06569v1 | 14 |
| 2025-03-09 | [Future-Aware Interaction Network For Motion Forecasting](https://arxiv.org/abs/2503.06565v1) | 2503.06565v1 | 8 |
| 2025-03-09 | [M$^3$amba: CLIP-driven Mamba Model for Multi-modal Remote Sensing Classification](https://arxiv.org/abs/2503.06446v1) | 2503.06446v1 | 6 |
| 2025-03-09 | [Swift Hydra: Self-Reinforcing Generative Framework for Anomaly Detection with Multiple Mamba Models](https://arxiv.org/abs/2503.06413v2) | 2503.06413v2 | 6 |
| 2025-03-09 | [Spectral State Space Model for Rotation-Invariant Visual Representation Learning](https://arxiv.org/abs/2503.06369v3) | 2503.06369v3 | 10 |
| 2025-03-07 | [Linear-MoE: Linear Sequence Modeling Meets Mixture-of-Experts](https://arxiv.org/abs/2503.05447v2) | 2503.05447v2 | 9 |
| 2025-03-06 | [Spectral Informed Mamba for Robust Point Cloud Processing](https://arxiv.org/abs/2503.04953v2) | 2503.04953v2 | 10 |
| 2025-03-06 | [An Extended State Space Model of Aggregated Electric Vehicles for Flexibility Estimation and Power Control](https://arxiv.org/abs/2503.04714v1) | 2503.04714v1 | 6 |
| 2025-03-06 | [STORM: Token-Efficient Long Video Understanding for Multimodal LLMs](https://arxiv.org/abs/2503.04130v4) | 2503.04130v4 | 8 |
| 2025-03-05 | [Tri-timescale Beamforming Design for Tri-hybrid Architectures with Reconfigurable Antennas](https://arxiv.org/abs/2503.03620v2) | 2503.03620v2 | 6 |
| 2025-03-05 | [State-offset Tuning: State-based Parameter-Efficient Fine-Tuning for State Space Models](https://arxiv.org/abs/2503.03499v2) | 2503.03499v2 | 6 |
| 2025-03-05 | [JamMa: Ultra-lightweight Local Feature Matching with Joint Mamba](https://arxiv.org/abs/2503.03437v1) | 2503.03437v1 | 6 |
| 2025-03-05 | [PathRWKV: Enhancing Whole Slide Image Inference with Asymmetric Recurrent Modeling](https://arxiv.org/abs/2503.03199v5) | 2503.03199v5 | 13 |
| 2025-03-04 | [XFMamba: Cross-Fusion Mamba for Multi-View Medical Image Classification](https://arxiv.org/abs/2503.02619v1) | 2503.02619v1 | 6 |
| 2025-03-04 | [COMMA: Coordinate-aware Modulated Mamba Network for 3D Dispersed Vessel Segmentation](https://arxiv.org/abs/2503.02332v3) | 2503.02332v3 | 6 |
| 2025-03-04 | [SSNet: Saliency Prior and State Space Model-based Network for Salient Object Detection in RGB-D Images](https://arxiv.org/abs/2503.02270v1) | 2503.02270v1 | 6 |
| 2025-03-04 | [Low-Level Matters: An Efficient Hybrid Architecture for Robust Multi-frame Infrared Small Target Detection](https://arxiv.org/abs/2503.02220v1) | 2503.02220v1 | 6 |
| 2025-03-03 | [Forgetting Transformer: Softmax Attention with a Forget Gate](https://arxiv.org/abs/2503.02130v2) | 2503.02130v2 | 6 |
| 2025-03-03 | [Mamba base PKD for efficient knowledge compression](https://arxiv.org/abs/2503.01727v2) | 2503.01727v2 | 6 |
| 2025-03-03 | [SparseMamba-PCL: Scribble-Supervised Medical Image Segmentation via SAM-Guided Progressive Collaborative Learning](https://arxiv.org/abs/2503.01633v1) | 2503.01633v1 | 6 |
| 2025-03-03 | [From Claims to Evidence: A Unified Framework and Critical Analysis of CNN vs. Transformer vs. Mamba in Medical Image Segmentation](https://arxiv.org/abs/2503.01306v1) | 2503.01306v1 | 6 |
| 2025-03-03 | [DCAMamba: Mamba-based Rapid Response DC Arc Fault Detection](https://arxiv.org/abs/2503.01264v1) | 2503.01264v1 | 6 |
| 2025-03-03 | [SCSegamba: Lightweight Structure-Aware Vision Mamba for Crack Segmentation in Structures](https://arxiv.org/abs/2503.01113v3) | 2503.01113v3 | 6 |
| 2025-03-01 | [2DMCG:2DMambawith Change Flow Guidance for Change Detection in Remote Sensing](https://arxiv.org/abs/2503.00521v1) | 2503.00521v1 | 6 |
| 2025-02-28 | [Visual Attention Exploration in Vision-Based Mamba Models](https://arxiv.org/abs/2502.20764v1) | 2502.20764v1 | 10 |
| 2025-02-28 | [A Quantum-Empowered SPEI Drought Forecasting Algorithm Using Spatially-Aware Mamba Network](https://arxiv.org/abs/2502.20703v2) | 2502.20703v2 | 8 |
| 2025-02-26 | [EndoMamba: An Efficient Foundation Model for Endoscopic Videos via Hierarchical Pre-training](https://arxiv.org/abs/2502.19090v2) | 2502.19090v2 | 10 |
| 2025-02-25 | [Systems and Algorithms for Convolutional Multi-Hybrid Language Models at Scale](https://arxiv.org/abs/2503.01868v1) | 2503.01868v1 | 8 |
| 2025-02-25 | [Enhancing Speech Quality through the Integration of BGRU and Transformer Architectures](https://arxiv.org/abs/2502.17911v1) | 2502.17911v1 | 6 |
| 2025-02-25 | [An Efficient Self-Supervised Framework for Long-Sequence EEG Modeling](https://arxiv.org/abs/2502.17873v2) | 2502.17873v2 | 6 |
| 2025-02-24 | [PICASO: Permutation-Invariant Context Composition with State Space Models](https://arxiv.org/abs/2502.17605v2) | 2502.17605v2 | 6 |
| 2025-02-24 | [MDN: Mamba-Driven Dualstream Network For Medical Hyperspectral Image Segmentation](https://arxiv.org/abs/2502.17255v1) | 2502.17255v1 | 8 |
| 2025-02-24 | [MambaFlow: A Novel and Flow-guided State Space Model for Scene Flow Estimation](https://arxiv.org/abs/2502.16907v1) | 2502.16907v1 | 12 |
| 2025-02-23 | [A Reverse Mamba Attention Network for Pathological Liver Segmentation](https://arxiv.org/abs/2502.18232v2) | 2502.18232v2 | 12 |
| 2025-02-23 | [MAPN: Enhancing Heterogeneous Sparse Graph Representation by Mamba-based Asynchronous Aggregation](https://arxiv.org/abs/2502.16454v1) | 2502.16454v1 | 6 |
| 2025-02-22 | [SalM$^{2}$: An Extremely Lightweight Saliency Mamba Model for Real-Time Cognitive Awareness of Driver Attention](https://arxiv.org/abs/2502.16214v2) | 2502.16214v2 | 6 |
| 2025-02-22 | [Improving Speech Enhancement by Cross- and Sub-band Processing with State Space Model](https://arxiv.org/abs/2502.16207v1) | 2502.16207v1 | 12 |
| 2025-02-21 | [LaTIM: Measuring Latent Token-to-Token Interactions in Mamba Models](https://arxiv.org/abs/2502.15612v2) | 2502.15612v2 | 12 |
| 2025-02-21 | [LightMamba: Efficient Mamba Acceleration on FPGA with Quantization and Hardware Co-design](https://arxiv.org/abs/2502.15260v2) | 2502.15260v2 | 10 |
| 2025-02-21 | [TransMamba: Fast Universal Architecture Adaption from Transformers to Mamba](https://arxiv.org/abs/2502.15130v2) | 2502.15130v2 | 7 |
| 2025-02-20 | [Exploring RWKV for Sentence Embeddings: Layer-wise Analysis and Baseline Comparison for Semantic Similarity](https://arxiv.org/abs/2502.14620v1) | 2502.14620v1 | 8 |
| 2025-02-20 | [Multiscale Byte Language Models -- A Hierarchical Architecture for Causal Million-Length Sequence Modeling](https://arxiv.org/abs/2502.14553v1) | 2502.14553v1 | 11 |
| 2025-02-20 | [Llamba: Scaling Distilled Recurrent Models for Efficient Language Processing](https://arxiv.org/abs/2502.14458v2) | 2502.14458v2 | 7 |
| 2025-02-20 | [Topology-Aware Wavelet Mamba for Airway Structure Segmentation in Postoperative Recurrent Nasopharyngeal Carcinoma CT Scans](https://arxiv.org/abs/2502.14363v1) | 2502.14363v1 | 11 |
| 2025-02-19 | [MambaLiteSR: Image Super-Resolution with Low-Rank Mamba using Knowledge Distillation](https://arxiv.org/abs/2502.14090v1) | 2502.14090v1 | 6 |
| 2025-02-19 | [MoM: Linear Sequence Modeling with Mixture-of-Memories](https://arxiv.org/abs/2502.13685v4) | 2502.13685v4 | 9 |
| 2025-02-19 | [CardiacMamba: A Multimodal RGB-RF Fusion Framework with State Space Models for Remote Physiological Measurement](https://arxiv.org/abs/2502.13624v1) | 2502.13624v1 | 12 |
| 2025-02-19 | [MobileViM: A Light-weight and Dimension-independent Vision Mamba for 3D Medical Image Analysis](https://arxiv.org/abs/2502.13524v4) | 2502.13524v4 | 6 |
| 2025-02-18 | [Multimodal Mamba: Decoder-only Multimodal State Space Model via Quadratic to Linear Distillation](https://arxiv.org/abs/2502.13145v2) | 2502.13145v2 | 16 |
| 2025-02-18 | [DAMamba: Vision State Space Model with Dynamic Adaptive Scan](https://arxiv.org/abs/2502.12627v1) | 2502.12627v1 | 12 |
| 2025-02-16 | [RT-DEMT: A hybrid real-time acupoint detection model combining mamba and transformer](https://arxiv.org/abs/2502.11179v1) | 2502.11179v1 | 6 |
| 2025-02-16 | [DA-Mamba: Domain Adaptive Hybrid Mamba-Transformer Based One-Stage Object Detection](https://arxiv.org/abs/2502.11178v2) | 2502.11178v2 | 10 |
| 2025-02-16 | [DuplexMamba: Enhancing Real-time Speech Conversations with Duplex and Streaming Capabilities](https://arxiv.org/abs/2502.11123v3) | 2502.11123v3 | 6 |
| 2025-02-15 | [HybriDNA: A Hybrid Transformer-Mamba2 Long-Range DNA Language Model](https://arxiv.org/abs/2502.10807v2) | 2502.10807v2 | 6 |
| 2025-02-15 | [Occlusion-aware Text-Image-Point Cloud Pretraining for Open-World 3D Object Recognition](https://arxiv.org/abs/2502.10674v2) | 2502.10674v2 | 8 |
| 2025-02-14 | [DeltaProduct: Improving State-Tracking in Linear RNNs via Householder Products](https://arxiv.org/abs/2502.10297v7) | 2502.10297v7 | 13 |
| 2025-02-14 | [From Markov to Laplace: How Mamba In-Context Learns Markov Chains](https://arxiv.org/abs/2502.10178v2) | 2502.10178v2 | 6 |
| 2025-02-14 | [Using Subspace Algorithms for the Estimation of Linear State Space Models for Over-Differenced Processes](https://arxiv.org/abs/2502.09987v1) | 2502.09987v1 | 6 |
| 2025-02-14 | [A Lightweight and Effective Image Tampering Localization Network with Vision Mamba](https://arxiv.org/abs/2502.09941v1) | 2502.09941v1 | 10 |
| 2025-02-12 | [scMamba: A Pre-Trained Model for Single-Nucleus RNA Sequencing Analysis in Neurodegenerative Disorders](https://arxiv.org/abs/2502.19429v1) | 2502.19429v1 | 6 |
| 2025-02-12 | [From Layers to States: A State Space Model Perspective to Deep Neural Network Layer Dynamics](https://arxiv.org/abs/2502.10463v1) | 2502.10463v1 | 8 |
| 2025-02-12 | [SS4Rec: Continuous-Time Sequential Recommendation with State Space Models](https://arxiv.org/abs/2502.08132v3) | 2502.08132v3 | 8 |
| 2025-02-11 | [Mamba Adaptive Anomaly Transformer with association discrepancy for time series](https://arxiv.org/abs/2502.07858v3) | 2502.07858v3 | 12 |
| 2025-02-11 | [Scaling Online Complex Event Detection with Synthetic Supervision and Mamba-Based Neural Algorithmic Reasoning](https://arxiv.org/abs/2502.07250v3) | 2502.07250v3 | 6 |
| 2025-02-11 | [A Survey on Mamba Architecture for Vision Applications](https://arxiv.org/abs/2502.07161v1) | 2502.07161v1 | 6 |
| 2025-02-10 | [Is Long Range Sequential Modeling Necessary For Colorectal Tumor Segmentation?](https://arxiv.org/abs/2502.07120v1) | 2502.07120v1 | 6 |
| 2025-02-10 | [FinMamba: Market-Aware Graph Enhanced Multi-Level Mamba for Stock Movement Prediction](https://arxiv.org/abs/2502.06707v2) | 2502.06707v2 | 6 |
| 2025-02-10 | [XAMBA: Enabling Efficient State Space Models on Resource-Constrained Neural Processing Units](https://arxiv.org/abs/2502.06924v4) | 2502.06924v4 | 6 |
| 2025-02-10 | [FEMBA: Efficient and Scalable EEG Analysis with a Bidirectional Mamba Foundation Model](https://arxiv.org/abs/2502.06438v2) | 2502.06438v2 | 6 |
| 2025-02-10 | [Hybrid State-Space and GRU-based Graph Tokenization Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2502.06427v1) | 2502.06427v1 | 8 |
| 2025-02-09 | [CacheMamba: Popularity Prediction for Mobile Edge Caching Networks via Selective State Spaces](https://arxiv.org/abs/2502.15746v1) | 2502.15746v1 | 9 |
| 2025-02-07 | [CMamba: Learned Image Compression with State Space Models](https://arxiv.org/abs/2502.04988v1) | 2502.04988v1 | 12 |
| 2025-02-07 | [SSMLoRA: Enhancing Low-Rank Adaptation with State Space Model](https://arxiv.org/abs/2502.04958v1) | 2502.04958v1 | 6 |
| 2025-02-07 | [Before It's Too Late: A State Space Model for the Early Prediction of Misinformation and Disinformation Engagement](https://arxiv.org/abs/2502.04655v1) | 2502.04655v1 | 10 |
| 2025-02-04 | [On the Expressivity of Selective State-Space Layers: A Multivariate Polynomial Approach](https://arxiv.org/abs/2502.02209v1) | 2502.02209v1 | 8 |
| 2025-02-04 | [UD-Mamba: A pixel-level uncertainty-driven Mamba model for medical image segmentation](https://arxiv.org/abs/2502.02024v1) | 2502.02024v1 | 6 |
| 2025-02-04 | [DCT-Mamba3D: Spectral Decorrelation and Spatial-Spectral Feature Extraction for Hyperspectral Image Classification](https://arxiv.org/abs/2502.01986v1) | 2502.01986v1 | 6 |
| 2025-02-03 | [Generalization Error Analysis for Selective State-Space Models Through the Lens of Attention](https://arxiv.org/abs/2502.01473v3) | 2502.01473v3 | 6 |
| 2025-02-03 | [Deep Active Speech Cancellation with Mamba-Masking Network](https://arxiv.org/abs/2502.01185v2) | 2502.01185v2 | 6 |
| 2025-02-03 | [Pushing the Boundaries of State Space Models for Image and Video Generation](https://arxiv.org/abs/2502.00972v1) | 2502.00972v1 | 11 |
| 2025-02-02 | [Parameter Estimation of State Space Models Using Particle Importance Sampling](https://arxiv.org/abs/2502.00904v1) | 2502.00904v1 | 6 |
| 2025-02-01 | [Fast Vision Mamba: Pooling Spatial Dimensions for Accelerated Processing](https://arxiv.org/abs/2502.00594v1) | 2502.00594v1 | 12 |
| 2025-02-01 | [Multilingual State Space Models for Structured Question Answering in Indic Languages](https://arxiv.org/abs/2502.01673v3) | 2502.01673v3 | 6 |
| 2025-02-01 | [EDELINE: Enhancing Memory in Diffusion-based World Models via Linear-Time Sequence Modeling](https://arxiv.org/abs/2502.00466v2) | 2502.00466v2 | 10 |
| 2025-02-01 | [MambaGlue: Fast and Robust Local Feature Matching With Mamba](https://arxiv.org/abs/2502.00462v1) | 2502.00462v1 | 6 |
| 2025-02-01 | [SatMamba: Development of Foundation Models for Remote Sensing Imagery Using State Space Models](https://arxiv.org/abs/2502.00435v1) | 2502.00435v1 | 12 |
| 2025-02-01 | [Sub-Sequential Physics-Informed Learning with State Space Model](https://arxiv.org/abs/2502.00318v2) | 2502.00318v2 | 12 |
| 2025-02-01 | [A Study on the Performance of U-Net Modifications in Retroperitoneal Tumor Segmentation](https://arxiv.org/abs/2502.00314v1) | 2502.00314v1 | 8 |
| 2025-01-30 | [HSRMamba: Contextual Spatial-Spectral State Space Model for Single Image Hyperspectral Super-Resolution](https://arxiv.org/abs/2501.18500v2) | 2501.18500v2 | 12 |
| 2025-01-30 | [MatIR: A Hybrid Mamba-Transformer Image Restoration Model](https://arxiv.org/abs/2501.18401v2) | 2501.18401v2 | 6 |
| 2025-01-28 | [Mamba-Shedder: Post-Transformer Compression for Efficient Selective Structured State Space Models](https://arxiv.org/abs/2501.17088v1) | 2501.17088v1 | 14 |
| 2025-01-28 | [Post-Training Quantization for Vision Mamba with k-Scaled Quantization and Reparameterization](https://arxiv.org/abs/2501.16738v2) | 2501.16738v2 | 6 |
| 2025-01-27 | [Directing Mamba to Complex Textures: An Efficient Texture-Aware State Space Model for Image Restoration](https://arxiv.org/abs/2501.16583v2) | 2501.16583v2 | 12 |
| 2025-01-27 | [Mixture-of-Mamba: Enhancing Multi-Modal State-Space Models with Modality-Aware Sparsity](https://arxiv.org/abs/2501.16295v1) | 2501.16295v1 | 10 |
| 2025-01-27 | [Application of Structured State Space Models to High energy physics with locality-sensitive hashing](https://arxiv.org/abs/2501.16237v1) | 2501.16237v1 | 10 |
| 2025-01-26 | [Mamba-Based Graph Convolutional Networks: Tackling Over-smoothing with Selective State Space](https://arxiv.org/abs/2501.15461v4) | 2501.15461v4 | 11 |
| 2025-01-26 | [CD-Lamba: Boosting Remote Sensing Change Detection via a Cross-Temporal Locally Adaptive State Space Model](https://arxiv.org/abs/2501.15455v1) | 2501.15455v1 | 10 |
| 2025-01-25 | [MambaTron: Efficient Cross-Modal Point Cloud Enhancement using Aggregate Selective State Space Modeling](https://arxiv.org/abs/2501.16384v1) | 2501.16384v1 | 15 |
| 2025-01-24 | [A Deep State Space Model for Rainfall-Runoff Simulations](https://arxiv.org/abs/2501.14980v1) | 2501.14980v1 | 6 |
| 2025-01-24 | [Surface Vision Mamba: Leveraging Bidirectional State Space Model for Efficient Spherical Manifold Representation](https://arxiv.org/abs/2501.14679v5) | 2501.14679v5 | 12 |
| 2025-01-24 | [State Space Models for Extractive Summarization in Low Resource Scenarios](https://arxiv.org/abs/2501.14673v1) | 2501.14673v1 | 10 |
| 2025-01-23 | [MV-GMN: State Space Model for Multi-View Action Recognition](https://arxiv.org/abs/2501.13829v1) | 2501.13829v1 | 10 |
| 2025-01-23 | [QMamba: Post-Training Quantization for Vision State Space Models](https://arxiv.org/abs/2501.13624v1) | 2501.13624v1 | 14 |
| 2025-01-23 | [MambaQuant: Quantizing the Mamba Family with Variance Aligned Rotation Methods](https://arxiv.org/abs/2501.13484v3) | 2501.13484v3 | 6 |
| 2025-01-23 | [Contrast: A Hybrid Architecture of Transformers and State Space Models for Low-Level Vision](https://arxiv.org/abs/2501.13353v2) | 2501.13353v2 | 16 |
| 2025-01-22 | [LiT: Delving into a Simple Linear Diffusion Transformer for Image Generation](https://arxiv.org/abs/2501.12976v2) | 2501.12976v2 | 6 |
| 2025-01-21 | [Parallel Sequence Modeling via Generalized Spatial Propagation Network](https://arxiv.org/abs/2501.12381v1) | 2501.12381v1 | 9 |
| 2025-01-21 | [Test-time regression: a unifying framework for designing sequence models with associative memory](https://arxiv.org/abs/2501.12352v3) | 2501.12352v3 | 6 |
| 2025-01-21 | [SMamba: Sparse Mamba for Event-based Object Detection](https://arxiv.org/abs/2501.11971v1) | 2501.11971v1 | 6 |
| 2025-01-21 | [GLAM: Global-Local Variation Awareness in Mamba-based World Model](https://arxiv.org/abs/2501.11949v1) | 2501.11949v1 | 6 |
| 2025-01-20 | [SeRpEnt: Selective Resampling for Expressive State Space Models](https://arxiv.org/abs/2501.11729v1) | 2501.11729v1 | 12 |
| 2025-01-16 | [WMamba: Wavelet-based Mamba for Face Forgery Detection](https://arxiv.org/abs/2501.09617v2) | 2501.09617v2 | 6 |
| 2025-01-15 | [MANTA: Diffusion Mamba for Efficient and Effective Stochastic Long-Term Dense Anticipation](https://arxiv.org/abs/2501.08837v2) | 2501.08837v2 | 6 |
| 2025-01-14 | [DH-Mamba: Exploring Dual-domain Hierarchical State Space Models for MRI Reconstruction](https://arxiv.org/abs/2501.08163v3) | 2501.08163v3 | 14 |
| 2025-01-14 | [AVS-Mamba: Exploring Temporal and Multi-modal Mamba for Audio-Visual Segmentation](https://arxiv.org/abs/2501.07810v1) | 2501.07810v1 | 12 |
| 2025-01-13 | [Skip Mamba Diffusion for Monocular 3D Semantic Scene Completion](https://arxiv.org/abs/2501.07260v1) | 2501.07260v1 | 6 |
| 2025-01-13 | [MSV-Mamba: A Multiscale Vision Mamba Network for Echocardiography Segmentation](https://arxiv.org/abs/2501.07120v1) | 2501.07120v1 | 6 |
| 2025-01-12 | [Mamba-MOC: A Multicategory Remote Object Counting via State Space Model](https://arxiv.org/abs/2501.06697v2) | 2501.06697v2 | 12 |
| 2025-01-10 | [MS-Temba: Multi-Scale Temporal Mamba for Understanding Long Untrimmed Videos](https://arxiv.org/abs/2501.06138v3) | 2501.06138v3 | 6 |
| 2025-01-10 | [Element-wise Attention Is All You Need](https://arxiv.org/abs/2501.05730v1) | 2501.05730v1 | 8 |
| 2025-01-09 | [MambaHSI: Spatial-Spectral Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2501.04944v1) | 2501.04944v1 | 6 |
| 2025-01-08 | [EDMB: Edge Detector with Mamba](https://arxiv.org/abs/2501.04846v1) | 2501.04846v1 | 6 |
| 2025-01-08 | [H-MBA: Hierarchical MamBa Adaptation for Multi-Modal Video Understanding in Autonomous Driving](https://arxiv.org/abs/2501.04302v1) | 2501.04302v1 | 10 |
| 2025-01-06 | [GLFC: Unified Global-Local Feature and Contrast Learning with Mamba-Enhanced UNet for Synthetic CT Generation from CBCT](https://arxiv.org/abs/2501.02992v2) | 2501.02992v2 | 6 |
| 2025-01-06 | [Samba-ASR: State-Of-The-Art Speech Recognition Leveraging Structured State-Space Models](https://arxiv.org/abs/2501.02832v3) | 2501.02832v3 | 8 |
| 2025-01-05 | [KM-UNet KAN Mamba UNet for medical image segmentation](https://arxiv.org/abs/2501.02559v1) | 2501.02559v1 | 6 |
| 2025-01-03 | [A Separable Self-attention Inspired by the State Space Model for Computer Vision](https://arxiv.org/abs/2501.02040v2) | 2501.02040v2 | 10 |
| 2025-01-03 | [SSM2Mel: State Space Model to Reconstruct Mel Spectrogram from the EEG](https://arxiv.org/abs/2501.10402v1) | 2501.10402v1 | 10 |
| 2025-01-03 | [Look Back for More: Harnessing Historical Sequential Updates for Personalized Federated Adapter Tuning](https://arxiv.org/abs/2501.01653v1) | 2501.01653v1 | 6 |
| 2025-01-03 | [Merging Context Clustering with Visual State Space Models for Medical Image Segmentation](https://arxiv.org/abs/2501.01618v1) | 2501.01618v1 | 10 |
| 2025-01-02 | [Detail Matters: Mamba-Inspired Joint Unfolding Network for Snapshot Spectral Compressive Imaging](https://arxiv.org/abs/2501.01262v1) | 2501.01262v1 | 12 |
| 2025-01-02 | [CryptoMamba: Leveraging State Space Models for Accurate Bitcoin Price Prediction](https://arxiv.org/abs/2501.01010v2) | 2501.01010v2 | 14 |
| 2025-01-01 | [HCMA-UNet: A Hybrid CNN-Mamba UNet with Axial Self-Attention for Efficient Breast Cancer Segmentation](https://arxiv.org/abs/2501.00751v2) | 2501.00751v2 | 6 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-31 | [Understanding and Mitigating Bottlenecks of State Space Models through the Lens of Recency and Over-smoothing](https://arxiv.org/abs/2501.00658v2) | 2501.00658v2 | 6 |
| 2024-12-31 | [GDSR: Global-Detail Integration through Dual-Branch Network with Wavelet Losses for Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2501.01460v4) | 2501.01460v4 | 8 |
| 2024-12-29 | [PTQ4VM: Post-Training Quantization for Visual Mamba](https://arxiv.org/abs/2412.20386v2) | 2412.20386v2 | 6 |
| 2024-12-28 | [STNMamba: Mamba-based Spatial-Temporal Normality Learning for Video Anomaly Detection](https://arxiv.org/abs/2412.20084v1) | 2412.20084v1 | 6 |
| 2024-12-28 | [MambaVO: Deep Visual Odometry Based on Sequential Matching Refinement and Training Smoothing](https://arxiv.org/abs/2412.20082v2) | 2412.20082v2 | 6 |
| 2024-12-28 | [MaIR: A Locality- and Continuity-Preserving Mamba for Image Restoration](https://arxiv.org/abs/2412.20066v2) | 2412.20066v2 | 6 |
| 2024-12-28 | [DepthMamba with Adaptive Fusion](https://arxiv.org/abs/2412.19964v1) | 2412.19964v1 | 6 |
| 2024-12-26 | [BSDB-Net: Band-Split Dual-Branch Network with Selective State Spaces Mechanism for Monaural Speech Enhancement](https://arxiv.org/abs/2412.19099v1) | 2412.19099v1 | 7 |
| 2024-12-24 | [Exploring Graph Mamba: A Comprehensive Survey on State-Space Models for Graph Learning](https://arxiv.org/abs/2412.18322v1) | 2412.18322v1 | 6 |
| 2024-12-24 | [U-Mamba-Net: A highly efficient Mamba-based U-net style network for noisy and reverberant speech separation](https://arxiv.org/abs/2412.18217v1) | 2412.18217v1 | 6 |
| 2024-12-24 | [Enhancing Online Continual Learning with Plug-and-Play State Space Model and Class-Conditional Mixture of Discretization](https://arxiv.org/abs/2412.18177v1) | 2412.18177v1 | 8 |
| 2024-12-24 | [COMO: Cross-Mamba Interaction and Offset-Guided Fusion for Multimodal Object Detection](https://arxiv.org/abs/2412.18076v1) | 2412.18076v1 | 6 |
| 2024-12-23 | [FlowMamba: Learning Point Cloud Scene Flow with Global Motion Propagation](https://arxiv.org/abs/2412.17366v1) | 2412.17366v1 | 10 |
| 2024-12-23 | [Brain-to-Text Benchmark '24: Lessons Learned](https://arxiv.org/abs/2412.17227v1) | 2412.17227v1 | 6 |
| 2024-12-21 | [From Pixels to Gigapixels: Bridging Local Inductive Bias and Long-Range Dependencies with Pixel-Mamba](https://arxiv.org/abs/2412.16711v1) | 2412.16711v1 | 6 |
| 2024-12-21 | [Mamba-SEUNet: Mamba UNet for Monaural Speech Enhancement](https://arxiv.org/abs/2412.16626v2) | 2412.16626v2 | 6 |
| 2024-12-21 | [V"Mean"ba: Visual State Space Models only need 1 hidden dimension](https://arxiv.org/abs/2412.16602v1) | 2412.16602v1 | 8 |
| 2024-12-21 | [Trusted Mamba Contrastive Network for Multi-View Clustering](https://arxiv.org/abs/2412.16487v2) | 2412.16487v2 | 6 |
| 2024-12-21 | [MOL-Mamba: Enhancing Molecular Representation with Structural & Electronic Insights](https://arxiv.org/abs/2412.16483v2) | 2412.16483v2 | 6 |
| 2024-12-20 | [Mamba2D: A Natively Multi-Dimensional State-Space Model for Vision Tasks](https://arxiv.org/abs/2412.16146v4) | 2412.16146v4 | 6 |
| 2024-12-20 | [BabyHGRN: Exploring RNNs for Sample-Efficient Training of Language Models](https://arxiv.org/abs/2412.15978v1) | 2412.15978v1 | 6 |
| 2024-12-20 | [Mamba-based Deep Learning Approach for Sleep Staging on a Wireless Multimodal Wearable System without Electroencephalography](https://arxiv.org/abs/2412.15947v4) | 2412.15947v4 | 8 |
| 2024-12-20 | [Multi-dimensional Visual Prompt Enhanced Image Restoration via Mamba-Transformer Aggregation](https://arxiv.org/abs/2412.15845v1) | 2412.15845v1 | 6 |
| 2024-12-19 | [{S$^3$-Mamba}: Small-Size-Sensitive Mamba for Lesion Segmentation](https://arxiv.org/abs/2412.14546v1) | 2412.14546v1 | 6 |
| 2024-12-19 | [Efficient Self-Supervised Video Hashing with Selective State Spaces](https://arxiv.org/abs/2412.14518v1) | 2412.14518v1 | 7 |
| 2024-12-18 | [MambaLCT: Boosting Tracking via Long-term Context State Space Model](https://arxiv.org/abs/2412.13615v1) | 2412.13615v1 | 12 |
| 2024-12-18 | [Robust Tracking via Mamba-based Context-aware Token Learning](https://arxiv.org/abs/2412.13611v1) | 2412.13611v1 | 6 |
| 2024-12-18 | [Hybrid CNN-LSTM based Indoor Pedestrian Localization with CSI Fingerprint Maps](https://arxiv.org/abs/2412.13601v2) | 2412.13601v2 | 6 |
| 2024-12-17 | [Expansion Span: Combining Fading Memory and Retrieval in Hybrid State Space Models](https://arxiv.org/abs/2412.13328v2) | 2412.13328v2 | 10 |
| 2024-12-17 | [TAME: Temporal Audio-based Mamba for Enhanced Drone Trajectory Estimation and Classification](https://arxiv.org/abs/2412.13037v7) | 2412.13037v7 | 6 |
| 2024-12-17 | [Faster Vision Mamba is Rebuilt in Minutes via Merged Token Re-training](https://arxiv.org/abs/2412.12496v4) | 2412.12496v4 | 6 |
| 2024-12-17 | [GG-SSMs: Graph-Generating State Space Models](https://arxiv.org/abs/2412.12423v2) | 2412.12423v2 | 10 |
| 2024-12-16 | [SegMAN: Omni-scale Context Modeling with State Space Models and Local Attention for Semantic Segmentation](https://arxiv.org/abs/2412.11890v2) | 2412.11890v2 | 11 |
| 2024-12-15 | [A Comparative Study on Dynamic Graph Embedding based on Mamba and Transformers](https://arxiv.org/abs/2412.11293v2) | 2412.11293v2 | 6 |
| 2024-12-15 | [Image Forgery Localization with State Space Models](https://arxiv.org/abs/2412.11214v2) | 2412.11214v2 | 10 |
| 2024-12-15 | [Deep Learning-based Approaches for State Space Models: A Selective Review](https://arxiv.org/abs/2412.11211v1) | 2412.11211v1 | 8 |
| 2024-12-15 | [BarcodeMamba: State Space Models for Biodiversity Analysis](https://arxiv.org/abs/2412.11084v1) | 2412.11084v1 | 15 |
| 2024-12-14 | [MASV: Speaker Verification with Global and Local Context Mamba](https://arxiv.org/abs/2412.10989v1) | 2412.10989v1 | 6 |
| 2024-12-14 | [MambaPro: Multi-Modal Object Re-Identification with Mamba Aggregation and Synergistic Prompt](https://arxiv.org/abs/2412.10707v1) | 2412.10707v1 | 6 |
| 2024-12-14 | [A Multiprocess State Space Model with Feedback and Switching for Patterns of Clinical Measurements Associated with COVID-19](https://arxiv.org/abs/2412.10639v1) | 2412.10639v1 | 6 |
| 2024-12-13 | [XYScanNet: A State Space Model for Single Image Deblurring](https://arxiv.org/abs/2412.10338v4) | 2412.10338v4 | 10 |
| 2024-12-13 | [Selective State Space Memory for Large Vision-Language Models](https://arxiv.org/abs/2412.09875v1) | 2412.09875v1 | 7 |
| 2024-12-12 | [Physics-Driven Autoregressive State Space Models for Medical Image Reconstruction](https://arxiv.org/abs/2412.09331v3) | 2412.09331v3 | 10 |
| 2024-12-12 | [Optimising TinyML with Quantization and Distillation of Transformer and Mamba Models for Indoor Localisation on Edge Devices](https://arxiv.org/abs/2412.09289v1) | 2412.09289v1 | 6 |
| 2024-12-12 | [Selective Visual Prompting in Vision Mamba](https://arxiv.org/abs/2412.08947v1) | 2412.08947v1 | 12 |
| 2024-12-11 | [Numerical Analysis of HiPPO-LegS ODE for Deep State Space Models](https://arxiv.org/abs/2412.08595v2) | 2412.08595v2 | 6 |
| 2024-12-11 | [SAM-Mamba: Mamba Guided SAM Architecture for Generalized Zero-Shot Polyp Segmentation](https://arxiv.org/abs/2412.08482v1) | 2412.08482v1 | 6 |
| 2024-12-11 | [LOMA: Language-assisted Semantic Occupancy Network via Triplane Mamba](https://arxiv.org/abs/2412.08388v1) | 2412.08388v1 | 6 |
| 2024-12-11 | [DG-Mamba: Robust and Efficient Dynamic Graph Structure Learning with Selective State Space Models](https://arxiv.org/abs/2412.08160v4) | 2412.08160v4 | 15 |
| 2024-12-10 | [Manta: Enhancing Mamba for Few-Shot Action Recognition of Long Sub-Sequence](https://arxiv.org/abs/2412.07481v7) | 2412.07481v7 | 6 |
| 2024-12-10 | [Bidirectional Mamba state-space model for anomalous diffusion](https://arxiv.org/abs/2412.07299v1) | 2412.07299v1 | 6 |
| 2024-12-10 | [MPSI: Mamba enhancement model for pixel-wise sequential interaction Image Super-Resolution](https://arxiv.org/abs/2412.07222v1) | 2412.07222v1 | 6 |
| 2024-12-09 | [MSCrackMamba: Leveraging Vision Mamba for Crack Detection in Fused Multispectral Imagery](https://arxiv.org/abs/2412.06211v1) | 2412.06211v1 | 6 |
| 2024-12-09 | [The Computational Limits of State-Space Models and Mamba via the Lens of Circuit Complexity](https://arxiv.org/abs/2412.06148v2) | 2412.06148v2 | 6 |
| 2024-12-09 | [PowerMamba: A Deep State Space Model and Comprehensive Benchmark for Time Series Prediction in Electric Power Systems](https://arxiv.org/abs/2412.06112v2) | 2412.06112v2 | 12 |
| 2024-12-06 | [MSECG: Incorporating Mamba for Robust and Efficient ECG Super-Resolution](https://arxiv.org/abs/2412.04861v1) | 2412.04861v1 | 8 |
| 2024-12-03 | [Segmentation of Coronary Artery Stenosis in X-ray Angiography using Mamba Models](https://arxiv.org/abs/2412.02568v1) | 2412.02568v1 | 6 |
| 2024-12-02 | [MamKPD: A Simple Mamba Baseline for Real-Time 2D Keypoint Detection](https://arxiv.org/abs/2412.01422v1) | 2412.01422v1 | 6 |
| 2024-12-02 | [MambaU-Lite: A Lightweight Model based on Mamba and Integrated Channel-Spatial Attention for Skin Lesion Segmentation](https://arxiv.org/abs/2412.01405v1) | 2412.01405v1 | 6 |
| 2024-12-01 | [AlignMamba: Enhancing Multimodal Mamba with Local and Global Cross-modal Alignment](https://arxiv.org/abs/2412.00833v1) | 2412.00833v1 | 6 |
| 2024-12-01 | [Learning Mamba as a Continual Learner: Meta-Learning Selective State Space Models for Continual Learning](https://arxiv.org/abs/2412.00776v5) | 2412.00776v5 | 15 |
| 2024-12-01 | [Decision Transformer vs. Decision Mamba: Analysing the Complexity of Sequential Decision Making in Atari Games](https://arxiv.org/abs/2412.00725v1) | 2412.00725v1 | 6 |
| 2024-12-01 | [2DMamba: Efficient State Space Model for Image Representation with Applications on Giga-Pixel Whole Slide Image Classification](https://arxiv.org/abs/2412.00678v3) | 2412.00678v3 | 14 |
| 2024-12-01 | [MambaNUT: Nighttime UAV Tracking via Mamba-based Adaptive Curriculum Learning](https://arxiv.org/abs/2412.00626v3) | 2412.00626v3 | 10 |
| 2024-11-29 | [SkelMamba: A State Space Model for Efficient Skeleton Action Recognition of Neurological Disorders](https://arxiv.org/abs/2411.19544v1) | 2411.19544v1 | 12 |
| 2024-11-29 | [Look Every Frame All at Once: Video-Ma$^2$mba for Efficient Long-form Video Understanding with Multi-Axis Gradient Checkpointing](https://arxiv.org/abs/2411.19460v1) | 2411.19460v1 | 8 |
| 2024-11-29 | [Autocorrelation Matters: Understanding the Role of Initialization Schemes for State Space Models](https://arxiv.org/abs/2411.19455v1) | 2411.19455v1 | 6 |
| 2024-11-28 | [Marconi: Prefix Caching for the Era of Hybrid LLMs](https://arxiv.org/abs/2411.19379v3) | 2411.19379v3 | 6 |
| 2024-11-28 | [MSEMG: Surface Electromyography Denoising with a Mamba-based Efficient Network](https://arxiv.org/abs/2411.18902v2) | 2411.18902v2 | 10 |
| 2024-11-27 | [Vision Mamba Distillation for Low-resolution Fine-grained Image Classification](https://arxiv.org/abs/2411.17980v1) | 2411.17980v1 | 6 |
| 2024-11-26 | [An Ensemble Approach for Brain Tumor Segmentation and Synthesis](https://arxiv.org/abs/2411.17617v1) | 2411.17617v1 | 8 |
| 2024-11-26 | [FTMoMamba: Motion Generation with Frequency and Text State Space Models](https://arxiv.org/abs/2411.17532v1) | 2411.17532v1 | 12 |
| 2024-11-26 | [TinyViM: Frequency Decoupling for Tiny Hybrid Vision Mamba](https://arxiv.org/abs/2411.17473v2) | 2411.17473v2 | 10 |
| 2024-11-26 | [BadScan: An Architectural Backdoor Attack on Visual State Space Models](https://arxiv.org/abs/2411.17283v1) | 2411.17283v1 | 10 |
| 2024-11-25 | [Deformable Mamba for Wide Field of View Segmentation](https://arxiv.org/abs/2411.16481v2) | 2411.16481v2 | 6 |
| 2024-11-25 | [M3: Mamba-assisted Multi-Circuit Optimization via MBRL with Effective Scheduling](https://arxiv.org/abs/2411.16019v1) | 2411.16019v1 | 6 |
| 2024-11-24 | [MobileMamba: Lightweight Multi-Receptive Visual Mamba Network](https://arxiv.org/abs/2411.15941v1) | 2411.15941v1 | 6 |
| 2024-11-24 | [MambaTrack: Exploiting Dual-Enhancement for Night UAV Tracking](https://arxiv.org/abs/2411.15761v2) | 2411.15761v2 | 6 |
| 2024-11-23 | [Best of Both Worlds: Advantages of Hybrid Graph Sequence Models](https://arxiv.org/abs/2411.15671v1) | 2411.15671v1 | 6 |
| 2024-11-23 | [Mamba-CL: Optimizing Selective State Space Model in Null Space for Continual Learning](https://arxiv.org/abs/2411.15469v3) | 2411.15469v3 | 17 |
| 2024-11-23 | [MambaVLT: Time-Evolving Multimodal State Space Model for Vision-Language Tracking](https://arxiv.org/abs/2411.15459v1) | 2411.15459v1 | 14 |
| 2024-11-22 | [Event USKT : U-State Space Model in Knowledge Transfer for Event Cameras](https://arxiv.org/abs/2411.15276v1) | 2411.15276v1 | 6 |
| 2024-11-22 | [MambaIRv2: Attentive State Space Restoration](https://arxiv.org/abs/2411.15269v2) | 2411.15269v2 | 6 |
| 2024-11-22 | [OSMamba: Omnidirectional Spectral Mamba with Dual-Domain Prior Generator for Exposure Correction](https://arxiv.org/abs/2411.15255v2) | 2411.15255v2 | 10 |
| 2024-11-22 | [Fast convolution algorithm for state space models](https://arxiv.org/abs/2411.17729v3) | 2411.17729v3 | 6 |
| 2024-11-22 | [Recursive Gaussian Process State Space Model](https://arxiv.org/abs/2411.14679v4) | 2411.14679v4 | 6 |
| 2024-11-22 | [EfficientViM: Efficient Vision Mamba with Hidden State Mixer based State Space Duality](https://arxiv.org/abs/2411.15241v2) | 2411.15241v2 | 10 |
| 2024-11-21 | [BEST-STD: Bidirectional Mamba-Enhanced Speech Tokenization for Spoken Term Detection](https://arxiv.org/abs/2411.14100v2) | 2411.14100v2 | 10 |
| 2024-11-21 | [Parameter Efficient Mamba Tuning via Projector-targeted Diagonal-centric Linear Transformation](https://arxiv.org/abs/2411.15224v3) | 2411.15224v3 | 6 |
| 2024-11-19 | [Unlocking State-Tracking in Linear RNNs Through Negative Eigenvalues](https://arxiv.org/abs/2411.12537v5) | 2411.12537v5 | 10 |
| 2024-11-19 | [Contrast Similarity-Aware Dual-Pathway Mamba for Multivariate Time Series Node Classification](https://arxiv.org/abs/2411.12222v2) | 2411.12222v2 | 6 |
| 2024-11-18 | [Bi-Mamba: Towards Accurate 1-Bit State Space Models](https://arxiv.org/abs/2411.11843v2) | 2411.11843v2 | 12 |
| 2024-11-18 | [RAWMamba: Unified sRGB-to-RAW De-rendering With State Space Model](https://arxiv.org/abs/2411.11717v1) | 2411.11717v1 | 12 |
| 2024-11-18 | [KAN-Mamba FusionNet: Redefining Medical Image Segmentation with Non-Linear Modeling](https://arxiv.org/abs/2411.11926v2) | 2411.11926v2 | 6 |
| 2024-11-16 | [$\text{S}^{3}$Mamba: Arbitrary-Scale Super-Resolution via Scaleable State Space Model](https://arxiv.org/abs/2411.11906v1) | 2411.11906v1 | 12 |
| 2024-11-16 | [MetaLA: Unified Optimal Linear Approximation to Softmax Attention Map](https://arxiv.org/abs/2411.10741v1) | 2411.10741v1 | 6 |
| 2024-11-15 | [XLSR-Mamba: A Dual-Column Bidirectional State Space Model for Spoofing Attack Detection](https://arxiv.org/abs/2411.10027v2) | 2411.10027v2 | 14 |
| 2024-11-13 | [Multimodal Instruction Tuning with Hybrid State Space Models](https://arxiv.org/abs/2411.08840v1) | 2411.08840v1 | 10 |
| 2024-11-13 | [MambaXCTrack: Mamba-based Tracker with SSM Cross-correlation and Motion Prompt for Ultrasound Needle Tracking](https://arxiv.org/abs/2411.08395v2) | 2411.08395v2 | 10 |
| 2024-11-12 | [CT-Mamba: A Hybrid Convolutional State Space Model for Low-Dose CT Denoising](https://arxiv.org/abs/2411.07930v5) | 2411.07930v5 | 12 |
| 2024-11-12 | [SAV-SE: Scene-aware Audio-Visual Speech Enhancement with Selective State Space Model](https://arxiv.org/abs/2411.07751v2) | 2411.07751v2 | 13 |
| 2024-11-11 | [AEROMamba: An efficient architecture for audio super-resolution using generative adversarial networks and state space models](https://arxiv.org/abs/2411.07364v1) | 2411.07364v1 | 14 |
| 2024-11-11 | [Mamba-based Decoder-Only Approach with Bidirectional Speech Modeling for Speech Recognition](https://arxiv.org/abs/2411.06968v1) | 2411.06968v1 | 12 |
| 2024-11-11 | [Correction to: Multivariate CARMA processes, continuous-time state space models and complete regularity of the innovations of the sampled processes, Bernoulli 18, pp. 46-63, 2012](https://arxiv.org/abs/2411.06935v1) | 2411.06935v1 | 6 |
| 2024-11-11 | [LFSamba: Marry SAM with Mamba for Light Field Salient Object Detection](https://arxiv.org/abs/2411.06652v1) | 2411.06652v1 | 6 |
| 2024-11-10 | [KMM: Key Frame Mask Mamba for Extended Motion Generation](https://arxiv.org/abs/2411.06481v2) | 2411.06481v2 | 6 |
| 2024-11-10 | [SEM-Net: Efficient Pixel Modelling for image inpainting with Spatially Enhanced SSM](https://arxiv.org/abs/2411.06318v1) | 2411.06318v1 | 8 |
| 2024-11-09 | [Selective State Space Model for Monaural Speech Enhancement](https://arxiv.org/abs/2411.06217v1) | 2411.06217v1 | 13 |
| 2024-11-06 | [DiMSUM: Diffusion Mamba -- A Scalable and Unified Spatial-Frequency Method for Image Generation](https://arxiv.org/abs/2411.04168v4) | 2411.04168v4 | 8 |
| 2024-11-06 | [Can Custom Models Learn In-Context? An Exploration of Hybrid Architecture Performance on In-Context Learning Tasks](https://arxiv.org/abs/2411.03945v1) | 2411.03945v1 | 10 |
| 2024-11-06 | [MambaPEFT: Exploring Parameter-Efficient Fine-Tuning for Mamba](https://arxiv.org/abs/2411.03855v3) | 2411.03855v3 | 10 |
| 2024-11-06 | [MetaSSC: Enhancing 3D Semantic Scene Completion for Autonomous Driving through Meta-Learning and Long-sequence Modeling](https://arxiv.org/abs/2411.03672v2) | 2411.03672v2 | 7 |
| 2024-11-05 | [ShadowMamba: State-Space Model with Boundary-Region Selective Scan for Shadow Removal](https://arxiv.org/abs/2411.03260v4) | 2411.03260v4 | 6 |
| 2024-11-05 | [A Mamba Foundation Model for Time Series Forecasting](https://arxiv.org/abs/2411.02941v1) | 2411.02941v1 | 6 |
| 2024-11-05 | [Layer-Adaptive State Pruning for Deep State Space Models](https://arxiv.org/abs/2411.02824v3) | 2411.02824v3 | 6 |
| 2024-11-05 | [The Evolution of RWKV: Advancements in Efficient Language Modeling](https://arxiv.org/abs/2411.02795v1) | 2411.02795v1 | 8 |
| 2024-11-04 | [Modulating State Space Model with SlowFast Framework for Compute-Efficient Ultra Low-Latency Speech Enhancement](https://arxiv.org/abs/2411.02019v2) | 2411.02019v2 | 6 |
| 2024-11-04 | [LE-PDE++: Mamba for accelerating PDEs Simulations](https://arxiv.org/abs/2411.01897v2) | 2411.01897v2 | 6 |
| 2024-11-03 | [Optical Flow Representation Alignment Mamba Diffusion Model for Medical Video Generation](https://arxiv.org/abs/2411.01647v1) | 2411.01647v1 | 6 |
| 2024-11-03 | [BiT-MamSleep: Bidirectional Temporal Mamba for EEG Sleep Staging](https://arxiv.org/abs/2411.01589v2) | 2411.01589v2 | 6 |
| 2024-11-03 | [MambaReg: Mamba-Based Disentangled Convolutional Sparse Coding for Unsupervised Deformable Multi-Modal Image Registration](https://arxiv.org/abs/2411.01399v1) | 2411.01399v1 | 6 |
| 2024-10-31 | [SambaMixer: State of Health Prediction of Li-ion Batteries using Mamba State Space Models](https://arxiv.org/abs/2411.00233v1) | 2411.00233v1 | 12 |
| 2024-10-31 | [NIMBA: Towards Robust and Principled Processing of Point Clouds With SSMs](https://arxiv.org/abs/2411.00151v1) | 2411.00151v1 | 10 |
| 2024-10-30 | [Sequential Order-Robust Mamba for Time Series Forecasting](https://arxiv.org/abs/2410.23356v1) | 2410.23356v1 | 6 |
| 2024-10-30 | [Adaptive Multi Scale Document Binarisation Using Vision Mamba](https://arxiv.org/abs/2410.22811v1) | 2410.22811v1 | 6 |
| 2024-10-30 | [Unfolding Target Detection with State Space Model](https://arxiv.org/abs/2410.22774v1) | 2410.22774v1 | 6 |
| 2024-10-29 | [A Large Recurrent Action Model: xLSTM enables Fast Inference for Robotics Tasks](https://arxiv.org/abs/2410.22391v3) | 2410.22391v3 | 10 |
| 2024-10-29 | [Long-context Protein Language Modeling Using Bidirectional Mamba with Shared Projection Layers](https://arxiv.org/abs/2411.08909v3) | 2411.08909v3 | 10 |
| 2024-10-29 | [Advancing Efficient Brain Tumor Multi-Class Classification -- New Insights from the Vision Mamba Model in Transfer Learning](https://arxiv.org/abs/2410.21872v2) | 2410.21872v2 | 6 |
| 2024-10-28 | [ECMamba: Consolidating Selective State Space Model with Retinex Guidance for Efficient Multiple Exposure Correction](https://arxiv.org/abs/2410.21535v1) | 2410.21535v1 | 17 |
| 2024-10-28 | [VISTA-SSM: Varying and Irregular Sampling Time-series Analysis via State Space Models](https://arxiv.org/abs/2410.21527v3) | 2410.21527v3 | 6 |
| 2024-10-28 | [SepMamba: State-space models for speaker separation using Mamba](https://arxiv.org/abs/2410.20997v1) | 2410.20997v1 | 6 |
| 2024-10-28 | [FACTS: A Factored State-Space Framework For World Modelling](https://arxiv.org/abs/2410.20922v2) | 2410.20922v2 | 6 |
| 2024-10-27 | [ThunderKittens: Simple, Fast, and Adorable AI Kernels](https://arxiv.org/abs/2410.20399v1) | 2410.20399v1 | 6 |
| 2024-10-27 | [Wavelet-based Mamba with Fourier Adjustment for Low-light Image Enhancement](https://arxiv.org/abs/2410.20314v1) | 2410.20314v1 | 6 |
| 2024-10-25 | [Topology-aware Mamba for Crack Segmentation in Structures](https://arxiv.org/abs/2410.19894v1) | 2410.19894v1 | 6 |
| 2024-10-25 | [Utilizing Image Transforms and Diffusion Models for Generative Modeling of Short and Long Time Series](https://arxiv.org/abs/2410.19538v1) | 2410.19538v1 | 6 |
| 2024-10-25 | [MambaCPU: Enhanced Correlation Mining with State Space Models for CPU Performance Prediction](https://arxiv.org/abs/2410.19297v2) | 2410.19297v2 | 12 |
| 2024-10-24 | [Bio2Token: All-atom tokenization of any biomolecular structure with Mamba](https://arxiv.org/abs/2410.19110v3) | 2410.19110v3 | 10 |
| 2024-10-24 | [Taipan: Efficient and Expressive State Space Language Models with Selective Attention](https://arxiv.org/abs/2410.18572v1) | 2410.18572v1 | 12 |
| 2024-10-23 | [Towards Safer Planetary Exploration: A Hybrid Architecture for Terrain Traversability Analysis in Mars Rovers](https://arxiv.org/abs/2410.17738v1) | 2410.17738v1 | 6 |
| 2024-10-22 | [SpikMamba: When SNN meets Mamba in Event-based Human Action Recognition](https://arxiv.org/abs/2410.16746v1) | 2410.16746v1 | 10 |
| 2024-10-21 | [R2Gen-Mamba: A Selective State Space Model for Radiology Report Generation](https://arxiv.org/abs/2410.18135v1) | 2410.18135v1 | 15 |
| 2024-10-21 | [START: A Generalized State Space Model with Saliency-Driven Token-Aware Transformation](https://arxiv.org/abs/2410.16020v2) | 2410.16020v2 | 10 |
| 2024-10-21 | [MBPU: A Plug-and-Play State Space Model for Point Cloud Upsamping with Fast Point Rendering](https://arxiv.org/abs/2410.15941v1) | 2410.15941v1 | 12 |
| 2024-10-21 | [Focus Where It Matters: Graph Selective State Focused Attention Networks](https://arxiv.org/abs/2410.15849v1) | 2410.15849v1 | 6 |
| 2024-10-21 | [Revealing and Mitigating the Local Pattern Shortcuts of Mamba](https://arxiv.org/abs/2410.15678v1) | 2410.15678v1 | 10 |
| 2024-10-20 | [Taming Mambas for Voxel Level 3D Medical Image Segmentation](https://arxiv.org/abs/2410.15496v1) | 2410.15496v1 | 12 |
| 2024-10-19 | [Spatial-Mamba: Effective Visual State Space Models via Structure-aware State Fusion](https://arxiv.org/abs/2410.15091v2) | 2410.15091v2 | 16 |
| 2024-10-19 | [MambaSOD: Dual Mamba-Driven Cross-Modal Fusion Network for RGB-D Salient Object Detection](https://arxiv.org/abs/2410.15015v1) | 2410.15015v1 | 6 |
| 2024-10-18 | [MambaSCI: Efficient Mamba-UNet for Quad-Bayer Patterned Video Snapshot Compressive Imaging](https://arxiv.org/abs/2410.14214v1) | 2410.14214v1 | 6 |
| 2024-10-17 | [Provable Benefits of Complex Parameterizations for Structured State Space Models](https://arxiv.org/abs/2410.14067v2) | 2410.14067v2 | 10 |
| 2024-10-17 | [RemoteDet-Mamba: A Hybrid Mamba-CNN Network for Multi-modal Object Detection in Remote Sensing Images](https://arxiv.org/abs/2410.13532v2) | 2410.13532v2 | 6 |
| 2024-10-17 | [SSD-TS: Exploring the Potential of Linear State Space Models for Diffusion Models in Time Series Imputation](https://arxiv.org/abs/2410.13338v2) | 2410.13338v2 | 12 |
| 2024-10-17 | [Quamba: A Post-Training Quantization Recipe for Selective State Space Models](https://arxiv.org/abs/2410.13229v2) | 2410.13229v2 | 15 |
| 2024-10-16 | [MambaBEV: An EV-based 3D detection model with Mamba2](https://arxiv.org/abs/2410.12673v3) | 2410.12673v3 | 6 |
| 2024-10-16 | [MambaPainter: Neural Stroke-Based Rendering in a Single Step](https://arxiv.org/abs/2410.12524v1) | 2410.12524v1 | 6 |
| 2024-10-16 | [Rethinking Token Reduction for State Space Models](https://arxiv.org/abs/2410.14725v1) | 2410.14725v1 | 10 |
| 2024-10-15 | [A Survey on Deep Tabular Learning](https://arxiv.org/abs/2410.12034v1) | 2410.12034v1 | 8 |
| 2024-10-15 | [UmambaTSF: A U-shaped Multi-Scale Long-Term Time Series Forecasting Method Using Mamba](https://arxiv.org/abs/2410.11278v1) | 2410.11278v1 | 10 |
| 2024-10-14 | [Mimetic Initialization Helps State Space Models Learn to Recall](https://arxiv.org/abs/2410.11135v1) | 2410.11135v1 | 10 |
| 2024-10-14 | [CleanUMamba: A Compact Mamba Network for Speech Denoising using Channel Pruning](https://arxiv.org/abs/2410.11062v2) | 2410.11062v2 | 6 |
| 2024-10-14 | [The Implicit Bias of Structured State Space Models Can Be Poisoned With Clean Labels](https://arxiv.org/abs/2410.10473v5) | 2410.10473v5 | 6 |
| 2024-10-14 | [V2M: Visual 2-Dimensional Mamba for Image Representation Learning](https://arxiv.org/abs/2410.10382v1) | 2410.10382v1 | 10 |
| 2024-10-14 | [GlobalMamba: Global Image Serialization for Vision Mamba](https://arxiv.org/abs/2410.10316v1) | 2410.10316v1 | 6 |
| 2024-10-14 | [Hi-Mamba: Hierarchical Mamba for Efficient Image Super-Resolution](https://arxiv.org/abs/2410.10140v1) | 2410.10140v1 | 10 |
| 2024-10-14 | [Dreaming to Assist: Learning to Align with Human Objectives for Shared Control in High-Speed Racing](https://arxiv.org/abs/2410.10062v1) | 2410.10062v1 | 6 |
| 2024-10-13 | [SlimSeiz: Efficient Channel-Adaptive Seizure Prediction Using a Mamba-Enhanced Network](https://arxiv.org/abs/2410.09998v1) | 2410.09998v1 | 6 |
| 2024-10-12 | [Mamba4Cast: Efficient Zero-Shot Time Series Forecasting with State Space Models](https://arxiv.org/abs/2410.09385v1) | 2410.09385v1 | 12 |
| 2024-10-11 | [Parameter-Efficient Fine-Tuning of State Space Models](https://arxiv.org/abs/2410.09016v3) | 2410.09016v3 | 10 |
| 2024-10-11 | [Drama: Mamba-Enabled Model-Based Reinforcement Learning Is Sample and Parameter Efficient](https://arxiv.org/abs/2410.08893v4) | 2410.08893v4 | 12 |
| 2024-10-10 | [RecurFormer: Not All Transformer Heads Need Self-Attention](https://arxiv.org/abs/2410.12850v1) | 2410.12850v1 | 6 |
| 2024-10-10 | [CountMamba: Exploring Multi-directional Selective State-Space Models for Plant Counting](https://arxiv.org/abs/2410.07528v1) | 2410.07528v1 | 10 |
| 2024-10-09 | [Stuffed Mamba: Oversized States Lead to the Inability to Forget](https://arxiv.org/abs/2410.07145v4) | 2410.07145v4 | 12 |
| 2024-10-09 | [QuadMamba: Learning Quadtree-based Selective Scan for Visual State Space Model](https://arxiv.org/abs/2410.06806v2) | 2410.06806v2 | 12 |
| 2024-10-09 | [MatMamba: A Matryoshka State Space Model](https://arxiv.org/abs/2410.06718v1) | 2410.06718v1 | 12 |
| 2024-10-09 | [Mamba-based Segmentation Model for Speaker Diarization](https://arxiv.org/abs/2410.06459v2) | 2410.06459v2 | 8 |
| 2024-10-08 | [Monocular Visual Place Recognition in LiDAR Maps via Cross-Modal State Space Model and Multi-View Matching](https://arxiv.org/abs/2410.06285v1) | 2410.06285v1 | 10 |
| 2024-10-08 | [DeMo: Decoupling Motion Forecasting into Directional Intentions and Dynamic States](https://arxiv.org/abs/2410.05982v1) | 2410.05982v1 | 6 |
| 2024-10-08 | [EMMA: Empowering Multi-modal Mamba with Structural and Hierarchical Alignment](https://arxiv.org/abs/2410.05938v1) | 2410.05938v1 | 7 |
| 2024-10-08 | [TIMBA: Time series Imputation with Bi-directional Mamba Blocks and Diffusion models](https://arxiv.org/abs/2410.05916v1) | 2410.05916v1 | 8 |
| 2024-10-08 | [Remote Sensing Image Segmentation Using Vision Mamba and Multi-Scale Multi-Frequency Feature Fusion](https://arxiv.org/abs/2410.05624v1) | 2410.05624v1 | 10 |
| 2024-10-07 | [Falcon Mamba: The First Competitive Attention-free 7B Language Model](https://arxiv.org/abs/2410.05355v1) | 2410.05355v1 | 12 |
| 2024-10-07 | [IGroupSS-Mamba: Interval Group Spatial-Spectral Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2410.05100v1) | 2410.05100v1 | 14 |
| 2024-10-07 | [SPikE-SSM: A Sparse, Precise, and Efficient Spiking State Space Model for Long Sequences Learning](https://arxiv.org/abs/2410.17268v1) | 2410.17268v1 | 8 |
| 2024-10-05 | [Fundamental Limitations on Subquadratic Alternatives to Transformers](https://arxiv.org/abs/2410.04271v2) | 2410.04271v2 | 8 |
| 2024-10-05 | [Mamba Capsule Routing Towards Part-Whole Relational Camouflaged Object Detection](https://arxiv.org/abs/2410.03987v1) | 2410.03987v1 | 6 |
| 2024-10-04 | [Oscillatory State-Space Models](https://arxiv.org/abs/2410.03943v3) | 2410.03943v3 | 6 |
| 2024-10-04 | [Crafting Narrative Closures: Zero-Shot Learning with SSM Mamba for Short Story Ending Generation](https://arxiv.org/abs/2410.10848v1) | 2410.10848v1 | 6 |
| 2024-10-04 | [PRF: Parallel Resonate and Fire Neuron for Long Sequence Learning in Spiking Neural Networks](https://arxiv.org/abs/2410.03530v2) | 2410.03530v2 | 6 |
| 2024-10-04 | [HMT-Grasp: A Hybrid Mamba-Transformer Approach for Robot Grasping in Cluttered Environments](https://arxiv.org/abs/2410.03522v2) | 2410.03522v2 | 10 |
| 2024-10-04 | [Exploring the Limitations of Mamba in COPY and CoT Reasoning](https://arxiv.org/abs/2410.03810v3) | 2410.03810v3 | 10 |
| 2024-10-04 | [Demystifying the Token Dynamics of Deep Selective State Space Models](https://arxiv.org/abs/2410.03292v2) | 2410.03292v2 | 13 |
| 2024-10-04 | [Efficient High-Resolution Visual Representation Learning with State Space Model for Human Pose Estimation](https://arxiv.org/abs/2410.03174v2) | 2410.03174v2 | 12 |
| 2024-10-04 | [Mathematical Formalism for Memory Compression in Selective State Space Models](https://arxiv.org/abs/2410.03158v1) | 2410.03158v1 | 11 |
| 2024-10-04 | [Mamba in Vision: A Comprehensive Survey of Techniques and Applications](https://arxiv.org/abs/2410.03105v1) | 2410.03105v1 | 10 |
| 2024-10-03 | [Deconstructing Recurrence, Attention, and Gating: Investigating the transferability of Transformers and Gated Recurrent Neural Networks in forecasting of dynamical systems](https://arxiv.org/abs/2410.02654v1) | 2410.02654v1 | 7 |
| 2024-10-03 | [A Comprehensive Survey of Mamba Architectures for Medical Image Analysis: Classification, Segmentation, Restoration and Beyond](https://arxiv.org/abs/2410.02362v3) | 2410.02362v3 | 10 |
| 2024-10-03 | [TRIS-HAR: Transmissive Reconfigurable Intelligent Surfaces-assisted Cognitive Wireless Human Activity Recognition Using State Space Models](https://arxiv.org/abs/2410.02334v1) | 2410.02334v1 | 10 |
| 2024-10-03 | [Mamba Neural Operator: Who Wins? Transformers vs. State-Space Models for PDEs](https://arxiv.org/abs/2410.02113v3) | 2410.02113v3 | 6 |
| 2024-10-02 | [Tuning Frequency Bias of State Space Models](https://arxiv.org/abs/2410.02035v1) | 2410.02035v1 | 6 |
| 2024-10-01 | [Back to Bayesics: Uncovering Human Mobility Distributions and Anomalies with an Integrated Statistical and Neural Framework](https://arxiv.org/abs/2410.01011v2) | 2410.01011v2 | 6 |
| 2024-10-01 | [MAP: Unleashing Hybrid Mamba-Transformer Vision Backbone's Potential with Masked Autoregressive Pretraining](https://arxiv.org/abs/2410.00871v3) | 2410.00871v3 | 10 |
| 2024-10-01 | [Zero-Shot Text-to-Speech from Continuous Text Streams](https://arxiv.org/abs/2410.00767v1) | 2410.00767v1 | 7 |
| 2024-09-30 | [A SSM is Polymerized from Multivariate Time Series](https://arxiv.org/abs/2409.20310v2) | 2409.20310v2 | 8 |
| 2024-09-30 | [Mamba for Streaming ASR Combined with Unimodal Aggregation](https://arxiv.org/abs/2410.00070v2) | 2410.00070v2 | 10 |
| 2024-09-30 | [MaskMamba: A Hybrid Mamba-Transformer Model for Masked Image Generation](https://arxiv.org/abs/2409.19937v1) | 2409.19937v1 | 6 |
| 2024-09-30 | [SWIM: Short-Window CNN Integrated with Mamba for EEG-Based Auditory Spatial Attention Decoding](https://arxiv.org/abs/2409.19884v2) | 2409.19884v2 | 6 |
| 2024-09-29 | [Hybrid Mamba for Few-Shot Segmentation](https://arxiv.org/abs/2409.19613v1) | 2409.19613v1 | 6 |
| 2024-09-28 | [MambaEviScrib: Mamba and Evidence-Guided Consistency Enhance CNN Robustness for Scribble-Based Weakly Supervised Ultrasound Image Segmentation](https://arxiv.org/abs/2409.19370v3) | 2409.19370v3 | 6 |
| 2024-09-27 | [Exploring Token Pruning in Vision State Space Models](https://arxiv.org/abs/2409.18962v1) | 2409.18962v1 | 10 |
| 2024-09-27 | [MECG-E: Mamba-based ECG Enhancer for Baseline Wander Removal](https://arxiv.org/abs/2409.18828v2) | 2409.18828v2 | 6 |
| 2024-09-27 | [Speech-Mamba: Long-Context Speech Recognition with Selective State Spaces Models](https://arxiv.org/abs/2409.18654v1) | 2409.18654v1 | 15 |
| 2024-09-26 | [MC-SEMamba: A Simple Multi-channel Extension of SEMamba](https://arxiv.org/abs/2409.17898v1) | 2409.17898v1 | 8 |
| 2024-09-26 | [EM-Net: Efficient Channel and Frequency Learning with Mamba for 3D Medical Image Segmentation](https://arxiv.org/abs/2409.17675v1) | 2409.17675v1 | 10 |
| 2024-09-26 | [Mamba Meets Financial Markets: A Graph-Mamba Approach for Stock Price Prediction](https://arxiv.org/abs/2410.03707v2) | 2410.03707v2 | 6 |
| 2024-09-25 | [Classification of Gleason Grading in Prostate Cancer Histopathology Images Using Deep Learning Techniques: YOLO, Vision Transformers, and Vision Mamba](https://arxiv.org/abs/2409.17122v2) | 2409.17122v2 | 6 |
| 2024-09-25 | [PASS: Path-selective State Space Model for Event-based Recognition](https://arxiv.org/abs/2409.16953v2) | 2409.16953v2 | 9 |
| 2024-09-25 | [Semi-LLIE: Semi-supervised Contrastive Learning with Mamba-based Low-light Image Enhancement](https://arxiv.org/abs/2409.16604v1) | 2409.16604v1 | 6 |
| 2024-09-25 | [MambaJSCC: Adaptive Deep Joint Source-Channel Coding with Generalized State Space Model](https://arxiv.org/abs/2409.16592v1) | 2409.16592v1 | 12 |
| 2024-09-24 | [Segmentation Strategies in Deep Learning for Prostate Cancer Diagnosis: A Comparative Study of Mamba, SAM, and YOLO](https://arxiv.org/abs/2409.16205v2) | 2409.16205v2 | 6 |
| 2024-09-24 | [TiM4Rec: An Efficient Sequential Recommendation Model Based on Time-Aware Structured State Space Duality Model](https://arxiv.org/abs/2409.16182v3) | 2409.16182v3 | 8 |
| 2024-09-24 | [DepMamba: Progressive Fusion Mamba for Multimodal Depression Detection](https://arxiv.org/abs/2409.15936v1) | 2409.15936v1 | 10 |
| 2024-09-24 | [Cambricon-LLM: A Chiplet-Based Hybrid Architecture for On-Device Inference of 70B LLM](https://arxiv.org/abs/2409.15654v1) | 2409.15654v1 | 6 |
| 2024-09-23 | [A Diagonal Structured State Space Model on Loihi 2 for Efficient Streaming Sequence Processing](https://arxiv.org/abs/2409.15022v1) | 2409.15022v1 | 10 |
| 2024-09-23 | [DiSPo: Diffusion-SSM based Policy Learning for Coarse-to-Fine Action Discretization](https://arxiv.org/abs/2409.14719v4) | 2409.14719v4 | 8 |
| 2024-09-22 | [Protein-Mamba: Biological Mamba Models for Protein Function Prediction](https://arxiv.org/abs/2409.14617v1) | 2409.14617v1 | 6 |
| 2024-09-22 | [GraspMamba: A Mamba-based Language-driven Grasp Detection Framework with Hierarchical Feature Learning](https://arxiv.org/abs/2409.14403v1) | 2409.14403v1 | 6 |
| 2024-09-22 | [DNN-based Enhanced DOA Sensing via Massive MIMO Receiver with Switches-based Hybrid Architecture](https://arxiv.org/abs/2409.14297v2) | 2409.14297v2 | 6 |
| 2024-09-19 | [DenoMamba: A fused state-space model for low-dose CT denoising](https://arxiv.org/abs/2409.13094v2) | 2409.13094v2 | 6 |
| 2024-09-19 | [MambaClinix: Hierarchical Gated Convolution and Mamba-Based U-Net for Enhanced 3D Medical Image Segmentation](https://arxiv.org/abs/2409.12533v1) | 2409.12533v1 | 10 |
| 2024-09-19 | [DeFT-Mamba: Universal Multichannel Sound Separation and Polyphonic Audio Classification](https://arxiv.org/abs/2409.12413v1) | 2409.12413v1 | 6 |
| 2024-09-19 | [MambaRecon: MRI Reconstruction with Structured State Space Models](https://arxiv.org/abs/2409.12401v1) | 2409.12401v1 | 12 |
| 2024-09-18 | [SPRMamba: Surgical Phase Recognition for Endoscopic Submucosal Dissection with Mamba](https://arxiv.org/abs/2409.12108v3) | 2409.12108v3 | 6 |
| 2024-09-18 | [Topological Deep Learning with State-Space Models: A Mamba Approach for Simplicial Complexes](https://arxiv.org/abs/2409.12033v1) | 2409.12033v1 | 8 |
| 2024-09-18 | [PhysMamba: Efficient Remote Physiological Measurement with SlowFast Temporal Difference Mamba](https://arxiv.org/abs/2409.12031v1) | 2409.12031v1 | 10 |
| 2024-09-18 | [DocMamba: Efficient Document Pre-training with State Space Model](https://arxiv.org/abs/2409.11887v2) | 2409.11887v2 | 12 |
| 2024-09-18 | [StableMamba: Distillation-free Scaling of Large SSMs for Images and Videos](https://arxiv.org/abs/2409.11867v2) | 2409.11867v2 | 6 |
| 2024-09-17 | [Bio-Inspired Mamba: Temporal Locality and Bioplausible Learning in Selective State Space Models](https://arxiv.org/abs/2409.11263v1) | 2409.11263v1 | 17 |
| 2024-09-17 | [Unleashing the Potential of Mamba: Boosting a LiDAR 3D Sparse Detector by Using Cross-Model Knowledge Distillation](https://arxiv.org/abs/2409.11018v3) | 2409.11018v3 | 8 |
| 2024-09-17 | [SkinMamba: A Precision Skin Lesion Segmentation Architecture with Cross-Scale Global State Modeling and Frequency Boundary Guidance](https://arxiv.org/abs/2409.10890v1) | 2409.10890v1 | 10 |
| 2024-09-16 | [CoMamba: Real-time Cooperative Perception Unlocked with State Space Models](https://arxiv.org/abs/2409.10699v2) | 2409.10699v2 | 12 |
| 2024-09-16 | [Flash STU: Fast Spectral Transform Units](https://arxiv.org/abs/2409.10489v6) | 2409.10489v6 | 10 |
| 2024-09-16 | [Mamba-ST: State Space Model for Efficient Style Transfer](https://arxiv.org/abs/2409.10385v1) | 2409.10385v1 | 12 |
| 2024-09-16 | [MARCA: Mamba Accelerator with ReConfigurable Architecture](https://arxiv.org/abs/2409.11440v1) | 2409.11440v1 | 6 |
| 2024-09-16 | [Leveraging Joint Spectral and Spatial Learning with MAMBA for Multichannel Speech Enhancement](https://arxiv.org/abs/2409.10376v2) | 2409.10376v2 | 6 |
| 2024-09-16 | [PixelBytes: Catching Unified Representation for Multimodal Generation](https://arxiv.org/abs/2410.01820v2) | 2410.01820v2 | 10 |
| 2024-09-15 | [Famba-V: Fast Vision Mamba with Cross-Layer Token Fusion](https://arxiv.org/abs/2409.09808v3) | 2409.09808v3 | 6 |
| 2024-09-15 | [SITSMamba for Crop Classification based on Satellite Image Time Series](https://arxiv.org/abs/2409.09673v2) | 2409.09673v2 | 6 |
| 2024-09-15 | [SparX: A Sparse Cross-Layer Connection Mechanism for Hierarchical Vision Mamba and Transformer Networks](https://arxiv.org/abs/2409.09649v2) | 2409.09649v2 | 11 |
| 2024-09-15 | [Self-supervised Learning for Acoustic Few-Shot Classification](https://arxiv.org/abs/2409.09647v2) | 2409.09647v2 | 8 |
| 2024-09-15 | [Spatial-Temporal Mamba Network for EEG-based Motor Imagery Classification](https://arxiv.org/abs/2409.09627v2) | 2409.09627v2 | 6 |
| 2024-09-14 | [Wave-U-Mamba: An End-To-End Framework For High-Quality And Efficient Speech Super Resolution](https://arxiv.org/abs/2409.09337v3) | 2409.09337v3 | 8 |
| 2024-09-13 | [MambaFoley: Foley Sound Generation using Selective State-Space Models](https://arxiv.org/abs/2409.09162v2) | 2409.09162v2 | 12 |
| 2024-09-13 | [Integration of Mamba and Transformer -- MAT for Long-Short Range Time Series Forecasting with Application to Weather Dynamics](https://arxiv.org/abs/2409.08530v1) | 2409.08530v1 | 6 |
| 2024-09-13 | [Mamba-YOLO-World: Marrying YOLO-World with Mamba for Open-Vocabulary Detection](https://arxiv.org/abs/2409.08513v3) | 2409.08513v3 | 10 |
| 2024-09-13 | [Tri-Plane Mamba: Efficiently Adapting Segment Anything Model for 3D Medical Images](https://arxiv.org/abs/2409.08492v1) | 2409.08492v1 | 6 |
| 2024-09-12 | [OCTAMamba: A State-Space Model Approach for Precision OCTA Vasculature Segmentation](https://arxiv.org/abs/2409.08000v2) | 2409.08000v2 | 6 |
| 2024-09-12 | [MambaMIC: An Efficient Baseline for Microscopic Image Classification with State Space Models](https://arxiv.org/abs/2409.07896v2) | 2409.07896v2 | 14 |
| 2024-09-12 | [Learning Brain Tumor Representation in 3D High-Resolution MR Images via Interpretable State Space Models](https://arxiv.org/abs/2409.07746v1) | 2409.07746v1 | 6 |
| 2024-09-12 | [CollaMamba: Efficient Collaborative Perception with Cross-Agent Spatial-Temporal State Space Model](https://arxiv.org/abs/2409.07714v3) | 2409.07714v3 | 12 |
| 2024-09-12 | [MedSegMamba: 3D CNN-Mamba Hybrid Architecture for Brain Segmentation](https://arxiv.org/abs/2409.08307v3) | 2409.08307v3 | 12 |
| 2024-09-11 | [miMamba: EEG-based Emotion Recognition with Multi-scale Inverted Mamba Models](https://arxiv.org/abs/2409.07589v2) | 2409.07589v2 | 6 |
| 2024-09-11 | [Mamba for Scalable and Efficient Personalized Recommendations](https://arxiv.org/abs/2409.17165v1) | 2409.17165v1 | 10 |
| 2024-09-11 | [Rethinking Mamba in Speech Processing by Self-Supervised Models](https://arxiv.org/abs/2409.07273v1) | 2409.07273v1 | 6 |
| 2024-09-11 | [Mamba Policy: Towards Efficient 3D Diffusion Policy with Hybrid Selective State Models](https://arxiv.org/abs/2409.07163v3) | 2409.07163v3 | 8 |
| 2024-09-11 | [Gated Slot Attention for Efficient Linear-Time Sequence Modeling](https://arxiv.org/abs/2409.07146v2) | 2409.07146v2 | 8 |
| 2024-09-11 | [Retinex-RAWMamba: Bridging Demosaicing and Denoising for Low-Light RAW Image Enhancement](https://arxiv.org/abs/2409.07040v5) | 2409.07040v5 | 6 |
| 2024-09-10 | [PPMamba: A Pyramid Pooling Local Auxiliary SSM-Based Model for Remote Sensing Image Semantic Segmentation](https://arxiv.org/abs/2409.06309v1) | 2409.06309v1 | 10 |
| 2024-09-10 | [A Two-Stage Band-Split Mamba-2 Network For Music Separation](https://arxiv.org/abs/2409.06245v2) | 2409.06245v2 | 6 |
| 2024-09-09 | [Rule Extrapolation in Language Models: A Study of Compositional Generalization on OOD Prompts](https://arxiv.org/abs/2409.13728v2) | 2409.13728v2 | 6 |
| 2024-09-09 | [DSDFormer: An Innovative Transformer-Mamba Framework for Robust High-Precision Driver Distraction Identification](https://arxiv.org/abs/2409.05587v2) | 2409.05587v2 | 6 |
| 2024-09-09 | [Shaking Up VLMs: Comparing Transformers and Structured State Space Models for Vision & Language Modeling](https://arxiv.org/abs/2409.05395v2) | 2409.05395v2 | 12 |
| 2024-09-08 | [Mamba-Enhanced Text-Audio-Video Alignment Network for Emotion Recognition in Conversations](https://arxiv.org/abs/2409.05243v1) | 2409.05243v1 | 6 |
| 2024-09-08 | [TF-Mamba: A Time-Frequency Network for Sound Source Localization](https://arxiv.org/abs/2409.05034v2) | 2409.05034v2 | 6 |
| 2024-09-07 | [Cross-attention Inspired Selective State Space Models for Target Sound Extraction](https://arxiv.org/abs/2409.04803v5) | 2409.04803v5 | 13 |
| 2024-09-06 | [Serp-Mamba: Advancing High-Resolution Retinal Vessel Segmentation with Selective State-Space Model](https://arxiv.org/abs/2409.04356v2) | 2409.04356v2 | 12 |
| 2024-09-06 | [MpoxMamba: A Grouped Mamba-based Lightweight Hybrid Network for Mpox Detection](https://arxiv.org/abs/2409.04218v2) | 2409.04218v2 | 10 |
| 2024-09-05 | [UV-Mamba: A DCN-Enhanced State Space Model for Urban Village Boundary Identification in High-Resolution Remote Sensing Images](https://arxiv.org/abs/2409.03431v3) | 2409.03431v3 | 14 |
| 2024-09-05 | [State-space models are accurate and efficient neural operators for dynamical systems](https://arxiv.org/abs/2409.03231v2) | 2409.03231v2 | 6 |
| 2024-09-05 | [Why mamba is effective? Exploit Linear Transformer-Mamba Network for Multi-Modality Image Fusion](https://arxiv.org/abs/2409.03223v1) | 2409.03223v1 | 6 |
| 2024-09-04 | [LongLLaVA: Scaling Multi-modal LLMs to 1000 Images Efficiently via a Hybrid Architecture](https://arxiv.org/abs/2409.02889v3) | 2409.02889v3 | 10 |
| 2024-09-04 | [Efficient Image Compression Using Advanced State Space Models](https://arxiv.org/abs/2409.02743v2) | 2409.02743v2 | 6 |
| 2024-09-04 | [MADiff: Motion-Aware Mamba Diffusion Models for Hand Trajectory Prediction on Egocentric Videos](https://arxiv.org/abs/2409.02638v2) | 2409.02638v2 | 6 |
| 2024-09-04 | [Mamba as a motion encoder for robotic imitation learning](https://arxiv.org/abs/2409.02636v2) | 2409.02636v2 | 10 |
| 2024-09-04 | [Rate-Adaptive Generative Semantic Communication Using Conditional Diffusion Models](https://arxiv.org/abs/2409.02597v3) | 2409.02597v3 | 6 |
| 2024-09-04 | [MusicMamba: A Dual-Feature Modeling Approach for Generating Chinese Traditional Music with Modal Precision](https://arxiv.org/abs/2409.02421v2) | 2409.02421v2 | 6 |
| 2024-09-03 | [LinFusion: 1 GPU, 1 Minute, 16K Image](https://arxiv.org/abs/2409.02097v3) | 2409.02097v3 | 10 |
| 2024-09-03 | [Shuffle Mamba: State Space Models with Random Shuffle for Multi-Modal Image Fusion](https://arxiv.org/abs/2409.01728v2) | 2409.01728v2 | 12 |
| 2024-09-03 | [PixelBytes: Catching Unified Embedding for Multimodal Generation](https://arxiv.org/abs/2409.15512v2) | 2409.15512v2 | 10 |
| 2024-09-03 | [EDCSSM: Edge Detection with Convolutional State Space Model](https://arxiv.org/abs/2409.01609v1) | 2409.01609v1 | 6 |
| 2024-09-02 | [SSD4Rec: A Structured State Space Duality Model for Efficient Sequential Recommendation](https://arxiv.org/abs/2409.01192v2) | 2409.01192v2 | 10 |
| 2024-09-02 | [FMRFT: Fusion Mamba and DETR for Query Time Sequence Intersection Fish Tracking](https://arxiv.org/abs/2409.01148v3) | 2409.01148v3 | 6 |
| 2024-08-31 | [Sparse Mamba: Introducing Controllability, Observability, And Stability To Structural State Space Models](https://arxiv.org/abs/2409.00563v3) | 2409.00563v3 | 12 |
| 2024-08-31 | [TrackSSM: A General Motion Predictor by State-Space Model](https://arxiv.org/abs/2409.00487v2) | 2409.00487v2 | 8 |
| 2024-08-31 | [A Hybrid Transformer-Mamba Network for Single Image Deraining](https://arxiv.org/abs/2409.00410v1) | 2409.00410v1 | 10 |
| 2024-08-30 | [State Space Model of Realized Volatility under the Existence of Dependent Market Microstructure Noise](https://arxiv.org/abs/2408.17187v1) | 2408.17187v1 | 6 |
| 2024-08-30 | [Stochastic Layer-Wise Shuffle for Improving Vision Mamba Training](https://arxiv.org/abs/2408.17081v2) | 2408.17081v2 | 6 |
| 2024-08-29 | [Evaluating Time-Series Training Dataset through Lens of Spectrum in Deep State Space Models](https://arxiv.org/abs/2408.16261v1) | 2408.16261v1 | 6 |
| 2024-08-28 | [DrowzEE-G-Mamba: Leveraging EEG and State Space Models for Driver Drowsiness Detection](https://arxiv.org/abs/2408.16145v2) | 2408.16145v2 | 12 |
| 2024-08-28 | [Mamba or Transformer for Time Series Forecasting? Mixture of Universals (MoU) Is All You Need](https://arxiv.org/abs/2408.15997v1) | 2408.15997v1 | 6 |
| 2024-08-28 | [SpineMamba: Enhancing 3D Spinal Segmentation in Clinical Imaging through Residual Visual Mamba Layers and Shape Priors](https://arxiv.org/abs/2408.15887v1) | 2408.15887v1 | 6 |
| 2024-08-28 | [MambaPlace:Text-to-Point-Cloud Cross-Modal Place Recognition with Attention Mamba Mechanisms](https://arxiv.org/abs/2408.15740v3) | 2408.15740v3 | 6 |
| 2024-08-28 | [ReMamba: Equip Mamba with Effective Long-Sequence Modeling](https://arxiv.org/abs/2408.15496v4) | 2408.15496v4 | 9 |
| 2024-08-27 | [DualKanbaFormer: An Efficient Selective Sparse Framework for Multimodal Aspect-based Sentiment Analysis](https://arxiv.org/abs/2408.15379v3) | 2408.15379v3 | 10 |
| 2024-08-27 | [The Mamba in the Llama: Distilling and Accelerating Hybrid Models](https://arxiv.org/abs/2408.15237v4) | 2408.15237v4 | 6 |
| 2024-08-27 | [MTMamba++: Enhancing Multi-Task Dense Scene Understanding via Mamba-Based Decoders](https://arxiv.org/abs/2408.15101v2) | 2408.15101v2 | 6 |
| 2024-08-27 | [SpikingSSMs: Learning Long Sequences with Sparse and Parallel Spiking State Space Models](https://arxiv.org/abs/2408.14909v2) | 2408.14909v2 | 6 |
| 2024-08-27 | [ZeroMamba: Exploring Visual State Space Model for Zero-Shot Learning](https://arxiv.org/abs/2408.14868v1) | 2408.14868v1 | 12 |
| 2024-08-26 | [LoG-VMamba: Local-Global Vision Mamba for Medical Image Segmentation](https://arxiv.org/abs/2408.14415v1) | 2408.14415v1 | 12 |
| 2024-08-26 | [MSFMamba: Multi-Scale Feature Fusion State Space Model for Multi-Source Remote Sensing Image Classification](https://arxiv.org/abs/2408.14255v2) | 2408.14255v2 | 12 |
| 2024-08-25 | [MSVM-UNet: Multi-Scale Vision Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2408.13735v1) | 2408.13735v1 | 10 |
| 2024-08-24 | [PointDGMamba: Domain Generalization of Point Cloud Classification via Generalized State Space Model](https://arxiv.org/abs/2408.13574v3) | 2408.13574v3 | 12 |
| 2024-08-23 | [Focus on Neighbors and Know the Whole: Towards Consistent Dense Multiview Text-to-Image Generator for 3D Creation](https://arxiv.org/abs/2408.13149v2) | 2408.13149v2 | 6 |
| 2024-08-23 | [Hierarchical Spatio-Temporal State-Space Modeling for fMRI Analysis](https://arxiv.org/abs/2408.13074v3) | 2408.13074v3 | 10 |
| 2024-08-23 | [O-Mamba: O-shape State-Space Model for Underwater Image Enhancement](https://arxiv.org/abs/2408.12816v1) | 2408.12816v1 | 6 |
| 2024-08-22 | [Jamba-1.5: Hybrid Transformer-Mamba Models at Scale](https://arxiv.org/abs/2408.12570v1) | 2408.12570v1 | 6 |
| 2024-08-22 | [Modeling Time-Dependent Responses of Optical Compressors with Selective State Space Models](https://arxiv.org/abs/2408.12549v4) | 2408.12549v4 | 11 |
| 2024-08-22 | [Scalable Autoregressive Image Generation with Mamba](https://arxiv.org/abs/2408.12245v5) | 2408.12245v5 | 8 |
| 2024-08-22 | [SDE: A Simplified and Disentangled Dependency Encoding Framework for State Space Models in Time Series Forecasting](https://arxiv.org/abs/2408.12068v3) | 2408.12068v3 | 6 |
| 2024-08-21 | [MambaCSR: Dual-Interleaved Scanning for Compressed Image Super-Resolution With SSMs](https://arxiv.org/abs/2408.11758v2) | 2408.11758v2 | 12 |
| 2024-08-21 | [BadVim: Unveiling Backdoor Threats in Visual State Space Model](https://arxiv.org/abs/2408.11679v3) | 2408.11679v3 | 6 |
| 2024-08-21 | [UNetMamba: An Efficient UNet-Like Mamba for Semantic Segmentation of High-Resolution Remote Sensing Images](https://arxiv.org/abs/2408.11545v3) | 2408.11545v3 | 6 |
| 2024-08-21 | [MambaOcc: Visual State Space Model for BEV-based Occupancy Prediction with Local Adaptive Reordering](https://arxiv.org/abs/2408.11464v1) | 2408.11464v1 | 12 |
| 2024-08-21 | [SIGMA: Selective Gated Mamba for Sequential Recommendation](https://arxiv.org/abs/2408.11451v4) | 2408.11451v4 | 8 |
| 2024-08-21 | [HMT-UNet: A hybird Mamba-Transformer Vision UNet for Medical Image Segmentation](https://arxiv.org/abs/2408.11289v2) | 2408.11289v2 | 10 |
| 2024-08-20 | [MambaDS: Near-Surface Meteorological Field Downscaling with Topography Constrained Selective State Space Modeling](https://arxiv.org/abs/2408.10854v1) | 2408.10854v1 | 15 |
| 2024-08-20 | [OMEGA: Efficient Occlusion-Aware Navigation for Air-Ground Robot in Dynamic Environments via State Space Model](https://arxiv.org/abs/2408.10618v2) | 2408.10618v2 | 10 |
| 2024-08-20 | [MUSE: Mamba is Efficient Multi-scale Learner for Text-video Retrieval](https://arxiv.org/abs/2408.10575v2) | 2408.10575v2 | 6 |
| 2024-08-20 | [Decision MetaMamba: Enhancing Selective SSM in Offline RL with Heterogeneous Sequence Mixing](https://arxiv.org/abs/2408.10517v6) | 2408.10517v6 | 6 |
| 2024-08-20 | [MambaEVT: Event Stream based Visual Object Tracking using State Space Model](https://arxiv.org/abs/2408.10487v1) | 2408.10487v1 | 12 |
| 2024-08-19 | [Transformers to SSMs: Distilling Quadratic Knowledge to Subquadratic Models](https://arxiv.org/abs/2408.10189v2) | 2408.10189v2 | 8 |
| 2024-08-19 | [OccMamba: Semantic Occupancy Prediction with State Space Models](https://arxiv.org/abs/2408.09859v2) | 2408.09859v2 | 12 |
| 2024-08-17 | [MambaTrack: A Simple Baseline for Multiple Object Tracking with State Space Model](https://arxiv.org/abs/2408.09178v1) | 2408.09178v1 | 14 |
| 2024-08-16 | [Improving VTE Identification through Language Models from Radiology Reports: A Comparative Study of Mamba, Phi-3 Mini, and BERT](https://arxiv.org/abs/2408.09043v1) | 2408.09043v1 | 6 |
| 2024-08-16 | [RGBT Tracking via All-layer Multimodal Interactions with Progressive Fusion Mamba](https://arxiv.org/abs/2408.08827v2) | 2408.08827v2 | 6 |
| 2024-08-16 | [QMambaBSR: Burst Image Super-Resolution with Query State Space Model](https://arxiv.org/abs/2408.08665v2) | 2408.08665v2 | 12 |
| 2024-08-16 | [GrassNet: State Space Model Meets Graph Neural Network](https://arxiv.org/abs/2408.08583v1) | 2408.08583v1 | 6 |
| 2024-08-15 | [ColorMamba: Towards High-quality NIR-to-RGB Spectral Translation with Mamba](https://arxiv.org/abs/2408.08087v1) | 2408.08087v1 | 10 |
| 2024-08-15 | [MambaMIM: Pre-training Mamba with State Space Token Interpolation and its Application to Medical Image Segmentation](https://arxiv.org/abs/2408.08070v2) | 2408.08070v2 | 12 |
| 2024-08-15 | [Mamba Retriever: Utilizing Mamba for Effective and Efficient Dense Retrieval](https://arxiv.org/abs/2408.08066v2) | 2408.08066v2 | 6 |
| 2024-08-15 | [MambaVT: Spatio-Temporal Contextual Modeling for robust RGB-T Tracking](https://arxiv.org/abs/2408.07889v1) | 2408.07889v1 | 12 |
| 2024-08-14 | [Costal Cartilage Segmentation with Topology Guided Deformable Mamba: Method and Benchmark](https://arxiv.org/abs/2408.07444v1) | 2408.07444v1 | 6 |
| 2024-08-13 | [DyG-Mamba: Continuous State Space Modeling on Dynamic Graphs](https://arxiv.org/abs/2408.06966v2) | 2408.06966v2 | 14 |
| 2024-08-12 | [MetMamba: Regional Weather Forecasting with Spatial-Temporal Mamba Model](https://arxiv.org/abs/2408.06400v2) | 2408.06400v2 | 6 |
| 2024-08-11 | [Neural Architecture Search based Global-local Vision Mamba for Palm-Vein Recognition](https://arxiv.org/abs/2408.05743v4) | 2408.05743v4 | 6 |
| 2024-08-11 | [SMILES-Mamba: Chemical Mamba Foundation Models for Drug ADMET Prediction](https://arxiv.org/abs/2408.05696v2) | 2408.05696v2 | 6 |
| 2024-08-10 | [Exploring Applications of State Space Models and Advanced Training Techniques in Sequential Recommendations: A Comparative Study on Efficiency and Performance](https://arxiv.org/abs/2408.05606v2) | 2408.05606v2 | 6 |
| 2024-08-09 | [SELD-Mamba: Selective State-Space Model for Sound Event Localization and Detection with Source Distance Estimation](https://arxiv.org/abs/2408.05057v1) | 2408.05057v1 | 6 |
| 2024-08-09 | [PTrajM: Efficient and Semantic-rich Trajectory Learning with Pretrained Trajectory-Mamba](https://arxiv.org/abs/2408.04916v1) | 2408.04916v1 | 6 |
| 2024-08-08 | [DyGMamba: Efficiently Modeling Long-Term Temporal Dependency on Continuous-Time Dynamic Graphs with State Space Models](https://arxiv.org/abs/2408.04713v4) | 2408.04713v4 | 12 |
| 2024-08-07 | [PackMamba: Efficient Processing of Variable-Length Sequences in Mamba training](https://arxiv.org/abs/2408.03865v2) | 2408.03865v2 | 6 |
| 2024-08-07 | [DRAMA: An Efficient End-to-end Motion Planner for Autonomous Driving with Mamba](https://arxiv.org/abs/2408.03601v2) | 2408.03601v2 | 6 |
| 2024-08-07 | [PoseMamba: Monocular 3D Human Pose Estimation with Bidirectional Global-Local Spatio-Temporal State Space Model](https://arxiv.org/abs/2408.03540v2) | 2408.03540v2 | 12 |
| 2024-08-06 | [Pose Magic: Efficient and Temporally Consistent Human Pose Estimation with a Hybrid Mamba-GCN Network](https://arxiv.org/abs/2408.02922v3) | 2408.02922v3 | 10 |
| 2024-08-05 | [Context-aware Mamba-based Reinforcement Learning for social robot navigation](https://arxiv.org/abs/2408.02661v2) | 2408.02661v2 | 10 |
| 2024-08-05 | [LaMamba-Diff: Linear-Time High-Fidelity Diffusion Models Based on Local Attention and Mamba](https://arxiv.org/abs/2408.02615v3) | 2408.02615v3 | 11 |
| 2024-08-05 | [BioMamba: Domain-Adaptive Biomedical Language Models](https://arxiv.org/abs/2408.02600v3) | 2408.02600v3 | 6 |
| 2024-08-04 | [Mamba-Spike: Enhancing the Mamba Architecture with a Spiking Front-End for Efficient Temporal Data Processing](https://arxiv.org/abs/2408.11823v1) | 2408.11823v1 | 13 |
| 2024-08-04 | [State Space Modelling for detecting and characterising Gravitational Waves afterglows](https://arxiv.org/abs/2408.01994v1) | 2408.01994v1 | 6 |
| 2024-08-04 | [DeMansia: Mamba Never Forgets Any Tokens](https://arxiv.org/abs/2408.01986v1) | 2408.01986v1 | 10 |
| 2024-08-03 | [JambaTalk: Speech-Driven 3D Talking Head Generation Based on Hybrid Transformer-Mamba Model](https://arxiv.org/abs/2408.01627v3) | 2408.01627v3 | 10 |
| 2024-08-02 | [Spatial and Spatial-Spectral Morphological Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2408.01372v3) | 2408.01372v3 | 10 |
| 2024-08-02 | [Wave-Mamba: Wavelet State Space Model for Ultra-High-Definition Low-Light Image Enhancement](https://arxiv.org/abs/2408.01276v1) | 2408.01276v1 | 14 |
| 2024-08-02 | [WaveMamba: Spatial-Spectral Wavelet Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2408.01231v2) | 2408.01231v2 | 6 |
| 2024-08-02 | [Multi-head Spatial-Spectral Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2408.01224v3) | 2408.01224v3 | 6 |
| 2024-08-02 | [A Survey of Mamba](https://arxiv.org/abs/2408.01129v8) | 2408.01129v8 | 10 |
| 2024-08-02 | [PhysMamba: State Space Duality Model for Remote Physiological Measurement](https://arxiv.org/abs/2408.01077v3) | 2408.01077v3 | 10 |
| 2024-08-02 | [MambaST: A Plug-and-Play Cross-Spectral Spatial-Temporal Fuser for Efficient Pedestrian Detection](https://arxiv.org/abs/2408.01037v1) | 2408.01037v1 | 10 |
| 2024-08-01 | [Cross-Scan Mamba with Masked Training for Robust Spectral Imaging](https://arxiv.org/abs/2408.00629v2) | 2408.00629v2 | 6 |
| 2024-08-01 | [MonoMM: A Multi-scale Mamba-Enhanced Network for Real-time Monocular 3D Object Detection](https://arxiv.org/abs/2408.00438v1) | 2408.00438v1 | 6 |
| 2024-08-01 | [Enhanced Structured State Space Models via Grouped FIR Filtering and Attention Sink Mechanisms](https://arxiv.org/abs/2408.00244v1) | 2408.00244v1 | 15 |
| 2024-07-31 | [RainMamba: Enhanced Locality Learning with State Space Models for Video Deraining](https://arxiv.org/abs/2407.21773v2) | 2407.21773v2 | 12 |
| 2024-07-30 | [MambaCapsule: Towards Transparent Cardiac Disease Diagnosis with Electrocardiography Using Mamba Capsule Network](https://arxiv.org/abs/2407.20893v2) | 2407.20893v2 | 6 |
| 2024-07-29 | [MambaGesture: Enhancing Co-Speech Gesture Generation with Mamba and Disentangled Multi-Modality Fusion](https://arxiv.org/abs/2407.19976v2) | 2407.19976v2 | 6 |
| 2024-07-29 | [ML-Mamba: Efficient Multi-Modal Large Language Model Utilizing Mamba-2](https://arxiv.org/abs/2407.19832v3) | 2407.19832v3 | 10 |
| 2024-07-27 | [Mamba-UIE: Enhancing Underwater Images with Physical Model Constraint](https://arxiv.org/abs/2407.19248v2) | 2407.19248v2 | 10 |
| 2024-07-27 | [MaTrRec: Uniting Mamba and Transformer for Sequential Recommendation](https://arxiv.org/abs/2407.19239v1) | 2407.19239v1 | 10 |
| 2024-07-27 | [Long Range Switching Time Series Prediction via State Space Model](https://arxiv.org/abs/2407.19201v1) | 2407.19201v1 | 6 |
| 2024-07-26 | [VSSD: Vision Mamba with Non-Causal State Space Duality](https://arxiv.org/abs/2407.18559v2) | 2407.18559v2 | 10 |
| 2024-07-25 | [LION: Linear Group RNN for 3D Object Detection in Point Clouds](https://arxiv.org/abs/2407.18232v1) | 2407.18232v1 | 8 |
| 2024-07-25 | [ALMRR: Anomaly Localization Mamba on Industrial Textured Surface with Feature Reconstruction and Refinement](https://arxiv.org/abs/2407.17705v1) | 2407.17705v1 | 6 |
| 2024-07-23 | [MxT: Mamba x Transformer for Image Inpainting](https://arxiv.org/abs/2407.16126v3) | 2407.16126v3 | 6 |
| 2024-07-22 | [Self-supervised Mamba-based Mastoidectomy Shape Prediction for Cochlear Implant Surgery](https://arxiv.org/abs/2407.15787v4) | 2407.15787v4 | 6 |
| 2024-07-22 | [GFE-Mamba: Mamba-based AD Multi-modal Progression Assessment via Generative Feature Extraction from MCI](https://arxiv.org/abs/2407.15719v3) | 2407.15719v3 | 6 |
| 2024-07-22 | [Mamba meets crack segmentation](https://arxiv.org/abs/2407.15714v1) | 2407.15714v1 | 6 |
| 2024-07-22 | [Particle Based Inference for Continuous-Discrete State Space Models](https://arxiv.org/abs/2407.15666v2) | 2407.15666v2 | 6 |
| 2024-07-21 | [Deep State Space Recurrent Neural Networks for Time Series Forecasting](https://arxiv.org/abs/2407.15236v1) | 2407.15236v1 | 7 |
| 2024-07-20 | [EEGMamba: Bidirectional State Space Model with Mixture of Experts for EEG Multi-task Classification](https://arxiv.org/abs/2407.20254v2) | 2407.20254v2 | 12 |
| 2024-07-20 | [FMamba: Mamba based on Fast-attention for Multivariate Time-series Forecasting](https://arxiv.org/abs/2407.14814v1) | 2407.14814v1 | 12 |
| 2024-07-19 | [Longhorn: State Space Models are Amortized Online Learners](https://arxiv.org/abs/2407.14207v5) | 2407.14207v5 | 12 |
| 2024-07-18 | [GroupMamba: Efficient Group-Based Visual State Space Model](https://arxiv.org/abs/2407.13772v2) | 2407.13772v2 | 12 |
| 2024-07-18 | [MLSA4Rec: Mamba Combined with Low-Rank Decomposed Self-Attention for Sequential Recommendation](https://arxiv.org/abs/2407.13135v1) | 2407.13135v1 | 6 |
| 2024-07-18 | [Enhancing Temporal Action Localization: Advanced S6 Modeling with Recurrent Mechanism](https://arxiv.org/abs/2407.13078v1) | 2407.13078v1 | 9 |
| 2024-07-17 | [Mamba-PTQ: Outlier Channels in Recurrent Large Language Models](https://arxiv.org/abs/2407.12397v1) | 2407.12397v1 | 9 |
| 2024-07-17 | [Serialized Point Mamba: A Serialized Point Cloud Mamba Segmentation Model](https://arxiv.org/abs/2407.12319v1) | 2407.12319v1 | 6 |
| 2024-07-15 | [Controlled Invariant Sets for Gaussian Process State Space Models](https://arxiv.org/abs/2407.11256v2) | 2407.11256v2 | 6 |
| 2024-07-15 | [OPa-Ma: Text Guided Mamba for 360-degree Image Out-painting](https://arxiv.org/abs/2407.10923v1) | 2407.10923v1 | 6 |
| 2024-07-15 | [ISMRNN: An Implicitly Segmented RNN Method with Mamba for Long-Term Time Series Forecasting](https://arxiv.org/abs/2407.10768v5) | 2407.10768v5 | 8 |
| 2024-07-15 | [MM-Tracker: Motion Mamba with Margin Loss for UAV-platform Multiple Object Tracking](https://arxiv.org/abs/2407.10485v3) | 2407.10485v3 | 6 |
| 2024-07-15 | [An Empirical Study of Mamba-based Pedestrian Attribute Recognition](https://arxiv.org/abs/2407.10374v2) | 2407.10374v2 | 6 |
| 2024-07-14 | [Enhancing Long-Range Dependency with State Space Model and Kolmogorov-Arnold Networks for Aspect-Based Sentiment Analysis](https://arxiv.org/abs/2407.10347v3) | 2407.10347v3 | 12 |
| 2024-07-14 | [Long Sequence Decoder Network for Mobile Sensing](https://arxiv.org/abs/2407.10338v1) | 2407.10338v1 | 6 |
| 2024-07-14 | [InfiniMotion: Mamba Boosts Memory in Transformer for Arbitrary Long Motion Generation](https://arxiv.org/abs/2407.10061v1) | 2407.10061v1 | 8 |
| 2024-07-13 | [Hydra: Bidirectional State Space Models Through Generalized Matrix Mixers](https://arxiv.org/abs/2407.09941v1) | 2407.09941v1 | 11 |
| 2024-07-13 | [Speech Slytherin: Examining the Performance and Efficiency of Mamba for Speech Separation, Recognition, and Synthesis](https://arxiv.org/abs/2407.09732v1) | 2407.09732v1 | 6 |
| 2024-07-12 | [Hamba: Single-view 3D Hand Reconstruction with Graph-guided Bi-Scanning Mamba](https://arxiv.org/abs/2407.09646v2) | 2407.09646v2 | 10 |
| 2024-07-11 | [ST-Mamba: Spatial-Temporal Mamba for Traffic Flow Estimation Recovery using Limited Data](https://arxiv.org/abs/2407.08558v1) | 2407.08558v1 | 6 |
| 2024-07-11 | [SliceMamba with Neural Architecture Search for Medical Image Segmentation](https://arxiv.org/abs/2407.08481v2) | 2407.08481v2 | 6 |
| 2024-07-11 | [VideoMamba: Spatio-Temporal Selective State Space Model](https://arxiv.org/abs/2407.08476v1) | 2407.08476v1 | 15 |
| 2024-07-11 | [Parallelizing Autoregressive Generation with Variational State Space Models](https://arxiv.org/abs/2407.08415v1) | 2407.08415v1 | 14 |
| 2024-07-11 | [SR-Mamba: Effective Surgical Phase Recognition with State Space Model](https://arxiv.org/abs/2407.08333v1) | 2407.08333v1 | 12 |
| 2024-07-11 | [GraphMamba: An Efficient Graph Structure Learning Vision Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2407.08255v1) | 2407.08255v1 | 6 |
| 2024-07-11 | [DMM: Disparity-guided Multispectral Mamba for Oriented Object Detection in Remote Sensing](https://arxiv.org/abs/2407.08132v1) | 2407.08132v1 | 6 |
| 2024-07-10 | [MambaVision: A Hybrid Mamba-Transformer Vision Backbone](https://arxiv.org/abs/2407.08083v2) | 2407.08083v2 | 6 |
| 2024-07-10 | [Towards a theory of learning dynamics in deep state space models](https://arxiv.org/abs/2407.07279v1) | 2407.07279v1 | 8 |
| 2024-07-09 | [RotRNN: Modelling Long Sequences with Rotations](https://arxiv.org/abs/2407.07239v3) | 2407.07239v3 | 6 |
| 2024-07-09 | [HTD-Mamba: Efficient Hyperspectral Target Detection with Pyramid State Space Model](https://arxiv.org/abs/2407.06841v2) | 2407.06841v2 | 12 |
| 2024-07-08 | [B'MOJO: Hybrid State Space Realizations of Foundation Models with Eidetic and Fading Memory](https://arxiv.org/abs/2407.06324v1) | 2407.06324v1 | 12 |
| 2024-07-08 | [Mamba-FSCIL: Dynamic Adaptation with Selective State Space Model for Few-Shot Class-Incremental Learning](https://arxiv.org/abs/2407.06136v4) | 2407.06136v4 | 15 |
| 2024-07-08 | [A Mamba-based Siamese Network for Remote Sensing Change Detection](https://arxiv.org/abs/2407.06839v1) | 2407.06839v1 | 7 |
| 2024-07-08 | [Self-Prior Guided Mamba-UNet Networks for Medical Image Super-Resolution](https://arxiv.org/abs/2407.05993v1) | 2407.05993v1 | 10 |
| 2024-07-08 | [Deform-Mamba Network for MRI Super-Resolution](https://arxiv.org/abs/2407.05969v1) | 2407.05969v1 | 6 |
| 2024-07-07 | [How Effective are State Space Models for Machine Translation?](https://arxiv.org/abs/2407.05489v1) | 2407.05489v1 | 12 |
| 2024-07-07 | [Just read twice: closing the recall gap for recurrent language models](https://arxiv.org/abs/2407.05483v1) | 2407.05483v1 | 11 |
| 2024-07-07 | [Mamba Hawkes Process for Event Sequence Modeling](https://arxiv.org/abs/2407.05302v2) | 2407.05302v2 | 15 |
| 2024-07-05 | [Learning to (Learn at Test Time): RNNs with Expressive Hidden States](https://arxiv.org/abs/2407.04620v4) | 2407.04620v4 | 6 |
| 2024-07-05 | [Fine-grained Context and Multi-modal Alignment for Freehand 3D Ultrasound Reconstruction](https://arxiv.org/abs/2407.04242v1) | 2407.04242v1 | 8 |
| 2024-07-04 | [QueryMamba: A Mamba-Based Encoder-Decoder Architecture with a Statistical Verb-Noun Interaction Module for Video Action Forecasting @ Ego4D Long-Term Action Anticipation Challenge 2024](https://arxiv.org/abs/2407.04184v1) | 2407.04184v1 | 6 |
| 2024-07-04 | [DASS: Distilled Audio State Space Models Are Stronger and More Duration-Scalable Learners](https://arxiv.org/abs/2407.04082v2) | 2407.04082v2 | 6 |
| 2024-07-04 | [Vision Mamba for Classification of Breast Ultrasound Images](https://arxiv.org/abs/2407.03552v2) | 2407.03552v2 | 6 |
| 2024-07-03 | [BVI-RLV: A Fully Registered Dataset for Low-Light Video Enhancement](https://arxiv.org/abs/2407.03535v3) | 2407.03535v3 | 8 |
| 2024-07-02 | [VFIMamba: Video Frame Interpolation with State Space Models](https://arxiv.org/abs/2407.02315v2) | 2407.02315v2 | 16 |
| 2024-07-02 | [MTMamba: Enhancing Multi-Task Dense Scene Understanding by Mamba-Based Decoders](https://arxiv.org/abs/2407.02228v2) | 2407.02228v2 | 6 |
| 2024-07-01 | [SpeakerBeam-SS: Real-time Target Speaker Extraction with Lightweight Conv-TasNet and State Space Modeling](https://arxiv.org/abs/2407.01857v1) | 2407.01857v1 | 6 |
| 2024-07-01 | [xLSTM-UNet can be an Effective 2D & 3D Medical Image Segmentation Backbone with Vision-LSTM (ViL) better than its Mamba Counterpart](https://arxiv.org/abs/2407.01530v2) | 2407.01530v2 | 10 |
| 2024-06-29 | [Time Series Clustering with General State Space Models via Stochastic Variational Inference](https://arxiv.org/abs/2407.00429v2) | 2407.00429v2 | 6 |
| 2024-06-27 | [Mamba or RWKV: Exploring High-Quality and High-Efficiency Segment Anything Model](https://arxiv.org/abs/2406.19369v1) | 2406.19369v1 | 14 |
| 2024-06-27 | [Snakes and Ladders: Two Steps Up for VideoMamba](https://arxiv.org/abs/2406.19006v4) | 2406.19006v4 | 6 |
| 2024-06-27 | [MMR-Mamba: Multi-Modal MRI Reconstruction with Mamba and Spatial-Frequency Information Fusion](https://arxiv.org/abs/2406.18950v2) | 2406.18950v2 | 6 |
| 2024-06-25 | [Pamba: Enhancing Global Interaction in Point Clouds via State Space Model](https://arxiv.org/abs/2406.17442v3) | 2406.17442v3 | 12 |
| 2024-06-25 | [SUM: Saliency Unification through Mamba for Visual Attention Modeling](https://arxiv.org/abs/2406.17815v2) | 2406.17815v2 | 6 |
| 2024-06-24 | [Exploring the Capability of Mamba in Speech Applications](https://arxiv.org/abs/2406.16808v1) | 2406.16808v1 | 10 |
| 2024-06-24 | [Venturing into Uncharted Waters: The Navigation Compass from Transformer to Mamba](https://arxiv.org/abs/2406.16722v1) | 2406.16722v1 | 10 |
| 2024-06-24 | [Vision Mamba-based autonomous crack segmentation on concrete, asphalt, and masonry surfaces](https://arxiv.org/abs/2406.16518v1) | 2406.16518v1 | 6 |
| 2024-06-24 | [OTCE: Hybrid SSM and Attention with Cross Domain Mixture of Experts to construct Observer-Thinker-Conceiver-Expresser](https://arxiv.org/abs/2406.16495v3) | 2406.16495v3 | 10 |
| 2024-06-23 | [Mamba-based Light Field Super-Resolution with Efficient Subspace Scanning](https://arxiv.org/abs/2406.16083v1) | 2406.16083v1 | 8 |
| 2024-06-23 | [Recursive variational Gaussian approximation with the Whittle likelihood for linear non-Gaussian state space models](https://arxiv.org/abs/2406.15998v3) | 2406.15998v3 | 6 |
| 2024-06-22 | [SEDMamba: Enhancing Selective State Space Modelling with Bottleneck Mechanism and Fine-to-Coarse Temporal Fusion for Efficient Error Detection in Robot-Assisted Surgery](https://arxiv.org/abs/2406.15920v4) | 2406.15920v4 | 15 |
| 2024-06-22 | [Soft Masked Mamba Diffusion Model for CT to MRI Conversion](https://arxiv.org/abs/2406.15910v1) | 2406.15910v1 | 6 |
| 2024-06-21 | [KalMamba: Towards Efficient Probabilistic State Space Models for RL under Uncertainty](https://arxiv.org/abs/2406.15131v1) | 2406.15131v1 | 12 |
| 2024-06-20 | [DeciMamba: Exploring the Length Extrapolation Potential of Mamba](https://arxiv.org/abs/2406.14528v3) | 2406.14528v3 | 6 |
| 2024-06-18 | [LFMamba: Light Field Image Super-Resolution with State Space Model](https://arxiv.org/abs/2406.12463v1) | 2406.12463v1 | 15 |
| 2024-06-18 | [Slot State Space Models](https://arxiv.org/abs/2406.12272v6) | 2406.12272v6 | 12 |
| 2024-06-17 | [SpoT-Mamba: Learning Long-Range Dependency on Spatio-Temporal Graphs with Selective State Spaces](https://arxiv.org/abs/2406.11244v1) | 2406.11244v1 | 13 |
| 2024-06-16 | [PyramidMamba: Rethinking Pyramid Feature Fusion with Selective Space State Model for Semantic Segmentation of Remote Sensing Imagery](https://arxiv.org/abs/2406.10828v1) | 2406.10828v1 | 6 |
| 2024-06-15 | [Voxel Mamba: Group-Free State Space Models for Point Cloud based 3D Object Detection](https://arxiv.org/abs/2406.10700v2) | 2406.10700v2 | 12 |
| 2024-06-14 | [ECGMamba: Towards Efficient ECG Classification with BiSSM](https://arxiv.org/abs/2406.10098v1) | 2406.10098v1 | 6 |
| 2024-06-14 | [SHMamba: Structured Hyperbolic State Space Model for Audio-Visual Question Answering](https://arxiv.org/abs/2406.09833v3) | 2406.09833v3 | 12 |
| 2024-06-13 | [QMamba: On First Exploration of Vision Mamba for Image Quality Assessment](https://arxiv.org/abs/2406.09546v2) | 2406.09546v2 | 10 |
| 2024-06-13 | [Towards Evaluating the Robustness of Visual State Space Models](https://arxiv.org/abs/2406.09407v3) | 2406.09407v3 | 12 |
| 2024-06-13 | [Q-S5: Towards Quantized State Space Models](https://arxiv.org/abs/2406.09477v1) | 2406.09477v1 | 10 |
| 2024-06-12 | [PixMamba: Leveraging State Space Models in a Dual-Level Architecture for Underwater Image Enhancement](https://arxiv.org/abs/2406.08444v1) | 2406.08444v1 | 12 |
| 2024-06-12 | [State Soup: In-Context Skill Learning, Retrieval and Mixing](https://arxiv.org/abs/2406.08423v1) | 2406.08423v1 | 8 |
| 2024-06-12 | [MaIL: Improving Imitation Learning with Mamba](https://arxiv.org/abs/2406.08234v2) | 2406.08234v2 | 6 |
| 2024-06-12 | [An Empirical Study of Mamba-based Language Models](https://arxiv.org/abs/2406.07887v1) | 2406.07887v1 | 10 |
| 2024-06-11 | [Autoregressive Pretraining with Mamba in Vision](https://arxiv.org/abs/2406.07537v1) | 2406.07537v1 | 12 |
| 2024-06-11 | [Samba: Simple Hybrid State Space Models for Efficient Unlimited Context Language Modeling](https://arxiv.org/abs/2406.07522v3) | 2406.07522v3 | 19 |
| 2024-06-11 | [MambaLRP: Explaining Selective State Space Sequence Models](https://arxiv.org/abs/2406.07592v3) | 2406.07592v3 | 11 |
| 2024-06-11 | [DualMamba: A Lightweight Spectral-Spatial Mamba-Convolution Network for Hyperspectral Image Classification](https://arxiv.org/abs/2406.07050v1) | 2406.07050v1 | 6 |
| 2024-06-11 | [FoodSky: A Food-oriented Large Language Model that Passes the Chef and Dietetic Examination](https://arxiv.org/abs/2406.10261v1) | 2406.10261v1 | 6 |
| 2024-06-10 | [Parallelizing Linear Transformers with the Delta Rule over Sequence Length](https://arxiv.org/abs/2406.06484v6) | 2406.06484v6 | 7 |
| 2024-06-10 | [MVGamba: Unify 3D Content Generation as State Space Sequence Modeling](https://arxiv.org/abs/2406.06367v3) | 2406.06367v3 | 7 |
| 2024-06-10 | [RawBMamba: End-to-End Bidirectional State Space Model for Audio Deepfake Detection](https://arxiv.org/abs/2406.06086v2) | 2406.06086v2 | 12 |
| 2024-06-10 | [PointABM:Integrating Bidirectional State Space Model with Multi-Head Self-Attention for Point Cloud Analysis](https://arxiv.org/abs/2406.06069v1) | 2406.06069v1 | 10 |
| 2024-06-10 | [MHS-VM: Multi-Head Scanning in Parallel Subspaces for Vision Mamba](https://arxiv.org/abs/2406.05992v1) | 2406.05992v1 | 10 |
| 2024-06-09 | [Mamba YOLO: A Simple Baseline for Object Detection with State Space Model](https://arxiv.org/abs/2406.05835v2) | 2406.05835v2 | 14 |
| 2024-06-09 | [What Can We Learn from State Space Models for Machine Learning on Graphs?](https://arxiv.org/abs/2406.05815v2) | 2406.05815v2 | 6 |
| 2024-06-09 | [CAMS: Convolution and Attention-Free Mamba-based Cardiac Image Segmentation](https://arxiv.org/abs/2406.05786v3) | 2406.05786v3 | 6 |
| 2024-06-09 | [Vision Mamba: Cutting-Edge Classification of Alzheimer's Disease with 3D MRI Scans](https://arxiv.org/abs/2406.05757v1) | 2406.05757v1 | 12 |
| 2024-06-09 | [HDMba: Hyperspectral Remote Sensing Imagery Dehazing with State Space Model](https://arxiv.org/abs/2406.05700v1) | 2406.05700v1 | 10 |
| 2024-06-08 | [Exploring Adversarial Robustness of Deep State Space Models](https://arxiv.org/abs/2406.05532v2) | 2406.05532v2 | 6 |
| 2024-06-08 | [Decision Mamba: A Multi-Grained State Space Model with Self-Evolution Regularization for Offline RL](https://arxiv.org/abs/2406.05427v3) | 2406.05427v3 | 14 |
| 2024-06-08 | [Benchmarking Neural Decoding Backbones towards Enhanced On-edge iBCI Applications](https://arxiv.org/abs/2406.06626v1) | 2406.06626v1 | 16 |
| 2024-06-08 | [CMamba: Channel Correlation Enhanced State Space Models for Multivariate Time Series Forecasting](https://arxiv.org/abs/2406.05316v3) | 2406.05316v3 | 12 |
| 2024-06-07 | [Efficient 3D Shape Generation via Diffusion Mamba with Bidirectional SSMs](https://arxiv.org/abs/2406.05038v1) | 2406.05038v1 | 10 |
| 2024-06-06 | [MambaDepth: Enhancing Long-range Dependency for Self-Supervised Fine-Structured Monocular Depth Estimation](https://arxiv.org/abs/2406.04532v1) | 2406.04532v1 | 10 |
| 2024-06-06 | [TSCMamba: Mamba Meets Multi-View Learning for Time Series Classification](https://arxiv.org/abs/2406.04419v2) | 2406.04419v2 | 12 |
| 2024-06-06 | [RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation](https://arxiv.org/abs/2406.04339v2) | 2406.04339v2 | 12 |
| 2024-06-06 | [Chimera: Effectively Modeling Multivariate Time Series with 2-Dimensional State Space Models](https://arxiv.org/abs/2406.04320v1) | 2406.04320v1 | 10 |
| 2024-06-06 | [CDMamba: Incorporating Local Clues into Mamba for Remote Sensing Image Binary Change Detection](https://arxiv.org/abs/2406.04207v2) | 2406.04207v2 | 10 |
| 2024-06-05 | [Combining Graph Neural Network and Mamba to Capture Local and Global Tissue Spatial Relationships in Whole Slide Images](https://arxiv.org/abs/2406.04377v1) | 2406.04377v1 | 10 |
| 2024-06-05 | [Computation-Efficient Era: A Comprehensive Survey of State Space Models in Medical Image Analysis](https://arxiv.org/abs/2406.03430v1) | 2406.03430v1 | 14 |
| 2024-06-05 | [Audio Mamba: Bidirectional State Space Model for Audio Representation Learning](https://arxiv.org/abs/2406.03344v1) | 2406.03344v1 | 12 |
| 2024-06-05 | [P-SpikeSSM: Harnessing Probabilistic Spiking State Space Models for Long-Range Dependency Tasks](https://arxiv.org/abs/2406.02923v5) | 2406.02923v5 | 6 |
| 2024-06-04 | [Feasibility of State Space Models for Network Traffic Generation](https://arxiv.org/abs/2406.02784v1) | 2406.02784v1 | 10 |
| 2024-06-04 | [GrootVL: Tree Topology is All You Need in State Space Model](https://arxiv.org/abs/2406.02395v1) | 2406.02395v1 | 6 |
| 2024-06-04 | [Audio Mamba: Selective State Spaces for Self-Supervised Audio Representations](https://arxiv.org/abs/2406.02178v2) | 2406.02178v2 | 13 |
| 2024-06-04 | [EchoMamba4Rec: Harmonizing Bidirectional State Space Models with Spectral Filtering for Advanced Sequential Recommendation](https://arxiv.org/abs/2406.02638v2) | 2406.02638v2 | 12 |
| 2024-06-04 | [Mamba as Decision Maker: Exploring Multi-scale Sequence Modeling in Offline Reinforcement Learning](https://arxiv.org/abs/2406.02013v2) | 2406.02013v2 | 9 |
| 2024-06-03 | [Universal In-Context Approximation By Prompting Fully Recurrent Models](https://arxiv.org/abs/2406.01424v2) | 2406.01424v2 | 7 |
| 2024-06-03 | [Dimba: Transformer-Mamba Diffusion Models](https://arxiv.org/abs/2406.01159v1) | 2406.01159v1 | 10 |
| 2024-06-03 | [LLEMamba: Low-Light Enhancement via Relighting-Guided Mamba with Deep Unfolding Network](https://arxiv.org/abs/2406.01028v1) | 2406.01028v1 | 6 |
| 2024-06-03 | [State Space Models on Temporal Graphs: A First-Principles Study](https://arxiv.org/abs/2406.00943v2) | 2406.00943v2 | 8 |
| 2024-06-02 | [Pretrained Hybrids with MAD Skills](https://arxiv.org/abs/2406.00894v2) | 2406.00894v2 | 12 |
| 2024-06-02 | [MGI: Multimodal Contrastive pre-training of Genomic and Medical Imaging](https://arxiv.org/abs/2406.00631v1) | 2406.00631v1 | 6 |
| 2024-06-01 | [Dual Hyperspectral Mamba for Efficient Spectral Compressive Imaging](https://arxiv.org/abs/2406.00449v1) | 2406.00449v1 | 6 |
| 2024-05-31 | [Mamba State-Space Models Are Lyapunov-Stable Learners](https://arxiv.org/abs/2406.00209v3) | 2406.00209v3 | 8 |
| 2024-05-31 | [Learning to Estimate System Specifications in Linear Temporal Logic using Transformers and Mamba](https://arxiv.org/abs/2405.20917v1) | 2405.20917v1 | 6 |
| 2024-05-31 | [S4Fusion: Saliency-aware Selective State Space Model for Infrared Visible Image Fusion](https://arxiv.org/abs/2405.20881v3) | 2405.20881v3 | 9 |
| 2024-05-31 | [Decision Mamba: Reinforcement Learning via Hybrid Selective Sequence Modeling](https://arxiv.org/abs/2406.00079v1) | 2406.00079v1 | 9 |
| 2024-05-30 | [MSSC-BiMamba: Multimodal Sleep Stage Classification and Early Diagnosis of Sleep Disorders with Bidirectional Mamba](https://arxiv.org/abs/2405.20142v2) | 2405.20142v2 | 10 |
| 2024-05-30 | [Language Models Need Inductive Biases to Count Inductively](https://arxiv.org/abs/2405.20131v2) | 2405.20131v2 | 6 |
| 2024-05-30 | [Joint Selective State Space Model and Detrending for Robust Time Series Anomaly Detection](https://arxiv.org/abs/2405.19823v2) | 2405.19823v2 | 9 |
| 2024-05-30 | [DeMamba: AI-Generated Video Detection on Million-Scale GenVideo Benchmark](https://arxiv.org/abs/2405.19707v3) | 2405.19707v3 | 6 |
| 2024-05-29 | [FourierMamba: Fourier Learning Integration with State Space Models for Image Deraining](https://arxiv.org/abs/2405.19450v2) | 2405.19450v2 | 12 |
| 2024-05-29 | [State Space Models are Provably Comparable to Transformers in Dynamic Token Selection](https://arxiv.org/abs/2405.19036v2) | 2405.19036v2 | 8 |
| 2024-05-29 | [Vim-F: Visual State Space Model Benefiting from Learning in the Frequency Domain](https://arxiv.org/abs/2405.18679v3) | 2405.18679v3 | 12 |
| 2024-05-28 | [Cardiovascular Disease Detection from Multi-View Chest X-rays with BI-Mamba](https://arxiv.org/abs/2405.18533v1) | 2405.18533v1 | 8 |
| 2024-05-28 | [Modeling Long Sequences in Bladder Cancer Recurrence: A Comparative Evaluation of LSTM,Transformer,and Mamba](https://arxiv.org/abs/2405.18518v2) | 2405.18518v2 | 8 |
| 2024-05-28 | [Coupled Mamba: Enhanced Multi-modal Fusion with Coupled State Space Model](https://arxiv.org/abs/2405.18014v2) | 2405.18014v2 | 12 |
| 2024-05-27 | [Sports-Traj: A Unified Trajectory Generation Model for Multi-Agent Movement in Sports](https://arxiv.org/abs/2405.17680v2) | 2405.17680v2 | 8 |
| 2024-05-27 | [Enhancing Global Sensitivity and Uncertainty Quantification in Medical Image Reconstruction with Monte Carlo Arbitrary-Masked Mamba](https://arxiv.org/abs/2405.17659v2) | 2405.17659v2 | 6 |
| 2024-05-27 | [SMR: State Memory Replay for Long Sequence Modeling](https://arxiv.org/abs/2405.17534v2) | 2405.17534v2 | 11 |
| 2024-05-27 | [The Expressive Capacity of State Space Models: A Formal Language Perspective](https://arxiv.org/abs/2405.17394v3) | 2405.17394v3 | 12 |
| 2024-05-27 | [Unlocking the Secrets of Linear Complexity Sequence Model from A Unified Perspective](https://arxiv.org/abs/2405.17383v1) | 2405.17383v1 | 8 |
| 2024-05-27 | [TokenUnify: Scaling Up Autoregressive Pretraining for Neuron Segmentation](https://arxiv.org/abs/2405.16847v2) | 2405.16847v2 | 7 |
| 2024-05-26 | [Limits of Deep Learning: Sequence Modeling through the Lens of Complexity Theory](https://arxiv.org/abs/2405.16674v3) | 2405.16674v3 | 7 |
| 2024-05-26 | [Mamba4KT:An Efficient and Effective Mamba-based Knowledge Tracing Model](https://arxiv.org/abs/2405.16542v1) | 2405.16542v1 | 8 |
| 2024-05-26 | [Explaining Modern Gated-Linear RNNs via a Unified Implicit Attention Formulation](https://arxiv.org/abs/2405.16504v2) | 2405.16504v2 | 11 |
| 2024-05-26 | [Image Deraining with Frequency-Enhanced State Space Model](https://arxiv.org/abs/2405.16470v4) | 2405.16470v4 | 6 |
| 2024-05-26 | [MambaTS: Improved Selective State Space Models for Long-term Time Series Forecasting](https://arxiv.org/abs/2405.16440v2) | 2405.16440v2 | 15 |
| 2024-05-25 | [UU-Mamba: Uncertainty-aware U-Mamba for Cardiac Image Segmentation](https://arxiv.org/abs/2405.17496v4) | 2405.17496v4 | 6 |
| 2024-05-25 | [Time-SSM: Simplifying and Unifying State Space Models for Time Series Forecasting](https://arxiv.org/abs/2405.16312v2) | 2405.16312v2 | 12 |
| 2024-05-25 | [MambaLLIE: Implicit Retinex-Aware Low Light Enhancement with Global-then-Local State Space](https://arxiv.org/abs/2405.16105v1) | 2405.16105v1 | 12 |
| 2024-05-24 | [MUCM-Net: A Mamba Powered UCM-Net for Skin Lesion Segmentation](https://arxiv.org/abs/2405.15925v2) | 2405.15925v2 | 6 |
| 2024-05-24 | [Scaling Diffusion Mamba with Bidirectional SSMs for Efficient Image and Video Generation](https://arxiv.org/abs/2405.15881v1) | 2405.15881v1 | 8 |
| 2024-05-24 | [MCDFN: Supply Chain Demand Forecasting via an Explainable Multi-Channel Data Fusion Network Model](https://arxiv.org/abs/2405.15598v5) | 2405.15598v5 | 6 |
| 2024-05-24 | [Meteor: Mamba-based Traversal of Rationale for Large Language and Vision Models](https://arxiv.org/abs/2405.15574v4) | 2405.15574v4 | 6 |
| 2024-05-24 | [PoinTramba: A Hybrid Transformer-Mamba Framework for Point Cloud Analysis](https://arxiv.org/abs/2405.15463v2) | 2405.15463v2 | 6 |
| 2024-05-24 | [MambaVC: Learned Visual Compression with Selective State Spaces](https://arxiv.org/abs/2405.15413v3) | 2405.15413v3 | 9 |
| 2024-05-24 | [PointRWKV: Efficient RWKV-Like Model for Hierarchical Point Cloud Learning](https://arxiv.org/abs/2405.15214v2) | 2405.15214v2 | 12 |
| 2024-05-23 | [Mamba-R: Vision Mamba ALSO Needs Registers](https://arxiv.org/abs/2405.14858v2) | 2405.14858v2 | 6 |
| 2024-05-23 | [EHRMamba: Towards Generalizable and Scalable Foundation Models for Electronic Health Records](https://arxiv.org/abs/2405.14567v3) | 2405.14567v3 | 6 |
| 2024-05-23 | [Scalable Visual State Space Model with Fractal Scanning](https://arxiv.org/abs/2405.14480v2) | 2405.14480v2 | 10 |
| 2024-05-23 | [Efficient Visual State Space Model for Image Deblurring](https://arxiv.org/abs/2405.14343v2) | 2405.14343v2 | 6 |
| 2024-05-23 | [MAMBA4D: Efficient Long-Sequence Point Cloud Video Understanding with Disentangled Spatial-Temporal State Space Models](https://arxiv.org/abs/2405.14338v3) | 2405.14338v3 | 12 |
| 2024-05-23 | [DiM: Diffusion Mamba for Efficient High-Resolution Image Synthesis](https://arxiv.org/abs/2405.14224v2) | 2405.14224v2 | 10 |
| 2024-05-23 | [Multi-Scale VMamba: Hierarchy in Hierarchy Visual State Space Model](https://arxiv.org/abs/2405.14174v1) | 2405.14174v1 | 12 |
| 2024-05-22 | [I2I-Mamba: Multi-modal medical image synthesis via selective state space modeling](https://arxiv.org/abs/2405.14022v6) | 2405.14022v6 | 15 |
| 2024-05-22 | [HOPE for a Robust Parameterization of Long-memory State Space Models](https://arxiv.org/abs/2405.13975v2) | 2405.13975v2 | 6 |
| 2024-05-22 | [HeteGraph-Mamba: Heterogeneous Graph Learning via Selective State Space Model](https://arxiv.org/abs/2405.13915v1) | 2405.13915v1 | 15 |
| 2024-05-22 | [Audio Mamba: Pretrained Audio State Space Model For Audio Tagging](https://arxiv.org/abs/2405.13636v1) | 2405.13636v1 | 12 |
| 2024-05-22 | [Deep Learning-Driven State Correction: A Hybrid Architecture for Radar-Based Dynamic Occupancy Grid Mapping](https://arxiv.org/abs/2405.13307v1) | 2405.13307v1 | 6 |
| 2024-05-21 | [Mamba in Speech: Towards an Alternative to Self-Attention](https://arxiv.org/abs/2405.12609v6) | 2405.12609v6 | 12 |
| 2024-05-21 | [3DSS-Mamba: 3D-Spectral-Spatial Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2405.12487v2) | 2405.12487v2 | 12 |
| 2024-05-20 | [Is Mamba Compatible with Trajectory Optimization in Offline Reinforcement Learning?](https://arxiv.org/abs/2405.12094v2) | 2405.12094v2 | 7 |
| 2024-05-20 | [Mamba-in-Mamba: Centralized Mamba-Cross-Scan in Tokenized Mamba Model for Hyperspectral Image Classification](https://arxiv.org/abs/2405.12003v4) | 2405.12003v4 | 12 |
| 2024-05-20 | [Alternators For Sequence Modeling](https://arxiv.org/abs/2405.11848v2) | 2405.11848v2 | 7 |
| 2024-05-20 | [SSAMBA: Self-Supervised Audio Representation Learning with Mamba State Space Model](https://arxiv.org/abs/2405.11831v2) | 2405.11831v2 | 12 |
| 2024-05-19 | [NetMamba: Efficient Network Traffic Classification via Pre-training Unidirectional Mamba](https://arxiv.org/abs/2405.11449v4) | 2405.11449v4 | 11 |
| 2024-05-18 | [MAMCA -- Optimal on Accuracy and Efficiency for Automatic Modulation Classification with Extended Signal Length](https://arxiv.org/abs/2405.11263v1) | 2405.11263v1 | 10 |
| 2024-05-17 | [Next-slot OFDM-CSI Prediction: Multi-head Self-attention or State Space Model?](https://arxiv.org/abs/2405.11072v1) | 2405.11072v1 | 6 |
| 2024-05-17 | [Know in AdVance: Linear-Complexity Forecasting of Ad Campaign Performance with Evolving User Interest](https://arxiv.org/abs/2405.10681v1) | 2405.10681v1 | 6 |
| 2024-05-17 | [CM-UNet: Hybrid CNN-Mamba UNet for Remote Sensing Image Semantic Segmentation](https://arxiv.org/abs/2405.10530v1) | 2405.10530v1 | 6 |
| 2024-05-16 | [RSDehamba: Lightweight Vision Mamba for Remote Sensing Satellite Image Dehazing](https://arxiv.org/abs/2405.10030v1) | 2405.10030v1 | 12 |
| 2024-05-16 | [IRSRMamba: Infrared Image Super-Resolution via Mamba-based Wavelet Transform Feature Modulation Model](https://arxiv.org/abs/2405.09873v2) | 2405.09873v2 | 6 |
| 2024-05-14 | [Rethinking Scanning Strategies with Vision Mamba in Semantic Segmentation of Remote Sensing Imagery: An Experimental Study](https://arxiv.org/abs/2405.08493v1) | 2405.08493v1 | 6 |
| 2024-05-14 | [WaterMamba: Visual State Space Model for Underwater Image Enhancement](https://arxiv.org/abs/2405.08419v1) | 2405.08419v1 | 12 |
| 2024-05-13 | [MambaOut: Do We Really Need Mamba for Vision?](https://arxiv.org/abs/2405.07992v3) | 2405.07992v3 | 10 |
| 2024-05-13 | [OverlapMamba: Novel Shift State Space Model for LiDAR-based Place Recognition](https://arxiv.org/abs/2405.07966v1) | 2405.07966v1 | 14 |
| 2024-05-13 | [Decision Mamba Architectures](https://arxiv.org/abs/2405.07943v2) | 2405.07943v2 | 6 |
| 2024-05-13 | [GMSR:Gradient-Guided Mamba for Spectral Reconstruction from RGB Images](https://arxiv.org/abs/2405.07777v2) | 2405.07777v2 | 6 |
| 2024-05-11 | [DTMamba : Dual Twin Mamba for Time Series Forecasting](https://arxiv.org/abs/2405.07022v1) | 2405.07022v1 | 6 |
| 2024-05-10 | [Linearizing Large Language Models](https://arxiv.org/abs/2405.06640v1) | 2405.06640v1 | 10 |
| 2024-05-10 | [An Investigation of Incorporating Mamba for Speech Enhancement](https://arxiv.org/abs/2405.06573v2) | 2405.06573v2 | 6 |
| 2024-05-09 | [Rethinking Efficient and Effective Point-based Networks for Event Camera Classification and Regression: EventMamba](https://arxiv.org/abs/2405.06116v4) | 2405.06116v4 | 10 |
| 2024-05-09 | [VM-DDPM: Vision Mamba Diffusion for Medical Image Synthesis](https://arxiv.org/abs/2405.05667v1) | 2405.05667v1 | 14 |
| 2024-05-08 | [StyleMamba : State Space Model for Efficient Text-driven Image Style Transfer](https://arxiv.org/abs/2405.05027v1) | 2405.05027v1 | 12 |
| 2024-05-08 | [HC-Mamba: Vision MAMBA with Hybrid Convolutional Techniques for Medical Image Segmentation](https://arxiv.org/abs/2405.05007v4) | 2405.05007v4 | 10 |
| 2024-05-08 | [Frequency-Assisted Mamba for Remote Sensing Image Super-Resolution](https://arxiv.org/abs/2405.04964v2) | 2405.04964v2 | 10 |
| 2024-05-07 | [Vision Mamba: A Comprehensive Survey and Taxonomy](https://arxiv.org/abs/2405.04404v1) | 2405.04404v1 | 12 |
| 2024-05-07 | [VMambaCC: A Visual State Space Model for Crowd Counting](https://arxiv.org/abs/2405.03978v1) | 2405.03978v1 | 12 |
| 2024-05-06 | [Trio-ViT: Post-Training Quantization and Acceleration for Softmax-Free Efficient Vision Transformer](https://arxiv.org/abs/2405.03882v3) | 2405.03882v3 | 6 |
| 2024-05-06 | [MemoryMamba: Memory-Augmented State Space Model for Defect Recognition](https://arxiv.org/abs/2405.03673v1) | 2405.03673v1 | 12 |
| 2024-05-06 | [Retinexmamba: Retinex-based Mamba for Low-light Image Enhancement](https://arxiv.org/abs/2405.03349v2) | 2405.03349v2 | 10 |
| 2024-05-06 | [MambaJSCC: Deep Joint Source-Channel Coding with Visual State Space Model](https://arxiv.org/abs/2405.03125v1) | 2405.03125v1 | 12 |
| 2024-05-05 | [Matten: Video Generation with Mamba-Attention](https://arxiv.org/abs/2405.03025v2) | 2405.03025v2 | 6 |
| 2024-05-05 | [AC-MAMBASEG: An adaptive convolution and Mamba-based architecture for enhanced skin lesion segmentation](https://arxiv.org/abs/2405.03011v1) | 2405.03011v1 | 6 |
| 2024-05-05 | [DVMSR: Distillated Vision Mamba for Efficient Super-Resolution](https://arxiv.org/abs/2405.03008v2) | 2405.03008v2 | 6 |
| 2024-05-05 | [SMCD: High Realism Motion Style Transfer via Mamba-based Diffusion](https://arxiv.org/abs/2405.02844v2) | 2405.02844v2 | 6 |
| 2024-05-04 | [From Generalization Analysis to Optimization Designs for State Space Models](https://arxiv.org/abs/2405.02670v1) | 2405.02670v1 | 8 |
| 2024-05-03 | [FER-YOLO-Mamba: Facial Expression Detection and Classification Based on Selective State Space](https://arxiv.org/abs/2405.01828v3) | 2405.01828v3 | 13 |
| 2024-05-02 | [SSUMamba: Spatial-Spectral Selective State Space Model for Hyperspectral Image Denoising](https://arxiv.org/abs/2405.01726v7) | 2405.01726v7 | 15 |
| 2024-05-02 | [SOAR: Advancements in Small Body Object Detection for Aerial Imagery Using State Space Models and Programmable Gradients](https://arxiv.org/abs/2405.01699v2) | 2405.01699v2 | 10 |
| 2024-05-02 | [TRAMBA: A Hybrid Transformer and Mamba Architecture for Practical Audio and Bone Conduction Speech Super Resolution and Enhancement on Mobile and Wearable Platforms](https://arxiv.org/abs/2405.01242v3) | 2405.01242v3 | 6 |
| 2024-04-30 | [CLIP-Mamba: CLIP Pretrained Mamba Models with OOD and Hessian Evaluation](https://arxiv.org/abs/2404.19394v1) | 2404.19394v1 | 10 |
| 2024-04-30 | [Revenge of the Fallen? Recurrent Models Match Transformers at Predicting Human Language Comprehension Metrics](https://arxiv.org/abs/2404.19178v2) | 2404.19178v2 | 11 |
| 2024-04-29 | [RSCaMa: Remote Sensing Image Change Captioning with State Space Model](https://arxiv.org/abs/2404.18895v3) | 2404.18895v3 | 10 |
| 2024-04-29 | [Visual Mamba: A Survey and New Outlooks](https://arxiv.org/abs/2404.18861v3) | 2404.18861v3 | 12 |
| 2024-04-29 | [Spectral-Spatial Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2404.18401v3) | 2404.18401v3 | 10 |
| 2024-04-28 | [S$^2$Mamba: A Spatial-spectral State Space Model for Hyperspectral Image Classification](https://arxiv.org/abs/2404.18213v2) | 2404.18213v2 | 12 |
| 2024-04-28 | [Mamba-FETrack: Frame-Event Tracking via State Space Model](https://arxiv.org/abs/2404.18174v1) | 2404.18174v1 | 12 |
| 2024-04-27 | [Revisiting Multi-modal Emotion Learning with Broad State Space Models and Probability-guidance Fusion](https://arxiv.org/abs/2404.17858v2) | 2404.17858v2 | 12 |
| 2024-04-26 | [Sparse Reconstruction of Optical Doppler Tomography with Alternative State Space Model and Attention](https://arxiv.org/abs/2404.17484v3) | 2404.17484v3 | 6 |
| 2024-04-26 | [Optimizing Universal Lesion Segmentation: State Space Model-Guided Hierarchical Networks with Feature Importance Adjustment](https://arxiv.org/abs/2404.17235v1) | 2404.17235v1 | 10 |
| 2024-04-25 | [CFMW: Cross-modality Fusion Mamba for Robust Object Detection under Adverse Weather](https://arxiv.org/abs/2404.16302v2) | 2404.16302v2 | 6 |
| 2024-04-24 | [Mamba-360: Survey of State Space Models as Transformer Alternative for Long Sequence Modelling: Methods, Applications, and Challenges](https://arxiv.org/abs/2404.16112v1) | 2404.16112v1 | 16 |
| 2024-04-24 | [A Survey on Visual Mamba](https://arxiv.org/abs/2404.15956v2) | 2404.15956v2 | 12 |
| 2024-04-24 | [ST-MambaSync: The Complement of Mamba and Transformers for Spatial-Temporal in Traffic Flow Prediction](https://arxiv.org/abs/2404.15899v3) | 2404.15899v3 | 6 |
| 2024-04-24 | [Bi-Mamba+: Bidirectional Mamba for Time Series Forecasting](https://arxiv.org/abs/2404.15772v3) | 2404.15772v3 | 10 |
| 2024-04-23 | [Mamba3D: Enhancing Local Features for 3D Point Cloud Analysis via State Space Model](https://arxiv.org/abs/2404.14966v2) | 2404.14966v2 | 12 |
| 2024-04-23 | [A Comprehensive Survey for Hyperspectral Image Classification: The Evolution from Conventional to Transformers and Mamba Models](https://arxiv.org/abs/2404.14955v4) | 2404.14955v4 | 6 |
| 2024-04-23 | [SST: Multi-Scale Hybrid Mamba-Transformer Experts for Time Series Forecasting](https://arxiv.org/abs/2404.14757v3) | 2404.14757v3 | 10 |
| 2024-04-22 | [A Multimodal Feature Distillation with Mamba-Transformer Network for Brain Tumor Segmentation with Incomplete Modalities](https://arxiv.org/abs/2404.14019v3) | 2404.14019v3 | 10 |
| 2024-04-22 | [MambaUIE&SR: Unraveling the Ocean's Secrets with Only 2.8 GFLOPs](https://arxiv.org/abs/2404.13884v2) | 2404.13884v2 | 6 |
| 2024-04-20 | [ST-Mamba: Spatial-Temporal Selective State Space Model for Traffic Flow Prediction](https://arxiv.org/abs/2404.13257v2) | 2404.13257v2 | 15 |
| 2024-04-20 | [Vim4Path: Self-Supervised Vision Mamba for Histopathology Images](https://arxiv.org/abs/2404.13222v2) | 2404.13222v2 | 10 |
| 2024-04-19 | [MambaMOS: LiDAR-based 3D Moving Object Segmentation with Motion-aware State Space Model](https://arxiv.org/abs/2404.12794v2) | 2404.12794v2 | 12 |
| 2024-04-17 | [CU-Mamba: Selective State Space Models with Channel Learning for Image Restoration](https://arxiv.org/abs/2404.11778v1) | 2404.11778v1 | 15 |
| 2024-04-17 | [Text-controlled Motion Mamba: Text-Instructed Temporal Grounding of Human Motion](https://arxiv.org/abs/2404.11375v2) | 2404.11375v2 | 6 |
| 2024-04-17 | [LongVQ: Long Sequence Modeling with Vector Quantization on Structured Memory](https://arxiv.org/abs/2404.11163v2) | 2404.11163v2 | 8 |
| 2024-04-16 | [HumMUSS: Human Motion Understanding using State Space Models](https://arxiv.org/abs/2404.10880v1) | 2404.10880v1 | 6 |
| 2024-04-15 | [HSIDMamba: Exploring Bidirectional State-Space Models for Hyperspectral Denoising](https://arxiv.org/abs/2404.09697v2) | 2404.09697v2 | 12 |
| 2024-04-15 | [State Space Model for New-Generation Network Alternative to Transformers: A Survey](https://arxiv.org/abs/2404.09516v1) | 2404.09516v1 | 10 |
| 2024-04-15 | [FusionMamba: Dynamic Feature Enhancement for Multimodal Image Fusion with Mamba](https://arxiv.org/abs/2404.09498v3) | 2404.09498v3 | 10 |
| 2024-04-15 | [FreqMamba: Viewing Mamba from a Frequency Perspective for Image Deraining](https://arxiv.org/abs/2404.09476v2) | 2404.09476v2 | 6 |
| 2024-04-14 | [A Novel State Space Model with Local Enhancement and State Sharing for Image Fusion](https://arxiv.org/abs/2404.09293v2) | 2404.09293v2 | 12 |
| 2024-04-14 | [Fusion-Mamba for Cross-modality Object Detection](https://arxiv.org/abs/2404.09146v1) | 2404.09146v1 | 6 |
| 2024-04-12 | [The Illusion of State in State-Space Models](https://arxiv.org/abs/2404.08819v3) | 2404.08819v3 | 6 |
| 2024-04-12 | [SpectralMamba: Efficient Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2404.08489v1) | 2404.08489v1 | 12 |
| 2024-04-12 | [MambaDFuse: A Mamba-based Dual-phase Model for Multi-modality Image Fusion](https://arxiv.org/abs/2404.08406v1) | 2404.08406v1 | 6 |
| 2024-04-11 | [FusionMamba: Efficient Remote Sensing Image Fusion with State Space Model](https://arxiv.org/abs/2404.07932v3) | 2404.07932v3 | 12 |
| 2024-04-11 | [SurvMamba: State Space Model with Multi-grained Multi-modal Interaction for Survival Prediction](https://arxiv.org/abs/2404.08027v2) | 2404.08027v2 | 12 |
| 2024-04-11 | [DGMamba: Domain Generalization via Generalized State Space Model](https://arxiv.org/abs/2404.07794v3) | 2404.07794v3 | 12 |
| 2024-04-11 | [ViM-UNet: Vision Mamba for Biomedical Segmentation](https://arxiv.org/abs/2404.07705v2) | 2404.07705v2 | 6 |
| 2024-04-11 | [Simba: Mamba augmented U-ShiftGCN for Skeletal Action Recognition in Videos](https://arxiv.org/abs/2404.07645v1) | 2404.07645v1 | 12 |
| 2024-04-10 | [3DMambaComplete: Exploring Structured State Space Model for Point Cloud Completion](https://arxiv.org/abs/2404.07106v2) | 2404.07106v2 | 12 |
| 2024-04-09 | [MambaAD: Exploring State Space Models for Multi-class Unsupervised Anomaly Detection](https://arxiv.org/abs/2404.06564v4) | 2404.06564v4 | 14 |
| 2024-04-09 | [RhythmMamba: Fast, Lightweight, and Accurate Remote Physiological Measurement](https://arxiv.org/abs/2404.06483v2) | 2404.06483v2 | 10 |
| 2024-04-09 | [Deep Mamba Multi-modal Learning](https://arxiv.org/abs/2406.18007v1) | 2406.18007v1 | 6 |
| 2024-04-09 | [Does Transformer Interpretability Transfer to RNNs?](https://arxiv.org/abs/2404.05971v1) | 2404.05971v1 | 10 |
| 2024-04-08 | [3DMambaIPF: A State Space Model for Iterative Point Cloud Filtering via Differentiable Rendering](https://arxiv.org/abs/2404.05522v2) | 2404.05522v2 | 14 |
| 2024-04-07 | [VMambaMorph: a Multi-Modality Deformable Image Registration Framework based on Visual State Space Model with Cross-Scan Module](https://arxiv.org/abs/2404.05105v2) | 2404.05105v2 | 12 |
| 2024-04-05 | [Sigma: Siamese Mamba Network for Multi-Modal Semantic Segmentation](https://arxiv.org/abs/2404.04256v3) | 2404.04256v3 | 10 |
| 2024-04-04 | [Locating and Editing Factual Associations in Mamba](https://arxiv.org/abs/2404.03646v2) | 2404.03646v2 | 10 |
| 2024-04-04 | [InsectMamba: Insect Pest Classification with State Space Model](https://arxiv.org/abs/2404.03611v1) | 2404.03611v1 | 12 |
| 2024-04-04 | [ChangeMamba: Remote Sensing Change Detection With Spatiotemporal State Space Model](https://arxiv.org/abs/2404.03425v7) | 2404.03425v7 | 12 |
| 2024-04-03 | [RS-Mamba for Large Remote Sensing Image Dense Prediction](https://arxiv.org/abs/2404.02668v2) | 2404.02668v2 | 6 |
| 2024-04-03 | [RS3Mamba: Visual State Space Model for Remote Sensing Images Semantic Segmentation](https://arxiv.org/abs/2404.02457v1) | 2404.02457v1 | 12 |
| 2024-04-02 | [SPMamba: State-space model is all you need in speech separation](https://arxiv.org/abs/2404.02063v2) | 2404.02063v2 | 6 |
| 2024-04-02 | [Samba: Semantic Segmentation of Remotely Sensed Images with State Space Model](https://arxiv.org/abs/2404.01705v2) | 2404.01705v2 | 10 |
| 2024-04-01 | [SpikeMba: Multi-Modal Spiking Saliency Mamba for Temporal Video Grounding](https://arxiv.org/abs/2404.01174v2) | 2404.01174v2 | 10 |
| 2024-04-01 | [T-Mamba: A unified framework with Long-Range Dependency in dual-domain for 2D & 3D Tooth Segmentation](https://arxiv.org/abs/2404.01065v2) | 2404.01065v2 | 6 |
| 2024-03-31 | [Enhancing Bangla Fake News Detection Using Bidirectional Gated Recurrent Units and Deep Learning Techniques](https://arxiv.org/abs/2404.01345v1) | 2404.01345v1 | 7 |
| 2024-03-31 | [RLGNet: Repeating-Local-Global History Network for Temporal Knowledge Graph Reasoning](https://arxiv.org/abs/2404.00586v2) | 2404.00586v2 | 6 |
| 2024-03-29 | [HARMamba: Efficient and Lightweight Wearable Sensor Human Activity Recognition Based on Bidirectional Mamba](https://arxiv.org/abs/2403.20183v3) | 2403.20183v3 | 6 |
| 2024-03-29 | [Learning Enriched Features via Selective State Spaces Model for Efficient Image Deblurring](https://arxiv.org/abs/2403.20106v2) | 2403.20106v2 | 7 |
| 2024-03-29 | [UltraLight VM-UNet: Parallel Vision Mamba Significantly Reduces Parameters for Skin Lesion Segmentation](https://arxiv.org/abs/2403.20035v3) | 2403.20035v3 | 6 |
| 2024-03-29 | [Decision Mamba: Reinforcement Learning via Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2403.19925v1) | 2403.19925v1 | 12 |
| 2024-03-29 | [MambaMixer: Efficient Selective State Space Models with Dual Token and Channel Selection](https://arxiv.org/abs/2403.19888v4) | 2403.19888v4 | 17 |
| 2024-03-28 | [Jamba: A Hybrid Transformer-Mamba Language Model](https://arxiv.org/abs/2403.19887v2) | 2403.19887v2 | 6 |
| 2024-03-28 | [RSMamba: Remote Sensing Image Classification with State Space Model](https://arxiv.org/abs/2403.19654v1) | 2403.19654v1 | 12 |
| 2024-03-27 | [Gamba: Marry Gaussian Splatting with Mamba for single view 3D reconstruction](https://arxiv.org/abs/2403.18795v3) | 2403.18795v3 | 6 |
| 2024-03-27 | [RankMamba: Benchmarking Mamba's Document Ranking Performance in the Era of Transformers](https://arxiv.org/abs/2403.18276v3) | 2403.18276v3 | 12 |
| 2024-03-27 | [Dual-path Mamba: Short and Long-term Bidirectional Selective Structured State Space Models for Speech Separation](https://arxiv.org/abs/2403.18257v2) | 2403.18257v2 | 14 |
| 2024-03-26 | [Heracles: A Hybrid SSM-Transformer Model for High-Resolution Image and Time-Series Analysis](https://arxiv.org/abs/2403.18063v2) | 2403.18063v2 | 8 |
| 2024-03-26 | [Serpent: Scalable and Efficient Image Restoration via Multi-scale Structured State Space Models](https://arxiv.org/abs/2403.17902v3) | 2403.17902v3 | 8 |
| 2024-03-26 | [Mechanistic Design and Scaling of Hybrid Architectures](https://arxiv.org/abs/2403.17844v2) | 2403.17844v2 | 12 |
| 2024-03-26 | [ReMamber: Referring Image Segmentation with Mamba Twister](https://arxiv.org/abs/2403.17839v2) | 2403.17839v2 | 6 |
| 2024-03-26 | [Rotate to Scan: UNet-like Mamba with Triplet SSM Module for Medical Image Segmentation](https://arxiv.org/abs/2403.17701v4) | 2403.17701v4 | 10 |
| 2024-03-26 | [PlainMamba: Improving Non-Hierarchical Mamba in Visual Recognition](https://arxiv.org/abs/2403.17695v2) | 2403.17695v2 | 10 |
| 2024-03-26 | [Integrating Mamba Sequence Model and Hierarchical Upsampling Network for Accurate Semantic Segmentation of Multiple Sclerosis Legion](https://arxiv.org/abs/2403.17432v1) | 2403.17432v1 | 10 |
| 2024-03-25 | [State Space Models as Foundation Models: A Control Theoretic Overview](https://arxiv.org/abs/2403.16899v1) | 2403.16899v1 | 12 |
| 2024-03-25 | [Proprioception Is All You Need: Terrain Classification for Boreal Forests](https://arxiv.org/abs/2403.16877v2) | 2403.16877v2 | 8 |
| 2024-03-25 | [VMRNN: Integrating Vision Mamba and LSTM for Efficient and Accurate Spatiotemporal Forecasting](https://arxiv.org/abs/2403.16536v3) | 2403.16536v3 | 10 |
| 2024-03-25 | [Uncovering Selective State Space Model's Capabilities in Lifelong Sequential Recommendation](https://arxiv.org/abs/2403.16371v1) | 2403.16371v1 | 13 |
| 2024-03-22 | [SiMBA: Simplified Mamba-Based Architecture for Vision and Multivariate Time series](https://arxiv.org/abs/2403.15360v2) | 2403.15360v2 | 12 |
| 2024-03-21 | [Cobra: Extending Mamba to Multi-Modal Large Language Model for Efficient Inference](https://arxiv.org/abs/2403.14520v4) | 2403.14520v4 | 6 |
| 2024-03-20 | [ZigMa: A DiT-style Zigzag Mamba Diffusion Model](https://arxiv.org/abs/2403.13802v3) | 2403.13802v3 | 8 |
| 2024-03-20 | [ProMamba: Prompt-Mamba for polyp segmentation](https://arxiv.org/abs/2403.13660v2) | 2403.13660v2 | 6 |
| 2024-03-20 | [H-vmunet: High-order Vision Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2403.13642v1) | 2403.13642v1 | 6 |
| 2024-03-20 | [VL-Mamba: Exploring State Space Models for Multimodal Learning](https://arxiv.org/abs/2403.13600v1) | 2403.13600v1 | 14 |
| 2024-03-19 | [STG-Mamba: Spatial-Temporal Graph Learning via Selective State Space Model](https://arxiv.org/abs/2403.12418v4) | 2403.12418v4 | 15 |
| 2024-03-18 | [VmambaIR: Visual State Space Model for Image Restoration](https://arxiv.org/abs/2403.11423v1) | 2403.11423v1 | 12 |
| 2024-03-17 | [Is Mamba Effective for Time Series Forecasting?](https://arxiv.org/abs/2403.11144v3) | 2403.11144v3 | 12 |
| 2024-03-16 | [Understanding Robustness of Visual State Space Models for Image Classification](https://arxiv.org/abs/2403.10935v1) | 2403.10935v1 | 10 |
| 2024-03-15 | [On the low-shot transferability of [V]-Mamba](https://arxiv.org/abs/2403.10696v1) | 2403.10696v1 | 6 |
| 2024-03-15 | [EfficientVMamba: Atrous Selective Scan for Light Weight Visual Mamba](https://arxiv.org/abs/2403.09977v1) | 2403.09977v1 | 10 |
| 2024-03-14 | [TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting](https://arxiv.org/abs/2403.09898v2) | 2403.09898v2 | 6 |
| 2024-03-14 | [Video Mamba Suite: State Space Model as a Versatile Alternative for Video Understanding](https://arxiv.org/abs/2403.09626v1) | 2403.09626v1 | 14 |
| 2024-03-14 | [Cloud gap-filling with deep learning for improved grassland monitoring](https://arxiv.org/abs/2403.09554v2) | 2403.09554v2 | 6 |
| 2024-03-14 | [MambaTalk: Efficient Holistic Gesture Synthesis with Selective State Space Models](https://arxiv.org/abs/2403.09471v6) | 2403.09471v6 | 15 |
| 2024-03-14 | [LocalMamba: Visual State Space Model with Windowed Selective Scan](https://arxiv.org/abs/2403.09338v1) | 2403.09338v1 | 14 |
| 2024-03-14 | [VM-UNET-V2 Rethinking Vision Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2403.09157v1) | 2403.09157v1 | 10 |
| 2024-03-13 | [MD-Dose: A diffusion model based on the Mamba for radiation dose prediction](https://arxiv.org/abs/2403.08479v2) | 2403.08479v2 | 6 |
| 2024-03-13 | [Activating Wider Areas in Image Super-Resolution](https://arxiv.org/abs/2403.08330v1) | 2403.08330v1 | 8 |
| 2024-03-12 | [Motion Mamba: Efficient and Long Sequence Motion Generation](https://arxiv.org/abs/2403.07487v4) | 2403.07487v4 | 12 |
| 2024-03-12 | [LKM-UNet: Large Kernel Vision Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2403.07332v2) | 2403.07332v2 | 6 |
| 2024-03-11 | [A multi-cohort study on prediction of acute brain dysfunction states using selective state space models](https://arxiv.org/abs/2403.07201v1) | 2403.07201v1 | 13 |
| 2024-03-11 | [VideoMamba: State Space Model for Efficient Video Understanding](https://arxiv.org/abs/2403.06977v2) | 2403.06977v2 | 12 |
| 2024-03-11 | [MambaMIL: Enhancing Long Sequence Modeling with Sequence Reordering in Computational Pathology](https://arxiv.org/abs/2403.06800v1) | 2403.06800v1 | 9 |
| 2024-03-11 | [Point Mamba: A Novel Point Cloud Backbone Based on State Space Model with Octree-Based Ordering Strategy](https://arxiv.org/abs/2403.06467v2) | 2403.06467v2 | 14 |
| 2024-03-09 | [ClinicalMamba: A Generative Clinical Language Model on Longitudinal Clinical Notes](https://arxiv.org/abs/2403.05795v1) | 2403.05795v1 | 6 |
| 2024-03-08 | [MambaLithium: Selective state space model for remaining-useful-life, state-of-health, and state-of-charge estimation of lithium-ion batteries](https://arxiv.org/abs/2403.05430v1) | 2403.05430v1 | 17 |
| 2024-03-08 | [LightM-UNet: Mamba Assists in Lightweight UNet for Medical Image Segmentation](https://arxiv.org/abs/2403.05246v2) | 2403.05246v2 | 10 |
| 2024-03-08 | [MamMIL: Multiple Instance Learning for Whole Slide Images with State Space Models](https://arxiv.org/abs/2403.05160v3) | 2403.05160v3 | 12 |
| 2024-03-06 | [Mamba4Rec: Towards Efficient Sequential Recommendation with Selective State Space Models](https://arxiv.org/abs/2403.03900v2) | 2403.03900v2 | 15 |
| 2024-03-06 | [MedMamba: Vision Mamba for Medical Image Classification](https://arxiv.org/abs/2403.03849v5) | 2403.03849v5 | 10 |
| 2024-03-05 | [Caduceus: Bi-Directional Equivariant Long-Range DNA Sequence Modeling](https://arxiv.org/abs/2403.03234v2) | 2403.03234v2 | 7 |
| 2024-03-04 | [MiM-ISTD: Mamba-in-Mamba for Efficient Infrared Small Target Detection](https://arxiv.org/abs/2403.02148v4) | 2403.02148v4 | 10 |
| 2024-03-03 | [The Hidden Attention of Mamba Models](https://arxiv.org/abs/2403.01590v2) | 2403.01590v2 | 12 |
| 2024-03-01 | [Point Cloud Mamba: Point Cloud Learning via State Space Model](https://arxiv.org/abs/2403.00762v4) | 2403.00762v4 | 12 |
| 2024-02-29 | [Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models](https://arxiv.org/abs/2402.19427v1) | 2402.19427v1 | 6 |
| 2024-02-29 | [MambaStock: Selective state space model for stock prediction](https://arxiv.org/abs/2402.18959v1) | 2402.18959v1 | 17 |
| 2024-02-28 | [Log Neural Controlled Differential Equations: The Lie Brackets Make a Difference](https://arxiv.org/abs/2402.18512v4) | 2402.18512v4 | 6 |
| 2024-02-28 | [MambaMIR: An Arbitrary-Masked Mamba for Joint Medical Image Reconstruction and Uncertainty Estimation](https://arxiv.org/abs/2402.18451v3) | 2402.18451v3 | 6 |
| 2024-02-26 | [DenseMamba: State Space Models with Dense Hidden Connection for Efficient Large Language Models](https://arxiv.org/abs/2403.00818v2) | 2403.00818v2 | 12 |
| 2024-02-24 | [Res-VMamba: Fine-Grained Food Category Visual Classification Using Selective State Space Models with Deep Residual Learning](https://arxiv.org/abs/2402.15761v3) | 2402.15761v3 | 15 |
| 2024-02-23 | [MambaIR: A Simple Baseline for Image Restoration with State-Space Model](https://arxiv.org/abs/2402.15648v3) | 2402.15648v3 | 10 |
| 2024-02-23 | [State Space Models for Event Cameras](https://arxiv.org/abs/2402.15584v3) | 2402.15584v3 | 6 |
| 2024-02-23 | [Efficient State Space Model via Fast Tensor Convolution and Block Diagonalization](https://arxiv.org/abs/2402.15290v4) | 2402.15290v4 | 10 |
| 2024-02-22 | [SICRN: Advancing Speech Enhancement through State Space Model and Inplace Convolution Techniques](https://arxiv.org/abs/2402.14225v1) | 2402.14225v1 | 8 |
| 2024-02-19 | [Pan-Mamba: Effective pan-sharpening with State Space Model](https://arxiv.org/abs/2402.12192v2) | 2402.12192v2 | 12 |
| 2024-02-16 | [Weak-Mamba-UNet: Visual Mamba Makes CNN and ViT Work Better for Scribble-based Medical Image Segmentation](https://arxiv.org/abs/2402.10887v1) | 2402.10887v1 | 6 |
| 2024-02-16 | [PointMamba: A Simple State Space Model for Point Cloud Analysis](https://arxiv.org/abs/2402.10739v5) | 2402.10739v5 | 12 |
| 2024-02-15 | [Hierarchical State Space Models for Continuous Sequence-to-Sequence Modeling](https://arxiv.org/abs/2402.10211v3) | 2402.10211v3 | 13 |
| 2024-02-13 | [Graph Mamba: Towards Learning on Graphs with State Space Models](https://arxiv.org/abs/2402.08678v2) | 2402.08678v2 | 12 |
| 2024-02-13 | [P-Mamba: Marrying Perona Malik Diffusion with Mamba for Efficient Pediatric Echocardiographic Left Ventricular Segmentation](https://arxiv.org/abs/2402.08506v3) | 2402.08506v3 | 6 |
| 2024-02-11 | [Semi-Mamba-UNet: Pixel-Level Contrastive and Pixel-Level Cross-Supervised Visual Mamba-based UNet for Semi-Supervised Medical Image Segmentation](https://arxiv.org/abs/2402.07245v3) | 2402.07245v3 | 6 |
| 2024-02-09 | [FD-Vision Mamba for Endoscopic Exposure Correction](https://arxiv.org/abs/2402.06378v2) | 2402.06378v2 | 6 |
| 2024-02-08 | [Mamba-ND: Selective State Space Modeling for Multi-Dimensional Data](https://arxiv.org/abs/2402.05892v5) | 2402.05892v5 | 17 |
| 2024-02-07 | [Mamba-UNet: UNet-Like Pure Visual Mamba for Medical Image Segmentation](https://arxiv.org/abs/2402.05079v2) | 2402.05079v2 | 10 |
| 2024-02-07 | [On Provable Length and Compositional Generalization](https://arxiv.org/abs/2402.04875v6) | 2402.04875v6 | 6 |
| 2024-02-06 | [Can Mamba Learn How to Learn? A Comparative Study on In-Context Learning Tasks](https://arxiv.org/abs/2402.04248v2) | 2402.04248v2 | 10 |
| 2024-02-06 | [U-shaped Vision Mamba for Single Image Dehazing](https://arxiv.org/abs/2402.04139v4) | 2402.04139v4 | 6 |
| 2024-02-05 | [nnMamba: 3D Biomedical Image Segmentation, Classification and Landmark Detection with State Space Model](https://arxiv.org/abs/2402.03526v2) | 2402.03526v2 | 12 |
| 2024-02-05 | [Swin-UMamba: Mamba-based UNet with ImageNet-based pretraining](https://arxiv.org/abs/2402.03302v2) | 2402.03302v2 | 8 |
| 2024-02-05 | [Is Mamba Capable of In-Context Learning?](https://arxiv.org/abs/2402.03170v2) | 2402.03170v2 | 10 |
| 2024-02-05 | [A Survey on Transformer Compression](https://arxiv.org/abs/2402.05964v2) | 2402.05964v2 | 8 |
| 2024-02-04 | [VM-UNet: Vision Mamba UNet for Medical Image Segmentation](https://arxiv.org/abs/2402.02491v2) | 2402.02491v2 | 10 |
| 2024-02-03 | [Attention-Mamba: A Mamba-Enhanced Multi-Scale Parallel Inference Network for Medical Image Segmentation](https://arxiv.org/abs/2402.02286v4) | 2402.02286v4 | 10 |
| 2024-02-01 | [Repeat After Me: Transformers are Better than State Space Models at Copying](https://arxiv.org/abs/2402.01032v2) | 2402.01032v2 | 8 |
| 2024-02-01 | [Graph-Mamba: Towards Long-Range Graph Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2402.00789v1) | 2402.00789v1 | 16 |
| 2024-02-01 | [BlackMamba: Mixture of Experts for State-Space Models](https://arxiv.org/abs/2402.01771v1) | 2402.01771v1 | 6 |
| 2024-01-25 | [Vivim: a Video Vision Mamba for Medical Video Segmentation](https://arxiv.org/abs/2401.14168v4) | 2401.14168v4 | 12 |
| 2024-01-25 | [MambaMorph: a Mamba-based Framework for Medical MR-CT Deformable Registration](https://arxiv.org/abs/2401.13934v5) | 2401.13934v5 | 6 |
| 2024-01-24 | [MambaByte: Token-free Selective State Space Model](https://arxiv.org/abs/2401.13660v3) | 2401.13660v3 | 15 |
| 2024-01-24 | [SegMamba: Long-range Sequential Modeling Mamba For 3D Medical Image Segmentation](https://arxiv.org/abs/2401.13560v4) | 2401.13560v4 | 10 |
| 2024-01-18 | [VMamba: Visual State Space Model](https://arxiv.org/abs/2401.10166v4) | 2401.10166v4 | 12 |
| 2024-01-18 | [MAMBA: Multi-level Aggregation via Memory Bank for Video Object Detection](https://arxiv.org/abs/2401.09923v2) | 2401.09923v2 | 6 |
| 2024-01-17 | [Vision Mamba: Efficient Visual Representation Learning with Bidirectional State Space Model](https://arxiv.org/abs/2401.09417v3) | 2401.09417v3 | 14 |
| 2024-01-16 | [MambaTab: A Plug-and-Play Model for Learning Tabular Data](https://arxiv.org/abs/2401.08867v2) | 2401.08867v2 | 6 |
| 2024-01-09 | [U-Mamba: Enhancing Long-range Dependency for Biomedical Image Segmentation](https://arxiv.org/abs/2401.04722v1) | 2401.04722v1 | 6 |
| 2024-01-08 | [MoE-Mamba: Efficient Selective State Space Models with Mixture of Experts](https://arxiv.org/abs/2401.04081v2) | 2401.04081v2 | 15 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-20 | [Particle Gibbs for Likelihood-Free Inference of State Space Models with Application to Stochastic Volatility](https://arxiv.org/abs/2312.13044v1) | 2312.13044v1 | 6 |
| 2023-12-15 | [Variational excess risk bound for general state space models](https://arxiv.org/abs/2312.09607v1) | 2312.09607v1 | 8 |
| 2023-12-14 | [Learning Long Sequences in Spiking Neural Networks](https://arxiv.org/abs/2401.00955v1) | 2401.00955v1 | 6 |
| 2023-12-11 | [Spectral State Space Models](https://arxiv.org/abs/2312.06837v4) | 2312.06837v4 | 8 |
| 2023-12-01 | [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752v2) | 2312.00752v2 | 21 |
| 2023-11-15 | [Accelerating Toeplitz Neural Network with Constant-time Inference Complexity](https://arxiv.org/abs/2311.08756v1) | 2311.08756v1 | 6 |
| 2023-11-08 | [Mixed orthogonality graphs for continuous-time state space models and orthogonal projections](https://arxiv.org/abs/2311.04478v2) | 2311.04478v2 | 6 |
| 2023-11-03 | [APRICOT-Mamba: Acuity Prediction in Intensive Care Unit (ICU): Development and Validation of a Stability, Transitions, and Life-Sustaining Therapies Prediction Model](https://arxiv.org/abs/2311.02026v2) | 2311.02026v2 | 6 |
| 2023-11-02 | [ABC-based Forecasting in State Space Models](https://arxiv.org/abs/2311.01021v1) | 2311.01021v1 | 6 |
| 2023-10-31 | [Progress and outlook on advanced fly scans based on Mamba](https://arxiv.org/abs/2310.20106v1) | 2310.20106v1 | 6 |
| 2023-10-30 | [Convolutional State Space Models for Long-Range Spatiotemporal Modeling](https://arxiv.org/abs/2310.19694v1) | 2310.19694v1 | 10 |
| 2023-10-12 | [Is attention required for ICL? Exploring the Relationship Between Model Architecture and In-Context Learning Ability](https://arxiv.org/abs/2310.08049v3) | 2310.08049v3 | 6 |
| 2023-09-26 | [Exploring RWKV for Memory Efficient and Low Latency Streaming ASR](https://arxiv.org/abs/2309.14758v1) | 2309.14758v1 | 8 |
| 2023-09-13 | [Out of Distribution Detection via Domain-Informed Gaussian Process State Space Models](https://arxiv.org/abs/2309.06655v2) | 2309.06655v2 | 6 |
| 2023-09-07 | [Spiking Structured State Space Model for Monaural Speech Enhancement](https://arxiv.org/abs/2309.03641v2) | 2309.03641v2 | 8 |
| 2023-09-05 | [TODM: Train Once Deploy Many Efficient Supernet-Based RNN-T Compression For On-device ASR Models](https://arxiv.org/abs/2309.01947v2) | 2309.01947v2 | 6 |
| 2023-08-29 | [Towards quantitative precision for ECG analysis: Leveraging state space models, self-supervision and patient metadata](https://arxiv.org/abs/2308.15291v1) | 2308.15291v1 | 6 |
| 2023-08-07 | [Mamba: Bringing Multi-Dimensional ABR to WebRTC](https://arxiv.org/abs/2308.03643v1) | 2308.03643v1 | 6 |
| 2023-08-02 | [The Bayesian Context Trees State Space Model for time series modelling and forecasting](https://arxiv.org/abs/2308.00913v3) | 2308.00913v3 | 6 |
| 2023-07-28 | [Dynamic Analysis and an Eigen Initializer for Recurrent Neural Networks](https://arxiv.org/abs/2307.15679v1) | 2307.15679v1 | 7 |
| 2023-07-21 | [Universality of Linear Recurrences Followed by Non-linear Projections: Finite-Width Guarantees and Benefits of Complex Eigenvalues](https://arxiv.org/abs/2307.11888v3) | 2307.11888v3 | 6 |
| 2023-07-11 | [Hybrid hidden Markov LSTM for short-term traffic flow prediction](https://arxiv.org/abs/2307.04954v2) | 2307.04954v2 | 6 |
| 2023-07-07 | [A Natural Language Processing Approach to Malware Classification](https://arxiv.org/abs/2307.11032v1) | 2307.11032v1 | 6 |
| 2023-07-04 | [Last layer state space model for representation learning and uncertainty quantification](https://arxiv.org/abs/2307.01566v1) | 2307.01566v1 | 6 |
| 2023-06-27 | [Structured State Space Models for Multiple Instance Learning in Digital Pathology](https://arxiv.org/abs/2306.15789v1) | 2306.15789v1 | 8 |
| 2023-06-20 | [State space models can express n-gram languages](https://arxiv.org/abs/2306.17184v3) | 2306.17184v3 | 12 |
| 2023-06-19 | [Sparse Modular Activation for Efficient Sequence Modeling](https://arxiv.org/abs/2306.11197v4) | 2306.11197v4 | 7 |
| 2023-06-15 | [Block-State Transformers](https://arxiv.org/abs/2306.09539v4) | 2306.09539v4 | 6 |
| 2023-06-15 | [A Recursive Newton Method for Smoothing in Nonlinear State Space Models](https://arxiv.org/abs/2306.09148v1) | 2306.09148v1 | 6 |
| 2023-05-22 | [RWKV: Reinventing RNNs for the Transformer Era](https://arxiv.org/abs/2305.13048v2) | 2305.13048v2 | 10 |
| 2023-05-21 | [Multi-Head State Space Model for Speech Recognition](https://arxiv.org/abs/2305.12498v2) | 2305.12498v2 | 6 |
| 2023-05-16 | [CQural: A Novel CNN based Hybrid Architecture for Quantum Continual Machine Learning](https://arxiv.org/abs/2305.09738v1) | 2305.09738v1 | 6 |
| 2023-05-16 | [Counterfactual Outcome Prediction using Structured State Space Model](https://arxiv.org/abs/2305.09207v1) | 2305.09207v1 | 6 |
| 2023-04-05 | [Inferring Population Dynamics in Macaque Cortex](https://arxiv.org/abs/2304.06040v2) | 2304.06040v2 | 6 |
| 2023-03-07 | [Structured State Space Models for In-Context Reinforcement Learning](https://arxiv.org/abs/2303.03982v3) | 2303.03982v3 | 8 |
| 2023-03-03 | [Descriptor State Space Modeling of Power Systems](https://arxiv.org/abs/2303.01701v1) | 2303.01701v1 | 6 |
| 2023-03-02 | [PlaNet-ClothPick: Effective Fabric Flattening Based on Latent Dynamic Planning](https://arxiv.org/abs/2303.01345v2) | 2303.01345v2 | 6 |
| 2023-02-17 | [Complex QA and language models hybrid architectures, Survey](https://arxiv.org/abs/2302.09051v5) | 2302.09051v5 | 6 |
| 2023-02-16 | [PandA(Box) flies on Bluesky: maintainable and user-friendly fly scans with Mamba at HEPS](https://arxiv.org/abs/2302.08304v2) | 2302.08304v2 | 6 |
| 2023-02-13 | [Simple Hardware-Efficient Long Convolutions for Sequence Modeling](https://arxiv.org/abs/2302.06646v1) | 2302.06646v1 | 7 |
| 2023-02-07 | [High-Dimensional Conditionally Gaussian State Space Models with Missing Data](https://arxiv.org/abs/2302.03172v1) | 2302.03172v1 | 6 |
| 2023-01-26 | [Neural Continuous-Discrete State Space Models for Irregularly-Sampled Time Series](https://arxiv.org/abs/2301.11308v3) | 2301.11308v3 | 6 |
| 2023-01-19 | [Diffusion-based Conditional ECG Generation with Structured State Space Models](https://arxiv.org/abs/2301.08227v2) | 2301.08227v2 | 6 |

### 2022
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2022-12-28 | [Hungry Hungry Hippos: Towards Language Modeling with State Space Models](https://arxiv.org/abs/2212.14052v3) | 2212.14052v3 | 10 |
| 2022-12-24 | [Deep Latent State Space Models for Time-Series Generation](https://arxiv.org/abs/2212.12749v3) | 2212.12749v3 | 6 |
| 2022-12-15 | [Efficient Long Sequence Modeling via State Space Augmented Transformer](https://arxiv.org/abs/2212.08136v1) | 2212.08136v1 | 7 |
| 2022-11-14 | [Advancing the State-of-the-Art for ECG Analysis through Structured State Space Models](https://arxiv.org/abs/2211.07579v1) | 2211.07579v1 | 6 |
| 2022-11-10 | [BERT-Based Combination of Convolutional and Recurrent Neural Network for Indonesian Sentiment Analysis](https://arxiv.org/abs/2211.05273v1) | 2211.05273v1 | 7 |
| 2022-10-31 | [Structured State Space Decoder for Speech Recognition and Synthesis](https://arxiv.org/abs/2210.17098v1) | 2210.17098v1 | 8 |
| 2022-10-20 | [Efficient variational approximations for state space models](https://arxiv.org/abs/2210.11010v3) | 2210.11010v3 | 6 |
| 2022-10-17 | [Modelling Emotion Dynamics in Song Lyrics with State Space Models](https://arxiv.org/abs/2210.09434v1) | 2210.09434v1 | 6 |
| 2022-10-17 | [What Makes Convolutional Models Great on Long Sequence Modeling?](https://arxiv.org/abs/2210.09298v1) | 2210.09298v1 | 7 |
| 2022-10-17 | [On Uncertainty in Deep State Space Models for Model-Based Reinforcement Learning](https://arxiv.org/abs/2210.09256v1) | 2210.09256v1 | 8 |
| 2022-10-14 | [LeVoice ASR Systems for the ISCSLP 2022 Intelligent Cockpit Speech Recognition Challenge](https://arxiv.org/abs/2210.07749v2) | 2210.07749v2 | 6 |
| 2022-10-13 | [Fast Estimation of Bayesian State Space Models Using Amortized Simulation-Based Inference](https://arxiv.org/abs/2210.07154v1) | 2210.07154v1 | 6 |
| 2022-09-21 | [Mega: Moving Average Equipped Gated Attention](https://arxiv.org/abs/2209.10655v3) | 2209.10655v3 | 6 |
| 2022-08-25 | [Time Series Clustering with an EM algorithm for Mixtures of Linear Gaussian State Space Models](https://arxiv.org/abs/2208.11907v3) | 2208.11907v3 | 6 |
| 2022-08-19 | [Diffusion-based Time Series Imputation and Forecasting with Structured State Space Models](https://arxiv.org/abs/2208.09399v3) | 2208.09399v3 | 6 |
| 2022-08-09 | [Simplified State Space Layers for Sequence Modeling](https://arxiv.org/abs/2208.04933v3) | 2208.04933v3 | 7 |
| 2022-08-08 | [fMRI-S4: learning short- and long-range dynamic fMRI dependencies using 1D Convolutions and State Space Models](https://arxiv.org/abs/2208.04166v1) | 2208.04166v1 | 6 |
| 2022-07-23 | [Combining Self-Training and Hybrid Architecture for Semi-supervised Abdominal Organ Segmentation](https://arxiv.org/abs/2207.11512v4) | 2207.11512v4 | 6 |
| 2022-06-29 | [Hidden Parameter Recurrent State Space Models For Changing Dynamics Scenarios](https://arxiv.org/abs/2206.14697v3) | 2206.14697v3 | 9 |
| 2022-06-29 | [Parallel square-root statistical linear regression for inference in nonlinear state space models](https://arxiv.org/abs/2207.00426v2) | 2207.00426v2 | 6 |
| 2022-06-29 | [State space model multiple imputation for missing data in non-stationary multivariate time series with application in digital Psychiatry](https://arxiv.org/abs/2206.14343v2) | 2206.14343v2 | 6 |
| 2022-06-27 | [Long Range Language Modeling via Gated State Spaces](https://arxiv.org/abs/2206.13947v3) | 2206.13947v3 | 6 |
| 2022-06-24 | [How to Train Your HiPPO: State Space Models with Generalized Orthogonal Basis Projections](https://arxiv.org/abs/2206.12037v2) | 2206.12037v2 | 6 |
| 2022-06-23 | [On the Parameterization and Initialization of Diagonal State Space Models](https://arxiv.org/abs/2206.11893v2) | 2206.11893v2 | 6 |
| 2022-06-07 | [Improving the Diagnosis of Psychiatric Disorders with Self-Supervised Graph State Space Models](https://arxiv.org/abs/2206.03331v1) | 2206.03331v1 | 6 |
| 2022-04-30 | [SVTR: Scene Text Recognition with a Single Visual Model](https://arxiv.org/abs/2205.00159v2) | 2205.00159v2 | 6 |
| 2022-04-12 | [A Tutorial on Solution Properties of State Space Models of Dynamical Systems](https://arxiv.org/abs/2204.06104v3) | 2204.06104v3 | 6 |
| 2022-03-29 | [State space models vs. multi-step predictors in predictive control: Are state space models complicating safe data-driven designs?](https://arxiv.org/abs/2203.15471v3) | 2203.15471v3 | 6 |
| 2022-03-28 | [Mamba: a systematic software solution for beamline experiments at HEPS](https://arxiv.org/abs/2203.17236v1) | 2203.17236v1 | 6 |
| 2022-03-03 | [Interpretable Latent Variables in Deep State Space Models](https://arxiv.org/abs/2203.02057v2) | 2203.02057v2 | 8 |
| 2022-02-25 | [Empirical spectral processes for stationary state space models](https://arxiv.org/abs/2202.12589v2) | 2202.12589v2 | 6 |
| 2022-01-25 | [Convolutional Xformers for Vision](https://arxiv.org/abs/2201.10271v1) | 2201.10271v1 | 6 |

### 2021
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2021-10-31 | [Efficiently Modeling Long Sequences with Structured State Spaces](https://arxiv.org/abs/2111.00396v3) | 2111.00396v3 | 6 |
| 2021-10-18 | [Assessing Ecosystem State Space Models: Identifiability and Estimation](https://arxiv.org/abs/2110.08967v1) | 2110.08967v1 | 6 |
| 2021-09-29 | [The Block-Correlated Pseudo Marginal Sampler for State Space Models](https://arxiv.org/abs/2109.14194v2) | 2109.14194v2 | 6 |
| 2021-09-18 | [Proposing a System Level Machine Learning Hybrid Architecture and Approach for a Comprehensive Autism Spectrum Disorder Diagnosis](https://arxiv.org/abs/2110.03775v1) | 2110.03775v1 | 6 |
| 2021-09-17 | [Non asymptotic estimation lower bounds for LTI state space models with Cramér-Rao and van Trees](https://arxiv.org/abs/2109.08582v1) | 2109.08582v1 | 6 |
| 2021-08-02 | [Representation learning for neural population activity with Neural Data Transformers](https://arxiv.org/abs/2108.01210v1) | 2108.01210v1 | 6 |
| 2021-07-30 | [Active Learning in Gaussian Process State Space Model](https://arxiv.org/abs/2108.00819v1) | 2108.00819v1 | 6 |
| 2021-07-14 | [Nonlinear State Space Modeling and Control of the Impact of Patients' Modifiable Lifestyle Behaviors on the Emergence of Multiple Chronic Conditions](https://arxiv.org/abs/2107.13394v1) | 2107.13394v1 | 6 |
| 2021-07-04 | [Graphical State Space Model](https://arxiv.org/abs/2107.01602v4) | 2107.01602v4 | 6 |
| 2021-06-23 | [Variational Bayes in State Space Models: Inferential and Predictive Accuracy](https://arxiv.org/abs/2106.12262v3) | 2106.12262v3 | 6 |
| 2021-06-14 | [Temporal Predictive Coding For Model-Based Planning In Latent Space](https://arxiv.org/abs/2106.07156v1) | 2106.07156v1 | 6 |
| 2021-06-04 | [Deep Switching State Space Model (DS$^3$M) for Nonlinear Time Series Forecasting with Regime Switching](https://arxiv.org/abs/2106.02329v3) | 2106.02329v3 | 8 |
| 2021-06-03 | [Deep Probabilistic Time Series Forecasting using Augmented Recurrent Input for Dynamic Systems](https://arxiv.org/abs/2106.05848v2) | 2106.05848v2 | 7 |
| 2021-04-26 | [Stochastic Recurrent Neural Network for Multistep Time Series Forecasting](https://arxiv.org/abs/2104.12311v3) | 2104.12311v3 | 7 |
| 2021-03-18 | [Lossless compression with state space models using bits back coding](https://arxiv.org/abs/2103.10150v3) | 2103.10150v3 | 6 |
| 2021-03-12 | [On Incorporating Forecasts into Linear State Space Model Markov Decision Processes](https://arxiv.org/abs/2103.07533v1) | 2103.07533v1 | 6 |
| 2021-02-17 | [LambdaNetworks: Modeling Long-Range Interactions Without Attention](https://arxiv.org/abs/2102.08602v1) | 2102.08602v1 | 6 |
| 2021-01-31 | [Learning Interpretable Deep State Space Model for Probabilistic Time Series Forecasting](https://arxiv.org/abs/2102.00397v1) | 2102.00397v1 | 8 |
| 2021-01-25 | [Spatial Wideband Channel Estimation for MmWave Massive MIMO Systems with Hybrid Architectures and Low-Resolution ADCs](https://arxiv.org/abs/2101.10158v1) | 2101.10158v1 | 6 |
| 2021-01-21 | [bssm: Bayesian Inference of Non-linear and Non-Gaussian State Space Models in R](https://arxiv.org/abs/2101.08492v2) | 2101.08492v2 | 6 |
| 2021-01-08 | [Spatiotemporal blocking of the bouncy particle sampler for efficient inference in state space models](https://arxiv.org/abs/2101.03079v2) | 2101.03079v2 | 6 |

### 2020
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2020-11-26 | [Physics-Informed Neural State Space Models via Learning and Evolution](https://arxiv.org/abs/2011.13497v1) | 2011.13497v1 | 6 |
| 2020-11-14 | [Bayesian recurrent state space model for rs-fMRI](https://arxiv.org/abs/2011.07365v1) | 2011.07365v1 | 9 |
| 2020-10-23 | [State space models for building control: how deep should you go?](https://arxiv.org/abs/2010.12257v1) | 2010.12257v1 | 8 |
| 2020-10-10 | [Hybrid-S2S: Video Object Segmentation with Recurrent Networks and Correspondence Matching](https://arxiv.org/abs/2010.05069v2) | 2010.05069v2 | 7 |
| 2020-08-31 | [Design and Simulation of a Hybrid Architecture for Edge Computing in 5G and Beyond](https://arxiv.org/abs/2009.00041v1) | 2009.00041v1 | 6 |
| 2020-08-18 | [Score-Based Parameter Estimation for a Class of Continuous-Time State Space Models](https://arxiv.org/abs/2008.07803v2) | 2008.07803v2 | 6 |
| 2020-08-12 | [Text Classification based on Multi-granularity Attention Hybrid Neural Network](https://arxiv.org/abs/2008.05282v1) | 2008.05282v1 | 6 |
| 2020-07-17 | [A Fourier State Space Model for Bayesian ODE Filters](https://arxiv.org/abs/2007.09118v2) | 2007.09118v2 | 6 |
| 2020-07-02 | [A Novel BGCapsule Network for Text Classification](https://arxiv.org/abs/2007.04302v1) | 2007.04302v1 | 6 |
| 2020-06-11 | [Stanza: A Nonlinear State Space Model for Probabilistic Inference in Non-Stationary Time Series](https://arxiv.org/abs/2006.06553v1) | 2006.06553v1 | 8 |
| 2020-06-09 | [Neural Physicist: Learning Physical Dynamics from Image Sequences](https://arxiv.org/abs/2006.05044v1) | 2006.05044v1 | 6 |
| 2020-05-19 | [Pairs Trading with Nonlinear and Non-Gaussian State Space Models](https://arxiv.org/abs/2005.09794v1) | 2005.09794v1 | 6 |
| 2020-05-04 | [Localized active learning of Gaussian process state space models](https://arxiv.org/abs/2005.02191v3) | 2005.02191v3 | 6 |
| 2020-04-28 | [Predicting Infection of COVID-19 in Japan: State Space Modeling Approach](https://arxiv.org/abs/2004.13483v1) | 2004.13483v1 | 6 |
| 2020-04-10 | [Robust Estimation for Discrete-Time State Space Models](https://arxiv.org/abs/2004.05023v1) | 2004.05023v1 | 6 |
| 2020-04-08 | [Variable Rate Video Compression using a Hybrid Recurrent Convolutional Learning Framework](https://arxiv.org/abs/2004.04244v2) | 2004.04244v2 | 7 |
| 2020-03-31 | [Deep State Space Models for Nonlinear System Identification](https://arxiv.org/abs/2003.14162v3) | 2003.14162v3 | 6 |
| 2020-02-26 | [Enforcing Mean Reversion in State Space Models for Prawn Pond Water Quality Forecasting](https://arxiv.org/abs/2002.11228v1) | 2002.11228v1 | 6 |
| 2020-02-21 | [Whittle estimation for stationary state space models with finite second moments](https://arxiv.org/abs/2002.09426v1) | 2002.09426v1 | 6 |
| 2020-02-13 | [Backward importance sampling for online estimation of state space models](https://arxiv.org/abs/2002.05438v2) | 2002.05438v2 | 6 |
| 2020-01-31 | [Domain-Adversarial and Conditional State Space Model for Imitation Learning](https://arxiv.org/abs/2001.11628v2) | 2001.11628v2 | 6 |
| 2020-01-12 | [Experimental Determination of an Extended DC Servo-Motor State Space Model: An Undergraduate Experiment](https://arxiv.org/abs/2001.03915v1) | 2001.03915v1 | 6 |
| 2020-01-07 | [HyGCN: A GCN Accelerator with Hybrid Architecture](https://arxiv.org/abs/2001.02514v1) | 2001.02514v1 | 6 |

### 2019
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2019-12-28 | [The Lévy State Space Model](https://arxiv.org/abs/1912.12524v2) | 1912.12524v2 | 6 |
| 2019-12-28 | [Opportunities and Challenges of Deep Learning Methods for Electrocardiogram Data: A Systematic Review](https://arxiv.org/abs/2001.01550v3) | 2001.01550v3 | 6 |
| 2019-11-09 | [Factored Latent-Dynamic Conditional Random Fields for Single and Multi-label Sequence Modeling](https://arxiv.org/abs/1911.03667v2) | 1911.03667v2 | 7 |
| 2019-10-08 | [Linking emotions to behaviors through deep transfer learning](https://arxiv.org/abs/1910.03641v1) | 1910.03641v1 | 6 |
| 2019-10-02 | [Content Delivery Through Hybrid Architecture in Video on Demand System](https://arxiv.org/abs/1910.05304v1) | 1910.05304v1 | 6 |
| 2019-10-02 | [The Neural Moving Average Model for Scalable Variational Inference of State Space Models](https://arxiv.org/abs/1910.00879v2) | 1910.00879v2 | 6 |
| 2019-10-02 | [Variational Temporal Abstraction](https://arxiv.org/abs/1910.00775v1) | 1910.00775v1 | 6 |
| 2019-08-18 | [A Dual-Staged Context Aggregation Method Towards Efficient End-To-End Speech Enhancement](https://arxiv.org/abs/1908.06468v4) | 1908.06468v4 | 6 |
| 2019-08-12 | [Channel Estimation for MIMO Hybrid Architectures with Low Resolution ADCs for mmWave Communication](https://arxiv.org/abs/1908.04162v2) | 1908.04162v2 | 6 |
| 2019-08-11 | [DynaNet: Neural Kalman Dynamical Model for Motion Estimation and Prediction](https://arxiv.org/abs/1908.03918v3) | 1908.03918v3 | 6 |
| 2019-07-18 | [Semi-parametric estimation and prediction intervals in state space models](https://arxiv.org/abs/1907.07915v2) | 1907.07915v2 | 6 |
| 2019-07-16 | [Structured Variational Inference in Unstable Gaussian Process State Space Models](https://arxiv.org/abs/1907.07035v3) | 1907.07035v3 | 6 |
| 2019-07-15 | [Dynamical Systems as Temporal Feature Spaces](https://arxiv.org/abs/1907.06382v3) | 1907.06382v3 | 6 |
| 2019-07-14 | [Markov-switching State Space Models for Uncovering Musical Interpretation](https://arxiv.org/abs/1907.06244v2) | 1907.06244v2 | 6 |
| 2019-07-06 | [Takens-inspired neuromorphic processor: a downsizing tool for random recurrent neural networks via feature extraction](https://arxiv.org/abs/1907.03122v1) | 1907.03122v1 | 7 |
| 2019-06-13 | [Recurrent Neural Processes](https://arxiv.org/abs/1906.05915v2) | 1906.05915v2 | 7 |
| 2019-06-08 | [Asymptotically Optimal Change Point Detection for Composite Hypothesis in State Space Models](https://arxiv.org/abs/1906.03416v1) | 1906.03416v1 | 6 |
| 2019-06-05 | [Ensemble MCMC: Accelerating Pseudo-Marginal MCMC for State Space Models using the Ensemble Kalman Filter](https://arxiv.org/abs/1906.02014v2) | 1906.02014v2 | 6 |
| 2019-03-06 | [Autoregressive Convolutional Recurrent Neural Network for Univariate and Multivariate Time Series Prediction](https://arxiv.org/abs/1903.02540v1) | 1903.02540v1 | 7 |
| 2019-02-27 | [Efficient Bayesian inference for nonlinear state space models with univariate autoregressive state equation](https://arxiv.org/abs/1902.10412v3) | 1902.10412v3 | 6 |
| 2019-02-19 | [Identifying nonlinear dynamical systems via generative recurrent neural networks with applications to fMRI](https://arxiv.org/abs/1902.07186v2) | 1902.07186v2 | 7 |
| 2019-01-31 | [A dynamic factor model approach to incorporate Big Data in state space models for official statistics](https://arxiv.org/abs/1901.11355v2) | 1901.11355v2 | 6 |
| 2019-01-29 | [Stochastic Gradient MCMC for Nonlinear State Space Models](https://arxiv.org/abs/1901.10568v3) | 1901.10568v3 | 6 |
| 2019-01-29 | [Comprehensive Evaluation of Deep Learning Architectures for Prediction of DNA/RNA Sequence Binding Specificities](https://arxiv.org/abs/1901.10526v1) | 1901.10526v1 | 6 |
| 2019-01-23 | [Recurrent Neural Filters: Learning Independent Bayesian Filtering Steps for Time Series Prediction](https://arxiv.org/abs/1901.08096v6) | 1901.08096v6 | 7 |
| 2019-01-03 | [Learning Nonlinear State Space Models with Hamiltonian Sequential Monte Carlo Sampler](https://arxiv.org/abs/1901.00862v1) | 1901.00862v1 | 6 |

### 2018
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2018-11-16 | [Equilibrium Distributions and Stability Analysis of Gaussian Process State Space Models](https://arxiv.org/abs/1811.06653v1) | 1811.06653v1 | 8 |
| 2018-11-16 | [Stability of Gaussian Process State Space Models](https://arxiv.org/abs/1811.06646v1) | 1811.06646v1 | 6 |
| 2018-10-22 | [Stochastic Gradient MCMC for State Space Models](https://arxiv.org/abs/1810.09098v2) | 1810.09098v2 | 6 |
| 2018-08-01 | [A Linear State Space Model for Photoacoustic Imaging in an Acoustic Attenuating Media](https://arxiv.org/abs/1808.00218v1) | 1808.00218v1 | 6 |
| 2018-07-31 | [Implementation of Smart Contracts Using Hybrid Architectures with On- and Off-Blockchain Components](https://arxiv.org/abs/1808.00093v1) | 1808.00093v1 | 6 |
| 2018-07-18 | [Streaming Video QoE Modeling and Prediction: A Long Short-Term Memory Approach](https://arxiv.org/abs/1807.07126v1) | 1807.07126v1 | 6 |
| 2018-07-06 | [Bayesian State Space Modeling of Physical Processes in Industrial Hygiene](https://arxiv.org/abs/1807.02228v1) | 1807.02228v1 | 6 |
| 2018-06-12 | [Deep State Space Models for Unconditional Word Generation](https://arxiv.org/abs/1806.04550v2) | 1806.04550v2 | 6 |
| 2018-05-30 | [Introducing shrinkage in heavy-tailed state space models to predict equity excess returns](https://arxiv.org/abs/1805.12217v2) | 1805.12217v2 | 6 |
| 2018-05-23 | [Scalable Bayesian Learning for State Space Models using Variational Inference with SMC Samplers](https://arxiv.org/abs/1805.09406v3) | 1805.09406v3 | 6 |
| 2018-05-08 | [A Regression Model of Recurrent Deep Neural Networks for Noise Robust Estimation of the Fundamental Frequency Contour of Speech](https://arxiv.org/abs/1805.02958v1) | 1805.02958v1 | 7 |
| 2018-05-02 | [Robust Particle Density Tempering for State Space Models](https://arxiv.org/abs/1805.00649v3) | 1805.00649v3 | 6 |
| 2018-04-12 | [The Correlated Particle Hybrid Sampler for State Space Models](https://arxiv.org/abs/1804.04359v4) | 1804.04359v4 | 6 |
| 2018-02-21 | [Data-Driven Forecasting of High-Dimensional Chaotic Systems with Long Short-Term Memory Networks](https://arxiv.org/abs/1802.07486v5) | 1802.07486v5 | 6 |
| 2018-01-24 | [Gaussian variational approximation for high-dimensional state space models](https://arxiv.org/abs/1801.07873v3) | 1801.07873v3 | 6 |
| 2018-01-03 | [Gated Recurrent Networks for Seizure Detection](https://arxiv.org/abs/1801.02471v1) | 1801.02471v1 | 7 |

### 2017
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2017-12-24 | [Efficient data augmentation techniques for some classes of state space models](https://arxiv.org/abs/1712.08887v3) | 1712.08887v3 | 6 |
| 2017-12-22 | [Quasi-maximum likelihood estimation for cointegrated continuous-time state space models observed at low frequencies](https://arxiv.org/abs/1712.08665v2) | 1712.08665v2 | 6 |
| 2017-12-22 | [Music Genre Classification with Paralleling Recurrent Convolutional Neural Network](https://arxiv.org/abs/1712.08370v1) | 1712.08370v1 | 7 |
| 2017-09-26 | [Tensor network subspace identification of polynomial state space models](https://arxiv.org/abs/1709.08773v1) | 1709.08773v1 | 6 |
| 2017-09-22 | [Approximate Bayesian Inference in Linear State Space Models for Intermittent Demand Forecasting at Scale](https://arxiv.org/abs/1709.07638v1) | 1709.07638v1 | 7 |
| 2017-09-19 | [Aspect-Based Relational Sentiment Analysis Using a Stacked Neural Network Architecture](https://arxiv.org/abs/1709.06309v1) | 1709.06309v1 | 6 |
| 2017-08-24 | [State Space Modeling of Inverter Based Microgrids Considering Distributed Secondary Voltage Control](https://arxiv.org/abs/1708.07501v1) | 1708.07501v1 | 6 |
| 2017-08-12 | [Classical Music Composition Using State Space Models](https://arxiv.org/abs/1708.03822v2) | 1708.03822v2 | 6 |
| 2017-05-30 | [Identification of Gaussian Process State Space Models](https://arxiv.org/abs/1705.10888v2) | 1705.10888v2 | 8 |
| 2017-05-24 | [Stochastic Sequential Neural Networks with Structured Inference](https://arxiv.org/abs/1705.08695v1) | 1705.08695v1 | 6 |
| 2017-05-03 | [A Hybrid Architecture for Multi-Party Conversational Systems](https://arxiv.org/abs/1705.01214v2) | 1705.01214v2 | 6 |
| 2017-04-10 | [Multiscale Bayesian State Space Model for Granger Causality Analysis of Brain Signal](https://arxiv.org/abs/1704.02778v2) | 1704.02778v2 | 6 |
| 2017-04-03 | [Analysis, detection and correction of misspecified discrete time state space models](https://arxiv.org/abs/1704.00587v1) | 1704.00587v1 | 6 |
| 2017-02-10 | [Substrate engineering for high quality emission of free and localized excitons from atomic monolayers in hybrid architectures](https://arxiv.org/abs/1702.03251v1) | 1702.03251v1 | 6 |
| 2017-02-08 | [A Hybrid Convolutional Variational Autoencoder for Text Generation](https://arxiv.org/abs/1702.02390v1) | 1702.02390v1 | 6 |

### 2016
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2016-12-23 | [A State Space Approach for Piecewise-Linear Recurrent Neural Networks for Reconstructing Nonlinear Dynamics from Neural Measurements](https://arxiv.org/abs/1612.07846v1) | 1612.07846v1 | 7 |
| 2016-12-21 | [Bayesian Inference for State Space Models using Block and Correlated Pseudo Marginal Methods](https://arxiv.org/abs/1612.07072v1) | 1612.07072v1 | 6 |
| 2016-12-06 | [KFAS: Exponential Family State Space Models in R](https://arxiv.org/abs/1612.01907v2) | 1612.01907v2 | 6 |
| 2016-11-09 | [Channel Estimation for Hybrid Architecture Based Wideband Millimeter Wave Systems](https://arxiv.org/abs/1611.03046v2) | 1611.03046v2 | 6 |
| 2016-10-26 | [Nonparametric Dynamic State Space Modeling of Observed Circular Time Series with Circular Latent States: A Bayesian Perspective](https://arxiv.org/abs/1610.08367v2) | 1610.08367v2 | 6 |
| 2016-09-30 | [Structured Inference Networks for Nonlinear State Space Models](https://arxiv.org/abs/1609.09869v2) | 1609.09869v2 | 8 |
| 2016-09-29 | [Empirical Evaluation of RNN Architectures on Sentence Classification Task](https://arxiv.org/abs/1609.09171v2) | 1609.09171v2 | 6 |
| 2016-09-07 | [Algebraic Tools for the Analysis of State Space Models](https://arxiv.org/abs/1609.07985v1) | 1609.07985v1 | 6 |
| 2016-07-19 | [FPGA based hybrid architecture for parallelizing RRT](https://arxiv.org/abs/1607.05704v1) | 1607.05704v1 | 6 |
| 2016-06-24 | [Standard State Space Models of Unawareness (Extended Abstract)](https://arxiv.org/abs/1606.07520v1) | 1606.07520v1 | 6 |
| 2016-06-16 | [Inversion Copulas from Nonlinear State Space Models](https://arxiv.org/abs/1606.05022v2) | 1606.05022v2 | 6 |
| 2016-06-06 | [Deep Linear Discriminant Analysis on Fisher Networks: A Hybrid Architecture for Person Re-identification](https://arxiv.org/abs/1606.01595v1) | 1606.01595v1 | 6 |
| 2016-05-27 | [On the two-filter approximations of marginal smoothing distributions in general state space models](https://arxiv.org/abs/1605.08534v1) | 1605.08534v1 | 6 |
| 2016-05-24 | [Sequential Neural Models with Stochastic Layers](https://arxiv.org/abs/1605.07571v2) | 1605.07571v2 | 6 |
| 2016-05-20 | [Deep Variational Bayes Filters: Unsupervised Learning of State Space Models from Raw Data](https://arxiv.org/abs/1605.06432v3) | 1605.06432v3 | 6 |
| 2016-05-17 | [Deep Action Sequence Learning for Causal Shape Transformation](https://arxiv.org/abs/1605.05368v3) | 1605.05368v3 | 6 |
| 2016-05-02 | [Hybrid Architectures with Few-Bit ADC Receivers: Achievable Rates and Energy-Rate Tradeoffs](https://arxiv.org/abs/1605.00668v2) | 1605.00668v2 | 6 |
| 2016-04-27 | [Auxiliary Likelihood-Based Approximate Bayesian Computation in State Space Models](https://arxiv.org/abs/1604.07949v3) | 1604.07949v3 | 6 |
| 2016-04-02 | [State Space Model based Trust Evaluation over Wireless Sensor Networks: An Iterative Particle Filter Approach](https://arxiv.org/abs/1604.00478v2) | 1604.00478v2 | 6 |
| 2016-03-17 | [Multi-Hop Cluster based IEEE 802.11p and LTE Hybrid Architecture for VANET Safety Message Dissemination](https://arxiv.org/abs/1603.05628v1) | 1603.05628v1 | 6 |
| 2016-03-17 | [A flexible state space model for learning nonlinear dynamical systems](https://arxiv.org/abs/1603.05486v2) | 1603.05486v2 | 6 |
| 2016-02-19 | [Sampling latent states for high-dimensional non-linear state space models with the embedded HMM method](https://arxiv.org/abs/1602.06030v2) | 1602.06030v2 | 6 |

### 2015
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2015-10-16 | [Optimizing and Contrasting Recurrent Neural Network Architectures](https://arxiv.org/abs/1510.04953v1) | 1510.04953v1 | 7 |
| 2015-10-02 | [Nonlinear State Space Model Identification Using a Regularized Basis Function Expansion](https://arxiv.org/abs/1510.00563v1) | 1510.00563v1 | 6 |
| 2015-06-10 | [Neural Adaptive Sequential Monte Carlo](https://arxiv.org/abs/1506.03338v3) | 1506.03338v3 | 6 |
| 2015-06-07 | [Computationally Efficient Bayesian Learning of Gaussian Process State Space Models](https://arxiv.org/abs/1506.02267v2) | 1506.02267v2 | 6 |
| 2015-02-12 | [Newton-based maximum likelihood estimation in nonlinear state space models](https://arxiv.org/abs/1502.03655v2) | 1502.03655v2 | 6 |
| 2015-01-26 | [Granger causality for state space models](https://arxiv.org/abs/1501.06502v2) | 1501.06502v2 | 6 |

### 2014
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2014-09-30 | [Approximate Bayesian Computation in State Space Models](https://arxiv.org/abs/1409.8363v1) | 1409.8363v1 | 6 |
| 2014-08-20 | [Sequential Bayesian inference for static parameters in dynamic state space models](https://arxiv.org/abs/1408.4559v2) | 1408.4559v2 | 6 |
| 2014-08-13 | [Bayesian Nonparametric Dynamic State Space Modeling with Circular Latent States](https://arxiv.org/abs/1408.3041v2) | 1408.3041v2 | 6 |
| 2014-02-04 | [Particle Metropolis adjusted Langevin algorithms for state space models](https://arxiv.org/abs/1402.0694v2) | 1402.0694v2 | 6 |

<!-- table:end papers -->
