# 🏋️ 优化器与训练动力学（Optimizers & Training）

> 架构决定损失曲面的形状，优化器决定你在上面怎么走。

Adam 统治了十年，但 LLM 时代的内存墙和规模墙逼出了新一代：
省状态的 Adafactor、二阶近似的 Shampoo/SOAP、牛顿方向的 Sophia、
以及 2024 年后异军突起的 Muon。μP 则从另一个维度回答"超参数怎么随规模迁移"。
这条赛道收录优化算法与训练动力学的关键节点。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Adam: A Method for Stochastic Optimization | [1412.6980](https://arxiv.org/abs/1412.6980) | 2014 | 自适应学习率的十年标准 |
| Decoupled Weight Decay Regularization (AdamW) | [1711.05101](https://arxiv.org/abs/1711.05101) | 2017 | 权重衰减与梯度解耦，LLM 训练的默认优化器 |
| Adafactor: Adaptive Learning Rates with Sublinear Memory Cost | [1804.04235](https://arxiv.org/abs/1804.04235) | 2018 | 因式分解二阶矩，优化器状态显存大减 |
| Shampoo: Preconditioned Stochastic Tensor Optimization | [1802.09568](https://arxiv.org/abs/1802.09568) | 2018 | 张量级二阶预条件的开端 |
| Large Batch Optimization for Deep Learning (LAMB) | [1904.00962](https://arxiv.org/abs/1904.00962) | 2019 | 分层自适应让超大 batch 可用 |
| Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer (μP) | [2203.03466](https://arxiv.org/abs/2203.03466) | 2022 | μP：小模型上调参，零样本迁移到大模型 |
| Symbolic Discovery of Optimization Algorithms (Lion) | [2302.06675](https://arxiv.org/abs/2302.06675) | 2023 | 符号搜索发现的符号动量优化器 |
| Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training | [2305.14342](https://arxiv.org/abs/2305.14342) | 2023 | 轻量二阶信息加速 LLM 预训练 |
| Schedule-Free Optimization (The Road Less Scheduled) | [2405.15682](https://arxiv.org/abs/2405.15682) | 2024 | 扔掉学习率 schedule，评估点即插即用 |
| SOAP: Improving and Stabilizing Shampoo using Adam | [2409.11321](https://arxiv.org/abs/2409.11321) | 2024 | 在 Shampoo 预条件子空间里跑 Adam |
| Muon is Scalable for LLM Training | [2502.16982](https://arxiv.org/abs/2502.16982) | 2025 | 牛顿-舒尔茨正交化动量，Muon 大规模验证 |

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-12 | [Factored One-sided Adam-Moment for Practical and Scalable SOAP](https://arxiv.org/abs/2611.16905v1) | 2611.16905v1 | 17 |
| 2026-11-12 | [Natural Gradient Learning in Predictive Coding through Lateral Circuits](https://arxiv.org/abs/2611.16666v1) | 2611.16666v1 | 9 |
| 2026-11-12 | [When and How SignSGD Outperforms SGD: A Functional Scaling Law Perspective](https://arxiv.org/abs/2611.16560v1) | 2611.16560v1 | 7 |
| 2026-11-12 | [SS-HSDP: Efficient and Flexible Sharded Data Parallelism via Runtime-Update Decoupling](https://arxiv.org/abs/2611.16467v1) | 2611.16467v1 | 8 |
| 2026-11-12 | [SoScale: Second-Order Scale Search for FP4 Quantization](https://arxiv.org/abs/2611.16426v1) | 2611.16426v1 | 6 |
| 2026-11-11 | [Machine learning and high accuracy: Neural preconditioners for computational gravity](https://arxiv.org/abs/2611.16106v1) | 2611.16106v1 | 7 |
| 2026-11-11 | [Characterizing the Edge of Stability in Variational Training Without Priors](https://arxiv.org/abs/2611.15990v1) | 2611.15990v1 | 7 |
| 2026-11-11 | [Optimal higher order convergence rates for the MUON optimizer](https://arxiv.org/abs/2611.15825v1) | 2611.15825v1 | 16 |
| 2026-11-11 | [Learning Rate Transfer and Feature Learning Across Depth for Constrained Spectral Optimizers: Complete Scion](https://arxiv.org/abs/2611.15291v1) | 2611.15291v1 | 11 |
| 2026-11-11 | [Probe-Based Routing for Join Optimizer Selection](https://arxiv.org/abs/2611.15263v1) | 2611.15263v1 | 6 |
| 2026-11-10 | [Weak Quasi-Convexity: First- and Second-Order Conditions, Monotonicity, and Quadratic Functions](https://arxiv.org/abs/2611.13878v1) | 2611.13878v1 | 7 |
| 2026-11-10 | [Exact (Non-)Accelerations of Heavy-Ball Discretizations](https://arxiv.org/abs/2611.13584v1) | 2611.13584v1 | 7 |
| 2026-11-10 | [Closing the BF16-FP16 Convergence Speed Gap in RL Post-Training with Stochastic Rounding](https://arxiv.org/abs/2611.13545v1) | 2611.13545v1 | 7 |
| 2026-11-10 | [Discrete total variation under the multinomial, Part 5: cyclic total variation](https://arxiv.org/abs/2611.14735v1) | 2611.14735v1 | 8 |
| 2026-11-10 | [CAFIN: CUDA-accelerated Adaptive Fisher Information Matrix Network Optimization via GPU-Native Kernel Fusion](https://arxiv.org/abs/2611.14589v1) | 2611.14589v1 | 18 |
| 2026-11-09 | [Maximizing Detection Probability in UAV Search Missions using Random-Key Optimizers](https://arxiv.org/abs/2611.12317v1) | 2611.12317v1 | 6 |
| 2026-11-09 | [On the Global Convergence of Stochastic Adam for Physics-Informed Neural Networks](https://arxiv.org/abs/2611.11905v1) | 2611.11905v1 | 12 |
| 2026-11-09 | [Byzantine-Robust Muon: Resilient Momentum Orthogonalization for Distributed Learning](https://arxiv.org/abs/2611.13137v1) | 2611.13137v1 | 14 |
| 2026-11-08 | [Weight-Space Programming of Variational Quantum Circuits: Large Language Models Write Quantum Circuit Parameters Without an Optimizer](https://arxiv.org/abs/2611.11537v1) | 2611.11537v1 | 7 |
| 2026-11-08 | [A Stability Analysis of AdamW: Unstable Equilibria and Non-Convergence](https://arxiv.org/abs/2611.11526v1) | 2611.11526v1 | 9 |
| 2026-11-08 | [MOMENT-DP: Momentum Aware Evaluation of Correlated Noise for Differentially Private Training](https://arxiv.org/abs/2611.11457v1) | 2611.11457v1 | 7 |
| 2026-11-08 | [Variance-Reduced Stochastic Hessian-Driven Nesterov Acceleration with Adam-Style Preconditioning](https://arxiv.org/abs/2611.11277v1) | 2611.11277v1 | 6 |
| 2026-11-08 | [Full Fine-Tuning is not the Problem: Why Adam Fails and SGD Succeeds in Few-Shot CLIP Adaptation](https://arxiv.org/abs/2611.11152v1) | 2611.11152v1 | 12 |
| 2026-11-07 | [Network Contention State Aware Dynamic Optimizer for Accelerator Collective Communication Libraries](https://arxiv.org/abs/2611.10984v1) | 2611.10984v1 | 6 |
| 2026-11-07 | [Breaking Precision Walls in First-, Second-, and Zeroth-Order Optimizers: One Constant, Set in Advance](https://arxiv.org/abs/2611.10730v1) | 2611.10730v1 | 13 |
| 2026-11-07 | [Spectral Bias Reduction in Local Gated ReLU Architectures](https://arxiv.org/abs/2611.10700v1) | 2611.10700v1 | 7 |
| 2026-11-07 | [STABLE: A Continual Learning Optimizer with Adaptive Drift Control](https://arxiv.org/abs/2611.10655v1) | 2611.10655v1 | 6 |
| 2026-11-07 | [STABLE: A Continual Learning Optimizer with Adaptive Drift Control](https://arxiv.org/abs/2611.10655v2) | 2611.10655v2 | 6 |
| 2026-11-06 | [Second-order optimality conditions for $C^{1,1}$ sparsity constrained optimization problems via disjunctive programming](https://arxiv.org/abs/2611.09146v1) | 2611.09146v1 | 6 |
| 2026-11-06 | [ResQAdam: Residual-Preserving Adaptive Optimization for Memory-Efficient Quantization Aware Training](https://arxiv.org/abs/2611.08924v1) | 2611.08924v1 | 6 |
| 2026-11-06 | [Learning to Restart: Differentiable Restart Policies for Optimization Dynamics](https://arxiv.org/abs/2611.08883v1) | 2611.08883v1 | 7 |
| 2026-11-06 | [DisMUSE: An Efficient Distributed Singular-Spectrum-Based Optimization Approach with Theoretical Convergence Guarantee](https://arxiv.org/abs/2611.10212v1) | 2611.10212v1 | 12 |
| 2026-11-06 | [BiMuon: A Geometry-Aware Stochastic Bilevel Optimization Approach](https://arxiv.org/abs/2611.10188v1) | 2611.10188v1 | 7 |
| 2026-11-06 | [Quantum Natural Muon: Spectral-Natural Optimization for Variational Quantum Circuits](https://arxiv.org/abs/2611.10105v1) | 2611.10105v1 | 7 |
| 2026-11-06 | [BiMuon: A Geometry-Aware Stochastic Bilevel Optimization Approach](https://arxiv.org/abs/2611.10188v2) | 2611.10188v2 | 7 |
| 2026-11-05 | [Spectral and Subspace Dynamics of LoRA in Supervised Fine-Tuning and Reinforcement Learning](https://arxiv.org/abs/2611.08414v1) | 2611.08414v1 | 7 |
| 2026-11-05 | [Module-Aware Optimization for Graph Neural Networks](https://arxiv.org/abs/2611.08379v1) | 2611.08379v1 | 8 |
| 2026-11-05 | [Second-order geometric consistency of nonlinear FE-HMM on surfaces via corrector non-degeneracy](https://arxiv.org/abs/2611.07761v1) | 2611.07761v1 | 8 |
| 2026-11-04 | [DMuon: Scaling Matrix Optimizers in Data Parallelism with Topology-Aware Matrix Ownership and Communication](https://arxiv.org/abs/2611.07084v1) | 2611.07084v1 | 13 |
| 2026-11-04 | [Adaptive Multi Mode: Budget-Aware Routing of Optimizers By Online Landscape Probes](https://arxiv.org/abs/2611.06879v1) | 2611.06879v1 | 6 |
| 2026-11-04 | [DMuon-2: Scaling Matrix Optimizers in Data Parallelism with Topology-Aware Matrix Ownership and Communication](https://arxiv.org/abs/2611.07084v2) | 2611.07084v2 | 13 |
| 2026-11-03 | [Mixed-Integer Second-Order Cone Formulations for the Euclidean Bottleneck Steiner Tree Problem in $\mathbb{R}^d$](https://arxiv.org/abs/2611.05733v1) | 2611.05733v1 | 6 |
| 2026-11-03 | [ZEMA: confidence-calibrated signed descent with only one state](https://arxiv.org/abs/2611.04987v1) | 2611.04987v1 | 11 |
| 2026-11-03 | [Theoretical Analysis of Muon on Transformers for Next-Token Prediction](https://arxiv.org/abs/2611.04465v1) | 2611.04465v1 | 7 |
| 2026-11-02 | [Pretraining Data Scale Reverses the Muon-AdamW Fine-Tuning Gap](https://arxiv.org/abs/2611.03633v2) | 2611.03633v2 | 11 |
| 2026-11-02 | [The Optimizer's Windfall: Bounding Hindsight Gain under Random Restrictions](https://arxiv.org/abs/2611.03468v1) | 2611.03468v1 | 6 |
| 2026-11-02 | [First- and second-order constrained optimisation for inverse homogenisation of unidirectionally varying microstructure](https://arxiv.org/abs/2611.03372v2) | 2611.03372v2 | 8 |
| 2026-11-02 | [Probing aQGCs from dimension-eight operators via neutral triboson production at muon colliders](https://arxiv.org/abs/2611.03218v1) | 2611.03218v1 | 6 |
| 2026-11-02 | [Inner optimizers in active-learning Kriging reliability analysis: a pre-specified comparison and the unconservative estimates left by unlearned failure modes](https://arxiv.org/abs/2611.03117v1) | 2611.03117v1 | 6 |
| 2026-11-02 | [Tune the Baseline First: Most of Muon's Scaled Weight Decay Gain Is a Tuning Gap, but Its Small Real Advantage Grows With Model Size](https://arxiv.org/abs/2611.02529v1) | 2611.02529v1 | 9 |
| 2026-11-01 | [Watch Your Step: Adam's Margin Maximization Bias Depends on the Learning Rate Schedule](https://arxiv.org/abs/2611.01929v1) | 2611.01929v1 | 9 |
| 2026-11-01 | [Robust preconditioners for finite element approximations of control-state constrained optimal control problems governed by elliptic equations](https://arxiv.org/abs/2611.01526v1) | 2611.01526v1 | 6 |
| 2026-10-31 | [Adaptive Optimizers Can Get a Policy Ranking Wrong: Momentum, Dependent Data, and a Two-Run Remedy](https://arxiv.org/abs/2611.01216v1) | 2611.01216v1 | 9 |
| 2026-10-31 | [Representative Learning for Distributed Support Vector Machines](https://arxiv.org/abs/2611.00641v1) | 2611.00641v1 | 6 |
| 2026-10-31 | [Do Orthogonality Constraints Help Language-Model Training Beyond Sphere Optimization?](https://arxiv.org/abs/2611.00593v1) | 2611.00593v1 | 8 |
| 2026-10-31 | [Guarded Compression of Adam Optimizer State with Shared-Gradient Bounds](https://arxiv.org/abs/2611.00589v1) | 2611.00589v1 | 9 |
| 2026-10-30 | [A Spectral Renormalization-Group View of Learning](https://arxiv.org/abs/2611.00422v1) | 2611.00422v1 | 8 |
| 2026-10-30 | [Second order Heisenberg Uncertainty Principle for solenoidal fields: sharp constants, optimizers and sharp stability](https://arxiv.org/abs/2611.00362v1) | 2611.00362v1 | 7 |
| 2026-10-30 | [A Preconditioned Semismooth Newton Method for Box-Constrained Elliptic Optimal Control Problems with Random Coefficients](https://arxiv.org/abs/2611.00246v1) | 2611.00246v1 | 9 |
| 2026-10-30 | [ProLand: A New Infeasible Manifold Optimization Method for LoRA Fine-Tuning](https://arxiv.org/abs/2611.00236v1) | 2611.00236v1 | 8 |
| 2026-10-30 | [Near-Optimal Second-Order Convex Finite-Sum Optimization under Individual Smoothness](https://arxiv.org/abs/2610.42040v1) | 2610.42040v1 | 6 |
| 2026-10-30 | [Model Checking for Metric Extensions of Monadic Second-Order Logic](https://arxiv.org/abs/2610.41974v1) | 2610.41974v1 | 6 |
| 2026-10-30 | [Critical Optimizers for the Finite-Rank Fractional Lieb--Thirring Inequality](https://arxiv.org/abs/2610.41148v1) | 2610.41148v1 | 6 |
| 2026-10-30 | [MUON-RT Reusing the Teacher's Trajectory for Momentum-Free Muon for LLM Self-Distillation](https://arxiv.org/abs/2610.41104v1) | 2610.41104v1 | 10 |
| 2026-10-30 | [A Spectral Renormalization-Group View of Learning](https://arxiv.org/abs/2611.00422v2) | 2611.00422v2 | 8 |
| 2026-10-29 | [Stochastic and Noisy Oracles in Smooth Continuous Optimization](https://arxiv.org/abs/2610.41086v1) | 2610.41086v1 | 6 |
| 2026-10-29 | [bf16 Rounding Silently Discards Most RL Policy Updates: A Hidden Training-Inference Mismatch and an Unbiased One-Line Fix](https://arxiv.org/abs/2610.41073v1) | 2610.41073v1 | 10 |
| 2026-10-29 | [Search for long-lived heavy neutral leptons in signatures with one prompt muon and a secondary vertex formed by two non-prompt muons in proton-proton collisions at $\sqrt{s}$ = 13 and 13.6 TeV](https://arxiv.org/abs/2610.40911v1) | 2610.40911v1 | 6 |
| 2026-10-29 | [FARO: Function-Space Adaptive Return-to-Risk Optimization via Cross-Block Equal-Risk-Contribution Budget Allocation](https://arxiv.org/abs/2610.40858v1) | 2610.40858v1 | 10 |
| 2026-10-29 | [The Precision Wall: An Optimizer-Dependent Boundary for Optimization under Power-Law Measurement Spectra](https://arxiv.org/abs/2610.40485v1) | 2610.40485v1 | 7 |
| 2026-10-29 | [Diagnosing Optimizer-Landscape Interaction via Representation in Subset Selection Multitasking: Evidence from Piano Fingering](https://arxiv.org/abs/2610.39779v1) | 2610.39779v1 | 6 |
| 2026-10-29 | [Dobb: Shard-Local Preconditioning in Block-Diagonal Eigenbases](https://arxiv.org/abs/2610.39412v1) | 2610.39412v1 | 10 |
| 2026-10-28 | [Rennala NSGD: Asynchronous Stochastic Optimization Beyond Euclidean Geometry](https://arxiv.org/abs/2610.38773v1) | 2610.38773v1 | 13 |
| 2026-10-28 | [New muon transfer cell for muonic x-ray spectroscopy on microgram-quantity targets based on liquid hydrogen](https://arxiv.org/abs/2610.38758v1) | 2610.38758v1 | 6 |
| 2026-10-27 | [Understanding Large Language Models as Numerical Optimizers](https://arxiv.org/abs/2610.37932v1) | 2610.37932v1 | 6 |
| 2026-10-27 | [MuonGS: Pretraining LLMs with Relaxed Weight-Norm Control](https://arxiv.org/abs/2610.37647v1) | 2610.37647v1 | 14 |
| 2026-10-27 | [Sharpness-Aware Muon: Matrix-Aware Optimization with Momentum-Guided Perturbations](https://arxiv.org/abs/2610.37225v1) | 2610.37225v1 | 14 |
| 2026-10-27 | [Does Your Generalist Skill Optimizer Really Incentivize Agentic Tasks? Rethinking Skill Optimization via Bipartite Attribution](https://arxiv.org/abs/2610.37201v1) | 2610.37201v1 | 6 |
| 2026-10-27 | [EnergyCal: Taming Loss Spikes in Muon-Family Optimizers for Sparse MoE Training](https://arxiv.org/abs/2610.37062v1) | 2610.37062v1 | 16 |
| 2026-10-27 | [Keeping Contact: Task-Adaptive Friction Margins for Bimanual Non-Prehensile Manipulation](https://arxiv.org/abs/2610.36961v1) | 2610.36961v1 | 8 |
| 2026-10-27 | [Does LLM Pre-Training Typically Occur at the Edge of Stability?](https://arxiv.org/abs/2610.36778v1) | 2610.36778v1 | 7 |
| 2026-10-27 | [Noise Shapes the Surplus: Strategic Play Against No-Regret Learners](https://arxiv.org/abs/2610.36621v1) | 2610.36621v1 | 6 |
| 2026-10-27 | [Efficient Quantization Training with Stochastic Rounding via Structured Subspace Randomness](https://arxiv.org/abs/2610.36587v1) | 2610.36587v1 | 6 |
| 2026-10-27 | [Moment-Guided Optimizers for Noisy Deep Learning: MGO-SC as a Simple Consistency Gate for Adam-Style Updates](https://arxiv.org/abs/2610.37712v1) | 2610.37712v1 | 15 |
| 2026-10-27 | [Second-order Sinkhorn Geometry and $\sqrt{n}$-Inference](https://arxiv.org/abs/2610.36488v1) | 2610.36488v1 | 6 |
| 2026-10-26 | [ADACT: PDE-Constrained Thermal Hardware/Software Co-Design Adjoint-Driven Optimal Control via Finite Difference Discretization](https://arxiv.org/abs/2610.35569v1) | 2610.35569v1 | 6 |
| 2026-10-26 | [Understanding Practical Optimization in Machine Learning](https://arxiv.org/abs/2610.35209v1) | 2610.35209v1 | 12 |
| 2026-10-26 | [TUON: A Tensor-Aware Optimizer Utilizing Tensor-SVD and Polarization for Large Language Model Pretraining](https://arxiv.org/abs/2610.35130v1) | 2610.35130v1 | 11 |
| 2026-10-26 | [UTA: Universal Training Adaptive Learning Rate Decay](https://arxiv.org/abs/2610.35113v1) | 2610.35113v1 | 7 |
| 2026-10-25 | [Error Diffusion Replaces Latent Weights: Training Binary-Weight Language Models on a Few Bits of Dithered State](https://arxiv.org/abs/2610.34566v1) | 2610.34566v1 | 7 |
| 2026-10-25 | [Last-Iterate Stationarity of Muon with Finitely Many Newton-Schulz Iterations](https://arxiv.org/abs/2610.34158v2) | 2610.34158v2 | 12 |
| 2026-10-24 | [Optimal Experimental Design for the Polynomial Maximization Method: a Higher-Order Reserve Beyond Second-Order Design Theory](https://arxiv.org/abs/2610.33921v3) | 2610.33921v3 | 6 |
| 2026-10-24 | [Reactive Optimizers](https://arxiv.org/abs/2610.33826v2) | 2610.33826v2 | 8 |
| 2026-10-23 | [Radiation damage and recovery of SiPMs exposed to low-momentum muon beams for innovative scintillation-based muon beam monitors](https://arxiv.org/abs/2610.32852v1) | 2610.32852v1 | 9 |
| 2026-10-23 | [Classical Pre-Training of Large Shallow Parametrized Quantum Circuits through Pauli Propagation and deployment on Quantum Hardware](https://arxiv.org/abs/2610.32571v1) | 2610.32571v1 | 6 |
| 2026-10-23 | [Sharpness-aware Orthogonalized Momentum Algorithms](https://arxiv.org/abs/2610.32465v1) | 2610.32465v1 | 12 |
| 2026-10-23 | [Curvature-Aware Clipping: Mitigating Bias in DPSGD via Approximate Second-Order Information](https://arxiv.org/abs/2610.32175v1) | 2610.32175v1 | 7 |
| 2026-10-23 | [RSI-Opt: Recursive Self-Improvement Optimizer Agents For Model Training](https://arxiv.org/abs/2610.32026v1) | 2610.32026v1 | 6 |
| 2026-10-22 | [A Globally Convergent Newton Method for Nonsmooth Optimization in the absence of Smooth Surrogates](https://arxiv.org/abs/2610.31992v1) | 2610.31992v1 | 6 |
| 2026-10-22 | [When and How Does Muon Precondition? The Role of Structured Gradient Noise](https://arxiv.org/abs/2610.31728v1) | 2610.31728v1 | 15 |
| 2026-10-22 | [IQuest-Q1: Advancing Foundation Capabilities for Agentic CLI Systems](https://arxiv.org/abs/2610.30949v1) | 2610.30949v1 | 6 |
| 2026-10-22 | [Soft-Update MSA for Nonconvex Stochastic Optimal Control: Theory and Algorithms](https://arxiv.org/abs/2610.30585v1) | 2610.30585v1 | 6 |
| 2026-10-21 | [A Quadratic Lens on Muon's Polar Update: Benefits, Pitfalls, and the Role of Newton-Schulz](https://arxiv.org/abs/2610.30280v1) | 2610.30280v1 | 11 |
| 2026-10-21 | [The Dynamics of RMSProp Beyond the Stability Threshold](https://arxiv.org/abs/2610.30078v1) | 2610.30078v1 | 7 |
| 2026-10-20 | [How Does Orthogonalization Adapt to the Neural Network Hessian Structure? A Gradient Self Outer-Product Analysis at Initialization](https://arxiv.org/abs/2610.28975v1) | 2610.28975v1 | 11 |
| 2026-10-20 | [From Qubit Tensorization to Gaussian Optimizers in Bosonic Systems](https://arxiv.org/abs/2610.28902v1) | 2610.28902v1 | 6 |
| 2026-10-20 | [Delayed Convergence of S-Parameter Sensitivities to Design Parameters in FDTD Simulations](https://arxiv.org/abs/2610.28496v1) | 2610.28496v1 | 6 |
| 2026-10-20 | [MuPACE: Learning to Pace Muon for LoRA Fine-Tuning](https://arxiv.org/abs/2610.28072v1) | 2610.28072v1 | 12 |
| 2026-10-20 | [Explicit Convex Inner Approximation of TSO-DSO Flexibility Regions via Exact Second-order Cone Relaxation in Radial Networks](https://arxiv.org/abs/2610.27897v1) | 2610.27897v1 | 6 |
| 2026-10-20 | [From Generic to Dedicated: A Novel Optimizer for Online Continual Learning](https://arxiv.org/abs/2610.27835v1) | 2610.27835v1 | 7 |
| 2026-10-20 | [Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics](https://arxiv.org/abs/2610.27747v1) | 2610.27747v1 | 13 |
| 2026-10-20 | [Hybrid Momentum Methods for Optimizing Deep Learning Models](https://arxiv.org/abs/2610.27674v2) | 2610.27674v2 | 8 |
| 2026-10-19 | [Physics-Inspired Optimizers beyond the Edge of Stability: Period-Two Orbits and Delayed Instability](https://arxiv.org/abs/2610.27321v2) | 2610.27321v2 | 11 |
| 2026-10-19 | [Polar Switch: Fast Muon Orthogonalization with Polynomial Circuits](https://arxiv.org/abs/2610.26742v1) | 2610.26742v1 | 11 |
| 2026-10-19 | [Learning SOCP Solver Dynamics with Graph Neural Networks](https://arxiv.org/abs/2610.26285v1) | 2610.26285v1 | 8 |
| 2026-10-19 | [Axion-Like Particle Searches at Muon Colliders: Photon-Neutrino Signatures and Heavy-Neutral-Lepton Feasibility](https://arxiv.org/abs/2610.27006v1) | 2610.27006v1 | 7 |
| 2026-10-18 | [Volume-dependent geometry and symmetry transitions of torsion optimizers in infinite cylinders](https://arxiv.org/abs/2610.25267v2) | 2610.25267v2 | 7 |
| 2026-10-18 | [T-MUON: Tensorizing Muon via t-SVD for Large Language Model Pre-training](https://arxiv.org/abs/2610.24938v1) | 2610.24938v1 | 12 |
| 2026-10-17 | [Stochastic optimization methods through statistical whitening](https://arxiv.org/abs/2610.24839v2) | 2610.24839v2 | 11 |
| 2026-10-17 | [How Does Muon Work in Private Deep Learning? Scalable Differentially Private Training via Orthogonalization](https://arxiv.org/abs/2610.24736v1) | 2610.24736v1 | 16 |
| 2026-10-17 | [AdamPM: Memory-Efficient LLM Optimization via Moment Pooling](https://arxiv.org/abs/2610.24598v1) | 2610.24598v1 | 6 |
| 2026-10-17 | [Low-Bit Distributed Constrained Optimization with Application to Optimal Scheduling and Allocation](https://arxiv.org/abs/2610.24431v1) | 2610.24431v1 | 6 |
| 2026-10-17 | [Adding Heavy-Ball Momentum to Distributed Constrained Optimization for Energy Resource Management Subject to Time-Delays and Quantization](https://arxiv.org/abs/2610.24421v1) | 2610.24421v1 | 9 |
| 2026-10-16 | [Muon Operates Beyond the Edge of Stability](https://arxiv.org/abs/2610.24305v1) | 2610.24305v1 | 14 |
| 2026-10-16 | [An important Bottleneck in LLM Optimizers: Principle-Level Local Optima](https://arxiv.org/abs/2610.24291v2) | 2610.24291v2 | 6 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-31 | [FANoS-v2: Feedback-Controlled Momentum with Thermostat Damping for Lightweight Neural Optimization](https://arxiv.org/abs/2601.00889v2) | 2601.00889v2 | 12 |
| 2025-12-31 | [Nested Learning: The Illusion of Deep Learning Architectures](https://arxiv.org/abs/2512.24695v1) | 2512.24695v1 | 7 |
| 2025-12-31 | [Distributed Bilevel Optimization with Dual Pruning for Resource-limited Clients](https://arxiv.org/abs/2512.24667v1) | 2512.24667v1 | 6 |
| 2025-12-31 | [OCP-GN: A Scalable Second-order Optimizer for Stochastic Optimization](https://arxiv.org/abs/2512.24552v2) | 2512.24552v2 | 12 |
| 2025-12-30 | [Adaptive Learning Guided by Bias-Noise-Alignment Diagnostics](https://arxiv.org/abs/2512.24445v2) | 2512.24445v2 | 6 |
| 2025-12-30 | [A regularity theory for second-order parabolic partial differential equations in weighted mixed norm Sobolev-Zygmund spaces](https://arxiv.org/abs/2512.24020v3) | 2512.24020v3 | 6 |
| 2025-12-28 | [Reconstructing Relativistic Magnetohydrodynamics with Physics-Informed Neural Networks](https://arxiv.org/abs/2512.23057v1) | 2512.23057v1 | 8 |
| 2025-12-27 | [Gold Price Prediction Using Long Short-Term Memory and Multi-Layer Perceptron with Gray Wolf Optimizer](https://arxiv.org/abs/2512.22606v1) | 2512.22606v1 | 6 |
| 2025-12-26 | [Completed Hyperparameter Transfer across Modules, Width, Depth, Batch and Duration](https://arxiv.org/abs/2512.22382v1) | 2512.22382v1 | 9 |
| 2025-12-25 | [BertsWin: Resolving Topological Sparsity in 3D Masked Autoencoders via Component-Balanced Structural Optimization](https://arxiv.org/abs/2512.21769v1) | 2512.21769v1 | 6 |
| 2025-12-25 | [NEMO-4-PAYPAL: Leveraging NVIDIA's Nemo Framework for empowering PayPal's Commerce Agent](https://arxiv.org/abs/2512.21578v3) | 2512.21578v3 | 6 |
| 2025-12-24 | [The Dynamical Anatomy of Anderson Acceleration:From Adaptive Momentum to Variable-Mass ODEs](https://arxiv.org/abs/2512.21269v2) | 2512.21269v2 | 9 |
| 2025-12-23 | [Status of the Muon g-2/EDM Experiment at J-PARC](https://arxiv.org/abs/2512.20335v1) | 2512.20335v1 | 6 |
| 2025-12-23 | [Effect of Activation Function and Model Optimizer on the Performance of Human Activity Recognition System Using Various Deep Learning Models](https://arxiv.org/abs/2512.20104v1) | 2512.20104v1 | 6 |
| 2025-12-22 | [GANeXt: A Fully ConvNeXt-Enhanced Generative Adversarial Network for MRI- and CBCT-to-CT Synthesis](https://arxiv.org/abs/2512.19336v2) | 2512.19336v2 | 6 |
| 2025-12-22 | [Optimizer Dynamics at the Edge of Stability with Differential Privacy](https://arxiv.org/abs/2512.19019v1) | 2512.19019v1 | 9 |
| 2025-12-22 | [A TraceFEM $C^0$ Interior Penalty Method for the Surface Biharmonic Equation](https://arxiv.org/abs/2512.18949v1) | 2512.18949v1 | 6 |
| 2025-12-21 | [Tight Lower Bounds and Optimal Algorithms for Stochastic Nonconvex Optimization with Heavy-Tailed Noise](https://arxiv.org/abs/2512.18713v2) | 2512.18713v2 | 8 |
| 2025-12-20 | [Towards Guided Descent: Optimization Algorithms for Training Neural Networks At Scale](https://arxiv.org/abs/2512.18373v1) | 2512.18373v1 | 7 |
| 2025-12-19 | [Optimal Control Problems with Nonlocal Conservation Laws: Existence of Optimizers and Singular Limits in Approximations of Local Conservation Laws](https://arxiv.org/abs/2512.17870v1) | 2512.17870v1 | 6 |
| 2025-12-19 | [GreedySnake: Accelerating SSD-Offloaded LLM Training with Efficient Scheduling and Optimizer Step Overlapping](https://arxiv.org/abs/2512.17570v2) | 2512.17570v2 | 7 |
| 2025-12-18 | [Smoothing DiLoCo with Primal Averaging for Faster Training of LLMs](https://arxiv.org/abs/2512.17131v3) | 2512.17131v3 | 8 |
| 2025-12-18 | [Bridging Training and Merging Through Momentum-Aware Optimization](https://arxiv.org/abs/2512.17109v3) | 2512.17109v3 | 9 |
| 2025-12-18 | [Risk-Aware GPU-Assisted Cardinality Estimation for Cost-Based Query Optimizers](https://arxiv.org/abs/2512.19750v2) | 2512.19750v2 | 6 |
| 2025-12-18 | [Muon is Provably Faster with Momentum Variance Reduction](https://arxiv.org/abs/2512.16598v1) | 2512.16598v1 | 14 |
| 2025-12-18 | [Classical solution to second-order Hamilton-Jacobi-Bellman equation and optimal feedback control for linear-convex problem](https://arxiv.org/abs/2512.16291v1) | 2512.16291v1 | 7 |
| 2025-12-18 | [Sharpness-aware Second-order Latent Factor Model for High-dimensional and Incomplete Data](https://arxiv.org/abs/2512.16277v1) | 2512.16277v1 | 6 |
| 2025-12-17 | [Precision continuous-wave laser measurement of the $\text{1}^\text{3}\text{S}_\text{1} \to \text{2}^\text{3}\text{S}_\text{1}$ interval in positronium](https://arxiv.org/abs/2512.16018v1) | 2512.16018v1 | 8 |
| 2025-12-17 | [A muon scattering tomography system based on high spatial resolution scintillating detector](https://arxiv.org/abs/2512.15444v2) | 2512.15444v2 | 6 |
| 2025-12-17 | [Historical Information Accelerates Decentralized Optimization: A Proximal Bundle Method](https://arxiv.org/abs/2512.15189v2) | 2512.15189v2 | 6 |
| 2025-12-16 | [Dynamic Learning Rate Scheduling based on Loss Changes Leads to Faster Convergence](https://arxiv.org/abs/2512.14527v1) | 2512.14527v1 | 8 |
| 2025-12-16 | [A preconditioned second-order convex splitting algorithm with extrapolation](https://arxiv.org/abs/2512.14468v3) | 2512.14468v3 | 7 |
| 2025-12-16 | [Adiabatic-Inspired Hybrid Quantum-Classical Methods for Molecular Ground State Preparation](https://arxiv.org/abs/2512.14449v1) | 2512.14449v1 | 6 |
| 2025-12-16 | [Optimizing Rank for High-Fidelity Implicit Neural Representations](https://arxiv.org/abs/2512.14366v3) | 2512.14366v3 | 8 |
| 2025-12-15 | [Better LMO-based Momentum Methods with Second-Order Information](https://arxiv.org/abs/2512.13227v1) | 2512.13227v1 | 14 |
| 2025-12-15 | [M-GRPO: Stabilizing Self-Supervised Reinforcement Learning for Large Language Models with Momentum-Anchored Policy Optimization](https://arxiv.org/abs/2512.13070v1) | 2512.13070v1 | 6 |
| 2025-12-12 | [Probing Vector-Like Quarks at a future Muon-Proton Collider](https://arxiv.org/abs/2512.11471v4) | 2512.11471v4 | 6 |
| 2025-12-12 | [Renormalization group approach to second-order Green's function theory](https://arxiv.org/abs/2512.11410v2) | 2512.11410v2 | 6 |
| 2025-12-10 | [Exqutor: Extended Query Optimizer for Vector-augmented Analytical Queries](https://arxiv.org/abs/2512.09695v4) | 2512.09695v4 | 6 |
| 2025-12-09 | [Second-Order $Λ$-Sets and Extensions to Non-Smooth, Hybrid, and Stochastic Optimal Control](https://arxiv.org/abs/2512.09126v1) | 2512.09126v1 | 6 |
| 2025-12-09 | [Unfolding quantum entanglement from $h\to ZZ^*\to jj\ell\ell$ at a muon collider](https://arxiv.org/abs/2512.09121v1) | 2512.09121v1 | 6 |
| 2025-12-09 | [BISTRO -- A Bi-Fidelity Stochastic Gradient Framework using Trust-Regions for Optimization Under Uncertainty](https://arxiv.org/abs/2512.09055v1) | 2512.09055v1 | 6 |
| 2025-12-09 | [Correction of Decoupled Weight Decay](https://arxiv.org/abs/2512.08217v3) | 2512.08217v3 | 12 |
| 2025-12-08 | [FOAM: Blocked State Folding for Memory-Efficient LLM Training](https://arxiv.org/abs/2512.07112v2) | 2512.07112v2 | 6 |
| 2025-12-07 | [OFF Newton-type Methods for Unconstrained Optimization with Inexact Derivatives](https://arxiv.org/abs/2512.06825v3) | 2512.06825v3 | 6 |
| 2025-12-07 | [ADAM Optimization with Adaptive Batch Selection](https://arxiv.org/abs/2512.06795v1) | 2512.06795v1 | 7 |
| 2025-12-07 | [Arc Gradient Descent: A Geometrically Motivated Gradient Descent-based Optimiser with Phase-Aware, User-Controlled Step Dynamics (proof-of-concept)](https://arxiv.org/abs/2512.06737v3) | 2512.06737v3 | 10 |
| 2025-12-07 | [Optimal Preconditioning is a Geodesically Convex Optimization Problem](https://arxiv.org/abs/2512.06618v1) | 2512.06618v1 | 6 |
| 2025-12-06 | [Greedy Alignment Principle for Optimizer Hyperparameter Selection](https://arxiv.org/abs/2512.06370v4) | 2512.06370v4 | 9 |
| 2025-12-05 | [Qualitative and Quantitative Analysis of Riemannian Optimization Methods for Ground States of Rotating Multicomponent Bose-Einstein Condensates](https://arxiv.org/abs/2512.05939v1) | 2512.05939v1 | 6 |
| 2025-12-05 | [Wasserstein Evolution : Evolutionary Optimization as Phase Transition](https://arxiv.org/abs/2512.05837v3) | 2512.05837v3 | 6 |
| 2025-12-05 | [Learnability Window in Gated Recurrent Neural Networks](https://arxiv.org/abs/2512.05790v10) | 2512.05790v10 | 7 |
| 2025-12-05 | [Modified global finite-time quasi-continuous second-order robust feedback control](https://arxiv.org/abs/2512.05727v1) | 2512.05727v1 | 7 |
| 2025-12-05 | [Hyperparameter Transfer Enables Consistent Gains of Matrix-Preconditioned Optimizers Across Scales](https://arxiv.org/abs/2512.05620v2) | 2512.05620v2 | 21 |
| 2025-12-05 | [Beyond Adam: Disentangling Optimizer Effects in the Fine-Tuning of Atomistic Foundation Models](https://arxiv.org/abs/2512.05489v1) | 2512.05489v1 | 12 |
| 2025-12-05 | [Evolving Deep Learning Optimizers](https://arxiv.org/abs/2512.11853v1) | 2512.11853v1 | 11 |
| 2025-12-05 | [First Demonstration of Second-order Training of Deep Neural Networks with In-memory Analog Matrix Computing](https://arxiv.org/abs/2512.05342v1) | 2512.05342v1 | 14 |
| 2025-12-04 | [Turbo-Muon: Almost-Orthogonal Pre-Conditioning for Fast Muon Updates](https://arxiv.org/abs/2512.04632v2) | 2512.04632v2 | 11 |
| 2025-12-03 | [When do spectral gradient updates help in deep learning?](https://arxiv.org/abs/2512.04299v2) | 2512.04299v2 | 9 |
| 2025-12-03 | [Phase-space open-systems dynamics of second-order nonlinear interactions with pulsed quantum light](https://arxiv.org/abs/2512.03933v1) | 2512.03933v1 | 6 |
| 2025-12-03 | [Parameter Optimization in Trajectory Planning via Differentiable Convex Programming](https://arxiv.org/abs/2512.03557v2) | 2512.03557v2 | 6 |
| 2025-12-02 | [Muon collider probes of the gluonic quartic gauge couplings](https://arxiv.org/abs/2512.03144v1) | 2512.03144v1 | 6 |
| 2025-12-02 | [An efficient fully decoupled finite element method with second-order accuracy for the micropolar Rayleigh-Benard convection system](https://arxiv.org/abs/2512.02770v1) | 2512.02770v1 | 8 |
| 2025-12-01 | [Unifying Sign and Magnitude for Optimizing Deep Vision Networks via ThermoLion](https://arxiv.org/abs/2512.01881v2) | 2512.01881v2 | 8 |
| 2025-12-01 | [Dion2: A Simple Method to Shrink Matrix in Muon](https://arxiv.org/abs/2512.16928v1) | 2512.16928v1 | 10 |
| 2025-12-01 | [Learning to Reconstruct: A Differentiable Approach to Muon Tracking at the LHC](https://arxiv.org/abs/2512.01647v2) | 2512.01647v2 | 8 |
| 2025-12-01 | [Convergence of long-time stable variable-step arbitrary order ETD-MS scheme for gradient flows with Lipschitz nonlinearity](https://arxiv.org/abs/2512.01601v1) | 2512.01601v1 | 6 |
| 2025-09-30 | [Per-example gradients: a new frontier for understanding and improving optimizers](https://arxiv.org/abs/2510.00236v2) | 2510.00236v2 | 11 |
| 2025-09-30 | [Directed-MAML: Meta Reinforcement Learning Algorithm with Task-directed Approximation](https://arxiv.org/abs/2510.00212v1) | 2510.00212v1 | 6 |
| 2025-09-30 | [FedMuon: Federated Learning with Bias-corrected LMO-based Optimization](https://arxiv.org/abs/2509.26337v1) | 2509.26337v1 | 11 |
| 2025-09-30 | [A Single-Loop Gradient Algorithm for Pessimistic Bilevel Optimization via Smooth Approximation](https://arxiv.org/abs/2509.26240v4) | 2509.26240v4 | 6 |
| 2025-09-30 | [Muon Outperforms Adam in Tail-End Associative Memory Learning](https://arxiv.org/abs/2509.26030v2) | 2509.26030v2 | 10 |
| 2025-09-29 | [Machine Learning Algorithms for Improving Black Box Optimization Solvers](https://arxiv.org/abs/2509.25592v2) | 2509.25592v2 | 7 |
| 2025-09-29 | [Proximal gradient methods in Banach spaces](https://arxiv.org/abs/2509.24685v1) | 2509.24685v1 | 6 |
| 2025-09-29 | [AuON: A Linear-time Alternative to Orthogonal Momentum Updates](https://arxiv.org/abs/2509.24320v4) | 2509.24320v4 | 12 |
| 2025-09-29 | [Conda: Column-Normalized Adam for Training Large Language Models Faster](https://arxiv.org/abs/2509.24218v2) | 2509.24218v2 | 12 |
| 2025-09-28 | [NeuSO: Neural Optimizer for Subgraph Queries](https://arxiv.org/abs/2509.23775v1) | 2509.23775v1 | 6 |
| 2025-09-27 | [Beyond Outliers: A Study of Optimizers Under Quantization](https://arxiv.org/abs/2509.23500v2) | 2509.23500v2 | 10 |
| 2025-09-27 | [Optimal Diagonal Preconditioning Beyond Worst-Case Conditioning: Theory and Practice of Omega Scaling](https://arxiv.org/abs/2509.23439v3) | 2509.23439v3 | 6 |
| 2025-09-27 | [A FFT-based GMRES for fast solving of Poisson equation in concatenated geometry](https://arxiv.org/abs/2509.23180v1) | 2509.23180v1 | 8 |
| 2025-09-27 | [Effective Quantization of Muon Optimizer States](https://arxiv.org/abs/2509.23106v3) | 2509.23106v3 | 13 |
| 2025-09-27 | [Optimization as a Dynamical System: Generative Schedules from Latent ODEs](https://arxiv.org/abs/2509.23052v2) | 2509.23052v2 | 7 |
| 2025-09-26 | [Understanding SOAP from the Perspective of Gradient Whitening](https://arxiv.org/abs/2509.22938v1) | 2509.22938v1 | 14 |
| 2025-09-26 | [Reconstruction of the Effective Energy-deposition Vertex of Muon Showers using PMT Waveform in a Large-scale Liquid Scintillator Detector](https://arxiv.org/abs/2509.21935v3) | 2509.21935v3 | 6 |
| 2025-09-25 | [Scalable Second-order Riemannian Optimization for $K$-means Clustering](https://arxiv.org/abs/2509.21675v2) | 2509.21675v2 | 6 |
| 2025-09-25 | [Provable Scaling Laws of Feature Emergence from Learning Dynamics of Grokking](https://arxiv.org/abs/2509.21519v5) | 2509.21519v5 | 13 |
| 2025-09-25 | [Knowledgeable Language Models as Black-Box Optimizers for Personalized Medicine](https://arxiv.org/abs/2509.20975v2) | 2509.20975v2 | 6 |
| 2025-09-25 | [Efficient Differentiable Contact Model with Long-range Influence](https://arxiv.org/abs/2509.20917v1) | 2509.20917v1 | 6 |
| 2025-09-25 | [Efficient Construction of Implicit Surface Models From a Single Image for Motion Generation](https://arxiv.org/abs/2509.20681v3) | 2509.20681v3 | 9 |
| 2025-09-24 | [Faster Than SVD, Smarter Than SGD: The OPLoRA Alternating Update](https://arxiv.org/abs/2509.19977v1) | 2509.19977v1 | 6 |
| 2025-09-24 | [High-order Multiscale Preconditioner for Elasticity of Arbitrary Structures](https://arxiv.org/abs/2509.19777v1) | 2509.19777v1 | 6 |
| 2025-09-22 | [Development of Deep Learning Optimizers: Approaches, Concepts, and Update Rules](https://arxiv.org/abs/2509.18396v2) | 2509.18396v2 | 13 |
| 2025-09-22 | [Probing the Ground State of the Antiferromagnetic Heisenberg Model on the Kagome Lattice using Geometrically Informed Variational Quantum Eigensolver](https://arxiv.org/abs/2509.18029v3) | 2509.18029v3 | 6 |
| 2025-09-22 | [Methods for Multi-objective Optimization PID Controller for quadrotor UAVs](https://arxiv.org/abs/2509.17423v1) | 2509.17423v1 | 7 |
| 2025-09-22 | [Optimizers of the Finite-Rank Hardy-Lieb-Thirring Inequality for Hardy-Schrödinger Operator](https://arxiv.org/abs/2509.17307v1) | 2509.17307v1 | 6 |
| 2025-09-21 | [Graph Coloring for Multi-Task Learning](https://arxiv.org/abs/2509.16959v5) | 2509.16959v5 | 6 |
| 2025-09-20 | [Hyperbolic Optimization](https://arxiv.org/abs/2509.25206v1) | 2509.25206v1 | 6 |
| 2025-09-19 | [ENSAM: an efficient foundation model for interactive segmentation of 3D medical images](https://arxiv.org/abs/2509.15874v1) | 2509.15874v1 | 9 |
| 2025-09-19 | [On the Convergence of Muon and Beyond](https://arxiv.org/abs/2509.15816v6) | 2509.15816v6 | 16 |
| 2025-09-19 | [Momentum-constrained Hybrid Heuristic Trajectory Optimization Framework with Residual-enhanced DRL for Visually Impaired Scenarios](https://arxiv.org/abs/2509.15582v2) | 2509.15582v2 | 6 |
| 2025-09-18 | [Inspired by machine learning optimization: can gradient-based optimizers solve cycle skipping in full waveform inversion given sufficient iterations?](https://arxiv.org/abs/2509.14919v1) | 2509.14919v1 | 9 |
| 2025-09-18 | [LiMuon: Light and Fast Muon Optimizer for Large Models](https://arxiv.org/abs/2509.14562v5) | 2509.14562v5 | 14 |
| 2025-09-17 | [Hierarchical Learning for Maze Navigation: Emergence of Mental Representations via Second-Order Learning](https://arxiv.org/abs/2509.14195v1) | 2509.14195v1 | 6 |
| 2025-09-17 | [A Reusable Library for Second-Order Orbital Optimization Using the Trust Region Method](https://arxiv.org/abs/2509.13931v2) | 2509.13931v2 | 6 |
| 2025-09-17 | [APFEx: Adaptive Pareto Front Explorer for Intersectional Fairness](https://arxiv.org/abs/2509.13908v2) | 2509.13908v2 | 6 |
| 2025-09-16 | [An Analysis of Optimizer Choice on Energy Efficiency and Performance in Neural Network Training](https://arxiv.org/abs/2509.13516v1) | 2509.13516v1 | 6 |
| 2025-09-16 | [PBPK-iPINNs: Inverse Physics-Informed Neural Networks for Physiologically Based Pharmacokinetic Brain Models](https://arxiv.org/abs/2509.12666v3) | 2509.12666v3 | 6 |
| 2025-09-15 | [Fractional-Order Nesterov Dynamics for Convex Optimization](https://arxiv.org/abs/2509.11987v1) | 2509.11987v1 | 6 |
| 2025-09-15 | [Low-rank Orthogonalization for Large-scale Matrix Optimization with Applications to Foundation Model Training](https://arxiv.org/abs/2509.11983v3) | 2509.11983v3 | 9 |
| 2025-09-15 | [Visualization and Analysis of the Loss Landscape in Graph Neural Networks](https://arxiv.org/abs/2509.11792v1) | 2509.11792v1 | 8 |
| 2025-09-12 | [Understanding Outer Optimizers in Local SGD: Learning Rates, Momentum, and Acceleration](https://arxiv.org/abs/2509.10439v2) | 2509.10439v2 | 14 |
| 2025-09-11 | [An improved educational competition optimizer with multi-covariance learning operators for global optimization problems](https://arxiv.org/abs/2509.09552v1) | 2509.09552v1 | 7 |
| 2025-09-11 | [Balancing Utility and Privacy: Dynamically Private SGD with Random Projection](https://arxiv.org/abs/2509.09485v2) | 2509.09485v2 | 6 |
| 2025-09-11 | [Second-order optimally stable IMEX (pseudo-)staggered Galerkin discretization with application to depth-integrated lava flow simulations](https://arxiv.org/abs/2509.09460v2) | 2509.09460v2 | 6 |
| 2025-09-10 | [One-shot acceleration of transient PDE solvers via online-learned preconditioners](https://arxiv.org/abs/2509.08765v4) | 2509.08765v4 | 7 |
| 2025-09-09 | [Sketched Gaussian Mechanism for Private Federated Learning](https://arxiv.org/abs/2509.08195v1) | 2509.08195v1 | 6 |
| 2025-09-06 | [Simple Optimizers for Convex Aligned Multi-Objective Optimization](https://arxiv.org/abs/2509.05811v1) | 2509.05811v1 | 8 |
| 2025-09-05 | [Reconstruction of cosmic-ray muon events with CUORE](https://arxiv.org/abs/2509.05528v2) | 2509.05528v2 | 6 |
| 2025-09-05 | [TripOptimizer: Generative 3D Shape Optimization and Drag Prediction using Triplane VAE Networks](https://arxiv.org/abs/2509.12224v1) | 2509.12224v1 | 6 |
| 2025-09-05 | [Synthetic Acceleration Preconditioners for Parametric Radiative Transfer Equations based on Trajectory-Aware Reduced Order Models](https://arxiv.org/abs/2509.05001v1) | 2509.05001v1 | 7 |
| 2025-06-30 | [Both Asymptotic and Non-Asymptotic Convergence of Quasi-Hyperbolic Momentum using Increasing Batch Size](https://arxiv.org/abs/2506.23544v3) | 2506.23544v3 | 7 |
| 2025-06-29 | [Closed-Form Robustness Bounds for Second-Order Pruning of Neural Controller Policies](https://arxiv.org/abs/2507.02953v1) | 2507.02953v1 | 6 |
| 2025-06-28 | [Performance Estimation of second-order optimization methods on classes of univariate functions](https://arxiv.org/abs/2506.22764v1) | 2506.22764v1 | 7 |
| 2025-06-27 | [Second-order methods for provably escaping strict saddle points in composite nonconvex and nonsmooth optimization](https://arxiv.org/abs/2506.22332v1) | 2506.22332v1 | 6 |
| 2025-06-26 | [Linear and Second-order-cone Valid Inequalities for Problems with Storage](https://arxiv.org/abs/2506.21470v1) | 2506.21470v1 | 6 |
| 2025-06-26 | [An adaptive dynamical low-rank optimizer for solving kinetic parameter identification problems](https://arxiv.org/abs/2506.21405v2) | 2506.21405v2 | 7 |
| 2025-06-26 | [DiLoCoX: A Low-Communication Large-Scale Training Framework for Decentralized Cluster](https://arxiv.org/abs/2506.21263v1) | 2506.21263v1 | 6 |
| 2025-06-24 | [Outlier-Safe Pre-Training for Robust 4-Bit Quantization of Large Language Models](https://arxiv.org/abs/2506.19697v1) | 2506.19697v1 | 9 |
| 2025-06-23 | [Comparative Analysis of Lion and AdamW Optimizers for Cross-Encoder Reranking with MiniLM, GTE, and ModernBERT](https://arxiv.org/abs/2506.18297v1) | 2506.18297v1 | 6 |
| 2025-06-22 | [Hindsight-Guided Momentum (HGM) Optimizer: An Approach to Adaptive Learning Rate](https://arxiv.org/abs/2506.22479v1) | 2506.22479v1 | 14 |
| 2025-06-21 | [Faster Low-Rank Approximation and Kernel Ridge Regression via the Block-Nyström Method](https://arxiv.org/abs/2506.17556v2) | 2506.17556v2 | 8 |
| 2025-06-20 | [A geometric framework for momentum-based optimizers for low-rank training](https://arxiv.org/abs/2506.17475v3) | 2506.17475v3 | 10 |
| 2025-06-20 | [Memory-Efficient LLM Pretraining via Minimalist Optimizer Design](https://arxiv.org/abs/2506.16659v3) | 2506.16659v3 | 17 |
| 2025-06-19 | [Monolithic and Block Overlapping Schwarz Preconditioners for the Incompressible Navier-Stokes Equations](https://arxiv.org/abs/2506.16179v2) | 2506.16179v2 | 6 |
| 2025-06-19 | [Convergence analysis of a Tikhonov regularized inertial dynamical system and algorithm for convex optimization problems](https://arxiv.org/abs/2506.15968v3) | 2506.15968v3 | 6 |
| 2025-06-18 | [Heavy Ball and Nesterov Accelerations with Hessian-driven Damping for Nonconvex Optimization](https://arxiv.org/abs/2506.15632v1) | 2506.15632v1 | 7 |
| 2025-06-18 | [Muon Optimizes Under Spectral Norm Constraints](https://arxiv.org/abs/2506.15054v2) | 2506.15054v2 | 12 |
| 2025-06-16 | [Gradient-Normalized Smoothness for Optimization with Approximate Hessians](https://arxiv.org/abs/2506.13710v1) | 2506.13710v1 | 6 |
| 2025-06-14 | [Is your batch size the problem? Revisiting the Adam-SGD gap in language modeling](https://arxiv.org/abs/2506.12543v1) | 2506.12543v1 | 7 |
| 2025-06-13 | [Vectorized Sparse Second-Order Forward Automatic Differentiation for Optimal Control Direct Methods](https://arxiv.org/abs/2506.11537v1) | 2506.11537v1 | 6 |
| 2025-06-12 | [Accelerating Newton-Schulz Iteration for Orthogonalization via Chebyshev-type Polynomials](https://arxiv.org/abs/2506.10935v2) | 2506.10935v2 | 8 |
| 2025-06-12 | [NoLoCo: No-all-reduce Low Communication Training Method for Large Models](https://arxiv.org/abs/2506.10911v2) | 2506.10911v2 | 7 |
| 2025-06-12 | [PyLO: Towards Accessible Learned Optimizers in PyTorch](https://arxiv.org/abs/2506.10315v3) | 2506.10315v3 | 10 |
| 2025-06-11 | [HiKO: A Hierarchical Framework for Beyond-Second-Order KO Codes](https://arxiv.org/abs/2506.10121v1) | 2506.10121v1 | 6 |
| 2025-06-10 | [FZOO: Fast Zeroth-Order Optimizer for Fine-Tuning Large Language Models towards Adam-Scale Speed](https://arxiv.org/abs/2506.09034v2) | 2506.09034v2 | 8 |
| 2025-06-10 | [An Efficient Augmented Lagrangian Framework for Dynamic Optimal Transport on Surfaces Based on Second-Order Cone Programming Reformulation](https://arxiv.org/abs/2506.08988v2) | 2506.08988v2 | 6 |
| 2025-06-10 | [MAC: An Efficient Gradient Preconditioning using Mean Activation Approximated Curvature](https://arxiv.org/abs/2506.08464v2) | 2506.08464v2 | 6 |
| 2025-06-10 | [Online Learning-guided Learning Rate Adaptation via Gradient Alignment](https://arxiv.org/abs/2506.08419v1) | 2506.08419v1 | 9 |
| 2025-06-10 | [Solving Convex-Concave Problems with $\tilde{\mathcal{O}}(ε^{-4/7})$ Second-Order Oracle Complexity](https://arxiv.org/abs/2506.08362v1) | 2506.08362v1 | 6 |
| 2025-06-10 | [NysAct: A Scalable Preconditioned Gradient Descent using Nystrom Approximation](https://arxiv.org/abs/2506.08360v1) | 2506.08360v1 | 6 |
| 2025-06-09 | [Neural Tangent Kernel Analysis to Probe Convergence in Physics-informed Neural Solvers: PIKANs vs. PINNs](https://arxiv.org/abs/2506.07958v1) | 2506.07958v1 | 6 |
| 2025-06-08 | [A Stable Whitening Optimizer for Efficient Neural Network Training](https://arxiv.org/abs/2506.07254v3) | 2506.07254v3 | 13 |
| 2025-06-08 | [pFedSOP : Accelerating Training Of Personalized Federated Learning Using Second-Order Optimization](https://arxiv.org/abs/2506.07159v1) | 2506.07159v1 | 8 |
| 2025-06-06 | [JGS2: Near Second-order Converging Jacobi/Gauss-Seidel for GPU Elastodynamics](https://arxiv.org/abs/2506.06494v1) | 2506.06494v1 | 7 |
| 2025-06-06 | [carps: A Framework for Comparing N Hyperparameter Optimizers on M Benchmarks](https://arxiv.org/abs/2506.06143v2) | 2506.06143v2 | 6 |
| 2025-06-05 | [Fast PET Reconstruction with Variance Reduction and Prior-Aware Preconditioning](https://arxiv.org/abs/2506.04976v1) | 2506.04976v1 | 6 |
| 2025-06-05 | [Adaptive Preconditioners Trigger Loss Spikes in Adam](https://arxiv.org/abs/2506.04805v2) | 2506.04805v2 | 11 |
| 2025-06-04 | [BINGO! Simple Optimizers Win Big if Problems Collapse to a Few Buckets](https://arxiv.org/abs/2506.04509v1) | 2506.04509v1 | 6 |
| 2025-06-04 | [OrthoGrad Improves Neural Calibration](https://arxiv.org/abs/2506.04487v3) | 2506.04487v3 | 6 |
| 2025-06-04 | [KOALA++: Efficient Kalman-Based Optimization with Gradient-Covariance Products](https://arxiv.org/abs/2506.04432v3) | 2506.04432v3 | 9 |
| 2025-06-04 | [Leveraging Coordinate Momentum in SignSGD and Muon: Memory-Optimized Zero-Order](https://arxiv.org/abs/2506.04430v4) | 2506.04430v4 | 15 |
| 2025-06-04 | [Lions and Muons: Optimization via Stochastic Frank-Wolfe under Heavy-Tailed Noise](https://arxiv.org/abs/2506.04192v4) | 2506.04192v4 | 14 |
| 2025-06-04 | [Spiking Brain Compression: Post-Training Second-order Compression for Spiking Neural Networks](https://arxiv.org/abs/2506.03996v3) | 2506.03996v3 | 6 |
| 2025-06-04 | [Sign-SGD via Parameter-Free Optimization](https://arxiv.org/abs/2506.03725v4) | 2506.03725v4 | 7 |
| 2025-06-04 | [Inexact projected preconditioned gradient methods with variable metrics: a Lyapunov convergence theory (extended version)](https://arxiv.org/abs/2506.03671v2) | 2506.03671v2 | 6 |
| 2025-06-04 | [An Improved Grey Wolf Optimizer Inspired by Advanced Cooperative Predation for UAV Shortest Path Planning](https://arxiv.org/abs/2506.03663v1) | 2506.03663v1 | 6 |
| 2025-06-04 | [Purifying Shampoo: Investigating Shampoo's Heuristics by Decomposing its Preconditioner](https://arxiv.org/abs/2506.03595v2) | 2506.03595v2 | 15 |
| 2025-06-03 | [On the Benefits of Accelerated Optimization in Robust and Private Estimation](https://arxiv.org/abs/2506.03044v1) | 2506.03044v1 | 6 |
| 2025-06-03 | [A Learned Cost Model-based Cross-engine Optimizer for SQL Workloads](https://arxiv.org/abs/2506.02802v1) | 2506.02802v1 | 6 |
| 2025-06-03 | [BenLOC: A Benchmark for Learning to Configure MIP Optimizers](https://arxiv.org/abs/2506.02752v1) | 2506.02752v1 | 6 |
| 2025-06-03 | [Multilevel Stochastic Gradient Descent for Optimal Control Under Uncertainty](https://arxiv.org/abs/2506.02647v2) | 2506.02647v2 | 6 |
| 2025-06-03 | [Efficient Quadratic Corrections for Frank-Wolfe Algorithms](https://arxiv.org/abs/2506.02635v5) | 2506.02635v5 | 6 |
| 2025-06-03 | [A Tree-guided CNN for image super-resolution](https://arxiv.org/abs/2506.02585v1) | 2506.02585v1 | 6 |
| 2025-06-02 | [GLASD: A Loss-Function-Agnostic Global Optimizer for Robust Correlation Estimation under Data Contamination and Heavy Tails](https://arxiv.org/abs/2506.14801v1) | 2506.14801v1 | 7 |
| 2025-06-02 | [Second-Order-Cone Formulations of Power Flow for Topology Optimization](https://arxiv.org/abs/2506.02234v1) | 2506.02234v1 | 6 |
| 2025-06-02 | [Generalized Gradient Norm Clipping & Non-Euclidean $(L_0,L_1)$-Smoothness](https://arxiv.org/abs/2506.01913v3) | 2506.01913v3 | 6 |
| 2025-06-02 | [MLorc: Momentum Low-rank Compression for Memory Efficient Large Language Model Adaptation](https://arxiv.org/abs/2506.01897v5) | 2506.01897v5 | 9 |
| 2025-06-02 | [Optimization Strategies for Variational Quantum Algorithms in Noisy Landscapes](https://arxiv.org/abs/2506.01715v2) | 2506.01715v2 | 6 |
| 2025-06-02 | [SysLLMatic: Large Language Models are Software System Optimizers](https://arxiv.org/abs/2506.01249v3) | 2506.01249v3 | 6 |
| 2025-06-01 | [Taming LLMs by Scaling Learning Rates with Gradient Grouping](https://arxiv.org/abs/2506.01049v1) | 2506.01049v1 | 9 |
| 2025-05-31 | [A Framework for Nonlinearly-Constrained Gradient-Enhanced Local Bayesian Optimization with Comparisons to Quasi-Newton Optimizers](https://arxiv.org/abs/2506.00648v2) | 2506.00648v2 | 8 |
| 2025-05-31 | [Antenna Q-Factor Topology Optimization with Auxiliary Edge Resistivities](https://arxiv.org/abs/2506.00595v2) | 2506.00595v2 | 6 |
| 2025-05-30 | [On the Interaction of Batch Noise, Adaptivity, and Compression, under $(L_0,L_1)$-Smoothness: An SDE Approach](https://arxiv.org/abs/2506.00181v2) | 2506.00181v2 | 7 |
| 2025-05-30 | [Who Gets Credit or Blame? Attributing Accountability in Modern AI Systems](https://arxiv.org/abs/2506.00175v5) | 2506.00175v5 | 6 |
| 2025-05-30 | [SUMO: Subspace-Aware Moment-Orthogonalization for Accelerating Memory-Efficient LLM Training](https://arxiv.org/abs/2505.24749v2) | 2505.24749v2 | 6 |
| 2025-05-30 | [LightSAM: Parameter-Agnostic Sharpness-Aware Minimization](https://arxiv.org/abs/2505.24399v1) | 2505.24399v1 | 7 |
| 2025-05-30 | [GradPower: Powering Gradients for Faster Language Model Pre-Training](https://arxiv.org/abs/2505.24275v4) | 2505.24275v4 | 9 |
| 2025-05-30 | [Unleashing High-Quality Image Generation in Diffusion Sampling Using Second-Order Levenberg-Marquardt-Langevin](https://arxiv.org/abs/2505.24222v1) | 2505.24222v1 | 7 |
| 2025-05-29 | [On the Convergence Analysis of Muon](https://arxiv.org/abs/2505.23737v3) | 2505.23737v3 | 12 |
| 2025-05-29 | [MuLoCo: Muon is a practical inner optimizer for DiLoCo](https://arxiv.org/abs/2505.23725v3) | 2505.23725v3 | 13 |
| 2025-05-29 | [Test-Time Training Done Right](https://arxiv.org/abs/2505.23884v1) | 2505.23884v1 | 8 |
| 2025-05-29 | [Accelerated Training of Federated Learning via Second-Order Methods](https://arxiv.org/abs/2505.23588v1) | 2505.23588v1 | 7 |
| 2025-05-28 | [Scalable Parameter and Memory Efficient Pretraining for LLM: Recent Algorithmic Advances and Benchmarking](https://arxiv.org/abs/2505.22922v1) | 2505.22922v1 | 6 |
| 2025-05-28 | [DES-LOC: Desynced Low Communication Adaptive Optimizers for Training Foundation Models](https://arxiv.org/abs/2505.22549v1) | 2505.22549v1 | 7 |
| 2025-05-28 | [On the Surprising Effectiveness of Large Learning Rates under Standard Width Scaling](https://arxiv.org/abs/2505.22491v2) | 2505.22491v2 | 8 |
| 2025-05-28 | [Learning to Pursue AC Optimal Power Flow Solutions with Feasibility Guarantees](https://arxiv.org/abs/2505.22399v2) | 2505.22399v2 | 6 |
| 2025-05-28 | [Numerical Optimization Strategies for the Variational Hamiltonian Ansatz in Noisy Quantum Environments](https://arxiv.org/abs/2505.22398v4) | 2505.22398v4 | 6 |
| 2025-05-28 | [PADAM: Parallel averaged Adam reduces the error for stochastic optimization in scientific machine learning](https://arxiv.org/abs/2505.22085v1) | 2505.22085v1 | 7 |
| 2025-05-28 | [Estimating the Effects of Sample Training Orders for Large Language Models without Retraining](https://arxiv.org/abs/2505.22042v1) | 2505.22042v1 | 8 |
| 2025-05-27 | [PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective](https://arxiv.org/abs/2505.21799v4) | 2505.21799v4 | 18 |
| 2025-05-27 | [Preconditioning transformations of adjoint systems for evolution equations](https://arxiv.org/abs/2505.21705v2) | 2505.21705v2 | 6 |
| 2025-05-27 | [LoFT: Low-Rank Adaptation That Behaves Like Full Fine-Tuning](https://arxiv.org/abs/2505.21289v2) | 2505.21289v2 | 6 |
| 2025-05-26 | [Gradient Flow Matching for Learning Update Dynamics in Neural Network Training](https://arxiv.org/abs/2505.20221v1) | 2505.20221v1 | 6 |
| 2025-05-26 | [Rethinking Probabilistic Circuit Parameter Learning](https://arxiv.org/abs/2505.19982v2) | 2505.19982v2 | 8 |
| 2025-05-26 | [Attention! Your Vision Language Model Could Be Maliciously Manipulated](https://arxiv.org/abs/2505.19911v2) | 2505.19911v2 | 6 |
| 2025-05-26 | [Rolling Ball Optimizer: Learning by ironing out loss landscape wrinkles](https://arxiv.org/abs/2505.19527v3) | 2505.19527v3 | 8 |
| 2025-05-25 | [Optimization-Inspired Few-Shot Adaptation for Large Language Models](https://arxiv.org/abs/2505.19107v1) | 2505.19107v1 | 6 |
| 2025-05-25 | [Efficient Data Selection at Scale via Influence Distillation](https://arxiv.org/abs/2505.19051v1) | 2505.19051v1 | 9 |
| 2025-05-24 | [Algebraic Multigrid with Filtering: An Efficient Preconditioner for Interior Point Methods in Large-Scale Contact Mechanics Optimization](https://arxiv.org/abs/2505.18576v2) | 2505.18576v2 | 7 |
| 2025-05-24 | [Autocomp: A Powerful and Portable Code Optimizer for Tensor Accelerators](https://arxiv.org/abs/2505.18574v5) | 2505.18574v5 | 6 |
| 2025-05-24 | [metaTextGrad: Automatically optimizing language model optimizers](https://arxiv.org/abs/2505.18524v2) | 2505.18524v2 | 6 |
| 2025-05-23 | [PLUMAGE: Probabilistic Low rank Unbiased Min Variance Gradient Estimator for Efficient Large Model Training](https://arxiv.org/abs/2505.18313v1) | 2505.18313v1 | 7 |
| 2025-05-22 | [The Polar Express: Optimal Matrix Sign Methods and Their Application to the Muon Algorithm](https://arxiv.org/abs/2505.16932v5) | 2505.16932v5 | 12 |
| 2025-05-22 | [AdamS: Momentum Itself Can Be A Normalizer for LLM Pretraining and Post-training](https://arxiv.org/abs/2505.16363v1) | 2505.16363v1 | 9 |
| 2025-05-21 | [Second-Order Convergence in Private Stochastic Non-Convex Optimization](https://arxiv.org/abs/2505.15647v2) | 2505.15647v2 | 8 |
| 2025-05-21 | [Mechanistic Insights into Grokking from the Embedding Layer](https://arxiv.org/abs/2505.15624v1) | 2505.15624v1 | 6 |
| 2025-05-20 | [KO: Kinetics-inspired Neural Optimizer with PDE Simulation Approaches](https://arxiv.org/abs/2505.14777v2) | 2505.14777v2 | 8 |
| 2025-05-20 | [Abacus: A Cost-Based Optimizer for Semantic Operator Systems](https://arxiv.org/abs/2505.14661v3) | 2505.14661v3 | 6 |
| 2025-05-20 | [VAMO: Efficient Zeroth-Order Variance Reduction for SGD with Faster Convergence](https://arxiv.org/abs/2505.13954v2) | 2505.13954v2 | 6 |
| 2025-05-19 | [Gluon: Making Muon & Scion Great Again! (Bridging Theory and Practice of LMO-based Optimizers for LLMs)](https://arxiv.org/abs/2505.13416v1) | 2505.13416v1 | 15 |
| 2025-05-19 | [Learning by solving differential equations](https://arxiv.org/abs/2505.13397v1) | 2505.13397v1 | 9 |
| 2025-05-19 | [Group Symmetry Enables Faster Optimization in Inverse Problems](https://arxiv.org/abs/2505.13223v2) | 2505.13223v2 | 6 |
| 2025-05-19 | [A Physics-Inspired Optimizer: Velocity Regularized Adam](https://arxiv.org/abs/2505.13196v3) | 2505.13196v3 | 11 |
| 2025-05-19 | [LiBOG: Lifelong Learning for Black-Box Optimizer Generation](https://arxiv.org/abs/2505.13025v1) | 2505.13025v1 | 6 |
| 2025-05-19 | [Implicit differentiation with second-order derivatives and benchmarks in finite-element-based differentiable physics](https://arxiv.org/abs/2505.12646v1) | 2505.12646v1 | 8 |
| 2025-05-17 | [Accelerating Neural Network Training Along Sharp and Flat Directions](https://arxiv.org/abs/2505.11972v1) | 2505.11972v1 | 6 |
| 2025-05-17 | [On the $O(\frac{\sqrt{d}}{K^{1/4}})$ Convergence Rate of AdamW Measured by $\ell_1$ Norm](https://arxiv.org/abs/2505.11840v4) | 2505.11840v4 | 7 |
| 2025-05-16 | [Permutation Randomization on Nonsmooth Nonconvex Optimization: A Theoretical and Experimental Study](https://arxiv.org/abs/2505.11752v1) | 2505.11752v1 | 6 |
| 2025-05-16 | [HOME-3: High-Order Momentum Estimator with Third-Power Gradient for Convex and Smooth Nonconvex Optimization](https://arxiv.org/abs/2505.11748v1) | 2505.11748v1 | 9 |
| 2025-05-16 | [Accelerating Natural Gradient Descent for PINNs with Randomized Numerical Linear Algebra](https://arxiv.org/abs/2505.11638v6) | 2505.11638v6 | 6 |
| 2025-05-15 | [Rethinking Prompt Optimizers: From Prompt Merits to Optimization](https://arxiv.org/abs/2505.09930v4) | 2505.09930v4 | 6 |
| 2025-05-14 | [Interim Report on Human-Guided Adaptive Hyperparameter Optimization with Multi-Fidelity Sprints](https://arxiv.org/abs/2505.09792v1) | 2505.09792v1 | 6 |
| 2025-05-14 | [A Standardized Benchmark Set of Clustering Problem Instances for Comparing Black-Box Optimizers](https://arxiv.org/abs/2505.09233v1) | 2505.09233v1 | 6 |
| 2025-05-11 | [Sparse Latent Factor Forecaster (SLFF) with Iterative Inference for Transparent Multi-Horizon Commodity Futures Prediction](https://arxiv.org/abs/2505.06795v5) | 2505.06795v5 | 6 |
| 2025-05-09 | [Fast Stochastic Second-Order Adagrad for Nonconvex Bound-Constrained Optimization](https://arxiv.org/abs/2505.06374v2) | 2505.06374v2 | 8 |
| 2025-05-08 | [The Evolution of Embedding Table Optimization and Multi-Epoch Training in Pinterest Ads Conversion](https://arxiv.org/abs/2505.05605v1) | 2505.05605v1 | 8 |
| 2025-05-08 | [An efficient second-order cone programming approach for dynamic optimal transport on staggered grid discretization](https://arxiv.org/abs/2505.05424v3) | 2505.05424v3 | 6 |
| 2025-05-08 | [ADMM-Based Training for Spiking Neural Networks](https://arxiv.org/abs/2505.05527v2) | 2505.05527v2 | 8 |
| 2025-05-07 | [FastMap: Revisiting Structure from Motion through First-Order Optimization](https://arxiv.org/abs/2505.04612v3) | 2505.04612v3 | 8 |
| 2025-05-07 | [Ordering Matters: Structure, Accuracy and Gate Cost in Second-Order Suzuki Product Formulas](https://arxiv.org/abs/2505.04240v1) | 2505.04240v1 | 6 |
| 2025-05-06 | [Iterative Orthogonalization Scaling Laws](https://arxiv.org/abs/2505.04005v2) | 2505.04005v2 | 12 |
| 2025-05-06 | [Artificial Protozoa Optimizer (APO): A novel bio-inspired metaheuristic algorithm for engineering optimization](https://arxiv.org/abs/2505.03512v1) | 2505.03512v1 | 6 |
| 2025-05-05 | [Optimal error estimates of a second-order temporally finite element method for electrohydrodynamic equations](https://arxiv.org/abs/2505.02345v1) | 2505.02345v1 | 7 |
| 2025-05-04 | [Practical Efficiency of Muon for Pretraining](https://arxiv.org/abs/2505.02222v4) | 2505.02222v4 | 16 |
| 2025-05-03 | [DiTOX: Fault Detection and Localization in the ONNX Optimizer](https://arxiv.org/abs/2505.01892v5) | 2505.01892v5 | 6 |
| 2025-05-03 | [Memory-Efficient LLM Training by Various-Grained Low-Rank Projection of Gradients](https://arxiv.org/abs/2505.01744v1) | 2505.01744v1 | 6 |
| 2025-05-03 | [DRSLF: Double Regularized Second-Order Low-Rank Representation for Web Service QoS Prediction](https://arxiv.org/abs/2505.03822v1) | 2505.03822v1 | 11 |
| 2025-05-02 | [Don't be lazy: CompleteP enables compute-efficient deep transformers](https://arxiv.org/abs/2505.01618v4) | 2505.01618v4 | 6 |
| 2025-05-02 | [Negative Stepsizes Make Gradient-Descent-Ascent Converge](https://arxiv.org/abs/2505.01423v2) | 2505.01423v2 | 8 |
| 2025-05-02 | [DHO$_2$: Accelerating Distributed Hybrid Order Optimization via Model Parallelism and ADMM](https://arxiv.org/abs/2505.00982v2) | 2505.00982v2 | 9 |
| 2025-05-01 | [Second-Order Adjoint Method for Quantum Optimal Control](https://arxiv.org/abs/2505.00529v1) | 2505.00529v1 | 11 |
| 2025-05-01 | [Pushing the Limits of Low-Bit Optimizers: A Focus on EMA Dynamics](https://arxiv.org/abs/2505.00347v2) | 2505.00347v2 | 10 |
| 2025-04-29 | [SAS-Prompt: Large Language Models as Numerical Optimizers for Robot Self-Improvement](https://arxiv.org/abs/2504.20459v1) | 2504.20459v1 | 6 |
| 2025-04-28 | [Sharp higher order convergence rates for the Adam optimizer](https://arxiv.org/abs/2504.19426v1) | 2504.19426v1 | 10 |
| 2025-04-26 | [An analytic model for description of muonic oxygen X-ray time distribution in muonic experiments](https://arxiv.org/abs/2504.19035v1) | 2504.19035v1 | 6 |
| 2025-04-26 | [Unveiling and Mitigating Adversarial Vulnerabilities in Iterative Optimizers](https://arxiv.org/abs/2504.19000v1) | 2504.19000v1 | 7 |
| 2025-04-26 | [A Langevin sampling algorithm inspired by the Adam optimizer](https://arxiv.org/abs/2504.18911v2) | 2504.18911v2 | 8 |
| 2025-04-26 | [Theoretical Framework for Tempered Fractional Gradient Descent: Application to Breast Cancer Classification](https://arxiv.org/abs/2504.18849v1) | 2504.18849v1 | 6 |
| 2025-04-26 | [Towards Practical Second-Order Optimizers in Deep Learning: Insights from Fisher Information Analysis](https://arxiv.org/abs/2504.20096v1) | 2504.20096v1 | 14 |
| 2025-04-26 | [Optimization of Next-Day Delivery Coverage using Constraint Programming and Random Key Optimizers](https://arxiv.org/abs/2504.18749v1) | 2504.18749v1 | 6 |
| 2025-04-25 | [A Gradient-Optimized TSK Fuzzy Framework for Explainable Phishing Detection](https://arxiv.org/abs/2504.18636v2) | 2504.18636v2 | 6 |
| 2025-04-24 | [Improving Deep Knowledge Tracing via Gated Architectures and Adaptive Optimization](https://arxiv.org/abs/2504.20070v1) | 2504.20070v1 | 8 |
| 2025-04-23 | [Preconditioning Natural and Second Order Gradient Descent in Quantum Optimization: A Performance Benchmark](https://arxiv.org/abs/2504.16518v1) | 2504.16518v1 | 6 |
| 2025-04-22 | [CGD: Modifying the Loss Landscape by Gradient Regularization](https://arxiv.org/abs/2504.16182v3) | 2504.16182v3 | 6 |
| 2025-04-22 | [Muon Optimizer Accelerates Grokking](https://arxiv.org/abs/2504.16041v1) | 2504.16041v1 | 16 |
| 2025-04-22 | [AlphaGrad: Non-Linear Gradient Normalization Optimizer](https://arxiv.org/abs/2504.16020v2) | 2504.16020v2 | 10 |
| 2025-04-22 | [Recovering Nesterov accelerated dynamics from Heavy Ball dynamics via time rescaling](https://arxiv.org/abs/2504.15852v1) | 2504.15852v1 | 6 |
| 2025-04-22 | [DualOptim: Enhancing Efficacy and Stability in Machine Unlearning with Dual Optimizers](https://arxiv.org/abs/2504.15827v2) | 2504.15827v2 | 10 |
| 2025-04-21 | [Improving Learning to Optimize Using Parameter Symmetries](https://arxiv.org/abs/2504.15399v1) | 2504.15399v1 | 6 |
| 2025-04-21 | [AdGT: Decentralized Gradient Tracking with Adaptive Per-Agent Stepsizes](https://arxiv.org/abs/2504.15196v5) | 2504.15196v5 | 6 |
| 2025-04-21 | [Fast-Slow Co-advancing Optimizer: Toward Harmonious Adversarial Training of GAN](https://arxiv.org/abs/2504.15099v1) | 2504.15099v1 | 11 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-31 | [Design Optimizer for Soft Growing Robot Manipulators in Three-Dimensional Environments](https://arxiv.org/abs/2501.00368v3) | 2501.00368v3 | 6 |
| 2024-12-30 | [Adaptive Batch Size Schedules for Distributed Training of Language Models with Data and Model Parallelism](https://arxiv.org/abs/2412.21124v2) | 2412.21124v2 | 6 |
| 2024-12-30 | [Fine-Tuning TransMorph with Gradient Correlation for Anatomical Alignment](https://arxiv.org/abs/2412.20822v1) | 2412.20822v1 | 6 |
| 2024-12-29 | [EXAdam: The Power of Adaptive Cross-Moments](https://arxiv.org/abs/2412.20302v2) | 2412.20302v2 | 6 |
| 2024-12-28 | [A Nearly Optimal Single Loop Algorithm for Stochastic Bilevel Optimization under Unbounded Smoothness](https://arxiv.org/abs/2412.20017v1) | 2412.20017v1 | 7 |
| 2024-12-27 | [On the numerical solution of Lasserre relaxations of unconstrained binary quadratic optimization problem](https://arxiv.org/abs/2412.19776v1) | 2412.19776v1 | 9 |
| 2024-12-27 | [Gradient Weight-normalized Low-rank Projection for Efficient LLM Training](https://arxiv.org/abs/2412.19616v2) | 2412.19616v2 | 6 |
| 2024-12-27 | [On second-order optimality conditions for $C^{1,1}$ optimization problems via Lagrangian functions](https://arxiv.org/abs/2412.19557v1) | 2412.19557v1 | 6 |
| 2024-12-26 | [Nanofiber-based second-order atomic Bragg lattice for collectively enhanced coupling](https://arxiv.org/abs/2412.19343v1) | 2412.19343v1 | 6 |
| 2024-12-26 | [Overlapping Schwarz Preconditioners for Randomized Neural Networks with Domain Decomposition](https://arxiv.org/abs/2412.19207v1) | 2412.19207v1 | 7 |
| 2024-12-26 | [Variational Quantum Eigensolver: A Comparative Analysis of Classical and Quantum Optimizer Methods](https://arxiv.org/abs/2412.19176v3) | 2412.19176v3 | 8 |
| 2024-12-25 | [New Theorem on Chaos Transitions in Second-Order Dynamical Systems with Tikhonov Regularization](https://arxiv.org/abs/2412.19003v1) | 2412.19003v1 | 6 |
| 2024-12-25 | [Torque-Aware Momentum](https://arxiv.org/abs/2412.18790v1) | 2412.18790v1 | 8 |
| 2024-12-24 | [Leveraging Convolutional Neural Network-Transformer Synergy for Predictive Modeling in Risk-Based Applications](https://arxiv.org/abs/2412.18222v1) | 2412.18222v1 | 6 |
| 2024-12-22 | [Second-order sufficient optimality conditions in the calculus of variations](https://arxiv.org/abs/2412.17166v1) | 2412.17166v1 | 6 |
| 2024-12-22 | [Adam on Local Time: Addressing Nonstationarity in RL with Relative Adam Timesteps](https://arxiv.org/abs/2412.17113v1) | 2412.17113v1 | 9 |
| 2024-12-22 | [Grams: Gradient Descent with Adaptive Momentum Scaling](https://arxiv.org/abs/2412.17107v3) | 2412.17107v3 | 9 |
| 2024-12-20 | [Foxtsage vs. Adam: Revolution or Evolution in Optimization?](https://arxiv.org/abs/2412.17855v1) | 2412.17855v1 | 6 |
| 2024-12-20 | [Task-Specific Preconditioner for Cross-Domain Few-Shot Learning](https://arxiv.org/abs/2412.15483v1) | 2412.15483v1 | 7 |
| 2024-12-19 | [Randomized Subspace Derivative-Free Optimization with Quadratic Models and Second-Order Convergence](https://arxiv.org/abs/2412.14431v1) | 2412.14431v1 | 7 |
| 2024-12-17 | [Training Dynamics of a 1.7B LLaMa Model: A Data-Efficient Approach](https://arxiv.org/abs/2412.13335v3) | 2412.13335v3 | 6 |
| 2024-12-17 | [A hierarchical splines-based $h$-adaptive isogeometric solver for all-electron Kohn--Sham equation](https://arxiv.org/abs/2412.12580v1) | 2412.12580v1 | 6 |
| 2024-12-16 | [No More Adam: Learning Rate Scaling at Initialization is All You Need](https://arxiv.org/abs/2412.11768v2) | 2412.11768v2 | 14 |
| 2024-12-16 | [Non-Convex Optimization in Federated Learning via Variance Reduction and Adaptive Learning](https://arxiv.org/abs/2412.11660v1) | 2412.11660v1 | 6 |
| 2024-12-15 | [GaLore$+$: Boosting Low-Rank Adaptation for LLMs with Cross-Head Projection](https://arxiv.org/abs/2412.19820v1) | 2412.19820v1 | 8 |
| 2024-12-14 | [Memory-Efficient 4-bit Preconditioned Stochastic Optimization](https://arxiv.org/abs/2412.10663v2) | 2412.10663v2 | 13 |
| 2024-12-13 | [OP-LoRA: The Blessing of Dimensionality](https://arxiv.org/abs/2412.10362v2) | 2412.10362v2 | 7 |
| 2024-12-13 | [Fully stochastic trust-region methods with Barzilai-Borwein steplengths](https://arxiv.org/abs/2412.12180v2) | 2412.12180v2 | 6 |
| 2024-12-12 | [GReaTer: Gradients over Reasoning Makes Smaller Language Models Strong Prompt Optimizers](https://arxiv.org/abs/2412.09722v2) | 2412.09722v2 | 7 |
| 2024-12-12 | [SMMF: Square-Matricized Momentum Factorization for Memory-Efficient Optimization](https://arxiv.org/abs/2412.08894v2) | 2412.08894v2 | 9 |
| 2024-12-11 | [MeshCone: Second-Order Cone Programming for Geometrically-Constrained Mesh Enhancement](https://arxiv.org/abs/2412.08484v5) | 2412.08484v5 | 6 |
| 2024-12-11 | [Towards Automated Algebraic Multigrid Preconditioner Design Using Genetic Programming for Large-Scale Laser Beam Welding Simulations](https://arxiv.org/abs/2412.08186v1) | 2412.08186v1 | 6 |
| 2024-12-11 | [Momentum-Accelerated Richardson(m) and Their Multilevel Neural Solvers](https://arxiv.org/abs/2412.08076v1) | 2412.08076v1 | 8 |
| 2024-12-09 | [Impact of Privacy Parameters on Deep Learning Models for Image Classification](https://arxiv.org/abs/2412.06689v1) | 2412.06689v1 | 6 |
| 2024-12-06 | [APOLLO: SGD-like Memory, AdamW-level Performance](https://arxiv.org/abs/2412.05270v4) | 2412.05270v4 | 7 |
| 2024-12-06 | [A Parametric, Second-Order Cone Representable Model of Fairness for Decision-Making Problems](https://arxiv.org/abs/2412.05143v1) | 2412.05143v1 | 6 |
| 2024-12-05 | [HeatFormer: A Neural Optimizer for Multiview Human Mesh Recovery](https://arxiv.org/abs/2412.04456v3) | 2412.04456v3 | 6 |
| 2024-12-04 | [Stochastic Gradient Estimation for Higher-order Differentiable Rendering](https://arxiv.org/abs/2412.03489v3) | 2412.03489v3 | 6 |
| 2024-12-04 | [Extracting Dual Solutions via Primal Optimizers](https://arxiv.org/abs/2412.02949v1) | 2412.02949v1 | 6 |
| 2024-12-03 | [Efficient parallel inversion of ParaOpt preconditioners](https://arxiv.org/abs/2412.02425v1) | 2412.02425v1 | 6 |
| 2024-12-03 | [HERO: Hint-Based Efficient and Reliable Query Optimizer](https://arxiv.org/abs/2412.02372v2) | 2412.02372v2 | 6 |
| 2024-12-03 | [Efficient Model Compression Techniques with FishLeg](https://arxiv.org/abs/2412.02328v1) | 2412.02328v1 | 8 |
| 2024-12-03 | [Conformal Symplectic Optimization for Stable Reinforcement Learning](https://arxiv.org/abs/2412.02291v2) | 2412.02291v2 | 10 |
| 2024-12-03 | [Revisiting the Initial Steps in Adaptive Gradient Descent Optimization](https://arxiv.org/abs/2412.02153v2) | 2412.02153v2 | 10 |
| 2024-12-02 | [PROFIT: A Specialized Optimizer for Deep Fine Tuning](https://arxiv.org/abs/2412.01930v3) | 2412.01930v3 | 7 |
| 2024-11-30 | [Enhancing Skin Cancer Diagnosis (SCD) Using Late Discrete Wavelet Transform (DWT) and New Swarm-Based Optimizers](https://arxiv.org/abs/2412.00472v1) | 2412.00472v1 | 6 |
| 2024-11-29 | [DeMo: Decoupled Momentum Optimization](https://arxiv.org/abs/2411.19870v2) | 2411.19870v2 | 9 |
| 2024-11-29 | [On the Performance Analysis of Momentum Method: A Frequency Domain Perspective](https://arxiv.org/abs/2411.19671v6) | 2411.19671v6 | 8 |
| 2024-11-29 | [CAdam: Confidence-Based Optimization for Online Learning](https://arxiv.org/abs/2411.19647v2) | 2411.19647v2 | 9 |
| 2024-11-28 | [ReMAP: Lossless Residual Neural Lifting for Scalable MAP Inference in Arbitrary-Order Markov Random Fields](https://arxiv.org/abs/2411.18954v5) | 2411.18954v5 | 9 |
| 2024-11-27 | [Second-order correlation and squeezing of photons in cavities with ultrastrong magnon-photon interactions](https://arxiv.org/abs/2411.18512v3) | 2411.18512v3 | 6 |
| 2024-11-27 | [Federated Learning with Uncertainty and Personalization via Efficient Second-order Optimization](https://arxiv.org/abs/2411.18385v1) | 2411.18385v1 | 6 |
| 2024-11-27 | [Preserving Deep Representations In One-Shot Pruning: A Hessian-Free Second-Order Optimization Framework](https://arxiv.org/abs/2411.18376v1) | 2411.18376v1 | 6 |
| 2024-11-27 | [Predicting Water Quality using Quantum Machine Learning: The Case of the Umgeni Catchment (U20A) Study Region](https://arxiv.org/abs/2411.18141v1) | 2411.18141v1 | 6 |
| 2024-11-26 | [Distributed Sign Momentum with Local Steps for Training Transformers](https://arxiv.org/abs/2411.17866v2) | 2411.17866v2 | 9 |
| 2024-11-25 | [Lion Cub: Minimizing Communication Overhead in Distributed Lion](https://arxiv.org/abs/2411.16462v2) | 2411.16462v2 | 8 |
| 2024-11-25 | [Deep Unfolding-Empowered MmWave Massive MIMO Joint Communications and Sensing](https://arxiv.org/abs/2411.17747v1) | 2411.17747v1 | 6 |
| 2024-11-25 | [A Learn-to-Optimize Approach for Coordinate-Wise Step Sizes for Quasi-Newton Methods](https://arxiv.org/abs/2412.00059v2) | 2412.00059v2 | 6 |
| 2024-11-25 | [Cautious Optimizers: Improving Training with One Line of Code](https://arxiv.org/abs/2411.16085v4) | 2411.16085v4 | 9 |
| 2024-11-24 | [Adaptive Methods through the Lens of SDEs: Theoretical Insights on the Role of Noise](https://arxiv.org/abs/2411.15958v2) | 2411.15958v2 | 6 |
| 2024-11-24 | [ExAL: An Exploration Enhanced Adversarial Learning Algorithm](https://arxiv.org/abs/2411.15878v1) | 2411.15878v1 | 6 |
| 2024-11-24 | [Beyond adaptive gradient: Fast-Controlled Minibatch Algorithm for large-scale optimization](https://arxiv.org/abs/2411.15795v3) | 2411.15795v3 | 6 |
| 2024-11-24 | [An Improved Dung Beetle Optimizer for Random Forest Optimization](https://arxiv.org/abs/2411.17738v1) | 2411.17738v1 | 7 |
| 2024-11-24 | [Learning Algorithm Hyperparameters for Fast Parametric Convex Optimization](https://arxiv.org/abs/2411.15717v1) | 2411.15717v1 | 6 |
| 2024-11-22 | [Jovis: A Visualization Tool for PostgreSQL Query Optimizer](https://arxiv.org/abs/2411.14788v2) | 2411.14788v2 | 6 |
| 2024-11-21 | [Post-selected von Neumann Measurement with Superpositions of Orbital-Angular-Momentum Pointer States](https://arxiv.org/abs/2411.14210v2) | 2411.14210v2 | 7 |
| 2024-11-21 | [Towards Adaptive Asynchronous Federated Learning for Human Activity Recognition](https://arxiv.org/abs/2411.14070v1) | 2411.14070v1 | 6 |
| 2024-11-20 | [Towards Query Optimizer as a Service (QOaaS) in a Unified LakeHouse Ecosystem: Can One QO Rule Them All?](https://arxiv.org/abs/2411.13704v1) | 2411.13704v1 | 6 |
| 2024-11-20 | [Optimization of Second-Order Transport Models for Transition-Continuum Flows](https://arxiv.org/abs/2411.13515v2) | 2411.13515v2 | 8 |
| 2024-11-19 | [Exact Risk Curves of signSGD in High-Dimensions: Quantifying Preconditioning and Noise-Compression Effects](https://arxiv.org/abs/2411.12135v3) | 2411.12135v3 | 7 |
| 2024-11-18 | [Don't Be So Positive: Negative Step Sizes in Second-Order Methods](https://arxiv.org/abs/2411.11224v2) | 2411.11224v2 | 10 |
| 2024-11-17 | [Timing-driven Approximate Logic Synthesis Based on Double-chase Grey Wolf Optimizer](https://arxiv.org/abs/2411.10990v1) | 2411.10990v1 | 6 |
| 2024-11-16 | [HELENE: Hessian Layer-wise Clipping and Gradient Annealing for Accelerating Fine-tuning LLM with Zeroth-order Optimization](https://arxiv.org/abs/2411.10696v1) | 2411.10696v1 | 10 |
| 2024-11-15 | [MARS: Unleashing the Power of Variance Reduction for Training Large Models](https://arxiv.org/abs/2411.10438v4) | 2411.10438v4 | 11 |
| 2024-11-15 | [Exploiting Negative Curvature in Conjunction with Adaptive Sampling: Theoretical Results and a Practical Algorithm](https://arxiv.org/abs/2411.10378v1) | 2411.10378v1 | 6 |
| 2024-11-14 | [Strong Metric Subregularity of the optimality mapping and second-order sufficient optimality conditions in extremal problems with constraints](https://arxiv.org/abs/2411.09395v1) | 2411.09395v1 | 6 |
| 2024-11-14 | [Iterative tomographic reconstruction with TV prior for low-dose CBCT dental imaging](https://arxiv.org/abs/2411.09306v1) | 2411.09306v1 | 6 |
| 2024-11-12 | [Exact, Tractable Gauss-Newton Optimization in Deep Reversible Architectures Reveal Poor Generalization](https://arxiv.org/abs/2411.07979v2) | 2411.07979v2 | 8 |
| 2024-11-12 | [FRUGAL: Memory-Efficient Optimization by Reducing State Overhead for Scalable Training](https://arxiv.org/abs/2411.07837v3) | 2411.07837v3 | 6 |
| 2024-11-12 | [Convergence Rate Analysis of LION](https://arxiv.org/abs/2411.07724v2) | 2411.07724v2 | 8 |
| 2024-11-12 | [Second-order Optimality Conditions for Time-Optimal Control Problems Governed by Semilinear Parabolic Equations](https://arxiv.org/abs/2411.07723v1) | 2411.07723v1 | 6 |
| 2024-11-11 | [Lean and Mean Adaptive Optimization via Subset-Norm and Subspace-Momentum with Convergence Guarantees](https://arxiv.org/abs/2411.07120v2) | 2411.07120v2 | 8 |
| 2024-11-11 | [Sketched Adaptive Federated Deep Learning: A Sharp Convergence Analysis](https://arxiv.org/abs/2411.06770v3) | 2411.06770v3 | 10 |
| 2024-11-09 | [A Natural Primal-Dual Hybrid Gradient Method for Adversarial Neural Network Training on Solving Partial Differential Equations](https://arxiv.org/abs/2411.06278v4) | 2411.06278v4 | 6 |
| 2024-11-09 | [StiffGIPC: Advancing GPU IPC for stiff affine-deformable simulation](https://arxiv.org/abs/2411.06224v4) | 2411.06224v4 | 6 |
| 2024-11-08 | [On Training of Kolmogorov-Arnold Networks](https://arxiv.org/abs/2411.05296v1) | 2411.05296v1 | 8 |
| 2024-11-07 | [Solving Hidden Monotone Variational Inequalities with Surrogate Losses](https://arxiv.org/abs/2411.05228v3) | 2411.05228v3 | 6 |
| 2024-11-07 | [GenJoin: Conditional Generative Plan-to-Plan Query Optimizer that Learns from Subplan Hints](https://arxiv.org/abs/2411.04525v2) | 2411.04525v2 | 6 |
| 2024-11-07 | [Optimal Allocation of Pauli Measurements for Low-rank Quantum State Tomography](https://arxiv.org/abs/2411.04452v1) | 2411.04452v1 | 6 |
| 2024-11-06 | [Variational Analysis of a Nonconvex and Nonsmooth Optimization Problem: An Introduction](https://arxiv.org/abs/2411.04317v2) | 2411.04317v2 | 6 |
| 2024-11-06 | [A Random-Key Optimizer for Combinatorial Optimization](https://arxiv.org/abs/2411.04293v3) | 2411.04293v3 | 6 |
| 2024-11-06 | [On a probabilistic global optimizer derived from the Walker slice sampling](https://arxiv.org/abs/2411.03851v1) | 2411.03851v1 | 6 |
| 2024-11-06 | [Designing a Linearized Potential Function in Neural Network Optimization Using Csiszár Type of Tsallis Entropy](https://arxiv.org/abs/2411.03611v1) | 2411.03611v1 | 6 |
| 2024-11-05 | [A stabilized nonconforming finite element method for the surface biharmonic problem](https://arxiv.org/abs/2411.02952v1) | 2411.02952v1 | 6 |
| 2024-11-04 | [Gradient Methods with Online Scaling](https://arxiv.org/abs/2411.01803v2) | 2411.01803v2 | 6 |
| 2024-11-03 | [Rethinking Weight Decay for Robust Fine-Tuning of Foundation Models](https://arxiv.org/abs/2411.01713v1) | 2411.01713v1 | 11 |
| 2024-11-01 | [Beyond the Boundaries of Proximal Policy Optimization](https://arxiv.org/abs/2411.00666v1) | 2411.00666v1 | 9 |
| 2024-11-01 | [Diffusion Models as Network Optimizers: Explorations and Analysis](https://arxiv.org/abs/2411.00453v5) | 2411.00453v5 | 7 |
| 2024-10-31 | [CaAdam: Improving Adam optimizer using connection aware methods](https://arxiv.org/abs/2410.24216v1) | 2410.24216v1 | 10 |
| 2024-10-31 | [Analyzing & Reducing the Need for Learning Rate Warmup in GPT Training](https://arxiv.org/abs/2410.23922v1) | 2410.23922v1 | 7 |
| 2024-10-31 | [Optimization over convex polyhedra via Hadamard parametrizations](https://arxiv.org/abs/2410.23874v1) | 2410.23874v1 | 6 |
| 2024-10-30 | [Exploring Gradient Subspaces: Addressing and Overcoming LoRA's Limitations in Federated Fine-Tuning of Large Language Models](https://arxiv.org/abs/2410.23111v6) | 2410.23111v6 | 6 |
| 2024-10-30 | [Coupling deal.II and FROSch: A Sustainable and Accessible (O)RAS Preconditioner](https://arxiv.org/abs/2410.22871v1) | 2410.22871v1 | 6 |
| 2024-10-30 | [An optimal diagonalization-based preconditioner for parabolic optimal control problems](https://arxiv.org/abs/2410.22686v2) | 2410.22686v2 | 7 |
| 2024-10-29 | [Fast Deep Hedging with Second-Order Optimization](https://arxiv.org/abs/2410.22568v1) | 2410.22568v1 | 8 |
| 2024-10-29 | [Flavors of Margin: Implicit Bias of Steepest Descent in Homogeneous Neural Networks](https://arxiv.org/abs/2410.22069v4) | 2410.22069v4 | 6 |
| 2024-10-28 | [Second-Order Analysis of CSMA Protocols for Age-of-Information Minimization](https://arxiv.org/abs/2410.21473v1) | 2410.21473v1 | 6 |
| 2024-10-27 | [Logarithmically Quantized Distributed Optimization over Dynamic Multi-Agent Networks](https://arxiv.org/abs/2410.20345v1) | 2410.20345v1 | 6 |
| 2024-10-26 | [Deep Optimizer States: Towards Scalable Training of Transformer Models Using Interleaved Offloading](https://arxiv.org/abs/2410.21316v2) | 2410.21316v2 | 7 |
| 2024-10-25 | [Improving Stochastic Cubic Newton with Momentum](https://arxiv.org/abs/2410.19644v2) | 2410.19644v2 | 9 |
| 2024-10-25 | [Asymptotic expansion for a class of second-order evolution equations in the energy space and its applications](https://arxiv.org/abs/2410.19366v1) | 2410.19366v1 | 6 |
| 2024-10-25 | [Fully First-Order Methods for Decentralized Bilevel Optimization](https://arxiv.org/abs/2410.19319v2) | 2410.19319v2 | 6 |
| 2024-10-25 | [COAT: Compressing Optimizer states and Activation for Memory-Efficient FP8 Training](https://arxiv.org/abs/2410.19313v3) | 2410.19313v3 | 6 |
| 2024-10-24 | [No-gap second-order optimality conditions for additive manufacturing](https://arxiv.org/abs/2410.18776v1) | 2410.18776v1 | 7 |
| 2024-10-24 | [Nonconforming virtual element method for general second-order elliptic problems on curved domain](https://arxiv.org/abs/2410.18526v1) | 2410.18526v1 | 7 |
| 2024-10-23 | [AdaRankGrad: Adaptive Gradient-Rank and Moments for Memory-Efficient LLMs Training and Fine-Tuning](https://arxiv.org/abs/2410.17881v2) | 2410.17881v2 | 6 |
| 2024-10-21 | [Revisiting Gradient Normalization and Clipping for Nonconvex SGD under Heavy-Tailed Noise: Necessity, Sufficiency, and Acceleration](https://arxiv.org/abs/2410.16561v4) | 2410.16561v4 | 6 |
| 2024-10-21 | [Efficient Neural Network Training via Subset Pretraining](https://arxiv.org/abs/2410.16523v2) | 2410.16523v2 | 7 |
| 2024-10-21 | [LDAdam: Adaptive Optimization from Low-Dimensional Gradient Statistics](https://arxiv.org/abs/2410.16103v4) | 2410.16103v4 | 6 |
| 2024-10-21 | [Natural GaLore: Accelerating GaLore for memory-efficient LLM Training and Fine-tuning](https://arxiv.org/abs/2410.16029v1) | 2410.16029v1 | 9 |
| 2024-10-21 | [An Efficient Local Optimizer-Tracking Solver for Differential-Algebriac Equations with Optimization Criteria](https://arxiv.org/abs/2410.15963v1) | 2410.15963v1 | 7 |
| 2024-10-21 | [Improving Parallel Program Performance with LLM Optimizers via Agent-System Interfaces](https://arxiv.org/abs/2410.15625v4) | 2410.15625v4 | 6 |
| 2024-10-20 | [SDP4Bit: Toward 4-bit Communication Quantization in Sharded Data Parallelism for LLM Training](https://arxiv.org/abs/2410.15526v2) | 2410.15526v2 | 6 |
| 2024-10-19 | [Optimizing Unitary Coupled Cluster Wave Functions on Quantum Hardware: Error Bound and Resource-Efficient Optimizer](https://arxiv.org/abs/2410.15129v3) | 2410.15129v3 | 7 |
| 2024-10-18 | [Debiasing Mini-Batch Quadratics for Applications in Deep Learning](https://arxiv.org/abs/2410.14325v2) | 2410.14325v2 | 8 |
| 2024-10-18 | [A Communication and Computation Efficient Fully First-order Method for Decentralized Bilevel Optimization](https://arxiv.org/abs/2410.14115v1) | 2410.14115v1 | 6 |
| 2024-10-16 | [Quantum Boltzmann machine learning of ground-state energies](https://arxiv.org/abs/2410.12935v3) | 2410.12935v3 | 6 |
| 2024-10-16 | [Loss Landscape Characterization of Neural Networks without Over-Parametrization](https://arxiv.org/abs/2410.12455v3) | 2410.12455v3 | 6 |
| 2024-10-15 | [LoKO: Low-Rank Kalman Optimizer for Online Fine-Tuning of Large Models](https://arxiv.org/abs/2410.11551v2) | 2410.11551v2 | 7 |
| 2024-10-14 | [What Does It Mean to Be a Transformer? Insights from a Theoretical Hessian Analysis](https://arxiv.org/abs/2410.10986v2) | 2410.10986v2 | 6 |
| 2024-10-14 | [SAMPa: Sharpness-aware Minimization Parallelized](https://arxiv.org/abs/2410.10683v1) | 2410.10683v1 | 6 |
| 2024-10-14 | [Non-convergence to global minimizers in data driven supervised deep learning: Adam and stochastic gradient descent optimization provably fail to converge to global minimizers in the training of deep neural networks with ReLU activation](https://arxiv.org/abs/2410.10533v2) | 2410.10533v2 | 8 |
| 2024-10-14 | [The Epochal Sawtooth Phenomenon: Unveiling Training Loss Oscillations in Adam and Other Optimizers](https://arxiv.org/abs/2410.10056v3) | 2410.10056v3 | 9 |
| 2024-10-13 | [Dynamic Estimation of Learning Rates Using a Non-Linear Autoregressive Model](https://arxiv.org/abs/2410.09943v2) | 2410.09943v2 | 11 |
| 2024-10-13 | [Simultaneous Computation and Memory Efficient Zeroth-Order Optimizer for Fine-Tuning Large Language Models](https://arxiv.org/abs/2410.09823v1) | 2410.09823v1 | 7 |
| 2024-10-12 | [Second-Order Min-Max Optimization with Lazy Hessians](https://arxiv.org/abs/2410.09568v2) | 2410.09568v2 | 6 |
| 2024-10-11 | [Efficient Hyperparameter Importance Assessment for CNNs](https://arxiv.org/abs/2410.08920v1) | 2410.08920v1 | 6 |
| 2024-10-10 | [On Barycenter Computation: Semi-Unbalanced Optimal Transport-based Method on Gaussians](https://arxiv.org/abs/2410.08117v1) | 2410.08117v1 | 6 |
| 2024-10-10 | [Second-Order Optimization via Quiescence](https://arxiv.org/abs/2410.08033v1) | 2410.08033v1 | 7 |
| 2024-10-10 | [Metamizer: a versatile neural optimizer for fast and accurate physics simulations](https://arxiv.org/abs/2410.19746v2) | 2410.19746v2 | 8 |
| 2024-10-10 | [Dense Optimizer : An Information Entropy-Guided Structural Search Method for Dense-like Neural Network Design](https://arxiv.org/abs/2410.07499v1) | 2410.07499v1 | 6 |
| 2024-10-10 | [Efficient Adaptive Federated Optimization](https://arxiv.org/abs/2410.18117v3) | 2410.18117v3 | 9 |
| 2024-10-09 | [Adversarial Vulnerability as a Consequence of On-Manifold Inseparibility](https://arxiv.org/abs/2410.06921v1) | 2410.06921v1 | 10 |
| 2024-10-09 | [Noise is All You Need: Private Second-Order Convergence of Noisy SGD](https://arxiv.org/abs/2410.06878v1) | 2410.06878v1 | 8 |
| 2024-10-09 | [Optimizing Transformer based on high-performance optimizer for predicting employment sentiment in American social media content](https://arxiv.org/abs/2410.10874v1) | 2410.10874v1 | 6 |
| 2024-10-09 | [Addax: Utilizing Zeroth-Order Gradients to Improve Memory Efficiency and Performance of SGD for Fine-Tuning Language Models](https://arxiv.org/abs/2410.06441v1) | 2410.06441v1 | 6 |
| 2024-10-08 | [Unveiling the Backbone-Optimizer Coupling Bias in Visual Representation Learning](https://arxiv.org/abs/2410.06373v1) | 2410.06373v1 | 8 |
| 2024-10-08 | [GLOV: Guided Large Language Models as Implicit Optimizers for Vision Language Models](https://arxiv.org/abs/2410.06154v6) | 2410.06154v6 | 6 |
| 2024-10-08 | [A second-order-like optimizer with adaptive gradient scaling for deep learning](https://arxiv.org/abs/2410.05871v2) | 2410.05871v2 | 15 |
| 2024-10-08 | [A Parameter Update Balancing Algorithm for Multi-task Ranking Models in Recommendation Systems](https://arxiv.org/abs/2410.05806v2) | 2410.05806v2 | 7 |
| 2024-10-07 | [$\ell_1$-norm rank-one symmetric matrix factorization has no spurious second-order stationary points](https://arxiv.org/abs/2410.05025v1) | 2410.05025v1 | 6 |
| 2024-10-07 | [Wide Neural Networks Trained with Weight Decay Provably Exhibit Neural Collapse](https://arxiv.org/abs/2410.04887v1) | 2410.04887v1 | 7 |
| 2024-10-07 | [On the Optimization and Generalization of Two-layer Transformers with Sign Gradient Descent](https://arxiv.org/abs/2410.04870v2) | 2410.04870v2 | 6 |
| 2024-10-06 | [Support Graph Preconditioners for Off-Lattice Cell-Based Models](https://arxiv.org/abs/2410.04512v2) | 2410.04512v2 | 7 |
| 2024-10-05 | [OPTAMI: Global Superlinear Convergence of High-order Methods](https://arxiv.org/abs/2410.04083v2) | 2410.04083v2 | 9 |
| 2024-10-05 | [Accessible Complexity Bounds for Restarted PDHG on Linear Programs with a Unique Optimizer](https://arxiv.org/abs/2410.04043v5) | 2410.04043v5 | 7 |
| 2024-10-04 | [DiSK: Differentially Private Optimizer with Simplified Kalman Filter for Noise Reduction](https://arxiv.org/abs/2410.03883v2) | 2410.03883v2 | 7 |
| 2024-06-30 | [BADM: Batch ADMM for Deep Learning](https://arxiv.org/abs/2407.01640v2) | 2407.01640v2 | 6 |
| 2024-06-29 | [A Review of Neural Network Solvers for Second-order Boundary Value Problems](https://arxiv.org/abs/2407.00442v2) | 2407.00442v2 | 6 |
| 2024-06-29 | [C-MASS: Combinatorial Mobility-Aware Sensor Scheduling for Collaborative Perception with Second-Order Topology Approximation](https://arxiv.org/abs/2407.00412v1) | 2407.00412v1 | 6 |
| 2024-06-27 | [Resolving Discrepancies in Compute-Optimal Scaling of Language Models](https://arxiv.org/abs/2406.19146v4) | 2406.19146v4 | 6 |
| 2024-06-27 | [Modified-Improved Fitness Dependent Optimizer for Complex and Engineering Problems](https://arxiv.org/abs/2407.14271v1) | 2407.14271v1 | 7 |
| 2024-06-26 | [Fast Optimizer Benchmark](https://arxiv.org/abs/2406.18701v1) | 2406.18701v1 | 6 |
| 2024-06-26 | [Learning-rate-free Momentum SGD with Reshuffling Converges in Nonsmooth Nonconvex Optimization](https://arxiv.org/abs/2406.18287v1) | 2406.18287v1 | 7 |
| 2024-06-25 | [Why Line Search when you can Plane Search? SO-Friendly Neural Networks allow Per-Iteration Optimization of Learning and Momentum Rates for Every Layer](https://arxiv.org/abs/2406.17954v1) | 2406.17954v1 | 6 |
| 2024-06-25 | [A New Perspective on Shampoo's Preconditioner](https://arxiv.org/abs/2406.17748v1) | 2406.17748v1 | 21 |
| 2024-06-25 | [Nonclassical Light in a Three-Waveguide Coupler with Second-Order Nonlinearity](https://arxiv.org/abs/2406.17407v1) | 2406.17407v1 | 6 |
| 2024-06-24 | [Adam-mini: Use Fewer Learning Rates To Gain More](https://arxiv.org/abs/2406.16793v7) | 2406.16793v7 | 7 |
| 2024-06-22 | [Towards Exact Computation of Inductive Bias](https://arxiv.org/abs/2406.15941v1) | 2406.15941v1 | 6 |
| 2024-06-20 | [Learning rate adaptive stochastic gradient descent optimization methods: numerical simulations for deep learning methods for partial differential equations and convergence analyses](https://arxiv.org/abs/2406.14340v2) | 2406.14340v2 | 9 |
| 2024-06-20 | [Improving Convergence Guarantees of Random Subspace Second-order Algorithm for Nonconvex Optimization](https://arxiv.org/abs/2406.14337v2) | 2406.14337v2 | 7 |
| 2024-06-20 | [Symplectic Stiefel manifold: tractable metrics, second-order geometry and Newton's methods](https://arxiv.org/abs/2406.14299v1) | 2406.14299v1 | 7 |
| 2024-06-20 | [Non-overshooting continuous in convergence sliding mode control of second-order systems](https://arxiv.org/abs/2406.14000v3) | 2406.14000v3 | 7 |
| 2024-06-19 | [Aubin Property and Strong Regularity Are Equivalent for Nonlinear Second-Order Cone Programming](https://arxiv.org/abs/2406.13798v3) | 2406.13798v3 | 6 |
| 2024-06-17 | [ExCP: Extreme LLM Checkpoint Compression via Weight-Momentum Joint Shrinking](https://arxiv.org/abs/2406.11257v1) | 2406.11257v1 | 7 |
| 2024-06-16 | [Two-level overlapping additive Schwarz preconditioner for training scientific machine learning applications](https://arxiv.org/abs/2406.10997v2) | 2406.10997v2 | 11 |
| 2024-06-15 | [Breaking the Memory Wall: A Study of I/O Patterns and GPU Memory Utilization for Hybrid CPU-GPU Offloaded Optimizers](https://arxiv.org/abs/2406.10728v1) | 2406.10728v1 | 7 |
| 2024-06-15 | [The Implicit Bias of Adam on Separable Data](https://arxiv.org/abs/2406.10650v1) | 2406.10650v1 | 8 |
| 2024-06-14 | [Technical Report: A Totally Asynchronous Nesterov's Accelerated Gradient Method for Convex Optimization](https://arxiv.org/abs/2406.10124v1) | 2406.10124v1 | 6 |
| 2024-06-14 | [Memory-Efficient Optimization with Factorized Hamiltonian Descent](https://arxiv.org/abs/2406.09958v3) | 2406.09958v3 | 7 |
| 2024-06-14 | [When Will Gradient Regularization Be Harmful?](https://arxiv.org/abs/2406.09723v1) | 2406.09723v1 | 7 |
| 2024-06-11 | [ACCO: Automated Causal CNN Scheduling Optimizer for Real-Time Edge Accelerators](https://arxiv.org/abs/2406.07161v1) | 2406.07161v1 | 6 |
| 2024-06-10 | [Fed-Sophia: A Communication-Efficient Second-Order Federated Learning Algorithm](https://arxiv.org/abs/2406.06655v1) | 2406.06655v1 | 8 |
| 2024-06-07 | [Generative Explore-Exploit: Training-free Optimization of Generative Recommender Systems using LLM Optimizers](https://arxiv.org/abs/2406.05255v1) | 2406.05255v1 | 6 |
| 2024-06-07 | [From Spikes to Heavy Tails: Unveiling the Spectral Evolution of Neural Networks](https://arxiv.org/abs/2406.04657v3) | 2406.04657v3 | 7 |
| 2024-06-06 | [A second-order accurate, original energy dissipative numerical scheme for chemotaxis and its convergence analysis](https://arxiv.org/abs/2406.03761v1) | 2406.03761v1 | 7 |
| 2024-06-05 | [Second-Order Algorithms for Finding Local Nash Equilibria in Zero-Sum Games](https://arxiv.org/abs/2406.03565v3) | 2406.03565v3 | 7 |
| 2024-06-04 | [Second-order optimality conditions for the sparse optimal control of nonviscous Cahn-Hilliard systems](https://arxiv.org/abs/2406.02384v2) | 2406.02384v2 | 6 |
| 2024-06-04 | [Adaptive and Optimal Second-order Optimistic Methods for Minimax Optimization](https://arxiv.org/abs/2406.02016v2) | 2406.02016v2 | 8 |
| 2024-06-03 | [Stochastic Newton Proximal Extragradient Method](https://arxiv.org/abs/2406.01478v2) | 2406.01478v2 | 6 |
| 2024-06-03 | [ACCO: Accumulate While You Communicate for Communication-Overlapped Sharded LLM Training](https://arxiv.org/abs/2406.02613v3) | 2406.02613v3 | 6 |
| 2024-06-03 | [Port-Hamiltonian structures in infinite-dimensional optimal control: Primal-Dual gradient method and control-by-interconnection](https://arxiv.org/abs/2406.01087v2) | 2406.01087v2 | 6 |
| 2024-06-03 | [Block $ω$-circulant preconditioners for parabolic optimal control problems](https://arxiv.org/abs/2406.00952v1) | 2406.00952v1 | 7 |
| 2024-06-02 | [Graph Neural Preconditioners for Iterative Solutions of Sparse Linear Systems](https://arxiv.org/abs/2406.00809v3) | 2406.00809v3 | 6 |
| 2024-06-01 | [Optimizing Age of Information in Random Access Networks: A Second-Order Approach for Active/Passive Users](https://arxiv.org/abs/2406.00491v1) | 2406.00491v1 | 6 |
| 2024-06-01 | [A computationally efficient arc-search interior-point algorithm for nonlinear constrained optimization](https://arxiv.org/abs/2406.00436v2) | 2406.00436v2 | 9 |
| 2024-06-01 | [Greedy Learning to Optimize with Convergence Guarantees](https://arxiv.org/abs/2406.00260v10) | 2406.00260v10 | 10 |
| 2024-05-31 | [$μ$LO: Compute-Efficient Meta-Generalization of Learned Optimizers](https://arxiv.org/abs/2406.00153v5) | 2406.00153v5 | 6 |
| 2024-05-31 | [Neural-network-supported basis optimizer for the configuration interaction problem in quantum many-body clusters: Feasibility study and numerical proof](https://arxiv.org/abs/2406.00151v1) | 2406.00151v1 | 6 |
| 2024-05-31 | [Improving Generalization and Convergence by Enhancing Implicit Regularization](https://arxiv.org/abs/2405.20763v4) | 2405.20763v4 | 7 |
| 2024-05-30 | [On the randomized Euler scheme for SDEs with integral-form drift](https://arxiv.org/abs/2405.20481v2) | 2405.20481v2 | 6 |
| 2024-05-30 | [Quantitative Convergences of Lie Group Momentum Optimizers](https://arxiv.org/abs/2405.20390v1) | 2405.20390v1 | 11 |
| 2024-05-30 | [LLM as a Complementary Optimizer to Gradient Descent: A Case Study in Prompt Tuning](https://arxiv.org/abs/2405.19732v4) | 2405.19732v4 | 7 |
| 2024-05-29 | [Diagonalization-Based Parallel-in-Time Preconditioners for Instationary Fluid Flow Control Problems](https://arxiv.org/abs/2405.18964v1) | 2405.18964v1 | 6 |
| 2024-05-28 | [The Unified Balance Theory of Second-Moment Exponential Scaling Optimizers in Visual Tasks](https://arxiv.org/abs/2405.18498v1) | 2405.18498v1 | 7 |
| 2024-05-28 | [4-bit Shampoo for Memory-Efficient Network Training](https://arxiv.org/abs/2405.18144v3) | 2405.18144v3 | 18 |
| 2024-05-28 | [Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment](https://arxiv.org/abs/2405.17931v1) | 2405.17931v1 | 7 |
| 2024-05-27 | [GDSW preconditioners for composite Discontinuous Galerkin discretizations of multicompartment reaction-diffusion problems](https://arxiv.org/abs/2405.17601v1) | 2405.17601v1 | 6 |
| 2024-05-27 | [How Do the Architecture and Optimizer Affect Representation Learning? On the Training Dynamics of Representations in Deep Neural Networks](https://arxiv.org/abs/2405.17377v2) | 2405.17377v2 | 6 |
| 2024-05-26 | [Variational Quantum Framework for Partial Differential Equation Constrained Optimization](https://arxiv.org/abs/2405.16651v2) | 2405.16651v2 | 6 |
| 2024-05-26 | [Fast TRAC: A Parameter-Free Optimizer for Lifelong Reinforcement Learning](https://arxiv.org/abs/2405.16642v3) | 2405.16642v3 | 6 |
| 2024-05-26 | [The Importance of Directional Feedback for LLM-based Optimizers](https://arxiv.org/abs/2405.16434v2) | 2405.16434v2 | 6 |
| 2024-05-26 | [AdaFisher: Adaptive Second Order Optimization via Fisher Information](https://arxiv.org/abs/2405.16397v3) | 2405.16397v3 | 10 |
| 2024-05-25 | [A Second-Order Perspective on Model Compositionality and Incremental Learning](https://arxiv.org/abs/2405.16350v3) | 2405.16350v3 | 6 |
| 2024-05-25 | [Near-Optimal Distributed Minimax Optimization under the Second-Order Similarity](https://arxiv.org/abs/2405.16126v1) | 2405.16126v1 | 7 |
| 2024-05-25 | [Does SGD really happen in tiny subspaces?](https://arxiv.org/abs/2405.16002v3) | 2405.16002v3 | 9 |
| 2024-05-25 | [Exploring Jacobian Inexactness in Second-Order Methods for Variational Inequalities: Lower Bounds, Optimal Algorithms and Quasi-Newton Approximations](https://arxiv.org/abs/2405.15990v2) | 2405.15990v2 | 7 |
| 2024-05-24 | [The Road Less Scheduled](https://arxiv.org/abs/2405.15682v4) | 2405.15682v4 | 8 |
| 2024-05-24 | [Kronecker-Factored Approximate Curvature for Physics-Informed Neural Networks](https://arxiv.org/abs/2405.15603v3) | 2405.15603v3 | 9 |
| 2024-05-24 | [MicroAdam: Accurate Adaptive Optimization with Low Space Overhead and Provable Convergence](https://arxiv.org/abs/2405.15593v2) | 2405.15593v2 | 6 |
| 2024-05-24 | [Unsupervised Deep Neural Network Approach To Solve Fermionic Systems](https://arxiv.org/abs/2405.15502v1) | 2405.15502v1 | 6 |
| 2024-05-24 | [Unsupervised Deep Neural Network Approach To Solve Bosonic Systems](https://arxiv.org/abs/2405.15488v1) | 2405.15488v1 | 7 |
| 2024-05-24 | [Efficient Recurrent Off-Policy RL Requires a Context-Encoder-Specific Learning Rate](https://arxiv.org/abs/2405.15384v1) | 2405.15384v1 | 6 |
| 2024-05-24 | [Athena: Efficient Block-Wise Post-Training Quantization for Large Language Models Using Second-Order Matrix Derivative Information](https://arxiv.org/abs/2405.17470v1) | 2405.17470v1 | 6 |
| 2024-05-23 | [Scalable Optimization in the Modular Norm](https://arxiv.org/abs/2405.14813v1) | 2405.14813v1 | 7 |
| 2024-05-23 | [Spectral analysis of block preconditioners for double saddle-point linear systems with application to PDE-constrained optimization](https://arxiv.org/abs/2405.14605v2) | 2405.14605v2 | 6 |
| 2024-05-23 | [Elastic Locomotion with Mixed Second-order Differentiation](https://arxiv.org/abs/2405.14595v1) | 2405.14595v1 | 7 |
| 2024-05-23 | [Surge Phenomenon in Optimal Learning Rate and Batch Size Scaling](https://arxiv.org/abs/2405.14578v5) | 2405.14578v5 | 9 |
| 2024-05-23 | [Exact Gauss-Newton Optimization for Training Deep Neural Networks](https://arxiv.org/abs/2405.14402v2) | 2405.14402v2 | 10 |
| 2024-05-22 | [Riemannian Bilevel Optimization](https://arxiv.org/abs/2405.15816v1) | 2405.15816v1 | 6 |
| 2024-05-22 | [The Power of Extrapolation in Federated Learning](https://arxiv.org/abs/2405.13766v5) | 2405.13766v5 | 6 |
| 2024-05-21 | [FAdam: Adam is a natural gradient optimizer using diagonal empirical Fisher information](https://arxiv.org/abs/2405.12807v11) | 2405.12807v11 | 11 |
| 2024-05-19 | [Error Analysis of Three-Layer Neural Network Trained with PGD for Deep Ritz Method](https://arxiv.org/abs/2405.11451v1) | 2405.11451v1 | 6 |
| 2024-05-18 | [Adjacent Leader Decentralized Stochastic Gradient Descent](https://arxiv.org/abs/2405.11389v2) | 2405.11389v2 | 6 |
| 2024-05-17 | [To Trade Or Not To Trade: Cascading Waterfall Round Robin Rebalancing Mechanism for Cryptocurrencies](https://arxiv.org/abs/2407.12150v1) | 2407.12150v1 | 6 |
| 2024-05-16 | [Revisiting OPRO: The Limitations of Small-Scale LLMs as Optimizers](https://arxiv.org/abs/2405.10276v2) | 2405.10276v2 | 6 |
| 2024-05-16 | [LLM and Simulation as Bilevel Optimizers: A New Paradigm to Advance Physical Scientific Discovery](https://arxiv.org/abs/2405.09783v1) | 2405.09783v1 | 6 |
| 2024-05-15 | [SOMTP: Self-Supervised Learning-Based Optimizer for MPC-Based Safe Trajectory Planning Problems in Robotics](https://arxiv.org/abs/2405.09212v1) | 2405.09212v1 | 6 |
| 2024-05-09 | [Efficient numerical computation of spiral spectra with exponentially-weighted preconditioners](https://arxiv.org/abs/2405.05897v1) | 2405.05897v1 | 6 |
| 2024-05-09 | [Mirage: A Multi-Level Superoptimizer for Tensor Programs](https://arxiv.org/abs/2405.05751v3) | 2405.05751v3 | 6 |
| 2024-05-08 | [A Parallel-in-Time Multigrid Preconditioner for Optimal Control](https://arxiv.org/abs/2405.04808v2) | 2405.04808v2 | 6 |
| 2024-05-07 | [Benchmarking Optimizers for Qumode State Preparation with Variational Quantum Algorithms](https://arxiv.org/abs/2405.04499v1) | 2405.04499v1 | 6 |
| 2024-05-07 | [Towards Stability of Parameter-Free Optimization](https://arxiv.org/abs/2405.04376v4) | 2405.04376v4 | 8 |
| 2024-05-06 | [A novel fourth-order scheme for two-dimensional Riesz space fractional nonlinear reaction-diffusion equations and its optimal preconditioned solver](https://arxiv.org/abs/2405.03143v1) | 2405.03143v1 | 6 |
| 2024-05-03 | [X-SLAM: Scalable Dense SLAM for Task-aware Optimization using CSFD](https://arxiv.org/abs/2405.02187v1) | 2405.02187v1 | 6 |
| 2024-05-03 | [Muon g-2, Long-Range Muon Spin Force, and Neutrino Oscillations](https://arxiv.org/abs/2405.02084v2) | 2405.02084v2 | 6 |
| 2024-05-01 | [Adjoint-based goal-oriented implicit shock tracking using full space mesh optimization](https://arxiv.org/abs/2405.00904v1) | 2405.00904v1 | 8 |
| 2024-04-30 | [Q-Newton: Hybrid Quantum-Classical Scheduling for Accelerating Neural Network Training with Newton's Gradient Descent](https://arxiv.org/abs/2405.00252v3) | 2405.00252v3 | 10 |
| 2024-04-30 | [Scheduling Weight Transitions for Quantization-Aware Training](https://arxiv.org/abs/2404.19248v4) | 2404.19248v4 | 7 |
| 2024-04-29 | [Random Reshuffling with Momentum: Complexity Bounds and Last-iterate Convergence](https://arxiv.org/abs/2404.18452v3) | 2404.18452v3 | 8 |
| 2024-04-28 | [SOUL: Unlocking the Power of Second-Order Optimization for LLM Unlearning](https://arxiv.org/abs/2404.18239v4) | 2404.18239v4 | 10 |
| 2024-04-27 | [Swarm-based gradient descent meets simulated annealing](https://arxiv.org/abs/2404.18015v2) | 2404.18015v2 | 6 |
| 2024-04-26 | [New second-order optimality conditions for directional optimality of a general set-constrained optimization problem](https://arxiv.org/abs/2404.17696v2) | 2404.17696v2 | 6 |
| 2024-04-26 | [Hard ASH: Sparsity and the right optimizer make a continual learner](https://arxiv.org/abs/2404.17651v1) | 2404.17651v1 | 8 |
| 2024-04-25 | [Water Cherenkov muon veto for the COSINUS experiment: design and simulation optimization](https://arxiv.org/abs/2406.12870v1) | 2406.12870v1 | 6 |
| 2024-04-23 | [Second-order Information Promotes Mini-Batch Robustness in Variance-Reduced Gradients](https://arxiv.org/abs/2404.14758v1) | 2404.14758v1 | 8 |
| 2024-04-22 | [Solving Combinatorial Optimization Problems with a Block Encoding Quantum Optimizer](https://arxiv.org/abs/2404.14054v3) | 2404.14054v3 | 6 |
| 2024-04-22 | [Data-Driven Performance Guarantees for Classical and Learned Optimizers](https://arxiv.org/abs/2404.13831v3) | 2404.13831v3 | 8 |
| 2024-04-21 | [How to Inverting the Leverage Score Distribution?](https://arxiv.org/abs/2404.13785v1) | 2404.13785v1 | 6 |
| 2024-04-19 | [SOPHON: Non-Fine-Tunable Learning to Restrain Task Transferability For Pre-trained Models](https://arxiv.org/abs/2404.12699v1) | 2404.12699v1 | 6 |
| 2024-04-17 | [Prompt Optimizer of Text-to-Image Diffusion Models for Abstract Concept Understanding](https://arxiv.org/abs/2404.11589v1) | 2404.11589v1 | 6 |
| 2024-04-17 | [A $τ$-preconditioner for space fractional diffusion equation with non-separable variable coefficients](https://arxiv.org/abs/2404.11390v1) | 2404.11390v1 | 7 |
| 2024-04-16 | [A preconditioner for solving linear programming problems with dense columns](https://arxiv.org/abs/2404.10930v1) | 2404.10930v1 | 6 |
| 2024-04-16 | [Decoupled Weight Decay for Any $p$ Norm](https://arxiv.org/abs/2404.10824v2) | 2404.10824v2 | 8 |
| 2024-04-16 | [Classification of Prostate Cancer in 3D Magnetic Resonance Imaging Data based on Convolutional Neural Networks](https://arxiv.org/abs/2404.10548v1) | 2404.10548v1 | 6 |
| 2024-04-15 | [Monitoring Second-Order Hyperproperties](https://arxiv.org/abs/2404.09652v1) | 2404.09652v1 | 6 |
| 2024-04-12 | [Riemannian optimization on the symplectic Stiefel manifold using second-order information](https://arxiv.org/abs/2404.08463v2) | 2404.08463v2 | 7 |
| 2024-04-10 | [Neural Optimizer Equation, Decay Function, and Learning Rate Schedule Joint Evolution](https://arxiv.org/abs/2404.06679v1) | 2404.06679v1 | 9 |
| 2024-04-09 | [An Enhanced Grey Wolf Optimizer with Elite Inheritance and Balance Search Mechanisms](https://arxiv.org/abs/2404.06524v1) | 2404.06524v1 | 7 |
| 2024-04-05 | [Adaptive Power Flow Approximations with Second-Order Sensitivity Insights](https://arxiv.org/abs/2404.04391v2) | 2404.04391v2 | 6 |
| 2024-04-04 | [A semi-implicit second-order temporal scheme for solving the pressure head-based form of Richards' and advection-dispersion equations](https://arxiv.org/abs/2404.03603v3) | 2404.03603v3 | 6 |
| 2024-04-02 | [LP++: A Surprisingly Strong Linear Probe for Few-Shot CLIP](https://arxiv.org/abs/2404.02285v1) | 2404.02285v1 | 7 |
| 2024-04-02 | [Conjugate-Gradient-like Based Adaptive Moment Estimation Optimization Algorithm for Deep Learning](https://arxiv.org/abs/2404.01714v4) | 2404.01714v4 | 6 |
| 2024-04-01 | [Convergence Guarantees for RMSProp and Adam in Generalized-smooth Non-convex Optimization with Affine Noise Variance](https://arxiv.org/abs/2404.01436v3) | 2404.01436v3 | 6 |
| 2024-03-30 | [Communication Efficient Distributed Training with Distributed Lion](https://arxiv.org/abs/2404.00438v1) | 2404.00438v1 | 6 |
| 2024-03-29 | [Fully Zeroth-Order Bilevel Programming via Gaussian Smoothing](https://arxiv.org/abs/2404.00158v1) | 2404.00158v1 | 6 |
| 2024-03-29 | [Monotone inclusion methods for a class of second-order non-potential mean-field games](https://arxiv.org/abs/2403.20290v1) | 2403.20290v1 | 7 |
| 2024-03-28 | [Quantum Realization of the Finite Element Method](https://arxiv.org/abs/2403.19512v4) | 2403.19512v4 | 8 |
| 2024-03-27 | [Improving Line Search Methods for Large Scale Neural Network Training](https://arxiv.org/abs/2403.18519v1) | 2403.18519v1 | 9 |
| 2024-03-27 | [Faster Convergence for Transformer Fine-tuning with Line Search Methods](https://arxiv.org/abs/2403.18506v1) | 2403.18506v1 | 6 |
| 2024-03-27 | [Learning in PINNs: Phase transition, diffusion equilibrium, and generalization](https://arxiv.org/abs/2403.18494v2) | 2403.18494v2 | 6 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-31 | [Effect of Optimizer, Initializer, and Architecture of Hypernetworks on Continual Learning from Demonstration](https://arxiv.org/abs/2401.00524v1) | 2401.00524v1 | 8 |
| 2023-12-31 | [Multiplayer Battle Game-Inspired Optimizer for Complex Optimization Problems](https://arxiv.org/abs/2401.00401v1) | 2401.00401v1 | 7 |
| 2023-12-30 | [Optimization of muonium yield in perforated silica aerogel](https://arxiv.org/abs/2401.00222v1) | 2401.00222v1 | 6 |
| 2023-12-28 | [Beyond PID Controllers: PPO with Neuralized PID Policy for Proton Beam Intensity Control in Mu2e](https://arxiv.org/abs/2312.17372v1) | 2312.17372v1 | 6 |
| 2023-12-27 | [Dual-stage optimizer for systematic overestimation adjustment applied to multi-objective genetic algorithms for biomarker selection](https://arxiv.org/abs/2312.16624v3) | 2312.16624v3 | 6 |
| 2023-12-26 | [Second-Order Subdifferential Optimality Conditions in Nonsmooth Optimization](https://arxiv.org/abs/2312.16277v2) | 2312.16277v2 | 6 |
| 2023-12-25 | [SantaQlaus: A resource-efficient method to leverage quantum shot-noise for optimization of variational quantum algorithms](https://arxiv.org/abs/2312.15791v1) | 2312.15791v1 | 6 |
| 2023-12-25 | [An Inexact Projected Regularized Newton Method for Fused Zero-norms Regularization Problems](https://arxiv.org/abs/2312.15718v1) | 2312.15718v1 | 6 |
| 2023-12-24 | [Perception-Distortion Balanced Super-Resolution: A Multi-Objective Optimization Perspective](https://arxiv.org/abs/2312.15408v2) | 2312.15408v2 | 6 |
| 2023-12-23 | [AdamL: A fast adaptive gradient method incorporating loss function](https://arxiv.org/abs/2312.15295v1) | 2312.15295v1 | 8 |
| 2023-12-23 | [ZO-AdaMU Optimizer: Adapting Perturbation by the Momentum and Uncertainty in Zeroth-order Optimization](https://arxiv.org/abs/2312.15184v1) | 2312.15184v1 | 11 |
| 2023-12-22 | [Probing flavor constrained SMEFT operators through $tc$ production at the Muon collider](https://arxiv.org/abs/2312.14872v2) | 2312.14872v2 | 6 |
| 2023-12-22 | [Accelerated Convergence of Stochastic Heavy Ball Method under Anisotropic Gradient Noise](https://arxiv.org/abs/2312.14567v2) | 2312.14567v2 | 6 |
| 2023-12-19 | [Transformed Primal-Dual Methods with Variable-Preconditioners](https://arxiv.org/abs/2312.12355v1) | 2312.12355v1 | 7 |
| 2023-12-19 | [On the Parameterization of Second-Order Optimization Effective Towards the Infinite Width](https://arxiv.org/abs/2312.12226v2) | 2312.12226v2 | 13 |
| 2023-12-17 | [Facial Emotion Recognition using CNN in PyTorch](https://arxiv.org/abs/2312.10818v1) | 2312.10818v1 | 6 |
| 2023-12-17 | [Automatic Optimisation of Normalised Neural Networks](https://arxiv.org/abs/2312.10672v1) | 2312.10672v1 | 7 |
| 2023-12-15 | [Resilient Federated Learning under Byzantine Attack in Distributed Nonconvex Optimization with 2-f Redundancy](https://arxiv.org/abs/2312.10189v1) | 2312.10189v1 | 6 |
| 2023-12-12 | [Sentiment analysis in Tourism: Fine-tuning BERT or sentence embeddings concatenation?](https://arxiv.org/abs/2312.07797v1) | 2312.07797v1 | 6 |
| 2023-12-12 | [Investigation into the Training Dynamics of Learned Optimizers](https://arxiv.org/abs/2312.07174v1) | 2312.07174v1 | 6 |
| 2023-12-11 | [Accelerated Gradient Dynamics on Riemannian Manifolds: Faster Rate and Trajectory Convergence](https://arxiv.org/abs/2312.06366v1) | 2312.06366v1 | 6 |
| 2023-12-11 | [FOSS: A Self-Learned Doctor for Query Optimizer](https://arxiv.org/abs/2312.06357v2) | 2312.06357v2 | 6 |
| 2023-12-07 | [Unnatural Algorithms in Machine Learning](https://arxiv.org/abs/2312.04739v1) | 2312.04739v1 | 7 |
| 2023-12-07 | [Entanglement generation via single-qubit rotations in a torn Hilbert space](https://arxiv.org/abs/2312.04507v2) | 2312.04507v2 | 6 |
| 2023-12-06 | [Understanding the Role of Optimization in Double Descent](https://arxiv.org/abs/2312.03951v1) | 2312.03951v1 | 8 |
| 2023-12-06 | [Gathering and Exploiting Higher-Order Information when Training Large Structured Models](https://arxiv.org/abs/2312.03885v4) | 2312.03885v4 | 7 |
| 2023-12-06 | [Achieving ${O}(ε^{-1.5})$ Complexity in Hessian/Jacobian-free Stochastic Bilevel Optimization](https://arxiv.org/abs/2312.03807v3) | 2312.03807v3 | 11 |
| 2023-12-05 | [Efficient Enumeration of Recursive Plans in Transformation-based Query Optimizers](https://arxiv.org/abs/2312.02572v3) | 2312.02572v3 | 6 |
| 2023-12-04 | [AGD: an Auto-switchable Optimizer using Stepwise Gradient Difference for Preconditioning Matrix](https://arxiv.org/abs/2312.01658v2) | 2312.01658v2 | 7 |
| 2023-12-02 | [Meta-learning Optimizers for Communication-Efficient Learning](https://arxiv.org/abs/2312.02204v2) | 2312.02204v2 | 7 |
| 2023-12-01 | [Temperature Balancing, Layer-wise Weight Analysis, and Neural Network Training](https://arxiv.org/abs/2312.00359v1) | 2312.00359v1 | 6 |
| 2023-12-01 | [PipeOptim: Ensuring Effective 1F1B Schedule with Optimizer-Dependent Weight Prediction](https://arxiv.org/abs/2312.00839v3) | 2312.00839v3 | 6 |
| 2023-11-29 | [Analyzing Query Optimizer Performance in the Presence and Absence of Cardinality Estimates](https://arxiv.org/abs/2311.17293v1) | 2311.17293v1 | 6 |
| 2023-11-28 | [Adaptive Step Sizes for Preconditioned Stochastic Gradient Descent](https://arxiv.org/abs/2311.16956v2) | 2311.16956v2 | 6 |
| 2023-11-27 | [Efficient high-resolution refinement in cryo-EM with stochastic gradient descent](https://arxiv.org/abs/2311.16100v3) | 2311.16100v3 | 6 |
| 2023-11-27 | [Application of Long-short Term Memory (LSTM) Model for Forecasting NOx Emission in Pohang Area](https://arxiv.org/abs/2311.15632v1) | 2311.15632v1 | 6 |
| 2023-11-26 | [Optimize the event selection strategy to study the anomalous quartic gauge couplings at muon colliders using the support vector machine and quantum support vector machine](https://arxiv.org/abs/2311.15280v3) | 2311.15280v3 | 6 |
| 2023-11-25 | [Gradient Descent with Polyak's Momentum Finds Flatter Minima via Large Catapults](https://arxiv.org/abs/2311.15051v3) | 2311.15051v3 | 6 |
| 2023-11-24 | [Second-order conditions for spatio-temporally sparse optimal control via second subderivatives](https://arxiv.org/abs/2311.14538v3) | 2311.14538v3 | 6 |
| 2023-11-23 | [Robust Decision Aggregation with Second-order Information](https://arxiv.org/abs/2311.14094v1) | 2311.14094v1 | 6 |
| 2023-11-20 | [Fine-Tuning Adaptive Stochastic Optimizers: Determining the Optimal Hyperparameter $ε$ via Gradient Magnitude Histogram Analysis](https://arxiv.org/abs/2311.11532v2) | 2311.11532v2 | 7 |
| 2023-11-18 | [Polynomial-Time Solutions for ReLU Network Training: A Complexity Classification via Max-Cut and Zonotopes](https://arxiv.org/abs/2311.10972v1) | 2311.10972v1 | 6 |
| 2023-11-16 | [Adaptive Optimization Algorithms for Machine Learning](https://arxiv.org/abs/2311.10203v1) | 2311.10203v1 | 9 |
| 2023-11-16 | [A Computationally Efficient Sparsified Online Newton Method](https://arxiv.org/abs/2311.10085v1) | 2311.10085v1 | 17 |
| 2023-11-15 | [A high-order local discontinuous Galerkin method for the $p$-Laplace equation](https://arxiv.org/abs/2311.09119v1) | 2311.09119v1 | 6 |
| 2023-11-15 | [Taming under isoperimetry](https://arxiv.org/abs/2311.09003v1) | 2311.09003v1 | 6 |
| 2023-11-15 | [StrategyLLM: Large Language Models as Strategy Generators, Executors, Optimizers, and Evaluators for Problem Solving](https://arxiv.org/abs/2311.08803v4) | 2311.08803v4 | 6 |
| 2023-11-14 | [DiLoCo: Distributed Low-Communication Training of Language Models](https://arxiv.org/abs/2311.08105v3) | 2311.08105v3 | 7 |
| 2023-11-10 | [Federated Learning with Manifold Regularization and Normalized Update Reaggregation](https://arxiv.org/abs/2311.05924v1) | 2311.05924v1 | 6 |
| 2023-11-08 | [Hubbard model on Semiclassical approximation in combination with an optimizer based on GPU technology](https://arxiv.org/abs/2311.04435v1) | 2311.04435v1 | 6 |
| 2023-11-06 | [Signal Processing Meets SGD: From Momentum to Filter](https://arxiv.org/abs/2311.02818v7) | 2311.02818v7 | 9 |
| 2023-11-04 | [NeuroEvoBench: Benchmarking Evolutionary Optimizers for Deep Learning Applications](https://arxiv.org/abs/2311.02394v1) | 2311.02394v1 | 7 |
| 2023-11-03 | [When linear inversion fails: neural-network optimization for sparse-ray travel-time tomography of a volcanic edifice](https://arxiv.org/abs/2311.01794v1) | 2311.01794v1 | 8 |
| 2023-11-03 | [Second-Order Convergent Collision-Constrained Optimization-Based Planner](https://arxiv.org/abs/2311.01717v1) | 2311.01717v1 | 7 |
| 2023-11-01 | [Training Dynamics of Contextual N-Grams in Language Models](https://arxiv.org/abs/2311.00863v1) | 2311.00863v1 | 6 |
| 2023-10-31 | [Information-Theoretic Trust Regions for Stochastic Gradient-Based Optimization](https://arxiv.org/abs/2310.20574v1) | 2310.20574v1 | 10 |
| 2023-10-30 | [AdaSub: Stochastic Optimization Using Second-Order Information in Low-Dimensional Subspaces](https://arxiv.org/abs/2310.20060v2) | 2310.20060v2 | 11 |
| 2023-10-30 | [The Anytime Convergence of Stochastic Gradient Descent with Momentum: From a Continuous-Time Perspective](https://arxiv.org/abs/2310.19598v7) | 2310.19598v7 | 9 |
| 2023-10-29 | [Large Language Models as Evolutionary Optimizers](https://arxiv.org/abs/2310.19046v3) | 2310.19046v3 | 6 |
| 2023-10-28 | [A randomized algorithm for nonconvex minimization with inexact evaluations and complexity guarantees](https://arxiv.org/abs/2310.18841v2) | 2310.18841v2 | 6 |
| 2023-10-27 | [Structured Semidefinite Programming for Recovering Structured Preconditioners](https://arxiv.org/abs/2310.18265v1) | 2310.18265v1 | 6 |
| 2023-10-27 | [Is Scaling Learned Optimizers Worth It? Evaluating The Value of VeLO's 4000 TPU Months](https://arxiv.org/abs/2310.18191v2) | 2310.18191v2 | 6 |
| 2023-10-27 | [Closing the Gap Between the Upper Bound and the Lower Bound of Adam's Iteration Complexity](https://arxiv.org/abs/2310.17998v1) | 2310.17998v1 | 10 |
| 2023-10-27 | [Parameter estimation for second-order SPDEs in multiple space dimensions](https://arxiv.org/abs/2310.17828v2) | 2310.17828v2 | 7 |
| 2023-10-26 | [Trust Region Methods For Nonconvex Stochastic Optimization Beyond Lipschitz Smoothness](https://arxiv.org/abs/2310.17319v2) | 2310.17319v2 | 6 |
| 2023-10-26 | [Generating a 4-photon Tetrahedron State: Towards Simultaneous Super-sensitivity to Non-commuting Rotations](https://arxiv.org/abs/2310.17150v1) | 2310.17150v1 | 6 |
| 2023-10-26 | [Transformers Learn to Achieve Second-Order Convergence Rates for In-Context Linear Regression](https://arxiv.org/abs/2310.17086v3) | 2310.17086v3 | 8 |
| 2023-10-25 | [Stochastic Gradient Sampling for Enhancing Neural Networks Training](https://arxiv.org/abs/2310.17042v4) | 2310.17042v4 | 8 |
| 2023-10-23 | [Studying K-FAC Heuristics by Viewing Adam through a Second-Order Lens](https://arxiv.org/abs/2310.14963v3) | 2310.14963v3 | 9 |
| 2023-10-21 | [Application of deep and reinforcement learning to boundary control problems](https://arxiv.org/abs/2310.15191v1) | 2310.15191v1 | 8 |
| 2023-10-20 | [Stable Nonconvex-Nonconcave Training via Linear Interpolation](https://arxiv.org/abs/2310.13459v4) | 2310.13459v4 | 6 |
| 2023-10-18 | [Jorge: Approximate Preconditioning for GPU-efficient Second-order Optimization](https://arxiv.org/abs/2310.12298v2) | 2310.12298v2 | 19 |
| 2023-10-18 | [Stochastic Optimization for Non-convex Problem with Inexact Hessian Matrix, Gradient, and Function](https://arxiv.org/abs/2310.11866v1) | 2310.11866v1 | 6 |
| 2023-10-18 | [A fast normal splitting preconditioner for attractive coupled nonlinear Schrödinger equations with fractional Laplacian](https://arxiv.org/abs/2310.11740v1) | 2310.11740v1 | 7 |
| 2023-10-17 | [A variational data assimilation approach for sparse velocity reference data in coarse RANS simulations through a corrective forcing term](https://arxiv.org/abs/2310.11543v2) | 2310.11543v2 | 7 |
| 2023-10-16 | [AdaLomo: Low-memory Optimization with Adaptive Learning Rate](https://arxiv.org/abs/2310.10195v3) | 2310.10195v3 | 15 |
| 2023-10-14 | [Randomized Benchmarking of Local Zeroth-Order Optimizers for Variational Quantum Systems](https://arxiv.org/abs/2310.09468v1) | 2310.09468v1 | 6 |
| 2023-10-13 | [Adam-family Methods with Decoupled Weight Decay in Deep Learning](https://arxiv.org/abs/2310.08858v1) | 2310.08858v1 | 9 |
| 2023-10-12 | [GeNIOS: an (almost) second-order operator-splitting solver for large-scale convex optimization](https://arxiv.org/abs/2310.08333v2) | 2310.08333v2 | 11 |
| 2023-10-12 | [Convergence of Arbitrary Lagrangian-Eulerian Second-order Projection Method for the Stokes Equations on an Evolving Domain](https://arxiv.org/abs/2310.08218v1) | 2310.08218v1 | 7 |
| 2023-10-11 | [Experimental quantum natural gradient optimization in photonics](https://arxiv.org/abs/2310.07371v1) | 2310.07371v1 | 6 |
| 2023-10-10 | [Quantum Shadow Gradient Descent for Variational Quantum Algorithms](https://arxiv.org/abs/2310.06935v2) | 2310.06935v2 | 6 |
| 2023-10-10 | [Reinforcement Learning in a Safety-Embedded MDP with Trajectory Optimization](https://arxiv.org/abs/2310.06903v2) | 2310.06903v2 | 6 |
| 2023-10-09 | [Provably Accelerating Ill-Conditioned Low-rank Estimation via Scaled Gradient Descent, Even with Overparameterization](https://arxiv.org/abs/2310.06159v1) | 2310.06159v1 | 6 |
| 2023-10-09 | [Lion Secretly Solves Constrained Optimization: As Lyapunov Predicts](https://arxiv.org/abs/2310.05898v7) | 2310.05898v7 | 9 |
| 2023-10-09 | [Making Scalable Meta Learning Practical](https://arxiv.org/abs/2310.05674v2) | 2310.05674v2 | 9 |
| 2023-10-09 | [Distributed Evolution Strategies with Multi-Level Learning for Large-Scale Black-Box Optimization](https://arxiv.org/abs/2310.05377v4) | 2310.05377v4 | 8 |
| 2023-10-08 | [Asymmetrically Decentralized Federated Learning](https://arxiv.org/abs/2310.05093v1) | 2310.05093v1 | 8 |
| 2023-10-07 | [Combining UPerNet and ConvNeXt for Contrails Identification to reduce Global Warming](https://arxiv.org/abs/2310.04808v1) | 2310.04808v1 | 6 |
| 2023-10-06 | [Profit: Benchmarking Personalization and Robustness Trade-off in Federated Prompt Tuning](https://arxiv.org/abs/2310.04627v1) | 2310.04627v1 | 6 |
| 2023-10-05 | [Design Optimizer for Planar Soft-Growing Robot Manipulators](https://arxiv.org/abs/2310.03374v2) | 2310.03374v2 | 6 |
| 2023-10-04 | [ProGO: Probabilistic Global Optimizer](https://arxiv.org/abs/2310.04457v2) | 2310.04457v2 | 8 |
| 2023-10-03 | [Computing a Sparse Approximate Inverse on Quantum Annealing Machines](https://arxiv.org/abs/2310.02388v1) | 2310.02388v1 | 6 |
| 2023-10-03 | [Stochastic Gradient Descent with Preconditioned Polyak Step-size](https://arxiv.org/abs/2310.02093v1) | 2310.02093v1 | 7 |
| 2023-10-03 | [A second-order sequential optimality condition for nonlinear second-order cone programming problems](https://arxiv.org/abs/2310.01971v2) | 2310.01971v2 | 7 |
| 2023-10-02 | [Nature Inspired Evolutionary Swarm Optimizers for Biomedical Image and Signal Processing -- A Systematic Review](https://arxiv.org/abs/2311.12830v1) | 2311.12830v1 | 7 |
| 2023-09-29 | [Enabling Differentially Private Federated Learning for Speech Recognition: Benchmarks, Adaptive Optimizers and Gradient Clipping](https://arxiv.org/abs/2310.00098v4) | 2310.00098v4 | 7 |
| 2023-09-25 | [Small-scale proxies for large-scale Transformer training instabilities](https://arxiv.org/abs/2309.14322v2) | 2309.14322v2 | 11 |
| 2023-09-25 | [Fuzzy Hunter Optimizer: An Bio-Metaheuristic Algorithm Inspired by Lévy Walks](https://arxiv.org/abs/2309.13829v1) | 2309.13829v1 | 6 |
| 2023-09-24 | [Accelerating Large Batch Training via Gradient Signal to Noise Ratio (GSNR)](https://arxiv.org/abs/2309.13681v1) | 2309.13681v1 | 6 |
| 2023-09-24 | [Graph-enhanced Optimizers for Structure-aware Recommendation Embedding Evolution](https://arxiv.org/abs/2310.03032v3) | 2310.03032v3 | 7 |
| 2023-09-22 | [Importance of Smoothness Induced by Optimizers in FL4ASR: Towards Understanding Federated Learning for End-to-End ASR](https://arxiv.org/abs/2309.13102v1) | 2309.13102v1 | 8 |
| 2023-09-21 | [Memory Efficient Mixed-Precision Optimizers](https://arxiv.org/abs/2309.12381v1) | 2309.12381v1 | 7 |
| 2023-09-19 | [The Parameterized Complexity of Learning Monadic Second-Order Logic](https://arxiv.org/abs/2309.10489v3) | 2309.10489v3 | 6 |
| 2023-09-18 | [Quantum Circuit Optimization through Iteratively Pre-Conditioned Gradient Descent](https://arxiv.org/abs/2309.09957v1) | 2309.09957v1 | 6 |
| 2023-09-15 | [EvoPrompt: Connecting LLMs with Evolutionary Algorithms Yields Powerful Prompt Optimizers](https://arxiv.org/abs/2309.08532v3) | 2309.08532v3 | 8 |
| 2023-09-14 | [A Multi-In and Multi-Out Dendritic Neuron Model and its Optimization](https://arxiv.org/abs/2309.07791v1) | 2309.07791v1 | 6 |
| 2023-09-12 | [A Distributed Data-Parallel PyTorch Implementation of the Distributed Shampoo Optimizer for Training Neural Networks At-Scale](https://arxiv.org/abs/2309.06497v1) | 2309.06497v1 | 17 |
| 2023-09-12 | [ELRA: Exponential learning rate adaption gradient descent optimization method](https://arxiv.org/abs/2309.06274v1) | 2309.06274v1 | 9 |
| 2023-09-12 | [Language Models as Black-Box Optimizers for Vision-Language Models](https://arxiv.org/abs/2309.05950v5) | 2309.05950v5 | 7 |
| 2023-09-12 | [Tumoral Angiogenic Optimizer: A new bio-inspired based metaheuristic](https://arxiv.org/abs/2309.05947v3) | 2309.05947v3 | 6 |
| 2023-09-11 | [A distributionally robust index tracking model with the CVaR penalty: tractable reformulation](https://arxiv.org/abs/2309.05597v1) | 2309.05597v1 | 6 |
| 2023-09-11 | [Simba: A Scalable Bilevel Preconditioned Gradient Method for Fast Evasion of Flat Areas and Saddle Points](https://arxiv.org/abs/2309.05309v1) | 2309.05309v1 | 6 |
| 2023-09-10 | [Riemannian Acceleration with Preconditioning for symmetric eigenvalue problems](https://arxiv.org/abs/2309.05143v2) | 2309.05143v2 | 6 |

### 2022
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2022-12-31 | [Genetic-tunneling driven energy optimizer for spin systems](https://arxiv.org/abs/2301.00207v2) | 2301.00207v2 | 6 |
| 2022-12-23 | [Exploring the Optimized Value of Each Hyperparameter in Various Gradient Descent Algorithms](https://arxiv.org/abs/2212.12279v2) | 2212.12279v2 | 6 |
| 2022-12-22 | [Random block coordinate methods for inconsistent convex optimisation problems](https://arxiv.org/abs/2212.12045v3) | 2212.12045v3 | 6 |
| 2022-12-21 | [Second-order optimality conditions for the bilinear optimal control of a degenerate equation](https://arxiv.org/abs/2212.11046v2) | 2212.11046v2 | 6 |
| 2022-12-20 | [Why Can GPT Learn In-Context? Language Models Implicitly Perform Gradient Descent as Meta-Optimizers](https://arxiv.org/abs/2212.10559v3) | 2212.10559v3 | 9 |
| 2022-12-20 | [Input Normalized Stochastic Gradient Descent Training of Deep Neural Networks](https://arxiv.org/abs/2212.09921v2) | 2212.09921v2 | 7 |
| 2022-12-19 | [Trial-Based Dominance Enables Non-Parametric Tests to Compare both the Speed and Accuracy of Stochastic Optimizers](https://arxiv.org/abs/2212.09423v1) | 2212.09423v1 | 6 |
| 2022-12-17 | [Improving Levenberg-Marquardt Algorithm for Neural Networks](https://arxiv.org/abs/2212.08769v1) | 2212.08769v1 | 8 |
| 2022-12-14 | [RAGO: Recurrent Graph Optimizer For Multiple Rotation Averaging](https://arxiv.org/abs/2212.07211v1) | 2212.07211v1 | 6 |
| 2022-12-14 | [RLEKF: An Optimizer for Deep Potential with Ab Initio Accuracy](https://arxiv.org/abs/2212.06989v1) | 2212.06989v1 | 7 |
| 2022-12-12 | [Generalizing DP-SGD with Shuffling and Batch Clipping](https://arxiv.org/abs/2212.05796v3) | 2212.05796v3 | 7 |
| 2022-12-06 | [DiffTune$^+$: Hyperparameter-Free Auto-Tuning using Auto-Differentiation](https://arxiv.org/abs/2212.03194v2) | 2212.03194v2 | 7 |
| 2022-12-06 | [How does the partition of unity influence SORAS preconditioner?](https://arxiv.org/abs/2212.03132v2) | 2212.03132v2 | 8 |
| 2022-12-06 | [Monitoring Spent Nuclear Fuel in a Dry Cask Using Momentum Integrated Muon Scattering Tomography](https://arxiv.org/abs/2212.04947v1) | 2212.04947v1 | 9 |
| 2022-12-02 | [Investigating certain choices of CNN configurations for brain lesion segmentation](https://arxiv.org/abs/2212.01235v1) | 2212.01235v1 | 8 |
| 2022-12-01 | [Second-order optimization with lazy Hessians](https://arxiv.org/abs/2212.00781v3) | 2212.00781v3 | 8 |
| 2022-12-01 | [Adaptive FEM with quasi-optimal overall cost for nonsymmetric linear elliptic PDEs](https://arxiv.org/abs/2212.00353v6) | 2212.00353v6 | 6 |
| 2022-12-01 | [Differentially Private Adaptive Optimization with Delayed Preconditioners](https://arxiv.org/abs/2212.00309v2) | 2212.00309v2 | 12 |
| 2022-11-30 | [New Searches for Muonphilic Particles at Proton Beam Dump Spectrometers](https://arxiv.org/abs/2212.00033v2) | 2212.00033v2 | 6 |
| 2022-11-30 | [Swarm-Based Gradient Descent Method for Non-Convex Optimization](https://arxiv.org/abs/2211.17157v2) | 2211.17157v2 | 6 |
| 2022-11-28 | [A survey of deep learning optimizers -- first and second order methods](https://arxiv.org/abs/2211.15596v2) | 2211.15596v2 | 6 |
| 2022-11-26 | [A Particle-based Sparse Gaussian Process Optimizer](https://arxiv.org/abs/2211.14517v1) | 2211.14517v1 | 7 |
| 2022-11-25 | [Analysis of Error Feedback in Federated Non-Convex Optimization with Biased Compression](https://arxiv.org/abs/2211.14292v1) | 2211.14292v1 | 6 |
| 2022-11-25 | [PipeFisher: Efficient Training of Large Language Models Using Pipelining and Fisher Information Matrices](https://arxiv.org/abs/2211.14133v2) | 2211.14133v2 | 9 |
| 2022-11-22 | [Direct Collocation for Numerical Optimal Control of Second-Order ODE](https://arxiv.org/abs/2211.12308v2) | 2211.12308v2 | 6 |
| 2022-11-21 | [Efficient Second-Order Plane Adjustment](https://arxiv.org/abs/2211.11542v1) | 2211.11542v1 | 8 |
| 2022-11-19 | [A Stochastic Second-Order Proximal Method for Distributed Optimization](https://arxiv.org/abs/2211.10591v1) | 2211.10591v1 | 8 |
| 2022-11-17 | [VeLO: Training Versatile Learned Optimizers by Scaling Up](https://arxiv.org/abs/2211.09760v1) | 2211.09760v1 | 7 |
| 2022-11-17 | [Synthesizing Quantum-Circuit Optimizers](https://arxiv.org/abs/2211.09691v3) | 2211.09691v3 | 6 |
| 2022-11-17 | [How to Fine-Tune Vision Models with SGD](https://arxiv.org/abs/2211.09359v2) | 2211.09359v2 | 7 |
| 2022-11-16 | [Beam-Based Diagnostics of Electric Guide Fields and Lattice Parameters for Run-1 of the Muon g-2 Storage Ring at Fermilab](https://arxiv.org/abs/2211.08951v1) | 2211.08951v1 | 6 |
| 2022-11-16 | [Differentially Private Optimizers Can Learn Adversarially Robust Models](https://arxiv.org/abs/2211.08942v2) | 2211.08942v2 | 6 |
| 2022-11-15 | [Empirical Study on Optimizer Selection for Out-of-Distribution Generalization](https://arxiv.org/abs/2211.08583v3) | 2211.08583v3 | 8 |
| 2022-11-15 | [Diffusion of muonic hydrogen in hydrogen gas and the measurement of the 1$s$ hyperfine splitting of muonic hydrogen](https://arxiv.org/abs/2211.08297v3) | 2211.08297v3 | 6 |
| 2022-11-14 | [Comment on $μp$ and $μA$ Luminosities of Muon-Ion Collider at BNL](https://arxiv.org/abs/2211.07513v1) | 2211.07513v1 | 10 |
| 2022-11-14 | [Adaptive Federated Minimax Optimization with Lower Complexities](https://arxiv.org/abs/2211.07303v4) | 2211.07303v4 | 6 |
| 2022-11-14 | [Automatic penalty and degree continuation for parallel pre-conditioned mesh curving on virtual geometry](https://arxiv.org/abs/2211.08426v1) | 2211.08426v1 | 8 |
| 2022-11-11 | [A convergence study of SGD-type methods for stochastic optimization](https://arxiv.org/abs/2211.06197v2) | 2211.06197v2 | 6 |
| 2022-11-11 | [Efficient Domain Coverage for Vehicles with Second-Order Dynamics via Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2211.05952v4) | 2211.05952v4 | 6 |
| 2022-11-09 | [Resource frugal optimizer for quantum machine learning](https://arxiv.org/abs/2211.04965v3) | 2211.04965v3 | 7 |
| 2022-11-09 | [A nonsmooth primal-dual method with interwoven PDE constraint solver](https://arxiv.org/abs/2211.04807v3) | 2211.04807v3 | 6 |
| 2022-11-08 | [Black Box Lie Group Preconditioners for SGD](https://arxiv.org/abs/2211.04422v1) | 2211.04422v1 | 18 |
| 2022-11-07 | [Analytical formulation of the second-order derivative of energy for orbital-optimized variational quantum eigensolver: application to polarizability](https://arxiv.org/abs/2211.03343v2) | 2211.03343v2 | 6 |
| 2022-11-04 | [How Does Adaptive Optimization Impact Local Neural Network Geometry?](https://arxiv.org/abs/2211.02254v1) | 2211.02254v1 | 6 |
| 2022-11-03 | [Extra-Newton: A First Approach to Noise-Adaptive Accelerated Second-Order Methods](https://arxiv.org/abs/2211.01832v2) | 2211.01832v2 | 7 |
| 2022-11-02 | [Faster variational quantum algorithms with quantum kernel-based surrogate models](https://arxiv.org/abs/2211.01134v2) | 2211.01134v2 | 6 |
| 2022-11-02 | [Fast Adaptive Federated Bilevel Optimization](https://arxiv.org/abs/2211.01122v3) | 2211.01122v3 | 6 |
| 2022-10-29 | [Recursive Reasoning in Minimax Games: A Level $k$ Gradient Play Method](https://arxiv.org/abs/2210.16482v1) | 2210.16482v1 | 6 |
| 2022-10-28 | [Flatter, faster: scaling momentum for optimal speedup of SGD](https://arxiv.org/abs/2210.16400v2) | 2210.16400v2 | 6 |
| 2022-10-27 | [RePAST: A ReRAM-based PIM Accelerator for Second-order Training of DNN](https://arxiv.org/abs/2210.15255v1) | 2210.15255v1 | 10 |
| 2022-10-26 | [Characterizing Datapoints via Second-Split Forgetting](https://arxiv.org/abs/2210.15031v1) | 2210.15031v1 | 6 |
| 2022-10-26 | [Sharp inequalities for coherent states and their optimizers](https://arxiv.org/abs/2210.14798v1) | 2210.14798v1 | 6 |
| 2022-10-24 | [Deploying a Steered Query Optimizer in Production at Microsoft](https://arxiv.org/abs/2210.13625v1) | 2210.13625v1 | 6 |
| 2022-10-24 | [Selecting and Composing Learning Rate Policies for Deep Neural Networks](https://arxiv.org/abs/2210.12936v1) | 2210.12936v1 | 7 |
| 2022-10-23 | [Explicit Second-Order Min-Max Optimization: Practical Algorithms and Complexity Analysis](https://arxiv.org/abs/2210.12860v8) | 2210.12860v8 | 8 |
| 2022-10-22 | [Upgrade and commissioning of the ALICE muon spectrometer](https://arxiv.org/abs/2210.12431v1) | 2210.12431v1 | 6 |
| 2022-10-21 | [Amos: An Adam-style Optimizer with Adaptive Weight Decay towards Model-Oriented Scale](https://arxiv.org/abs/2210.11693v2) | 2210.11693v2 | 10 |
| 2022-10-19 | [Differentiable Self-Adaptive Learning Rate](https://arxiv.org/abs/2210.10290v1) | 2210.10290v1 | 11 |
| 2022-10-18 | [Second-order self-consistent field algorithms: from classical to quantum nuclei](https://arxiv.org/abs/2210.10170v2) | 2210.10170v2 | 7 |
| 2022-10-18 | [STay-ON-the-Ridge: Guaranteed Convergence to Local Minimax Equilibrium in Nonconvex-Nonconcave Games](https://arxiv.org/abs/2210.09769v1) | 2210.09769v1 | 6 |
| 2022-10-18 | [FLECS-CGD: A Federated Learning Second-Order Framework via Compression and Sketching with Compressed Gradient Differences](https://arxiv.org/abs/2210.09626v1) | 2210.09626v1 | 8 |
| 2022-10-17 | [On the convergence of policy gradient methods to Nash equilibria in general stochastic games](https://arxiv.org/abs/2210.08857v1) | 2210.08857v1 | 6 |
| 2022-10-14 | [Hybrid Decentralized Optimization: Leveraging Both First- and Zeroth-Order Optimizers for Faster Convergence](https://arxiv.org/abs/2210.07703v4) | 2210.07703v4 | 8 |
| 2022-10-12 | [Improving information retention in large scale online continual learning](https://arxiv.org/abs/2210.06401v1) | 2210.06401v1 | 7 |
| 2022-10-12 | [AdaNorm: Adaptive Gradient Norm Correction based Optimizer for CNNs](https://arxiv.org/abs/2210.06364v1) | 2210.06364v1 | 10 |
| 2022-10-12 | [Almost Sure Convergence of Distributed Optimization with Imperfect Information Sharing](https://arxiv.org/abs/2210.05897v2) | 2210.05897v2 | 6 |
| 2022-10-11 | [Learning to Optimize Quasi-Newton Methods](https://arxiv.org/abs/2210.06171v2) | 2210.06171v2 | 9 |
| 2022-10-06 | [SCORE: A Second-Order Conic Initialization for Range-Aided SLAM](https://arxiv.org/abs/2210.03177v1) | 2210.03177v1 | 6 |
| 2022-10-05 | [A Novel Entropy-Maximizing TD3-based Reinforcement Learning for Automatic PID Tuning](https://arxiv.org/abs/2210.02381v1) | 2210.02381v1 | 6 |
| 2022-10-05 | [Non-Convergence and Limit Cycles in the Adam optimizer](https://arxiv.org/abs/2210.02070v1) | 2210.02070v1 | 10 |
| 2022-10-03 | [Efficient Meta-Learning for Continual Learning with Taylor Expansion Approximation](https://arxiv.org/abs/2210.00713v1) | 2210.00713v1 | 7 |
| 2022-10-02 | [The Second-Order Football-Pool Problem and the Optimal Rate of Generalized-Covering Codes](https://arxiv.org/abs/2210.00531v1) | 2210.00531v1 | 6 |
| 2022-09-30 | [Improving Robustness with Adaptive Weight Decay](https://arxiv.org/abs/2210.00094v2) | 2210.00094v2 | 6 |
| 2022-09-29 | [NAG-GS: A Semi-Implicit Stochastic Optimizer with Large-Step Stability](https://arxiv.org/abs/2209.14937v3) | 2209.14937v3 | 10 |
| 2022-09-29 | [ELFPIE: an error-laxity Fourier ptychographic iterative engine](https://arxiv.org/abs/2209.14671v1) | 2209.14671v1 | 11 |
| 2022-09-28 | [High-order accurate multi-sub-step implicit integration algorithms with dissipation control for second-order hyperbolic problems](https://arxiv.org/abs/2209.13820v3) | 2209.13820v3 | 6 |
| 2022-09-27 | [Efficient Non-Parametric Optimizer Search for Diverse Tasks](https://arxiv.org/abs/2209.13575v1) | 2209.13575v1 | 7 |
| 2022-09-26 | [Generalized conditional gradient and learning in potential mean field games](https://arxiv.org/abs/2209.12772v2) | 2209.12772v2 | 6 |
| 2022-09-25 | [A simple proof of second-order sufficient optimality conditions in nonlinear semidefinite optimization](https://arxiv.org/abs/2209.12209v2) | 2209.12209v2 | 6 |
| 2022-09-24 | [Mountain muon tomography using a liquid scintillator detector](https://arxiv.org/abs/2209.11974v2) | 2209.11974v2 | 6 |
| 2022-09-15 | [Training Neural Networks in Single vs Double Precision](https://arxiv.org/abs/2209.07219v1) | 2209.07219v1 | 6 |
| 2022-09-14 | [Time rescaling of a primal-dual dynamical system with asymptotically vanishing damping](https://arxiv.org/abs/2209.06438v1) | 2209.06438v1 | 6 |
| 2022-09-12 | [Convergence of Batch Updating Methods with Approximate Gradients and/or Noisy Measurements: Theory and Computational Results](https://arxiv.org/abs/2209.05372v2) | 2209.05372v2 | 8 |
| 2022-09-10 | [Revisiting second-order optimality conditions for equality-contrained minimization problem](https://arxiv.org/abs/2209.04690v1) | 2209.04690v1 | 6 |
| 2022-09-08 | [A second-order fully-balanced structure-preserving variational discretization scheme for the Cahn-Hilliard Navier-Stokes system](https://arxiv.org/abs/2209.03849v2) | 2209.03849v2 | 7 |
| 2022-09-08 | [Double stabilizations and convergence analysis of a second-order linear numerical scheme for the nonlocal Cahn-Hilliard equation](https://arxiv.org/abs/2209.03647v1) | 2209.03647v1 | 7 |
| 2022-09-06 | [6D (2,0) Bootstrap with soft-Actor-Critic](https://arxiv.org/abs/2209.02801v2) | 2209.02801v2 | 6 |
| 2022-09-06 | [$1D$ to $nD$: A Meta Algorithm for Multivariate Global Optimization via Univariate Optimizers](https://arxiv.org/abs/2209.03246v1) | 2209.03246v1 | 6 |
| 2022-09-06 | [Faster federated optimization under second-order similarity](https://arxiv.org/abs/2209.02257v2) | 2209.02257v2 | 7 |
| 2022-09-03 | [Quantitative homogenization of principal Dirichlet eigenvalue shape optimizers](https://arxiv.org/abs/2209.01446v1) | 2209.01446v1 | 7 |
| 2022-09-03 | [Simplified Quadratic Gradient: A Unified Framework Bridging Gradient Descent and Newton-Type Methods by Synthesizing Hessians and Gradients](https://arxiv.org/abs/2209.03282v5) | 2209.03282v5 | 12 |
| 2022-09-01 | [Versatile Single-Loop Method for Gradient Estimator: First and Second Order Optimality, and its Application to Federated Learning](https://arxiv.org/abs/2209.00361v2) | 2209.00361v2 | 6 |
| 2022-09-01 | [Efficient preconditioners for solving dynamical optimal transport via interior point methods](https://arxiv.org/abs/2209.00315v3) | 2209.00315v3 | 6 |
| 2022-09-01 | [Analysis and Numerical Approximation of Stationary Second-Order Mean Field Game Partial Differential Inclusions](https://arxiv.org/abs/2209.00303v4) | 2209.00303v4 | 7 |
| 2022-08-30 | [Optimal geometric multigrid preconditioners for HDG-P0 schemes for the reaction-diffusion equation and the generalized Stokes equations](https://arxiv.org/abs/2208.14418v2) | 2208.14418v2 | 6 |
| 2022-08-30 | [Cardinal Optimizer (COPT) User Guide](https://arxiv.org/abs/2208.14314v4) | 2208.14314v4 | 6 |
| 2022-08-30 | [Using Taylor-Approximated Gradients to Improve the Frank-Wolfe Method for Empirical Risk Minimization](https://arxiv.org/abs/2208.13933v2) | 2208.13933v2 | 6 |
| 2022-08-28 | [Mean viability theorems and second-order Hamilton-Jacobi equations](https://arxiv.org/abs/2208.13276v4) | 2208.13276v4 | 6 |
| 2022-08-26 | [Flexible Vertical Federated Learning with Heterogeneous Parties](https://arxiv.org/abs/2208.12672v3) | 2208.12672v3 | 7 |
| 2022-08-25 | [Non-existence of perturbed solutions under a second-order sufficient condition](https://arxiv.org/abs/2208.12115v1) | 2208.12115v1 | 6 |
| 2022-08-23 | [Robustness to Unbounded Smoothness of Generalized SignSGD](https://arxiv.org/abs/2208.11195v1) | 2208.11195v1 | 8 |
| 2022-08-22 | [Benchmarking of Different Optimizers in the Variational Quantum Algorithms for Applications in Quantum Chemistry](https://arxiv.org/abs/2208.10285v3) | 2208.10285v3 | 8 |
| 2022-08-22 | [Local Geometry of Nonconvex Spike Deconvolution from Low-Pass Measurements](https://arxiv.org/abs/2208.10073v3) | 2208.10073v3 | 8 |
| 2022-08-21 | [Critical Bach Size Minimizes Stochastic First-Order Oracle Complexity of Deep Learning Optimizer using Hyperparameters Close to One](https://arxiv.org/abs/2208.09814v1) | 2208.09814v1 | 12 |
| 2022-08-13 | [Adan: Adaptive Nesterov Momentum Algorithm for Faster Optimizing Deep Models](https://arxiv.org/abs/2208.06677v5) | 2208.06677v5 | 13 |
| 2022-08-12 | [A Practical Second-order Latent Factor Model via Distributed Particle Swarm Optimization](https://arxiv.org/abs/2208.06125v1) | 2208.06125v1 | 11 |
| 2022-08-05 | [On the weak second-order optimality condition for nonlinear semidefinite and second-order cone programming](https://arxiv.org/abs/2208.03076v1) | 2208.03076v1 | 7 |

### 2019
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2019-12-31 | [Investigating Wave Energy Potential in Southern Coasts of the Caspian Sea Using Grey Wolf Optimizer Algorithm](https://arxiv.org/abs/1912.13201v2) | 1912.13201v2 | 6 |
| 2019-12-30 | [Opytimizer: A Nature-Inspired Python Optimizer](https://arxiv.org/abs/1912.13002v2) | 1912.13002v2 | 7 |
| 2019-12-24 | [CProp: Adaptive Learning Rate Scaling from Past Gradient Conformity](https://arxiv.org/abs/1912.11493v1) | 1912.11493v1 | 8 |
| 2019-12-23 | [Self-consistent range-separated density-functional theory with second-order perturbative correction via the optimized-effective-potential method](https://arxiv.org/abs/1912.10893v1) | 1912.10893v1 | 6 |
| 2019-12-23 | [Fortified Test Functions for Global Optimization and the Power of Multiple Runs](https://arxiv.org/abs/1912.10575v1) | 1912.10575v1 | 6 |
| 2019-12-20 | [Robust Preconditioners for Multiple Saddle Point Problems and Applications to Optimal Control Problems](https://arxiv.org/abs/1912.09995v1) | 1912.09995v1 | 6 |
| 2019-12-20 | [Second-order Information in First-order Optimization Methods](https://arxiv.org/abs/1912.09926v1) | 1912.09926v1 | 9 |
| 2019-12-16 | [PETSc TSAdjoint: a discrete adjoint ODE solver for first-order and second-order sensitivity analysis](https://arxiv.org/abs/1912.07696v2) | 1912.07696v2 | 7 |
| 2019-12-16 | [PyHessian: Neural Networks Through the Lens of the Hessian](https://arxiv.org/abs/1912.07145v3) | 1912.07145v3 | 9 |
| 2019-12-10 | [Robust Training and Initialization of Deep Neural Networks: An Adaptive Basis Viewpoint](https://arxiv.org/abs/1912.04862v1) | 1912.04862v1 | 6 |
| 2019-12-10 | [Second-Order Non-Convex Optimization for Constrained Fixed-Structure Static Output Feedback Controller Synthesis](https://arxiv.org/abs/1912.04617v3) | 1912.04617v3 | 7 |
| 2019-12-09 | [Trust-Region Newton-CG with Strong Second-Order Complexity Guarantees for Nonconvex Optimization](https://arxiv.org/abs/1912.04365v3) | 1912.04365v3 | 7 |
| 2019-12-04 | [A Verified Optimizer for Quantum Circuits](https://arxiv.org/abs/1912.02250v3) | 1912.02250v3 | 6 |
| 2019-12-04 | [Domain-independent Dominance of Adaptive Methods](https://arxiv.org/abs/1912.01823v3) | 1912.01823v3 | 6 |
| 2019-12-03 | [Axial vector transition form factors in holographic QCD and their contribution to the anomalous magnetic moment of the muon](https://arxiv.org/abs/1912.01596v5) | 1912.01596v5 | 6 |
| 2019-11-30 | [Rational Polyhedral Outer-Approximations of the Second-Order Cone](https://arxiv.org/abs/1912.00256v2) | 1912.00256v2 | 6 |
| 2019-11-30 | [Learning Rate Dropout](https://arxiv.org/abs/1912.00144v2) | 1912.00144v2 | 8 |
| 2019-11-26 | [A wave function perspective and efficient truncation of renormalised second-order perturbation theory](https://arxiv.org/abs/1911.11695v4) | 1911.11695v4 | 7 |
| 2019-11-24 | [Second-order optimality conditions for SDCMPCC and application to rank optimization problems](https://arxiv.org/abs/1911.10551v1) | 1911.10551v1 | 6 |
| 2019-11-22 | [Optimal-order preconditioners for the Morse-Ingard equations](https://arxiv.org/abs/1911.10247v1) | 1911.10247v1 | 6 |
| 2019-11-21 | [GPU-Accelerated Event Reconstruction for the COMET Phase-I Experiment](https://arxiv.org/abs/1911.09340v3) | 1911.09340v3 | 6 |
| 2019-11-19 | [Finite element methods based on two families of second-order numerical formulas for the fractional Cable model with smooth solutions](https://arxiv.org/abs/1911.08166v2) | 1911.08166v2 | 7 |
| 2019-11-18 | [Convergence Analysis of a Momentum Algorithm with Adaptive Step Size for Non Convex Optimization](https://arxiv.org/abs/1911.07596v2) | 1911.07596v2 | 7 |
| 2019-11-17 | [Status of the DeeMe Experiment, an Experimental Search for $μ$-$e$ Conversion at J-PARC MLF](https://arxiv.org/abs/1911.07143v1) | 1911.07143v1 | 6 |
| 2019-11-16 | [A Fully Stochastic Second-Order Trust Region Method](https://arxiv.org/abs/1911.06920v1) | 1911.06920v1 | 8 |
| 2019-11-14 | [Accelerating Least Squares Imaging Using Deep Learning Techniques](https://arxiv.org/abs/1911.06027v2) | 1911.06027v2 | 6 |
| 2019-11-14 | [Towards an $O(\frac{1}{t})$ convergence rate for distributed dual averaging](https://arxiv.org/abs/1911.05979v2) | 1911.05979v2 | 6 |
| 2019-11-14 | [Understanding the Disharmony between Weight Normalization Family and Weight Decay: $ε-$shifted $L_2$ Regularizer](https://arxiv.org/abs/1911.05920v1) | 1911.05920v1 | 9 |
| 2019-11-13 | [A new preconditioner for elliptic PDE-constrained optimization problems](https://arxiv.org/abs/1911.05807v1) | 1911.05807v1 | 7 |
| 2019-11-11 | [Collision-Free Trajectory Design for 2D Persistent Monitoring Using Second-Order Agents](https://arxiv.org/abs/1911.04297v1) | 1911.04297v1 | 7 |
| 2019-11-11 | [Split generalized-$α$ method: A linear-cost solver for a modified generalized-method for multi-dimensional second-order hyperbolic systems](https://arxiv.org/abs/1911.04125v1) | 1911.04125v1 | 7 |
| 2019-11-11 | [Second-order optimality conditions for non-convex set-constrained optimization problems](https://arxiv.org/abs/1911.04076v2) | 1911.04076v2 | 6 |
| 2019-11-07 | [A Hierarchical Optimizer for Recommendation System Based on Shortest Path Algorithm](https://arxiv.org/abs/1911.08994v1) | 1911.08994v1 | 6 |
| 2019-11-06 | [Faster Least Squares Optimization](https://arxiv.org/abs/1911.02675v3) | 1911.02675v3 | 8 |
| 2019-11-06 | [On fixed-point, Krylov, and $2\times 2$ block preconditioners for nonsymmetric problems](https://arxiv.org/abs/1911.02664v4) | 1911.02664v4 | 7 |
| 2019-11-01 | [On Second-Order Group Influence Functions for Black-Box Predictions](https://arxiv.org/abs/1911.00418v2) | 1911.00418v2 | 6 |
| 2019-11-01 | [Does Adam optimizer keep close to the optimal point?](https://arxiv.org/abs/1911.00289v1) | 1911.00289v1 | 11 |
| 2019-10-30 | [Understanding the Role of Momentum in Stochastic Gradient Methods](https://arxiv.org/abs/1910.13962v1) | 1910.13962v1 | 7 |
| 2019-10-28 | [FD-Net with Auxiliary Time Steps: Fast Prediction of PDEs using Hessian-Free Trust-Region Methods](https://arxiv.org/abs/1910.12680v2) | 1910.12680v2 | 9 |
| 2019-10-25 | [Optimizer Benchmarking Needs to Account for Hyperparameter Tuning](https://arxiv.org/abs/1910.11758v4) | 1910.11758v4 | 6 |
| 2019-10-21 | [Learning to Learn by Zeroth-Order Oracle](https://arxiv.org/abs/1910.09464v2) | 1910.09464v2 | 6 |
| 2019-10-21 | [Implementation of a modified Nesterov's Accelerated quasi-Newton Method on Tensorflow](https://arxiv.org/abs/1910.09158v1) | 1910.09158v1 | 6 |
| 2019-10-18 | [First-Order Preconditioning via Hypergradient Descent](https://arxiv.org/abs/1910.08461v2) | 1910.08461v2 | 14 |
| 2019-10-16 | [An Exponential Learning Rate Schedule for Deep Learning](https://arxiv.org/abs/1910.07454v3) | 1910.07454v3 | 8 |
| 2019-10-15 | [ZO-AdaMM: Zeroth-Order Adaptive Momentum Method for Black-Box Optimization](https://arxiv.org/abs/1910.06513v2) | 1910.06513v2 | 7 |
| 2019-10-14 | [Second-Order Convergence of Asynchronous Parallel Stochastic Gradient Descent: When Is the Linear Speedup Achieved?](https://arxiv.org/abs/1910.06000v6) | 1910.06000v6 | 8 |
| 2019-10-11 | [On Empirical Comparisons of Optimizers for Deep Learning](https://arxiv.org/abs/1910.05446v3) | 1910.05446v3 | 9 |
| 2019-10-11 | [Demon: Improved Neural Network Training with Momentum Decay](https://arxiv.org/abs/1910.04952v4) | 1910.04952v4 | 10 |
| 2019-10-10 | [One Sample Stochastic Frank-Wolfe](https://arxiv.org/abs/1910.04322v1) | 1910.04322v1 | 6 |
| 2019-10-09 | [Black-box Optimizer with Implicit Natural Gradient](https://arxiv.org/abs/1910.04301v3) | 1910.04301v3 | 8 |
| 2019-10-09 | [Second-order coding rates for key distillation in quantum key distribution](https://arxiv.org/abs/1910.03883v2) | 1910.03883v2 | 6 |
| 2019-10-08 | [On the sensitivity of the optimal partition for parametric second-order conic optimization](https://arxiv.org/abs/1910.03684v2) | 1910.03684v2 | 6 |
| 2019-10-08 | [On Polyhedral and Second-Order Cone Decompositions of Semidefinite Optimization Problems](https://arxiv.org/abs/1910.03143v2) | 1910.03143v2 | 7 |
| 2019-10-03 | [A muon source based on planar channelling radiation](https://arxiv.org/abs/1910.01541v2) | 1910.01541v2 | 6 |
| 2019-10-02 | [Stochastic gradient descent for hybrid quantum-classical optimization](https://arxiv.org/abs/1910.01155v3) | 1910.01155v3 | 6 |
| 2019-10-01 | [SlowMo: Improving Communication-Efficient Distributed SGD with Slow Momentum](https://arxiv.org/abs/1910.00643v2) | 1910.00643v2 | 8 |
| 2019-10-01 | [Revisiting Fine-tuning for Few-shot Learning](https://arxiv.org/abs/1910.00216v2) | 1910.00216v2 | 7 |
| 2019-09-30 | [Min-Max Optimization without Gradients: Convergence and Applications to Adversarial ML](https://arxiv.org/abs/1909.13806v3) | 1909.13806v3 | 6 |
| 2019-09-30 | [$H^1$-norm error estimate for a nonstandard finite element approximation of second-order linear elliptic PDEs in non-divergence form](https://arxiv.org/abs/1909.13803v1) | 1909.13803v1 | 6 |
| 2019-09-29 | [Gradient Descent: The Ultimate Optimizer](https://arxiv.org/abs/1909.13371v2) | 1909.13371v2 | 9 |
| 2019-09-28 | [Preisach Based Storage Devices and Global Optimizers](https://arxiv.org/abs/1909.13148v1) | 1909.13148v1 | 6 |
| 2019-09-27 | [Global Sparse Momentum SGD for Pruning Very Deep Neural Networks](https://arxiv.org/abs/1909.12778v3) | 1909.12778v3 | 6 |
| 2019-09-27 | [Error estimation for second-order PDEs in non-variational form](https://arxiv.org/abs/1909.12676v2) | 1909.12676v2 | 6 |
| 2019-09-27 | [On families of optimal Hardy-weights for linear second-order elliptic operators](https://arxiv.org/abs/1909.12512v1) | 1909.12512v1 | 6 |
| 2019-09-26 | [At Stability's Edge: How to Adjust Hyperparameters to Preserve Minima Selection in Asynchronous Training of Neural Networks?](https://arxiv.org/abs/1909.12340v2) | 1909.12340v2 | 8 |
| 2019-09-26 | [Military Dog Based Optimizer and its Application to Fake Review](https://arxiv.org/abs/1909.11890v1) | 1909.11890v1 | 7 |
| 2019-09-23 | [Second-order cone interior-point method for quasistatic and moderate dynamic cohesive fracture](https://arxiv.org/abs/1909.10641v1) | 1909.10641v1 | 6 |
| 2019-09-21 | [Using Statistics to Automate Stochastic Optimization](https://arxiv.org/abs/1909.09785v1) | 1909.09785v1 | 7 |
| 2019-09-19 | [An Adaptive Optimizer for Measurement-Frugal Variational Algorithms](https://arxiv.org/abs/1909.09083v3) | 1909.09083v3 | 8 |
| 2019-09-18 | [Schwarz solvers and preconditioners for the closest point method](https://arxiv.org/abs/1909.08734v2) | 1909.08734v2 | 7 |
| 2019-09-12 | [An Extension of Fast Iterative Shrinkage-thresholding to Riemannian Optimization for Sparse Principal Component Analysis](https://arxiv.org/abs/1909.05485v4) | 1909.05485v4 | 6 |
| 2019-09-12 | [diffGrad: An Optimization Method for Convolutional Neural Networks](https://arxiv.org/abs/1909.11015v4) | 1909.11015v4 | 6 |
| 2019-09-11 | [Adversarial Model Predictive Control via Second-Order Cone Programming](https://arxiv.org/abs/1909.05169v1) | 1909.05169v1 | 6 |
| 2019-09-09 | [Measurements of differential Z boson production cross sections in proton-proton collisions at $\sqrt{s} =$ 13 TeV](https://arxiv.org/abs/1909.04133v2) | 1909.04133v2 | 6 |
| 2019-09-05 | [Training High-Performance and Large-Scale Deep Neural Networks with Full 8-bit Integers](https://arxiv.org/abs/1909.02384v2) | 1909.02384v2 | 7 |
| 2019-09-04 | [Quasi-Newton Optimization Methods For Deep Learning Applications](https://arxiv.org/abs/1909.01994v1) | 1909.01994v1 | 6 |
| 2019-09-03 | [Fast Gradient Methods with Alignment for Symmetric Linear Systems without Using Cauchy Step](https://arxiv.org/abs/1909.01479v2) | 1909.01479v2 | 6 |
| 2019-09-03 | [L-Sweeps: A scalable, parallel preconditioner for the high-frequency Helmholtz equation](https://arxiv.org/abs/1909.01467v2) | 1909.01467v2 | 6 |
| 2019-09-03 | [On Loss Functions for Supervised Monaural Time-Domain Speech Enhancement](https://arxiv.org/abs/1909.01019v2) | 1909.01019v2 | 7 |
| 2019-08-27 | [On the Convergence Theory of Gradient-Based Model-Agnostic Meta-Learning Algorithms](https://arxiv.org/abs/1908.10400v4) | 1908.10400v4 | 8 |
| 2019-08-22 | [On the convergence of single-call stochastic extra-gradient methods](https://arxiv.org/abs/1908.08465v2) | 1908.08465v2 | 6 |
| 2019-08-21 | [A Full Quantum Eigensolver for Quantum Chemistry Simulations](https://arxiv.org/abs/1908.07927v2) | 1908.07927v2 | 6 |
| 2019-08-21 | [Nesterov's method with decreasing learning rate leads to accelerated stochastic gradient descent](https://arxiv.org/abs/1908.07861v5) | 1908.07861v5 | 6 |
| 2019-08-20 | [Automatic and Simultaneous Adjustment of Learning Rate and Momentum for Stochastic Gradient Descent](https://arxiv.org/abs/1908.07607v1) | 1908.07607v1 | 7 |
| 2019-08-19 | [Second-Order Guarantees of Stochastic Gradient Descent in Non-Convex Optimization](https://arxiv.org/abs/1908.07023v1) | 1908.07023v1 | 7 |
| 2019-08-19 | [Quantum algorithms for Second-Order Cone Programming and Support Vector Machines](https://arxiv.org/abs/1908.06720v4) | 1908.06720v4 | 6 |
| 2019-08-16 | [Optimal Paired Comparison Experiments for Second-Order Interactions](https://arxiv.org/abs/1908.06090v2) | 1908.06090v2 | 6 |
| 2019-08-15 | [Muon Identification Using Deep Neural Networks with the Muon Telescope Detector at STAR](https://arxiv.org/abs/1908.05645v1) | 1908.05645v1 | 6 |
| 2019-08-13 | [On the Convergence of AdaBound and its Connection to SGD](https://arxiv.org/abs/1908.04457v2) | 1908.04457v2 | 8 |
| 2019-08-07 | [A Generic Efficient Biased Optimizer for Consensus Protocols](https://arxiv.org/abs/1908.02675v1) | 1908.02675v1 | 6 |
| 2019-08-02 | [Calibrating the Adaptive Learning Rate to Improve Convergence of ADAM](https://arxiv.org/abs/1908.00700v2) | 1908.00700v2 | 7 |
| 2019-07-28 | [ROAM: Recurrently Optimizing Tracking Model](https://arxiv.org/abs/1907.12006v3) | 1907.12006v3 | 6 |
| 2019-07-27 | [The Wang-Landau Algorithm as Stochastic Optimization and Its Acceleration](https://arxiv.org/abs/1907.11985v2) | 1907.11985v2 | 6 |
| 2019-07-26 | [A simple Newton method for local nonsmooth optimization](https://arxiv.org/abs/1907.11742v1) | 1907.11742v1 | 6 |
| 2019-07-26 | [BGADAM: Boosting based Genetic-Evolutionary ADAM for Neural Network Optimization](https://arxiv.org/abs/1908.08015v2) | 1908.08015v2 | 6 |
| 2019-07-23 | [BagNet: Berkeley Analog Generator with Layout Optimizer Boosted with Deep Neural Networks](https://arxiv.org/abs/1907.10515v1) | 1907.10515v1 | 6 |
| 2019-07-19 | [Lookahead Optimizer: k steps forward, 1 step back](https://arxiv.org/abs/1907.08610v2) | 1907.08610v2 | 11 |
| 2019-07-19 | [Average Linear and Angular Momentum and Power of Random Fields Near a Perfectly Conducting Boundary](https://arxiv.org/abs/1907.09304v2) | 1907.09304v2 | 7 |
| 2019-07-16 | [SGD momentum optimizer with step estimation by online parabola model](https://arxiv.org/abs/1907.07063v3) | 1907.07063v3 | 12 |
| 2019-07-16 | [Quantitative truncation estimates for fractional Hardy-Sobolev optimizers](https://arxiv.org/abs/1907.06892v1) | 1907.06892v1 | 6 |
| 2019-07-09 | [Which Algorithmic Choices Matter at Which Batch Sizes? Insights From a Noisy Quadratic Model](https://arxiv.org/abs/1907.04164v2) | 1907.04164v2 | 9 |
| 2019-07-08 | [Sparse Hierarchical Preconditioners Using Piecewise Smooth Approximations of Eigenvectors](https://arxiv.org/abs/1907.03406v3) | 1907.03406v3 | 7 |
| 2019-07-03 | [BPX preconditioners for isogeometric analysis using analysis-suitable T-splines](https://arxiv.org/abs/1907.01790v1) | 1907.01790v1 | 6 |
| 2019-07-02 | [Training Auto-encoder-based Optimizers for Terahertz Image Reconstruction](https://arxiv.org/abs/1907.01377v2) | 1907.01377v2 | 6 |
| 2019-06-30 | [Universal Online Convex Optimization with Minimax Optimal Second-Order Dynamic Regret](https://arxiv.org/abs/1907.00497v3) | 1907.00497v3 | 9 |
| 2019-06-29 | [Multi-objective multi-generation Gaussian process optimizer for design optimization](https://arxiv.org/abs/1907.00250v2) | 1907.00250v2 | 7 |
| 2019-06-28 | [Resolution of the ATLAS muon spectrometer monitored drift tubes in LHC Run 2](https://arxiv.org/abs/1906.12226v2) | 1906.12226v2 | 8 |
| 2019-06-27 | [Adaptive First-Order System Least-Squares Finite Element Methods for Second Order Elliptic Equations in Non-Divergence Form](https://arxiv.org/abs/1906.11436v1) | 1906.11436v1 | 6 |
| 2019-06-24 | [Exact formula for the second-order tangent set of the second-order cone complementarity set](https://arxiv.org/abs/1906.09976v1) | 1906.09976v1 | 6 |
| 2019-06-24 | [In Hindsight: A Smooth Reward for Steady Exploration](https://arxiv.org/abs/1906.09781v1) | 1906.09781v1 | 6 |
| 2019-06-21 | [On Second-Order Optimality Conditions for Optimal Control Problems Governed by the Obstacle Problem](https://arxiv.org/abs/1906.09065v1) | 1906.09065v1 | 6 |
| 2019-06-11 | [Large Scale Structure of Neural Network Loss Landscapes](https://arxiv.org/abs/1906.04724v1) | 1906.04724v1 | 6 |
| 2019-06-10 | [Continuous Time Analysis of Momentum Methods](https://arxiv.org/abs/1906.04285v2) | 1906.04285v2 | 6 |
| 2019-06-10 | [Exploration and Exploitation in Symbolic Regression using Quality-Diversity and Evolutionary Strategies Algorithms](https://arxiv.org/abs/1906.03959v1) | 1906.03959v1 | 6 |
| 2019-06-08 | [Using learned optimizers to make models robust to input noise](https://arxiv.org/abs/1906.03367v1) | 1906.03367v1 | 6 |

<!-- table:end papers -->
