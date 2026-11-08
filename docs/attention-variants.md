# 🧭 注意力变体（Attention Variants）

> 从 MHA 到 MLA：一部 KV cache 的压缩简史。

标准多头注意力（MHA）给每个头独立的 K/V，推理时的 KV cache 随头数、层数、上下文长度线性膨胀。
这条赛道收录对注意力头结构本身的改造：共享 KV 头（MQA/GQA）、把 KV 压进低秩隐空间（MLA）等。
它们不改变注意力的二次复杂度，但直接决定长上下文模型能不能被便宜地部署。

## 奠基与必读

### 起源：前 Transformer 时代

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Learning Phrase Representations using RNN Encoder-Decoder (GRU) | [1406.1078](https://arxiv.org/abs/1406.1078) | 2014 | 门控循环单元，attention 诞生前的序列建模基座 |
| Sequence to Sequence Learning with Neural Networks | [1409.3215](https://arxiv.org/abs/1409.3215) | 2014 | 定长向量的信息瓶颈——正是 attention 要解决的问题 |
| Neural Machine Translation by Jointly Learning to Align and Translate | [1409.0473](https://arxiv.org/abs/1409.0473) | 2014 | Bahdanau 注意力：attention 的第一次亮相 |
| Memory Networks | [1410.3916](https://arxiv.org/abs/1410.3916) | 2014 | 可读写外部记忆，注意力即寻址 |
| Neural Turing Machines | [1410.5401](https://arxiv.org/abs/1410.5401) | 2014 | 软寻址记忆机制，注意力的另一条源头 |
| Show, Attend and Tell | [1502.03044](https://arxiv.org/abs/1502.03044) | 2015 | 注意力走进视觉：soft / hard attention |
| Effective Approaches to Attention-based Neural Machine Translation | [1508.04025](https://arxiv.org/abs/1508.04025) | 2015 | Luong 注意力：global / local 与点积打分 |
| Hopfield Networks is All You Need | [2008.02217](https://arxiv.org/abs/2008.02217) | 2020 | 理论桥：注意力 = 现代 Hopfield 网络的更新规则 |

### Transformer 时代

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Attention Is All You Need | [1706.03762](https://arxiv.org/abs/1706.03762) | 2017 | 一切的起点：scaled dot-product attention + MHA |
| BERT: Pre-training of Deep Bidirectional Transformers | [1810.04805](https://arxiv.org/abs/1810.04805) | 2018 | 双向编码器分支的起点 |
| Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer (T5) | [1910.10683](https://arxiv.org/abs/1910.10683) | 2019 | encoder-decoder 统一框架的标尺 |
| Fast Transformer Decoding: One Write-Head is All You Need | [1911.02150](https://arxiv.org/abs/1911.02150) | 2019 | MQA：所有 query 头共享一份 K/V，KV cache 除以头数 |
| GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints | [2305.13245](https://arxiv.org/abs/2305.13245) | 2023 | GQA：分组共享 K/V，质量与效率的甜点，Llama 2/3 标配 |
| Mixtral of Experts | [2401.04088](https://arxiv.org/abs/2401.04088) | 2024 | GQA + MoE 组合在开放权重模型上的标杆实现 |
| DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model | [2405.04434](https://arxiv.org/abs/2405.04434) | 2024 | MLA：把 K/V 压成低秩隐向量再缓存，同等压缩率下质量反超 MHA |
| Differential Transformer | [2410.05258](https://arxiv.org/abs/2410.05258) | 2024 | 差分注意力：两图相减抵消注意力噪声 |
| DeepSeek-V3 Technical Report | [2412.19437](https://arxiv.org/abs/2412.19437) | 2024 | MLA 在 671B MoE 上的规模化验证 |

## 相关实现

- [deepseek-ai/DeepSeek-V2](https://github.com/deepseek-ai/DeepSeek-V2) — MLA 官方参考实现。
- [meta-llama/llama3](https://github.com/meta-llama/llama3) — GQA 在 8B–405B 全尺寸上的应用。
- [lucidrains/x-transformers](https://github.com/lucidrains/x-transformers) — 一个文件集齐各种注意力实验特性。

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-10-29 | [Where Position Matters: Profiling-Guided Layer-Wise RoPE Allocation in Transformers](https://arxiv.org/abs/2610.39223v1) | 2610.39223v1 | 0 |
| 2026-10-24 | [RAQ-MLA: Role-Aware Quantization for Multi-Head Latent Attention Caches](https://arxiv.org/abs/2610.33625v1) | 2610.33625v1 | 12 |
| 2026-10-15 | [When the KV Cache Is Slower Than the GPU: Scaling Remote KV Tiers for Context-Parallel Prefill](https://arxiv.org/abs/2610.21500v1) | 2610.21500v1 | 3 |
| 2026-10-14 | [RoLaQ: Joint Rotation and Range Calibration for 2-Bit KV Caches in Multi-Head Latent Attention](https://arxiv.org/abs/2610.20686v1) | 2610.20686v1 | 9 |
| 2026-10-13 | [Joint Subspace Sparse Attention for Efficient Long-Context Decoding](https://arxiv.org/abs/2610.19026v1) | 2610.19026v1 | 0 |
| 2026-10-12 | [MLAfication: Efficiently Enabling High-Fidelity MLA for Modern LLMs](https://arxiv.org/abs/2610.17202v1) | 2610.17202v1 | 6 |
| 2026-10-08 | [Kronecker Product Attention: Memory-Efficient KV Compression via Structured Factorization](https://arxiv.org/abs/2610.12657v1) | 2610.12657v1 | 0 |
| 2026-10-02 | [Page-EntroKV: Hardware-Aligned, Entropy-Weighted KV-Cache Eviction under Grouped-Query Attention](https://arxiv.org/abs/2610.03135v1) | 2610.03135v1 | 6 |
| 2026-09-29 | [QuantMLA: Function-Aligned Dual-Path Quantization for Low-Bit MLA KV Caching](https://arxiv.org/abs/2609.36760v2) | 2609.36760v2 | 6 |
| 2026-09-08 | [Grouped Value Attention: Efficient KV Caching via On-Demand Key Reconstruction](https://arxiv.org/abs/2609.13285v2) | 2609.13285v2 | 0 |
| 2026-09-07 | [RedKnot-MLA: Multi-Head Offline-Online Reuse for DeepSeek-V4 Long-Context Serving](https://arxiv.org/abs/2609.07008v2) | 2609.07008v2 | 6 |
| 2026-09-01 | [Instella-MoE Technical Report](https://arxiv.org/abs/2609.00791v1) | 2609.00791v1 | 0 |
| 2026-08-28 | [An Exploratory Ablation of a Small MLA--SSM Hybrid Language Model](https://arxiv.org/abs/2609.29618v1) | 2609.29618v1 | 6 |
| 2026-08-20 | [Let's Scale Step by Step: Compute-Efficient Hyperparameter Transfer for Large-Scale Mixture-of-Experts](https://arxiv.org/abs/2608.20061v1) | 2608.20061v1 | 0 |
| 2026-07-30 | [Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers](https://arxiv.org/abs/2607.28611v1) | 2607.28611v1 | 0 |
| 2026-07-29 | [Beyond KV Reconstruction: Functional Reconstruction for MLA Draft Models in Speculative Decoding](https://arxiv.org/abs/2607.27269v1) | 2607.27269v1 | 6 |
| 2026-07-27 | [DynaCalKV: Key-Value Cache Compression via Head Grouping and Adaptive Rank Allocation](https://arxiv.org/abs/2607.24331v1) | 2607.24331v1 | 3 |
| 2026-07-25 | [Through the Bottleneck: How Multi-head Latent Attention Separates Content from Position in Language Models](https://arxiv.org/abs/2607.23054v1) | 2607.23054v1 | 6 |
| 2026-07-21 | [MoA-Structured Decode Attention DNF Derivation, KV-Cache Accumulation, GQA/MQA, and OpenACC Kernel](https://arxiv.org/abs/2607.19456v1) | 2607.19456v1 | 0 |
| 2026-07-20 | [A Training-Memory Regression in MLA Sequence Parallelism: Why Megatron-Core Forbids Absorption, and LAGA -- a Communication-Efficient Fix](https://arxiv.org/abs/2607.17644v1) | 2607.17644v1 | 6 |
| 2026-07-14 | [A JoLT for the KV cache: Near-Lossless KV Cache Compression via Joint Rank-bit Allocation](https://arxiv.org/abs/2607.12550v4) | 2607.12550v4 | 3 |
| 2026-06-19 | [Does RoPE Prevent or Degrade Retrieval Heads? A Mechanistic Analysis Across Model Families](https://arxiv.org/abs/2606.21249v1) | 2606.21249v1 | 0 |
| 2026-06-18 | [Grouped Query Experts: Mixture-of-Experts on GQA Self-Attention](https://arxiv.org/abs/2606.20945v2) | 2606.20945v2 | 0 |
| 2026-06-15 | [QK-Normed MLA: QK normalization without full key caching](https://arxiv.org/abs/2606.16310v1) | 2606.16310v1 | 6 |
| 2026-06-03 | [Depth-Attention: Cross-Layer Value Mixing for Language Models](https://arxiv.org/abs/2606.05014v2) | 2606.05014v2 | 0 |
| 2026-05-31 | [Move the Query, Not the Cache: Characterizing Cross-Instance Latent Attention Redistribution Across GPU Fabrics](https://arxiv.org/abs/2606.01502v1) | 2606.01502v1 | 0 |
| 2026-05-31 | [CryoProt: A Protein Pretraining Framework with Cross-Box Interactions on Cryo-EM Density Maps](https://arxiv.org/abs/2606.00955v1) | 2606.00955v1 | 0 |
| 2026-05-28 | [VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion](https://arxiv.org/abs/2605.30351v1) | 2605.30351v1 | 9 |
| 2026-05-19 | [SelKV: Selective KV Cache Merging with Per-Token Merge-or-Drop and Attention Compensation](https://arxiv.org/abs/2607.16213v1) | 2607.16213v1 | 3 |
| 2026-05-14 | [GQLA: Group-Query Latent Attention for Hardware-Adaptive Decoding](https://arxiv.org/abs/2605.15250v4) | 2605.15250v4 | 0 |
| 2026-05-07 | [Irminsul: MLA-Native Position-Independent Caching for Agentic LLM Serving](https://arxiv.org/abs/2605.05696v1) | 2605.05696v1 | 6 |
| 2026-04-27 | [Long-Context Aware Upcycling: A New Frontier for Hybrid LLM Scaling](https://arxiv.org/abs/2604.24715v1) | 2604.24715v1 | 0 |
| 2026-04-19 | [Predictive Multi-Tier Memory Management for KV Cache in Large-Scale GPU Inference](https://arxiv.org/abs/2604.26968v2) | 2604.26968v2 | 3 |
| 2026-04-16 | [The Illusion of Equivalence: Systematic FP16 Divergence in KV-Cached Autoregressive Inference](https://arxiv.org/abs/2604.15409v1) | 2604.15409v1 | 0 |
| 2026-04-14 | [Latent-Condensed Transformer for Efficient Long Context Modeling](https://arxiv.org/abs/2604.12452v3) | 2604.12452v3 | 0 |
| 2026-04-10 | [Modality-Aware Zero-Shot Pruning and Sparse Attention for Efficient Multimodal Edge Inference](https://arxiv.org/abs/2604.08971v1) | 2604.08971v1 | 0 |
| 2026-04-08 | [TRAPTI: Time-Resolved Analysis for SRAM Banking and Power Gating Optimization in Embedded Transformer Inference](https://arxiv.org/abs/2604.06955v1) | 2604.06955v1 | 0 |
| 2026-04-07 | [Attention Editing: A Versatile Framework for Cross-Architecture Attention Conversion](https://arxiv.org/abs/2604.05688v1) | 2604.05688v1 | 0 |
| 2026-03-31 | [Tucker Attention: A generalization of approximate attention mechanisms](https://arxiv.org/abs/2603.30033v1) | 2603.30033v1 | 0 |
| 2026-03-21 | [MKA: Memory-Keyed Attention for Efficient Long-Context Reasoning](https://arxiv.org/abs/2603.20586v2) | 2603.20586v2 | 0 |
| 2026-03-18 | [CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head Latent Attention](https://arxiv.org/abs/2603.17946v1) | 2603.17946v1 | 6 |
| 2026-03-02 | [Multi-Head Low-Rank Attention](https://arxiv.org/abs/2603.02188v1) | 2603.02188v1 | 0 |
| 2026-02-28 | [Whisper-MLA: Reducing GPU Memory Consumption of ASR Models based on MHA2MLA Conversion](https://arxiv.org/abs/2603.00563v1) | 2603.00563v1 | 6 |
| 2026-02-16 | [Thin Keys, Full Values: Reducing KV Cache via Low-Dimensional Attention Selection](https://arxiv.org/abs/2603.04427v4) | 2603.04427v4 | 3 |
| 2026-02-12 | [RooflineBench: A Benchmarking Framework for On-Device LLMs via Roofline Analysis](https://arxiv.org/abs/2602.11506v4) | 2602.11506v4 | 0 |
| 2026-02-11 | [SnapMLA: Efficient Long-Context MLA Decoding via Hardware-Aware FP8 Quantized Pipelining](https://arxiv.org/abs/2602.10718v3) | 2602.10718v3 | 6 |
| 2026-02-10 | [LLM-CoOpt: A Co-Design and Optimization Framework for Efficient LLM Inference on Heterogeneous Platforms](https://arxiv.org/abs/2602.09323v1) | 2602.09323v1 | 0 |
| 2026-01-20 | [LLMOrbit: A Circular Taxonomy of Large Language Models -From Scaling Walls to Agentic AI Systems](https://arxiv.org/abs/2601.14053v2) | 2601.14053v2 | 0 |
| 2026-01-16 | [MHA2MLA-VLM: Enabling DeepSeek's Economical Multi-Head Latent Attention across Vision-Language Models](https://arxiv.org/abs/2601.11464v1) | 2601.11464v1 | 12 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-16 | [Mixture of Attention Schemes (MoAS): Learning to Route Between MHA, GQA, and MQA](https://arxiv.org/abs/2512.20650v1) | 2512.20650v1 | 0 |
| 2025-11-02 | [Optimizing Native Sparse Attention with Latent Attention and Local Global Alternating Strategies](https://arxiv.org/abs/2511.00819v1) | 2511.00819v1 | 8 |
| 2025-10-30 | [Kimi Linear: An Expressive, Efficient Attention Architecture](https://arxiv.org/abs/2510.26692v2) | 2510.26692v2 | 10 |
| 2025-10-27 | [Knocking-Heads Attention](https://arxiv.org/abs/2510.23052v1) | 2510.23052v1 | 8 |
| 2025-10-02 | [Sparse Query Attention (SQA): A Computationally Efficient Attention Mechanism with Query Heads Reduction](https://arxiv.org/abs/2510.01817v1) | 2510.01817v1 | 9 |
| 2025-09-29 | [Muon: Training and Trade-offs with Latent Attention and MoE](https://arxiv.org/abs/2509.24406v1) | 2509.24406v1 | 8 |
| 2025-09-25 | [TyphoonMLA: A Mixed Naive-Absorb MLA Kernel For Shared Prefix](https://arxiv.org/abs/2509.21081v2) | 2509.21081v2 | 10 |
| 2025-09-24 | [AMLA: MUL by ADD in FlashAttention Rescaling](https://arxiv.org/abs/2509.25224v1) | 2509.25224v1 | 10 |
| 2025-09-20 | [EG-MLA: Embedding-Gated Multi-head Latent Attention for Scalable and Efficient LLMs](https://arxiv.org/abs/2509.16686v1) | 2509.16686v1 | 14 |
| 2025-08-21 | [TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill and Decode Inference](https://arxiv.org/abs/2508.15881v2) | 2508.15881v2 | 12 |
| 2025-08-02 | [Unifying Mixture of Experts and Multi-Head Latent Attention for Efficient Language Models](https://arxiv.org/abs/2508.01261v1) | 2508.01261v1 | 12 |
| 2025-07-23 | [PointLAMA: Latent Attention meets Mamba for Efficient Point Cloud Pretraining](https://arxiv.org/abs/2507.17296v1) | 2507.17296v1 | 8 |
| 2025-07-21 | [Rethinking LLM Inference Bottlenecks: Insights from Latent Attention and Mixture-of-Experts](https://arxiv.org/abs/2507.15465v3) | 2507.15465v3 | 12 |
| 2025-07-14 | [DeepSeek: Paradigm Shifts and Technical Evolution in Large AI Models](https://arxiv.org/abs/2507.09955v1) | 2507.09955v1 | 8 |
| 2025-07-12 | [A Random Matrix Theory Perspective on the Learning Dynamics of Multi-head Latent Attention](https://arxiv.org/abs/2507.09394v1) | 2507.09394v1 | 10 |
| 2025-07-10 | [SAS: Simulated Attention Score](https://arxiv.org/abs/2507.07694v2) | 2507.07694v2 | 9 |
| 2025-07-09 | [Attentions Under the Microscope: A Comparative Study of Resource Utilization for Variants of Self-Attention](https://arxiv.org/abs/2507.07247v2) | 2507.07247v2 | 10 |
| 2025-07-09 | [SpindleKV: A Novel KV Cache Reduction Method Balancing Both Shallow and Deep Layers](https://arxiv.org/abs/2507.06517v1) | 2507.06517v1 | 7 |
| 2025-06-15 | [GTA: Grouped-head latenT Attention](https://arxiv.org/abs/2506.17286v2) | 2506.17286v2 | 10 |
| 2025-06-03 | [Hardware-Centric Analysis of DeepSeek's Multi-Head Latent Attention](https://arxiv.org/abs/2506.02523v1) | 2506.02523v1 | 10 |
| 2025-05-30 | [HELM: Hyperbolic Large Language Models via Mixture-of-Curvature Experts](https://arxiv.org/abs/2505.24722v2) | 2505.24722v2 | 8 |
| 2025-05-27 | [Hardware-Efficient Attention for Fast Decoding](https://arxiv.org/abs/2505.21487v1) | 2505.21487v1 | 14 |
| 2025-05-22 | [Zebra-Llama: Towards Extremely Efficient Hybrid Models](https://arxiv.org/abs/2505.17272v2) | 2505.17272v2 | 11 |
| 2025-05-21 | [Hunyuan-TurboS: Advancing Large Language Models through Mamba-Transformer Synergy and Adaptive Chain-of-Thought](https://arxiv.org/abs/2505.15431v3) | 2505.15431v3 | 6 |
| 2025-05-19 | [Multi-head Temporal Latent Attention](https://arxiv.org/abs/2505.13544v3) | 2505.13544v3 | 7 |
| 2025-05-14 | [Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures](https://arxiv.org/abs/2505.09343v2) | 2505.09343v2 | 8 |
| 2025-05-13 | [FlashMLA-ETAP: Efficient Transpose Attention Pipeline for Accelerating MLA Inference on NVIDIA H20 GPUs](https://arxiv.org/abs/2506.01969v3) | 2506.01969v3 | 10 |
| 2025-03-14 | [X-EcoMLA: Upcycling Pre-Trained Attention into MLA for Efficient and Extreme KV Compression](https://arxiv.org/abs/2503.11132v4) | 2503.11132v4 | 12 |
| 2025-03-12 | [Cost-Optimal Grouped-Query Attention for Long-Context Modeling](https://arxiv.org/abs/2503.09579v3) | 2503.09579v3 | 8 |
| 2025-02-20 | [Towards Economical Inference: Enabling DeepSeek's Multi-Head Latent Attention in Any Transformer-based LLMs](https://arxiv.org/abs/2502.14837v2) | 2502.14837v2 | 16 |
| 2025-01-11 | [Tensor Product Attention Is All You Need](https://arxiv.org/abs/2501.06425v7) | 2501.06425v7 | 18 |
| 2025-01-07 | [Powerful Design of Small Vision Transformer on CIFAR10](https://arxiv.org/abs/2501.06220v1) | 2501.06220v1 | 8 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-30 | [Align Attention Heads Before Merging Them: An Effective Way for Converting MHA to GQA](https://arxiv.org/abs/2412.20677v2) | 2412.20677v2 | 7 |
| 2024-12-27 | [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437v2) | 2412.19437v2 | 8 |
| 2024-12-13 | [DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding](https://arxiv.org/abs/2412.10302v1) | 2412.10302v1 | 6 |
| 2024-07-15 | [Weighted Grouped Query Attention in Transformers](https://arxiv.org/abs/2407.10855v1) | 2407.10855v1 | 8 |
| 2024-06-21 | [Optimised Grouped-Query Attention Mechanism for Transformers](https://arxiv.org/abs/2406.14963v1) | 2406.14963v1 | 6 |
| 2024-06-13 | [MLKV: Multi-Layer Key-Value Heads for Memory Efficient Transformer Decoding](https://arxiv.org/abs/2406.09297v3) | 2406.09297v3 | 10 |
| 2024-06-11 | [Effectively Compress KV Heads for LLM](https://arxiv.org/abs/2406.07056v1) | 2406.07056v1 | 10 |
| 2024-05-21 | [Reducing Transformer Key-Value Cache Size with Cross-Layer Attention](https://arxiv.org/abs/2405.12981v1) | 2405.12981v1 | 13 |
| 2024-05-07 | [DeepSeek-V2: A Strong, Economical, and Efficient Mixture-of-Experts Language Model](https://arxiv.org/abs/2405.04434v5) | 2405.04434v5 | 10 |
| 2024-04-18 | [KV-weights are all you need for skipless transformers](https://arxiv.org/abs/2404.12362v2) | 2404.12362v2 | 8 |
| 2024-03-14 | [Dynamic Memory Compression: Retrofitting LLMs for Accelerated Inference](https://arxiv.org/abs/2403.09636v2) | 2403.09636v2 | 6 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-05-22 | [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245v3) | 2305.13245v3 | 8 |

<!-- table:end papers -->
