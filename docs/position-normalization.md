# 🧱 位置编码与归一化（Position & Normalization）

> 位置怎么编、层怎么稳：决定模型能外推多远、能堆多深。

注意力本身不含顺序信息，残差堆叠又带来训练稳定性问题。这条赛道收录两类"地基模块"：
位置编码（正弦/可学习/相对/旋转/线性偏置）与归一化（LayerNorm/RMSNorm、Pre-LN 与 Post-LN 之争）。
它们不性感，但每一次上下文长度外推、每一次加深层数，背后都是这两类模块的改进。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Batch Normalization: Accelerating Deep Network Training by Reducing Internal Covariate Shift | [1502.03167](https://arxiv.org/abs/1502.03167) | 2015 | 归一化思路的前身，理解 LayerNorm 的起点 |
| Highway Networks | [1505.00387](https://arxiv.org/abs/1505.00387) | 2015 | 门控直通路径：残差连接的直接前身 |
| Deep Residual Learning for Image Recognition | [1512.03385](https://arxiv.org/abs/1512.03385) | 2015 | ResNet：残差流成为可堆叠深度模块的地基 |
| Layer Normalization | [1607.06450](https://arxiv.org/abs/1607.06450) | 2016 | 层归一化，Transformer 稳定训练的起点 |
| Root Mean Square Layer Normalization | [1910.07467](https://arxiv.org/abs/1910.07467) | 2019 | RMSNorm：去掉均值中心化，更快且几乎不掉点 |
| On Layer Normalization in the Transformer Architecture | [2002.04745](https://arxiv.org/abs/2002.04745) | 2020 | Pre-LN vs Post-LN 的经典分析，现在大家都用 Pre-LN |
| RoFormer: Enhanced Transformer with Rotary Position Embedding | [2104.09864](https://arxiv.org/abs/2104.09864) | 2021 | RoPE：用旋转编码把相对位置写进 QK 内积，当代 LLM 事实标准 |
| Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation | [2108.12409](https://arxiv.org/abs/2108.12409) | 2021 | ALiBi：给注意力加线性距离惩罚，短训长推 |
| DeepNet: Scaling Transformers to 1,000 Layers | [2203.00555](https://arxiv.org/abs/2203.00555) | 2022 | DeepNorm：把 Transformer 堆到 1000 层的归一化手术 |
| YaRN: Efficient Context Window Extension of Large Language Models | [2309.00071](https://arxiv.org/abs/2309.00071) | 2023 | RoPE 频率插值改进，上下文窗口扩展的主流做法 |
| GLU Variants Improve Transformer | [2002.05202](https://arxiv.org/abs/2002.05202) | 2020 | （跨赛道）SwiGLU 等门控 FFN，也常与归一化调整一起讨论 |

## 相关实现

- [lucidrains/rotary-embedding-torch](https://github.com/lucidrains/rotary-embedding-torch) — 独立可插拔的 RoPE 实现。
- [ofirpress/attention_with_linear_biases](https://github.com/ofirpress/attention_with_linear_biases) — ALiBi 官方代码。

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-09 | [A Geometric Invariant of Attention Predicts Head Specialization from Weights Alone](https://arxiv.org/abs/2611.12206v1) | 2611.12206v1 | 8 |
| 2026-11-06 | [Query-Guided RoPE Modulation for Lost-in-the-Middle Mitigation in Long-Context LLMs](https://arxiv.org/abs/2611.09554v1) | 2611.09554v1 | 12 |
| 2026-11-05 | [How Deep is the Signal? Time-Context up to 30 Years for Colorectal Cancer Prediction in a Primary-Care EHR Model](https://arxiv.org/abs/2611.07265v1) | 2611.07265v1 | 0 |
| 2026-11-04 | [RDT-3D: Resolution-Decoupled Training for High-Fidelity 3D Geometry Generation](https://arxiv.org/abs/2611.06141v1) | 2611.06141v1 | 0 |
| 2026-11-04 | [Ray-Tracing-Based Dynamic Channel Sounding With Autoregressive Wi-Fi CSI Prediction](https://arxiv.org/abs/2611.05970v1) | 2611.05970v1 | 0 |
| 2026-11-03 | [Positional Encoding is All You Need for Scalable Equivariance Constraint Relaxation](https://arxiv.org/abs/2611.05041v1) | 2611.05041v1 | 6 |
| 2026-11-02 | [In-context learning of solution to simple linear regression task using transformer with masked linear self-attention](https://arxiv.org/abs/2611.02817v1) | 2611.02817v1 | 0 |
| 2026-11-01 | [Causal Optimal-Transport Attention: Positional Priors and Length Extrapolation](https://arxiv.org/abs/2611.01472v1) | 2611.01472v1 | 6 |
| 2026-11-01 | [Causal Optimal-Transport Attention: Positional Priors and Length Extrapolation](https://arxiv.org/abs/2611.01472v2) | 2611.01472v2 | 10 |
| 2026-10-27 | [Rethinking Positional Encoding and Interaction Granularity for CTR Prediction](https://arxiv.org/abs/2610.37140v1) | 2610.37140v1 | 6 |
| 2026-10-25 | [Wave Is All You Need: A Quantum Language Model Based on Fully Connected Quantum Boltzmann Machine](https://arxiv.org/abs/2610.34492v1) | 2610.34492v1 | 0 |
| 2026-10-23 | [Where Rounding Happens Matters: Rounding-Location Alignment Stabilizes LLM Reinforcement Learning](https://arxiv.org/abs/2610.32951v1) | 2610.32951v1 | 0 |
| 2026-10-21 | [BrainCodes: A Lightweight EEG Foundation Model over Discrete Neural Codes](https://arxiv.org/abs/2610.29320v1) | 2610.29320v1 | 0 |
| 2026-10-20 | [HRoPE: Homography Relative Positional Encoding](https://arxiv.org/abs/2610.28284v1) | 2610.28284v1 | 12 |
| 2026-10-20 | [When Does Sharing Work? Scaling a Shared SigLIP2 Across Image, Video, Audio, and Audio-Visual Representations](https://arxiv.org/abs/2611.05406v1) | 2611.05406v1 | 0 |
| 2026-10-20 | [Scaling Graph Reasoning in Language Models with Learnable Graph Positional Encodings](https://arxiv.org/abs/2610.27439v2) | 2610.27439v2 | 6 |
| 2026-10-15 | [PACE: Pareto-Adaptive Compression for Efficient Native MLLMs](https://arxiv.org/abs/2610.24005v3) | 2610.24005v3 | 0 |
| 2026-10-15 | [Activation-Adjacent Layer Normalization: Effects on Approximation Power](https://arxiv.org/abs/2610.21527v1) | 2610.21527v1 | 6 |
| 2026-10-15 | [DuET: Note-Frame Dual Encoding for Piano Performance-to-Score Transcription](https://arxiv.org/abs/2610.21467v1) | 2610.21467v1 | 0 |
| 2026-10-15 | [Compression Does Not End at Selection: Post-Selection Positional Geometry for Sparse KV Caches](https://arxiv.org/abs/2610.21126v1) | 2610.21126v1 | 0 |
| 2026-10-14 | [Coordi-pi: Coordination-Aware Dual-Hand Action Representation for Bimanual Dexterous Manipulation](https://arxiv.org/abs/2610.19753v1) | 2610.19753v1 | 0 |
| 2026-10-14 | [Beyond Static Positional Encoding: Bayesian Time-aware Attention for Non-Stationary Long-term Time Series Forecasting](https://arxiv.org/abs/2610.19603v1) | 2610.19603v1 | 6 |
| 2026-10-14 | [Asymptotic Behavior of Transformers](https://arxiv.org/abs/2610.19358v1) | 2610.19358v1 | 0 |
| 2026-10-13 | [ShoeFit: A New Dataset and Dual-image-stream DiT Framework for Virtual Footwear Try-On](https://arxiv.org/abs/2610.18325v1) | 2610.18325v1 | 0 |
| 2026-10-13 | [LensErase: A Foundation Model for Erase Anything](https://arxiv.org/abs/2610.18072v1) | 2610.18072v1 | 0 |
| 2026-10-13 | [Persistence Positional Encoding: A Minimal Transformer Recipe for Persistence Diagrams](https://arxiv.org/abs/2610.17848v1) | 2610.17848v1 | 6 |
| 2026-10-12 | [Counting with Attention and LayerNorm: Norm Scaling and Representation Geometry](https://arxiv.org/abs/2610.16653v1) | 2610.16653v1 | 0 |
| 2026-10-12 | [WorldRoPE: Probabilistic World-Centric Rotary Embedding for Multi-View Attention](https://arxiv.org/abs/2610.16337v1) | 2610.16337v1 | 6 |
| 2026-10-12 | [FON: A Draft-Revise Dual-Organ Language Model without Sequence-Level Quadratic Attention](https://arxiv.org/abs/2610.16301v1) | 2610.16301v1 | 0 |
| 2026-10-09 | [Chronos Policy: Learning Robot Policies on Physical Time](https://arxiv.org/abs/2610.13929v1) | 2610.13929v1 | 0 |
| 2026-10-07 | [HySPE: Positional Encoding via Symplectic Dual Shears](https://arxiv.org/abs/2610.10154v1) | 2610.10154v1 | 6 |
| 2026-10-06 | [LayerRoPE: Dynamic Depth-wise Magnitude & Angular Superposition](https://arxiv.org/abs/2610.09179v1) | 2610.09179v1 | 6 |
| 2026-10-06 | [Algorithmic Scratchpads and Curriculum Staging for Arithmetic Reasoning in Tiny Transformers](https://arxiv.org/abs/2610.09003v1) | 2610.09003v1 | 0 |
| 2026-10-06 | [Dynamic Positional Attention Modulation for Parameter-Efficient Fine-Tuning of Large Language Models](https://arxiv.org/abs/2610.07848v1) | 2610.07848v1 | 0 |
| 2026-10-03 | [WavePrune: One period is often enough for RoPE](https://arxiv.org/abs/2610.06963v1) | 2610.06963v1 | 6 |
| 2026-10-03 | [Length Generalization Needs Proper Regularization](https://arxiv.org/abs/2610.04518v1) | 2610.04518v1 | 6 |
| 2026-10-02 | [Feedforward Novel View Synthesis for Heterogeneous Cameras](https://arxiv.org/abs/2610.03522v1) | 2610.03522v1 | 0 |
| 2026-10-02 | [Improving Atomic-Fact Recall via Focused Views in Unstructured Knowledge Editing](https://arxiv.org/abs/2610.02772v1) | 2610.02772v1 | 0 |
| 2026-10-01 | [Higher-Order Positional Encodings for Graph Representation Learning](https://arxiv.org/abs/2610.01903v1) | 2610.01903v1 | 6 |
| 2026-09-30 | [EFormer: Temporally Aligned Local Correction for Continuous sEMG-Based Hand Pose Tracking](https://arxiv.org/abs/2609.38932v1) | 2609.38932v1 | 0 |
| 2026-09-30 | [Scaling Parameter and Context in Attention: Native Sparse Attention from Mixture-of-Head](https://arxiv.org/abs/2609.38832v1) | 2609.38832v1 | 0 |
| 2026-09-29 | [Shifting Mechanisms: How Positional Encoding Choice Shapes In-Context Retrieval](https://arxiv.org/abs/2609.38530v1) | 2609.38530v1 | 6 |
| 2026-09-29 | [MUGEN: Interactive Panoramic World Exploration via Camera Control](https://arxiv.org/abs/2609.38077v1) | 2609.38077v1 | 0 |
| 2026-09-29 | [Delta-Matching: Closing the Final Gap of Native 8-bit Training for LLMs](https://arxiv.org/abs/2609.37852v2) | 2609.37852v2 | 0 |
| 2026-09-29 | [Aperture: Merge-Consistent Rotary States for Compressed Tokens](https://arxiv.org/abs/2609.36781v1) | 2609.36781v1 | 0 |
| 2026-09-29 | [Bits Under ZK-LLM: Evaluating Zero-Knowledge-Friendly Quantization for Verifiable Private LLM Inference](https://arxiv.org/abs/2609.36437v1) | 2609.36437v1 | 0 |
| 2026-09-28 | [Physical Cross-Modal Masked Autoencoding for Seismic-to-Well Representation Learning](https://arxiv.org/abs/2609.36193v1) | 2609.36193v1 | 0 |
| 2026-09-28 | [Dual-Stream Simultaneous Translation via 2D Grid Attention](https://arxiv.org/abs/2609.34902v1) | 2609.34902v1 | 0 |
| 2026-09-28 | [DirectUV: Image-Conditioned UV Texture Generation with Surface-Aware Positional Encoding](https://arxiv.org/abs/2609.34651v2) | 2609.34651v2 | 6 |
| 2026-09-28 | [RoPE is Dead, Long Live RoPE: Towards Scalable Data-aware Positional Encodings](https://arxiv.org/abs/2609.34556v2) | 2609.34556v2 | 12 |
| 2026-09-27 | [MinkowskiPE: Minkowski Positional Encoding for Spatiotemporal Perception](https://arxiv.org/abs/2609.33804v1) | 2609.33804v1 | 6 |
| 2026-09-26 | [How Vision Transformers Represent Position: A Mechanistic Comparison of Absolute and Rotary Positional Encodings](https://arxiv.org/abs/2610.13992v1) | 2610.13992v1 | 6 |
| 2026-09-26 | [Analytic-Walk Rotary Positional Encodings for Graphs](https://arxiv.org/abs/2609.32178v1) | 2609.32178v1 | 6 |
| 2026-09-25 | [MoSAR: Mixture of Semantic Attention Regimes for Learning Adaptive and Approximable Attention Geometries](https://arxiv.org/abs/2609.31261v1) | 2609.31261v1 | 0 |
| 2026-09-24 | [T-RoPE: Time-Aware Rotary Position Embedding for Sequential Recommendation](https://arxiv.org/abs/2609.30576v1) | 2609.30576v1 | 15 |
| 2026-09-23 | [hyperbolix: Hyperbolic Deep Learning in JAX](https://arxiv.org/abs/2609.28248v2) | 2609.28248v2 | 0 |
| 2026-09-20 | [Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms](https://arxiv.org/abs/2609.23658v1) | 2609.23658v1 | 0 |
| 2026-09-20 | [Paragraph Boundaries Are Not White Space:Compression Depth as the Signature of Hierarchical Structure](https://arxiv.org/abs/2609.23551v2) | 2609.23551v2 | 0 |
| 2026-09-16 | [Mask IPL: Noise-Free Intrinsic Position Learning via Computation Graph Clipping for Event-Based Spike-Driven Tracking](https://arxiv.org/abs/2609.18716v1) | 2609.18716v1 | 0 |
| 2026-09-16 | [The Drift Contract: Spectral Updates for Depth-Robust Local Learning](https://arxiv.org/abs/2609.26811v1) | 2609.26811v1 | 0 |
| 2026-09-15 | [SPEAR NeXT Causal Latent Forecasting Across Multiple Horizons for Spectral Temporal Earth Representation Learning](https://arxiv.org/abs/2609.16871v1) | 2609.16871v1 | 0 |
| 2026-09-13 | [Depth and Scale in the Sub-150M Regime: JugnuLM-53M vs JugnuLM-110M](https://arxiv.org/abs/2609.14715v1) | 2609.14715v1 | 0 |
| 2026-09-11 | [AttnFuse: A Composable DSL for Compiling Attentions to Fused GPU Kernels](https://arxiv.org/abs/2609.13612v1) | 2609.13612v1 | 0 |
| 2026-09-10 | [Distance generalization in transformers: why bother with positional encoding?](https://arxiv.org/abs/2609.11913v1) | 2609.11913v1 | 6 |
| 2026-09-07 | [MeRoTune: RoPE-Safe Merging with a Tunable Dial](https://arxiv.org/abs/2609.07971v1) | 2609.07971v1 | 6 |
| 2026-09-07 | [RelightFormer: Feed-forward Generative Transformer for Multiview Object Relighting](https://arxiv.org/abs/2609.07414v1) | 2609.07414v1 | 0 |
| 2026-09-07 | [Content-Based Addressing for Long Context](https://arxiv.org/abs/2609.07314v2) | 2609.07314v2 | 0 |
| 2026-09-06 | [RoLA: Rotary-Positioned Low-Rank Linear Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2609.06712v3) | 2609.06712v3 | 0 |
| 2026-09-04 | [UniMate: One Unified Model to Animate Diverse Skeletons](https://arxiv.org/abs/2609.05415v1) | 2609.05415v1 | 0 |
| 2026-09-01 | [MeRoPE: Metric Rotary Position Embedding for Camera-Controlled Video Generation](https://arxiv.org/abs/2609.01252v1) | 2609.01252v1 | 15 |
| 2026-08-31 | [Converse and Collision-Based Achievability for Node Localization with Hybrid Distance-Spectral Graph Positional Encodings](https://arxiv.org/abs/2608.30152v1) | 2608.30152v1 | 6 |
| 2026-08-30 | [Higher-Dimensional Rotary Position Embedding](https://arxiv.org/abs/2608.29715v1) | 2608.29715v1 | 9 |
| 2026-08-24 | [Sigmoid Attention as a Better Substrate for Learned KV Cache Eviction](https://arxiv.org/abs/2608.23296v1) | 2608.23296v1 | 0 |
| 2026-08-23 | [HeatTok: Enhancing Remote Sensing Image Understanding via Thermodiffusion-based Tokenization](https://arxiv.org/abs/2608.22485v1) | 2608.22485v1 | 0 |
| 2026-08-15 | [Do Geometry-Aware Positional Encodings Help Transformers in Spatial Imperfect-Information Games?](https://arxiv.org/abs/2608.14982v1) | 2608.14982v1 | 6 |
| 2026-08-12 | [Disentangling the Expressivity of RoPE](https://arxiv.org/abs/2608.11909v1) | 2608.11909v1 | 6 |
| 2026-08-12 | [Chain-of-Thought Shows the Path to a Tree: Realizing Branching Complexity](https://arxiv.org/abs/2608.11716v1) | 2608.11716v1 | 8 |
| 2026-08-10 | [ZetaGPT: A Reference Implementation of Positional--Encoding--Free State--Space--Attention Language Models](https://arxiv.org/abs/2608.09432v1) | 2608.09432v1 | 8 |
| 2026-08-10 | [Why Post-Norm Transformers Collapse: Attention Amplification and Gradient Repair Failure](https://arxiv.org/abs/2608.09417v2) | 2608.09417v2 | 16 |
| 2026-08-10 | [SwiftQK: Fast and Communication-Efficient Tensor Parallelism for Query-Key Normalization](https://arxiv.org/abs/2608.09160v1) | 2608.09160v1 | 8 |
| 2026-08-09 | [Position Encoding in Transformers: From Absolute and Relative Methods to Rotary Position Embeddings and Long-Context Scaling](https://arxiv.org/abs/2608.10021v1) | 2608.10021v1 | 17 |
| 2026-08-07 | [ControlRef: Efficient Layout-Guided Multi-Instance Generation via Anchored 4D-RoPE](https://arxiv.org/abs/2608.06878v1) | 2608.06878v1 | 10 |
| 2026-08-04 | [When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings](https://arxiv.org/abs/2608.03994v1) | 2608.03994v1 | 6 |
| 2026-08-04 | [MDLMPE: Distribution Aware Positional Encoding for Masked Diffusion Language Models](https://arxiv.org/abs/2608.03769v1) | 2608.03769v1 | 10 |
| 2026-08-03 | [ATFlash: Per-RoPE-Wavelength Attention Windows for Compute/Memory-Efficient LLM Inference](https://arxiv.org/abs/2608.02947v1) | 2608.02947v1 | 12 |
| 2026-08-03 | [Wiring Beats Blending: Structure-Aware Compensation for Transformer Downscaling](https://arxiv.org/abs/2608.02829v5) | 2608.02829v5 | 7 |
| 2026-07-30 | [EgoGenesis: Egocentric World-Action Modeling with Online Anchored Projective Memory and Action-3D RoPE](https://arxiv.org/abs/2607.28243v1) | 2607.28243v1 | 12 |
| 2026-07-30 | [Now You Have My Healthy Attention: A U-DiT for Brain-MRI Inpainting](https://arxiv.org/abs/2607.27974v2) | 2607.27974v2 | 7 |
| 2026-07-29 | [InferScale: GPU-Native KV Injection for Personalized LLM Serving](https://arxiv.org/abs/2607.27090v2) | 2607.27090v2 | 10 |
| 2026-07-29 | [Journey Operators for Structured Multi-Axis Composition](https://arxiv.org/abs/2607.26775v1) | 2607.26775v1 | 10 |
| 2026-07-29 | [ClockRoPE: Random Fourier Rotations for Temporal Routine Modeling](https://arxiv.org/abs/2607.26369v2) | 2607.26369v2 | 12 |
| 2026-07-28 | [Phase Structure in Rotary Attention: A Spectral Framework for Semantic Continuity and Execution-Boundary Governance](https://arxiv.org/abs/2607.25507v2) | 2607.25507v2 | 10 |
| 2026-07-27 | [CameraAnything: Refilming Videos with Arbitrary Camera Control](https://arxiv.org/abs/2607.24591v1) | 2607.24591v1 | 8 |
| 2026-07-27 | [Self-Attention Dynamics with Rotary Position Embeddings: Twisted States and Explicit Consensus Rates on the Sphere](https://arxiv.org/abs/2607.24502v1) | 2607.24502v1 | 13 |
| 2026-07-27 | [Unsupervised Graph Representation Learning with Complementary View Alignment](https://arxiv.org/abs/2607.24338v1) | 2607.24338v1 | 8 |
| 2026-07-23 | [Anti-Periodic Positional Encoding: Möbius Boundary Conditions Make In-Context Retrieval Reliable](https://arxiv.org/abs/2607.21405v1) | 2607.21405v1 | 10 |
| 2026-07-21 | [Enhancing Transformer-based Routing by Encoding Distance via Relative Positional Encoding](https://arxiv.org/abs/2607.18909v1) | 2607.18909v1 | 6 |
| 2026-07-21 | [Relative Positions Generalize, Absolute Positions Memorize: An Implicit-Bias Account of Length Generalization in Attention](https://arxiv.org/abs/2607.18759v1) | 2607.18759v1 | 6 |
| 2026-07-20 | [ShotPlan: Cinematic Video Generation with Learnable Planning Token](https://arxiv.org/abs/2607.17675v1) | 2607.17675v1 | 10 |
| 2026-07-19 | [The Geometry of Semantic Space: A Continuous Geometric Framework for the Transformer Architecture](https://arxiv.org/abs/2607.17146v1) | 2607.17146v1 | 9 |
| 2026-07-19 | [Physics-Guided Masked Multi-Task Network for Edge-Friendly Battery Health Diagnostics from Sto-chastically Fragmented Charging Profiles](https://arxiv.org/abs/2607.18330v1) | 2607.18330v1 | 11 |
| 2026-07-19 | [Dynamic Loss Balancing for Joint SOH and RUL Prediction of Lithium-Ion Batteries via a Rotary SOH-Injected Prior Battery Transformer](https://arxiv.org/abs/2607.18329v1) | 2607.18329v1 | 11 |
| 2026-07-17 | [Frontier Language Models Struggle to Copy: Text Can Be Better Viewed in 2D](https://arxiv.org/abs/2607.16072v1) | 2607.16072v1 | 8 |
| 2026-07-17 | [In-context learning of closed form solution to simple linear regression task using transformer with linear self-attention](https://arxiv.org/abs/2607.15819v1) | 2607.15819v1 | 8 |
| 2026-07-15 | [2D Rotary Position Embedding for Scene Text Recognition with Transformers](https://arxiv.org/abs/2607.13458v1) | 2607.13458v1 | 17 |
| 2026-07-14 | [What Does a Temporal Benchmark Score Measure? Decomposing Channel Use in Video VLM Evaluation](https://arxiv.org/abs/2607.12304v1) | 2607.12304v1 | 8 |
| 2026-07-12 | [Contrastive Joint-Embedding Prediction for Representation Learning in Structural MRI](https://arxiv.org/abs/2607.11962v1) | 2607.11962v1 | 8 |
| 2026-07-11 | [LeRoPE: Learnable RoPE Frequencies Improve Language Modeling](https://arxiv.org/abs/2607.10134v1) | 2607.10134v1 | 10 |
| 2026-07-09 | [Attention Degradation, Function Token Anchoring, and the Limits of Attention-Based Intervention in Large Language Models](https://arxiv.org/abs/2607.20524v1) | 2607.20524v1 | 8 |
| 2026-07-08 | [How Data Shapes RoPE Frequency Usage: From Positional Scale Matching to Length Generalization](https://arxiv.org/abs/2607.07678v1) | 2607.07678v1 | 12 |
| 2026-07-08 | [Eigenbasis-Independent Learnable Spectral Positional Encodings for Directed Graphs via Hermitian Block Krylov Subspaces](https://arxiv.org/abs/2607.07032v2) | 2607.07032v2 | 6 |
| 2026-07-02 | [EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$](https://arxiv.org/abs/2607.02479v1) | 2607.02479v1 | 8 |
| 2026-07-01 | [The Wiola Architecture for Efficient Small Language Models](https://arxiv.org/abs/2607.01394v1) | 2607.01394v1 | 8 |
| 2026-07-01 | [Nexus: Depth-Adaptive KV-Cache Splicing and Retrieval-Decoupled Tool Routing for Agentic LLMs on Unified Memory](https://arxiv.org/abs/2608.20397v1) | 2608.20397v1 | 10 |
| 2026-07-01 | [RotateAttention: RoPE-Aware Rotation and Range Rectification for INT4 Quantized Attention in Video Generation](https://arxiv.org/abs/2607.02584v2) | 2607.02584v2 | 12 |
| 2026-06-30 | [SpheRoPE: Zero-Shot Optimization-Free 360 Panorama Generation with Spherical RoPE](https://arxiv.org/abs/2606.32033v1) | 2606.32033v1 | 12 |
| 2026-06-30 | [Signed-Permutation Coordinate Transport for RMSNorm Transformers](https://arxiv.org/abs/2606.31963v1) | 2606.31963v1 | 7 |
| 2026-06-30 | [Review Residuals: Update-Conditioned Residual Gating for Transformers](https://arxiv.org/abs/2606.31859v1) | 2606.31859v1 | 9 |
| 2026-06-30 | [DPPE: Rethinking Camera-Based Positional Encoding for Scaling Multi-View Transformers](https://arxiv.org/abs/2606.31585v2) | 2606.31585v2 | 6 |
| 2026-06-30 | [Scaling Storm-Resolving Atmospheric AI Simulation to the Entire Planet](https://arxiv.org/abs/2606.31248v1) | 2606.31248v1 | 10 |
| 2026-06-29 | [Hierarchical Global Attention (HGA)](https://arxiv.org/abs/2606.30709v1) | 2606.30709v1 | 8 |
| 2026-06-28 | [Dead-Direction Conditioners: Gauge-Equivariant Preconditioning for Deep Networks](https://arxiv.org/abs/2606.29176v1) | 2606.29176v1 | 8 |
| 2026-06-26 | [Mitigating Position Bias in Transformers via Layer-Specific Positional Embedding Scaling](https://arxiv.org/abs/2606.27705v1) | 2606.27705v1 | 10 |
| 2026-06-25 | [RoPEMover: Depth-Aware Object Relocation via Positional Embeddings](https://arxiv.org/abs/2606.27332v1) | 2606.27332v1 | 6 |
| 2026-06-24 | [Communicability-Inspired Positional Encoding (CIPE)](https://arxiv.org/abs/2606.25293v1) | 2606.25293v1 | 6 |
| 2026-06-23 | [G$^3$VLA: Geometric Inductive Bias for Vision-Language-Action Models](https://arxiv.org/abs/2606.24472v2) | 2606.24472v2 | 8 |
| 2026-06-23 | [Block-GTQ: RoPE-Block Rate Allocation for KV-Cache Quantization](https://arxiv.org/abs/2606.24033v2) | 2606.24033v2 | 12 |
| 2026-06-22 | [OrthoMotion:Disentangling Camera and Subject Motion via Geometry Semantics Orthogonal Attention](https://arxiv.org/abs/2606.22835v1) | 2606.22835v1 | 10 |
| 2026-06-19 | [Soliton-like Waves in a Two-Dimensional Recurrent Spiking Neural Network with Weighted Spike-Timing-Dependent Plasticity](https://arxiv.org/abs/2606.21432v1) | 2606.21432v1 | 6 |
| 2026-06-18 | [QG-MIL: A Gated Transformer Aggregator for Domain-Agnostic Multiple Instance Learning in Medical Imaging](https://arxiv.org/abs/2606.20027v1) | 2606.20027v1 | 8 |
| 2026-06-16 | [PAIWorld: A 3D-Consistent World Foundation Model for Robotic Manipulation](https://arxiv.org/abs/2606.18375v3) | 2606.18375v3 | 6 |
| 2026-06-16 | [Robustness of Similarity-based Positional Encoding Under Rotations: Theoretical Analysis and Experimental Validation](https://arxiv.org/abs/2606.17961v1) | 2606.17961v1 | 6 |
| 2026-06-16 | [Functional Equivalence in Attention: A Comprehensive Study with Applications to Linear Mode Connectivity](https://arxiv.org/abs/2606.17830v1) | 2606.17830v1 | 8 |
| 2026-06-16 | [MIVE: A Minimalist Integer Vector Engine for Softmax LayerNorm and RMSNorm Acceleration](https://arxiv.org/abs/2606.17781v1) | 2606.17781v1 | 8 |
| 2026-06-15 | [DreamX-World 1.0: A General-Purpose Interactive World Model](https://arxiv.org/abs/2606.16993v1) | 2606.16993v1 | 9 |
| 2026-06-15 | [Privacy from Symmetry: Orthogonally Equivariant Transformers for LLM Inference](https://arxiv.org/abs/2606.16461v1) | 2606.16461v1 | 6 |
| 2026-06-13 | [HiRo: A Compact Four-Directional Hierarchical Reservoir Token-Mixer for Efficient Image Classification](https://arxiv.org/abs/2606.15151v1) | 2606.15151v1 | 9 |
| 2026-06-12 | [Dense Supervision Is Not Enough: The Readout Blind Spot in Looped Language Models](https://arxiv.org/abs/2606.24898v1) | 2606.24898v1 | 9 |
| 2026-06-11 | [CineOrchestra: Unified Entity-Centric Conditioning for Cinematic Video Generation](https://arxiv.org/abs/2606.13768v2) | 2606.13768v2 | 8 |
| 2026-06-11 | [Understanding Truncated Positional Encodings for Graph Neural Networks](https://arxiv.org/abs/2606.13671v1) | 2606.13671v1 | 10 |
| 2026-06-11 | [Flex4DHuman: Flexible Multi-view Video Diffusion for 4D Human Reconstruction](https://arxiv.org/abs/2606.13655v2) | 2606.13655v2 | 8 |
| 2026-06-11 | [Positional Encoding in the Context of Memristor-Based Analog Computation for Automatic Speech Recognition](https://arxiv.org/abs/2606.13379v1) | 2606.13379v1 | 6 |
| 2026-06-10 | [nD-RoPE: A Generalized RoPE for n-Dimensional Position Embedding](https://arxiv.org/abs/2606.12146v1) | 2606.12146v1 | 13 |
| 2026-06-09 | [RoVE: Rotary Value Embeddings Attention for Relative Position-dependent Value Pathways](https://arxiv.org/abs/2606.11275v2) | 2606.11275v2 | 10 |
| 2026-06-09 | [Data compression for fast dimension reduction and clustering of high-dimensional discrete data](https://arxiv.org/abs/2606.10593v2) | 2606.10593v2 | 8 |
| 2026-06-08 | [Mixture-of-Experts Transformer for Automatic Modulation Recognition](https://arxiv.org/abs/2606.09085v2) | 2606.09085v2 | 10 |
| 2026-06-07 | [Inside the LLM Word Factory](https://arxiv.org/abs/2606.08562v2) | 2606.08562v2 | 8 |
| 2026-06-05 | [AdaRoPE: Not All Attention Heads Should Rotate and Scale Equally](https://arxiv.org/abs/2607.19363v3) | 2607.19363v3 | 12 |
| 2026-06-04 | [Performance Variation in Deep Reinforcement Learning](https://arxiv.org/abs/2606.06746v1) | 2606.06746v1 | 8 |
| 2026-06-03 | [Trajectory Dynamics in Language Model Hidden States Predict Human Processing Costs Beyond Surprisal](https://arxiv.org/abs/2606.05346v1) | 2606.05346v1 | 8 |
| 2026-06-03 | [Low-Rank Decay for Grokking in Scale-Invariant Transformers: A Spectral-Geometric View](https://arxiv.org/abs/2606.04405v1) | 2606.04405v1 | 6 |
| 2026-06-03 | [LazyAttention: Efficient Retrieval-Augmented Generation with Deferred Positional Encoding](https://arxiv.org/abs/2606.04302v1) | 2606.04302v1 | 6 |
| 2026-06-01 | [Forget Attention: Importance-Aware Attention Is All You Need](https://arxiv.org/abs/2606.02332v3) | 2606.02332v3 | 12 |
| 2026-06-01 | [Massive Spikes in LLMs are Bias Vectors: Mechanistic Uncovering and Spike-Free Quantization](https://arxiv.org/abs/2606.02288v1) | 2606.02288v1 | 6 |
| 2026-06-01 | [Rethinking the Role of Positional Encoding: Sliding-Window Transformers without PE Remain Turing Complete](https://arxiv.org/abs/2606.01532v2) | 2606.01532v2 | 6 |
| 2026-05-31 | [Beyond Sinusoids: A Morlet Wavelet Framework for Transformer Positional Encoding](https://arxiv.org/abs/2606.01258v1) | 2606.01258v1 | 10 |
| 2026-05-30 | [Looped Transformers with Layer Normalization Provably Learn the Power Method](https://arxiv.org/abs/2606.00605v1) | 2606.00605v1 | 6 |
| 2026-05-30 | [Harmonic: Hierarchical State Space Models for Efficient Long-Context Language Modeling](https://arxiv.org/abs/2606.24650v1) | 2606.24650v1 | 8 |
| 2026-05-28 | [Anti Mode-Collapse in Mean-Field Transformer via Auxiliary Variables](https://arxiv.org/abs/2605.30229v1) | 2605.30229v1 | 8 |
| 2026-05-28 | [Give it Space! Explicit Disentangling of Positional and Semantic Representations in Encoders](https://arxiv.org/abs/2605.30022v2) | 2605.30022v2 | 8 |
| 2026-05-28 | [Positional Encodings Anchor Spatial Structure in Vision Transformers: A Geometric Perspective on Robustness](https://arxiv.org/abs/2606.00124v1) | 2606.00124v1 | 10 |
| 2026-05-28 | [Benchmarking Positional Encoding Strategies for Transformer-Based EEG Foundation Models](https://arxiv.org/abs/2605.29754v1) | 2605.29754v1 | 6 |
| 2026-05-26 | [PRISM: Position-encoded Regressive Inverse Spectral Model for Multilayer Thin-Film Design](https://arxiv.org/abs/2605.26502v2) | 2605.26502v2 | 6 |
| 2026-05-25 | [Energy-Gated Attention and Wavelet Positional Encoding: Complementary Inductive Biases for Transformer Attention](https://arxiv.org/abs/2605.26355v1) | 2605.26355v1 | 6 |
| 2026-05-25 | [Helix4D: Complex 4D Mesh Generation](https://arxiv.org/abs/2605.26109v1) | 2605.26109v1 | 8 |
| 2026-05-24 | [Baton: Explicit Semantic Blueprints for Joint Video-Audio Generation](https://arxiv.org/abs/2605.25195v2) | 2605.25195v2 | 8 |
| 2026-05-21 | [SEGA: Spectral-Energy Guided Attention for Resolution Extrapolation in Diffusion Transformers](https://arxiv.org/abs/2605.22668v1) | 2605.22668v1 | 10 |
| 2026-05-21 | [RIG-RoPE: Relation-Stratified Multimodal Attention with Instance-Local Rotary Geometry and Representation-Aware Traversal Coordinates](https://arxiv.org/abs/2608.05154v4) | 2608.05154v4 | 10 |
| 2026-05-20 | [Weierstrass Positional Encoding for Vision Transformers](https://arxiv.org/abs/2605.23719v1) | 2605.23719v1 | 10 |
| 2026-05-20 | [RoPeSLR: 3D RoPE-driven Sparse-LowRank Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2605.20659v1) | 2605.20659v1 | 12 |
| 2026-05-19 | [TrajTok: Adaptive Spatial Tokenization for Trajectory Representation Learning](https://arxiv.org/abs/2605.20134v1) | 2605.20134v1 | 10 |
| 2026-05-19 | [A Measure-Theoretic Analysis of Reasoning in Transformers: Structural Generalization and Approximation Limits](https://arxiv.org/abs/2605.19944v2) | 2605.19944v2 | 14 |
| 2026-05-18 | [A Geometric Analysis of Sign-Magnitude Asymmetry in a ReLU + RMSNorm Block under Ternary Quantization](https://arxiv.org/abs/2605.18933v1) | 2605.18933v1 | 8 |
| 2026-05-15 | [Modeling Music as a Time-Frequency Image: A 2D Tokenizer for Music Generation](https://arxiv.org/abs/2605.15831v1) | 2605.15831v1 | 11 |
| 2026-05-15 | [HyperDiT: Hyper-Connected Transformers for High-Fidelity Pixel-Space Diffusion](https://arxiv.org/abs/2605.15741v2) | 2605.15741v2 | 10 |
| 2026-05-14 | [MetaBackdoor: Exploiting Positional Encoding as a Backdoor Attack Surface in LLMs](https://arxiv.org/abs/2605.15172v1) | 2605.15172v1 | 6 |
| 2026-05-14 | [EndPrompt: Efficient Long-Context Extension via Terminal Anchoring](https://arxiv.org/abs/2605.14589v3) | 2605.14589v3 | 10 |
| 2026-05-14 | [Enjoy Your Layer Normalization with the Computational Efficiency of RMSNorm](https://arxiv.org/abs/2605.14521v1) | 2605.14521v1 | 12 |
| 2026-05-14 | [Head Forcing: Long Autoregressive Video Generation via Head Heterogeneity](https://arxiv.org/abs/2605.14487v1) | 2605.14487v1 | 8 |
| 2026-05-13 | [VectraYX-Nano: A 42M-Parameter Spanish Cybersecurity Language Model with Curriculum Learning and Native Tool Use](https://arxiv.org/abs/2605.13989v3) | 2605.13989v3 | 8 |
| 2026-05-13 | [CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation](https://arxiv.org/abs/2605.12938v2) | 2605.12938v2 | 6 |
| 2026-05-12 | [Rethinking Positional Encoding for Neural Vehicle Routing](https://arxiv.org/abs/2605.11910v1) | 2605.11910v1 | 10 |
| 2026-05-11 | [RelFlexformer: Efficient Attention 3D-Transformers for Integrable Relative Positional Encodings](https://arxiv.org/abs/2605.10706v1) | 2605.10706v1 | 6 |
| 2026-05-11 | [TIE: Time Interval Encoding for Video Generation over Events](https://arxiv.org/abs/2605.10543v2) | 2605.10543v2 | 8 |
| 2026-05-11 | [Remember to Forget: Gated Adaptive Positional Encoding](https://arxiv.org/abs/2605.10414v2) | 2605.10414v2 | 10 |
| 2026-05-11 | [Attention Drift: What Autoregressive Speculative Decoding Models Learn](https://arxiv.org/abs/2605.09992v1) | 2605.09992v1 | 13 |
| 2026-05-10 | [The Transformer as a Polar State Estimator](https://arxiv.org/abs/2605.11007v4) | 2605.11007v4 | 7 |
| 2026-05-09 | [PPI2Text: Captioning Protein-Protein Interactions with Coordinate-Aligned Pair-Map Decoding](https://arxiv.org/abs/2605.08924v1) | 2605.08924v1 | 8 |
| 2026-05-08 | [Every Feedforward Neural Network Definable in an o-Minimal Structure Has Finite Sample Complexity](https://arxiv.org/abs/2605.07097v1) | 2605.07097v1 | 11 |
| 2026-05-07 | [Cubit: Token Mixer with Kernel Ridge Regression](https://arxiv.org/abs/2605.06501v3) | 2605.06501v3 | 7 |
| 2026-05-06 | [Demystifying Manifold Constraints in LLM Pre-training](https://arxiv.org/abs/2605.04418v2) | 2605.04418v2 | 6 |
| 2026-05-05 | [Jordan-RoPE: Non-Semisimple Relative Positional Encoding via Complex Jordan Blocks](https://arxiv.org/abs/2605.04217v2) | 2605.04217v2 | 12 |
| 2026-05-03 | [TCDA: Thread-Constrained Discourse-Aware Modeling for Conversational Sentiment Quadruple Analysis](https://arxiv.org/abs/2605.01717v2) | 2605.01717v2 | 10 |
| 2026-05-02 | [Toward a foundational thermal model for residential buildings](https://arxiv.org/abs/2605.01364v1) | 2605.01364v1 | 6 |
| 2026-05-01 | [Adaptive 3D-RoPE: Physics-Aligned Rotary Positional Encoding for Wireless Foundation Models](https://arxiv.org/abs/2605.00968v2) | 2605.00968v2 | 12 |
| 2026-05-01 | [Spiking Sequence Machines and Transformers](https://arxiv.org/abs/2605.00662v1) | 2605.00662v1 | 8 |
| 2026-04-30 | [Efficient Spatio-Temporal Vegetation Pixel Classification with Vision Transformers](https://arxiv.org/abs/2605.00296v1) | 2605.00296v1 | 6 |
| 2026-04-30 | [RETO: A Rotary-Enhanced Transformer Operator for High-Fidelity Prediction of Automotive Aerodynamics](https://arxiv.org/abs/2605.00062v3) | 2605.00062v3 | 8 |
| 2026-04-29 | [GMT: A Geometric Multigrid Transformer Solver for Microstructure Homogenization](https://arxiv.org/abs/2604.26518v1) | 2604.26518v1 | 9 |
| 2026-04-27 | [PEPS: Positional Encoding Projected Sampling -- Extended](https://arxiv.org/abs/2604.24167v1) | 2604.24167v1 | 6 |
| 2026-04-26 | [Hardware-Efficient Softmax and Layer Normalization with Guaranteed Normalization for Edge Devices](https://arxiv.org/abs/2604.23647v1) | 2604.23647v1 | 6 |
| 2026-04-20 | [URoPE: Universal Relative Position Embedding across Geometric Spaces](https://arxiv.org/abs/2604.18747v2) | 2604.18747v2 | 17 |
| 2026-04-19 | [Shape: A Self-Supervised 3D Geometry Foundation Model for Industrial CAD Analysis](https://arxiv.org/abs/2604.22826v1) | 2604.22826v1 | 6 |
| 2026-04-18 | [Representation Before Training: A Practical Benchmark for Generative Medical Event Model Tokenization](https://arxiv.org/abs/2604.16775v3) | 2604.16775v3 | 10 |
| 2026-04-17 | [Hierarchical Codec Diffusion for Video-to-Speech Generation](https://arxiv.org/abs/2604.15923v1) | 2604.15923v1 | 9 |
| 2026-04-15 | [Three-Phase Transformer](https://arxiv.org/abs/2604.14430v1) | 2604.14430v1 | 11 |
| 2026-04-15 | [ASTRA: Enhancing Multi-Subject Generation with Retrieval-Augmented Pose Guidance and Disentangled Position Embedding](https://arxiv.org/abs/2604.13938v1) | 2604.13938v1 | 11 |
| 2026-04-14 | [Forge-UGC: FX optimization and register-graph engine for universal graph compiler](https://arxiv.org/abs/2604.16498v1) | 2604.16498v1 | 6 |
| 2026-04-12 | [FishRoPE: Projective Rotary Position Embeddings for Omnidirectional Visual Perception](https://arxiv.org/abs/2604.10391v1) | 2604.10391v1 | 15 |
| 2026-04-10 | [Tango: Taming Visual Signals for Efficient Video Large Language Models](https://arxiv.org/abs/2604.09547v2) | 2604.09547v2 | 10 |
| 2026-04-10 | [Efficient Matrix Implementation for Rotary Position Embedding](https://arxiv.org/abs/2604.09742v1) | 2604.09742v1 | 13 |
| 2026-04-09 | [Sensitivity-Positional Co-Localization in GQA Transformers](https://arxiv.org/abs/2604.07766v1) | 2604.07766v1 | 8 |
| 2026-04-08 | [Training-free Spatially Grounded Geometric Shape Encoding (Technical Report)](https://arxiv.org/abs/2604.07522v2) | 2604.07522v2 | 8 |
| 2026-04-07 | [Short Data, Long Context: Distilling Positional Knowledge in Transformers](https://arxiv.org/abs/2604.06070v1) | 2604.06070v1 | 10 |
| 2026-04-06 | [On the Geometry of Positional Encodings in Transformers](https://arxiv.org/abs/2604.05217v1) | 2604.05217v1 | 16 |
| 2026-04-02 | [SafeRoPE: Risk-specific Head-wise Embedding Rotation for Safe Generation in Rectified Flow Transformers](https://arxiv.org/abs/2604.01826v1) | 2604.01826v1 | 6 |
| 2026-04-02 | [T5Gemma-TTS Technical Report](https://arxiv.org/abs/2604.01760v1) | 2604.01760v1 | 10 |
| 2026-04-02 | [Does Your Optimizer Care How You Normalize? Normalization-Optimizer Coupling in LLM Training](https://arxiv.org/abs/2604.01563v1) | 2604.01563v1 | 7 |
| 2026-03-29 | [OPRO: Orthogonal Panel-Relative Operators for Panel-Aware In-Context Image Generation](https://arxiv.org/abs/2603.27637v1) | 2603.27637v1 | 8 |
| 2026-03-28 | [The Geometric Cost of Normalization: Affine Bounds on the Bayesian Complexity of Neural Networks](https://arxiv.org/abs/2603.27432v1) | 2603.27432v1 | 7 |
| 2026-03-28 | [3D-IDE: 3D Implicit Depth Emergent](https://arxiv.org/abs/2604.03296v1) | 2604.03296v1 | 8 |
| 2026-03-27 | [TurboESM: Ultra-Efficient 3-Bit KV Cache Quantization for Protein Language Models with Orthogonal Rotation and QJL Correction](https://arxiv.org/abs/2603.26110v1) | 2603.26110v1 | 11 |
| 2026-03-26 | [AdaSFormer: Adaptive Serialized Transformers for Monocular Semantic Scene Completion from Indoor Environments](https://arxiv.org/abs/2603.25494v1) | 2603.25494v1 | 8 |
| 2026-03-26 | [Information-Theoretic Limits of Node Localization under Hybrid Graph Positional Encodings](https://arxiv.org/abs/2603.25030v1) | 2603.25030v1 | 6 |
| 2026-03-25 | [Marchuk: Efficient Global Weather Forecasting from Mid-Range to Sub-Seasonal Scales via Flow Matching](https://arxiv.org/abs/2603.24428v1) | 2603.24428v1 | 8 |
| 2026-03-23 | [RotorMap and Quantum Fingerprints of DNA Sequences via Rotary Position Embeddings](https://arxiv.org/abs/2603.22245v2) | 2603.22245v2 | 13 |
| 2026-03-23 | [SegMaFormer: A Hybrid State-Space and Transformer Model for Efficient Segmentation](https://arxiv.org/abs/2603.22002v1) | 2603.22002v1 | 6 |
| 2026-03-23 | [SHARP: Spectrum-aware Highly-dynamic Adaptation for Resolution Promotion in Remote Sensing Synthesis](https://arxiv.org/abs/2603.21783v4) | 2603.21783v4 | 10 |
| 2026-03-22 | [Identity-Consistent Video Generation under Large Facial-Angle Variations](https://arxiv.org/abs/2603.21299v1) | 2603.21299v1 | 8 |
| 2026-03-18 | [LaDe: Unified Multi-Layered Graphic Media Generation and Decomposition](https://arxiv.org/abs/2603.17965v1) | 2603.17965v1 | 8 |
| 2026-03-18 | [Attention Sinks Induce Gradient Sinks: Massive Activations as Gradient Regulators in Transformers](https://arxiv.org/abs/2603.17771v3) | 2603.17771v3 | 7 |
| 2026-03-18 | [Stereo World Model: Camera-Guided Stereo Video Generation](https://arxiv.org/abs/2603.17375v1) | 2603.17375v1 | 8 |
| 2026-03-17 | [What DINO saw: ALiBi positional encoding reduces positional bias in Vision Transformers](https://arxiv.org/abs/2603.16840v2) | 2603.16840v2 | 6 |
| 2026-03-13 | [MXNorm: Reusing MXFP block scales for efficient tensor normalisation](https://arxiv.org/abs/2603.13180v1) | 2603.13180v1 | 6 |
| 2026-03-12 | [Fractional Rotation, Full Potential? Investigating Performance and Convergence of Partial RoPE](https://arxiv.org/abs/2603.11611v2) | 2603.11611v2 | 10 |
| 2026-03-11 | [Multimodal Self-Attention Network with Temporal Alignment for Audio-Visual Emotion Recognition](https://arxiv.org/abs/2603.11095v1) | 2603.11095v1 | 10 |
| 2026-03-10 | [Lost in the Middle at Birth: An Exact Theory of Transformer Position Bias](https://arxiv.org/abs/2603.10123v1) | 2603.10123v1 | 9 |
| 2026-03-10 | [An Optimal Control Approach To Transformer Training](https://arxiv.org/abs/2603.09571v2) | 2603.09571v2 | 8 |
| 2026-03-09 | [LinearARD: Linear-Memory Attention Distillation for RoPE Restoration](https://arxiv.org/abs/2604.00004v3) | 2604.00004v3 | 16 |
| 2026-03-06 | [NerVE: Nonlinear Eigenspectrum Dynamics in LLM Feed-Forward Networks](https://arxiv.org/abs/2603.06922v2) | 2603.06922v2 | 6 |
| 2026-03-04 | [Efficient Point Cloud Processing with High-Dimensional Positional Encoding and Non-Local MLPs](https://arxiv.org/abs/2603.04099v1) | 2603.04099v1 | 6 |
| 2026-03-03 | [Retrievit: In-context Retrieval Capabilities of Transformers, State Space Models, and Hybrid Architectures](https://arxiv.org/abs/2603.02874v2) | 2603.02874v2 | 8 |
| 2026-03-02 | [Accelerating Video Generation Inference with Sequential-Parallel 3D Positional Encoding Using a Global Time Index](https://arxiv.org/abs/2603.06664v1) | 2603.06664v1 | 16 |
| 2026-02-26 | [From Agnostic to Specific: Latent Preference Diffusion for Multi-Behavior Sequential Recommendation](https://arxiv.org/abs/2602.23132v1) | 2602.23132v1 | 8 |
| 2026-02-26 | [UCM: Unified Modeling of Camera Control and Memory with Time-aware Positional Encoding Warping for World Models](https://arxiv.org/abs/2602.22960v2) | 2602.22960v2 | 6 |
| 2026-02-26 | [SoPE: Spherical Coordinate-Based Positional Embedding for Enhancing Spatial Perception of 3D LVLMs](https://arxiv.org/abs/2602.22716v1) | 2602.22716v1 | 10 |
| 2026-02-25 | [An Evaluation of Context Length Extrapolation in Long Code via Positional Embeddings and Efficient Attention](https://arxiv.org/abs/2602.21800v1) | 2602.21800v1 | 6 |
| 2026-02-25 | [SigVLP: Sigmoid Volume-Language Pre-Training for Self-Supervised CT-Volume Adaptive Representation Learning](https://arxiv.org/abs/2602.21735v1) | 2602.21735v1 | 10 |
| 2026-02-24 | [Frayed RoPE and Long Inputs: A Geometric Perspective](https://arxiv.org/abs/2603.18017v1) | 2603.18017v1 | 6 |
| 2026-02-23 | [DTT-BSR: GAN-based DTTNet with RoPE Transformer Enhancement for Music Source Restoration](https://arxiv.org/abs/2602.19825v2) | 2602.19825v2 | 6 |
| 2026-02-22 | [DGPO: RL-Steered Graph Diffusion for Neural Architecture Generation](https://arxiv.org/abs/2602.19261v2) | 2602.19261v2 | 8 |
| 2026-02-20 | [Balancing Symmetry and Efficiency in Graph Flow Matching](https://arxiv.org/abs/2602.18084v2) | 2602.18084v2 | 8 |
| 2026-02-20 | [ZACH-ViT: Regime-Dependent Inductive Bias in Compact Vision Transformers for Medical Imaging](https://arxiv.org/abs/2602.17929v2) | 2602.17929v2 | 6 |
| 2026-02-17 | [Why Any-Order Autoregressive Models Need Two-Stream Attention: A Structural-Semantic Tradeoff](https://arxiv.org/abs/2602.16092v1) | 2602.16092v1 | 10 |
| 2026-02-16 | [Size-Transferability of Graph Transformers with Convolutional Positional Encodings](https://arxiv.org/abs/2602.15239v4) | 2602.15239v4 | 6 |
| 2026-02-13 | [Order Matters in Retrosynthesis: Structure-aware Generation via Reaction-Center-Guided Discrete Flow Matching](https://arxiv.org/abs/2602.13136v2) | 2602.13136v2 | 10 |
| 2026-02-12 | [WaveFormer: Wavelet Embedding Transformer for Biomedical Signals](https://arxiv.org/abs/2602.12189v1) | 2602.12189v1 | 6 |
| 2026-02-12 | [Hi-SAM: A Hierarchical Structure-Aware Multi-modal Framework for Large-Scale Recommendation](https://arxiv.org/abs/2602.11799v2) | 2602.11799v2 | 9 |
| 2026-02-11 | [CADET: Context-Conditioned Ads CTR Prediction With a Decoder-Only Transformer](https://arxiv.org/abs/2602.11410v2) | 2602.11410v2 | 10 |
| 2026-02-11 | [C^2ROPE: Causal Continuous Rotary Positional Encoding for 3D Large Multimodal-Models Reasoning](https://arxiv.org/abs/2602.10551v2) | 2602.10551v2 | 18 |
| 2026-02-11 | [Gated Normalization Removal and Scale Anchoring in Pre-Norm Transformers](https://arxiv.org/abs/2602.10408v2) | 2602.10408v2 | 10 |
| 2026-02-09 | [StretchTime: Adaptive Time Series Forecasting via Symplectic Attention](https://arxiv.org/abs/2602.08983v2) | 2602.08983v2 | 14 |
| 2026-02-08 | [ViT-5: Vision Transformers for The Mid-2020s](https://arxiv.org/abs/2602.08071v1) | 2602.08071v1 | 6 |
| 2026-02-08 | [ReRoPE: Repurposing RoPE for Relative Camera Control](https://arxiv.org/abs/2602.08068v1) | 2602.08068v1 | 6 |
| 2026-02-06 | [RoPE-LIME: RoPE-Space Locality + Sparse-K Sampling for Efficient LLM Attribution](https://arxiv.org/abs/2602.06275v2) | 2602.06275v2 | 6 |
| 2026-02-05 | [CoPE: Clipped RoPE as A Scalable Free Lunch for Long Context LLMs](https://arxiv.org/abs/2602.05258v1) | 2602.05258v1 | 6 |
| 2026-02-04 | [Untwisting RoPE: Frequency Control for Shared Attention in DiTs](https://arxiv.org/abs/2602.05013v1) | 2602.05013v1 | 10 |
| 2026-02-03 | [Spiral RoPE: Rotate Your Rotary Positional Embeddings in the 2D Plane](https://arxiv.org/abs/2602.03227v1) | 2602.03227v1 | 20 |
| 2026-02-03 | [IVC-Prune: Revealing the Implicit Visual Coordinates in LVLMs for Vision Token Pruning](https://arxiv.org/abs/2602.03060v1) | 2602.03060v1 | 10 |
| 2026-02-02 | [HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control](https://arxiv.org/abs/2602.02268v1) | 2602.02268v1 | 8 |
| 2026-02-02 | [The Inlet Rank Collapse in Implicit Neural Representations: Diagnosis and Unified Remedy](https://arxiv.org/abs/2602.01526v1) | 2602.01526v1 | 6 |
| 2026-02-01 | [Parabolic Positional Encoding: A Vision-Centric, Principled, Extrapolatable, and General Approach](https://arxiv.org/abs/2602.01418v3) | 2602.01418v3 | 6 |
| 2026-02-01 | [RAP: KV-Cache Compression via RoPE-Aligned Pruning](https://arxiv.org/abs/2602.02599v4) | 2602.02599v4 | 12 |
| 2026-01-31 | [NPNet: A Non-Parametric Network with Adaptive Gaussian-Fourier Positional Encoding for 3D Classification and Segmentation](https://arxiv.org/abs/2602.00542v1) | 2602.00542v1 | 6 |
| 2026-01-30 | [A Unified View of Attention and Residual Sinks: Outlier-Driven Rescaling is Essential for Transformer Training](https://arxiv.org/abs/2601.22966v1) | 2601.22966v1 | 8 |
| 2026-01-29 | [Bifocal Attention: Harmonizing Geometric and Spectral Positional Embeddings for Algorithmic Generalization](https://arxiv.org/abs/2601.22402v2) | 2601.22402v2 | 8 |
| 2026-01-28 | [Dissecting Multimodal In-Context Learning: Modality Asymmetries and Circuit Dynamics in modern Transformers](https://arxiv.org/abs/2601.20796v2) | 2601.20796v2 | 10 |
| 2026-01-28 | [MrRoPE: Mixed-radix Rotary Position Embedding](https://arxiv.org/abs/2601.22181v1) | 2601.22181v1 | 15 |
| 2026-01-23 | [LoL: Longer than Longer, Scaling Video Generation to Hour](https://arxiv.org/abs/2601.16914v1) | 2601.16914v1 | 10 |
| 2026-01-21 | [RayRoPE: Projective Ray Positional Encoding for Multi-view Attention](https://arxiv.org/abs/2601.15275v3) | 2601.15275v3 | 12 |
| 2026-01-21 | [OmniSpectra: A Unified Foundation Model for Universal Spectra Representation Learning](https://arxiv.org/abs/2601.15351v2) | 2601.15351v2 | 6 |
| 2026-01-13 | [Demystifying the Slash Pattern in Attention: The Role of RoPE](https://arxiv.org/abs/2601.08297v2) | 2601.08297v2 | 12 |
| 2026-01-11 | [CLIMP: Contrastive Language-Image Mamba Pretraining](https://arxiv.org/abs/2601.06891v2) | 2601.06891v2 | 8 |
| 2026-01-08 | [LooseRoPE: Content-aware Attention Manipulation for Semantic Harmonization](https://arxiv.org/abs/2601.05127v2) | 2601.05127v2 | 10 |
| 2026-01-07 | [TellWhisper: Tell Whisper Who Speaks When](https://arxiv.org/abs/2601.03712v3) | 2601.03712v3 | 8 |
| 2026-01-06 | [CRoPE: Efficient Parametrization of Rotary Positional Embedding](https://arxiv.org/abs/2601.02728v2) | 2601.02728v2 | 6 |
| 2026-01-06 | [Chronicals: A High-Performance Framework for LLM Fine-Tuning with 3.51x Speedup over Unsloth](https://arxiv.org/abs/2601.02609v1) | 2601.02609v1 | 8 |
| 2026-01-05 | [FFP-300K: Scaling First-Frame Propagation for Generalizable Video Editing](https://arxiv.org/abs/2601.01720v3) | 2601.01720v3 | 8 |
| 2026-01-03 | [Towards Infinite Length Extrapolation: A Unified Approach](https://arxiv.org/abs/2601.06113v1) | 2601.06113v1 | 14 |
| 2026-01-02 | [BSAT: B-Spline Adaptive Tokenizer for Long-Term Time Series Forecasting](https://arxiv.org/abs/2601.00698v1) | 2601.00698v1 | 8 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-27 | [SPECTRE: Spectral Pre-training Embeddings with Cylindrical Temporal Rotary Position Encoding for Fine-Grained sEMG-Based Movement Decoding](https://arxiv.org/abs/2512.22481v1) | 2512.22481v1 | 14 |
| 2025-12-26 | [Bounded Hyperbolic Tangent: A Stable and Efficient Alternative to Pre-Layer Normalization in Large Language Models](https://arxiv.org/abs/2601.09719v3) | 2601.09719v3 | 10 |
| 2025-12-25 | [Towards Long-window Anchoring in Vision-Language Model Distillation](https://arxiv.org/abs/2512.21576v1) | 2512.21576v1 | 10 |
| 2025-12-22 | [Alternative positional encoding functions for neural transformers](https://arxiv.org/abs/2512.19323v1) | 2512.19323v1 | 10 |
| 2025-12-21 | [EchoMotion: Unified Human Video and Motion Generation via Dual-Modality Diffusion Transformer](https://arxiv.org/abs/2512.18814v1) | 2512.18814v1 | 8 |
| 2025-12-18 | [MEPIC: Memory Efficient Position Independent Caching for LLM Serving](https://arxiv.org/abs/2512.16822v1) | 2512.16822v1 | 14 |
| 2025-12-17 | [How Smoothing is N-simplicial Attention?](https://arxiv.org/abs/2512.15600v1) | 2512.15600v1 | 10 |
| 2025-12-17 | [Understanding NTK Variance in Implicit Neural Representations](https://arxiv.org/abs/2512.15169v1) | 2512.15169v1 | 6 |
| 2025-12-16 | [EXAONE Path 2.5: Pathology Foundation Model with Multi-Omics Alignment](https://arxiv.org/abs/2512.14019v1) | 2512.14019v1 | 8 |
| 2025-12-15 | [LitePT: Lighter Yet Stronger Point Transformer](https://arxiv.org/abs/2512.13689v3) | 2512.13689v3 | 8 |
| 2025-12-14 | [From Small to Large: Generalization Bounds for Transformers on Variable-Size Inputs](https://arxiv.org/abs/2512.12805v2) | 2512.12805v2 | 8 |
| 2025-12-12 | [JoyStreamer-Flash: Real-time and Infinite Audio-Driven Avatar Generation with Autoregressive Diffusion](https://arxiv.org/abs/2512.11423v3) | 2512.11423v3 | 8 |
| 2025-12-11 | [Stronger Normalization-Free Transformers](https://arxiv.org/abs/2512.10938v2) | 2512.10938v2 | 11 |
| 2025-12-10 | [Impact of Positional Encoding: Clean and Adversarial Rademacher Complexity for Transformers under In-Context Regression](https://arxiv.org/abs/2512.09275v2) | 2512.09275v2 | 6 |
| 2025-12-09 | [Can TabPFN Compete with GNNs for Node Classification via Graph Tabularization?](https://arxiv.org/abs/2512.08798v1) | 2512.08798v1 | 8 |
| 2025-12-08 | [Group Representational Position Encoding](https://arxiv.org/abs/2512.07805v6) | 2512.07805v6 | 8 |
| 2025-12-08 | [Beyond Real: Imaginary Extension of Rotary Position Embeddings for Long-Context LLMs](https://arxiv.org/abs/2512.07525v1) | 2512.07525v1 | 13 |
| 2025-12-08 | [Unified Camera Positional Encoding for Controlled Video Generation](https://arxiv.org/abs/2512.07237v2) | 2512.07237v2 | 6 |
| 2025-12-07 | [Adaptive Normalization Mamba with Multi Scale Trend Decomposition and Patch MoE Encoding](https://arxiv.org/abs/2512.06929v1) | 2512.06929v1 | 7 |
| 2025-12-04 | [BulletTime: Decoupled Control of Time and Camera Pose for Video Generation](https://arxiv.org/abs/2512.05076v2) | 2512.05076v2 | 6 |
| 2025-12-03 | [CookAnything: A Framework for Flexible and Consistent Multi-Step Recipe Image Generation](https://arxiv.org/abs/2512.03540v2) | 2512.03540v2 | 8 |
| 2025-12-01 | [DreamingComics: A Story Visualization Pipeline via Subject and Layout Customized Generation using Video Models](https://arxiv.org/abs/2512.01686v1) | 2512.01686v1 | 8 |
| 2025-12-01 | [ResDiT: Evoking the Intrinsic Resolution Scalability in Diffusion Transformers](https://arxiv.org/abs/2512.01426v1) | 2512.01426v1 | 6 |
| 2025-11-30 | [Smol-GS: Compact Representations for Abstract 3D Gaussian Splatting](https://arxiv.org/abs/2512.00850v3) | 2512.00850v3 | 8 |
| 2025-11-25 | [Dynamical Properties of Tokens in Self-Attention and Effects of Positional Encoding](https://arxiv.org/abs/2512.03058v1) | 2512.03058v1 | 12 |
| 2025-11-25 | [Infinity-RoPE: Action-Controllable Infinite Video Generation Emerges From Autoregressive Self-Rollout](https://arxiv.org/abs/2511.20649v3) | 2511.20649v3 | 6 |
| 2025-11-25 | [UltraViCo: Breaking Extrapolation Limits in Video Diffusion Transformers](https://arxiv.org/abs/2511.20123v2) | 2511.20123v2 | 12 |
| 2025-11-24 | [Phase-Aligned RoPE for Mixed-Resolution Diffusion Transformer](https://arxiv.org/abs/2511.19778v2) | 2511.19778v2 | 6 |
| 2025-11-24 | [MapFormer: Self-Supervised Learning of Cognitive Maps with Input-Dependent Positional Embeddings](https://arxiv.org/abs/2511.19279v4) | 2511.19279v4 | 8 |
| 2025-11-23 | [Zero-Reference Joint Low-Light Enhancement and Deblurring via Visual Autoregressive Modeling with VLM-Derived Modulation](https://arxiv.org/abs/2511.18591v1) | 2511.18591v1 | 8 |
| 2025-11-23 | [NAF: Zero-Shot Feature Upsampling via Neighborhood Attention Filtering](https://arxiv.org/abs/2511.18452v1) | 2511.18452v1 | 10 |
| 2025-11-23 | [From Tables to Signals: Revealing Spectral Adaptivity in TabPFN](https://arxiv.org/abs/2511.18278v1) | 2511.18278v1 | 8 |
| 2025-11-22 | [UltraFlux: Data-Model Co-Design for High-quality Native 4K Text-to-Image Generation across Diverse Aspect Ratios](https://arxiv.org/abs/2511.18050v1) | 2511.18050v1 | 8 |
| 2025-11-22 | [Equivalence of Context and Parameter Updates in Modern Transformer Blocks](https://arxiv.org/abs/2511.17864v3) | 2511.17864v3 | 10 |
| 2025-11-21 | [Selective Rotary Position Embedding](https://arxiv.org/abs/2511.17388v3) | 2511.17388v3 | 13 |
| 2025-11-21 | [RoSA: Enhancing Parameter-Efficient Fine-Tuning via RoPE-aware Selective Adaptation in Large Language Models](https://arxiv.org/abs/2511.21733v1) | 2511.21733v1 | 12 |
| 2025-11-17 | [Tab-PET: Graph-Based Positional Encodings for Tabular Transformers](https://arxiv.org/abs/2511.13338v2) | 2511.13338v2 | 6 |
| 2025-11-14 | [Power law attention biases for molecular transformers](https://arxiv.org/abs/2511.11489v1) | 2511.11489v1 | 8 |
| 2025-11-14 | [PAS: A Training-Free Stabilizer for Temporal Encoding in Video LLMs](https://arxiv.org/abs/2511.10979v2) | 2511.10979v2 | 14 |
| 2025-11-13 | [Remember Me: Bridging the Long-Range Gap in LVLMs with Three-Step Inference-Only Decay Resilience Strategies](https://arxiv.org/abs/2511.09868v1) | 2511.09868v1 | 9 |
| 2025-11-12 | [Mip-NeWRF: Enhanced Wireless Radiance Field with Hybrid Encoding for Channel Prediction](https://arxiv.org/abs/2511.09150v2) | 2511.09150v2 | 6 |
| 2025-11-12 | [DoPE: Denoising Rotary Position Embedding](https://arxiv.org/abs/2511.09146v2) | 2511.09146v2 | 21 |
| 2025-11-11 | [A Circular Argument : Does RoPE need to be Equivariant for Vision?](https://arxiv.org/abs/2511.08368v1) | 2511.08368v1 | 10 |
| 2025-11-11 | [Do traveling waves make good positional encodings?](https://arxiv.org/abs/2511.11668v1) | 2511.11668v1 | 10 |
| 2025-11-11 | [Clifford Algebraic Rotor Embeddings : Maybe embeddings should start to CARE](https://arxiv.org/abs/2511.11665v1) | 2511.11665v1 | 8 |
| 2025-11-11 | [Gate-level boolean evolutionary geometric attention neural networks](https://arxiv.org/abs/2511.17550v1) | 2511.17550v1 | 10 |
| 2025-11-11 | [On the Interplay between Positional Encodings, Morphological Complexity, and Word Order Flexibility](https://arxiv.org/abs/2511.08139v1) | 2511.08139v1 | 6 |
| 2025-11-11 | [Laytrol: Preserving Pretrained Knowledge in Layout Control for Multimodal Diffusion Transformers](https://arxiv.org/abs/2511.07934v1) | 2511.07934v1 | 6 |
| 2025-11-09 | [Vocabulary In-Context Learning in Transformers: Benefits of Positional Encoding](https://arxiv.org/abs/2511.06376v1) | 2511.06376v1 | 10 |
| 2025-11-05 | [Sketch-Augmented Features Improve Learning Long-Range Dependencies in Graph Neural Networks](https://arxiv.org/abs/2511.03824v1) | 2511.03824v1 | 8 |
| 2025-10-29 | [IBNorm: Information-Bottleneck Inspired Normalization for Representation Learning](https://arxiv.org/abs/2510.25262v2) | 2510.25262v2 | 7 |
| 2025-10-27 | [Revisiting Multimodal Positional Encoding in Vision-Language Models](https://arxiv.org/abs/2510.23095v3) | 2510.23095v3 | 10 |
| 2025-10-26 | [SeeDNorm: Self-Rescaled Dynamic Normalization](https://arxiv.org/abs/2510.22777v3) | 2510.22777v3 | 7 |
| 2025-10-25 | [Mitigating Coordinate Prediction Bias from Positional Encoding Failures](https://arxiv.org/abs/2510.22102v2) | 2510.22102v2 | 6 |
| 2025-10-23 | [Stateful KV Cache Management for LLMs: Balancing Space, Time, Accuracy, and Positional Fidelity](https://arxiv.org/abs/2511.04686v1) | 2511.04686v1 | 8 |
| 2025-10-23 | [Rotate Both Ways: Time-and-Order RoPE for Generative Recommendation](https://arxiv.org/abs/2510.20455v1) | 2510.20455v1 | 12 |
| 2025-10-23 | [Positional Encoding Field](https://arxiv.org/abs/2510.20385v1) | 2510.20385v1 | 6 |
| 2025-10-23 | [Seeing the Unseen: Mask-Driven Positional Encoding and Strip-Convolution Context Modeling for Cross-View Object Geo-Localization](https://arxiv.org/abs/2510.20247v1) | 2510.20247v1 | 6 |
| 2025-10-21 | [Kaleido: Open-Sourced Multi-Subject Reference Video Generation Model](https://arxiv.org/abs/2510.18573v2) | 2510.18573v2 | 8 |
| 2025-10-19 | [Closing the Curvature Gap: Full Transformer Hessians](https://arxiv.org/abs/2510.16927v2) | 2510.16927v2 | 9 |
| 2025-10-12 | [Head-wise Adaptive Rotary Positional Encoding for Fine-Grained Image Generation](https://arxiv.org/abs/2510.10489v2) | 2510.10489v2 | 16 |
| 2025-10-10 | [Stability of Transformers under Layer Normalization](https://arxiv.org/abs/2510.09904v2) | 2510.09904v2 | 8 |
| 2025-10-04 | [Exploring the Hierarchical Reasoning Model for Small Natural-Image Classification Without Augmentation](https://arxiv.org/abs/2510.03598v1) | 2510.03598v1 | 10 |
| 2025-10-03 | [Decoupling Positional and Symbolic Attention Behavior in Transformers](https://arxiv.org/abs/2511.11579v1) | 2511.11579v1 | 8 |
| 2025-10-02 | [PyramidStyler: Transformer-Based Neural Style Transfer with Pyramidal Positional Encoding and Reinforcement Learning](https://arxiv.org/abs/2510.01715v1) | 2510.01715v1 | 6 |
| 2025-10-01 | [LEAP: Local ECT-Based Learnable Positional Encodings for Graphs](https://arxiv.org/abs/2510.00757v3) | 2510.00757v3 | 6 |
| 2025-10-01 | [Arbitrary Generative Video Interpolation](https://arxiv.org/abs/2510.00578v3) | 2510.00578v3 | 10 |
| 2025-10-01 | [Microsaccade-Inspired Probing: Positional Encoding Perturbations Reveal LLM Misbehaviours](https://arxiv.org/abs/2510.01288v1) | 2510.01288v1 | 6 |
| 2025-09-29 | [SemShareKV: Efficient KVCache Sharing for Semantically Similar Prompts via Token-Level LSH Matching](https://arxiv.org/abs/2509.24832v2) | 2509.24832v2 | 10 |
| 2025-09-26 | [Learning the Neighborhood: Contrast-Free Multimodal Self-Supervised Molecular Graph Pretraining](https://arxiv.org/abs/2509.22468v2) | 2509.22468v2 | 8 |
| 2025-09-20 | [Causality-Induced Positional Encoding for Transformer-Based Representation Learning of Non-Sequential Features](https://arxiv.org/abs/2509.16629v2) | 2509.16629v2 | 10 |
| 2025-09-18 | [DyWPE: Signal-Aware Dynamic Wavelet Positional Encoding for Time Series Transformers](https://arxiv.org/abs/2509.14640v2) | 2509.14640v2 | 6 |
| 2025-09-17 | [AToken: A Unified Tokenizer for Vision](https://arxiv.org/abs/2509.14476v2) | 2509.14476v2 | 6 |
| 2025-09-17 | [ST-LINK: Spatially-Aware Large Language Models for Spatio-Temporal Forecasting](https://arxiv.org/abs/2509.13753v1) | 2509.13753v1 | 6 |
| 2025-09-16 | [Positional Encoding via Token-Aware Phase Attention](https://arxiv.org/abs/2509.12635v4) | 2509.12635v4 | 10 |
| 2025-09-14 | [Length-Aware Rotary Position Embedding for Text-Speech Alignment](https://arxiv.org/abs/2509.11084v1) | 2509.11084v1 | 13 |
| 2025-09-09 | [Improving Machine Learning-Based Robot Self-Collision Checking with Input Positional Encoding](https://arxiv.org/abs/2509.07542v2) | 2509.07542v2 | 6 |
| 2025-09-05 | [HoPE: Hyperbolic Rotary Positional Encoding for Stable Long-Range Dependency Modeling in Large Language Models](https://arxiv.org/abs/2509.05218v2) | 2509.05218v2 | 10 |
| 2025-09-05 | [Decoupling the "What" and "Where" With Polar Coordinate Positional Embeddings](https://arxiv.org/abs/2509.10534v3) | 2509.10534v3 | 18 |
| 2025-09-04 | [SAC-MIL: Spatial-Aware Correlated Multiple Instance Learning for Histopathology Whole Slide Image Classification](https://arxiv.org/abs/2509.03973v1) | 2509.03973v1 | 8 |
| 2025-09-02 | [The Transparent Earth: A Multimodal Foundation Model for the Earth's Subsurface](https://arxiv.org/abs/2509.02783v2) | 2509.02783v2 | 8 |
| 2025-09-02 | [Anisotropic Fourier Features for Positional Encoding in Medical Imaging](https://arxiv.org/abs/2509.02488v1) | 2509.02488v1 | 6 |
| 2025-09-02 | [GenCompositor: Generative Video Compositing with Diffusion Transformer](https://arxiv.org/abs/2509.02460v2) | 2509.02460v2 | 10 |
| 2025-08-26 | [Beyond flattening: a geometrically principled positional encoding for vision transformers with Weierstrass elliptic functions](https://arxiv.org/abs/2508.19167v1) | 2508.19167v1 | 10 |
| 2025-08-23 | [CoPE: A Lightweight Complex Positional Encoding](https://arxiv.org/abs/2508.18308v1) | 2508.18308v1 | 10 |
| 2025-08-21 | [CineScale: Tuning-Free High-Resolution Video Generation](https://arxiv.org/abs/2508.15774v3) | 2508.15774v3 | 8 |
| 2025-08-07 | [Advanced Hybrid Transformer LSTM Technique with Attention and TS Mixer for Drilling Rate of Penetration Prediction](https://arxiv.org/abs/2508.05210v3) | 2508.05210v3 | 8 |
| 2025-08-06 | [GraphProp: Training the Graph Foundation Models using Graph Properties](https://arxiv.org/abs/2508.04594v2) | 2508.04594v2 | 10 |
| 2025-08-04 | [LaMPE: Length-aware Multi-grained Positional Encoding for Adaptive Long-context Scaling Without Training](https://arxiv.org/abs/2508.02308v2) | 2508.02308v2 | 20 |
| 2025-07-30 | [Context-aware Rotary Position Embedding](https://arxiv.org/abs/2507.23083v1) | 2507.23083v1 | 17 |
| 2025-07-22 | [Dens3R: A Foundation Model for 3D Geometry Prediction](https://arxiv.org/abs/2507.16290v1) | 2507.16290v1 | 8 |
| 2025-07-21 | [Supernova: Achieving More with Less in Transformer Architectures](https://arxiv.org/abs/2507.15773v2) | 2507.15773v2 | 8 |
| 2025-07-21 | [DynImg: Key Frames with Visual Prompts are Good Representation for Multi-Modal Video Understanding](https://arxiv.org/abs/2507.15569v1) | 2507.15569v1 | 6 |
| 2025-07-20 | [Evaluation of Coding Schemes for Transformer-based Gene Sequence Modeling](https://arxiv.org/abs/2507.15087v1) | 2507.15087v1 | 8 |
| 2025-07-14 | [Cameras as Relative Positional Encoding](https://arxiv.org/abs/2507.10496v2) | 2507.10496v2 | 10 |
| 2025-07-11 | [Infinite Video Understanding](https://arxiv.org/abs/2507.09068v2) | 2507.09068v2 | 8 |
| 2025-07-11 | [Hybrid Systolic Array Accelerator with Optimized Dataflow for Edge Large Language Model Inference](https://arxiv.org/abs/2507.09010v1) | 2507.09010v1 | 16 |
| 2025-07-07 | [AXLearn: Modular, Hardware-Agnostic Large Model Training](https://arxiv.org/abs/2507.05411v3) | 2507.05411v3 | 10 |
| 2025-07-04 | [UWB TDoA Error Correction using Transformers: Patching and Positional Encoding Strategies](https://arxiv.org/abs/2507.03523v1) | 2507.03523v1 | 6 |
| 2025-06-22 | [Dynamic Temporal Positional Encodings for Early Intrusion Detection in IoT](https://arxiv.org/abs/2506.18114v1) | 2506.18114v1 | 6 |
| 2025-06-19 | [On the Existence and Uniqueness of Symmetric Structures Generating Complete Ordered Pairs](https://arxiv.org/abs/2506.16414v1) | 2506.16414v1 | 8 |
| 2025-06-19 | [Knee-Deep in C-RASP: A Transformer Depth Hierarchy](https://arxiv.org/abs/2506.16055v3) | 2506.16055v3 | 8 |
| 2025-06-17 | [LongLLaDA: Unlocking Long Context Capabilities in Diffusion LLMs](https://arxiv.org/abs/2506.14429v3) | 2506.14429v3 | 14 |
| 2025-06-16 | [Robust Physics-Informed Neural Network Approach for Estimating Heterogeneous Elastic Properties from Noisy Displacement Data](https://arxiv.org/abs/2506.14036v2) | 2506.14036v2 | 10 |
| 2025-06-16 | [GLU Attention Improve Transformer](https://arxiv.org/abs/2507.00022v2) | 2507.00022v2 | 10 |
| 2025-06-16 | [SeqPE: Transformer with Sequential Position Encoding](https://arxiv.org/abs/2506.13277v2) | 2506.13277v2 | 14 |
| 2025-06-13 | [Long-Short Alignment for Effective Long-Context Modeling in LLMs](https://arxiv.org/abs/2506.11769v1) | 2506.11769v1 | 8 |
| 2025-06-13 | [DIVER-0 : A Fully Channel Equivariant EEG Foundation Model](https://arxiv.org/abs/2507.14141v1) | 2507.14141v1 | 14 |
| 2025-06-11 | [TransXSSM: A Hybrid Transformer State Space Model with Unified Rotary Position Embedding](https://arxiv.org/abs/2506.09507v3) | 2506.09507v3 | 17 |
| 2025-06-10 | [LaDCast: A Latent Diffusion Model for Medium-Range Ensemble Weather Forecasting](https://arxiv.org/abs/2506.09193v1) | 2506.09193v1 | 10 |
| 2025-06-10 | [Transformers Meet Hyperspectral Imaging: A Comprehensive Study of Models, Challenges and Open Problems](https://arxiv.org/abs/2506.08596v1) | 2506.08596v1 | 8 |
| 2025-06-10 | [Learnable Spatial-Temporal Positional Encoding for Link Prediction](https://arxiv.org/abs/2506.08309v2) | 2506.08309v2 | 10 |
| 2025-06-09 | [Return of ChebNet: Understanding and Improving an Overlooked GNN on Long Range Tasks](https://arxiv.org/abs/2506.07624v2) | 2506.07624v2 | 8 |
| 2025-06-08 | [TV-LiVE: Training-Free, Text-Guided Video Editing via Layer Informed Vitality Exploitation](https://arxiv.org/abs/2506.07205v1) | 2506.07205v1 | 10 |
| 2025-06-07 | [Exploring Length Generalization For Transformer-based Speech Enhancement](https://arxiv.org/abs/2506.06697v1) | 2506.06697v1 | 8 |
| 2025-06-06 | [CoMemo: LVLMs Need Image Context with Image Memory](https://arxiv.org/abs/2506.06279v1) | 2506.06279v1 | 8 |
| 2025-06-06 | [Positional Encoding meets Persistent Homology on Graphs](https://arxiv.org/abs/2506.05814v1) | 2506.05814v1 | 10 |
| 2025-06-05 | [Theoretical Analysis of Positional Encodings in Transformer Models: Impact on Expressiveness and Generalization](https://arxiv.org/abs/2506.06398v1) | 2506.06398v1 | 6 |
| 2025-06-05 | [TextVidBench: A Benchmark for Long Video Scene Text Understanding](https://arxiv.org/abs/2506.04983v1) | 2506.04983v1 | 8 |
| 2025-06-05 | [OpenGT: A Comprehensive Benchmark For Graph Transformers](https://arxiv.org/abs/2506.04765v1) | 2506.04765v1 | 8 |
| 2025-06-04 | [UNIC: Unified In-Context Video Editing](https://arxiv.org/abs/2506.04216v1) | 2506.04216v1 | 8 |
| 2025-06-04 | [ComRoPE: Scalable and Robust Rotary Position Embedding Parameterized by Trainable Commuting Angle Matrices](https://arxiv.org/abs/2506.03737v1) | 2506.03737v1 | 19 |
| 2025-06-02 | [Revisiting LRP: Positional Attribution as the Missing Ingredient for Transformer Explainability](https://arxiv.org/abs/2506.02138v1) | 2506.02138v1 | 8 |
| 2025-06-02 | [Understanding and Improving Laplacian Positional Encodings For Temporal GNNs](https://arxiv.org/abs/2506.01596v1) | 2506.01596v1 | 6 |
| 2025-06-01 | [Position as Probability: Self-Supervised Transformers that Think Past Their Training for Length Extrapolation](https://arxiv.org/abs/2506.00920v2) | 2506.00920v2 | 10 |
| 2025-05-30 | [UniGeo: Taming Video Diffusion for Unified Consistent Geometry Estimation](https://arxiv.org/abs/2505.24521v1) | 2505.24521v1 | 8 |
| 2025-05-29 | [Graph Positional Autoencoders as Self-supervised Learners](https://arxiv.org/abs/2505.23345v2) | 2505.23345v2 | 8 |
| 2025-05-28 | [Let Them Talk: Audio-Driven Multi-Person Conversational Video Generation](https://arxiv.org/abs/2505.22647v1) | 2505.22647v1 | 10 |
| 2025-05-27 | [ID-Align: RoPE-Conscious Position Remapping for Dynamic High-Resolution Adaptation in Vision-Language Models](https://arxiv.org/abs/2505.21465v2) | 2505.21465v2 | 12 |
| 2025-05-27 | [FireQ: Fast INT4-FP8 Kernel and RoPE-aware Quantization for LLM Inference Acceleration](https://arxiv.org/abs/2505.20839v3) | 2505.20839v3 | 6 |
| 2025-05-26 | [VoiceStar: Robust Zero-Shot Autoregressive TTS with Duration Control and Extrapolation](https://arxiv.org/abs/2505.19462v2) | 2505.19462v2 | 10 |
| 2025-05-24 | [Parameter-Efficient CLIP Adaptation for 3D Understanding via Unified Tokenization](https://arxiv.org/abs/2505.18819v2) | 2505.18819v2 | 6 |
| 2025-05-23 | [DAM-GT: Dual Positional Encoding-Based Attention Masking Graph Transformer for Node Classification](https://arxiv.org/abs/2505.17660v1) | 2505.17660v1 | 6 |
| 2025-05-22 | [Circle-RoPE: Cone-like Decoupled Rotary Positional Embedding for Large Vision-Language Models](https://arxiv.org/abs/2505.16416v3) | 2505.16416v3 | 12 |
| 2025-05-21 | [Directional Non-Commutative Monoidal Structures for Compositional Embeddings in Machine Learning](https://arxiv.org/abs/2505.15507v1) | 2505.15507v1 | 8 |
| 2025-05-19 | [RoPECraft: Training-Free Motion Transfer with Trajectory-Guided RoPE Optimization on Diffusion Transformers](https://arxiv.org/abs/2505.13344v2) | 2505.13344v2 | 6 |
| 2025-05-19 | [Parallel Layer Normalization for Universal Approximation](https://arxiv.org/abs/2505.13142v3) | 2505.13142v3 | 10 |
| 2025-05-19 | [Graph Alignment for Benchmarking Graph Neural Networks and Learning Positional Encodings](https://arxiv.org/abs/2505.13087v2) | 2505.13087v2 | 6 |
| 2025-05-19 | [Deconstructing Positional Information: From Attention Logits to Training Biases](https://arxiv.org/abs/2505.13027v2) | 2505.13027v2 | 8 |
| 2025-05-18 | [PSC: Extending Context Window of Large Language Models via Phase Shift Calibration](https://arxiv.org/abs/2505.12423v1) | 2505.12423v1 | 10 |
| 2025-05-18 | [Context-Aware Autoregressive Models for Multi-Conditional Image Generation](https://arxiv.org/abs/2505.12274v1) | 2505.12274v1 | 10 |
| 2025-05-17 | [VFRTok: Variable Frame Rates Video Tokenizer with Duration-Proportional Information Assumption](https://arxiv.org/abs/2505.12053v2) | 2505.12053v2 | 10 |
| 2025-05-17 | [Fast RoPE Attention: Combining the Polynomial Method and Fast Fourier Transform](https://arxiv.org/abs/2505.11892v1) | 2505.11892v1 | 12 |
| 2025-05-16 | [The Counting Power of Transformers](https://arxiv.org/abs/2505.11199v3) | 2505.11199v3 | 8 |
| 2025-05-15 | [ComplexFormer: Disruptively Advancing Transformer Inference Ability via Head-Specific Complex Vector Attention](https://arxiv.org/abs/2505.10222v2) | 2505.10222v2 | 8 |
| 2025-05-11 | [Technical Report for ICRA 2025 GOOSE 2D Semantic Segmentation Challenge: Leveraging Color Shift Correction, RoPE-Swin Backbone, and Quantile-based Label Denoising Strategy for Robust Outdoor Scene Understanding](https://arxiv.org/abs/2505.06991v1) | 2505.06991v1 | 17 |
| 2025-05-08 | [Mogao: An Omni Foundation Model for Interleaved Multi-Modal Generation](https://arxiv.org/abs/2505.05472v2) | 2505.05472v2 | 6 |
| 2025-04-29 | [Learning Laplacian Positional Encodings for Heterophilous Graphs](https://arxiv.org/abs/2504.20430v1) | 2504.20430v1 | 10 |
| 2025-04-28 | [A Comparative Study on Positional Encoding for Time-frequency Domain Dual-path Transformer-based Source Separation Models](https://arxiv.org/abs/2504.19605v2) | 2504.19605v2 | 10 |
| 2025-04-21 | [A Diagnostic Evaluation of Neural Networks Trained with the Error Diffusion Learning Algorithm](https://arxiv.org/abs/2504.14814v4) | 2504.14814v4 | 6 |
| 2025-04-18 | [HMPE:HeatMap Embedding for Efficient Transformer-Based Small Object Detection](https://arxiv.org/abs/2504.13469v1) | 2504.13469v1 | 6 |
| 2025-04-17 | [Plain Transformers Can be Powerful Graph Learners](https://arxiv.org/abs/2504.12588v4) | 2504.12588v4 | 6 |
| 2025-04-15 | [Multi-output Classification Framework and Frequency Layer Normalization for Compound Fault Diagnosis in Motor](https://arxiv.org/abs/2504.11513v2) | 2504.11513v2 | 10 |
| 2025-04-14 | [The Scalability of Simplicity: Empirical Analysis of Vision-Language Learning with a Single Transformer](https://arxiv.org/abs/2504.10462v1) | 2504.10462v1 | 8 |
| 2025-04-12 | [Accurate Diagnosis of Respiratory Viruses Using an Explainable Machine Learning with Mid-Infrared Biomolecular Fingerprinting of Nasopharyngeal Secretions](https://arxiv.org/abs/2504.09211v1) | 2504.09211v1 | 12 |
| 2025-04-11 | [SWAN-GPT: An Efficient and Scalable Approach for Long-Context Language Modeling](https://arxiv.org/abs/2504.08719v1) | 2504.08719v1 | 12 |
| 2025-04-09 | [Analyzing the Training Dynamics of Image Restoration Transformers: A Revisit to Layer Normalization](https://arxiv.org/abs/2504.06629v3) | 2504.06629v3 | 6 |
| 2025-04-08 | [Hogwild! Inference: Parallel LLM Generation via Concurrent Attention](https://arxiv.org/abs/2504.06261v4) | 2504.06261v4 | 10 |
| 2025-04-07 | [Rethinking RoPE: A Mathematical Blueprint for N-dimensional Positional Embedding](https://arxiv.org/abs/2504.06308v2) | 2504.06308v2 | 12 |
| 2025-04-07 | [Of All StrIPEs: Investigating Structure-informed Positional Encoding for Efficient Music Generation](https://arxiv.org/abs/2504.05364v1) | 2504.05364v1 | 10 |
| 2025-04-05 | [Sensitivity Meets Sparsity: The Impact of Extremely Sparse Parameter Patterns on Theory-of-Mind of Large Language Models](https://arxiv.org/abs/2504.04238v1) | 2504.04238v1 | 14 |
| 2025-04-03 | [Graph Attention for Heterogeneous Graphs with Positional Encoding](https://arxiv.org/abs/2504.02938v1) | 2504.02938v1 | 6 |
| 2025-04-03 | [Spline-based Transformers](https://arxiv.org/abs/2504.02797v1) | 2504.02797v1 | 8 |
| 2025-04-02 | [Less-to-More Generalization: Unlocking More Controllability by In-Context Generation](https://arxiv.org/abs/2504.02160v1) | 2504.02160v1 | 6 |
| 2025-03-27 | [On the Mathematical Relationship Between Layer Normalization and Dynamic Activation Functions](https://arxiv.org/abs/2503.21708v4) | 2503.21708v4 | 10 |
| 2025-03-24 | [Boosting Resolution Generalization of Diffusion Transformers with Randomized Positional Encodings](https://arxiv.org/abs/2503.18719v2) | 2503.18719v2 | 6 |
| 2025-03-21 | [Beyond Semantics: Rediscovering Spatial Awareness in Vision-Language Models](https://arxiv.org/abs/2503.17349v2) | 2503.17349v2 | 10 |
| 2025-03-20 | [FreeFlux: Understanding and Exploiting Layer-Specific Roles in RoPE-Based MMDiT for Versatile Image Editing](https://arxiv.org/abs/2503.16153v1) | 2503.16153v1 | 12 |
| 2025-03-20 | [MASH-VLM: Mitigating Action-Scene Hallucination in Video-LLMs through Disentangled Spatial-Temporal Representations](https://arxiv.org/abs/2503.15871v1) | 2503.15871v1 | 10 |
| 2025-03-19 | [DRoPE: Directional Rotary Position Embedding for Efficient Agent Interaction Modeling](https://arxiv.org/abs/2503.15029v1) | 2503.15029v1 | 15 |
| 2025-03-11 | [Context-aware Biases for Length Extrapolation](https://arxiv.org/abs/2503.08067v3) | 2503.08067v3 | 10 |
| 2025-03-06 | [HybridNorm: Towards Stable and Efficient Transformer Training via Hybrid Normalization](https://arxiv.org/abs/2503.04598v4) | 2503.04598v4 | 9 |
| 2025-03-06 | [Layer-Specific Scaling of Positional Encodings for Superior Long-Context Modeling](https://arxiv.org/abs/2503.04355v1) | 2503.04355v1 | 16 |
| 2025-03-06 | [LEDiT: Your Length-Extrapolatable Diffusion Transformer without Positional Encoding](https://arxiv.org/abs/2503.04344v3) | 2503.04344v3 | 14 |
| 2025-03-04 | [Graph Transformer with Disease Subgraph Positional Encoding for Improved Comorbidity Prediction](https://arxiv.org/abs/2503.03046v1) | 2503.03046v1 | 6 |
| 2025-03-04 | [Wyckoff Transformer: Generation of Symmetric Crystals](https://arxiv.org/abs/2503.02407v4) | 2503.02407v4 | 8 |
| 2025-03-03 | [Rotary Offset Features in Large Language Models](https://arxiv.org/abs/2503.01832v2) | 2503.01832v2 | 8 |
| 2025-03-03 | [EliteKV: Scalable KV Cache Compression via RoPE Frequency Selection and Joint Low-Rank Projection](https://arxiv.org/abs/2503.01586v1) | 2503.01586v1 | 12 |
| 2025-02-25 | [Self-Adjust Softmax](https://arxiv.org/abs/2502.18277v1) | 2502.18277v1 | 8 |
| 2025-02-24 | [Shakti-VLMs: Scalable Vision-Language Models for Enterprise AI](https://arxiv.org/abs/2502.17092v1) | 2502.17092v1 | 6 |
| 2025-02-19 | [Herglotz-NET: Implicit Neural Representation of Spherical Data with Harmonic Positional Encoding](https://arxiv.org/abs/2502.13777v3) | 2502.13777v3 | 10 |
| 2025-02-18 | [A$^2$ATS: Retrieval-Based KV Cache Reduction via Windowed Rotary Position Embedding and Query-Aware Vector Quantization](https://arxiv.org/abs/2502.12665v2) | 2502.12665v2 | 9 |
| 2025-02-17 | [Positional Encoding in Transformer-Based Time Series Models: A Survey](https://arxiv.org/abs/2502.12370v3) | 2502.12370v3 | 6 |
| 2025-02-17 | [HAAN: A Holistic Approach for Accelerating Normalization Operations in Large Language Models](https://arxiv.org/abs/2502.11832v1) | 2502.11832v1 | 6 |
| 2025-02-17 | [VRoPE: Rotary Position Embedding for Video Large Language Models](https://arxiv.org/abs/2502.11664v4) | 2502.11664v4 | 19 |
| 2025-02-16 | [The Rotary Position Embedding May Cause Dimension Inefficiency in Attention Heads for Long-Distance Retrieval](https://arxiv.org/abs/2502.11276v1) | 2502.11276v1 | 13 |
| 2025-02-16 | [CacheFocus: Dynamic Cache Re-Positioning for Efficient Retrieval-Augmented Generation](https://arxiv.org/abs/2502.11101v1) | 2502.11101v1 | 10 |
| 2025-02-16 | [CL-MFAP: A Contrastive Learning-Based Multimodal Foundation Model for Molecular Property Prediction and Antibiotic Screening](https://arxiv.org/abs/2502.11001v1) | 2502.11001v1 | 12 |
| 2025-02-14 | [F-StrIPE: Fast Structure-Informed Positional Encoding for Symbolic Music Generation](https://arxiv.org/abs/2502.10491v1) | 2502.10491v1 | 6 |
| 2025-02-13 | [AttentionSmithy: A Modular Framework for Rapid Transformer Development and Customization](https://arxiv.org/abs/2502.09503v2) | 2502.09503v2 | 6 |
| 2025-02-13 | [Can Classic GNNs Be Strong Baselines for Graph-level Tasks? Simple Architectures Meet Excellence](https://arxiv.org/abs/2502.09263v3) | 2502.09263v3 | 7 |
| 2025-02-10 | [Col-OLHTR: A Novel Framework for Multimodal Online Handwritten Text Recognition](https://arxiv.org/abs/2502.06100v1) | 2502.06100v1 | 6 |
| 2025-02-09 | [Provably Overwhelming Transformer Models with Designed Inputs](https://arxiv.org/abs/2502.06038v2) | 2502.06038v2 | 8 |
| 2025-02-07 | [VideoRoPE: What Makes for Good Video Rotary Position Embedding?](https://arxiv.org/abs/2502.05173v3) | 2502.05173v3 | 15 |
| 2025-02-05 | [Maximizing the Position Embedding for Vision Transformers with Global Average Pooling](https://arxiv.org/abs/2502.02919v1) | 2502.02919v1 | 7 |
| 2025-02-04 | [Learning the RoPEs: Better 2D and 3D Position Encodings with STRING](https://arxiv.org/abs/2502.02562v1) | 2502.02562v1 | 6 |
| 2025-02-04 | [Wavelet-based Positional Representation for Long Context](https://arxiv.org/abs/2502.02004v1) | 2502.02004v1 | 10 |
| 2025-02-04 | [On the Emergence of Position Bias in Transformers](https://arxiv.org/abs/2502.01951v4) | 2502.01951v4 | 8 |
| 2025-02-03 | [Massive Values in Self-Attention Modules are the Key to Contextual Knowledge Understanding](https://arxiv.org/abs/2502.01563v4) | 2502.01563v4 | 8 |
| 2025-02-03 | [FragmentNet: Adaptive Graph Fragmentation for Graph-to-Sequence Molecular Representation Learning](https://arxiv.org/abs/2502.01184v2) | 2502.01184v2 | 8 |
| 2025-02-03 | [Learning Efficient Positional Encodings with Graph Neural Networks](https://arxiv.org/abs/2502.01122v1) | 2502.01122v1 | 10 |
| 2025-02-01 | [PolarQuant: Leveraging Polar Transformation for Efficient Key Cache Quantization and Decoding Acceleration](https://arxiv.org/abs/2502.00527v2) | 2502.00527v2 | 6 |
| 2025-01-31 | [The role of positional encodings in the ARC benchmark](https://arxiv.org/abs/2502.00174v1) | 2502.00174v1 | 12 |
| 2025-01-30 | [Rope to Nope and Back Again: A New Hybrid Attention Strategy](https://arxiv.org/abs/2501.18795v2) | 2501.18795v2 | 14 |
| 2025-01-28 | [Toward Relative Positional Encoding in Spiking Transformers](https://arxiv.org/abs/2501.16745v3) | 2501.16745v3 | 10 |
| 2025-01-24 | [On the locality bias and results in the Long Range Arena](https://arxiv.org/abs/2501.14850v1) | 2501.14850v1 | 8 |
| 2025-01-24 | [Point-LN: A Lightweight Framework for Efficient Point Cloud Classification Using Non-Parametric Positional Encoding](https://arxiv.org/abs/2501.14238v2) | 2501.14238v2 | 6 |
| 2025-01-19 | [Generative Retrieval for Book search](https://arxiv.org/abs/2501.11034v1) | 2501.11034v1 | 8 |
| 2025-01-19 | [Advancing General Multimodal Capability of Vision-language Models with Pyramid-descent Visual Position Encoding](https://arxiv.org/abs/2501.10967v2) | 2501.10967v2 | 10 |
| 2025-01-10 | [Benchmarking Rotary Position Embeddings for Automatic Speech Recognition](https://arxiv.org/abs/2501.06051v2) | 2501.06051v2 | 13 |
| 2025-01-06 | [Analysis of mean-field models arising from self-attention dynamics in transformer architectures with layer normalization](https://arxiv.org/abs/2501.03096v2) | 2501.03096v2 | 6 |
| 2025-01-06 | [Self-Attention as a Parametric Endofunctor: A Categorical Framework for Transformer Architectures](https://arxiv.org/abs/2501.02931v2) | 2501.02931v2 | 8 |
| 2025-01-01 | [Rethinking Addressing in Language Models via Contexualized Equivariant Positional Encoding](https://arxiv.org/abs/2501.00712v2) | 2501.00712v2 | 6 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-31 | [Why Are Positional Encodings Nonessential for Deep Autoregressive Transformers? Revisiting a Petroglyph](https://arxiv.org/abs/2501.00659v2) | 2501.00659v2 | 10 |
| 2024-12-30 | [Position Information Emerges in Causal Transformers Without Positional Encodings via Similarity of Nearby Embeddings](https://arxiv.org/abs/2501.00073v1) | 2501.00073v1 | 6 |
| 2024-12-26 | [On the Expressiveness and Length Generalization of Selective State-Space Models on Regular Languages](https://arxiv.org/abs/2412.19350v2) | 2412.19350v2 | 8 |
| 2024-12-25 | [UNIC-Adapter: Unified Image-instruction Adapter with Multi-modal Transformer for Image Generation](https://arxiv.org/abs/2412.18928v1) | 2412.18928v1 | 6 |
| 2024-12-23 | [Theoretical Constraints on the Expressive Power of $\mathsf{RoPE}$-based Tensor Attention Transformers](https://arxiv.org/abs/2412.18040v1) | 2412.18040v1 | 12 |
| 2024-12-23 | [Fourier Position Embedding: Enhancing Attention's Periodic Extension for Length Generalization](https://arxiv.org/abs/2412.17739v4) | 2412.17739v4 | 11 |
| 2024-12-23 | [RoPE Attention Can Be Trained in Almost Linear Time](https://arxiv.org/abs/2412.17316v3) | 2412.17316v3 | 12 |
| 2024-12-16 | [Wonderful Matrices: Combining for a More Efficient and Effective Foundation Model Architecture](https://arxiv.org/abs/2412.11834v3) | 2412.11834v3 | 6 |
| 2024-12-11 | [Euclidean Fast Attention -- Machine Learning Global Atomic Representations at Linear Cost](https://arxiv.org/abs/2412.08541v2) | 2412.08541v2 | 8 |
| 2024-12-06 | [Mind the Time: Temporally-Controlled Multi-Event Video Generation](https://arxiv.org/abs/2412.05263v2) | 2412.05263v2 | 8 |
| 2024-12-04 | [Point-GN: A Non-Parametric Network Using Gaussian Positional Encoding for Point Cloud Classification](https://arxiv.org/abs/2412.03056v2) | 2412.03056v2 | 6 |
| 2024-11-23 | [DiM-Gestor: Co-Speech Gesture Generation with Adaptive Layer Normalization Mamba-2](https://arxiv.org/abs/2411.16729v1) | 2411.16729v1 | 6 |
| 2024-11-20 | [When Precision Meets Position: BFloat16 Breaks Down RoPE in Long-Context Training](https://arxiv.org/abs/2411.13476v2) | 2411.13476v2 | 10 |
| 2024-11-19 | [Benchmarking Positional Encodings for GNNs and Graph Transformers](https://arxiv.org/abs/2411.12732v2) | 2411.12732v2 | 6 |
| 2024-11-12 | [Circuit Complexity Bounds for RoPE-based Transformer Architecture](https://arxiv.org/abs/2411.07602v2) | 2411.07602v2 | 12 |
| 2024-11-12 | [FlowTS: Time Series Generation via Rectified Flow](https://arxiv.org/abs/2411.07506v3) | 2411.07506v3 | 10 |
| 2024-11-11 | [Fast and Robust Contextual Node Representation Learning over Dynamic Graphs](https://arxiv.org/abs/2411.07123v1) | 2411.07123v1 | 8 |
| 2024-11-07 | [The Fibonacci Network: A Simple Alternative for Positional Encoding](https://arxiv.org/abs/2411.05052v1) | 2411.05052v1 | 8 |
| 2024-11-06 | [Where Do We Stand with Implicit Neural Representations? A Technical and Performance Survey](https://arxiv.org/abs/2411.03688v2) | 2411.03688v2 | 8 |
| 2024-11-04 | [ElasTST: Towards Robust Varied-Horizon Forecasting with Elastic Time-Series Transformer](https://arxiv.org/abs/2411.01842v1) | 2411.01842v1 | 6 |
| 2024-10-30 | [WaveRoRA: Wavelet Rotary Route Attention for Multivariate Time Series Forecasting](https://arxiv.org/abs/2410.22649v2) | 2410.22649v2 | 6 |
| 2024-10-29 | [Scalable Message Passing Neural Networks: No Need for Attention in Large Graph Representation Learning](https://arxiv.org/abs/2411.00835v2) | 2411.00835v2 | 9 |
| 2024-10-28 | [HoPE: A Novel Positional Encoding Without Long-Term Decay for Enhanced Context Awareness and Extrapolation](https://arxiv.org/abs/2410.21216v2) | 2410.21216v2 | 10 |
| 2024-10-24 | [Homomorphism Counts as Structural Encodings for Graph Learning](https://arxiv.org/abs/2410.18676v2) | 2410.18676v2 | 8 |
| 2024-10-24 | [The Nature of Mathematical Modeling and Probabilistic Optimization Engineering in Generative AI](https://arxiv.org/abs/2410.18441v1) | 2410.18441v1 | 8 |
| 2024-10-23 | [Beyond Position: the emergence of wavelet-like properties in Transformers](https://arxiv.org/abs/2410.18067v4) | 2410.18067v4 | 16 |
| 2024-10-23 | [Music102: An $D_{12}$-equivariant transformer for chord progression accompaniment](https://arxiv.org/abs/2410.18151v2) | 2410.18151v2 | 8 |
| 2024-10-21 | [Moonshine: Speech Recognition for Live Transcription and Voice Commands](https://arxiv.org/abs/2410.15608v2) | 2410.15608v2 | 10 |
| 2024-10-16 | [Theoretical Analysis of Hierarchical Language Recognition and Generation by Transformers without Positional Encoding](https://arxiv.org/abs/2410.12413v1) | 2410.12413v1 | 6 |
| 2024-10-11 | [On the token distance modeling ability of higher RoPE attention dimension](https://arxiv.org/abs/2410.08703v2) | 2410.08703v2 | 16 |
| 2024-10-08 | [Round and Round We Go! What makes Rotary Positional Encodings useful?](https://arxiv.org/abs/2410.06205v3) | 2410.06205v3 | 10 |
| 2024-10-07 | [DAPE V2: Process Attention Score as Feature Map for Length Extrapolation](https://arxiv.org/abs/2410.04798v3) | 2410.04798v3 | 6 |
| 2024-10-07 | [Efficient transformer with reinforced position embedding for language models](https://arxiv.org/abs/2410.04731v1) | 2410.04731v1 | 7 |
| 2024-10-02 | [Extending Context Window of Large Language Models from a Distributional Perspective](https://arxiv.org/abs/2410.01490v2) | 2410.01490v2 | 10 |
| 2024-09-30 | [Preconditioning for Accelerated Gradient Descent Optimization and Regularization](https://arxiv.org/abs/2410.00232v2) | 2410.00232v2 | 8 |
| 2024-09-29 | [2D-TPE: Two-Dimensional Positional Encoding Enhances Table Understanding for Large Language Models](https://arxiv.org/abs/2409.19700v3) | 2409.19700v3 | 6 |
| 2024-09-27 | [Range-aware Positional Encoding via High-order Pretraining: Theory and Practice](https://arxiv.org/abs/2409.19117v1) | 2409.19117v1 | 10 |
| 2024-09-19 | [Geometric Interpretation of Layer Normalization and a Comparative Analysis with RMSNorm](https://arxiv.org/abs/2409.12951v2) | 2409.12951v2 | 12 |
| 2024-09-18 | [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191v2) | 2409.12191v2 | 10 |
| 2024-09-17 | [PropEnc: A Property Encoder for Graph Neural Networks](https://arxiv.org/abs/2409.11554v3) | 2409.11554v3 | 10 |
| 2024-09-15 | [GRIN: Zero-Shot Metric Depth with Pixel-Level Diffusion](https://arxiv.org/abs/2409.09896v1) | 2409.09896v1 | 8 |
| 2024-09-10 | [TeXBLEU: Automatic Metric for Evaluate LaTeX Format](https://arxiv.org/abs/2409.06639v3) | 2409.06639v3 | 8 |
| 2024-09-05 | [TC-LLaVA: Rethinking the Transfer from Image to Video Understanding with Temporal Considerations](https://arxiv.org/abs/2409.03206v1) | 2409.03206v1 | 10 |
| 2024-08-20 | [Want to train KANS at scale? Now UKAN!](https://arxiv.org/abs/2408.11200v4) | 2408.11200v4 | 10 |
| 2024-08-09 | [TrajFM: A Vehicle Trajectory Foundation Model for Region and Task Transferability](https://arxiv.org/abs/2408.15251v1) | 2408.15251v1 | 6 |
| 2024-08-01 | [DiM-Gesture: Co-Speech Gesture Generation with Adaptive Layer Normalization Mamba-2 framework](https://arxiv.org/abs/2408.00370v1) | 2408.00370v1 | 6 |
| 2024-07-30 | [What Are Good Positional Encodings for Directed Graphs?](https://arxiv.org/abs/2407.20912v3) | 2407.20912v3 | 6 |
| 2024-07-24 | [Dynamic Graph Transformer with Correlated Spatial-Temporal Positional Encoding](https://arxiv.org/abs/2407.16959v2) | 2407.16959v2 | 10 |
| 2024-07-16 | [Adversarial Robustness of Graph Transformers](https://arxiv.org/abs/2407.11764v2) | 2407.11764v2 | 8 |
| 2024-07-12 | [Learning High-Frequency Functions Made Easy with Sinusoidal Positional Encoding](https://arxiv.org/abs/2407.09370v2) | 2407.09370v2 | 6 |
| 2024-07-12 | [FlashNorm: Fast Normalization for Transformers](https://arxiv.org/abs/2407.09577v6) | 2407.09577v6 | 11 |
| 2024-07-01 | [Domain Influence in MRI Medical Image Segmentation: spatial versus k-space inputs](https://arxiv.org/abs/2407.01367v3) | 2407.01367v3 | 8 |
| 2024-06-19 | [Understanding the RoPE Extensions of Long-Context LLMs: An Attention Perspective](https://arxiv.org/abs/2406.13282v3) | 2406.13282v3 | 12 |
| 2024-06-18 | [Hierarchical Associative Memory, Parallelized MLP-Mixer, and Symmetry Breaking](https://arxiv.org/abs/2406.12220v1) | 2406.12220v1 | 8 |
| 2024-06-16 | [STAR: Scale-wise Text-conditioned AutoRegressive image generation](https://arxiv.org/abs/2406.10797v4) | 2406.10797v4 | 8 |
| 2024-06-14 | [LieRE: Lie Rotational Positional Encodings](https://arxiv.org/abs/2406.10322v5) | 2406.10322v5 | 10 |
| 2024-06-13 | [Alleviating Distortion in Image Generation via Multi-Resolution Diffusion Models and Time-Dependent Layer Normalization](https://arxiv.org/abs/2406.09416v2) | 2406.09416v2 | 6 |
| 2024-06-12 | [Learning interpretable positional encodings in transformers depends on initialization](https://arxiv.org/abs/2406.08272v4) | 2406.08272v4 | 6 |
| 2024-06-11 | [GridPE: A Grid Cell-Inspired Unified Position Embedding for Arbitrary-Dimensional Spaces](https://arxiv.org/abs/2406.07049v3) | 2406.07049v3 | 7 |
| 2024-06-04 | [What Improves the Generalization of Graph Transformers? A Theoretical Dive into the Self-attention and Positional Encoding](https://arxiv.org/abs/2406.01977v1) | 2406.01977v1 | 6 |
| 2024-06-03 | [On the Nonlinearity of Layer Normalization](https://arxiv.org/abs/2406.01255v1) | 2406.01255v1 | 6 |
| 2024-05-30 | [CycleFormer : TSP Solver Based on Language Modeling](https://arxiv.org/abs/2405.20042v4) | 2405.20042v4 | 8 |
| 2024-05-29 | [On the Role of Attention Masks and LayerNorm in Transformers](https://arxiv.org/abs/2405.18781v2) | 2405.18781v2 | 8 |
| 2024-05-28 | [I-LLM: Efficient Integer-Only Inference for Fully-Quantized Low-Bit Large Language Models](https://arxiv.org/abs/2405.17849v2) | 2405.17849v2 | 6 |
| 2024-05-27 | [Occlusion Handling in 3D Human Pose Estimation with Perturbed Positional Encoding](https://arxiv.org/abs/2405.17397v1) | 2405.17397v1 | 6 |
| 2024-05-25 | [The Power of Hard Attention Transformers on Data Sequences: A Formal Language Theoretic Perspective](https://arxiv.org/abs/2405.16166v2) | 2405.16166v2 | 8 |
| 2024-05-23 | [DAPE: Data-Adaptive Positional Encoding for Length Extrapolation](https://arxiv.org/abs/2405.14722v6) | 2405.14722v6 | 12 |
| 2024-05-21 | [Equipping Transformer with Random-Access Reading for Long-Context Understanding](https://arxiv.org/abs/2405.13216v1) | 2405.13216v1 | 8 |
| 2024-05-21 | [Quantum Positional Encodings for Graph Neural Networks](https://arxiv.org/abs/2406.06547v1) | 2406.06547v1 | 6 |
| 2024-05-16 | [Positional encoding is not the same as context: A study on positional encoding for sequential recommendation](https://arxiv.org/abs/2405.10436v2) | 2405.10436v2 | 7 |
| 2024-05-15 | [Improving Transformers using Faithful Positional Encoding](https://arxiv.org/abs/2405.09061v2) | 2405.09061v2 | 6 |
| 2024-05-13 | [A Semantic and Motion-Aware Spatiotemporal Transformer Network for Action Detection](https://arxiv.org/abs/2405.08204v1) | 2405.08204v1 | 8 |
| 2024-05-11 | [RoTHP: Rotary Position Embedding-based Transformer Hawkes Process](https://arxiv.org/abs/2405.06985v1) | 2405.06985v1 | 13 |
| 2024-05-09 | [Lumina-T2X: Transforming Text into Any Modality, Resolution, and Duration via Flow-based Large Diffusion Transformers](https://arxiv.org/abs/2405.05945v3) | 2405.05945v3 | 8 |
| 2024-04-29 | [PoPE: Legendre Orthogonal Polynomials Based Position Encoding for Large Language Models](https://arxiv.org/abs/2405.04585v1) | 2405.04585v1 | 8 |
| 2024-04-21 | [CKGConv: General Graph Convolution with Continuous Kernels](https://arxiv.org/abs/2404.13604v2) | 2404.13604v2 | 8 |
| 2024-04-18 | [LongEmbed: Extending Embedding Models for Long Context Retrieval](https://arxiv.org/abs/2404.12096v3) | 2404.12096v3 | 10 |
| 2024-04-18 | [SIGformer: Sign-aware Graph Transformer for Recommendation](https://arxiv.org/abs/2404.11982v3) | 2404.11982v3 | 8 |
| 2024-04-15 | [σ-GPTs: A New Approach to Autoregressive Models](https://arxiv.org/abs/2404.09562v2) | 2404.09562v2 | 8 |
| 2024-04-06 | [A Morphology-Based Investigation of Positional Encodings](https://arxiv.org/abs/2404.04530v2) | 2404.04530v2 | 6 |
| 2024-04-04 | [GP-MoLFormer: A Foundation Model For Molecular Generation](https://arxiv.org/abs/2405.04912v2) | 2405.04912v2 | 8 |
| 2024-03-28 | [HiRoPE: Length Extrapolation for Code Models Using Hierarchical Position](https://arxiv.org/abs/2403.19115v2) | 2403.19115v2 | 18 |
| 2024-03-26 | [EulerFormer: Sequential User Behavior Modeling with Complex Vector Attention](https://arxiv.org/abs/2403.17729v2) | 2403.17729v2 | 8 |
| 2024-03-26 | [MEP: Multiple Kernel Learning Enhancing Relative Positional Encoding Length Extrapolation](https://arxiv.org/abs/2403.17698v1) | 2403.17698v1 | 12 |
| 2024-03-26 | [Equipping Sketch Patches with Context-Aware Positional Encoding for Graphic Sketch Representation](https://arxiv.org/abs/2403.17525v2) | 2403.17525v2 | 6 |
| 2024-03-23 | [Geotokens and Geotransformers](https://arxiv.org/abs/2403.15940v1) | 2403.15940v1 | 10 |
| 2024-03-20 | [Rotary Position Embedding for Vision Transformer](https://arxiv.org/abs/2403.13298v2) | 2403.13298v2 | 17 |
| 2024-03-19 | [Pretraining Codomain Attention Neural Operators for Solving Multiphysics PDEs](https://arxiv.org/abs/2403.12553v3) | 2403.12553v3 | 6 |
| 2024-03-13 | [Structural Positional Encoding for knowledge integration in transformer-based medical process monitoring](https://arxiv.org/abs/2403.08836v1) | 2403.08836v1 | 6 |
| 2024-03-06 | [CrossNet: Leveraging Global, Cross-Band, Narrow-Band, and Positional Encoding for Single- and Multi-Channel Speaker Separation](https://arxiv.org/abs/2403.03411v1) | 2403.03411v1 | 6 |
| 2024-03-05 | [Found in the Middle: How Language Models Use Long Contexts Better via Plug-and-Play Positional Encoding](https://arxiv.org/abs/2403.04797v1) | 2403.04797v1 | 10 |
| 2024-03-04 | [Neural Redshift: Random Networks are not Random Functions](https://arxiv.org/abs/2403.02241v3) | 2403.02241v3 | 9 |
| 2024-02-29 | [Resonance RoPE: Improving Context Length Generalization of Large Language Models](https://arxiv.org/abs/2403.00071v2) | 2403.00071v2 | 12 |
| 2024-02-27 | [GIN-SD: Source Detection in Graphs with Incomplete Nodes via Positional Encoding and Attentive Fusion](https://arxiv.org/abs/2403.00014v1) | 2403.00014v1 | 6 |
| 2024-02-23 | [Seamless Human Motion Composition with Blended Positional Encodings](https://arxiv.org/abs/2402.15509v1) | 2402.15509v1 | 6 |
| 2024-02-22 | [Comparing Graph Transformers via Positional Encodings](https://arxiv.org/abs/2402.14202v4) | 2402.14202v4 | 6 |
| 2024-02-21 | [From Self-Attention to Markov Models: Unveiling the Dynamics of Generative Transformers](https://arxiv.org/abs/2402.13512v1) | 2402.13512v1 | 8 |
| 2024-02-20 | [Structure-informed Positional Encoding for Music Generation](https://arxiv.org/abs/2402.13301v2) | 2402.13301v2 | 6 |
| 2024-02-08 | [A Sampling Theory Perspective on Activations for Implicit Neural Representations](https://arxiv.org/abs/2402.05427v1) | 2402.05427v1 | 8 |
| 2024-02-01 | [Understanding the Expressive Power and Mechanisms of Transformer for Sequence Modeling](https://arxiv.org/abs/2402.00522v6) | 2402.00522v6 | 8 |
| 2024-01-31 | [Positional Encoding Helps Recurrent Neural Networks Handle a Large Vocabulary](https://arxiv.org/abs/2402.00236v5) | 2402.00236v5 | 6 |
| 2024-01-31 | [Graph Transformers without Positional Encodings](https://arxiv.org/abs/2401.17791v3) | 2401.17791v3 | 6 |
| 2024-01-29 | [Two Stones Hit One Bird: Bilevel Positional Encoding for Better Length Extrapolation](https://arxiv.org/abs/2401.16421v2) | 2401.16421v2 | 12 |
| 2024-01-29 | [Leveraging Positional Encoding for Robust Multi-Reference-Based Object 6D Pose Estimation](https://arxiv.org/abs/2401.16284v1) | 2401.16284v1 | 8 |
| 2024-01-22 | [MVSFormer++: Revealing the Devil in Transformer's Details for Multi-View Stereo](https://arxiv.org/abs/2401.11673v1) | 2401.11673v1 | 8 |
| 2024-01-18 | [An Empirical Study on the Impact of Positional Encoding in Transformer-based Monaural Speech Enhancement](https://arxiv.org/abs/2401.09686v2) | 2401.09686v2 | 8 |
| 2024-01-13 | [3QFP: Efficient neural implicit surface reconstruction using Tri-Quadtrees and Fourier feature Positional encoding](https://arxiv.org/abs/2401.07164v2) | 2401.07164v2 | 6 |
| 2024-01-13 | [Extending LLMs' Context Window with 100 Samples](https://arxiv.org/abs/2401.07004v1) | 2401.07004v1 | 10 |
| 2024-01-09 | [Cuff-less Arterial Blood Pressure Waveform Synthesis from Single-site PPG using Transformer & Frequency-domain Learning](https://arxiv.org/abs/2401.05452v2) | 2401.05452v2 | 8 |
| 2024-01-02 | [On Optimal Sampling for Learning SDF Using MLPs Equipped with Positional Encoding](https://arxiv.org/abs/2401.01391v2) | 2401.01391v2 | 6 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-28 | [Length Extrapolation of Transformers: A Survey from the Perspective of Positional Encoding](https://arxiv.org/abs/2312.17044v5) | 2312.17044v5 | 12 |
| 2023-12-26 | [Algebraic Positional Encodings](https://arxiv.org/abs/2312.16045v3) | 2312.16045v3 | 10 |
| 2023-12-22 | [How Smooth Is Attention?](https://arxiv.org/abs/2312.14820v2) | 2312.14820v2 | 8 |
| 2023-12-16 | [Conformer-Based Speech Recognition On Extreme Edge-Computing Devices](https://arxiv.org/abs/2312.10359v3) | 2312.10359v3 | 6 |
| 2023-12-11 | [HyPE-GT: where Graph Transformers meet Hyperbolic Positional Encodings](https://arxiv.org/abs/2312.06576v2) | 2312.06576v2 | 6 |
| 2023-12-07 | [Fortify the Shortest Stave in Attention: Enhancing Context Awareness of Large Language Models for Effective Tool Use](https://arxiv.org/abs/2312.04455v4) | 2312.04455v4 | 6 |
| 2023-12-04 | [Expressive Sign Equivariant Networks for Spectral Geometric Learning](https://arxiv.org/abs/2312.02339v1) | 2312.02339v1 | 8 |
| 2023-11-24 | [Effective Structural Encodings via Local Curvature Profiles](https://arxiv.org/abs/2311.14864v2) | 2311.14864v2 | 8 |
| 2023-11-22 | [Positional Description Matters for Transformers Arithmetic](https://arxiv.org/abs/2311.14737v1) | 2311.14737v1 | 8 |
| 2023-11-20 | [Mixing-Denoising Generalizable Occupancy Networks](https://arxiv.org/abs/2311.12125v1) | 2311.12125v1 | 8 |
| 2023-11-10 | [Improved Positional Encoding for Implicit Neural Representation based Compact Data Representation](https://arxiv.org/abs/2311.06059v1) | 2311.06059v1 | 6 |
| 2023-11-06 | [APGL4SR: A Generic Framework with Adaptive and Personalized Global Collaborative Information in Sequential Recommendation](https://arxiv.org/abs/2311.02816v1) | 2311.02816v1 | 8 |
| 2023-10-30 | [HyPE: Attention with Hyperbolic Biases for Relative Positional Encoding](https://arxiv.org/abs/2310.19676v2) | 2310.19676v2 | 10 |
| 2023-10-27 | [Style Description based Text-to-Speech with Conditional Prosodic Layer Normalization based Diffusion GAN](https://arxiv.org/abs/2310.18169v1) | 2310.18169v1 | 6 |
| 2023-10-27 | [Positional Encoding-based Resident Identification in Multi-resident Smart Homes](https://arxiv.org/abs/2310.17836v1) | 2310.17836v1 | 6 |
| 2023-10-25 | [CLEX: Continuous Length Extrapolation for Large Language Models](https://arxiv.org/abs/2310.16450v3) | 2310.16450v3 | 12 |
| 2023-10-19 | [The Locality and Symmetry of Positional Encodings](https://arxiv.org/abs/2310.12864v1) | 2310.12864v1 | 10 |
| 2023-10-18 | [Position Interpolation Improves ALiBi Extrapolation](https://arxiv.org/abs/2310.13017v1) | 2310.13017v1 | 10 |
| 2023-10-17 | [Enhanced Transformer Architecture for Natural Language Processing](https://arxiv.org/abs/2310.10930v1) | 2310.10930v1 | 9 |
| 2023-10-16 | [GTA: A Geometry-Aware Attention Mechanism for Multi-View Transformers](https://arxiv.org/abs/2310.10375v3) | 2310.10375v3 | 8 |
| 2023-10-08 | [Scaling Laws of RoPE-based Extrapolation](https://arxiv.org/abs/2310.05209v2) | 2310.05209v2 | 12 |
| 2023-10-04 | [Spherical Position Encoding for Transformers](https://arxiv.org/abs/2310.04454v1) | 2310.04454v1 | 10 |
| 2023-10-04 | [On the Stability of Expressive Positional Encodings for Graphs](https://arxiv.org/abs/2310.02579v3) | 2310.02579v3 | 10 |
| 2023-10-03 | [Mel-Band RoFormer for Music Source Separation](https://arxiv.org/abs/2310.01809v1) | 2310.01809v1 | 10 |
| 2023-09-26 | [Local Positional Encoding for Multi-Layer Perceptrons](https://arxiv.org/abs/2309.15101v2) | 2309.15101v2 | 6 |
| 2023-09-15 | [CoCA: Fusing Position Embedding with Collinear Constrained Attention in Transformers for Long Context Window Extending](https://arxiv.org/abs/2309.08646v3) | 2309.08646v3 | 11 |
| 2023-09-13 | [Traveling Words: A Geometric Interpretation of Transformers](https://arxiv.org/abs/2309.07315v2) | 2309.07315v2 | 8 |
| 2023-09-11 | [CONFLATOR: Incorporating Switching Point based Rotatory Positional Encodings for Code-Mixed Language Modeling](https://arxiv.org/abs/2309.05270v2) | 2309.05270v2 | 6 |
| 2023-09-06 | [MLN-net: A multi-source medical image segmentation method for clustered microcalcifications using multiple layer normalization](https://arxiv.org/abs/2309.02742v2) | 2309.02742v2 | 6 |
| 2023-09-05 | [Music Source Separation with Band-Split RoPE Transformer](https://arxiv.org/abs/2309.02612v2) | 2309.02612v2 | 12 |
| 2023-08-31 | [YaRN: Efficient Context Window Extension of Large Language Models](https://arxiv.org/abs/2309.00071v3) | 2309.00071v3 | 10 |
| 2023-08-18 | [Understanding the Role of Layer Normalization in Label-Skewed Federated Learning](https://arxiv.org/abs/2308.09565v2) | 2308.09565v2 | 6 |
| 2023-08-11 | [Positional Encodings for Light Curve Transformers: Playing with Positions and Attention](https://arxiv.org/abs/2308.06404v1) | 2308.06404v1 | 6 |
| 2023-07-19 | [Exploring Transformer Extrapolation](https://arxiv.org/abs/2307.10156v2) | 2307.10156v2 | 12 |
| 2023-07-18 | [Linearized Relative Positional Encoding](https://arxiv.org/abs/2307.09270v1) | 2307.09270v1 | 6 |
| 2023-07-11 | [Image Reconstruction using Enhanced Vision Transformer](https://arxiv.org/abs/2307.05616v1) | 2307.05616v1 | 10 |
| 2023-07-06 | [Revisiting Computer-Aided Tuberculosis Diagnosis](https://arxiv.org/abs/2307.02848v2) | 2307.02848v2 | 8 |
| 2023-06-19 | [SGFormer: Simplifying and Empowering Transformers for Large-Graph Representations](https://arxiv.org/abs/2306.10759v5) | 2306.10759v5 | 8 |
| 2023-06-13 | [Reviving Shift Equivariance in Vision Transformers](https://arxiv.org/abs/2306.07470v1) | 2306.07470v1 | 8 |
| 2023-06-11 | [2-D SSM: A General Spatial Layer for Visual Transformers](https://arxiv.org/abs/2306.06635v1) | 2306.06635v1 | 6 |
| 2023-05-31 | [The Impact of Positional Encoding on Length Generalization in Transformers](https://arxiv.org/abs/2305.19466v2) | 2305.19466v2 | 8 |
| 2023-05-26 | [Randomized Positional Encodings Boost Length Generalization of Transformers](https://arxiv.org/abs/2305.16843v1) | 2305.16843v1 | 6 |
| 2023-05-24 | [Pre-RMSNorm and Pre-CRMSNorm Transformers: Equivalent and Efficient Pre-LN Transformers](https://arxiv.org/abs/2305.14858v2) | 2305.14858v2 | 10 |
| 2023-05-24 | [What functions can Graph Neural Networks compute on random graphs? The role of Positional Encoding](https://arxiv.org/abs/2305.14814v1) | 2305.14814v1 | 8 |
| 2023-05-16 | [Exploring the Impact of Layer Normalization for Zero-shot Neural Machine Translation](https://arxiv.org/abs/2305.09312v1) | 2305.09312v1 | 7 |
| 2023-05-09 | [PET-NeuS: Positional Encoding Tri-Planes for Neural Surfaces](https://arxiv.org/abs/2305.05594v1) | 2305.05594v1 | 6 |
| 2023-05-04 | [On the Expressivity Role of LayerNorm in Transformers' Attention](https://arxiv.org/abs/2305.02582v2) | 2305.02582v2 | 8 |
| 2023-04-26 | [Technical Report: Impact of Position Bias on Language Models in Token Classification](https://arxiv.org/abs/2304.13567v4) | 2304.13567v4 | 10 |
| 2023-04-19 | [LipsFormer: Introducing Lipschitz Continuity to Vision Transformers](https://arxiv.org/abs/2304.09856v1) | 2304.09856v1 | 10 |
| 2023-04-14 | [Memory Efficient Diffusion Probabilistic Models via Patch-based Generation](https://arxiv.org/abs/2304.07087v1) | 2304.07087v1 | 8 |
| 2023-03-20 | [Polynomial Implicit Neural Representations For Large Diverse Datasets](https://arxiv.org/abs/2303.11424v1) | 2303.11424v1 | 6 |
| 2023-03-06 | [Graph Positional Encoding via Random Feature Propagation](https://arxiv.org/abs/2303.02918v3) | 2303.02918v3 | 6 |
| 2023-03-04 | [NeuDA: Neural Deformable Anchor for High-Fidelity Implicit Surface Reconstruction](https://arxiv.org/abs/2303.02375v2) | 2303.02375v2 | 8 |
| 2023-02-20 | [FormerTime: Hierarchical Multi-Scale Representations for Multivariate Time Series Classification](https://arxiv.org/abs/2302.09818v1) | 2302.09818v1 | 8 |
| 2023-02-17 | [Multiresolution Graph Transformers and Wavelet Positional Encoding for Learning Hierarchical Structures](https://arxiv.org/abs/2302.08647v4) | 2302.08647v4 | 10 |
| 2023-02-13 | [A Study on ReLU and Softmax in Transformer](https://arxiv.org/abs/2302.06461v1) | 2302.06461v1 | 8 |
| 2023-02-08 | [Attending to Graph Transformers](https://arxiv.org/abs/2302.04181v3) | 2302.04181v3 | 8 |
| 2023-02-07 | [On the Ideal Number of Groups for Isometric Gradient Propagation](https://arxiv.org/abs/2302.03193v1) | 2302.03193v1 | 8 |
| 2023-02-03 | [Learning a Fourier Transform for Linear Relative Positional Encodings in Transformers](https://arxiv.org/abs/2302.01925v2) | 2302.01925v2 | 6 |
| 2023-01-25 | [Faster DAN: Multi-target Queries with Document Positional Encoding for End-to-end Handwritten Document Recognition](https://arxiv.org/abs/2301.10593v1) | 2301.10593v1 | 6 |
| 2023-01-14 | [Understanding the Spectral Bias of Coordinate Based MLPs Via Training Dynamics](https://arxiv.org/abs/2301.05816v4) | 2301.05816v4 | 8 |

### 2022
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2022-12-13 | [Comparing the Decision-Making Mechanisms by Transformers and CNNs via Explanation Methods](https://arxiv.org/abs/2212.06872v5) | 2212.06872v5 | 8 |
| 2022-12-10 | [Position Embedding Needs an Independent Layer Normalization](https://arxiv.org/abs/2212.05262v2) | 2212.05262v2 | 9 |
| 2022-11-30 | [Attention-Based Depth Distillation with 3D-Aware Positional Encoding for Monocular 3D Object Detection](https://arxiv.org/abs/2211.16779v2) | 2211.16779v2 | 6 |
| 2022-11-27 | [3DPPE: 3D Point Positional Encoding for Multi-Camera 3D Object Detection Transformers](https://arxiv.org/abs/2211.14710v3) | 2211.14710v3 | 6 |
| 2022-11-25 | [PIP: Positional-encoding Image Prior](https://arxiv.org/abs/2211.14298v3) | 2211.14298v3 | 8 |
| 2022-11-23 | [Learning Regularized Positional Encoding for Molecular Prediction](https://arxiv.org/abs/2211.12773v1) | 2211.12773v1 | 10 |
| 2022-11-16 | [Parameter-Efficient Tuning on Layer Normalization for Pre-trained Language Models](https://arxiv.org/abs/2211.08682v3) | 2211.08682v3 | 6 |
| 2022-11-14 | [ParCNetV2: Oversized Kernel with Enhanced Attention](https://arxiv.org/abs/2211.07157v3) | 2211.07157v3 | 8 |
| 2022-11-08 | [DepthFormer: Multimodal Positional Encodings and Cross-Input Attention for Transformer-Based Segmentation Networks](https://arxiv.org/abs/2211.04188v2) | 2211.04188v2 | 6 |
| 2022-10-28 | [Generalized Laplacian Positional Encoding for Graph Representation Learning](https://arxiv.org/abs/2210.15956v2) | 2210.15956v2 | 10 |
| 2022-10-07 | [Rethinking Normalization Methods in Federated Learning](https://arxiv.org/abs/2210.03277v1) | 2210.03277v1 | 9 |
| 2022-09-28 | [Breaking Time Invariance: Assorted-Time Normalization for RNNs](https://arxiv.org/abs/2209.14439v1) | 2209.14439v1 | 9 |
| 2022-09-19 | [Batch Layer Normalization, A new normalization layer for CNNs and RNN](https://arxiv.org/abs/2209.08898v1) | 2209.08898v1 | 6 |
| 2022-09-13 | [Document-aware Positional Encoding and Linguistic-guided Encoding for Abstractive Multi-document Summarization](https://arxiv.org/abs/2209.05929v1) | 2209.05929v1 | 6 |
| 2022-08-30 | [Persistence Initialization: A novel adaptation of the Transformer architecture for Time Series Forecasting](https://arxiv.org/abs/2208.14236v1) | 2208.14236v1 | 7 |
| 2022-08-01 | [Multi-spectral Vehicle Re-identification with Cross-directional Consistency Network and a High-quality Benchmark](https://arxiv.org/abs/2208.00632v2) | 2208.00632v2 | 8 |
| 2022-07-15 | [Parameterization of Cross-Token Relations with Relative Positional Encoding for Vision MLP](https://arxiv.org/abs/2207.07284v2) | 2207.07284v2 | 6 |
| 2022-07-10 | [Deep Transformer Model with Pre-Layer Normalization for COVID-19 Growth Prediction](https://arxiv.org/abs/2207.06356v1) | 2207.06356v1 | 6 |
| 2022-04-23 | [Investigating Neural Architectures by Synthetic Dataset Design](https://arxiv.org/abs/2204.11045v1) | 2204.11045v1 | 8 |
| 2022-04-18 | [Dynamic Position Encoding for Transformers](https://arxiv.org/abs/2204.08142v2) | 2204.08142v2 | 6 |
| 2022-03-30 | [Transformer Language Models without Positional Encodings Still Learn Positional Information](https://arxiv.org/abs/2203.16634v2) | 2203.16634v2 | 6 |
| 2022-03-21 | [An Intellectual Property Entity Recognition Method Based on Transformer and Technological Word Information](https://arxiv.org/abs/2203.10717v1) | 2203.10717v1 | 6 |
| 2022-03-17 | [Generalized Classification of Satellite Image Time Series with Thermal Positional Encoding](https://arxiv.org/abs/2203.09175v2) | 2203.09175v2 | 10 |
| 2022-03-14 | [XYLayoutLM: Towards Layout-Aware Multimodal Networks For Visually-Rich Document Understanding](https://arxiv.org/abs/2203.06947v2) | 2203.06947v2 | 6 |
| 2022-03-02 | [Incremental Transformer Structure Enhanced Image Inpainting with Masking Positional Encoding](https://arxiv.org/abs/2203.00867v2) | 2203.00867v2 | 7 |
| 2022-03-01 | [Equivariant and Stable Positional Encoding for More Powerful Graph Neural Networks](https://arxiv.org/abs/2203.00199v5) | 2203.00199v5 | 6 |
| 2022-02-17 | [Improving English to Sinhala Neural Machine Translation using Part-of-Speech Tag](https://arxiv.org/abs/2202.08882v1) | 2202.08882v1 | 8 |
| 2022-01-30 | [GRPE: Relative Positional Encoding for Graph Transformer](https://arxiv.org/abs/2201.12787v3) | 2201.12787v3 | 6 |
| 2022-01-29 | [Rewiring with Positional Encodings for Graph Neural Networks](https://arxiv.org/abs/2201.12674v4) | 2201.12674v4 | 6 |

### 2021
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2021-12-28 | [Synchronized Audio-Visual Frames with Fractional Positional Encoding for Transformers in Video-to-Text Translation](https://arxiv.org/abs/2112.14088v1) | 2112.14088v1 | 6 |
| 2021-12-12 | [Towards More Efficient Insertion Transformer with Fractional Positional Encoding](https://arxiv.org/abs/2112.06295v3) | 2112.06295v3 | 6 |
| 2021-12-10 | [Enhancing Multi-Scale Implicit Learning in Image Super-Resolution with Integrated Positional Encoding](https://arxiv.org/abs/2112.05756v1) | 2112.05756v1 | 6 |
| 2021-11-12 | [PESTO: Switching Point based Dynamic and Relative Positional Encoding for Code-Mixed Languages](https://arxiv.org/abs/2111.06599v1) | 2111.06599v1 | 10 |
| 2021-10-26 | [Geometric Transformer for End-to-End Molecule Properties Prediction](https://arxiv.org/abs/2110.13721v3) | 2110.13721v3 | 6 |
| 2021-10-15 | [Graph Neural Networks with Learnable Structural and Positional Representations](https://arxiv.org/abs/2110.07875v2) | 2110.07875v2 | 8 |
| 2021-10-13 | [Study of positional encoding approaches for Audio Spectrogram Transformers](https://arxiv.org/abs/2110.06999v1) | 2110.06999v1 | 6 |
| 2021-10-08 | [Cross-speaker Emotion Transfer Based on Speaker Condition Layer Normalization and Semi-Supervised Training in Text-To-Speech](https://arxiv.org/abs/2110.04153v2) | 2110.04153v2 | 6 |
| 2021-09-15 | [Incorporating Residual and Normalization Layers into Analysis of Masked Language Models](https://arxiv.org/abs/2109.07152v1) | 2109.07152v1 | 6 |
| 2021-09-11 | [The Impact of Positional Encodings on Multilingual Compression](https://arxiv.org/abs/2109.05388v1) | 2109.05388v1 | 6 |
| 2021-08-11 | [Variable-Length Music Score Infilling via XLNet and Musically Specialized Positional Encoding](https://arxiv.org/abs/2108.05064v1) | 2108.05064v1 | 6 |
| 2021-07-29 | [Using Perturbed Length-aware Positional Encoding for Non-autoregressive Neural Machine Translation](https://arxiv.org/abs/2107.13689v1) | 2107.13689v1 | 6 |
| 2021-07-20 | [Assessment of Self-Attention on Learned Features For Sound Event Localization and Detection](https://arxiv.org/abs/2107.09388v2) | 2107.09388v2 | 6 |
| 2021-07-13 | [Conformer-based End-to-end Speech Recognition With Rotary Position Embedding](https://arxiv.org/abs/2107.05907v1) | 2107.05907v1 | 13 |
| 2021-07-12 | [The Brownian motion in the transformer model](https://arxiv.org/abs/2107.05264v1) | 2107.05264v1 | 8 |
| 2021-07-06 | [Rethinking Positional Encoding](https://arxiv.org/abs/2107.02561v3) | 2107.02561v3 | 6 |
| 2021-07-05 | [Vision Xformers: Efficient Attention for Image Classification](https://arxiv.org/abs/2107.02239v4) | 2107.02239v4 | 10 |
| 2021-07-02 | [Exploiting Positional Information for Session-based Recommendation](https://arxiv.org/abs/2107.00846v2) | 2107.00846v2 | 8 |
| 2021-07-02 | [Cross-view Geo-localization with Evolving Transformer](https://arxiv.org/abs/2107.00842v2) | 2107.00842v2 | 8 |
| 2021-06-23 | [Stable, Fast and Accurate: Kernelized Attention with Relative Positional Encoding](https://arxiv.org/abs/2106.12566v2) | 2106.12566v2 | 10 |
| 2021-06-21 | [ROPE: Reading Order Equivariant Positional Encoding for Graph-based Document Information Extraction](https://arxiv.org/abs/2106.10786v1) | 2106.10786v1 | 12 |
| 2021-06-17 | [Large-Scale Chemical Language Representations Capture Molecular Structure and Properties](https://arxiv.org/abs/2106.09553v3) | 2106.09553v3 | 6 |
| 2021-06-16 | [Temporal Convolution Networks with Positional Encoding for Evoked Expression Estimation](https://arxiv.org/abs/2106.08596v1) | 2106.08596v1 | 6 |
| 2021-06-07 | [Rethinking Graph Transformers with Spectral Attention](https://arxiv.org/abs/2106.03893v3) | 2106.03893v3 | 8 |
| 2021-06-05 | [Learnable Fourier Features for Multi-Dimensional Spatial Positional Encoding](https://arxiv.org/abs/2106.02795v3) | 2106.02795v3 | 6 |
| 2021-06-03 | [Spline Positional Encoding for Learning 3D Implicit Signed Distance Fields](https://arxiv.org/abs/2106.01553v2) | 2106.01553v2 | 6 |
| 2021-05-18 | [Relative Positional Encoding for Transformers with Linear Complexity](https://arxiv.org/abs/2105.08399v2) | 2105.08399v2 | 6 |
| 2021-05-15 | [Rethinking Skip Connection with Layer Normalization in Transformers and ResNets](https://arxiv.org/abs/2105.07205v1) | 2105.07205v1 | 6 |
| 2021-05-06 | [Speech Enhancement using Separable Polling Attention and Global Layer Normalization followed with PReLU](https://arxiv.org/abs/2105.02509v1) | 2105.02509v1 | 6 |
| 2021-04-20 | [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864v5) | 2104.09864v5 | 13 |
| 2021-04-18 | [A Simple and Effective Positional Encoding for Transformers](https://arxiv.org/abs/2104.08698v2) | 2104.08698v2 | 6 |
| 2021-03-29 | [CvT: Introducing Convolutions to Vision Transformers](https://arxiv.org/abs/2103.15808v1) | 2103.15808v1 | 8 |
| 2021-03-12 | [PLADE-Net: Towards Pixel-Level Accuracy for Self-Supervised Single-View Depth Estimation with Neural Positional Encoding and Distilled Matting Loss](https://arxiv.org/abs/2103.07362v1) | 2103.07362v1 | 10 |
| 2021-02-25 | [Investigating the Limitations of Transformers with Simple Arithmetic Tasks](https://arxiv.org/abs/2102.13019v3) | 2102.13019v3 | 8 |
| 2021-02-22 | [Conditional Positional Encodings for Vision Transformers](https://arxiv.org/abs/2102.10882v3) | 2102.10882v3 | 6 |
| 2021-01-11 | [Context- and Sequence-Aware Convolutional Recurrent Encoder for Neural Machine Translation](https://arxiv.org/abs/2101.04030v2) | 2101.04030v2 | 6 |

### 2020
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2020-12-17 | [A Generalization of Transformer Networks to Graphs](https://arxiv.org/abs/2012.09699v2) | 2012.09699v2 | 12 |
| 2020-12-09 | [Positional Encoding as Spatial Inductive Bias in GANs](https://arxiv.org/abs/2012.05217v1) | 2012.05217v1 | 6 |
| 2020-10-10 | [What Do Position Embeddings Learn? An Empirical Study of Pre-Trained Language Model Positional Encoding](https://arxiv.org/abs/2010.04903v1) | 2010.04903v1 | 13 |
| 2020-09-28 | [Improve Transformer Models with Better Relative Position Embeddings](https://arxiv.org/abs/2009.13658v1) | 2009.13658v1 | 7 |
| 2020-09-23 | [On the Ability and Limitations of Transformers to Recognize Formal Languages](https://arxiv.org/abs/2009.11264v2) | 2009.11264v2 | 8 |
| 2020-06-28 | [Rethinking Positional Encoding in Language Pre-training](https://arxiv.org/abs/2006.15595v4) | 2006.15595v4 | 6 |
| 2020-06-23 | [Keyframe Segmentation and Positional Encoding for Video-guided Machine Translation Challenge 2020](https://arxiv.org/abs/2006.12799v1) | 2006.12799v1 | 6 |
| 2020-06-11 | [Optimization Theory for ReLU Neural Networks Trained with Normalization Layers](https://arxiv.org/abs/2006.06878v1) | 2006.06878v1 | 9 |
| 2020-05-20 | [Relative Positional Encoding for Speech Recognition and Direct Translation](https://arxiv.org/abs/2005.09940v1) | 2005.09940v1 | 6 |
| 2020-05-11 | [Normalized Convolutional Neural Network](https://arxiv.org/abs/2005.05274v4) | 2005.05274v4 | 7 |
| 2020-02-12 | [On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745v2) | 2002.04745v2 | 7 |

### 2019
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2019-12-20 | [Are Transformers universal approximators of sequence-to-sequence functions?](https://arxiv.org/abs/1912.10077v2) | 1912.10077v2 | 8 |
| 2019-11-16 | [Understanding and Improving Layer Normalization](https://arxiv.org/abs/1911.07013v1) | 1911.07013v1 | 6 |
| 2019-10-16 | [Root Mean Square Layer Normalization](https://arxiv.org/abs/1910.07467v1) | 1910.07467v1 | 14 |
| 2019-08-21 | [U-Net Training with Instance-Layer Normalization](https://arxiv.org/abs/1908.08466v2) | 1908.08466v2 | 6 |
| 2019-06-05 | [Learning Deep Transformer Models for Machine Translation](https://arxiv.org/abs/1906.01787v1) | 1906.01787v1 | 8 |
| 2019-05-23 | [Positional Encoding by Robots with Non-Rigid Movements](https://arxiv.org/abs/1905.09786v1) | 1905.09786v1 | 6 |
| 2019-04-16 | [Positional Encoding to Control Output Sequence Length](https://arxiv.org/abs/1904.07418v1) | 1904.07418v1 | 6 |
| 2019-04-06 | [Instance-Level Meta Normalization](https://arxiv.org/abs/1904.03516v1) | 1904.03516v1 | 9 |

### 2018
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2018-07-09 | [Position-aware Self-attention with Relative Positional Encodings for Slot Filling](https://arxiv.org/abs/1807.03052v1) | 1807.03052v1 | 6 |

### 2017
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2017-07-19 | [Dynamic Layer Normalization for Adaptive Neural Acoustic Modeling in Speech Recognition](https://arxiv.org/abs/1707.06065v1) | 1707.06065v1 | 6 |

### 2016
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2016-07-21 | [Layer Normalization](https://arxiv.org/abs/1607.06450v1) | 1607.06450v1 | 6 |

<!-- table:end papers -->
