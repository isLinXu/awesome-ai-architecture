# 🏛️ 里程碑模型（Landmark Models）

> 模块论文回答"积木怎么造"，模型报告回答"积木拼起来行不行"。

每一条架构路线的成立，最终都要靠一个里程碑模型来背书：MHA 靠 GPT-3，RoPE+SwiGLU 靠 LLaMA，
GQA 靠 Llama 2/3，MLA 靠 DeepSeek-V3。这条赛道收录定义时代的模型技术报告与 scaling law，
读它们的价值在于看**模块组合的真实工程配比**，而不只是单点创新。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Scaling Laws for Neural Language Models (Kaplan) | [2001.08361](https://arxiv.org/abs/2001.08361) | 2020 | 幂律 scaling law，"往哪扩"有了量化依据 |
| Language Models are Few-Shot Learners (GPT-3) | [2005.14165](https://arxiv.org/abs/2005.14165) | 2020 | 175B MHA 稠密模型，规模即能力的宣言 |
| An Image is Worth 16x16 Words (ViT) | [2010.11929](https://arxiv.org/abs/2010.11929) | 2020 | Transformer 不加归纳偏置正面攻入视觉 |
| PaLM: Scaling Language Modeling with Pathways | [2204.02311](https://arxiv.org/abs/2204.02311) | 2022 | 540B + MQA + Pathways 系统工程 |
| Training Compute-Optimal Large Language Models (Chinchilla) | [2203.15556](https://arxiv.org/abs/2203.15556) | 2022 | 修正 Kaplan：数据与参数应等比扩，1:20 配比 |
| LLaMA: Open and Efficient Foundation Language Models | [2302.13971](https://arxiv.org/abs/2302.13971) | 2023 | RoPE+SwiGLU+RMSNorm 组合成为开放模型标准件 |
| GPT-4 Technical Report | [2303.08774](https://arxiv.org/abs/2303.08774) | 2023 | 闭源旗舰的时代分界 |
| Llama 2: Open Foundation and Fine-Tuned Chat Models | [2307.09288](https://arxiv.org/abs/2307.09288) | 2023 | GQA 进入主流，开放权重生态起飞 |
| Gemini: A Family of Highly Capable Multimodal Models | [2312.11805](https://arxiv.org/abs/2312.11805) | 2023 | 原生多模态架构的闭源标杆 |
| Gemma: Open Models Based on Gemini Research and Technology | [2403.08295](https://arxiv.org/abs/2403.08295) | 2024 | 局部/全局交替注意力的推广者 |
| The Llama 3 Herd of Models | [2407.21783](https://arxiv.org/abs/2407.21783) | 2024 | 405B 全 GQA，开放权重追平闭源 |
| Qwen Technical Report | [2309.16609](https://arxiv.org/abs/2309.16609) | 2023 | 中文生态开放权重的体系化起点 |
| DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning | [2501.12948](https://arxiv.org/abs/2501.12948) | 2025 | RL 激发推理，架构之上训练范式的拐点 |

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-12 | [Ropedia Xperience 2: A Gold Standard for Scaling Physical AI Environments and Behaviors](https://arxiv.org/abs/2611.17060v1) | 2611.17060v1 | 8 |
| 2026-11-12 | [A scaling law for numerical computation of fracture stress intensity factors](https://arxiv.org/abs/2611.16850v1) | 2611.16850v1 | 7 |
| 2026-11-10 | [Emergent Biological Capabilities in a Foundation Model for Molecular Interactions](https://arxiv.org/abs/2611.14504v1) | 2611.14504v1 | 13 |
| 2026-11-04 | [Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817v2) | 2611.06817v2 | 14 |
| 2026-11-04 | [Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models](https://arxiv.org/abs/2611.06817v3) | 2611.06817v3 | 14 |
| 2026-11-03 | [Scaling Laws For Data-Constrained Dense Retrieval](https://arxiv.org/abs/2611.04979v1) | 2611.04979v1 | 7 |
| 2026-11-03 | [Amortized Nonlinear Variable Selection with Prior-Data Fitted Networks](https://arxiv.org/abs/2611.04848v1) | 2611.04848v1 | 8 |
| 2026-11-02 | [A Scaling Theory of Multi-Epoch Pretraining: Late-Time Overfitting and Ensembling](https://arxiv.org/abs/2611.03590v1) | 2611.03590v1 | 7 |
| 2026-11-01 | [Hinted Scaling Laws](https://arxiv.org/abs/2611.02270v1) | 2611.02270v1 | 9 |
| 2026-10-28 | [Data Scaling Laws in Stereo Matching: From In-domain Fitting to Cross-domain Generalization](https://arxiv.org/abs/2610.38600v1) | 2610.38600v1 | 11 |
| 2026-10-28 | [LLM-PowerTrace: A Dataset of Time-Resolved GPU Power Traces for AI Compute](https://arxiv.org/abs/2610.38315v1) | 2610.38315v1 | 7 |
| 2026-10-27 | [Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis](https://arxiv.org/abs/2610.37648v1) | 2610.37648v1 | 9 |
| 2026-10-24 | [How To Build A Modern Diffusion Language Model](https://arxiv.org/abs/2610.33391v1) | 2610.33391v1 | 8 |
| 2026-10-22 | [Rewriting Scaling Laws for Synthetic Data with Compute and Data Constraints](https://arxiv.org/abs/2610.31867v1) | 2610.31867v1 | 8 |
| 2026-10-22 | [CURTAIN: Towards a Foundation Model for Neutrino Telescopes](https://arxiv.org/abs/2610.30894v1) | 2610.30894v1 | 13 |
| 2026-10-20 | [Scaling in Games: Continued Pre-Training For Embodied Agents In Diverse Virtual Worlds](https://arxiv.org/abs/2610.28698v1) | 2610.28698v1 | 7 |
| 2026-10-20 | [Foundations of the Scaling Law](https://arxiv.org/abs/2610.27789v2) | 2610.27789v2 | 7 |
| 2026-10-14 | [The Cost of Context: Profiling the Energy Footprint of Input Tokens in Large Language Models](https://arxiv.org/abs/2610.19819v1) | 2610.19819v1 | 7 |
| 2026-10-13 | [Exact Scaling Laws for a Random-Features Bigram Model](https://arxiv.org/abs/2610.19281v1) | 2610.19281v1 | 8 |
| 2026-10-13 | [Mixed Precision Scaling Laws for Quantized Pretraining](https://arxiv.org/abs/2610.17637v1) | 2610.17637v1 | 9 |
| 2026-10-13 | [Revisiting the 16x Pretraining Compute Gap between Diffusion and Autoregressive Language Models](https://arxiv.org/abs/2610.17590v2) | 2610.17590v2 | 8 |
| 2026-10-12 | [SLDBench v2: Active Scaling Law Discovery](https://arxiv.org/abs/2610.16297v2) | 2610.16297v2 | 8 |
| 2026-10-11 | [Genesis: Visual Augmentation Primitives for Multimodal Chain-of-Thought Reasoning](https://arxiv.org/abs/2610.15565v1) | 2610.15565v1 | 7 |
| 2026-10-10 | [Scaling Laws for Multimodal Data Mixtures](https://arxiv.org/abs/2610.14423v2) | 2610.14423v2 | 8 |
| 2026-10-08 | [How Data Scales in Agentic Reinforcement Learning: Laws and Synthesis Strategies](https://arxiv.org/abs/2610.23946v2) | 2610.23946v2 | 8 |
| 2026-10-08 | [Emergent Inverse-Depth Scaling From Nonlinearity In Attention](https://arxiv.org/abs/2610.11063v1) | 2610.11063v1 | 7 |
| 2026-10-07 | [Fault-tolerant foundation models](https://arxiv.org/abs/2610.10311v1) | 2610.10311v1 | 10 |
| 2026-10-05 | [Localize Any Object in X-Ray Security Scans without Human Annotation](https://arxiv.org/abs/2610.07326v2) | 2610.07326v2 | 9 |
| 2026-10-05 | [How to scale your HEP ML models: A recipe for robust architecture comparisons at scale](https://arxiv.org/abs/2610.06784v1) | 2610.06784v1 | 8 |
| 2026-10-05 | [Scaling Down the Scaling Laws: Parameter Efficiency and Compute-Optimal Training in Resource-Constrained Large Language Models](https://arxiv.org/abs/2610.06387v2) | 2610.06387v2 | 9 |
| 2026-10-05 | [Training and Scaling Compute-Optimal Physiological Waveform Foundation Models](https://arxiv.org/abs/2610.05649v1) | 2610.05649v1 | 12 |
| 2026-10-04 | [A Unified Scaling Law for Time Series Foundation Models](https://arxiv.org/abs/2610.05269v1) | 2610.05269v1 | 12 |
| 2026-10-03 | [How RL Reshapes LLM Reasoning: Transferability, Coverage, and Scaling Laws](https://arxiv.org/abs/2610.04158v1) | 2610.04158v1 | 8 |
| 2026-10-01 | [Neural scaling laws and evolution of learnable activation functions of Kolmogorov-Arnold networks](https://arxiv.org/abs/2610.00985v1) | 2610.00985v1 | 7 |
| 2026-09-30 | [Emergent Unfaithfulness: How Alignment Training Causes Language Models to Silently Override Task Faithfulness](https://arxiv.org/abs/2610.00568v1) | 2610.00568v1 | 7 |
| 2026-09-30 | [How Much Is an AI Token Worth? Scaling Laws for Wild AI-Generated Web Text](https://arxiv.org/abs/2609.40295v1) | 2609.40295v1 | 8 |
| 2026-09-30 | [Scaling law of variational quantum algorithms](https://arxiv.org/abs/2609.39949v1) | 2609.39949v1 | 7 |
| 2026-09-28 | [ScAn-Bench: Evaluating Scaling Analysis Methodology](https://arxiv.org/abs/2609.35707v2) | 2609.35707v2 | 9 |
| 2026-09-28 | [How Far Are We from Removing the Visual Encoder? Scaling Laws for Encoder-Free Multimodal Pretraining](https://arxiv.org/abs/2609.35457v1) | 2609.35457v1 | 11 |
| 2026-09-28 | [Privacy-Preserving Full-Body Meshing from mmWave Radar via Mesh Foundation Model Supervision](https://arxiv.org/abs/2609.34768v3) | 2609.34768v3 | 11 |
| 2026-09-28 | [X-MoD: Practical Scaling Laws for Sparse-Depth Routing Beyond Mixture-of-Depths](https://arxiv.org/abs/2609.34212v1) | 2609.34212v1 | 8 |
| 2026-09-26 | [Emergent One-Third Scaling Law as Attention Tries to Concentrate](https://arxiv.org/abs/2609.32100v1) | 2609.32100v1 | 9 |
| 2026-09-25 | [Game Arena: Strategic LLM Evaluation in Competitive Environments](https://arxiv.org/abs/2609.31473v1) | 2609.31473v1 | 7 |
| 2026-09-23 | [SGA: Uncertainty Quantification for Multi-Step Forecasting in Time Series Foundation Models](https://arxiv.org/abs/2609.28582v1) | 2609.28582v1 | 10 |
| 2026-09-23 | [A Scaling Study for fMRI Foundation Models](https://arxiv.org/abs/2609.27232v1) | 2609.27232v1 | 12 |
| 2026-09-21 | [Universal $Z^{2/3}/\sqrt{Q_α}$ Scaling Law in Alpha Decay from Nuclei to Neutron-Star Mergers](https://arxiv.org/abs/2609.25162v1) | 2609.25162v1 | 7 |
| 2026-09-15 | [LimiX-2: A Contextual Mechanism Network Towards General Structured-Data Intelligence](https://arxiv.org/abs/2609.17488v1) | 2609.17488v1 | 10 |
| 2026-09-13 | [Empirical Scaling Laws of Quantum Vision Transformers](https://arxiv.org/abs/2610.13970v1) | 2610.13970v1 | 8 |
| 2026-09-13 | [When does a scaling result justify a different allocation? A critical review of resource-allocation evidence for AI systems](https://arxiv.org/abs/2609.14500v1) | 2609.14500v1 | 7 |
| 2026-09-10 | [Benchmark Radar: A Living Database and Search Engine for AI Benchmarks and Evaluation](https://arxiv.org/abs/2609.11115v4) | 2609.11115v4 | 7 |
| 2026-09-09 | [Cooperative LEO-Terrestrial Multistatic ISAC: CRLB Analysis, Scaling Laws, and Satellite Selection](https://arxiv.org/abs/2609.09784v1) | 2609.09784v1 | 7 |
| 2026-09-04 | [Amortizing Scaling Law Construction Costs](https://arxiv.org/abs/2609.05016v1) | 2609.05016v1 | 10 |
| 2026-09-01 | [Modelpedia: A Catalog of Model Findings for the Meta-Science of AI](https://arxiv.org/abs/2609.01090v2) | 2609.01090v2 | 8 |
| 2026-09-01 | [Efficiently Estimating Optimal Hyperparameter Scaling Laws through Power-Law Entropy Search](https://arxiv.org/abs/2609.01431v3) | 2609.01431v3 | 9 |
| 2026-09-01 | [SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers](https://arxiv.org/abs/2609.01343v3) | 2609.01343v3 | 7 |
| 2026-08-31 | [When LLM Meets Tree Search: A Systematic View of Inference as Search in Large Language Models](https://arxiv.org/abs/2608.30395v1) | 2608.30395v1 | 9 |
| 2026-08-27 | [Scaling Neural Network Quantum States for Ab Initio Quantum Chemistry](https://arxiv.org/abs/2609.02929v1) | 2609.02929v1 | 7 |
| 2026-08-25 | [Effective Learning Rate Governs Loss Dynamics in Language Model Pretraining](https://arxiv.org/abs/2608.24814v1) | 2608.24814v1 | 7 |
| 2026-08-24 | [MLLM-Assisted Audio VOS: A 3rd Place Report for the MeViS-Audio Track, 8th LSVOS Challenge](https://arxiv.org/abs/2608.23234v1) | 2608.23234v1 | 10 |
| 2026-08-23 | [Linear RNN Scaling Laws: When Longer Sequences Beat More Sequences](https://arxiv.org/abs/2609.27964v2) | 2609.27964v2 | 8 |
| 2026-08-05 | [The First EgoCross Challenge at EgoVis 2026: Cross-Domain Egocentric Video Question Answering](https://arxiv.org/abs/2608.04589v1) | 2608.04589v1 | 7 |
| 2026-08-05 | [K-EXAONE 2.0 Technical Report](https://arxiv.org/abs/2608.04505v1) | 2608.04505v1 | 10 |
| 2026-08-04 | [EXAONE Finance 1.0: An Attention-free Time Series Foundation Model for Financial Time Series](https://arxiv.org/abs/2609.04239v2) | 2609.04239v2 | 13 |
| 2026-08-03 | [Scaling an Autoregressive Transformer for Single-Cell Generation](https://arxiv.org/abs/2608.02961v2) | 2608.02961v2 | 10 |
| 2026-08-03 | [Generative AI and Foundation Models in Medical Image](https://arxiv.org/abs/2608.01686v1) | 2608.01686v1 | 12 |
| 2026-07-30 | [Towards joint scaling laws with optimal batch size schedules](https://arxiv.org/abs/2607.27731v1) | 2607.27731v1 | 8 |
| 2026-07-28 | [Bridging Compute- and Data-Optimal Pretraining](https://arxiv.org/abs/2607.25271v1) | 2607.25271v1 | 7 |
| 2026-07-28 | [A scaling law of contextual persistence in human language](https://arxiv.org/abs/2607.25184v1) | 2607.25184v1 | 8 |
| 2026-07-25 | [Predict before you train: Scaling Laws for particle physics foundation models](https://arxiv.org/abs/2607.23377v2) | 2607.23377v2 | 17 |
| 2026-07-25 | [The Curse of Precision: A Data Scaling Law for High-Precision Robotic Manipulation](https://arxiv.org/abs/2607.23108v1) | 2607.23108v1 | 7 |
| 2026-07-24 | [Multi-Agent Debate and Visual Information Extraction for SeePhys Pro: A 1st-Place Technical Report from ICML 2026 AI4Math Track 3 Challenge](https://arxiv.org/abs/2607.21946v1) | 2607.21946v1 | 8 |
| 2026-07-24 | [DomainPilot: Domain-Level Loss-Guided Two-Stage Data Mixture Optimization for Efficient Language Model Fine-Tuning](https://arxiv.org/abs/2607.22769v1) | 2607.22769v1 | 8 |
| 2026-07-21 | [Scaling Laws for Hypernetwork-Based Knowledge Injection in Large Language Models](https://arxiv.org/abs/2607.19604v1) | 2607.19604v1 | 9 |
| 2026-07-20 | [PGN: Design and Implementation of a Vision-Language Navigation System Based on Pangu Multimodal Foundation Model](https://arxiv.org/abs/2607.17806v1) | 2607.17806v1 | 12 |
| 2026-07-13 | [Domain-Aware Scaling Laws Uncover Data Synergy](https://arxiv.org/abs/2607.11052v1) | 2607.11052v1 | 9 |
| 2026-07-08 | [Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report](https://arxiv.org/abs/2607.07370v2) | 2607.07370v2 | 10 |
| 2026-07-06 | [EdgeBench: Unveiling Scaling Laws of Learning from Real-World Environments](https://arxiv.org/abs/2607.05155v1) | 2607.05155v1 | 8 |
| 2026-07-05 | [Lights, Camera, Carbon: Architectural Scaling Laws for Video Generation Energy Consumption](https://arxiv.org/abs/2607.04553v1) | 2607.04553v1 | 7 |
| 2026-07-02 | [Will Scaling Improve Social Simulation with LLMs?](https://arxiv.org/abs/2607.02464v2) | 2607.02464v2 | 7 |
| 2026-07-02 | [Alternative routes to universal diversity scaling in component systems: from proteomes to large language models](https://arxiv.org/abs/2607.02221v1) | 2607.02221v1 | 8 |
| 2026-07-01 | [Scaling Laws for Collapse in Asynchronous GRPO](https://arxiv.org/abs/2607.01083v3) | 2607.01083v3 | 8 |
| 2026-06-24 | [What Transfers from Text to Vision? Capability Scaling Laws and Transfer Dynamics for VLMs](https://arxiv.org/abs/2608.00013v5) | 2608.00013v5 | 9 |
| 2026-06-23 | [Can Scale Save Us From Plasticity Loss in Large Language Models?](https://arxiv.org/abs/2606.24752v1) | 2606.24752v1 | 7 |
| 2026-06-23 | [Scaling Laws for Task-Specific LLM Distillation](https://arxiv.org/abs/2606.24747v2) | 2606.24747v2 | 9 |
| 2026-06-22 | [The Origins of Stochasticity: Comprehensive Investigations on Uncertainty Quantification for Large Language Models](https://arxiv.org/abs/2606.22792v1) | 2606.22792v1 | 8 |
| 2026-06-20 | [On the Expressive Power of Weight Quantization in Large Language Models](https://arxiv.org/abs/2606.22249v1) | 2606.22249v1 | 7 |
| 2026-06-20 | [L20-Edu-135M: An Auditable Single-GPU Study of Data-Efficient Small Language Modeling](https://arxiv.org/abs/2606.22189v1) | 2606.22189v1 | 7 |
| 2026-06-18 | [Towards Engineering Scaling Laws with Pretraining Data Composition](https://arxiv.org/abs/2606.19781v2) | 2606.19781v2 | 11 |
| 2026-06-05 | [Data-Constrained Language Model Pretraining: Improved Regularization and Scaling Laws](https://arxiv.org/abs/2606.06888v2) | 2606.06888v2 | 9 |
| 2026-06-04 | [Compute-Optimal Network Design for Echocardiography Myocardial Segmentation and Perfusion Quantification using Neural Scaling Laws](https://arxiv.org/abs/2606.06725v1) | 2606.06725v1 | 8 |
| 2026-06-04 | [Predictable Scaling Laws of Optimal Hyperparameters for LLM Continued Pre-training](https://arxiv.org/abs/2606.05610v1) | 2606.05610v1 | 8 |
| 2026-06-03 | [Scaling Laws for Behavioral Foundation Models over User Event Sequences](https://arxiv.org/abs/2606.05257v1) | 2606.05257v1 | 12 |
| 2026-06-03 | [Validity Threats for Foundation Model Research](https://arxiv.org/abs/2606.05029v1) | 2606.05029v1 | 10 |
| 2026-06-02 | [Where Do Large Language Models Fail on Competitive Programming? A Taxonomy of Failures by Algorithm Type and Difficulty Rating](https://arxiv.org/abs/2606.05228v1) | 2606.05228v1 | 8 |
| 2026-06-01 | [SoulX-Transcriber: A Robust End-to-End Framework for Multi-Speaker Speech Transcription](https://arxiv.org/abs/2606.02400v2) | 2606.02400v2 | 7 |
| 2026-06-01 | [Scaling Laws for Neural-Network Quantum States](https://arxiv.org/abs/2606.02794v1) | 2606.02794v1 | 7 |
| 2026-05-30 | [OmniEEG-Bench: A Standardized Evaluation Benchmark for EEG Foundation Models](https://arxiv.org/abs/2606.00815v1) | 2606.00815v1 | 9 |
| 2026-05-29 | [Item Response Scaling Laws: A Measurement Theory Approach for Efficient and Generalizable Neural Scaling Estimation](https://arxiv.org/abs/2606.07616v1) | 2606.07616v1 | 7 |
| 2026-05-29 | [Spectral Reach: Understanding Neural Scaling as Progress into the Spectral Tail](https://arxiv.org/abs/2605.31244v2) | 2605.31244v2 | 8 |
| 2026-05-28 | [WF-Bench: A Benchmark for Neural Network WaveFunction Expressivity and Scaling Laws](https://arxiv.org/abs/2605.29683v2) | 2605.29683v2 | 7 |
| 2026-05-28 | [LoopFM: Learning frOm HistOrical RePresentations of Foundation Model for Recommendation](https://arxiv.org/abs/2605.29280v3) | 2605.29280v3 | 11 |
| 2026-05-27 | [Neural Scaling Laws for Jet Generation](https://arxiv.org/abs/2605.28940v2) | 2605.28940v2 | 10 |
| 2026-05-27 | [SuperValid: Capability-Aligned OOD Validation for Generalizable Downstream Scaling](https://arxiv.org/abs/2605.28179v2) | 2605.28179v2 | 7 |
| 2026-05-27 | [The Model Shape Behind Scaling Laws: A Gradient Superposition Perspective](https://arxiv.org/abs/2605.27989v2) | 2605.27989v2 | 8 |
| 2026-05-25 | [How Should LLMs Consume High-Quality Data? Optimal Data Scheduling via Quality-Aware Functional Scaling Laws](https://arxiv.org/abs/2605.25698v2) | 2605.25698v2 | 9 |
| 2026-05-22 | [LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws](https://arxiv.org/abs/2605.23901v1) | 2605.23901v1 | 8 |
| 2026-05-21 | [ChronoVAE-HOPE: Beyond Attention -- A Next-Generation VAE Foundation Model for Specialized Time Series Classification](https://arxiv.org/abs/2605.22684v2) | 2605.22684v2 | 11 |
| 2026-05-18 | [KairosHope: A Next-Generation Time-Series Foundation Model for Specialized Classification via Dual-Memory Architecture](https://arxiv.org/abs/2605.18657v2) | 2605.18657v2 | 11 |
| 2026-05-17 | [How Do Electrocardiogram Models Scale?](https://arxiv.org/abs/2605.17276v1) | 2605.17276v1 | 8 |
| 2026-05-13 | [Venus-DeFakerOne: Unified Fake Image Detection & Localization](https://arxiv.org/abs/2605.14091v2) | 2605.14091v2 | 9 |
| 2026-05-13 | [AttenA+: Rectifying Action Inequality in Robotic Foundation Models](https://arxiv.org/abs/2605.13548v3) | 2605.13548v3 | 11 |
| 2026-05-12 | [Scaling Laws for Mixture Pretraining Under Data Constraints](https://arxiv.org/abs/2605.12715v2) | 2605.12715v2 | 9 |
| 2026-05-12 | [Scaling Laws and Tradeoffs in Recurrent Networks of Expressive Neurons](https://arxiv.org/abs/2605.12049v2) | 2605.12049v2 | 7 |
| 2026-05-09 | [Practical Scaling Laws: Converting Compute into Performance in a Data-Constrained World](https://arxiv.org/abs/2605.09189v2) | 2605.09189v2 | 8 |
| 2026-05-08 | [How Big Should a Wireless Foundation Model Be?](https://arxiv.org/abs/2605.07266v1) | 2605.07266v1 | 10 |
| 2026-05-07 | [An Interpretable and Scalable Framework for Evaluating Large Language Models](https://arxiv.org/abs/2605.07046v1) | 2605.07046v1 | 8 |
| 2026-05-07 | [Knowledge Transfer Scaling Laws for 3D Medical Imaging](https://arxiv.org/abs/2605.06859v1) | 2605.06859v1 | 12 |
| 2026-05-07 | [Causal Probing for Internal Visual Representations in Multimodal Large Language Models](https://arxiv.org/abs/2605.05593v3) | 2605.05593v3 | 7 |
| 2026-05-06 | [Retrieval Mechanisms Surpass Long-Context Scaling in Time Series Forecasting](https://arxiv.org/abs/2605.08217v1) | 2605.08217v1 | 9 |
| 2026-05-04 | [InfoLaw: Information Scaling Laws for Large Language Models with Quality-Weighted Mixture Data and Repetition](https://arxiv.org/abs/2605.02364v1) | 2605.02364v1 | 11 |
| 2026-05-03 | [Finite-Size Gradient Transport in Large Language Model Pretraining: From Cascade Size to Intensive Transport Efficiency](https://arxiv.org/abs/2605.02968v1) | 2605.02968v1 | 10 |
| 2026-05-02 | [Prescriptive Scaling Laws for Data Constrained Training](https://arxiv.org/abs/2605.01640v2) | 2605.01640v2 | 8 |
| 2026-04-27 | [A Limit Theory of Foundation Models: A Mathematical Approach to Understanding Emergent Intelligence and Scaling Laws](https://arxiv.org/abs/2604.24037v4) | 2604.24037v4 | 13 |
| 2026-04-24 | [Spend Less, Fit Better: Budget-Efficient Scaling Law Fitting via Active Experiment Selection](https://arxiv.org/abs/2604.22753v2) | 2604.22753v2 | 7 |
| 2026-04-24 | [A Nationwide Japanese Medical Claims Foundation Model: Balancing Model Scaling and Task-Specific Computational Efficiency](https://arxiv.org/abs/2604.22348v1) | 2604.22348v1 | 12 |
| 2026-04-22 | [How Much Is One Recurrence Worth? Iso-Depth Scaling Laws for Looped Language Models](https://arxiv.org/abs/2604.21106v4) | 2604.21106v4 | 8 |
| 2026-04-14 | [Open dataset for benchmarking scaling laws of high-energy laser atmospheric propagation](https://arxiv.org/abs/2604.12604v2) | 2604.12604v2 | 7 |
| 2026-04-13 | [SOLARIS: Speculative Offloading of Latent-bAsed Representation for Inference Scaling](https://arxiv.org/abs/2604.12110v2) | 2604.12110v2 | 8 |
| 2026-04-09 | [What do Language Models Learn and When? The Implicit Curriculum Hypothesis](https://arxiv.org/abs/2604.08510v1) | 2604.08510v1 | 8 |
| 2026-04-08 | [Geometric Properties of the Voronoi Tessellation in Latent Semantic Manifolds of Large Language Models](https://arxiv.org/abs/2604.06767v1) | 2604.06767v1 | 8 |
| 2026-04-02 | [Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning](https://arxiv.org/abs/2604.02322v1) | 2604.02322v1 | 10 |
| 2026-04-02 | [Generalization Bounds and Statistical Guarantees for Multi-Task and Multiple Operator Learning with MNO Networks](https://arxiv.org/abs/2604.01961v1) | 2604.01961v1 | 8 |
| 2026-03-26 | [On Neural Scaling Laws for Weather Emulation through Continual Training](https://arxiv.org/abs/2603.25687v1) | 2603.25687v1 | 10 |
| 2026-03-25 | [When Is Collective Intelligence a Lottery? Multi-Agent Scaling Laws for Memetic Drift in LLMs](https://arxiv.org/abs/2603.24676v1) | 2603.24676v1 | 8 |
| 2026-03-19 | [Optimal Splitting of Language Models from Mixtures to Specialized Domains](https://arxiv.org/abs/2603.19149v1) | 2603.19149v1 | 7 |
| 2026-03-18 | [MOSS-TTS Technical Report](https://arxiv.org/abs/2603.18090v2) | 2603.18090v2 | 12 |
| 2026-03-18 | [ShapleyLaw: A Game-Theoretic Approach to Multilingual Scaling Laws](https://arxiv.org/abs/2603.17945v3) | 2603.17945v3 | 8 |
| 2026-03-17 | [Latent Semantic Manifolds in Large Language Models](https://arxiv.org/abs/2603.22301v1) | 2603.22301v1 | 7 |
| 2026-03-14 | [JointFM-0.1: A Foundation Model for Multi-Target Joint Distributional Prediction](https://arxiv.org/abs/2603.20266v2) | 2603.20266v2 | 10 |
| 2026-03-12 | [Scaling Laws for Educational AI Agents](https://arxiv.org/abs/2603.11709v1) | 2603.11709v1 | 8 |
| 2026-03-11 | [Jailbreak Scaling Laws for Large Language Models: Polynomial-Exponential Crossover](https://arxiv.org/abs/2603.11331v4) | 2603.11331v4 | 10 |
| 2026-03-11 | [Systematic Scaling Analysis of Jailbreak Attacks in Large Language Models](https://arxiv.org/abs/2603.11149v2) | 2603.11149v2 | 7 |
| 2026-03-09 | [Capacity-Aware Mixture Law Enables Efficient LLM Data Optimization](https://arxiv.org/abs/2603.08022v2) | 2603.08022v2 | 7 |
| 2026-03-07 | [Scaling Laws in the Tiny Regime: How Small Models Change Their Mistakes](https://arxiv.org/abs/2603.07365v1) | 2603.07365v1 | 8 |
| 2026-03-05 | [Revisiting Shape from Polarization in the Era of Vision Foundation Models](https://arxiv.org/abs/2603.04817v1) | 2603.04817v1 | 10 |
| 2026-03-03 | [Beyond Language Modeling: An Exploration of Multimodal Pretraining](https://arxiv.org/abs/2603.03276v1) | 2603.03276v1 | 11 |
| 2026-02-28 | [Multi-Domain Riemannian Graph Gluing for Building Graph Foundation Models](https://arxiv.org/abs/2603.00618v1) | 2603.00618v1 | 10 |
| 2026-02-26 | [Distributed LLM Pretraining During Renewable Curtailment Windows: A Feasibility Study](https://arxiv.org/abs/2602.22760v1) | 2602.22760v1 | 9 |
| 2026-02-26 | [Agentic Exploration of PDE Spaces using Latent Foundation Models for Parameterized Simulations](https://arxiv.org/abs/2604.09584v1) | 2604.09584v1 | 12 |
| 2026-02-19 | [Bigger Is Safer: Provable Robustness in In-Context Learning Scales with Capacity](https://arxiv.org/abs/2602.17743v2) | 2602.17743v2 | 8 |
| 2026-02-19 | [Bending the Scaling Law Curve in Large-Scale Recommendation Systems](https://arxiv.org/abs/2602.16986v2) | 2602.16986v2 | 9 |
| 2026-02-18 | [AdaptOrch: Task-Adaptive Multi-Agent Orchestration in the Era of LLM Performance Convergence](https://arxiv.org/abs/2602.16873v1) | 2602.16873v1 | 7 |
| 2026-02-18 | [Scaling Open Discrete Audio Foundation Models with Interleaved Semantic, Acoustic, and Text Tokens](https://arxiv.org/abs/2602.16687v1) | 2602.16687v1 | 10 |
| 2026-02-17 | [Neural Scaling Laws for Boosted Jet Tagging](https://arxiv.org/abs/2602.15781v1) | 2602.15781v1 | 12 |
| 2026-02-17 | [Quantifying construct validity in large language model evaluations](https://arxiv.org/abs/2602.15532v1) | 2602.15532v1 | 8 |
| 2026-02-16 | [Frontier AI Risk Management Framework in Practice: A Risk Analysis Technical Report v1.5](https://arxiv.org/abs/2602.14457v1) | 2602.14457v1 | 9 |
| 2026-02-16 | [Scaling Laws for Masked-Reconstruction Transformers on Single-Cell Transcriptomics](https://arxiv.org/abs/2602.15253v2) | 2602.15253v2 | 10 |
| 2026-02-15 | [Fast Catch-Up, Late Switching: Optimal Batch Size Scheduling via Functional Scaling Laws](https://arxiv.org/abs/2602.14208v2) | 2602.14208v2 | 10 |
| 2026-02-14 | [sleep2vec: Unified Cross-Modal Alignment for Heterogeneous Nocturnal Biosignals](https://arxiv.org/abs/2602.13857v1) | 2602.13857v1 | 8 |
| 2026-02-12 | [Benchmark Health Index: A Systematic Framework for Benchmarking the Benchmarks of LLMs](https://arxiv.org/abs/2602.11674v2) | 2602.11674v2 | 7 |
| 2026-02-12 | [Stabilizing Native Low-Rank LLM Pretraining](https://arxiv.org/abs/2602.12429v2) | 2602.12429v2 | 13 |
| 2026-02-11 | [Weight Decay Improves Language Model Plasticity](https://arxiv.org/abs/2602.11137v2) | 2602.11137v2 | 8 |
| 2026-02-10 | [Hardware Co-Design Scaling Laws via Roofline Modelling for On-Device LLMs](https://arxiv.org/abs/2602.10377v1) | 2602.10377v1 | 8 |
| 2026-02-10 | [Configuration-to-Performance Scaling Law with Neural Ansatz](https://arxiv.org/abs/2602.10300v1) | 2602.10300v1 | 10 |
| 2026-02-10 | [Kunlun: Establishing Scaling Laws for Massive-Scale Recommendation Systems through Unified Architecture Design](https://arxiv.org/abs/2602.10016v3) | 2602.10016v3 | 8 |
| 2026-02-10 | [EVA: Towards a universal model of the immune system](https://arxiv.org/abs/2602.10168v2) | 2602.10168v2 | 11 |
| 2026-02-08 | [MedCoG: Maximizing LLM Inference Density in Medical Reasoning via Meta-Cognitive Regulation](https://arxiv.org/abs/2602.07905v2) | 2602.07905v2 | 7 |
| 2026-02-08 | [MARTI-MARS$^2$: Scaling Multi-Agent Self-Search via Reinforcement Learning for Code Generation](https://arxiv.org/abs/2602.07848v1) | 2602.07848v1 | 7 |
| 2026-02-07 | [Towards Robust Scaling Laws for Optimizers](https://arxiv.org/abs/2602.07712v2) | 2602.07712v2 | 10 |
| 2026-02-07 | [Deriving Neural Scaling Laws from the statistics of natural language](https://arxiv.org/abs/2602.07488v3) | 2602.07488v3 | 7 |
| 2026-02-07 | [Principled Synthetic Data Enables the First Scaling Laws for LLMs in Recommendation](https://arxiv.org/abs/2602.07298v3) | 2602.07298v3 | 8 |
| 2026-02-04 | [Billion-Scale Graph Foundation Models](https://arxiv.org/abs/2602.04768v2) | 2602.04768v2 | 12 |
| 2026-02-02 | [Performance of Small Language Model Pretraining on FABRIC: An Empirical Study](https://arxiv.org/abs/2602.02632v1) | 2602.02632v1 | 9 |
| 2026-02-01 | [Predicting and improving test-time scaling laws via reward tail-guided search](https://arxiv.org/abs/2602.01485v1) | 2602.01485v1 | 8 |
| 2026-02-01 | [Probing the Knowledge Boundary: An Interactive Agentic Framework for Deep Knowledge Extraction](https://arxiv.org/abs/2602.00959v2) | 2602.00959v2 | 9 |
| 2026-01-31 | [Hessian Spectral Analysis at Foundation Model Scale](https://arxiv.org/abs/2602.00816v1) | 2602.00816v1 | 10 |
| 2026-01-30 | [Beyond the Loss Curve: Scaling Laws, Active Learning, and the Limits of Learning from Exact Posteriors](https://arxiv.org/abs/2602.00315v2) | 2602.00315v2 | 7 |
| 2026-01-30 | [Quantifying Model Uniqueness in Heterogeneous AI Ecosystems](https://arxiv.org/abs/2601.22977v2) | 2601.22977v2 | 10 |
| 2026-01-30 | [How Much of a Model Do We Need? Redundancy and Slimmability in Remote Sensing Foundation Models](https://arxiv.org/abs/2601.22841v2) | 2601.22841v2 | 12 |
| 2026-01-30 | [Statistical Estimation of Adversarial Risk in Large Language Models under Best-of-N Sampling](https://arxiv.org/abs/2601.22636v2) | 2601.22636v2 | 7 |
| 2026-01-29 | [MetricAnything: Scaling Metric Depth Pretraining with Noisy Heterogeneous Sources](https://arxiv.org/abs/2601.22054v2) | 2601.22054v2 | 13 |
| 2026-01-25 | [Scaling Laws for Moral Machine Judgment in Large Language Models](https://arxiv.org/abs/2601.17637v3) | 2601.17637v3 | 9 |
| 2026-01-24 | [Diversified Scaling Inference in Time Series Foundation Models](https://arxiv.org/abs/2601.17376v1) | 2601.17376v1 | 10 |
| 2026-01-21 | [A Contrastive Pre-trained Foundation Model for Deciphering Imaging Noisomics across Modalities](https://arxiv.org/abs/2601.17047v1) | 2601.17047v1 | 11 |
| 2026-01-19 | [The Geometry of Thought: How Scale Restructures Reasoning In Large Language Models](https://arxiv.org/abs/2601.13358v2) | 2601.13358v2 | 7 |
| 2026-01-15 | [DecisionLLM: Large Language Models for Long Sequence Decision Exploration](https://arxiv.org/abs/2601.10148v1) | 2601.10148v1 | 8 |
| 2026-01-14 | [A.X K1 Technical Report](https://arxiv.org/abs/2601.09200v5) | 2601.09200v5 | 11 |
| 2026-01-13 | [KidVis: Do Multimodal Large Language Models Possess the Visual Perceptual Capabilities of a 6-Year-Old?](https://arxiv.org/abs/2601.08292v1) | 2601.08292v1 | 8 |
| 2026-01-08 | [PROMISE: Process Reward Models Unlock Test-Time Scaling Laws in Generative Recommendations](https://arxiv.org/abs/2601.04674v1) | 2601.04674v1 | 8 |
| 2026-01-08 | [Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing](https://arxiv.org/abs/2601.04575v2) | 2601.04575v2 | 8 |
| 2026-01-07 | [Quantifying the Effect of Test Set Contamination on Generative Evaluations](https://arxiv.org/abs/2601.04301v3) | 2601.04301v3 | 7 |
| 2026-01-05 | [K-EXAONE Technical Report](https://arxiv.org/abs/2601.01739v2) | 2601.01739v2 | 11 |
| 2026-01-03 | [From RLHF to Direct Alignment: A Theoretical Unification of Preference Learning for Large Language Models](https://arxiv.org/abs/2601.06108v1) | 2601.06108v1 | 7 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-31 | [Dynamic Large Concept Models: Latent Reasoning in an Adaptive Semantic Space](https://arxiv.org/abs/2512.24617v2) | 2512.24617v2 | 7 |
| 2025-12-30 | [Training Report of TeleChat3-MoE](https://arxiv.org/abs/2512.24157v1) | 2512.24157v1 | 8 |
| 2025-12-29 | [Scaling Remote Sensing Foundation Models: Data Domain Tradeoffs at the Peta-Scale](https://arxiv.org/abs/2512.23903v2) | 2512.23903v2 | 10 |
| 2025-12-29 | [Universal Aging Dynamics and Scaling Laws in Three-Dimensional Driven Granular Gases](https://arxiv.org/abs/2512.23625v1) | 2512.23625v1 | 7 |
| 2025-12-29 | [Theoretical Foundations of Scaling Law in Familial Models](https://arxiv.org/abs/2512.23407v2) | 2512.23407v2 | 8 |
| 2025-12-29 | [The Law of Multi-Model Collaboration: Scaling Limits of Model Ensembling for Large Language Models](https://arxiv.org/abs/2512.23340v2) | 2512.23340v2 | 7 |
| 2025-12-26 | [Unifying Learning Dynamics and Generalization in Transformers Scaling Law](https://arxiv.org/abs/2512.22088v3) | 2512.22088v3 | 8 |
| 2025-12-25 | [Perplexity-Aware Data Scaling Law: Perplexity Landscapes Predict Performance for Continual Pre-training](https://arxiv.org/abs/2512.21515v1) | 2512.21515v1 | 11 |
| 2025-12-24 | [Scaling Laws for Economic Productivity: Experimental Evidence in LLM-Assisted Consulting, Data Analyst, and Management Tasks](https://arxiv.org/abs/2512.21316v1) | 2512.21316v1 | 8 |
| 2025-12-18 | [Scaling Laws for Energy Efficiency of Local LLMs](https://arxiv.org/abs/2512.16531v4) | 2512.16531v4 | 9 |
| 2025-12-17 | [Uni-Parser Technical Report](https://arxiv.org/abs/2512.15098v4) | 2512.15098v4 | 8 |
| 2025-12-16 | [Ladder Up, Memory Down: Low-Cost Fine-Tuning With Side Nets](https://arxiv.org/abs/2512.14237v2) | 2512.14237v2 | 7 |
| 2025-12-15 | [From Zipf's Law to Neural Scaling through Heaps' Law and Hilberg's Hypothesis](https://arxiv.org/abs/2512.13491v3) | 2512.13491v3 | 10 |
| 2025-12-15 | [Scaling Laws for Code: Every Programming Language Matters](https://arxiv.org/abs/2512.13472v1) | 2512.13472v1 | 8 |
| 2025-12-15 | [Scaling laws for stationary Navier-Stokes-Fourier flows and the unreasonable effectiveness of hydrodynamics at the molecular level](https://arxiv.org/abs/2512.13205v1) | 2512.13205v1 | 7 |
| 2025-12-13 | [The Data Efficiency Frontier of Financial Foundation Models: Scaling Laws from Continued Pretraining](https://arxiv.org/abs/2512.12384v1) | 2512.12384v1 | 17 |
| 2025-12-09 | [Revisiting the Scaling Properties of Downstream Metrics in Large Language Model Training](https://arxiv.org/abs/2512.08894v1) | 2512.08894v1 | 10 |
| 2025-12-08 | [START: Spatial and Textual Learning for Chart Understanding](https://arxiv.org/abs/2512.07186v1) | 2512.07186v1 | 7 |
| 2025-12-06 | [A Latent Variable Framework for Scaling Laws in Large Language Models](https://arxiv.org/abs/2512.06553v2) | 2512.06553v2 | 10 |
| 2025-12-06 | [Nanbeige4-3B Technical Report: Exploring the Frontier of Small Language Models](https://arxiv.org/abs/2512.06266v1) | 2512.06266v1 | 11 |
| 2025-12-04 | [Sequential Enumeration in Large Language Models](https://arxiv.org/abs/2512.04727v2) | 2512.04727v2 | 8 |
| 2025-11-30 | [Silhouette-based Gait Foundation Model](https://arxiv.org/abs/2512.00691v3) | 2512.00691v3 | 12 |
| 2025-11-25 | [Fluid Intelligence: A Forward Look on AI Foundation Models in Computational Fluid Dynamics](https://arxiv.org/abs/2511.20455v1) | 2511.20455v1 | 10 |
| 2025-11-23 | [From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence](https://arxiv.org/abs/2511.18538v5) | 2511.18538v5 | 13 |
| 2025-11-10 | [AIA Forecaster: Technical Report](https://arxiv.org/abs/2511.07678v1) | 2511.07678v1 | 9 |
| 2025-11-09 | [Beyond Correctness: Confidence-Aware Reward Modeling for Enhancing Large Language Model Reasoning](https://arxiv.org/abs/2511.07483v1) | 2511.07483v1 | 8 |
| 2025-11-09 | [Scaling Laws and In-Context Learning: A Unified Theoretical Framework](https://arxiv.org/abs/2511.06232v1) | 2511.06232v1 | 8 |
| 2025-10-31 | [Diffuse Thinking: Exploring Diffusion Language Models as Efficient Thought Proposers for Reasoning](https://arxiv.org/abs/2510.27469v1) | 2510.27469v1 | 7 |
| 2025-10-31 | [A Survey on Generative Recommendation: Data, Model, and Tasks](https://arxiv.org/abs/2510.27157v2) | 2510.27157v2 | 7 |
| 2025-10-30 | [Entanglement and Dynamical Scaling Laws in Quantum Superabsorption](https://arxiv.org/abs/2510.26373v2) | 2510.26373v2 | 7 |
| 2025-10-28 | [Relative Scaling Laws for LLMs](https://arxiv.org/abs/2510.24626v2) | 2510.24626v2 | 8 |
| 2025-10-28 | [MiniOneRec: An Open-Source Framework for Scaling Generative Recommendation](https://arxiv.org/abs/2510.24431v1) | 2510.24431v1 | 7 |
| 2025-10-24 | [ATLAS: Adaptive Transfer Scaling Laws for Multilingual Pretraining, Finetuning, and Decoding the Curse of Multilinguality](https://arxiv.org/abs/2510.22037v2) | 2510.22037v2 | 9 |
| 2025-10-23 | [Relative-Based Scaling Law for Neural Language Models](https://arxiv.org/abs/2510.20387v1) | 2510.20387v1 | 8 |
| 2025-10-22 | [ColorAgent: Building A Robust, Personalized, and Interactive OS Agent](https://arxiv.org/abs/2510.19386v2) | 2510.19386v2 | 7 |
| 2025-10-21 | [KAT-Coder Technical Report](https://arxiv.org/abs/2510.18779v3) | 2510.18779v3 | 8 |
| 2025-10-21 | [Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs](https://arxiv.org/abs/2510.18245v3) | 2510.18245v3 | 8 |
| 2025-10-20 | [Foundation Models for Discovery and Exploration in Chemical Space](https://arxiv.org/abs/2510.18900v2) | 2510.18900v2 | 11 |
| 2025-10-18 | [NP-Engine: Empowering Optimization Reasoning in Large Language Models with Verifiable Synthetic NP Problems](https://arxiv.org/abs/2510.16476v1) | 2510.16476v1 | 8 |
| 2025-10-18 | [Scaling Laws for Deepfake Detection](https://arxiv.org/abs/2510.16320v2) | 2510.16320v2 | 8 |
| 2025-10-16 | [Predicting Task Performance with Context-aware Scaling Laws](https://arxiv.org/abs/2510.14919v1) | 2510.14919v1 | 8 |
| 2025-10-14 | [DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving](https://arxiv.org/abs/2510.12796v2) | 2510.12796v2 | 7 |
| 2025-10-13 | [Scaling Language-Centric Omnimodal Representation Learning](https://arxiv.org/abs/2510.11693v1) | 2510.11693v1 | 9 |
| 2025-10-13 | [Unify Variables in Neural Scaling Laws for General Audio Representations via Embedding Effective Rank](https://arxiv.org/abs/2510.10948v1) | 2510.10948v1 | 10 |
| 2025-10-10 | [All Code, No Thought: Current Language Models Struggle to Reason in Ciphered Language](https://arxiv.org/abs/2510.09714v2) | 2510.09714v2 | 8 |
| 2025-10-10 | [Scaling Law in LLM Simulated Personality: More Detailed and Realistic Persona Profile Is All You Need](https://arxiv.org/abs/2510.11734v1) | 2510.11734v1 | 8 |
| 2025-10-09 | [Scaling Laws for Code: A More Data-Hungry Regime](https://arxiv.org/abs/2510.08702v2) | 2510.08702v2 | 8 |
| 2025-10-09 | [Single layer tiny Co$^4$ outpaces GPT-2 and GPT-BERT](https://arxiv.org/abs/2510.08404v1) | 2510.08404v1 | 7 |
| 2025-10-05 | [What Scales in Cross-Entropy Scaling Law?](https://arxiv.org/abs/2510.04067v2) | 2510.04067v2 | 8 |
| 2025-10-02 | [xLSTM Scaling Laws: Competitive Performance with Linear Time-Complexity](https://arxiv.org/abs/2510.02228v2) | 2510.02228v2 | 8 |
| 2025-10-02 | [Demystifying Synthetic Data in LLM Pre-training: A Systematic Study of Scaling Laws, Benefits, and Pitfalls](https://arxiv.org/abs/2510.01631v1) | 2510.01631v1 | 8 |
| 2025-10-01 | [Spectral Scaling Laws in Language Models: How Effectively Do Feed-Forward Networks Use Their Latent Space?](https://arxiv.org/abs/2510.00537v1) | 2510.00537v1 | 8 |
| 2025-09-30 | [Scaling Laws Revisited: Modeling the Role of Data Quality in Language Model Pretraining](https://arxiv.org/abs/2510.03313v2) | 2510.03313v2 | 9 |
| 2025-09-30 | [Are neural scaling laws leading quantum chemistry astray?](https://arxiv.org/abs/2509.26397v1) | 2509.26397v1 | 10 |
| 2025-09-30 | [CAST: Continuous and Differentiable Semi-Structured Sparsity-Aware Training for Large Language Models](https://arxiv.org/abs/2509.25996v1) | 2509.25996v1 | 9 |
| 2025-09-29 | [Understanding Generative Recommendation with Semantic IDs from a Model-scaling View](https://arxiv.org/abs/2509.25522v3) | 2509.25522v3 | 10 |
| 2025-09-29 | [Model Merging Scaling Laws in Large Language Models](https://arxiv.org/abs/2509.24244v4) | 2509.24244v4 | 9 |
| 2025-09-28 | [Pretraining Scaling Laws for Generative Evaluations of Language Models](https://arxiv.org/abs/2509.24012v2) | 2509.24012v2 | 10 |
| 2025-09-28 | [Contrastive Learning Enhances Language Model Based Cell Embeddings for Low-Sample Single Cell Transcriptomics](https://arxiv.org/abs/2509.23543v1) | 2509.23543v1 | 10 |
| 2025-09-25 | [VC-Agent: An Interactive Agent for Customized Video Dataset Collection](https://arxiv.org/abs/2509.21291v1) | 2509.21291v1 | 7 |
| 2025-09-24 | [CyberSOCEval: Benchmarking LLMs Capabilities for Malware Analysis and Threat Intelligence Reasoning](https://arxiv.org/abs/2509.20166v2) | 2509.20166v2 | 7 |
| 2025-09-23 | [Functional Scaling Laws in Kernel Regression: Loss Dynamics and Learning Rate Schedules](https://arxiv.org/abs/2509.19189v4) | 2509.19189v4 | 8 |
| 2025-09-21 | [seqBench: A Tunable Benchmark to Quantify Sequential Reasoning Limits of LLMs](https://arxiv.org/abs/2509.16866v1) | 2509.16866v1 | 7 |
| 2025-09-19 | [How to inject knowledge efficiently? Knowledge Infusion Scaling Law for Pre-training Large Language Models](https://arxiv.org/abs/2509.19371v1) | 2509.19371v1 | 12 |
| 2025-09-16 | [Large Language Model Scaling Laws for Neural Quantum States in Quantum Chemistry](https://arxiv.org/abs/2509.12679v1) | 2509.12679v1 | 9 |
| 2025-09-12 | [Neural Scaling Laws for Deep Regression](https://arxiv.org/abs/2509.10000v2) | 2509.10000v2 | 8 |
| 2025-09-11 | [LLM Architecture, Scaling Laws, and Economics: A Quick Summary](https://arxiv.org/abs/2511.11572v1) | 2511.11572v1 | 8 |
| 2025-09-10 | [Two Facets of the Same Optimization Coin: Model Degradation and Representation Collapse in Graph Foundation Models](https://arxiv.org/abs/2509.08401v4) | 2509.08401v4 | 10 |
| 2025-09-10 | [Evaluation Awareness Scales Predictably in Open-Weights Large Language Models](https://arxiv.org/abs/2509.13333v2) | 2509.13333v2 | 7 |
| 2025-09-09 | [Uncovering Scaling Laws for Large Language Models via Inverse Problems](https://arxiv.org/abs/2509.07909v1) | 2509.07909v1 | 9 |
| 2025-09-09 | [Video Parallel Scaling: Aggregating Diverse Frame Subsets for VideoLLMs](https://arxiv.org/abs/2509.08016v2) | 2509.08016v2 | 7 |
| 2025-09-08 | [MachineLearningLM: Scaling Many-shot In-context Learning via Continued Pretraining](https://arxiv.org/abs/2509.06806v6) | 2509.06806v6 | 9 |
| 2025-09-08 | [Does DINOv3 Set a New Medical Vision Standard? Benchmarking 2D and 3D Classification, Segmentation, and Registration](https://arxiv.org/abs/2509.06467v3) | 2509.06467v3 | 9 |
| 2025-09-08 | [Text-Trained LLMs Can Zero-Shot Extrapolate PDE Dynamics, Revealing a Three-Stage In-Context Learning Mechanism](https://arxiv.org/abs/2509.06322v3) | 2509.06322v3 | 11 |
| 2025-09-05 | [Scaling Law for Large-Scale Pre-Training Using Chaotic Time Series and Predictability in Financial Time Series](https://arxiv.org/abs/2509.04921v1) | 2509.04921v1 | 10 |
| 2025-09-03 | [LimiX: Unleashing Structured-Data Modeling Capability for Generalist Intelligence](https://arxiv.org/abs/2509.03505v2) | 2509.03505v2 | 9 |
| 2025-08-28 | [GDS Agent for Graph Algorithmic Reasoning](https://arxiv.org/abs/2508.20637v2) | 2508.20637v2 | 7 |
| 2025-08-26 | [Can Structured Templates Facilitate LLMs in Tackling Harder Tasks? : An Exploration of Scaling Laws by Difficulty](https://arxiv.org/abs/2508.19069v1) | 2508.19069v1 | 9 |
| 2025-08-26 | [Task-Stratified Knowledge Scaling Laws for Post-Training Quantized Large Language Models](https://arxiv.org/abs/2508.18609v4) | 2508.18609v4 | 9 |
| 2025-08-21 | [Waver: Wave Your Way to Lifelike Video Generation](https://arxiv.org/abs/2508.15761v2) | 2508.15761v2 | 8 |
| 2025-08-18 | [Signal and Noise: A Framework for Reducing Uncertainty in Language Model Evaluation](https://arxiv.org/abs/2508.13144v1) | 2508.13144v1 | 7 |
| 2025-08-16 | [Data Mixing Optimization for Supervised Fine-Tuning of Large Language Models](https://arxiv.org/abs/2508.11953v1) | 2508.11953v1 | 7 |
| 2025-08-15 | [Audio Flamingo Sound-CoT Technical Report: Improving Chain-of-Thought Reasoning in Sound Understanding](https://arxiv.org/abs/2508.11818v1) | 2508.11818v1 | 9 |
| 2025-08-15 | [LETToT: Label-Free Evaluation of Large Language Models On Tourism Using Expert Tree-of-Thought](https://arxiv.org/abs/2508.11280v2) | 2508.11280v2 | 8 |
| 2025-08-13 | [DINOv3](https://arxiv.org/abs/2508.10104v1) | 2508.10104v1 | 8 |
| 2025-08-13 | [Beyond Scaling Law: A Data-Efficient Distillation Framework for Reasoning](https://arxiv.org/abs/2508.09883v2) | 2508.09883v2 | 9 |
| 2025-08-08 | [Generalizing Scaling Laws for Dense and Sparse Large Language Models](https://arxiv.org/abs/2508.06617v3) | 2508.06617v3 | 11 |
| 2025-08-06 | [Benchmarking Foundation Models for Mitotic Figure Classification](https://arxiv.org/abs/2508.04441v3) | 2508.04441v3 | 11 |
| 2025-08-06 | [Why are LLMs' abilities emergent?](https://arxiv.org/abs/2508.04401v1) | 2508.04401v1 | 7 |
| 2025-08-06 | [Efficient Scaling for LLM-based ASR](https://arxiv.org/abs/2508.04096v1) | 2508.04096v1 | 8 |
| 2025-08-04 | [Realizing Scaling Laws in Recommender Systems: A Foundation-Expert Paradigm for Hyperscale Model Deployment](https://arxiv.org/abs/2508.02929v3) | 2508.02929v3 | 10 |
| 2025-08-04 | [Infrared Object Detection with Ultra Small ConvNets: Is ImageNet Pretraining Still Useful?](https://arxiv.org/abs/2508.02927v2) | 2508.02927v2 | 7 |
| 2025-08-04 | [CauKer: Classification Time Series Foundation Models Can Be Pretrained on Synthetic Data](https://arxiv.org/abs/2508.02879v3) | 2508.02879v3 | 10 |
| 2025-08-04 | [Neural Scaling Laws Surpass Chemical Accuracy for the Many-Electron Schrödinger Equation](https://arxiv.org/abs/2508.02570v2) | 2508.02570v2 | 7 |
| 2025-08-04 | [AlignGuard-LoRA: Alignment-Preserving Fine-Tuning via Fisher-Guided Decomposition and Riemannian-Geodesic Collision Regularization](https://arxiv.org/abs/2508.02079v1) | 2508.02079v1 | 7 |
| 2025-08-02 | [MeshLLM: Empowering Large Language Models to Progressively Understand and Generate 3D Mesh](https://arxiv.org/abs/2508.01242v2) | 2508.01242v2 | 7 |
| 2025-08-02 | [CarbonScaling: Extending Neural Scaling Laws for Carbon Footprint in Large Language Models](https://arxiv.org/abs/2508.06524v2) | 2508.06524v2 | 9 |
| 2025-07-29 | [Using Scaling Laws for Data Source Utility Estimation in Domain-Specific Pre-Training](https://arxiv.org/abs/2507.22250v1) | 2507.22250v1 | 12 |
| 2025-07-27 | [Can Language Models Discover Scaling Laws?](https://arxiv.org/abs/2507.21184v5) | 2507.21184v5 | 8 |
| 2025-07-25 | [The wall confronting large language models](https://arxiv.org/abs/2507.19703v2) | 2507.19703v2 | 7 |
| 2025-07-24 | [Predictive Scaling Laws for Efficient GRPO Training of Large Reasoning Models](https://arxiv.org/abs/2507.18014v3) | 2507.18014v3 | 8 |
| 2025-07-23 | [CartoonAlive: Towards Expressive Live2D Modeling from Single Portraits](https://arxiv.org/abs/2507.17327v1) | 2507.17327v1 | 8 |
| 2025-07-21 | [Solving Formal Math Problems by Decomposition and Iterative Reflection](https://arxiv.org/abs/2507.15225v1) | 2507.15225v1 | 7 |
| 2025-07-16 | [Language Models Improve When Pretraining Data Matches Target Tasks](https://arxiv.org/abs/2507.12466v1) | 2507.12466v1 | 8 |
| 2025-07-15 | [Towards Depth Foundation Model: Recent Trends in Vision-Based Depth Estimation](https://arxiv.org/abs/2507.11540v2) | 2507.11540v2 | 10 |
| 2025-07-13 | [Sub-Scaling Laws: On the Role of Data Density and Training Strategies in LLMs](https://arxiv.org/abs/2507.10613v1) | 2507.10613v1 | 8 |
| 2025-07-12 | [Scaling Laws for Optimal Data Mixtures](https://arxiv.org/abs/2507.09404v2) | 2507.09404v2 | 14 |
| 2025-07-11 | [AMix-1: A Pathway to Test-Time Scalable Protein Foundation Model](https://arxiv.org/abs/2507.08920v4) | 2507.08920v4 | 13 |
| 2025-07-08 | [PaddleOCR 3.0 Technical Report](https://arxiv.org/abs/2507.05595v1) | 2507.05595v1 | 8 |
| 2025-07-07 | [ICAS: Detecting Training Data from Autoregressive Image Generative Models](https://arxiv.org/abs/2507.05068v2) | 2507.05068v2 | 8 |
| 2025-07-01 | [Scaling Laws Are Unreliable for Downstream Tasks: A Reality Check](https://arxiv.org/abs/2507.00885v2) | 2507.00885v2 | 8 |
| 2025-06-28 | [Spectra 1.1: Scaling Laws and Efficient Inference for Ternary Language Models](https://arxiv.org/abs/2506.23025v1) | 2506.23025v1 | 8 |
| 2025-06-27 | [R1-Track: Direct Application of MLLMs to Visual Object Tracking via Reinforcement Learning](https://arxiv.org/abs/2506.21980v3) | 2506.21980v3 | 7 |
| 2025-06-23 | [From Web Search towards Agentic Deep Research: Incentivizing Search with Reasoning Agents](https://arxiv.org/abs/2506.18959v3) | 2506.18959v3 | 7 |
| 2025-06-18 | [RAS-Eval: A Comprehensive Benchmark for Security Evaluation of LLM Agents in Real-World Environments](https://arxiv.org/abs/2506.15253v1) | 2506.15253v1 | 7 |
| 2025-06-17 | [Scaling Laws for Geospatial Foundation Models: A case study on PhilEO Bench](https://arxiv.org/abs/2506.14765v5) | 2506.14765v5 | 15 |
| 2025-06-16 | [OneRec Technical Report](https://arxiv.org/abs/2506.13695v4) | 2506.13695v4 | 10 |
| 2025-06-16 | [Capability Salience Vector: Fine-grained Alignment of Loss and Capabilities for Downstream Task Scaling Law](https://arxiv.org/abs/2506.13216v1) | 2506.13216v1 | 7 |
| 2025-06-15 | [Humanity's Last Code Exam: Can Advanced LLMs Conquer Human's Hardest Code Competition?](https://arxiv.org/abs/2506.12713v2) | 2506.12713v2 | 7 |
| 2025-06-14 | [Pushing the Limits of Safety: A Technical Report on the ATLAS Challenge 2025](https://arxiv.org/abs/2506.12430v2) | 2506.12430v2 | 9 |
| 2025-06-12 | [Predictable Scale: Part II, Farseer: A Refined Scaling Law in Large Language Models](https://arxiv.org/abs/2506.10972v3) | 2506.10972v3 | 9 |
| 2025-06-10 | [Technical Report for Argoverse2 Scenario Mining Challenges on Iterative Error Correction and Spatially-Aware Prompting](https://arxiv.org/abs/2506.11124v1) | 2506.11124v1 | 8 |
| 2025-06-10 | [A Theory of Inference Compute Scaling: Reasoning through Directed Stochastic Skill Search](https://arxiv.org/abs/2507.00004v2) | 2507.00004v2 | 7 |
| 2025-06-10 | [Improved Scaling Laws in Linear Regression via Data Reuse](https://arxiv.org/abs/2506.08415v2) | 2506.08415v2 | 8 |
| 2025-06-09 | [Scaling Laws of Motion Forecasting and Planning -- Technical Report](https://arxiv.org/abs/2506.08228v2) | 2506.08228v2 | 12 |
| 2025-06-05 | [Recycling the Web: A Method to Enhance Pre-training Data Quality and Quantity for Language Models](https://arxiv.org/abs/2506.04689v3) | 2506.04689v3 | 7 |
| 2025-06-05 | [Scaling Laws for Robust Comparison of Open Foundation Language-Vision Models and Datasets](https://arxiv.org/abs/2506.04598v1) | 2506.04598v1 | 10 |
| 2025-06-02 | [A Graph Neural Network for the Era of Large Atomistic Models](https://arxiv.org/abs/2506.01686v3) | 2506.01686v3 | 9 |
| 2025-06-02 | [Incentivizing LLMs to Self-Verify Their Answers](https://arxiv.org/abs/2506.01369v2) | 2506.01369v2 | 7 |
| 2025-05-29 | [Diversity of Transformer Layers: One Aspect of Parameter Scaling Laws](https://arxiv.org/abs/2505.24009v2) | 2505.24009v2 | 8 |
| 2025-05-29 | [Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning](https://arxiv.org/abs/2505.23195v3) | 2505.23195v3 | 11 |
| 2025-05-29 | [Scalable Complexity Control Facilitates Reasoning Ability of LLMs](https://arxiv.org/abs/2505.23013v1) | 2505.23013v1 | 7 |
| 2025-05-29 | [Exploring Scaling Laws for EHR Foundation Models](https://arxiv.org/abs/2505.22964v2) | 2505.22964v2 | 14 |
| 2025-05-27 | [Leveraging Large Language Models in Visual Speech Recognition: Model Scaling, Context-Aware Decoding, and Iterative Polishing](https://arxiv.org/abs/2506.02012v1) | 2506.02012v1 | 7 |
| 2025-05-23 | [Trinity-RFT: A General-Purpose and Unified Framework for Reinforcement Fine-Tuning of Large Language Models](https://arxiv.org/abs/2505.17826v3) | 2505.17826v3 | 7 |
| 2025-05-23 | [TabSTAR: A Tabular Foundation Model for Tabular Data with Text Fields](https://arxiv.org/abs/2505.18125v2) | 2505.18125v2 | 13 |
| 2025-05-23 | [A Coreset Selection of Coreset Selection Literature: Introduction and Recent Advances](https://arxiv.org/abs/2505.17799v2) | 2505.17799v2 | 8 |
| 2025-05-23 | [BehaveGPT: A Foundation Model for Large-scale User Behavior Modeling](https://arxiv.org/abs/2505.17631v1) | 2505.17631v1 | 12 |
| 2025-05-22 | [How do Scaling Laws Apply to Knowledge Graph Engineering Tasks? The Impact of Model Size on Large Language Model Performance](https://arxiv.org/abs/2505.16276v1) | 2505.16276v1 | 10 |
| 2025-05-21 | [Large Language Models as Computable Approximations to Solomonoff Induction](https://arxiv.org/abs/2505.15784v1) | 2505.15784v1 | 9 |
| 2025-05-20 | [Quartet: Native FP4 Training Can Be Optimal for Large Language Models](https://arxiv.org/abs/2505.14669v4) | 2505.14669v4 | 7 |
| 2025-05-20 | [Scaling Law for Quantization-Aware Training](https://arxiv.org/abs/2505.14302v1) | 2505.14302v1 | 8 |
| 2025-05-19 | [Panda: A pretrained forecast model for chaotic dynamics](https://arxiv.org/abs/2505.13755v3) | 2505.13755v3 | 9 |
| 2025-05-19 | [Seek in the Dark: Reasoning via Test-Time Instance-Level Policy Gradient in Latent Space](https://arxiv.org/abs/2505.13308v3) | 2505.13308v3 | 7 |
| 2025-05-16 | [Context parroting: A simple but tough-to-beat baseline for foundation models in scientific machine learning](https://arxiv.org/abs/2505.11349v3) | 2505.11349v3 | 12 |
| 2025-05-15 | [Neural Thermodynamic Laws for Large Language Model Training](https://arxiv.org/abs/2505.10559v1) | 2505.10559v1 | 7 |
| 2025-05-15 | [Does Scaling Law Apply in Time Series Forecasting?](https://arxiv.org/abs/2505.10172v1) | 2505.10172v1 | 7 |
| 2025-05-12 | [YuLan-OneSim: Towards the Next Generation of Social Simulator with Large Language Models](https://arxiv.org/abs/2505.07581v3) | 2505.07581v3 | 7 |
| 2025-05-12 | [Learning Dynamics in Continual Pre-Training for Large Language Models](https://arxiv.org/abs/2505.07796v2) | 2505.07796v2 | 11 |
| 2025-05-10 | [Model Steering: Learning with a Reference Model Improves Generalization Bounds and Scaling Laws](https://arxiv.org/abs/2505.06699v3) | 2505.06699v3 | 12 |
| 2025-05-09 | [Full-Parameter Continual Pretraining of Gemma2: Insights into Fluency and Domain Knowledge](https://arxiv.org/abs/2505.05946v2) | 2505.05946v2 | 10 |
| 2025-05-09 | [A Scaling Law for Token Efficiency in LLM Fine-Tuning Under Fixed Compute Budgets](https://arxiv.org/abs/2505.06150v2) | 2505.06150v2 | 8 |
| 2025-05-08 | [Scaling Laws for Speculative Decoding](https://arxiv.org/abs/2505.07858v1) | 2505.07858v1 | 10 |
| 2025-04-30 | [COSMOS: Predictable and Cost-Effective Adaptation of LLMs](https://arxiv.org/abs/2505.01449v1) | 2505.01449v1 | 7 |
| 2025-04-28 | [Emergence and scaling laws in SGD learning of shallow neural networks](https://arxiv.org/abs/2504.19983v2) | 2504.19983v2 | 7 |
| 2025-04-28 | [Can a Crow Hatch a Falcon? Lineage Matters in Predicting Large Language Model Performance](https://arxiv.org/abs/2504.19811v2) | 2504.19811v2 | 8 |
| 2025-04-25 | [Large Language Model-Based Intelligent Antenna Design System](https://arxiv.org/abs/2504.18271v2) | 2504.18271v2 | 7 |
| 2025-04-21 | [Compute-Optimal LLMs Provably Generalize Better With Scale](https://arxiv.org/abs/2504.15208v1) | 2504.15208v1 | 8 |
| 2025-04-17 | [LLMs Meet Finance: Fine-Tuning Foundation Models for the Open FinLLM Leaderboard](https://arxiv.org/abs/2504.13125v1) | 2504.13125v1 | 13 |
| 2025-04-17 | [Scaling Laws for Data-Efficient Visual Transfer Learning](https://arxiv.org/abs/2504.13219v1) | 2504.13219v1 | 8 |
| 2025-04-15 | [DataDecide: How to Predict Best Pretraining Data with Small Experiments](https://arxiv.org/abs/2504.11393v2) | 2504.11393v2 | 10 |
| 2025-04-13 | [Understanding LLM Behaviors via Compression: Data Generation, Knowledge Acquisition and Scaling Laws](https://arxiv.org/abs/2504.09597v6) | 2504.09597v6 | 8 |
| 2025-04-11 | [Seaweed-7B: Cost-Effective Training of Video Generation Foundation Model](https://arxiv.org/abs/2504.08685v2) | 2504.08685v2 | 10 |
| 2025-04-11 | [Position: Beyond Euclidean -- Foundation Models Should Embrace Non-Euclidean Geometries](https://arxiv.org/abs/2504.08896v2) | 2504.08896v2 | 12 |
| 2025-04-10 | [Scaling Laws of Graph Neural Networks for Atomistic Materials Modeling](https://arxiv.org/abs/2504.08112v1) | 2504.08112v1 | 8 |
| 2025-04-10 | [On Model and Data Scaling for Skeleton-based Self-Supervised Gait Recognition](https://arxiv.org/abs/2504.07598v1) | 2504.07598v1 | 7 |
| 2025-04-06 | [Hessian of Perplexity for Large Language Models by PyTorch autograd (Open Source)](https://arxiv.org/abs/2504.04520v1) | 2504.04520v1 | 7 |
| 2025-04-04 | [Finding the Minimal Parameter Budget for Implicit Reasoning: A Data Complexity Driven Scaling Law for Language Models](https://arxiv.org/abs/2504.03635v5) | 2504.03635v5 | 10 |
| 2025-04-02 | [Study of scaling laws in language families](https://arxiv.org/abs/2504.01681v1) | 2504.01681v1 | 7 |
| 2025-04-01 | [Command A: An Enterprise-Ready Large Language Model](https://arxiv.org/abs/2504.00698v2) | 2504.00698v2 | 8 |
| 2025-03-31 | [Can Test-Time Scaling Improve World Foundation Model?](https://arxiv.org/abs/2503.24320v2) | 2503.24320v2 | 12 |
| 2025-03-26 | [Dewey Long Context Embedding Model: A Technical Report](https://arxiv.org/abs/2503.20376v1) | 2503.20376v1 | 9 |
| 2025-03-26 | [Wan: Open and Advanced Large-Scale Video Generative Models](https://arxiv.org/abs/2503.20314v2) | 2503.20314v2 | 9 |
| 2025-03-25 | [Unlocking Multi-Task Electric Energy System Intelligence: Data Scaling Laws and Performance with Limited Fine-Tuning](https://arxiv.org/abs/2503.20040v1) | 2503.20040v1 | 10 |
| 2025-03-25 | [Scaling Laws of Synthetic Data for Language Models](https://arxiv.org/abs/2503.19551v3) | 2503.19551v3 | 8 |
| 2025-03-24 | [Exploring Training and Inference Scaling Laws in Generative Retrieval](https://arxiv.org/abs/2503.18941v2) | 2503.18941v2 | 8 |
| 2025-03-19 | [Foundation models may exhibit staged progression in novel CBRN threat disclosure](https://arxiv.org/abs/2503.15182v1) | 2503.15182v1 | 10 |
| 2025-03-14 | [Reinforcement Learning Outperforms Supervised Fine-Tuning: A Case Study on Audio Question Answering](https://arxiv.org/abs/2503.11197v4) | 2503.11197v4 | 7 |
| 2025-03-13 | [Foundation Models for Atomistic Simulation of Chemistry and Materials](https://arxiv.org/abs/2503.10538v3) | 2503.10538v3 | 10 |
| 2025-03-12 | [PharMolixFM: All-Atom Foundation Models for Molecular Modeling and Generation](https://arxiv.org/abs/2503.21788v3) | 2503.21788v3 | 10 |
| 2025-03-11 | [Will LLMs Scaling Hit the Wall? Breaking Barriers via Distributed Resources on Massive Edge Devices](https://arxiv.org/abs/2503.08223v3) | 2503.08223v3 | 10 |
| 2025-03-06 | [Predictable Scale: Part I, Step Law -- Optimal Hyperparameter Scaling Law in Large Language Model Pretraining](https://arxiv.org/abs/2503.04715v7) | 2503.04715v7 | 12 |
| 2025-03-03 | [Comparative Analysis of OpenAI GPT-4o and DeepSeek R1 for Scientific Text Categorization Using Prompt Engineering](https://arxiv.org/abs/2503.02032v1) | 2503.02032v1 | 7 |
| 2025-03-03 | [Scaling Law Phenomena Across Regression Paradigms: Multiple and Kernel Approaches](https://arxiv.org/abs/2503.01314v1) | 2503.01314v1 | 8 |
| 2025-03-03 | [Hypergraph Foundation Model](https://arxiv.org/abs/2503.01203v2) | 2503.01203v2 | 10 |
| 2025-02-28 | [Emergent Abilities in Large Language Models: A Survey](https://arxiv.org/abs/2503.05788v3) | 2503.05788v3 | 8 |
| 2025-02-27 | [Evaluating System 1 vs. 2 Reasoning Approaches for Zero-Shot Time Series Forecasting: A Benchmark and Insights](https://arxiv.org/abs/2503.01895v2) | 2503.01895v2 | 7 |
| 2025-02-26 | [DataMan: Data Manager for Pre-training Large Language Models](https://arxiv.org/abs/2502.19363v3) | 2502.19363v3 | 7 |
| 2025-02-26 | [UQABench: Evaluating User Embedding for Prompting LLMs in Personalized Question Answering](https://arxiv.org/abs/2502.19178v2) | 2502.19178v2 | 7 |
| 2025-02-26 | [(Mis)Fitting: A Survey of Scaling Laws](https://arxiv.org/abs/2502.18969v1) | 2502.18969v1 | 10 |
| 2025-02-24 | [Unveiling Downstream Performance Scaling of LLMs: A Clustering-Based Perspective](https://arxiv.org/abs/2502.17262v4) | 2502.17262v4 | 7 |
| 2025-02-24 | [Reasoning Does Not Necessarily Improve Role-Playing Ability](https://arxiv.org/abs/2502.16940v2) | 2502.16940v2 | 7 |
| 2025-02-23 | [Compression Scaling Laws:Unifying Sparsity and Quantization](https://arxiv.org/abs/2502.16440v1) | 2502.16440v1 | 10 |
| 2025-02-18 | [MCTS-Judge: Test-Time Scaling in LLM-as-a-Judge for Code Correctness Evaluation](https://arxiv.org/abs/2502.12468v2) | 2502.12468v2 | 7 |
| 2025-02-17 | [What Are They Filtering Out? An Experimental Benchmark of Filtering Strategies for Harm Reduction in Pretraining Datasets](https://arxiv.org/abs/2503.05721v2) | 2503.05721v2 | 10 |
| 2025-02-17 | [LLMs on the Line: Data Determines Loss-to-Loss Scaling Laws](https://arxiv.org/abs/2502.12120v3) | 2502.12120v3 | 10 |
| 2025-02-16 | [SURGE: On the Potential of Large Language Models as General-Purpose Surrogate Code Executors](https://arxiv.org/abs/2502.11167v5) | 2502.11167v5 | 8 |
| 2025-02-14 | [OWLS: Scaling Laws for Multilingual Speech Recognition and Translation Models](https://arxiv.org/abs/2502.10373v1) | 2502.10373v1 | 7 |
| 2025-02-12 | [Salamandra Technical Report](https://arxiv.org/abs/2502.08489v2) | 2502.08489v2 | 9 |
| 2025-02-12 | [Unlocking Scaling Law in Industrial Recommendation Systems with a Three-step Paradigm based Large User Model](https://arxiv.org/abs/2502.08309v2) | 2502.08309v2 | 8 |
| 2025-02-11 | [Magic 1-For-1: Generating One Minute Video Clips within One Minute](https://arxiv.org/abs/2502.07701v3) | 2502.07701v3 | 8 |
| 2025-02-10 | [EfficientLLM: Scalable Pruning-Aware Pretraining for Architecture-Agnostic Edge Language Models](https://arxiv.org/abs/2502.06663v2) | 2502.06663v2 | 10 |
| 2025-02-10 | [Hephaestus: Improving Fundamental Agent Capabilities of Large Language Models through Continual Pre-Training](https://arxiv.org/abs/2502.06589v1) | 2502.06589v1 | 8 |
| 2025-02-09 | [Scaling Laws for Forgetting during Finetuning with Pretraining Data Injection](https://arxiv.org/abs/2502.06042v2) | 2502.06042v2 | 9 |
| 2025-02-08 | [Iterative Deepening Sampling as Efficient Test-Time Scaling](https://arxiv.org/abs/2502.05449v2) | 2502.05449v2 | 7 |
| 2025-02-05 | [Scaling laws in wearable human activity recognition](https://arxiv.org/abs/2502.03364v2) | 2502.03364v2 | 7 |
| 2025-02-05 | [Electronic Circuit Principles of Large Language Models](https://arxiv.org/abs/2502.03325v2) | 2502.03325v2 | 7 |
| 2025-02-03 | [GFM-RAG: Graph Foundation Model for Retrieval Augmented Generation](https://arxiv.org/abs/2502.01113v3) | 2502.01113v3 | 12 |
| 2025-02-02 | [Can the Nexus of Scaling Laws Coupled with Constant or Variable Elasticity of Substitution Predict AI and Other Technology Adoption?](https://arxiv.org/abs/2502.00909v1) | 2502.00909v1 | 7 |
| 2025-02-01 | [MetaOpenFOAM 2.0: Large Language Model Driven Chain of Thought for Automating CFD Simulation and Post-Processing](https://arxiv.org/abs/2502.00498v1) | 2502.00498v1 | 8 |
| 2025-01-31 | [Test-Time Training Scaling Laws for Chemical Exploration in Drug Design](https://arxiv.org/abs/2501.19153v4) | 2501.19153v4 | 9 |
| 2025-01-31 | [Scaling Laws for Differentially Private Language Models](https://arxiv.org/abs/2501.18914v1) | 2501.18914v1 | 8 |
| 2025-01-25 | [Scaling laws for decoding images from brain activity](https://arxiv.org/abs/2501.15322v2) | 2501.15322v2 | 7 |
| 2025-01-22 | [Quantification of Large Language Model Distillation](https://arxiv.org/abs/2501.12619v3) | 2501.12619v3 | 7 |
| 2025-01-21 | [The Journey Matters: Average Parameter Count over Pre-training Unifies Sparse and Dense Scaling Laws](https://arxiv.org/abs/2501.12486v2) | 2501.12486v2 | 8 |
| 2025-01-16 | [SMPLest-X: Ultimate Scaling for Expressive Human Pose and Shape Estimation](https://arxiv.org/abs/2501.09782v1) | 2501.09782v1 | 9 |
| 2025-01-16 | [Inference-Time Scaling for Diffusion Models beyond Scaling Denoising Steps](https://arxiv.org/abs/2501.09732v1) | 2501.09732v1 | 7 |
| 2025-01-16 | [Empowering Large Language Models in Wireless Communication: A Novel Dataset and Fine-Tuning Framework](https://arxiv.org/abs/2501.09631v1) | 2501.09631v1 | 7 |
| 2025-01-10 | [Scalable Vision Language Model Training via High Quality Data Curation](https://arxiv.org/abs/2501.05952v3) | 2501.05952v3 | 7 |
| 2025-01-09 | [Exploring Large Language Models (LLMs) through interactive Python activities](https://arxiv.org/abs/2501.05577v1) | 2501.05577v1 | 7 |
| 2025-01-06 | [The Scaling Law for LoRA Base on Mutual Information Upper Bound](https://arxiv.org/abs/2501.03152v1) | 2501.03152v1 | 7 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-22 | [OpenRFT: Adapting Reasoning Foundation Model for Domain-specific Tasks with Reinforcement Fine-Tuning](https://arxiv.org/abs/2412.16849v1) | 2412.16849v1 | 10 |
| 2024-12-19 | [Why We Build Local Large Language Models: An Observational Analysis from 35 Japanese and Multilingual LLMs](https://arxiv.org/abs/2412.14471v2) | 2412.14471v2 | 8 |
| 2024-12-17 | [Efficient Diffusion Transformer Policies with Mixture of Expert Denoisers for Multitask Learning](https://arxiv.org/abs/2412.12953v1) | 2412.12953v1 | 7 |
| 2024-12-16 | [MERaLiON-SpeechEncoder: Towards a Speech Foundation Model for Singapore and Beyond](https://arxiv.org/abs/2412.11538v3) | 2412.11538v3 | 13 |
| 2024-12-16 | [FTP: A Fine-grained Token-wise Pruner for Large Language Models via Token Routing](https://arxiv.org/abs/2412.11494v1) | 2412.11494v1 | 8 |
| 2024-12-10 | [Predictable Emergent Abilities of LLMs: Proxy Tasks Are All You Need](https://arxiv.org/abs/2412.07111v1) | 2412.07111v1 | 7 |
| 2024-12-09 | [Sloth: scaling laws for LLM skills to predict multi-benchmark performance across families](https://arxiv.org/abs/2412.06540v5) | 2412.06540v5 | 9 |
| 2024-12-05 | [Densing Law of LLMs](https://arxiv.org/abs/2412.04315v2) | 2412.04315v2 | 7 |
| 2024-12-02 | [Yi-Lightning Technical Report](https://arxiv.org/abs/2412.01253v5) | 2412.01253v5 | 9 |
| 2024-12-02 | [Scaling Law for Language Models Training Considering Batch Size](https://arxiv.org/abs/2412.01505v1) | 2412.01505v1 | 8 |
| 2024-12-02 | [Berezinskii--Kosterlitz--Thouless transition in a context-sensitive random language model](https://arxiv.org/abs/2412.01212v2) | 2412.01212v2 | 7 |
| 2024-11-29 | [Provable Scaling Laws for the Test-Time Compute of Large Language Models](https://arxiv.org/abs/2411.19477v5) | 2411.19477v5 | 9 |
| 2024-11-26 | [D$^2$-World: An Efficient World Model through Decoupled Dynamic Flow](https://arxiv.org/abs/2411.17027v1) | 2411.17027v1 | 9 |
| 2024-11-26 | [Low-Bit Quantization Favors Undertrained LLMs: Scaling Laws for Quantized LLMs with 100T Training Tokens](https://arxiv.org/abs/2411.17691v2) | 2411.17691v2 | 8 |
| 2024-11-25 | [Scaling Laws for Black box Adversarial Attacks](https://arxiv.org/abs/2411.16782v4) | 2411.16782v4 | 7 |
| 2024-11-24 | [ScalingNote: Scaling up Retrievers with Large Language Models for Real-World Dense Retrieval](https://arxiv.org/abs/2411.15766v1) | 2411.15766v1 | 7 |
| 2024-11-22 | [Health AI Developer Foundations](https://arxiv.org/abs/2411.15128v2) | 2411.15128v2 | 8 |
| 2024-11-21 | [Velocitune: A Velocity-based Dynamic Domain Reweighting Method for Continual Pre-training](https://arxiv.org/abs/2411.14318v2) | 2411.14318v2 | 7 |
| 2024-11-20 | [A Collaborative Ensemble Framework for CTR Prediction](https://arxiv.org/abs/2411.13700v1) | 2411.13700v1 | 8 |
| 2024-11-20 | [Scaling Laws for Online Advertisement Retrieval](https://arxiv.org/abs/2411.13322v2) | 2411.13322v2 | 8 |
| 2024-11-20 | [Training Bilingual LMs with Data Constraints in the Targeted Language](https://arxiv.org/abs/2411.12986v2) | 2411.12986v2 | 8 |
| 2024-11-11 | [Understanding Scaling Laws with Statistical and Approximation Theory for Transformer Neural Networks on Intrinsically Low-dimensional Data](https://arxiv.org/abs/2411.06646v1) | 2411.06646v1 | 8 |
| 2024-11-08 | [Scaling Laws for Task-Optimized Models of the Primate Visual Ventral Stream](https://arxiv.org/abs/2411.05712v3) | 2411.05712v3 | 7 |
| 2024-11-07 | [Scaling Laws for Precision](https://arxiv.org/abs/2411.04330v2) | 2411.04330v2 | 8 |
| 2024-10-31 | [BitStack: Any-Size Compression of Large Language Models in Variable Memory Environments](https://arxiv.org/abs/2410.23918v3) | 2410.23918v3 | 7 |
| 2024-10-23 | [TabDPT: Scaling Tabular Foundation Models on Real Data](https://arxiv.org/abs/2410.18164v3) | 2410.18164v3 | 13 |
| 2024-10-21 | [Bayesian scaling laws for in-context learning](https://arxiv.org/abs/2410.16531v4) | 2410.16531v4 | 7 |
| 2024-10-21 | [A Simple Model of Inference Scaling Laws](https://arxiv.org/abs/2410.16377v2) | 2410.16377v2 | 8 |
| 2024-10-21 | [Pre-training Distillation for Large Language Models: A Design Space Exploration](https://arxiv.org/abs/2410.16215v1) | 2410.16215v1 | 7 |
| 2024-10-19 | [Diversity Explains Inference Scaling Laws: Through a Case Study of Minimum Bayes Risk Decoding](https://arxiv.org/abs/2410.15021v2) | 2410.15021v2 | 8 |
| 2024-10-17 | [Scaling Wearable Foundation Models](https://arxiv.org/abs/2410.13638v1) | 2410.13638v1 | 10 |
| 2024-10-16 | [Towards Neural Scaling Laws for Time Series Foundation Models](https://arxiv.org/abs/2410.12360v3) | 2410.12360v3 | 12 |
| 2024-10-16 | [$M^3$ Scaling Law: Optimizing Multi-Epoch, Multi-Lingual, and Multi-Stage Training for Low-Resource Language Models](https://arxiv.org/abs/2410.12325v2) | 2410.12325v2 | 10 |
| 2024-10-15 | [Scaling Laws for Post Training Quantized Large Language Models](https://arxiv.org/abs/2410.12119v3) | 2410.12119v3 | 9 |
| 2024-10-15 | [Scaling Laws for Multilingual Language Models](https://arxiv.org/abs/2410.12883v2) | 2410.12883v2 | 8 |
| 2024-10-15 | [A Hitchhiker's Guide to Scaling Law Estimation](https://arxiv.org/abs/2410.11840v2) | 2410.11840v2 | 8 |
| 2024-10-15 | [Adaptive Data Optimization: Dynamic Sample Selection with Scaling Laws](https://arxiv.org/abs/2410.11820v1) | 2410.11820v1 | 12 |
| 2024-10-14 | [BrainGPT: Unleashing the Potential of EEG Generalist Foundation Model by Autoregressive Pre-training](https://arxiv.org/abs/2410.19779v2) | 2410.19779v2 | 11 |
| 2024-10-14 | [GraphCLIP: Enhancing Transferability in Graph Foundation Models for Text-Attributed Graphs](https://arxiv.org/abs/2410.10329v4) | 2410.10329v4 | 14 |
| 2024-10-12 | [OpenR: An Open Source Framework for Advanced Reasoning with Large Language Models](https://arxiv.org/abs/2410.09671v1) | 2410.09671v1 | 7 |
| 2024-10-11 | [Scaling Laws for Predicting Downstream Performance in LLMs](https://arxiv.org/abs/2410.08527v2) | 2410.08527v2 | 10 |
| 2024-10-10 | [Scaling Laws For Diffusion Transformers](https://arxiv.org/abs/2410.08184v2) | 2410.08184v2 | 9 |
| 2024-10-09 | [Improving Data Efficiency via Curating LLM-Driven Rating Systems](https://arxiv.org/abs/2410.10877v2) | 2410.10877v2 | 7 |
| 2024-10-09 | [Scaling Laws For Mixed Quantization](https://arxiv.org/abs/2410.06722v3) | 2410.06722v3 | 8 |
| 2024-10-08 | [Scaling Laws Across Model Architectures: A Comparative Analysis of Dense and MoE Models in Large Language Models](https://arxiv.org/abs/2410.05661v1) | 2410.05661v1 | 9 |
| 2024-10-06 | [LLM Gesticulator: Leveraging Large Language Models for Scalable and Controllable Co-Speech Gesture Synthesis](https://arxiv.org/abs/2410.10851v2) | 2410.10851v2 | 7 |
| 2024-10-06 | [Inference Scaling for Long-Context Retrieval Augmented Generation](https://arxiv.org/abs/2410.04343v2) | 2410.04343v2 | 7 |
| 2024-10-04 | [How Much Can We Forget about Data Contamination?](https://arxiv.org/abs/2410.03249v4) | 2410.03249v4 | 7 |
| 2024-09-23 | [Rethinking Conventional Wisdom in Machine Learning: From Generalization to Scaling](https://arxiv.org/abs/2409.15156v2) | 2409.15156v2 | 8 |
| 2024-09-23 | [Scaling Laws of Decoder-Only Models on the Multilingual Machine Translation Task](https://arxiv.org/abs/2409.15051v1) | 2409.15051v1 | 8 |
| 2024-09-23 | [DH-FaceVid-1K: A Large-Scale High-Quality Dataset for Face Video Generation](https://arxiv.org/abs/2410.07151v2) | 2410.07151v2 | 9 |
| 2024-09-20 | [Exploring Scaling Laws for Local SGD in Large Language Model Training](https://arxiv.org/abs/2409.13198v1) | 2409.13198v1 | 9 |
| 2024-09-18 | [Development and bilingual evaluation of Japanese medical large language model within reasonably low computational resources](https://arxiv.org/abs/2409.11783v2) | 2409.11783v2 | 8 |
| 2024-09-14 | [Symbolic Regression with a Learned Concept Library](https://arxiv.org/abs/2409.09359v3) | 2409.09359v3 | 7 |
| 2024-09-10 | [A Practice of Post-Training on Llama-3 70B with Optimal Selection of Additional Language Mixture Ratio](https://arxiv.org/abs/2409.06624v4) | 2409.06624v4 | 7 |
| 2024-09-09 | [Unified Neural Network Scaling Laws and Scale-time Equivalence](https://arxiv.org/abs/2409.05782v1) | 2409.05782v1 | 7 |
| 2024-09-07 | [Optimization Hyper-parameter Laws for Large Language Models](https://arxiv.org/abs/2409.04777v4) | 2409.04777v4 | 7 |
| 2024-09-04 | [Scaling Laws for Economic Productivity: Experimental Evidence in LLM-Assisted Translation](https://arxiv.org/abs/2409.02391v2) | 2409.02391v2 | 8 |
| 2024-08-28 | [LeMON: Learning to Learn Multi-Operator Networks](https://arxiv.org/abs/2408.16168v2) | 2408.16168v2 | 10 |
| 2024-08-26 | [Foundation Models for Music: A Survey](https://arxiv.org/abs/2408.14340v3) | 2408.14340v3 | 13 |
| 2024-08-23 | [LLM-PBE: Assessing Data Privacy in Large Language Models](https://arxiv.org/abs/2408.12787v2) | 2408.12787v2 | 7 |
| 2024-08-20 | [Do Neural Scaling Laws Exist on Graph Self-Supervised Learning?](https://arxiv.org/abs/2408.11243v2) | 2408.11243v2 | 11 |
| 2024-08-19 | [Performance Law of Large Language Models](https://arxiv.org/abs/2408.09895v4) | 2408.09895v4 | 7 |
| 2024-08-16 | [OpenCity: Open Spatio-Temporal Foundation Models for Traffic Prediction](https://arxiv.org/abs/2408.10269v1) | 2408.10269v1 | 10 |
| 2024-08-15 | [ScalingFilter: Assessing Data Quality through Inverse Utilization of Scaling Laws](https://arxiv.org/abs/2408.08310v1) | 2408.08310v1 | 8 |
| 2024-08-14 | [Knowledge in Superposition: Unveiling the Failures of Lifelong Knowledge Editing for Large Language Models](https://arxiv.org/abs/2408.07413v3) | 2408.07413v3 | 7 |
| 2024-08-12 | [Evaluating Language Models for Efficient Code Generation](https://arxiv.org/abs/2408.06450v1) | 2408.06450v1 | 7 |
| 2024-08-05 | [Why Are My Prompts Leaked? Unraveling Prompt Extraction Threats in Customized Large Language Models](https://arxiv.org/abs/2408.02416v2) | 2408.02416v2 | 7 |
| 2024-08-01 | [Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models](https://arxiv.org/abs/2408.00724v3) | 2408.00724v3 | 9 |
| 2024-08-01 | [Are Bigger Encoders Always Better in Vision Large Models?](https://arxiv.org/abs/2408.00620v1) | 2408.00620v1 | 8 |
| 2024-07-24 | [CMR Scaling Law: Predicting Critical Mixture Ratios for Continual Pre-training of Language Models](https://arxiv.org/abs/2407.17467v2) | 2407.17467v2 | 8 |
| 2024-07-15 | [Q-Sparse: All Large Language Models can be Fully Sparsely-Activated](https://arxiv.org/abs/2407.10969v3) | 2407.10969v3 | 7 |
| 2024-07-15 | [GRUtopia: Dream General Robots in a City at Scale](https://arxiv.org/abs/2407.10943v1) | 2407.10943v1 | 7 |
| 2024-07-11 | [Have We Reached AGI? Comparing ChatGPT, Claude, and Gemini to Human Literacy and Education Benchmarks](https://arxiv.org/abs/2407.09573v1) | 2407.09573v1 | 7 |
| 2024-07-11 | [Skywork-Math: Data Scaling Laws for Mathematical Reasoning in Large Language Models -- The Story Goes On](https://arxiv.org/abs/2407.08348v2) | 2407.08348v2 | 10 |
| 2024-07-10 | [Toto: Time Series Optimized Transformer for Observability](https://arxiv.org/abs/2407.07874v2) | 2407.07874v2 | 9 |
| 2024-07-10 | [GLBench: A Comprehensive Benchmark for Graph with Large Language Models](https://arxiv.org/abs/2407.07457v4) | 2407.07457v4 | 8 |
| 2024-07-03 | [52B to 1T: Lessons Learned via Tele-FLM Series](https://arxiv.org/abs/2407.02783v1) | 2407.02783v1 | 10 |
| 2024-07-02 | [Breaking Language Barriers: Cross-Lingual Continual Pre-Training at Scale](https://arxiv.org/abs/2407.02118v2) | 2407.02118v2 | 8 |
| 2024-07-01 | [Collaborative Performance Prediction for Large Language Models](https://arxiv.org/abs/2407.01300v2) | 2407.01300v2 | 7 |
| 2024-06-29 | [Beyond Scaleup: Knowledge-aware Parsimony Learning from Deep Networks](https://arxiv.org/abs/2407.00478v3) | 2407.00478v3 | 8 |
| 2024-06-29 | [LLM-Generated Natural Language Meets Scaling Laws: New Explorations and Data Augmentation Methods](https://arxiv.org/abs/2407.00322v1) | 2407.00322v1 | 8 |
| 2024-06-28 | [YuLan: An Open-source Large Language Model](https://arxiv.org/abs/2406.19853v1) | 2406.19853v1 | 8 |
| 2024-06-24 | [Scaling Laws for Linear Complexity Language Models](https://arxiv.org/abs/2406.16690v1) | 2406.16690v1 | 8 |
| 2024-06-22 | [Scaling Laws for Fact Memorization of Large Language Models](https://arxiv.org/abs/2406.15720v1) | 2406.15720v1 | 9 |
| 2024-06-21 | [Uni-Mol2: Exploring Molecular Pretraining Model at Scale](https://arxiv.org/abs/2406.14969v2) | 2406.14969v2 | 7 |
| 2024-06-20 | [Evidence of a log scaling law for political persuasion with large language models](https://arxiv.org/abs/2406.14508v1) | 2406.14508v1 | 11 |
| 2024-06-11 | [Scaling Large Language Model-based Multi-Agent Collaboration](https://arxiv.org/abs/2406.07155v3) | 2406.07155v3 | 7 |
| 2024-06-10 | [Compute Better Spent: Replacing Dense Layers with Structured Matrices](https://arxiv.org/abs/2406.06248v1) | 2406.06248v1 | 8 |
| 2024-06-09 | [Technical Report for CVPR 2024 WeatherProof Dataset Challenge: Semantic Segmentation on Paired Real Data](https://arxiv.org/abs/2407.01579v1) | 2407.01579v1 | 10 |
| 2024-06-06 | [Why Has Predicting Downstream Capabilities of Frontier AI Models with Scale Remained Elusive?](https://arxiv.org/abs/2406.04391v2) | 2406.04391v2 | 7 |
| 2024-06-06 | [Empirical Guidelines for Deploying LLMs onto Resource-constrained Edge Devices](https://arxiv.org/abs/2406.03777v3) | 2406.03777v3 | 7 |
| 2024-06-04 | [Alice in Wonderland: Simple Tasks Showing Complete Reasoning Breakdown in State-Of-the-Art Large Language Models](https://arxiv.org/abs/2406.02061v5) | 2406.02061v5 | 12 |
| 2024-06-03 | [D-CPT Law: Domain-specific Continual Pre-Training Scaling Law for Large Language Models](https://arxiv.org/abs/2406.01375v1) | 2406.01375v1 | 9 |
| 2024-05-29 | [Large Language Models for Code Summarization](https://arxiv.org/abs/2405.19032v1) | 2405.19032v1 | 7 |
| 2024-05-28 | [ORLM: A Customizable Framework in Training Large Models for Automated Optimization Modeling](https://arxiv.org/abs/2405.17743v5) | 2405.17743v5 | 7 |
| 2024-05-23 | [Aya 23: Open Weight Releases to Further Multilingual Progress](https://arxiv.org/abs/2405.15032v2) | 2405.15032v2 | 8 |
| 2024-05-23 | [AstroPT: Scaling Large Observation Models for Astronomy](https://arxiv.org/abs/2405.14930v1) | 2405.14930v1 | 8 |
| 2024-05-22 | [Neural Scaling Laws in Robotics](https://arxiv.org/abs/2405.14005v2) | 2405.14005v2 | 12 |
| 2024-05-17 | [Observational Scaling Laws and the Predictability of Language Model Performance](https://arxiv.org/abs/2405.10938v3) | 2405.10938v3 | 8 |
| 2024-05-17 | [The Future of Large Language Model Pre-training is Federated](https://arxiv.org/abs/2405.10853v3) | 2405.10853v3 | 7 |
| 2024-05-13 | [RLHF Workflow: From Reward Modeling to Online RLHF](https://arxiv.org/abs/2405.07863v3) | 2405.07863v3 | 7 |
| 2024-05-13 | [UCCIX: Irish-eXcellence Large Language Model](https://arxiv.org/abs/2405.13010v1) | 2405.13010v1 | 8 |
| 2024-05-07 | [SEED-Data-Edit Technical Report: A Hybrid Dataset for Instructional Image Editing](https://arxiv.org/abs/2405.04007v1) | 2405.04007v1 | 8 |
| 2024-05-05 | [Labeling supervised fine-tuning data with the scaling law](https://arxiv.org/abs/2405.02817v2) | 2405.02817v2 | 8 |
| 2024-04-30 | [Knowledge Distillation vs. Pretraining from Scratch under a Fixed (Computation) Budget](https://arxiv.org/abs/2404.19319v1) | 2404.19319v1 | 7 |
| 2024-04-29 | [HELPER-X: A Unified Instructable Embodied Agent to Tackle Four Interactive Vision-Language Domains with Memory-Augmented Language Models](https://arxiv.org/abs/2404.19065v1) | 2404.19065v1 | 7 |
| 2024-04-28 | [PatentGPT: A Large Language Model for Intellectual Property](https://arxiv.org/abs/2404.18255v5) | 2404.18255v5 | 8 |
| 2024-04-27 | [Temporal Scaling Law for Large Language Models](https://arxiv.org/abs/2404.17785v4) | 2404.17785v4 | 9 |
| 2024-04-12 | [Pretraining and Updates of Domain-Specific LLM: A Case Study in the Japanese Business Domain](https://arxiv.org/abs/2404.08262v3) | 2404.08262v3 | 10 |
| 2024-04-10 | [A Mathematical Theory for Learning Semantic Languages by Abstract Learners](https://arxiv.org/abs/2404.07009v3) | 2404.07009v3 | 10 |
| 2024-04-08 | [Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws](https://arxiv.org/abs/2404.05405v1) | 2404.05405v1 | 7 |
| 2024-04-03 | [Toward Inference-optimal Mixture-of-Expert Large Language Models](https://arxiv.org/abs/2404.02852v1) | 2404.02852v1 | 7 |
| 2024-04-01 | [The Fine Line: Navigating Large Language Model Pretraining with Down-streaming Capability Analysis](https://arxiv.org/abs/2404.01204v3) | 2404.01204v3 | 10 |
| 2024-03-25 | [Data Mixing Laws: Optimizing Data Mixtures by Predicting Language Modeling Performance](https://arxiv.org/abs/2403.16952v2) | 2403.16952v2 | 8 |
| 2024-03-23 | [CodeShell Technical Report](https://arxiv.org/abs/2403.15747v1) | 2403.15747v1 | 12 |
| 2024-03-13 | [OverleafCopilot: Empowering Academic Writing in Overleaf with Large Language Models](https://arxiv.org/abs/2403.09733v1) | 2403.09733v1 | 7 |
| 2024-03-12 | [Towards a clinically accessible radiology foundation model: open-access and lightweight, with automated evaluation](https://arxiv.org/abs/2403.08002v5) | 2403.08002v5 | 11 |
| 2024-03-11 | [Unraveling the Mystery of Scaling Laws: Part I](https://arxiv.org/abs/2403.06563v3) | 2403.06563v3 | 12 |
| 2024-03-04 | [Wukong: Towards a Scaling Law for Large-Scale Recommendation](https://arxiv.org/abs/2403.02545v4) | 2403.02545v4 | 8 |
| 2024-03-04 | [NeuSpeech: Decode Neural signal as Speech](https://arxiv.org/abs/2403.01748v3) | 2403.01748v3 | 8 |
| 2024-02-28 | [Meta-Task Prompting Elicits Embeddings from Large Language Models](https://arxiv.org/abs/2402.18458v2) | 2402.18458v2 | 8 |
| 2024-02-27 | [The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits](https://arxiv.org/abs/2402.17764v1) | 2402.17764v1 | 7 |
| 2024-02-27 | [When Scaling Meets LLM Finetuning: The Effect of Data, Model and Finetuning Method](https://arxiv.org/abs/2402.17193v1) | 2402.17193v1 | 9 |
| 2024-02-20 | [Scaling Laws Behind Code Understanding Model](https://arxiv.org/abs/2402.12813v1) | 2402.12813v1 | 8 |
| 2024-02-12 | [Only the Curve Shape Matters: Training Foundation Models for Zero-Shot Multivariate Time Series Forecasting through Next Curve Shape Prediction](https://arxiv.org/abs/2402.07570v2) | 2402.07570v2 | 10 |
| 2024-02-10 | [A Tale of Tails: Model Collapse as a Change of Scaling Laws](https://arxiv.org/abs/2402.07043v2) | 2402.07043v2 | 8 |
| 2024-02-09 | [Large Language Models: A Survey](https://arxiv.org/abs/2402.06196v3) | 2402.06196v3 | 8 |
| 2024-02-06 | [Scaling Laws for Downstream Task Performance of Large Language Models](https://arxiv.org/abs/2402.04177v3) | 2402.04177v3 | 11 |
| 2024-02-04 | [Selecting Large Language Model to Fine-tune via Rectified Scaling Law](https://arxiv.org/abs/2402.02314v3) | 2402.02314v3 | 9 |
| 2024-02-03 | [Position: Graph Foundation Models are Already Here](https://arxiv.org/abs/2402.02216v3) | 2402.02216v3 | 10 |
| 2024-02-03 | [Towards Neural Scaling Laws on Graphs](https://arxiv.org/abs/2402.02054v3) | 2402.02054v3 | 7 |
| 2024-02-01 | [LLMs learn governing principles of dynamical systems, revealing an in-context neural scaling law](https://arxiv.org/abs/2402.00795v4) | 2402.00795v4 | 8 |
| 2024-02-01 | [The Information of Large Language Model Geometry](https://arxiv.org/abs/2402.03471v1) | 2402.03471v1 | 7 |
| 2024-01-23 | [Towards Trustable Language Models: Investigating Information Quality of Large Language Models](https://arxiv.org/abs/2401.13086v1) | 2401.13086v1 | 7 |
| 2024-01-11 | [Scaling Laws for Forgetting When Fine-Tuning Large Language Models](https://arxiv.org/abs/2401.05605v1) | 2401.05605v1 | 9 |
| 2024-01-08 | [TeleChat Technical Report](https://arxiv.org/abs/2401.03804v2) | 2401.03804v2 | 11 |
| 2024-01-05 | [DeepSeek LLM: Scaling Open-Source Language Models with Longtermism](https://arxiv.org/abs/2401.02954v1) | 2401.02954v1 | 7 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-31 | [GeoGalactica: A Scientific Large Language Model in Geoscience](https://arxiv.org/abs/2401.00434v2) | 2401.00434v2 | 7 |
| 2023-12-31 | [Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws](https://arxiv.org/abs/2401.00448v3) | 2401.00448v3 | 8 |
| 2023-12-29 | [An Empirical Study of Scaling Law for OCR](https://arxiv.org/abs/2401.00028v3) | 2401.00028v3 | 7 |
| 2023-12-22 | [YAYI 2: Multilingual Open-Source Large Language Models](https://arxiv.org/abs/2312.14862v1) | 2312.14862v1 | 8 |
| 2023-12-21 | [Typhoon: Thai Large Language Models](https://arxiv.org/abs/2312.13951v1) | 2312.13951v1 | 10 |
| 2023-12-18 | [VinaLLaMA: LLaMA-based Vietnamese Foundation Model](https://arxiv.org/abs/2312.11011v1) | 2312.11011v1 | 13 |
| 2023-12-12 | [Large Foundation Models for Power Systems](https://arxiv.org/abs/2312.07044v1) | 2312.07044v1 | 12 |
| 2023-12-12 | [On Diversified Preferences of Large Language Model Alignment](https://arxiv.org/abs/2312.07401v5) | 2312.07401v5 | 7 |
| 2023-12-04 | [Scaling Laws in Jet Classification](https://arxiv.org/abs/2312.02264v1) | 2312.02264v1 | 7 |
| 2023-12-01 | [The Efficiency Spectrum of Large Language Models: An Algorithmic Survey](https://arxiv.org/abs/2312.00678v2) | 2312.00678v2 | 7 |
| 2023-11-21 | [AcademicGPT: Empowering Academic Research](https://arxiv.org/abs/2311.12315v1) | 2311.12315v1 | 11 |
| 2023-11-06 | [GPT4All: An Ecosystem of Open Source Compressed Language Models](https://arxiv.org/abs/2311.04931v1) | 2311.04931v1 | 7 |
| 2023-11-06 | [Ziya2: Data-centric Learning is All LLMs Need](https://arxiv.org/abs/2311.03301v2) | 2311.03301v2 | 11 |
| 2023-10-30 | [Skywork: A More Open Bilingual Foundation Model](https://arxiv.org/abs/2310.19341v1) | 2310.19341v1 | 13 |
| 2023-10-25 | [ConvNets Match Vision Transformers at Scale](https://arxiv.org/abs/2310.16764v1) | 2310.16764v1 | 8 |
| 2023-10-22 | [One Model for All: Large Language Models are Domain-Agnostic Recommendation Systems](https://arxiv.org/abs/2310.14304v2) | 2310.14304v2 | 7 |
| 2023-10-17 | [BitNet: Scaling 1-bit Transformers for Large Language Models](https://arxiv.org/abs/2310.11453v1) | 2310.11453v1 | 7 |
| 2023-10-13 | [Vision-by-Language for Training-Free Compositional Image Retrieval](https://arxiv.org/abs/2310.09291v2) | 2310.09291v2 | 7 |
| 2023-10-05 | [Predicting Emergent Abilities with Infinite Resolution Evaluation](https://arxiv.org/abs/2310.03262v3) | 2310.03262v3 | 7 |
| 2023-10-03 | [A Neural Scaling Law from Lottery Ticket Ensembling](https://arxiv.org/abs/2310.02258v2) | 2310.02258v2 | 8 |
| 2023-09-29 | [SMPLer-X: Scaling Up Expressive Human Pose and Shape Estimation](https://arxiv.org/abs/2309.17448v3) | 2309.17448v3 | 9 |
| 2023-09-28 | [Neural scaling laws for phenotypic drug discovery](https://arxiv.org/abs/2309.16773v1) | 2309.16773v1 | 7 |
| 2023-09-19 | [Baichuan 2: Open Large-scale Language Models](https://arxiv.org/abs/2309.10305v4) | 2309.10305v4 | 7 |
| 2023-09-15 | [Scaling Laws for Sparsely-Connected Foundation Models](https://arxiv.org/abs/2309.08520v1) | 2309.08520v1 | 12 |
| 2023-09-15 | [Uncovering Neural Scaling Laws in Molecular Representation Learning](https://arxiv.org/abs/2309.15123v2) | 2309.15123v2 | 7 |
| 2023-09-13 | [EarthPT: a time series foundation model for Earth Observation](https://arxiv.org/abs/2309.07207v2) | 2309.07207v2 | 12 |
| 2023-08-23 | [Local Distortion Aware Efficient Transformer Adaptation for Image Quality Assessment](https://arxiv.org/abs/2308.12001v1) | 2308.12001v1 | 8 |
| 2023-08-20 | [FoodGPT: A Large Language Model in Food Testing Domain with Incremental Pre-training and Knowledge Graph Prompt](https://arxiv.org/abs/2308.10173v1) | 2308.10173v1 | 7 |
| 2023-08-09 | [Extrapolating Large Language Models to Non-English by Aligning Languages](https://arxiv.org/abs/2308.04948v2) | 2308.04948v2 | 8 |
| 2023-07-24 | [Leveraging Large Language Models (LLMs) for Process Mining (Technical Report)](https://arxiv.org/abs/2307.12701v1) | 2307.12701v1 | 9 |
| 2023-07-11 | [Secrets of RLHF in Large Language Models Part I: PPO](https://arxiv.org/abs/2307.04964v2) | 2307.04964v2 | 7 |
| 2023-07-05 | [Flacuna: Unleashing the Problem Solving Power of Vicuna using FLAN Fine-Tuning](https://arxiv.org/abs/2307.02053v1) | 2307.02053v1 | 7 |
| 2023-06-15 | [2nd Place Winning Solution for the CVPR2023 Visual Anomaly and Novelty Detection Challenge: Multimodal Prompting for Data-centric Anomaly Detection](https://arxiv.org/abs/2306.09067v2) | 2306.09067v2 | 9 |
| 2023-06-14 | [Revealing the structure of language model capabilities](https://arxiv.org/abs/2306.10062v1) | 2306.10062v1 | 7 |
| 2023-05-17 | [Statistical Knowledge Assessment for Large Language Models](https://arxiv.org/abs/2305.10519v2) | 2305.10519v2 | 7 |
| 2023-05-11 | [An Inverse Scaling Law for CLIP Training](https://arxiv.org/abs/2305.07017v2) | 2305.07017v2 | 10 |
| 2023-04-21 | [Emergent and Predictable Memorization in Large Language Models](https://arxiv.org/abs/2304.11158v2) | 2304.11158v2 | 8 |
| 2023-04-06 | [Can Large Language Models Play Text Games Well? Current State-of-the-Art and Open Questions](https://arxiv.org/abs/2304.02868v2) | 2304.02868v2 | 7 |
| 2023-02-18 | [Bag of Tricks for Effective Language Model Pretraining and Downstream Adaptation: A Case Study on GLUE](https://arxiv.org/abs/2302.09268v1) | 2302.09268v1 | 9 |
| 2023-02-14 | [Cliff-Learning](https://arxiv.org/abs/2302.07348v2) | 2302.07348v2 | 8 |
| 2023-01-18 | [Human-Timescale Adaptation in an Open-Ended Task Space](https://arxiv.org/abs/2301.07608v1) | 2301.07608v1 | 8 |
| 2023-01-10 | [Scaling Laws for Generative Mixed-Modal Language Models](https://arxiv.org/abs/2301.03728v1) | 2301.03728v1 | 7 |

### 2022
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2022-12-19 | [The case for 4-bit precision: k-bit Inference Scaling Laws](https://arxiv.org/abs/2212.09720v2) | 2212.09720v2 | 8 |
| 2022-12-04 | [Toward Efficient Language Model Pretraining and Downstream Adaptation via Self-Evolution: A Case Study on SuperGLUE](https://arxiv.org/abs/2212.01853v1) | 2212.01853v1 | 12 |
| 2022-11-02 | [On the development and analysis of coupled surface-subsurface models of catchments. Part 3. Analytical solutions and scaling laws](https://arxiv.org/abs/2211.00972v3) | 2211.00972v3 | 7 |
| 2022-10-30 | [A Solvable Model of Neural Scaling Laws](https://arxiv.org/abs/2210.16859v1) | 2210.16859v1 | 8 |
| 2022-10-26 | [Broken Neural Scaling Laws](https://arxiv.org/abs/2210.14891v17) | 2210.14891v17 | 7 |
| 2022-09-26 | [Can Large Language Models Truly Understand Prompts? A Case Study with Negated Prompts](https://arxiv.org/abs/2209.12711v1) | 2209.12711v1 | 7 |
| 2022-09-13 | [Revisiting Neural Scaling Laws in Language and Vision](https://arxiv.org/abs/2209.06640v2) | 2209.06640v2 | 7 |
| 2022-06-29 | [Beyond neural scaling laws: beating power law scaling via data pruning](https://arxiv.org/abs/2206.14486v6) | 2206.14486v6 | 7 |
| 2022-05-24 | [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916v4) | 2205.11916v4 | 8 |

### 2021
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2021-10-13 | [Scaling Laws for the Few-Shot Adaptation of Pre-trained Image Classifiers](https://arxiv.org/abs/2110.06990v2) | 2110.06990v2 | 7 |
| 2021-08-25 | [A Scaling Law for Synthetic-to-Real Transfer: How Much Is Your Pre-training Effective?](https://arxiv.org/abs/2108.11018v3) | 2108.11018v3 | 7 |
| 2021-06-04 | [Layered gradient accumulation and modular pipeline parallelism: fast and efficient training of large language models](https://arxiv.org/abs/2106.02679v1) | 2106.02679v1 | 7 |

### 2020
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2020-05-23 | [Generalized scaling law for exciton binding energy in two-dimensional materials](https://arxiv.org/abs/2005.11569v1) | 2005.11569v1 | 7 |
| 2020-02-12 | [Power Scaling Laws and Near-Field Behaviors of Massive MIMO and Intelligent Reflecting Surfaces](https://arxiv.org/abs/2002.04960v5) | 2002.04960v5 | 7 |

<!-- table:end papers -->
