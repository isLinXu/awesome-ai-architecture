# ⚡ 高效注意力与长上下文（Efficient Attention & Long Context）

> O(n²) 太贵：稀疏、线性、滑窗，以及只读 top-k。

注意力变体压缩的是"每个 token 存多少"，这条赛道压缩的是"每个 query 看多少"：
固定稀疏模式（Longformer/BigBird）、低秩/核方法线性化（Linformer/Performer）、
IO 感知的精确计算（FlashAttention）、KV cache 驱逐与选择（H2O/SnapKV/Quest），
以及 2025 年后的可训练稀疏注意力（NSA/MoBA）。目标只有一个：长上下文想得起，也想得便宜。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Generating Long Sequences with Sparse Transformers | [1904.10509](https://arxiv.org/abs/1904.10509) | 2019 | 固定稀疏模式的开山之作 |
| Transformer-XL: Attentive Language Models Beyond a Fixed-Length Context | [1901.02860](https://arxiv.org/abs/1901.02860) | 2019 | 段级循环记忆：突破定长上下文的第一种范式 |
| Reformer: The Efficient Transformer | [2001.04451](https://arxiv.org/abs/2001.04451) | 2020 | LSH 注意力 + 可逆层，O(L log L) |
| Longformer: The Long-Document Transformer | [2004.05150](https://arxiv.org/abs/2004.05150) | 2020 | 滑窗 + 全局注意力的经典组合 |
| Linformer: Self-Attention with Linear Complexity | [2006.04768](https://arxiv.org/abs/2006.04768) | 2020 | 低秩投影把复杂度降到线性 |
| Transformers are RNNs: Fast Autoregressive Transformers with Linear Attention | [2006.16236](https://arxiv.org/abs/2006.16236) | 2020 | 核化线性注意力，推理即 RNN |
| Big Bird: Transformers for Longer Sequences | [2007.14062](https://arxiv.org/abs/2007.14062) | 2020 | 随机+窗口+全局稀疏，理论完备的长文档方案 |
| Rethinking Attention with Performers | [2009.14794](https://arxiv.org/abs/2009.14794) | 2020 | FAVOR+ 随机特征近似 softmax 注意力 |
| FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness | [2205.14135](https://arxiv.org/abs/2205.14135) | 2022 | 不改数学改访存：tiling + 重计算，精确注意力提速数倍 |
| FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning | [2307.08691](https://arxiv.org/abs/2307.08691) | 2023 | 更优的并行与 warp 分工，成为训练标配 kernel |
| Mistral 7B | [2310.06825](https://arxiv.org/abs/2310.06825) | 2023 | 滑窗注意力（SWA）生产化的标志性节点 |
| Efficient Streaming Language Models with Attention Sinks | [2309.17453](https://arxiv.org/abs/2309.17453) | 2023 | 发现 attention sink，流式长对话只需 sink + 滑窗 |
| H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | [2306.14048](https://arxiv.org/abs/2306.14048) | 2023 | 按注意力得分驱逐 KV cache |
| SnapKV: LLM Knows What You are Looking for Before Generation | [2404.14469](https://arxiv.org/abs/2404.14469) | 2024 | 用 prompt 尾部观测窗挑选重要 KV 位置 |
| Quest: Query-Aware Sparsity for Efficient Long-Context LLM Inference | [2406.10774](https://arxiv.org/abs/2406.10774) | 2024 | 页级 query-aware KV 选择，加速 decode |
| MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention | [2407.02490](https://arxiv.org/abs/2407.02490) | 2024 | 动态稀疏模式调度，加速 prefill 一个数量级 |
| FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision | [2407.08608](https://arxiv.org/abs/2407.08608) | 2024 | Hopper 异步 + FP8，kernel 榨干硬件的教科书 |
| Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention | [2502.11089](https://arxiv.org/abs/2502.11089) | 2025 | NSA：压缩/选择/滑窗三分支，稀疏注意力原生可训练 |
| MoBA: Mixture of Block Attention for Long-Context LLMs | [2502.13189](https://arxiv.org/abs/2502.13189) | 2025 | 把 MoE 思想搬到注意力：按块路由上下文 |

## 相关实现

- [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention) — FlashAttention 官方 CUDA/Triton 实现。
- [facebookresearch/xformers](https://github.com/facebookresearch/xformers) — 可组合的内存高效注意力算子库。
- [fla-org/flash-linear-attention](https://github.com/fla-org/flash-linear-attention) — 线性注意力/SSM/稀疏注意力的 Triton kernel 全家桶。

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-11 | [Keep Images in Sight: Visual Position Re-Anchoring for Long-Context MLLMs](https://arxiv.org/abs/2611.15100v1) | 2611.15100v1 | 7 |
| 2026-11-09 | [NearFormer: Linear-Size Sparse Attention via Randomized Near Neighbors](https://arxiv.org/abs/2611.12186v1) | 2611.12186v1 | 6 |
| 2026-11-09 | [Decode Token Parallelism: Memory-Efficient Distributed Attention Parallelism for Scalable LLM Decoding](https://arxiv.org/abs/2611.13293v1) | 2611.13293v1 | 6 |
| 2026-11-08 | [Verify Before You Fetch: Reliable KV Cache Compression for LLM Inference](https://arxiv.org/abs/2611.11319v1) | 2611.11319v1 | 7 |
| 2026-11-07 | [Coverage-Verified Sparse Attention: Closed-Loop Quality Control for Long-Context LLM Decoding](https://arxiv.org/abs/2611.10634v1) | 2611.10634v1 | 11 |
| 2026-11-07 | [ADIndex: Layer-Adaptive Sparse Attention Indexing via Group-Level Distillation](https://arxiv.org/abs/2611.12956v1) | 2611.12956v1 | 12 |
| 2026-11-06 | [Attend at the Right Resolution: Head-Adaptive Sparse Attention via Query-Key Interaction Structure](https://arxiv.org/abs/2611.09700v1) | 2611.09700v1 | 8 |
| 2026-11-06 | [Transformer-FSQ: Discrete Latents for Extreme KV-Cache Compression](https://arxiv.org/abs/2611.09598v1) | 2611.09598v1 | 6 |
| 2026-11-05 | [Muir: Linear Attention with Sensitivity-Allocated Gating and Matched-Filter Readout](https://arxiv.org/abs/2611.08376v1) | 2611.08376v1 | 6 |
| 2026-11-05 | [SPARE: Fast Linear Attention Decoding with Compact Recurrent States](https://arxiv.org/abs/2611.07552v1) | 2611.07552v1 | 6 |
| 2026-11-05 | [FlashOffloading: Low-Latency KV Cache Offloading for Long-Context LLM Serving](https://arxiv.org/abs/2611.07542v1) | 2611.07542v1 | 6 |
| 2026-11-04 | [Recursive Sparse Attention: Million-Token Length Extrapolation at Logarithmic Cost](https://arxiv.org/abs/2611.07232v1) | 2611.07232v1 | 6 |
| 2026-11-04 | [LowRAM: Low-Rank Keys and Amortised Values for Composable KV Cache Compression at Test-Time](https://arxiv.org/abs/2611.07025v1) | 2611.07025v1 | 3 |
| 2026-11-04 | [Systolic Linear Attention: Co-Designing Tile-Grouped Gated Delta Attention for TPUs](https://arxiv.org/abs/2611.06828v1) | 2611.06828v1 | 6 |
| 2026-11-04 | [Accelerating Long-Context Decoding in Large-Scale Hybrid LLMs Without Retraining](https://arxiv.org/abs/2611.06133v1) | 2611.06133v1 | 3 |
| 2026-11-04 | [DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion](https://arxiv.org/abs/2611.05917v1) | 2611.05917v1 | 6 |
| 2026-11-03 | [Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning](https://arxiv.org/abs/2611.06956v1) | 2611.06956v1 | 0 |
| 2026-11-03 | [LeanSparse: Memory-Efficient Serving for Native Sparse-Attention LLMs](https://arxiv.org/abs/2611.04671v1) | 2611.04671v1 | 0 |
| 2026-11-03 | [Coarse Semantic Blocks for Efficient Training-Free Sparse Attention](https://arxiv.org/abs/2611.04313v1) | 2611.04313v1 | 6 |
| 2026-11-02 | [Multi-layer Indexer: Overlapping Selection and Attention in DeepSeek Sparse Attention](https://arxiv.org/abs/2611.03768v1) | 2611.03768v1 | 6 |
| 2026-11-02 | [CISA: Retrofitting Dense Attention Models with Chunk-Indexed Sparse Attention](https://arxiv.org/abs/2611.03200v1) | 2611.03200v1 | 6 |
| 2026-11-02 | [SpecOPD: Branch-Parallel On-Policy Distillation for Speculative Decoding](https://arxiv.org/abs/2611.02846v1) | 2611.02846v1 | 0 |
| 2026-11-02 | [AttentionIndex: Accelerating Learned Sparse Attention with a Causal Inverted-File Index](https://arxiv.org/abs/2611.02508v1) | 2611.02508v1 | 6 |
| 2026-11-01 | [Who Asks, Who Answers: Linear Attention Builds the Query in Hybrid Language Models](https://arxiv.org/abs/2611.01909v1) | 2611.01909v1 | 6 |
| 2026-10-31 | [Step-dLLM: Adaptive Step-aware Sparse Attention for Efficient Diffusion LLM Inference](https://arxiv.org/abs/2611.01320v1) | 2611.01320v1 | 6 |
| 2026-10-30 | [TileWeave: Heterogeneous Tiling for Sparse Prefill on Mobile SoCs](https://arxiv.org/abs/2611.00408v1) | 2611.00408v1 | 0 |
| 2026-10-30 | [Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention](https://arxiv.org/abs/2610.42147v2) | 2610.42147v2 | 9 |
| 2026-10-30 | [Subquadratic Attention with a Hierarchical Tree-Structured Indexer](https://arxiv.org/abs/2610.42112v2) | 2610.42112v2 | 0 |
| 2026-10-30 | [DAMI: Dual-Axis Memory Initialization for Enhanced Long-Context Retrieval in Gated Linear Attention](https://arxiv.org/abs/2610.41994v2) | 2610.41994v2 | 9 |
| 2026-10-30 | [SparseGDN: Chunk Sparse in Linear Attention](https://arxiv.org/abs/2610.41420v1) | 2610.41420v1 | 6 |
| 2026-10-29 | [Low-Bit GDN Recurrent-State Quantization: Global Gradient-aware Allocation and Pure-Write Sliding Windows](https://arxiv.org/abs/2610.39931v1) | 2610.39931v1 | 0 |
| 2026-10-28 | [Dual DeltaNet: Value-Side Memory Reorganization for Linear Attention](https://arxiv.org/abs/2610.38578v1) | 2610.38578v1 | 6 |
| 2026-10-27 | [Multi-State Linear Attention with Generalized Second-Order Routing](https://arxiv.org/abs/2610.37645v1) | 2610.37645v1 | 6 |
| 2026-10-26 | [MCF: A Memory- and Communication-Aware Co-Designed Framework for Long-Context LLM Inference](https://arxiv.org/abs/2610.34731v1) | 2610.34731v1 | 3 |
| 2026-10-25 | [INTRA: Interleaved Non-contiguous Token spaRse Attention](https://arxiv.org/abs/2610.34056v2) | 2610.34056v2 | 6 |
| 2026-10-24 | [Cross-Scale Sparse Attention for Referring Segmentation in Remote Sensing](https://arxiv.org/abs/2610.33551v1) | 2610.33551v1 | 6 |
| 2026-10-23 | [HyScale: Scaling Long-Context Training for Learned Sparse Attention](https://arxiv.org/abs/2610.32057v3) | 2610.32057v3 | 9 |
| 2026-10-22 | [LazyFlash: Forward-Dense, Backward-Sparse Attention for Accelerated Long-Context Fine-Tuning](https://arxiv.org/abs/2610.31911v1) | 2610.31911v1 | 9 |
| 2026-10-22 | [RIFT: KV Cache Compression for Draft Models with Complementary Compressibility Training](https://arxiv.org/abs/2610.31098v1) | 2610.31098v1 | 3 |
| 2026-10-22 | [OpenAttention: One Percent Is Enough with Tail Proxies](https://arxiv.org/abs/2610.30951v3) | 2610.30951v3 | 0 |
| 2026-10-21 | [UlaCache: Unified Logical Addressing for Sparse LLM Serving](https://arxiv.org/abs/2610.29820v2) | 2610.29820v2 | 0 |
| 2026-10-21 | [Sparsity Should Be ALLOTted by Output: Training-Free Allocation of Block-Sparse Attention for Video Diffusion Transformers](https://arxiv.org/abs/2610.29441v1) | 2610.29441v1 | 6 |
| 2026-10-20 | [Building AI Research Teams for Autonomous Discovery of Linear Attention Architectures](https://arxiv.org/abs/2610.28887v1) | 2610.28887v1 | 6 |
| 2026-10-20 | [Stratified Sparse Attention: Reducing the Sparse-to-Dense Gap at Extreme Sparsity](https://arxiv.org/abs/2610.28441v1) | 2610.28441v1 | 6 |
| 2026-10-20 | [Local Inference of LLMs on Long Contexts: A Data Systems Perspective](https://arxiv.org/abs/2610.28223v1) | 2610.28223v1 | 3 |
| 2026-10-20 | [KPage: Cross-Block Page Compaction for Hardware-Efficient Sparse Attention](https://arxiv.org/abs/2610.28096v1) | 2610.28096v1 | 6 |
| 2026-10-20 | [MLIPS: Multi-Layer Indexer Pool Sharing](https://arxiv.org/abs/2610.27438v2) | 2610.27438v2 | 0 |
| 2026-10-19 | [Kronecker Delta Rule for Long Context Linear Attention](https://arxiv.org/abs/2610.26834v1) | 2610.26834v1 | 9 |
| 2026-10-19 | [Dynamics-Aware Sparse Attention for Efficient Autoregressive Video Diffusion](https://arxiv.org/abs/2610.26262v1) | 2610.26262v1 | 6 |
| 2026-10-19 | [RECAP: Reciprocal Sparse Attention and Hierarchical Caching for Efficient Video Diffusion](https://arxiv.org/abs/2610.26244v1) | 2610.26244v1 | 6 |
| 2026-10-18 | [Improving the Expressive Power of Hybrid Sequence Models via Multi-Hop Retrieval](https://arxiv.org/abs/2610.25250v1) | 2610.25250v1 | 0 |
| 2026-10-18 | [Certified Sparse Attention via Perturbed Retrieval](https://arxiv.org/abs/2610.24991v1) | 2610.24991v1 | 6 |
| 2026-10-17 | [TideKV: Delayed KV Eviction via Layer-Wise Chunked Prefill for Memory-Efficient Long-Context LLM Inference](https://arxiv.org/abs/2610.24499v1) | 2610.24499v1 | 3 |
| 2026-10-16 | [Prism Attention: Proposal-Refined Index Sharing Mechanism for Efficient LLMs Inference](https://arxiv.org/abs/2610.22985v1) | 2610.22985v1 | 0 |
| 2026-10-15 | [Beyond Context Length: Characterising the Difficulty of Long-Context Reasoning](https://arxiv.org/abs/2610.22067v1) | 2610.22067v1 | 6 |
| 2026-10-15 | [From Long Context to Selective Memory:A Survey of Memory-Centric Compression for Large Language Models](https://arxiv.org/abs/2610.21165v1) | 2610.21165v1 | 3 |
| 2026-10-15 | [Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search](https://arxiv.org/abs/2610.21129v1) | 2610.21129v1 | 6 |
| 2026-10-14 | [ReaDy: Recurrent States as Dynamic Context for Speculative Drafting in Hybrid Linear Attention Large Language Models](https://arxiv.org/abs/2610.20503v2) | 2610.20503v2 | 6 |
| 2026-10-13 | [Titan-Llama: Retrofitting Pre-trained LLMs with External Neural Memory Modules](https://arxiv.org/abs/2610.19210v1) | 2610.19210v1 | 0 |
| 2026-10-12 | [In-context classification: Calibration and noise in linear attention with softmax readout](https://arxiv.org/abs/2610.17061v1) | 2610.17061v1 | 8 |
| 2026-10-10 | [Competition Domains Matter: Selective Head Globalization for Training-Free Sparse Attention in Video Diffusion Transformers](https://arxiv.org/abs/2610.14672v1) | 2610.14672v1 | 6 |
| 2026-10-09 | [Learnable Low-Rank Polynomial Sketch for Effective Linear Attention](https://arxiv.org/abs/2610.14219v1) | 2610.14219v1 | 8 |
| 2026-10-09 | [Orthros: Phase-Aware Heterogeneous Attention for Efficient Transformers](https://arxiv.org/abs/2610.13735v1) | 2610.13735v1 | 6 |
| 2026-10-09 | [S$^3$R: Fast and Faithful RL Rollouts via Self-Sparse Speculative Decoding](https://arxiv.org/abs/2610.13202v2) | 2610.13202v2 | 8 |
| 2026-10-09 | [DP-MIND: Differentially private memory-guided Long context Inference](https://arxiv.org/abs/2610.13132v1) | 2610.13132v1 | 7 |
| 2026-10-08 | [BioBigBird: A Sparse Attention Model for Long-Range Dependency Processing in Biomedical Text](https://arxiv.org/abs/2610.11430v1) | 2610.11430v1 | 8 |
| 2026-10-08 | [iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity](https://arxiv.org/abs/2610.11302v2) | 2610.11302v2 | 6 |
| 2026-10-08 | [Bridging KV-Cache Quantization and Linear Attention: From Theory to Pretrained Weight Migration](https://arxiv.org/abs/2610.11214v1) | 2610.11214v1 | 6 |
| 2026-10-08 | [PageWeaver: KV-Guided Query Unions for Sparse Attention](https://arxiv.org/abs/2610.11201v1) | 2610.11201v1 | 6 |
| 2026-10-08 | [QUILT: Rethinking Sparse-Attention Prefill through Shared Query Execution](https://arxiv.org/abs/2610.11134v1) | 2610.11134v1 | 6 |
| 2026-10-07 | [Sparse Attention Is Matrix Approximation, Not Choosing from a Bag of Values](https://arxiv.org/abs/2610.10871v1) | 2610.10871v1 | 6 |
| 2026-10-07 | [What can linear attention learn from nonlinear teachers in-context?](https://arxiv.org/abs/2610.10761v1) | 2610.10761v1 | 6 |
| 2026-10-07 | [Attention via Black-Box Vector Search](https://arxiv.org/abs/2610.10135v2) | 2610.10135v2 | 6 |
| 2026-10-07 | [Mechanics of Long-Context Hybrid Models Part 1.1: From Hybrid Attention to Hybrid Position](https://arxiv.org/abs/2610.10114v1) | 2610.10114v1 | 9 |
| 2026-10-07 | [Dual-QK: Sharp Queries and Flat Keys for Prunable 2-bit KV Caches](https://arxiv.org/abs/2610.09827v1) | 2610.09827v1 | 7 |
| 2026-10-06 | [SPIN: Shadow Predictive Indexer for Sparse Attention](https://arxiv.org/abs/2610.09025v3) | 2610.09025v3 | 12 |
| 2026-10-06 | [Backend-Agnostic Sparse Attention for Fast High-Resolution Visual Generation](https://arxiv.org/abs/2610.08772v3) | 2610.08772v3 | 6 |
| 2026-10-05 | [MC-Sparse: Deconstructing and Closing the Dense-Sparse Attention Gap in Diffusion Transformers](https://arxiv.org/abs/2610.06801v1) | 2610.06801v1 | 6 |
| 2026-10-05 | [OVAL: Output-Aware Local Page Bases for KV Cache Retrieval](https://arxiv.org/abs/2610.06686v1) | 2610.06686v1 | 9 |
| 2026-10-05 | [HLA: Expressive Hybrid Linear Attention via Chunk-Wise Dynamic Mixing](https://arxiv.org/abs/2610.05842v1) | 2610.05842v1 | 8 |
| 2026-10-05 | [HLA-WM: Hybrid Linear Attention for Long-Horizon Video World Models](https://arxiv.org/abs/2610.05739v1) | 2610.05739v1 | 8 |
| 2026-10-04 | [Prism: Dynamic Sparse Attention for Native 2K Joint Video-Audio Generation Model Training](https://arxiv.org/abs/2610.05416v1) | 2610.05416v1 | 6 |
| 2026-10-03 | [More Value per Key: Asymmetric Sparse Attention for Faster LLM Decoding](https://arxiv.org/abs/2610.04753v2) | 2610.04753v2 | 8 |
| 2026-10-03 | [LatentIndex: Cross-Layer Sharing with Layer-Specific Selection for Sparse Attention](https://arxiv.org/abs/2610.04635v1) | 2610.04635v1 | 6 |
| 2026-10-03 | [On the Trade-off Between Information Loss and Generalization in Sparse Attention](https://arxiv.org/abs/2610.04424v2) | 2610.04424v2 | 6 |
| 2026-10-03 | [AttSVD:Prompt-Adaptive Low-Rank KV Cache Compression via Attention-Guided SVD](https://arxiv.org/abs/2610.06927v1) | 2610.06927v1 | 7 |
| 2026-10-02 | [SlimKV: Joint Token-Feature KV Cache Compression with Reconstruction-Free Beacon Attention](https://arxiv.org/abs/2610.02953v1) | 2610.02953v1 | 7 |
| 2026-10-02 | [Gated Slot Attention-2: Two-Sided Associative Memory Correction in Linear Attention](https://arxiv.org/abs/2610.02816v1) | 2610.02816v1 | 6 |
| 2026-10-01 | [In-context Learning of Single-index Targets: Comparing Kernel and Feature Learners](https://arxiv.org/abs/2610.01712v1) | 2610.01712v1 | 6 |
| 2026-10-01 | [HHR: Hierarchical Hash Retrieval for Efficient LLM Generation](https://arxiv.org/abs/2610.01230v2) | 2610.01230v2 | 8 |
| 2026-10-01 | [VASC: Value-Aware Sparse Attention with Cross-Layer Memory for Efficient 3D Reconstruction](https://arxiv.org/abs/2610.01013v1) | 2610.01013v1 | 6 |
| 2026-09-30 | [CommunityKV: Efficient Long-Context Decoding via Graph Partitioning](https://arxiv.org/abs/2610.00418v1) | 2610.00418v1 | 9 |
| 2026-09-30 | [SparseEngine: Sparse-First Inference Engine](https://arxiv.org/abs/2609.39068v1) | 2609.39068v1 | 6 |
| 2026-09-30 | [Switching Linear Attention](https://arxiv.org/abs/2609.39034v1) | 2609.39034v1 | 7 |
| 2026-09-30 | [PARK: Accurate Block Retrieval for Sparse Attention in Video Diffusion Transformers](https://arxiv.org/abs/2609.38978v1) | 2609.38978v1 | 6 |
| 2026-09-30 | [SparLeak: Privacy Leakage from Sparse Attention in LLM Inference on Shared GPUs](https://arxiv.org/abs/2609.38830v1) | 2609.38830v1 | 8 |
| 2026-09-29 | [STEPQuant: When and Where Errors Matter in Delta-Rule Recurrent State Quantization](https://arxiv.org/abs/2609.38169v1) | 2609.38169v1 | 6 |
| 2026-09-29 | [LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization](https://arxiv.org/abs/2609.38166v1) | 2609.38166v1 | 8 |
| 2026-09-29 | [WUSH-KV: KV Cache Quantization with Data-Adaptive Transforms](https://arxiv.org/abs/2609.38121v1) | 2609.38121v1 | 7 |
| 2026-09-29 | [How Local Mixing Encodes Relative Position in Global NoPE Attention](https://arxiv.org/abs/2609.38109v1) | 2609.38109v1 | 8 |
| 2026-09-29 | [AVSG: Accelerated Vectorized Sparse Gather for Efficient KV Cache Offload in Sparse-Attention LLM Serving](https://arxiv.org/abs/2609.37538v2) | 2609.37538v2 | 9 |
| 2026-09-29 | [ReMem: Rethinking Perception and Memory in Long-Context Recommendation Agents](https://arxiv.org/abs/2609.37311v2) | 2609.37311v2 | 7 |
| 2026-09-29 | [Efficient Agentic LLM Serving over SSD-based Sparse KV Storage](https://arxiv.org/abs/2609.36938v1) | 2609.36938v1 | 6 |
| 2026-09-29 | [Triadic Linear Attention: Three-Dimensional Recurrent States for Long-Context Sequence Modeling](https://arxiv.org/abs/2609.36529v1) | 2609.36529v1 | 9 |
| 2026-09-28 | [Adapting Linear-Time Architectures for Tabular In-Context Learning](https://arxiv.org/abs/2609.36337v1) | 2609.36337v1 | 6 |
| 2026-09-28 | [SMat-Attention: Structured Long-Context Sequence Modeling](https://arxiv.org/abs/2609.36062v1) | 2609.36062v1 | 7 |
| 2026-09-28 | [MS-GLA: Multi-Scale Gated Linear Attention for Addressing Representational Bottlenecks via Multi-Temporal Resolution](https://arxiv.org/abs/2609.35664v2) | 2609.35664v2 | 8 |
| 2026-09-28 | [Cartridges++: KV Cache Compression without Off-Context Derailment](https://arxiv.org/abs/2609.35621v1) | 2609.35621v1 | 7 |
| 2026-09-28 | [ReSS: Residual-Restoring Sparse Attention for 3D Vision Transformers](https://arxiv.org/abs/2609.35593v1) | 2609.35593v1 | 6 |
| 2026-09-28 | [WaveAlign: Cache-Aware Query-Row Scheduling for Sparse Attention in Long-Video Generation](https://arxiv.org/abs/2609.34814v1) | 2609.34814v1 | 6 |
| 2026-09-28 | [OmniTide: Co-Designing Algorithms and Systems for Efficient On-Device Omni-LLM Streaming](https://arxiv.org/abs/2609.34653v2) | 2609.34653v2 | 6 |
| 2026-09-28 | [SPIMOE: Exploiting Hybrid Sparsity for Reasoning MoE Inference on Heterogeneous PIM Architectures](https://arxiv.org/abs/2609.34612v1) | 2609.34612v1 | 6 |
| 2026-09-28 | [WorldAttention: An Efficient Attention Architecture for Interactive Video World Models](https://arxiv.org/abs/2609.34606v1) | 2609.34606v1 | 6 |
| 2026-09-28 | [PulseInfer: I/O-Centric Sparse KV Cache Offloading for Efficient Long-Context LLM Decoding](https://arxiv.org/abs/2609.34555v1) | 2609.34555v1 | 6 |
| 2026-09-27 | [PQ-HSA: Reusing Product-Quantized Scores for Hybrid Sparse-Approximate Attention](https://arxiv.org/abs/2609.33746v1) | 2609.33746v1 | 10 |
| 2026-09-27 | [FoldAttention: Declared-Reference Softmax for Fast Decode and Deterministic Backward](https://arxiv.org/abs/2609.33410v1) | 2609.33410v1 | 6 |
| 2026-09-27 | [How Linear Attention Remembers](https://arxiv.org/abs/2609.33093v1) | 2609.33093v1 | 8 |
| 2026-09-26 | [Improving Video Sparse Attention with Fine-grained Router and Sparse Rebasing](https://arxiv.org/abs/2609.32882v1) | 2609.32882v1 | 6 |
| 2026-09-26 | [DoSA: Dots Sparse Attention](https://arxiv.org/abs/2610.13990v1) | 2610.13990v1 | 6 |
| 2026-09-26 | [Distance-KV: Exploiting Relative Distance for Efficient Long-Context Inference](https://arxiv.org/abs/2609.32663v1) | 2609.32663v1 | 10 |
| 2026-09-26 | [Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs](https://arxiv.org/abs/2609.32259v2) | 2609.32259v2 | 7 |
| 2026-09-25 | [On-Policy Attention Linearization](https://arxiv.org/abs/2609.31947v1) | 2609.31947v1 | 6 |
| 2026-09-25 | [Block Sparse Attention with Log-Linear Complexity](https://arxiv.org/abs/2609.31093v1) | 2609.31093v1 | 8 |
| 2026-09-25 | [The KV Cache Is the New Memory Wall](https://arxiv.org/abs/2609.30854v1) | 2609.30854v1 | 7 |
| 2026-09-24 | [FlashLoop: Fast and Memory-Efficient Looped Transformers via Lazy Updates](https://arxiv.org/abs/2609.29812v2) | 2609.29812v2 | 6 |
| 2026-09-23 | [DeltaS: Reading the Gated Linear Attention State for KV Cache Eviction in Streaming Video](https://arxiv.org/abs/2609.27470v1) | 2609.27470v1 | 11 |
| 2026-09-22 | [HySparse2: Hybrid Sparse Attention with Two-Level KV Sharing](https://arxiv.org/abs/2609.26368v1) | 2609.26368v1 | 10 |
| 2026-09-22 | [CompKV: Compensation-Aware KV Selection for Long-Context LLM Inference](https://arxiv.org/abs/2609.26300v1) | 2609.26300v1 | 9 |
| 2026-09-22 | [Decoupling Logical Masks from GPU Execution for Dynamic Block-Sparse Attention](https://arxiv.org/abs/2609.25869v1) | 2609.25869v1 | 6 |
| 2026-09-21 | [Opinion Leader Dynamics: How Sparse Attention Shapes Token Clustering](https://arxiv.org/abs/2609.24202v1) | 2609.24202v1 | 6 |
| 2026-09-20 | [SPLASH: Co-Designing Sparse Attention with High-Bandwidth Flash for Efficient Long-Context Inference](https://arxiv.org/abs/2609.23816v1) | 2609.23816v1 | 13 |
| 2026-09-19 | [Block-Sparse Attention with Semantic-Geometric Decoupled Routing](https://arxiv.org/abs/2609.22884v1) | 2609.22884v1 | 10 |
| 2026-09-18 | [Rethinking Vision Architectures with Gated Linear Attention and KAN](https://arxiv.org/abs/2609.22506v3) | 2609.22506v3 | 6 |
| 2026-09-18 | [TierKV: Long-Context On-Device LLMs via Predictive Multi-Tier KV Caching](https://arxiv.org/abs/2609.21172v2) | 2609.21172v2 | 7 |
| 2026-09-17 | [DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression](https://arxiv.org/abs/2609.19969v1) | 2609.19969v1 | 9 |
| 2026-09-17 | [Understanding and Exploiting Diagonal Attention Sparsity in Autoregressive Image Generation](https://arxiv.org/abs/2609.19702v1) | 2609.19702v1 | 6 |
| 2026-09-16 | [Elastic Threshold Attention: Learned Contextual Sparsity for Long-Context Decoding](https://arxiv.org/abs/2609.20888v2) | 2609.20888v2 | 11 |
| 2026-09-16 | [ASPIRE: Asynchronous Batched Self-Speculative Decoding for Long-Context LLM Inference](https://arxiv.org/abs/2609.17943v1) | 2609.17943v1 | 7 |
| 2026-09-15 | [The Inference Engineering Pareto Atlas: Which Optimizations Dominate the Cost, Quality, and Latency Frontier?](https://arxiv.org/abs/2609.17863v1) | 2609.17863v1 | 6 |
| 2026-09-13 | [Physically Partitioned KVCache Format for CPU--GPU Load Balancing in MoE Inference](https://arxiv.org/abs/2609.14507v1) | 2609.14507v1 | 10 |
| 2026-09-13 | [SpectralShift: Effective Context Window Extension of Gated DeltaNet via Spectral Reparameterization](https://arxiv.org/abs/2609.14320v1) | 2609.14320v1 | 6 |
| 2026-09-13 | [Flattening Every Memory Peak in Long-Context Mixture-of-Experts Training](https://arxiv.org/abs/2609.14306v1) | 2609.14306v1 | 7 |
| 2026-09-11 | [SAS: Simple Attention Sparsification via End-to-End Optimization of Context Ranking](https://arxiv.org/abs/2609.13141v1) | 2609.13141v1 | 6 |
| 2026-09-11 | [Rethinking Heterogeneous System Disaggregation for Subquadratic Attention](https://arxiv.org/abs/2609.13134v1) | 2609.13134v1 | 6 |
| 2026-09-11 | [RunningTensor: Generalizing Linear Attention to Higher-Order Recurrent States](https://arxiv.org/abs/2609.12814v1) | 2609.12814v1 | 6 |
| 2026-09-11 | [Residual Vector-based Reconstruction as Long-Context Recall Regardless of Context Window Size](https://arxiv.org/abs/2609.12686v1) | 2609.12686v1 | 7 |
| 2026-09-09 | [AMEND: Audited Margins Enable Nonblocking Drops in GPU-PIM LLM Decoding](https://arxiv.org/abs/2609.09823v1) | 2609.09823v1 | 6 |
| 2026-09-09 | [Fine-Tuning a KV Cache Concatenation-Aware Model or Recomputing KV Caches? Why Not Both?](https://arxiv.org/abs/2609.09768v1) | 2609.09768v1 | 7 |
| 2026-09-08 | [Sample-Guided Exact Top-K Selection for Long-Context Sparse Attention](https://arxiv.org/abs/2609.08450v1) | 2609.08450v1 | 9 |
| 2026-09-07 | [Kalman Delta Networks: Uncertainty-aware Associative Memory](https://arxiv.org/abs/2609.07816v2) | 2609.07816v2 | 6 |
| 2026-09-07 | [RouteRelay: Event-Triggered Cross-Layer Route Reuse for Efficient Dynamic Sparse Attention](https://arxiv.org/abs/2609.07306v1) | 2609.07306v1 | 8 |
| 2026-09-07 | [CEDAR: Error-Bounded Residual Routing for Efficient Long-Context Attention](https://arxiv.org/abs/2609.07237v1) | 2609.07237v1 | 7 |
| 2026-09-04 | [Interface-Aware KV Cache Quantization for Dense On-Chip NVM in Long-Context LLM Decoding](https://arxiv.org/abs/2609.05764v1) | 2609.05764v1 | 6 |
| 2026-09-03 | [VestigeKV: The NoPE-MLA KV Cache Carries Its Own Sparse-Attention Signal in a Vestigial Branch](https://arxiv.org/abs/2609.03949v2) | 2609.03949v2 | 7 |
| 2026-09-02 | [Language Models Can Control Their Own Attention](https://arxiv.org/abs/2609.02737v2) | 2609.02737v2 | 8 |
| 2026-09-02 | [Modern Transformers Are Implicit Hybrids: From Functional Differentiation to Principled Hybrid Architecture Design](https://arxiv.org/abs/2609.02986v2) | 2609.02986v2 | 6 |
| 2026-09-02 | [HeadWiseKV: Budgeted Per-Head Cache Residency for Hybrid Long-Context Language Models](https://arxiv.org/abs/2609.02029v1) | 2609.02029v1 | 7 |
| 2026-09-01 | [CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing](https://arxiv.org/abs/2609.01925v1) | 2609.01925v1 | 8 |
| 2026-08-31 | [Can Video World Models Track Unobserved World States?](https://arxiv.org/abs/2608.30692v2) | 2608.30692v2 | 6 |
| 2026-08-31 | [Event-Driven Language Models with Sparse Neural Activity for Neuromorphic Hardware](https://arxiv.org/abs/2608.30439v1) | 2608.30439v1 | 6 |
| 2026-08-31 | [Tail-Replay: Escaping the Curse of Linear Attention in Prefix Caching for Hybrid LLMs](https://arxiv.org/abs/2608.30310v2) | 2608.30310v2 | 8 |
| 2026-08-31 | [CateKV: On Sequential Consistency for Long-Context LLM Inference Acceleration](https://arxiv.org/abs/2608.30295v1) | 2608.30295v1 | 7 |
| 2026-08-31 | [Strong Drafts Need Compact Memories: Long-Context Speculative Decoding with Compressed KV Cache](https://arxiv.org/abs/2608.30252v1) | 2608.30252v1 | 6 |
| 2026-08-31 | [A.X K2 Technical Report](https://arxiv.org/abs/2608.30181v1) | 2608.30181v1 | 8 |
| 2026-08-31 | [Efficient and High-Quality Depth Estimation via Pixel-Space Diffusion with Linear Attention](https://arxiv.org/abs/2608.30129v1) | 2608.30129v1 | 6 |
| 2026-08-30 | [REIGN: Refurbished Embeddings with Integrated Guidance Networks for Efficient Context-Length Scaling](https://arxiv.org/abs/2608.29899v2) | 2608.29899v2 | 6 |
| 2026-08-29 | [RouteSparse: Input-Conditional Pattern Routing for Budgeted Long-Context Prefilling](https://arxiv.org/abs/2608.29058v1) | 2608.29058v1 | 7 |
| 2026-08-28 | [SemKV: Semantic Mixed-Precision KV Cache Quantization Guided by the Quality Cliff for Long-Context LLM Inference](https://arxiv.org/abs/2608.28911v1) | 2608.28911v1 | 8 |
| 2026-08-28 | [Sliding-window beats linear attention](https://arxiv.org/abs/2608.28444v2) | 2608.28444v2 | 14 |
| 2026-08-26 | [Visual Representation and History Modeling for Navigation World Models](https://arxiv.org/abs/2609.29555v1) | 2609.29555v1 | 8 |
| 2026-08-24 | [PuzzleKV: Page-Wise Low-Rank Decomposition for KV Cache Compression](https://arxiv.org/abs/2608.23843v1) | 2608.23843v1 | 7 |
| 2026-08-22 | [Benchmarking Composable Compression Techniques in Mixture-of-Experts LLMs](https://arxiv.org/abs/2608.21693v1) | 2608.21693v1 | 8 |
| 2026-08-20 | [Learning how to Forget: Fine-tuning for Long-Context Sparse Attention](https://arxiv.org/abs/2608.19920v2) | 2608.19920v2 | 11 |
| 2026-08-20 | [FlashPrefill V2: Block-Sparse Prefill Attention for Long-Context LLM Serving](https://arxiv.org/abs/2608.19758v1) | 2608.19758v1 | 11 |
| 2026-08-19 | [Partition the Support, Reconstruct the Residual: Training-Free Sparse Attention for Video Generation and World Models](https://arxiv.org/abs/2608.18484v2) | 2608.18484v2 | 6 |
| 2026-08-18 | [MoNe: Modular Neural Memory for Efficient Long Context Inference](https://arxiv.org/abs/2608.17616v1) | 2608.17616v1 | 7 |
| 2026-08-17 | [Proteus: Incremental Memory Activation for Long-Context Sequence Modeling](https://arxiv.org/abs/2608.16844v1) | 2608.16844v1 | 7 |
| 2026-08-16 | [DeltaLog: Deferred Materialization of Recurrent States for Linear Attention Decoding](https://arxiv.org/abs/2608.15533v1) | 2608.15533v1 | 8 |
| 2026-08-16 | [Efficient Audio-Visual Generation via Synchrony-Aware Cross-Modal Sparse Attention](https://arxiv.org/abs/2608.15522v1) | 2608.15522v1 | 6 |
| 2026-08-16 | [Not All Attention Is Equal: A Quantitative Survey of the EEI Trade-off](https://arxiv.org/abs/2608.15459v1) | 2608.15459v1 | 8 |
| 2026-08-13 | [The Query Knows What to Forget: A Second Erase Direction for Linear Attention](https://arxiv.org/abs/2608.13668v1) | 2608.13668v1 | 10 |
| 2026-08-12 | [Massive Activations in Hybrid Linear Attention Large Language Models: Pre-Attention Spikes and Inter-Spike Plateaus](https://arxiv.org/abs/2608.12149v3) | 2608.12149v3 | 6 |
| 2026-08-12 | [MARCH: Scaling Recurrent Memory with Content-Routed State Anchors](https://arxiv.org/abs/2608.12435v1) | 2608.12435v1 | 8 |
| 2026-08-12 | [LoSA: Near-Lossless Sparse Attention for Training-Free Video Diffusion Acceleration](https://arxiv.org/abs/2608.12032v1) | 2608.12032v1 | 6 |
| 2026-08-11 | [SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](https://arxiv.org/abs/2608.10519v3) | 2608.10519v3 | 6 |
| 2026-08-10 | [Cracks in the Foundation: Seemingly Minor Architectural Choices Impact Long Context Extension](https://arxiv.org/abs/2608.10296v1) | 2608.10296v1 | 11 |
| 2026-08-10 | [MixFormer: Linear Transformer with Mixture of Memory Experts](https://arxiv.org/abs/2608.09468v1) | 2608.09468v1 | 6 |
| 2026-08-09 | [Sparse Attention to Emotion: Efficient Facial Emotion Recognition via Token Reduction](https://arxiv.org/abs/2608.08873v1) | 2608.08873v1 | 6 |
| 2026-08-09 | [VoxZip: Semantic-Anchored Temporal KV Cache Compression for Long-Context Audio Inference](https://arxiv.org/abs/2608.08569v1) | 2608.08569v1 | 6 |
| 2026-08-09 | [MotionCraft: Latent World Modeling with Sparse Attention for Visual Upscaling](https://arxiv.org/abs/2608.08553v1) | 2608.08553v1 | 6 |
| 2026-08-08 | [SPECTRA: Pushing the KV Cache Beyond the 2-Bit Cliff via Spectral Transform Coding](https://arxiv.org/abs/2608.07915v1) | 2608.07915v1 | 7 |
| 2026-08-07 | [CoinRAG: Contextualized Information Nugget KV Cache Reuse for Long-Context RAG](https://arxiv.org/abs/2608.07458v2) | 2608.07458v2 | 6 |
| 2026-08-07 | [HiSparse: Scaling Sparse-Attention Decoding with Hierarchical KV Cache Management](https://arxiv.org/abs/2608.07009v1) | 2608.07009v1 | 11 |
| 2026-08-07 | [Every Cache Entry Earns Its Place: Global Allocation of Resolution and Coverage for KV Cache Compression](https://arxiv.org/abs/2608.07001v2) | 2608.07001v2 | 7 |
| 2026-08-07 | [Autonomy-of-Heads: Data-Free Sparse Attention from Frozen Query-Key Geometry](https://arxiv.org/abs/2608.06849v1) | 2608.06849v1 | 8 |
| 2026-08-07 | [StateFlow: Sequence Pipeline Parallelism for Long-Context Modeling with Linear Recurrence](https://arxiv.org/abs/2608.06838v1) | 2608.06838v1 | 9 |
| 2026-08-07 | [HSMLA: Hierarchical Softmax Multi-scale Linear Attention for Efficient Vision Transformers](https://arxiv.org/abs/2608.07616v2) | 2608.07616v2 | 6 |
| 2026-08-06 | [Retrofitting Linear Attention into Diffusion Language Models](https://arxiv.org/abs/2608.06628v1) | 2608.06628v1 | 6 |
| 2026-08-06 | [Evidence-Driven Dynamic Visual Selector for Efficient Long Video Understanding](https://arxiv.org/abs/2608.05780v1) | 2608.05780v1 | 6 |
| 2026-08-05 | [Training-Free Hashing-Based Attention via Binary Principal Components](https://arxiv.org/abs/2608.04405v1) | 2608.04405v1 | 6 |
| 2026-08-04 | [Heterogeneous LLM Serving with General-Purpose Processing-Near-Memory for Retrieval-Based Sparse Attention](https://arxiv.org/abs/2608.03555v1) | 2608.03555v1 | 10 |
| 2026-08-04 | [SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335v1) | 2608.03335v1 | 6 |
| 2026-08-04 | [TaskPress: Query-Agnostic KV Cache Compression via Task-Guided Pruning](https://arxiv.org/abs/2608.03276v2) | 2608.03276v2 | 7 |
| 2026-08-03 | [Mamba with Hierarchical Memory: Solving Representation Bottleneck in Long Sequence Modeling](https://arxiv.org/abs/2608.02347v2) | 2608.02347v2 | 6 |
| 2026-08-03 | [DART: Decoded Attention over Recurrent States for Efficient Long-Context Sequence Modeling](https://arxiv.org/abs/2608.02032v1) | 2608.02032v1 | 7 |
| 2026-08-03 | [Understanding Sparse Attention Selectivity in Long-Context Foundation Models via Counterfactual Evaluation](https://arxiv.org/abs/2608.01676v1) | 2608.01676v1 | 13 |
| 2026-08-03 | [LongCat Sparse Attention: Taming the Lightning via Streaming-aware Hierarchical Cross-Layer Indexing](https://arxiv.org/abs/2608.01662v2) | 2608.01662v2 | 10 |
| 2026-08-03 | [Twig: Parallel and Memory-Efficient Tree Speculative Decoding for Hybrid-Attention LLMs](https://arxiv.org/abs/2608.01651v2) | 2608.01651v2 | 8 |
| 2026-07-30 | [GroupKV: Hierarchical KV Cache Management for Long-Context Diffusion LLM Inference](https://arxiv.org/abs/2609.17573v1) | 2609.17573v1 | 8 |
| 2026-07-30 | [S-CEReBrO: Breaking the Memory Barrier in Continuous EEG Monitoring](https://arxiv.org/abs/2607.27913v3) | 2607.27913v3 | 6 |
| 2026-07-30 | [Recall Before You Rank: Similarity-Guided Top-$K$ Reuse for Efficient Long-Context Attention](https://arxiv.org/abs/2607.27692v1) | 2607.27692v1 | 11 |
| 2026-07-29 | [NELSSA: A GPU-PNM Heterogeneous System for Mixed-Length LLM Serving via Length-based Request Placement](https://arxiv.org/abs/2607.26633v1) | 2607.26633v1 | 8 |
| 2026-07-29 | [DualDecoder: Accelerate Long Context LLM Inference by Predictive Prefetch](https://arxiv.org/abs/2607.26475v1) | 2607.26475v1 | 9 |
| 2026-07-28 | [Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037v1) | 2607.26037v1 | 6 |
| 2026-07-28 | [CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention](https://arxiv.org/abs/2607.25291v2) | 2607.25291v2 | 11 |
| 2026-07-27 | [PIVOT: Efficient Query-Group Indexing for Token-Level Sparse Attention](https://arxiv.org/abs/2607.24593v1) | 2607.24593v1 | 8 |
| 2026-07-24 | [RIS-Kernel: A Model-Agnostic Architecture for Long-Context LLM Inference via Sparse Attention](https://arxiv.org/abs/2607.21927v2) | 2607.21927v2 | 9 |
| 2026-07-23 | [Parameter-free Adaptive Sparse Attention via Compression-Based Content Selection](https://arxiv.org/abs/2607.21752v1) | 2607.21752v1 | 6 |
| 2026-07-23 | [SANA-Video 2.0: Hybrid Linear Attention with Attention Residuals for Efficient Video Generation](https://arxiv.org/abs/2607.21553v1) | 2607.21553v1 | 10 |
| 2026-07-22 | [ELSAA: Efficient Low-Rank and Sparse Attention Approximation for Training Transformers](https://arxiv.org/abs/2607.20214v1) | 2607.20214v1 | 6 |
| 2026-07-21 | [Beyond Transformers: Linear Attention Policy for Open-Vocabulary Object Goal Navigation](https://arxiv.org/abs/2607.18794v1) | 2607.18794v1 | 8 |
| 2026-07-20 | [C$^2$KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](https://arxiv.org/abs/2607.17715v1) | 2607.17715v1 | 7 |
| 2026-07-19 | [Kernelized Linear Attention: Breaking the Capacity Wall with Symmetric Cones](https://arxiv.org/abs/2607.17419v1) | 2607.17419v1 | 6 |
| 2026-07-17 | [FVAttn: Adaptive Sparse Attention with Runtime Load Balancing for Video Generation](https://arxiv.org/abs/2607.16190v1) | 2607.16190v1 | 6 |
| 2026-07-16 | [VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs](https://arxiv.org/abs/2607.15498v1) | 2607.15498v1 | 6 |
| 2026-07-13 | [LiteTopK: Exploiting the Curse of Dimensionality for a Fused Indexer-TopK Kernel in Long-Context Sparse Attention](https://arxiv.org/abs/2607.11976v4) | 2607.11976v4 | 11 |
| 2026-07-10 | [COBS: Cumulant Order Block Sparse Attention](https://arxiv.org/abs/2607.09052v1) | 2607.09052v1 | 14 |
| 2026-07-08 | [Linear Attention Architectures: Mechanisms, Trade-offs, and Cross-Layer Routing](https://arxiv.org/abs/2607.07953v1) | 2607.07953v1 | 8 |
| 2026-07-08 | [Sparse Delta Memory: Scaling the State of Linear RNNs through Sparsity](https://arxiv.org/abs/2607.07386v1) | 2607.07386v1 | 6 |
| 2026-07-07 | [DepthWeave-KV: Token-Adaptive Cross-Layer Residual Factorization for Long-Context KV Cache Compression](https://arxiv.org/abs/2607.06523v1) | 2607.06523v1 | 6 |
| 2026-07-07 | [FreqDepthKV: Frequency-Guided Depth Sharing for Robust KV Cache Compression in Long-Context LLM Inference](https://arxiv.org/abs/2607.06519v1) | 2607.06519v1 | 6 |
| 2026-07-04 | [Uncertainty-gated selection for block-sparse attention](https://arxiv.org/abs/2607.07724v1) | 2607.07724v1 | 8 |
| 2026-07-04 | [Sequential Correlations Change In-Context Learning: Effective Context Length and Architectural Mismatch](https://arxiv.org/abs/2607.03660v1) | 2607.03660v1 | 7 |
| 2026-07-04 | [ELiTeFormer: An Efficient Transformer for FPGAs](https://arxiv.org/abs/2607.03652v1) | 2607.03652v1 | 8 |
| 2026-07-03 | [SAF3R: Dynamic Sparse Attention for Feed-Forward 3D Reconstruction Transformers](https://arxiv.org/abs/2607.03612v2) | 2607.03612v2 | 6 |
| 2026-07-03 | [HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion](https://arxiv.org/abs/2607.03012v2) | 2607.03012v2 | 6 |
| 2026-07-03 | [Hierarchical Sparse Attention Done Right: Toward Infinite Context Modeling](https://arxiv.org/abs/2607.02980v1) | 2607.02980v1 | 12 |
| 2026-07-02 | [ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning](https://arxiv.org/abs/2607.02509v1) | 2607.02509v1 | 7 |
| 2026-07-02 | [A Hippocampus for Linear Attention: An Exact Memory for What the Recurrent State Forgets](https://arxiv.org/abs/2607.02303v1) | 2607.02303v1 | 8 |
| 2026-07-01 | [Multi-Head Recurrent Memory Agents](https://arxiv.org/abs/2607.01523v1) | 2607.01523v1 | 6 |
| 2026-07-01 | [HYPIC: Position-Independent Caching for Hybrid-Attention LLM Serving](https://arxiv.org/abs/2607.01299v3) | 2607.01299v3 | 6 |
| 2026-07-01 | [MosaicKV: Serving Long-Context LLM with Dynamic Two-D KV Cache Compression](https://arxiv.org/abs/2607.00760v1) | 2607.00760v1 | 8 |
| 2026-07-01 | [Ghost in the Kernel: In-Context Learning with Efficient Transformers via Domain Generalization](https://arxiv.org/abs/2607.00479v1) | 2607.00479v1 | 6 |
| 2026-06-30 | [RaBitQCache: Rotated Binary Quantization for KVCache in Long Context LLM Inference](https://arxiv.org/abs/2606.31519v1) | 2606.31519v1 | 9 |
| 2026-06-30 | [SeKV: Resolution-Adaptive KV Cache with Hierarchical Semantic Memory for Long-Context LLM Inference](https://arxiv.org/abs/2606.31145v2) | 2606.31145v2 | 8 |
| 2026-06-29 | [Morphing into Hybrid Attention Models](https://arxiv.org/abs/2606.30562v1) | 2606.30562v1 | 6 |
| 2026-06-29 | [Predict, Reuse, and Repair: Accelerating Dynamic Sparse Attention for Long-Context LLM Decoding](https://arxiv.org/abs/2606.30389v1) | 2606.30389v1 | 9 |
| 2026-06-29 | [MATCH: Modulating Attention via In-Context Retrieval for Long-Context Transformers](https://arxiv.org/abs/2606.29844v1) | 2606.29844v1 | 7 |
| 2026-06-26 | [Turn-Averaged SAEs for Feature Discovery and Long-Context Attribution](https://arxiv.org/abs/2606.28548v1) | 2606.28548v1 | 7 |
| 2026-06-26 | [GLIDE: Guided Layerwise Hybrid Attention for Efficient LLM Inference](https://arxiv.org/abs/2607.24788v1) | 2607.24788v1 | 6 |
| 2026-06-25 | [Erase-then-Delta Attention: Decoupling Erase and Write Addresses in Delta-Rule Linear Attention](https://arxiv.org/abs/2606.26560v1) | 2606.26560v1 | 8 |
| 2026-06-23 | [Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control](https://arxiv.org/abs/2606.25136v1) | 2606.25136v1 | 6 |
| 2026-06-23 | [Emergent Capabilities Arise Randomly from Learning Sparse Attention Patterns](https://arxiv.org/abs/2606.25010v1) | 2606.25010v1 | 8 |
| 2026-06-23 | [VSANet: View-aware Sparse Attention Network for Light Field Image Denoising](https://arxiv.org/abs/2606.24737v1) | 2606.24737v1 | 6 |
| 2026-06-22 | [SpotAttention: Plug-In Block-Sparse Routing for Pretrained Long-Context Transformers](https://arxiv.org/abs/2606.22874v1) | 2606.22874v1 | 9 |
| 2026-06-21 | [moBERTo: A Modern Encoder for Portuguese via Continued Pretraining of ModernBERT](https://arxiv.org/abs/2606.22722v1) | 2606.22722v1 | 6 |
| 2026-06-19 | [HERALD: High-Throughput Block Diffusion LLM Inference via CPU-GPU Cooperative KV Cache Retrieval](https://arxiv.org/abs/2606.21633v3) | 2606.21633v3 | 9 |
| 2026-06-18 | [HydraHead: From Head-Level Functional Heterogeneity to Specialized Attention Hybridization](https://arxiv.org/abs/2606.20097v1) | 2606.20097v1 | 8 |
| 2026-06-18 | [StreamKL: Fast and Memory-Efficient KL Divergence for Boosting Attention Distillation](https://arxiv.org/abs/2606.20005v1) | 2606.20005v1 | 6 |
| 2026-06-18 | [SAC: Disaggregated KV Cache System for Sparse Attention LLMs with CXL](https://arxiv.org/abs/2606.19746v1) | 2606.19746v1 | 11 |
| 2026-06-15 | [Training and Evaluating Diffusion Policies with Long Context Lengths](https://arxiv.org/abs/2606.16447v2) | 2606.16447v2 | 8 |
| 2026-06-15 | [Taylor-Calibrate: Principled Initialization for Hybrid Linear Attention Distillation](https://arxiv.org/abs/2606.16429v1) | 2606.16429v1 | 8 |
| 2026-06-15 | [Training-free sparse attention based on cumulative energy filtering](https://arxiv.org/abs/2606.16317v1) | 2606.16317v1 | 10 |
| 2026-06-13 | [Ling and Ring 2.6 Technical Report: Efficient and Instant Agentic Intelligence at Trillion-Parameter Scale](https://arxiv.org/abs/2606.15079v1) | 2606.15079v1 | 6 |
| 2026-06-12 | [Semidirect Fourier Delta Attention: Phase-Controlled Delta Memory with Constructive Chunk-WY Kernels](https://arxiv.org/abs/2607.11897v1) | 2607.11897v1 | 8 |
| 2026-06-12 | [Knowledge Graph Enhanced Memory-Augmented Retrieval for Long Context Modeling](https://arxiv.org/abs/2606.14047v1) | 2606.14047v1 | 7 |
| 2026-06-11 | [MiniMax Sparse Attention](https://arxiv.org/abs/2606.13392v2) | 2606.13392v2 | 8 |
| 2026-06-10 | [Unified KV Pooling to Accelerate Long-Context LLM Serving](https://arxiv.org/abs/2606.14779v1) | 2606.14779v1 | 7 |
| 2026-06-09 | [Kwai Keye-VL-2.0 Technical Report](https://arxiv.org/abs/2606.10651v1) | 2606.10651v1 | 6 |
| 2026-06-09 | [Dynamic Linear Attention](https://arxiv.org/abs/2606.10650v1) | 2606.10650v1 | 8 |
| 2026-06-08 | [End-to-End Context Compression at Scale](https://arxiv.org/abs/2606.09659v2) | 2606.09659v2 | 8 |
| 2026-06-08 | [From Rigid to Dynamic: Entropy-Guided Adaptive Inference for Long-Context LLMs](https://arxiv.org/abs/2606.09508v1) | 2606.09508v1 | 9 |
| 2026-06-08 | [FlashMemory-DeepSeek-V4: Lightning Index Ultra-Long Context via Lookahead Sparse Attention](https://arxiv.org/abs/2606.09079v3) | 2606.09079v3 | 13 |
| 2026-06-07 | [Q-Delta: Beyond Key-Value Associative State Evolution](https://arxiv.org/abs/2606.08804v1) | 2606.08804v1 | 6 |
| 2026-06-07 | [Sparrow: Sparse Rollout for Stable and Efficient Long-context RL of Large Language Models](https://arxiv.org/abs/2606.08446v1) | 2606.08446v1 | 7 |
| 2026-06-06 | [Customer-Agent: Overcoming Context Limitations in Ultra-Long Shopping Trajectories via Tool-Augmented Agents and RLVR](https://arxiv.org/abs/2606.07995v1) | 2606.07995v1 | 6 |
| 2026-06-05 | [Still: Amortized KV Cache Compaction in a Single Forward Pass](https://arxiv.org/abs/2606.07878v1) | 2606.07878v1 | 7 |
| 2026-06-05 | [Gated Bidirectional Linear Attention for Generative Retrieval](https://arxiv.org/abs/2606.07317v2) | 2606.07317v2 | 6 |
| 2026-06-04 | [You Only Index Once: Cross-Layer Sparse Attention with Shared Routing](https://arxiv.org/abs/2606.06467v1) | 2606.06467v1 | 10 |
| 2026-06-04 | [Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents](https://arxiv.org/abs/2606.06453v1) | 2606.06453v1 | 6 |
| 2026-06-04 | [When Good Enough Is Optimal: Multiplication-Only Matrix Inversion Approximation for Quantized Gated DeltaNet](https://arxiv.org/abs/2606.06034v1) | 2606.06034v1 | 6 |
| 2026-06-03 | [SparDA: Sparse Decoupled Attention for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2606.04511v1) | 2606.04511v1 | 11 |
| 2026-06-02 | [Value-Aware Stochastic KV Cache Eviction for Reasoning Models](https://arxiv.org/abs/2606.03928v1) | 2606.03928v1 | 7 |
| 2026-06-02 | [An Asymptotic Theory of Chain-of-Thought in In-Context Learning](https://arxiv.org/abs/2606.03217v2) | 2606.03217v2 | 6 |
| 2026-06-01 | [MomentKV: Closing the Directional Gap in KV Cache Eviction for Long-Context Inference](https://arxiv.org/abs/2606.01563v1) | 2606.01563v1 | 6 |
| 2026-05-31 | [Blurry Window Attention](https://arxiv.org/abs/2606.09862v1) | 2606.09862v1 | 12 |
| 2026-05-31 | [Don't Read Everything: A Curvature-Conditioned Query for Linear Attention](https://arxiv.org/abs/2606.01294v2) | 2606.01294v2 | 8 |
| 2026-05-30 | [WaveFilter: Enhancing the Long-Context Capability of Diffusion LLMs via Wavelet-Guided KV Cache Filtering](https://arxiv.org/abs/2606.00724v1) | 2606.00724v1 | 8 |
| 2026-05-29 | [Memory by Design: Bayesian Layers for Sequence Modeling](https://arxiv.org/abs/2605.31163v5) | 2605.31163v5 | 6 |
| 2026-05-29 | [GRKV: Global Regression for Training-Free KV Cache Compression in Long-Context LLMs](https://arxiv.org/abs/2605.31105v3) | 2605.31105v3 | 8 |
| 2026-05-29 | [LVSA: Training-Free Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2605.31057v1) | 2605.31057v1 | 6 |
| 2026-05-29 | [LISA: Linear-Indexed Sparse Attention for Efficient Long-Context Reasoning](https://arxiv.org/abs/2607.19358v2) | 2607.19358v2 | 11 |
| 2026-05-29 | [BudgetDraft: Acceptance-Aware Multi-View Training for Sparse-KV Speculative Decoding](https://arxiv.org/abs/2606.00144v1) | 2606.00144v1 | 6 |
| 2026-05-28 | [Veda: Scalable Video Diffusion via Distilled Sparse Attention](https://arxiv.org/abs/2605.30325v1) | 2605.30325v1 | 6 |
| 2026-05-27 | [Parallax: Parameterized Local Linear Attention for Language Modeling](https://arxiv.org/abs/2605.29157v1) | 2605.29157v1 | 8 |
| 2026-05-27 | [Multi-Mixer Models: Flexible Sequence Modeling with Shared Representations](https://arxiv.org/abs/2605.28769v1) | 2605.28769v1 | 6 |
| 2026-05-27 | [Periodic RoPE for Infinite Context LLMs](https://arxiv.org/abs/2605.27980v1) | 2605.27980v1 | 8 |
| 2026-05-26 | [UNIQUE: Universal Top-k Sparse Attention for Training-free Inference and Sparsity-aware Training](https://arxiv.org/abs/2605.27740v1) | 2605.27740v1 | 10 |
| 2026-05-26 | [NestedKV: Nested Memory Routing for Long-Context KV Cache Compression](https://arxiv.org/abs/2605.26678v2) | 2605.26678v2 | 6 |
| 2026-05-25 | [A Method for Neutron-Gamma Pulse Shape Discrimination of CLYC Detector Based on a Gated Residual-Linear Attention Network](https://arxiv.org/abs/2606.02613v1) | 2606.02613v1 | 6 |
| 2026-05-25 | [IndexMem: Learned KV-Cache Eviction with Latent Memory for Long-Context LLM Inference](https://arxiv.org/abs/2605.25475v2) | 2605.25475v2 | 7 |
| 2026-05-23 | [Grammatically-Guided Sparse Attention for Efficient and Interpretable Transformers](https://arxiv.org/abs/2605.24518v1) | 2605.24518v1 | 6 |
| 2026-05-22 | [Efficient One-Step Diffusion Restoration Model with Compact Token Compression and Linear Attention](https://arxiv.org/abs/2605.23451v2) | 2605.23451v2 | 6 |
| 2026-05-22 | [DFSAttn: Dynamic Fine-grained Sparse Attention for Efficient Video Generation](https://arxiv.org/abs/2605.23445v1) | 2605.23445v1 | 6 |
| 2026-05-22 | [Positional Failures in Long-Context LLMs: A Blind Spot in Reasoning Benchmarks](https://arxiv.org/abs/2605.23170v1) | 2605.23170v1 | 7 |
| 2026-05-21 | [Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention](https://arxiv.org/abs/2605.22791v1) | 2605.22791v1 | 8 |
| 2026-05-21 | [Tensor Cache: Eviction-conditioned Associative Memory for Transformers](https://arxiv.org/abs/2605.22884v1) | 2605.22884v1 | 6 |
| 2026-05-20 | [EntmaxKV: Support-Aware Decoding for Entmax Attention](https://arxiv.org/abs/2605.21649v2) | 2605.21649v2 | 6 |
| 2026-05-20 | [Fast and Stable Triangular Inversion for Delta-Rule Linear Transformers](https://arxiv.org/abs/2605.21325v2) | 2605.21325v2 | 6 |
| 2026-05-20 | [Adaptive KV Cache Reuse for Fast Long-Context LLM Serving](https://arxiv.org/abs/2605.24022v2) | 2605.24022v2 | 6 |
| 2026-05-20 | [PulseCol: Periodically Refreshed Column-Sparse Attention for Accelerating Diffusion Language Models](https://arxiv.org/abs/2605.20813v1) | 2605.20813v1 | 10 |
| 2026-05-20 | [LT2: Linear-Time Looped Transformers](https://arxiv.org/abs/2605.20670v2) | 2605.20670v2 | 8 |
| 2026-05-19 | [SSV: Sparse Speculative Verification for Efficient LLM Inference](https://arxiv.org/abs/2605.19893v2) | 2605.19893v2 | 6 |
| 2026-05-19 | [Efficient Long-Context Modeling in Diffusion Language Models via Block Approximate Sparse Attention](https://arxiv.org/abs/2605.19726v1) | 2605.19726v1 | 9 |
| 2026-05-18 | [KVBuffer: IO-aware Serving for Linear Attention](https://arxiv.org/abs/2605.19049v2) | 2605.19049v2 | 10 |
| 2026-05-18 | [KVDrive: A Holistic Multi-Tier KV Cache Management System for Long-Context LLM Inference](https://arxiv.org/abs/2605.18071v1) | 2605.18071v1 | 8 |
| 2026-05-18 | [OSCAR: Offline Spectral Covariance-Aware Rotation for 2-bit KV Cache Quantization](https://arxiv.org/abs/2605.17757v1) | 2605.17757v1 | 7 |
| 2026-05-17 | [VeriCache: Turning Lossy KV Cache into Lossless LLM Inference](https://arxiv.org/abs/2605.17613v1) | 2605.17613v1 | 7 |
| 2026-05-16 | [Full Attention Strikes Back: Transferring Full Attention into Sparse within Hundred Training Steps](https://arxiv.org/abs/2605.16928v2) | 2605.16928v2 | 8 |
| 2026-05-16 | [CompactAttention: Accelerating Chunked Prefill with Block-Union KV Selection](https://arxiv.org/abs/2605.16839v2) | 2605.16839v2 | 10 |
| 2026-05-15 | [Attend Locally, Remember Linearly: Linear Attention as Cross-Frame Memory for Autoregressive Video Diffusion](https://arxiv.org/abs/2605.16579v2) | 2605.16579v2 | 10 |
| 2026-05-15 | [From Sparsity to Simplicity: Enabling Simpler Sequential Replacements via Sparse Attention Distillation](https://arxiv.org/abs/2605.18865v1) | 2605.18865v1 | 6 |
| 2026-05-15 | [RoPE Distinguishes Neither Positions Nor Tokens in Long Contexts, Provably](https://arxiv.org/abs/2605.15514v1) | 2605.15514v1 | 7 |
| 2026-05-15 | [STS: Efficient Sparse Attention with Speculative Token Sparsity](https://arxiv.org/abs/2605.15508v3) | 2605.15508v3 | 6 |
| 2026-05-14 | [DualKV: Shared-Prompt Flash Attention for Efficient RL Training with Large Rollouts and Long Contexts](https://arxiv.org/abs/2605.15422v5) | 2605.15422v5 | 11 |
| 2026-05-14 | [SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer](https://arxiv.org/abs/2605.15178v1) | 2605.15178v1 | 6 |
| 2026-05-14 | [HEART: Exploiting Head Heterogeneity in Sparse Attention for Video Diffusion](https://arxiv.org/abs/2605.14513v2) | 2605.14513v2 | 6 |
| 2026-05-13 | [SPHERICAL KV: Angle-Domain Attention and Rate-Distortion Retention for Efficient Long-Context Inference](https://arxiv.org/abs/2605.18856v3) | 2605.18856v3 | 7 |
| 2026-05-13 | [OSDN: Improving Delta Rule with Provable Online Preconditioning in Linear Attention](https://arxiv.org/abs/2605.13473v1) | 2605.13473v1 | 6 |
| 2026-05-13 | [Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory](https://arxiv.org/abs/2605.13370v1) | 2605.13370v1 | 6 |
| 2026-05-13 | [Exact Linear Attention](https://arxiv.org/abs/2605.18848v4) | 2605.18848v4 | 8 |
| 2026-05-12 | [Discovering KV Cache Eviction Policies via LLM-Guided Program Evolution](https://arxiv.org/abs/2608.14555v1) | 2608.14555v1 | 7 |
| 2026-05-12 | [BFLA: Block-Filtered Long-Context Attention Mechanism](https://arxiv.org/abs/2605.12193v2) | 2605.12193v2 | 7 |
| 2026-05-12 | [AB-Sparse: Sparse Attention with Adaptive Block Size for Accurate and Efficient Long-Context Inference](https://arxiv.org/abs/2605.12110v1) | 2605.12110v1 | 11 |
| 2026-05-12 | [Learning Subspace-Preserving Sparse Attention Graphs from Heterogeneous Multiview Data](https://arxiv.org/abs/2605.11881v2) | 2605.11881v2 | 10 |
| 2026-05-12 | [Training-Inference Consistent Segmented Execution for Long-Context LLMs](https://arxiv.org/abs/2605.11744v1) | 2605.11744v1 | 7 |
| 2026-05-12 | [FibQuant: Universal Vector Quantization for Random-Access KV-Cache Compression](https://arxiv.org/abs/2605.11478v1) | 2605.11478v1 | 6 |
| 2026-05-11 | [Variational Linear Attention: Stable Associative Memory for Long-Context Transformers](https://arxiv.org/abs/2605.11196v1) | 2605.11196v1 | 9 |
| 2026-05-11 | [FocuSFT: Bilevel Optimization for Dilution-Aware Long-Context Fine-Tuning](https://arxiv.org/abs/2605.09932v1) | 2605.09932v1 | 7 |
| 2026-05-10 | [Make Each Token Count: Towards Improving Long-Context Performance with KV Cache Eviction](https://arxiv.org/abs/2605.09649v1) | 2605.09649v1 | 8 |
| 2026-05-10 | [Attention Itself Could Retrieve.RetrieveVGGT: Training-Free Long Context Streaming 3D Reconstruction via Query-Key Similarity Retrieval](https://arxiv.org/abs/2605.09644v1) | 2605.09644v1 | 7 |
| 2026-05-09 | [ReST-KV: Robust KV Cache Eviction with Layer-wise Output Reconstruction and Spatial-Temporal Smoothing](https://arxiv.org/abs/2605.08840v1) | 2605.08840v1 | 7 |
| 2026-05-09 | [Kaczmarz Linear Attention](https://arxiv.org/abs/2605.08587v1) | 2605.08587v1 | 8 |
| 2026-05-08 | [An Efficient Hybrid Sparse Attention with CPU-GPU Parallelism for Long-Context Inference](https://arxiv.org/abs/2605.07719v1) | 2605.07719v1 | 11 |
| 2026-05-08 | [HexiSeq: Accommodating Long Context Training of LLMs over Heterogeneous Hardware](https://arxiv.org/abs/2605.07569v1) | 2605.07569v1 | 7 |
| 2026-05-08 | [MISA: Mixture of Indexer Sparse Attention for Long-Context LLM Inference](https://arxiv.org/abs/2605.07363v1) | 2605.07363v1 | 11 |
| 2026-05-08 | [Beyond Linear Attention: Softmax Transformers Implement In-Context Reinforcement Learning](https://arxiv.org/abs/2605.07333v2) | 2605.07333v2 | 6 |
| 2026-05-08 | [Reformulating KV Cache Eviction Problem for Long-Context LLM Inference](https://arxiv.org/abs/2605.07234v1) | 2605.07234v1 | 6 |
| 2026-05-08 | [Federated Nested Learning: Collaborative Training of Self-Referential Memories for Test-Time Adaptation](https://arxiv.org/abs/2605.16350v1) | 2605.16350v1 | 6 |
| 2026-05-07 | [Adaptive Memory Decay for Log-Linear Attention](https://arxiv.org/abs/2605.06946v1) | 2605.06946v1 | 6 |
| 2026-05-07 | [Sparse Attention as a Range Searching Problem: Towards an Inference-Efficient Index for KV Cache](https://arxiv.org/abs/2605.06763v2) | 2605.06763v2 | 9 |
| 2026-05-07 | [UniPrefill: Universal Long-Context Prefill Acceleration via Block-wise Dynamic Sparsification](https://arxiv.org/abs/2605.06221v2) | 2605.06221v2 | 9 |
| 2026-05-07 | [MDN: Parallelizing Stepwise Momentum for Delta Linear Attention](https://arxiv.org/abs/2605.05838v1) | 2605.05838v1 | 6 |
| 2026-05-06 | [LIVEditor-14B: Lightning Unified Video Editing via In-Context Sparse Attention](https://arxiv.org/abs/2605.04569v2) | 2605.04569v2 | 6 |
| 2026-05-05 | [AdapShot: Adaptive Many-Shot In-Context Learning with Semantic-Aware KV Cache Reuse](https://arxiv.org/abs/2605.03644v2) | 2605.03644v2 | 6 |
| 2026-05-04 | [StreamIndex: Memory-Bounded Compressed Sparse Attention via Streaming Top-k](https://arxiv.org/abs/2605.02568v1) | 2605.02568v1 | 6 |
| 2026-05-03 | [Stochastic Sparse Attention for Memory-Bound Inference](https://arxiv.org/abs/2605.01910v2) | 2605.01910v2 | 13 |
| 2026-04-29 | [Unifying Sparse Attention with Hierarchical Memory for Scalable Long-Context LLM Serving](https://arxiv.org/abs/2604.26837v1) | 2604.26837v1 | 11 |
| 2026-04-27 | [DepthKV: Layer-Dependent KV Cache Pruning for Long-Context LLM Inference](https://arxiv.org/abs/2604.24647v1) | 2604.24647v1 | 6 |
| 2026-04-27 | [Salca: A Sparsity-Aware Hardware Accelerator for Efficient Long-Context Attention Decoding](https://arxiv.org/abs/2604.24820v1) | 2604.24820v1 | 11 |
| 2026-04-27 | [SparseContrast: Dynamic Sparse Attention for Efficient and Accurate Contrastive Learning in Medical Imaging](https://arxiv.org/abs/2605.00887v2) | 2605.00887v2 | 6 |
| 2026-04-26 | [DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence](https://arxiv.org/abs/2606.19348v1) | 2606.19348v1 | 10 |
| 2026-04-24 | [SpikingBrain2.0: Brain-Inspired Foundation Models for Efficient Long-Context and Cross-Platform Inference](https://arxiv.org/abs/2604.22575v1) | 2604.22575v1 | 13 |
| 2026-04-24 | [Guess-Verify-Refine: Data-Aware Top-K for Sparse-Attention Decoding on Blackwell via Temporal Correlation](https://arxiv.org/abs/2604.22312v1) | 2604.22312v1 | 6 |
| 2026-04-23 | [Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1) | 2604.21221v1 | 8 |
| 2026-04-22 | [Preconditioned DeltaNet: Curvature-aware Sequence Modeling for Linear Recurrences](https://arxiv.org/abs/2604.21100v1) | 2604.21100v1 | 6 |
| 2026-04-22 | [DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470v1) | 2604.20470v1 | 6 |
| 2026-04-22 | [LaplacianFormer:Rethinking Linear Attention with Laplacian Kernel](https://arxiv.org/abs/2604.20368v1) | 2604.20368v1 | 6 |
| 2026-04-22 | [Simplified Sparse Attention via Gist Tokens](https://arxiv.org/abs/2604.20920v2) | 2604.20920v2 | 10 |
| 2026-04-21 | [DASH-KV: Accelerating Long-Context LLM Inference via Asymmetric KV Cache Hashing](https://arxiv.org/abs/2604.19351v4) | 2604.19351v4 | 6 |
| 2026-04-21 | [FG$^2$-GDN: Enhancing Long-Context Gated Delta Networks with Doubly Fine-Grained Control](https://arxiv.org/abs/2604.19021v3) | 2604.19021v3 | 7 |
| 2026-04-20 | [AdaCluster: Adaptive Query-Key Clustering for Sparse Attention in Video Generation](https://arxiv.org/abs/2604.18348v1) | 2604.18348v1 | 6 |
| 2026-04-20 | [AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization](https://arxiv.org/abs/2604.18137v1) | 2604.18137v1 | 8 |
| 2026-04-16 | [AdaSplash-2: Faster Differentiable Sparse Attention](https://arxiv.org/abs/2604.15180v1) | 2604.15180v1 | 10 |
| 2026-04-15 | [SparseBalance: Load-Balanced Long Context Training with Dynamic Sparse Attention](https://arxiv.org/abs/2604.13847v2) | 2604.13847v2 | 11 |
| 2026-04-15 | [ART: Attention Run-time Termination for Efficient Large Language Model Decoding](https://arxiv.org/abs/2606.00024v3) | 2606.00024v3 | 6 |
| 2026-04-14 | [VFA: Relieving Vector Operations in Flash Attention with Global Maximum Pre-computation](https://arxiv.org/abs/2604.12798v1) | 2604.12798v1 | 10 |
| 2026-04-14 | [Ride the Wave: Precision-Allocated Sparse Attention for Smooth Video Generation](https://arxiv.org/abs/2604.12219v1) | 2604.12219v1 | 6 |
| 2026-04-13 | [LoSA: Locality Aware Sparse Attention for Block-Wise Diffusion Language Models](https://arxiv.org/abs/2604.12056v1) | 2604.12056v1 | 8 |
| 2026-04-11 | [Long-Horizon Streaming Video Generation via Hybrid Attention with Decoupled Distillation](https://arxiv.org/abs/2604.10103v2) | 2604.10103v2 | 8 |
| 2026-04-11 | [On The Application of Linear Attention in Multimodal Transformers](https://arxiv.org/abs/2604.10064v1) | 2604.10064v1 | 6 |
| 2026-04-09 | [Dual-Pool Token-Budget Routing for Cost-Efficient and Reliable LLM Serving](https://arxiv.org/abs/2604.08075v1) | 2604.08075v1 | 6 |
| 2026-04-09 | [AsyncTLS: Efficient Generative LLM Inference with Asynchronous Two-level Sparse Attention](https://arxiv.org/abs/2604.07815v1) | 2604.07815v1 | 10 |
| 2026-04-08 | [Optimal Decay Spectra for Linear Recurrences](https://arxiv.org/abs/2604.07658v1) | 2604.07658v1 | 8 |
| 2026-04-08 | [Flux Attention: Context-Aware Hybrid Attention for Efficient LLMs Inference](https://arxiv.org/abs/2604.07394v2) | 2604.07394v2 | 6 |
| 2026-04-06 | [LSRM: High-Fidelity Object-Centric Reconstruction via Scaled Context Windows](https://arxiv.org/abs/2604.05182v3) | 2604.05182v3 | 8 |
| 2026-04-01 | [AgentWatcher: A Rule-based Prompt Injection Monitor](https://arxiv.org/abs/2604.01194v2) | 2604.01194v2 | 6 |
| 2026-03-31 | [MAC-Attention: a Match-Amend-Complete Scheme for Fast and Accurate Attention Computation](https://arxiv.org/abs/2604.00235v1) | 2604.00235v1 | 6 |
| 2026-03-31 | [VecAttention: Vector-wise Sparse Attention for Accelerating Long Context Inference](https://arxiv.org/abs/2603.29494v1) | 2603.29494v1 | 11 |
| 2026-03-30 | [Understand and Accelerate Memory Processing Pipeline for Large Language Model Inference](https://arxiv.org/abs/2603.29002v3) | 2603.29002v3 | 6 |
| 2026-03-30 | [HISA: Efficient Hierarchical Indexing for Fine-Grained Sparse Attention](https://arxiv.org/abs/2603.28458v5) | 2603.28458v5 | 8 |
| 2026-03-30 | [CSAttention: Centroid-Scoring Attention for Accelerating LLM Inference](https://arxiv.org/abs/2604.08584v1) | 2604.08584v1 | 8 |
| 2026-03-28 | [ScoutAttention: Efficient KV Cache Offloading via Layer-Ahead CPU Pre-computation for LLM Inference](https://arxiv.org/abs/2603.27138v1) | 2603.27138v1 | 9 |
| 2026-03-27 | [Switch Attention: Towards Dynamic and Fine-grained Hybrid Transformers](https://arxiv.org/abs/2603.26380v3) | 2603.26380v3 | 8 |
| 2026-03-23 | [PRISM: Breaking the O(n) Memory Wall in Long-Context LLM Inference via O(1) Photonic Block Selection](https://arxiv.org/abs/2603.21576v2) | 2603.21576v2 | 9 |
| 2026-03-21 | [Beyond Token Eviction: Mixed-Dimension Budget Allocation for Efficient KV Cache Compression](https://arxiv.org/abs/2603.20616v1) | 2603.20616v1 | 7 |
| 2026-03-20 | [Coding Agents are Effective Long-Context Processors](https://arxiv.org/abs/2603.20432v1) | 2603.20432v1 | 7 |
| 2026-03-20 | [KV Cache Optimization Strategies for Scalable and Efficient LLM Inference](https://arxiv.org/abs/2603.20397v1) | 2603.20397v1 | 7 |
| 2026-03-19 | [Accurate and Efficient Multi-Channel Time Series Forecasting via Sparse Attention Mechanism](https://arxiv.org/abs/2603.18712v3) | 2603.18712v3 | 6 |
| 2026-03-19 | [Attention Sparsity is Input-Stable: Training-Free Sparse Attention for Video Generation via Offline Sparsity Profiling and Online QK Co-Clustering](https://arxiv.org/abs/2603.18636v2) | 2603.18636v2 | 6 |
| 2026-03-19 | [Self-Tuning Sparse Attention: Multi-Fidelity Hyperparameter Optimization for Transformer Acceleration](https://arxiv.org/abs/2603.18417v1) | 2603.18417v1 | 8 |
| 2026-03-18 | [Learning When to Attend: Conditional Memory Access for Long-Context LLMs](https://arxiv.org/abs/2603.17484v2) | 2603.17484v2 | 7 |
| 2026-03-17 | [ViT-AdaLA: Adapting Vision Transformers with Linear Attention](https://arxiv.org/abs/2603.16063v2) | 2603.16063v2 | 6 |
| 2026-03-15 | [M$^2$RNN: Non-Linear RNNs with Matrix-Valued States for Scalable Language Modeling](https://arxiv.org/abs/2603.14360v3) | 2603.14360v3 | 6 |
| 2026-03-15 | [Self-Indexing KVCache: Predicting Sparse Attention from Compressed Keys](https://arxiv.org/abs/2603.14224v1) | 2603.14224v1 | 10 |
| 2026-03-13 | [98$\times$ Faster LLM Routing Without a Dedicated GPU: Flash Attention, Prompt Compression, and Near-Streaming for the vLLM Semantic Router](https://arxiv.org/abs/2603.12646v1) | 2603.12646v1 | 8 |
| 2026-03-13 | [Dynamic Sparse Attention: Access Patterns and Architecture](https://arxiv.org/abs/2603.13430v1) | 2603.13430v1 | 6 |
| 2026-03-12 | [IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse](https://arxiv.org/abs/2603.12201v1) | 2603.12201v1 | 8 |
| 2026-03-09 | [The $qs$ Inequality: Quantifying the Double Penalty of Mixture-of-Experts at Inference](https://arxiv.org/abs/2603.08960v1) | 2603.08960v1 | 8 |
| 2026-03-09 | [LycheeCluster: Efficient Long-Context Inference with Structure-Aware Chunking and Hierarchical KV Indexing](https://arxiv.org/abs/2603.08453v1) | 2603.08453v1 | 7 |
| 2026-03-07 | [Recursive Language Models Meet Uncertainty: The Surprising Effectiveness of Self-Reflective Program Search for Long Context](https://arxiv.org/abs/2603.15653v1) | 2603.15653v1 | 7 |
| 2026-03-06 | [Stem: Rethinking Causal Information Flow in Sparse Attention](https://arxiv.org/abs/2603.06274v2) | 2603.06274v2 | 8 |
| 2026-03-06 | [Low-Latency Event-Based Object Detection with Spatially-Sparse Linear Attention](https://arxiv.org/abs/2603.06228v4) | 2603.06228v4 | 6 |
| 2026-03-06 | [FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling](https://arxiv.org/abs/2603.06199v1) | 2603.06199v1 | 9 |
| 2026-03-06 | [A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA](https://arxiv.org/abs/2603.05931v1) | 2603.05931v1 | 8 |
| 2026-03-06 | [MSA: Memory Sparse Attention for Efficient End-to-End Memory Model Scaling to 100M Tokens](https://arxiv.org/abs/2603.23516v2) | 2603.23516v2 | 16 |
| 2026-03-05 | [Accelerating Text-to-Video Generation with Calibrated Sparse Attention](https://arxiv.org/abs/2603.05503v1) | 2603.05503v1 | 6 |
| 2026-03-03 | [LoGeR: Long-Context Geometric Reconstruction with Hybrid Memory](https://arxiv.org/abs/2603.03269v2) | 2603.03269v2 | 7 |
| 2026-03-03 | [VSPrefill: Vertical-Slash Sparse Attention with Lightweight Indexing for Long-Context Prefilling](https://arxiv.org/abs/2603.04460v1) | 2603.04460v1 | 11 |
| 2026-03-03 | [Gated Differential Linear Attention: A Linear-Time Decoder for High-Fidelity Medical Segmentation](https://arxiv.org/abs/2603.02727v4) | 2603.02727v4 | 6 |
| 2026-03-03 | [SOLAR: SVD-Optimized Lifelong Attention for Recommendation](https://arxiv.org/abs/2603.02561v2) | 2603.02561v2 | 6 |
| 2026-02-27 | [FuXi-Linear: Unleashing the Power of Linear Attention in Long-term Time-aware Sequential Recommendation](https://arxiv.org/abs/2602.23671v1) | 2602.23671v1 | 6 |
| 2026-02-26 | [Fine-Tuning Without Forgetting In-Context Learning: A Theoretical Analysis of Linear Attention Models](https://arxiv.org/abs/2602.23197v2) | 2602.23197v2 | 6 |
| 2026-02-26 | [S2O: Early Stopping for Sparse Attention via Online Permutation](https://arxiv.org/abs/2602.22575v2) | 2602.22575v2 | 8 |
| 2026-02-25 | [DySCO: Dynamic Attention-Scaling Decoding for Long-Context Language Models](https://arxiv.org/abs/2602.22175v2) | 2602.22175v2 | 7 |
| 2026-02-24 | [Test-Time Training with KV Binding Is Secretly Linear Attention](https://arxiv.org/abs/2602.21204v4) | 2602.21204v4 | 6 |
| 2026-02-24 | [Scaling State-Space Models on Multiple GPUs with Tensor Parallelism](https://arxiv.org/abs/2602.21144v1) | 2602.21144v1 | 6 |
| 2026-02-24 | [FAST-Prefill: FPGA Accelerated Sparse Attention for Long Context LLM Prefill](https://arxiv.org/abs/2602.20515v1) | 2602.20515v1 | 15 |
| 2026-02-22 | [Incremental Learning of Sparse Attention Patterns in Transformers](https://arxiv.org/abs/2602.19143v2) | 2602.19143v2 | 6 |
| 2026-02-19 | [ARKV: Adaptive and Resource-Efficient KV Cache Management under Limited Memory Budget for Long-Context Inference in LLMs](https://arxiv.org/abs/2603.08727v1) | 2603.08727v1 | 8 |
| 2026-02-19 | [2Mamba2Furious: Linear in Complexity, Competitive in Accuracy](https://arxiv.org/abs/2602.17363v3) | 2602.17363v3 | 9 |
| 2026-02-17 | [The Limits of Long-Context Reasoning in Automated Bug Fixing](https://arxiv.org/abs/2602.16069v2) | 2602.16069v2 | 7 |
| 2026-02-16 | [How to Train Your Long-Context Visual Document Model](https://arxiv.org/abs/2602.15257v3) | 2602.15257v3 | 7 |
| 2026-02-16 | [Long Context, Less Focus: A Scaling Gap in LLMs Revealed through Privacy and Personalization](https://arxiv.org/abs/2602.15028v1) | 2602.15028v1 | 7 |
| 2026-02-15 | [MAGE: All-[MASK] Block Already Knows Where to Look in Block Diffusion LLM](https://arxiv.org/abs/2602.14209v2) | 2602.14209v2 | 6 |
| 2026-02-15 | [TS-Haystack: A Multi-Task Retrieval Benchmark for Long-Context Time-Series Reasoning](https://arxiv.org/abs/2602.14200v6) | 2602.14200v6 | 7 |
| 2026-02-14 | [Attention in Constant Time: Vashista Sparse Attention for Long-Context Decoding with Exponential Guarantees](https://arxiv.org/abs/2602.13804v1) | 2602.13804v1 | 11 |
| 2026-02-14 | [AllMem: A Memory-centric Recipe for Efficient Long-context Modeling](https://arxiv.org/abs/2602.13680v1) | 2602.13680v1 | 9 |
| 2026-02-13 | [SpargeAttention2: Trainable Sparse Attention via Hybrid Top-k+Top-p Masking and Distillation Fine-Tuning](https://arxiv.org/abs/2602.13515v2) | 2602.13515v2 | 6 |
| 2026-02-13 | [SLA2: Sparse-Linear Attention with Learnable Routing and Quantization-aware Training](https://arxiv.org/abs/2602.12675v2) | 2602.12675v2 | 6 |
| 2026-02-12 | [MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271v1) | 2602.12271v1 | 6 |
| 2026-02-12 | [HLA: Hadamard Linear Attention](https://arxiv.org/abs/2602.12128v1) | 2602.12128v1 | 6 |
| 2026-02-12 | [MiniCPM-SALA: Hybridizing Sparse and Linear Attention for Efficient Long-Context Modeling](https://arxiv.org/abs/2602.11761v2) | 2602.11761v2 | 17 |
| 2026-02-11 | [Rotary Positional Embeddings as Phase Modulation: Theoretical Bounds on the RoPE Base for Long-Context Transformers](https://arxiv.org/abs/2602.10959v1) | 2602.10959v1 | 7 |
| 2026-02-11 | [Routing Absorption in Sparse Attention: Why Random Gates Are Hard to Beat](https://arxiv.org/abs/2603.02227v2) | 2603.02227v2 | 6 |
| 2026-02-11 | [Kalman Linear Attention: Parallel Bayesian Filtering For Efficient Language Modelling and State Tracking](https://arxiv.org/abs/2602.10743v2) | 2602.10743v2 | 6 |
| 2026-02-11 | [When to Memorize and When to Stop: Gated Recurrent Memory for Long-Context Reasoning](https://arxiv.org/abs/2602.10560v1) | 2602.10560v1 | 7 |
| 2026-02-09 | [Prism: Spectral-Aware Block-Sparse Attention](https://arxiv.org/abs/2602.08426v2) | 2602.08426v2 | 8 |
| 2026-02-09 | [Dynamic Long Context Reasoning over Compressed Memory via End-to-End Reinforcement Learning](https://arxiv.org/abs/2602.08382v1) | 2602.08382v1 | 7 |
| 2026-02-08 | [ResidualKV: Residual-Based KV Cache Compression for Efficient Long-Context Inference](https://arxiv.org/abs/2602.08005v2) | 2602.08005v2 | 14 |
| 2026-02-07 | [ParisKV: Fast and Drift-Robust KV-Cache Retrieval for Long-Context LLMs](https://arxiv.org/abs/2602.07721v3) | 2602.07721v3 | 7 |
| 2026-02-07 | [AngelSlim: A more accessible, comprehensive, and efficient toolkit for large model compression](https://arxiv.org/abs/2602.21233v3) | 2602.21233v3 | 6 |
| 2026-02-07 | [Scout Before You Attend: Sketch-and-Walk Sparse Attention for Efficient LLM Inference](https://arxiv.org/abs/2602.07397v1) | 2602.07397v1 | 10 |
| 2026-02-06 | [Vegas: Self-Speculative Decoding with Verification-Guided Sparse Attention](https://arxiv.org/abs/2602.07223v2) | 2602.07223v2 | 10 |
| 2026-02-06 | [CALM: Class-Conditional Sparse Attention Vectors for Large Audio-Language Models](https://arxiv.org/abs/2602.07077v2) | 2602.07077v2 | 6 |
| 2026-02-06 | [SOCKET: SOft Collision Kernel EsTimator for Sparse Attention](https://arxiv.org/abs/2602.06283v3) | 2602.06283v3 | 8 |
| 2026-02-05 | [Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://arxiv.org/abs/2602.06028v1) | 2602.06028v1 | 7 |
| 2026-02-05 | [RRAttention: Dynamic Block Sparse Attention via Per-Head Round-Robin Shifts for Long-Context Inference](https://arxiv.org/abs/2602.05853v1) | 2602.05853v1 | 13 |
| 2026-02-05 | [FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion](https://arxiv.org/abs/2602.05305v3) | 2602.05305v3 | 9 |
| 2026-02-05 | [ReGLA: Efficient Receptive-Field Modeling with Gated Linear Attention Network](https://arxiv.org/abs/2602.05262v1) | 2602.05262v1 | 6 |
| 2026-02-05 | [ZeroS: Zero-Sum Linear Attention for Efficient Transformers](https://arxiv.org/abs/2602.05230v1) | 2602.05230v1 | 8 |
| 2026-02-05 | [Double-P: Hierarchical Top-P Sparse Attention for Long-Context LLMs](https://arxiv.org/abs/2602.05191v1) | 2602.05191v1 | 9 |
| 2026-02-04 | [On State Reduction in Linear Attention](https://arxiv.org/abs/2602.04852v3) | 2602.04852v3 | 6 |
| 2026-02-04 | [Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention](https://arxiv.org/abs/2602.04789v4) | 2602.04789v4 | 6 |
| 2026-02-04 | [Addressing Corpus Knowledge Poisoning Attacks on RAG Using Sparse Attention](https://arxiv.org/abs/2602.04711v3) | 2602.04711v3 | 6 |
| 2026-02-04 | [MirrorLA: Reflecting Feature Map for Vision Linear Attention](https://arxiv.org/abs/2602.04346v1) | 2602.04346v1 | 8 |
| 2026-02-03 | [Online Vector Quantized Attention](https://arxiv.org/abs/2602.03922v3) | 2602.03922v3 | 8 |
| 2026-02-03 | [Neural Attention Search Linear: Towards Adaptive Token-Level Hybrid Attention Models](https://arxiv.org/abs/2602.03681v2) | 2602.03681v2 | 6 |
| 2026-02-03 | [HySparse: A Hybrid Sparse Attention Architecture with Oracle Token Selection and KV Cache Sharing](https://arxiv.org/abs/2602.03560v1) | 2602.03560v1 | 9 |
| 2026-02-03 | [Token Sparse Attention: Efficient Long-Context Inference with Interleaved Token Selection](https://arxiv.org/abs/2602.03216v3) | 2602.03216v3 | 13 |
| 2026-02-03 | [FASA: Frequency-aware Sparse Attention](https://arxiv.org/abs/2602.03152v3) | 2602.03152v3 | 8 |
| 2026-02-02 | [State Rank Dynamics in Linear Attention LLMs](https://arxiv.org/abs/2602.02195v1) | 2602.02195v1 | 6 |
| 2026-02-02 | [STILL: Selecting Tokens for Intra-Layer Hybrid Attention to Linearize LLMs](https://arxiv.org/abs/2602.02180v2) | 2602.02180v2 | 6 |
| 2026-02-02 | [Focus-dLLM: Accelerating Long-Context Diffusion LLM Inference via Confidence-Guided Context Focusing](https://arxiv.org/abs/2602.02159v1) | 2602.02159v1 | 9 |
| 2026-02-02 | [Out of the Memory Barrier: A Highly Memory Efficient Training System for LLMs with Million-Token Contexts](https://arxiv.org/abs/2602.02108v4) | 2602.02108v4 | 11 |
| 2026-02-02 | [Q Cache: Visual Attention is Valuable in Less than Half of Decode Layers for Multimodal Large Language Model](https://arxiv.org/abs/2602.01901v1) | 2602.01901v1 | 6 |
| 2026-02-02 | [Softmax Linear Attention: Reclaiming Global Competition](https://arxiv.org/abs/2602.01744v1) | 2602.01744v1 | 8 |
| 2026-02-01 | [PISA: Piecewise Sparse Attention Is Wiser for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.01077v4) | 2602.01077v4 | 6 |
| 2026-01-31 | [HyLRA: Hybrid Layer Reuse Attention for Efficient Long-Context Inference](https://arxiv.org/abs/2602.00777v1) | 2602.00777v1 | 7 |
| 2026-01-30 | [Sparse Attention as Compact Kernel Regression](https://arxiv.org/abs/2601.22766v4) | 2601.22766v4 | 6 |
| 2026-01-29 | [SPLA: Block Sparse Plus Linear Attention for Long Context Modeling](https://arxiv.org/abs/2601.22379v1) | 2601.22379v1 | 15 |
| 2026-01-29 | [Hybrid Linear Attention Done Right: Efficient Distillation and Effective Architectures for Extremely Long Contexts](https://arxiv.org/abs/2601.22156v1) | 2601.22156v1 | 11 |
| 2026-01-26 | [Superlinear Multi-Step Attention](https://arxiv.org/abs/2601.18401v1) | 2601.18401v1 | 8 |
| 2026-01-25 | [S$^3$-Attention:Attention-Aligned Endogenous Retrieval for Memory-Bounded Long-Context Inference](https://arxiv.org/abs/2601.17702v2) | 2601.17702v2 | 7 |
| 2026-01-23 | [SALAD: Achieve High-Sparsity Attention via Efficient Linear Attention Tuning for Video Diffusion Transformer](https://arxiv.org/abs/2601.16515v2) | 2601.16515v2 | 10 |
| 2026-01-20 | [Interpretable and Sparse Linear Attention with Decoupled Membership-Subspace Modeling via MCR2 Objective](https://arxiv.org/abs/2601.17042v1) | 2601.17042v1 | 6 |
| 2026-01-20 | [HeteroCache: A Dynamic Retrieval Approach to Heterogeneous KV Cache Compression for Long-Context LLM Inference](https://arxiv.org/abs/2601.13684v2) | 2601.13684v2 | 6 |
| 2026-01-20 | [Dynamic Differential Linear Attention: Enhancing Linear Diffusion Transformer for High-Quality Image Generation](https://arxiv.org/abs/2601.13683v1) | 2601.13683v1 | 6 |
| 2026-01-17 | [MemoryRewardBench: Benchmarking Reward Models for Long-Term Memory Management in Large Language Models](https://arxiv.org/abs/2601.11969v2) | 2601.11969v2 | 6 |
| 2026-01-17 | [LSTM-MAS: A Long Short-Term Memory Inspired Multi-Agent System for Long-Context Understanding](https://arxiv.org/abs/2601.11913v2) | 2601.11913v2 | 7 |
| 2026-01-16 | [Building Production-Ready Probes For Gemini](https://arxiv.org/abs/2601.11516v4) | 2601.11516v4 | 6 |
| 2026-01-14 | [Mixture of Distributions Matters: Dynamic Sparse Attention for Efficient Video Diffusion Transformers](https://arxiv.org/abs/2601.11641v3) | 2601.11641v3 | 6 |
| 2026-01-13 | [TableCache: Primary Foreign Key Guided KV Cache Precomputation for Low Latency Text-to-SQL](https://arxiv.org/abs/2601.08743v1) | 2601.08743v1 | 7 |
| 2026-01-12 | [Gated Sparse Attention: Combining Computational Efficiency with Training Stability for Long-Context Language Models](https://arxiv.org/abs/2601.15305v1) | 2601.15305v1 | 9 |
| 2026-01-12 | [MHLA: Restoring Expressivity of Linear Attention via Token-Level Multi-Head](https://arxiv.org/abs/2601.07832v2) | 2601.07832v2 | 6 |
| 2026-01-12 | [KVzap: Fast, Adaptive, and Faithful KV Cache Pruning](https://arxiv.org/abs/2601.07891v2) | 2601.07891v2 | 7 |
| 2026-01-06 | [Punctuation-aware Hybrid Trainable Sparse Attention for Large Language Models](https://arxiv.org/abs/2601.02819v1) | 2601.02819v1 | 8 |
| 2026-01-05 | [OrbitFlow: SLO-Aware Long-Context LLM Serving with Fine-Grained KV Cache Reconfiguration](https://arxiv.org/abs/2601.10729v2) | 2601.10729v2 | 6 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-30 | [RainFusion2.0: Temporal-Spatial Awareness and Hardware-Efficient Block-wise Sparse Attention](https://arxiv.org/abs/2512.24086v2) | 2512.24086v2 | 6 |
| 2025-12-30 | [Efficient Context Scaling with LongCat ZigZag Attention](https://arxiv.org/abs/2512.23966v2) | 2512.23966v2 | 6 |
| 2025-12-29 | [End-to-End Test-Time Training for Long Context](https://arxiv.org/abs/2512.23675v2) | 2512.23675v2 | 7 |
| 2025-12-27 | [SagaScale: A Realistic, Scalable, and High-Quality Long-Context Benchmark Built from Full-Length Novels](https://arxiv.org/abs/2601.09723v1) | 2601.09723v1 | 7 |
| 2025-12-27 | [Bright 4B: Scaling Hyperspherical Learning for Segmentation in 3D Brightfield Microscopy](https://arxiv.org/abs/2512.22423v1) | 2512.22423v1 | 8 |
| 2025-12-23 | [SA-DiffuSeq: Addressing Computational and Scalability Challenges in Long-Document Generation with Sparse Attention](https://arxiv.org/abs/2512.20724v1) | 2512.20724v1 | 8 |
| 2025-12-23 | [MoE-DiffuSeq: Enhancing Long-Document Diffusion Models with Sparse Attention and Mixture of Experts](https://arxiv.org/abs/2512.20604v2) | 2512.20604v2 | 8 |
| 2025-12-19 | [Linear Attention for Joint Power Optimization and User-Centric Clustering in Cell-Free Networks](https://arxiv.org/abs/2512.17466v3) | 2512.17466v3 | 6 |
| 2025-12-18 | [Trainable Log-linear Sparse Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2512.16615v2) | 2512.16615v2 | 6 |
| 2025-12-18 | [Kascade: A Practical Sparse Attention Method for Long-Context LLM Inference](https://arxiv.org/abs/2512.16391v2) | 2512.16391v2 | 9 |
| 2025-12-17 | [CTkvr: KV Cache Retrieval for Long-Context LLMs via Centroid then Token Indexing](https://arxiv.org/abs/2512.15550v1) | 2512.15550v1 | 10 |
| 2025-12-17 | [LADY: Linear Attention for Autonomous Driving Efficiency without Transformers](https://arxiv.org/abs/2512.15038v3) | 2512.15038v3 | 6 |
| 2025-12-16 | [MemFlow: Flowing Adaptive Memory for Consistent and Efficient Long Video Narratives](https://arxiv.org/abs/2512.14699v1) | 2512.14699v1 | 6 |
| 2025-12-16 | [PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion](https://arxiv.org/abs/2512.14322v2) | 2512.14322v2 | 6 |
| 2025-12-16 | [A Unified Sparse Attention via Multi-Granularity Compression](https://arxiv.org/abs/2512.14082v1) | 2512.14082v1 | 8 |
| 2025-12-15 | [Let's (not) just put things in Context: Test-Time Training for Long-Context LLMs](https://arxiv.org/abs/2512.13898v1) | 2512.13898v1 | 7 |
| 2025-12-15 | [BlossomRec: Block-level Fused Sparse Attention Mechanism for Sequential Recommendations](https://arxiv.org/abs/2512.13368v3) | 2512.13368v3 | 6 |
| 2025-12-14 | [Exact Flow Linear Attention: Exact Solution from Continuous-Time Dynamics](https://arxiv.org/abs/2512.12602v5) | 2512.12602v5 | 6 |
| 2025-12-12 | [BLASST: Dynamic BLocked Attention Sparsity via Softmax Thresholding](https://arxiv.org/abs/2512.12087v3) | 2512.12087v3 | 8 |
| 2025-12-12 | [Hold Onto That Thought: Assessing KV Cache Compression On Reasoning](https://arxiv.org/abs/2512.12008v1) | 2512.12008v1 | 7 |
| 2025-12-12 | [Softmax as Linear Attention in the Large-Prompt Regime: a Measure-based Perspective](https://arxiv.org/abs/2512.11784v2) | 2512.11784v2 | 6 |
| 2025-12-11 | [ESS: An Offload-Centric Latent-Cache Management Architecture for DeepSeek-V3.2-Exp](https://arxiv.org/abs/2512.10576v1) | 2512.10576v1 | 8 |
| 2025-12-11 | [SWAA: Sliding Window Attention Adaptation for Efficient and Quality Preserving Long Context Processing](https://arxiv.org/abs/2512.10411v5) | 2512.10411v5 | 13 |
| 2025-12-10 | [Training-free Context-adaptive Attention for Efficient Long Context Modeling](https://arxiv.org/abs/2512.09238v2) | 2512.09238v2 | 13 |
| 2025-12-09 | [InfiniteVL: Synergizing Linear and Sparse Attention for Highly-Efficient, Unlimited-Input Vision-Language Models](https://arxiv.org/abs/2512.08829v2) | 2512.08829v2 | 8 |
| 2025-12-08 | [FRWKV:Frequency-Domain Linear Attention for Long-Term Time Series Forecasting](https://arxiv.org/abs/2512.07539v2) | 2512.07539v2 | 6 |
| 2025-12-07 | [Block Sparse Flash Attention](https://arxiv.org/abs/2512.07011v2) | 2512.07011v2 | 14 |
| 2025-12-04 | [EgoLCD: Egocentric Video Generation with Long Context Diffusion](https://arxiv.org/abs/2512.04515v1) | 2512.04515v1 | 7 |
| 2025-12-03 | [Evaluating Long-Context Reasoning in LLM-Based WebAgents](https://arxiv.org/abs/2512.04307v1) | 2512.04307v1 | 7 |
| 2025-12-03 | [PSA: Pyramid Sparse Attention for Efficient Video Understanding and Generation](https://arxiv.org/abs/2512.04025v1) | 2512.04025v1 | 6 |
| 2025-12-03 | [KVNAND: Efficient On-Device Large Language Model Inference Using DRAM-Free In-Flash Computing](https://arxiv.org/abs/2512.03608v1) | 2512.03608v1 | 6 |
| 2025-12-03 | [A Preliminary Study on the Promises and Challenges of Native Top-$k$ Sparse Attention](https://arxiv.org/abs/2512.03494v1) | 2512.03494v1 | 8 |
| 2025-12-02 | [Invasive Context Engineering to Control Large Language Models](https://arxiv.org/abs/2512.03001v1) | 2512.03001v1 | 6 |
| 2025-12-02 | [DeepSeek-V3.2: Pushing the Frontier of Open Large Language Models](https://arxiv.org/abs/2512.02556v1) | 2512.02556v1 | 6 |
| 2025-12-01 | [KV Pareto: Systems-Level Optimization of KV Cache and Model Compression for Long Context Inference](https://arxiv.org/abs/2512.01953v1) | 2512.01953v1 | 10 |
| 2025-11-29 | [HIMOSA: Efficient Remote Sensing Image Super-Resolution with Hierarchical Mixture of Sparse Attention](https://arxiv.org/abs/2512.00275v1) | 2512.00275v1 | 6 |
| 2025-11-28 | [Every Token Counts: Generalizing 16M Ultra-Long Context in Large Language Models](https://arxiv.org/abs/2511.23319v1) | 2511.23319v1 | 11 |
| 2025-11-28 | [db-SP: Accelerating Sparse Attention for Visual Generative Models with Dual-Balanced Sequence Parallelism](https://arxiv.org/abs/2511.23113v1) | 2511.23113v1 | 6 |
| 2025-11-25 | [SSA: Sparse Sparse Attention by Aligning Full and Sparse Attention Outputs in Feature Space](https://arxiv.org/abs/2511.20102v4) | 2511.20102v4 | 8 |
| 2025-11-18 | [IMSE: Efficient U-Net-based Speech Enhancement using Inception Depthwise Convolution and Amplitude-Aware Linear Attention](https://arxiv.org/abs/2511.14515v2) | 2511.14515v2 | 6 |
| 2025-11-15 | [FaNe: Towards Fine-Grained Cross-Modal Contrast with False-Negative Reduction and Text-Conditioned Sparse Attention](https://arxiv.org/abs/2511.12215v1) | 2511.12215v1 | 6 |
| 2025-11-15 | [OmniSparse: Training-Aware Fine-Grained Sparse Attention for Long-Video MLLMs](https://arxiv.org/abs/2511.12201v2) | 2511.12201v2 | 8 |
| 2025-11-14 | [KVSwap: Disk-aware KV Cache Offloading for Long-Context On-device Inference](https://arxiv.org/abs/2511.11907v2) | 2511.11907v2 | 8 |
| 2025-11-14 | [LiteAttention: A Temporal Sparse Attention for Diffusion Transformers](https://arxiv.org/abs/2511.11062v1) | 2511.11062v1 | 6 |
| 2025-11-12 | [$π$-Attention: Online Efficient Sparse Transformers for Long-Context Modeling](https://arxiv.org/abs/2511.10696v3) | 2511.10696v3 | 9 |
| 2025-11-10 | [Learning to Focus: Focal Attention for Selective and Scalable Transformers](https://arxiv.org/abs/2511.06818v1) | 2511.06818v1 | 6 |
| 2025-11-09 | [Transolver is a Linear Transformer: Revisiting Physics-Attention through the Lens of Linear Attention](https://arxiv.org/abs/2511.06294v3) | 2511.06294v3 | 6 |
| 2025-11-08 | [MoSKA: Mixture of Shared KV Attention for Efficient Long-Sequence LLM Inference](https://arxiv.org/abs/2511.06010v1) | 2511.06010v1 | 6 |
| 2025-11-07 | [Controllably Efficient Language Models](https://arxiv.org/abs/2511.05313v2) | 2511.05313v2 | 10 |
| 2025-11-05 | [Neural Beamforming with Doppler-Aware Sparse Attention for High Mobility Environments](https://arxiv.org/abs/2511.03632v1) | 2511.03632v1 | 6 |
| 2025-11-05 | [Efficient Linear Attention for Multivariate Time Series Modeling via Entropy Calibration](https://arxiv.org/abs/2511.03190v2) | 2511.03190v2 | 6 |
| 2025-11-05 | [Jailbreaking in the Haystack](https://arxiv.org/abs/2511.04707v2) | 2511.04707v2 | 6 |
| 2025-11-04 | [Orion-MSP: Multi-Scale Sparse Attention for Tabular In-Context Learning](https://arxiv.org/abs/2511.02818v3) | 2511.02818v3 | 6 |
| 2025-11-04 | [Oolong: Evaluating Long Context Reasoning and Aggregation Capabilities](https://arxiv.org/abs/2511.02817v2) | 2511.02817v2 | 7 |
| 2025-11-04 | [Sample-Efficient Language Modeling with Linear Attention and Lightweight Enhancements](https://arxiv.org/abs/2511.05560v1) | 2511.05560v1 | 10 |
| 2025-11-02 | [FlexiCache: Leveraging Temporal Stability of Attention Heads for Efficient KV Cache Management](https://arxiv.org/abs/2511.00868v2) | 2511.00868v2 | 7 |
| 2025-10-31 | [SpecAttn: Speculating Sparse Attention](https://arxiv.org/abs/2510.27641v1) | 2510.27641v1 | 8 |
| 2025-10-31 | [BiSparse-AAS: Bilinear Sparse Attention and Adaptive Spans Framework for Scalable and Efficient Text Summarization](https://arxiv.org/abs/2510.27516v1) | 2510.27516v1 | 10 |
| 2025-10-31 | [Higher-order Linear Attention](https://arxiv.org/abs/2510.27258v3) | 2510.27258v3 | 8 |
| 2025-10-29 | [PureKV: Plug-and-Play KV Cache Optimization with Spatial-Temporal Sparse Attention for Vision-Language Large Models](https://arxiv.org/abs/2510.25600v2) | 2510.25600v2 | 9 |
| 2025-10-28 | [Long-Context Modeling with Dynamic Hierarchical Sparse Attention for Memory-Constrained LLM Inference](https://arxiv.org/abs/2510.24606v2) | 2510.24606v2 | 11 |
| 2025-10-28 | [SALS: Sparse Attention in Latent Space for KV cache Compression](https://arxiv.org/abs/2510.24273v1) | 2510.24273v1 | 9 |
| 2025-10-27 | [Tagging-Augmented Generation: Assisting Language Models in Finding Intricate Knowledge In Long Contexts](https://arxiv.org/abs/2510.22956v1) | 2510.22956v1 | 7 |
| 2025-10-26 | [SABlock: Semantic-Aware KV Cache Eviction with Adaptive Compression Block Size](https://arxiv.org/abs/2510.22556v1) | 2510.22556v1 | 7 |
| 2025-10-24 | [Transformer Based Linear Attention with Optimized GPU Kernel Implementation](https://arxiv.org/abs/2510.21956v1) | 2510.21956v1 | 6 |
| 2025-10-24 | [Sparser Block-Sparse Attention via Token Permutation](https://arxiv.org/abs/2510.21270v2) | 2510.21270v2 | 10 |
| 2025-10-23 | [Alleviating Forgetfulness of Linear Attention by Hybrid Sparse Attention and Contextualized Learnable Token Eviction](https://arxiv.org/abs/2510.20787v2) | 2510.20787v2 | 16 |
| 2025-10-22 | [Stream: Scaling up Mechanistic Interpretability to Long Context in LLMs via Sparse Attention](https://arxiv.org/abs/2510.19875v2) | 2510.19875v2 | 11 |
| 2025-10-22 | [Every Attention Matters: An Efficient Hybrid Architecture for Long-Context Reasoning](https://arxiv.org/abs/2510.19338v2) | 2510.19338v2 | 7 |
| 2025-10-21 | [MTraining: Distributed Dynamic Sparse Attention for Efficient Ultra-Long Context Training](https://arxiv.org/abs/2510.18830v2) | 2510.18830v2 | 13 |
| 2025-10-21 | [MoGA: Mixture-of-Groups Attention for End-to-End Long Video Generation](https://arxiv.org/abs/2510.18692v1) | 2510.18692v1 | 6 |
| 2025-10-21 | [Adamas: Hadamard Sparse Attention for Efficient Long-Context Inference](https://arxiv.org/abs/2510.18413v1) | 2510.18413v1 | 9 |
| 2025-10-20 | [Efficient Long-context Language Model Training by Core Attention Disaggregation](https://arxiv.org/abs/2510.18121v1) | 2510.18121v1 | 7 |
| 2025-10-20 | [Understanding and Improving Length Generalization in Hierarchical Sparse Attention Models](https://arxiv.org/abs/2510.17196v3) | 2510.17196v3 | 14 |
| 2025-10-19 | [Efficient High-Accuracy PDEs Solver with the Linear Attention Neural Operator](https://arxiv.org/abs/2510.16816v1) | 2510.16816v1 | 6 |
| 2025-10-19 | [LC-Eval: A Bilingual Multi-Task Evaluation Benchmark for Long-Context Understanding](https://arxiv.org/abs/2510.16783v1) | 2510.16783v1 | 7 |
| 2025-10-19 | [Long-Context Attention Benchmark: From Kernel Efficiency to Distributed Context Parallelism](https://arxiv.org/abs/2510.17896v1) | 2510.17896v1 | 7 |
| 2025-10-15 | [NOSA: Native and Offloadable Sparse Attention](https://arxiv.org/abs/2510.13602v3) | 2510.13602v3 | 8 |
| 2025-10-14 | [APCE: Adaptive Progressive Context Expansion for Long Context Processing](https://arxiv.org/abs/2510.12051v1) | 2510.12051v1 | 7 |
| 2025-10-12 | [DCP: Addressing Input Dynamism In Long-Context Training via Dynamic Context Parallelism](https://arxiv.org/abs/2510.10620v1) | 2510.10620v1 | 7 |
| 2025-10-10 | [DELTA: Dynamic Layer-Aware Token Attention for Efficient Long-Context Reasoning](https://arxiv.org/abs/2510.09883v2) | 2510.09883v2 | 9 |
| 2025-10-09 | [LinearSR: Unlocking Linear Attention for Stable and Efficient Image Super-Resolution](https://arxiv.org/abs/2510.08771v4) | 2510.08771v4 | 6 |
| 2025-10-09 | [OBCache: Optimal Brain KV Cache Pruning for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2510.07651v4) | 2510.07651v4 | 6 |
| 2025-10-08 | [AudioMarathon: A Comprehensive Benchmark for Long-Context Audio Understanding and Efficiency in Audio LLMs](https://arxiv.org/abs/2510.07293v1) | 2510.07293v1 | 7 |
| 2025-10-08 | [Native Hybrid Attention for Efficient Sequence Modeling](https://arxiv.org/abs/2510.07019v3) | 2510.07019v3 | 6 |
| 2025-10-07 | [VecInfer: Efficient LLM Inference with Low-Bit KV Cache via Outlier-Suppressed Vector Quantization](https://arxiv.org/abs/2510.06175v1) | 2510.06175v1 | 6 |
| 2025-10-07 | [Untangling Component Imbalance in Hybrid Linear Attention Conversion Methods](https://arxiv.org/abs/2510.05901v2) | 2510.05901v2 | 6 |
| 2025-10-07 | [vAttention: Verified Sparse Attention](https://arxiv.org/abs/2510.05688v2) | 2510.05688v2 | 6 |
| 2025-10-06 | [KVLinC : KV Cache Quantization with Hadamard Rotation and Linear Correction](https://arxiv.org/abs/2510.05373v1) | 2510.05373v1 | 9 |
| 2025-10-05 | [PatternKV: Flattening KV Representation Expands Quantization Headroom](https://arxiv.org/abs/2510.05176v2) | 2510.05176v2 | 6 |
| 2025-10-04 | [No Tokens Wasted: Leveraging Long Context in Biomedical Vision-Language Models](https://arxiv.org/abs/2510.03978v1) | 2510.03978v1 | 7 |
| 2025-10-02 | [Input-Aware Sparse Attention for Real-Time Co-Speech Video Generation](https://arxiv.org/abs/2510.02617v1) | 2510.02617v1 | 6 |
| 2025-10-02 | [VideoNSA: Native Sparse Attention Scales Video Understanding](https://arxiv.org/abs/2510.02295v2) | 2510.02295v2 | 14 |
| 2025-10-02 | [ReSSFormer: A Recursive Sparse Structured Transformer for Scalable and Long-Context Reasoning](https://arxiv.org/abs/2510.01585v1) | 2510.01585v1 | 7 |
| 2025-10-01 | [Local Linear Attention: An Optimal Interpolation of Linear and Softmax Attention For Test-Time Regression](https://arxiv.org/abs/2510.01450v1) | 2510.01450v1 | 6 |
| 2025-09-29 | [FlashOmni: A Unified Sparse Attention Engine for Diffusion Transformers](https://arxiv.org/abs/2509.25401v1) | 2509.25401v1 | 6 |
| 2025-09-29 | [ProxyAttn: Guided Sparse Attention via Representative Heads](https://arxiv.org/abs/2509.24745v2) | 2509.24745v2 | 6 |
| 2025-09-29 | [SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer](https://arxiv.org/abs/2509.24695v2) | 2509.24695v2 | 6 |
| 2025-09-29 | [InfLLM-V2: Dense-Sparse Switchable Attention for Seamless Short-to-Long Adaptation](https://arxiv.org/abs/2509.24663v1) | 2509.24663v1 | 6 |
| 2025-09-29 | [SparseServe: Unlocking Parallelism for Dynamic Sparse Attention in Long-Context LLM Serving](https://arxiv.org/abs/2509.24626v1) | 2509.24626v1 | 13 |
| 2025-09-29 | [Short window attention enables long-term memorization](https://arxiv.org/abs/2509.24552v3) | 2509.24552v3 | 8 |
| 2025-09-28 | [SparseD: Sparse Attention for Diffusion Language Models](https://arxiv.org/abs/2509.24014v1) | 2509.24014v1 | 10 |
| 2025-09-28 | [SLA: Beyond Sparsity in Diffusion Transformers via Fine-Tunable Sparse-Linear Attention](https://arxiv.org/abs/2509.24006v2) | 2509.24006v2 | 6 |
| 2025-09-28 | [Efficient Turing Machine Simulation with Transformers](https://arxiv.org/abs/2512.00003v2) | 2512.00003v2 | 6 |
| 2025-09-27 | [LOTFormer: Doubly-Stochastic Linear Attention via Low-Rank Optimal Transport](https://arxiv.org/abs/2509.23436v2) | 2509.23436v2 | 8 |
| 2025-09-26 | [StateX: Enhancing RNN Recall via Post-training State Expansion](https://arxiv.org/abs/2509.22630v3) | 2509.22630v3 | 6 |
| 2025-09-24 | [Enhancing Linear Attention with Residual Learning](https://arxiv.org/abs/2509.25223v1) | 2509.25223v1 | 6 |
| 2025-09-23 | [CompLLM: Compression for Long Context Q&A](https://arxiv.org/abs/2509.19228v2) | 2509.19228v2 | 7 |
| 2025-09-22 | [LAWCAT: Efficient Distillation from Quadratic to Linear Attention with Convolution across Tokens for Long Context Modeling](https://arxiv.org/abs/2509.18467v2) | 2509.18467v2 | 13 |
| 2025-09-20 | [FG-Attn: Leveraging Fine-Grained Sparse Attention in Video Diffusion Models](https://arxiv.org/abs/2509.16518v2) | 2509.16518v2 | 10 |
| 2025-09-19 | [UniGist: Towards General and Hardware-aligned Sequence-level Long Context Compression](https://arxiv.org/abs/2509.15763v1) | 2509.15763v1 | 7 |
| 2025-09-16 | [SAGA: Selective Adaptive Gating for Efficient and Expressive Linear Attention](https://arxiv.org/abs/2509.12817v2) | 2509.12817v2 | 6 |
| 2025-09-11 | [Efficient Transformer-Based Piano Transcription With Sparse Attention Mechanisms](https://arxiv.org/abs/2509.09318v1) | 2509.09318v1 | 6 |
| 2025-09-05 | [Elucidating the Design Space of Decay in Linear Attention](https://arxiv.org/abs/2509.05282v1) | 2509.05282v1 | 6 |
| 2025-09-05 | [SpikingBrain: Spiking Brain-inspired Large Models](https://arxiv.org/abs/2509.05276v4) | 2509.05276v4 | 6 |
| 2025-09-05 | [KVCompose: Efficient Structured KV Cache Compression with Composite Tokens](https://arxiv.org/abs/2509.05165v2) | 2509.05165v2 | 7 |
| 2025-09-01 | [Bidirectional Sparse Attention for Faster Video Diffusion Training](https://arxiv.org/abs/2509.01085v4) | 2509.01085v4 | 6 |
| 2025-08-28 | [Mixture of Contexts for Long Video Generation](https://arxiv.org/abs/2508.21058v3) | 2508.21058v3 | 8 |
| 2025-08-28 | [Rethinking Transformer Connectivity: TLinFormer, A Path to Exact, Full Context-Aware Linear Attention](https://arxiv.org/abs/2508.20407v1) | 2508.20407v1 | 8 |
| 2025-08-27 | [FLASepformer: Efficient Speech Separation with Gated Focused Linear Attention Transformer](https://arxiv.org/abs/2508.19528v1) | 2508.19528v1 | 6 |
| 2025-08-26 | [Strata: Hierarchical Context Caching for Long Context Language Model Serving](https://arxiv.org/abs/2508.18572v1) | 2508.18572v1 | 7 |
| 2025-08-25 | [FSA: An Alternative Efficient Implementation of Native Sparse Attention Kernel](https://arxiv.org/abs/2508.18224v3) | 2508.18224v3 | 14 |
| 2025-08-20 | [Hydra: A Modular Architecture for Efficient Long-Context Reasoning](https://arxiv.org/abs/2508.15099v3) | 2508.15099v3 | 7 |
| 2025-08-20 | [H2EAL: Hybrid-Bonding Architecture with Hybrid Sparse Attention for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2508.16653v2) | 2508.16653v2 | 13 |
| 2025-08-17 | [ZigzagAttention: Efficient Long-Context Inference with Exclusive Retrieval and Streaming Heads](https://arxiv.org/abs/2508.12407v1) | 2508.12407v1 | 7 |
| 2025-08-14 | [BLADE: Block-Sparse Attention Meets Step Distillation for Efficient Video Generation](https://arxiv.org/abs/2508.10774v2) | 2508.10774v2 | 6 |
| 2025-08-14 | [Natively Trainable Sparse Attention for Hierarchical Point Cloud Datasets](https://arxiv.org/abs/2508.10758v1) | 2508.10758v1 | 10 |
| 2025-08-14 | [REAL: REtrieval-reAsoning and Logic-constructed Attention Behaviors for Long-Context KV Cache Compression](https://arxiv.org/abs/2508.15806v2) | 2508.15806v2 | 6 |
| 2025-08-13 | [Multimodal Fusion And Sparse Attention-based Alignment Model for Long Sequential Recommendation](https://arxiv.org/abs/2508.09664v1) | 2508.09664v1 | 6 |
| 2025-08-12 | [Retrospective Sparse Attention for Efficient Long-Context Generation](https://arxiv.org/abs/2508.09001v2) | 2508.09001v2 | 11 |
| 2025-08-09 | [Less Is More: Fast and Accurate Reasoning with Cross-Head Unified Sparse Attention](https://arxiv.org/abs/2508.07101v2) | 2508.07101v2 | 8 |
| 2025-08-06 | [TCSAFormer: Efficient Vision Transformer with Token Compression and Sparse Attention for Medical Image Segmentation](https://arxiv.org/abs/2508.04058v1) | 2508.04058v1 | 6 |
| 2025-08-06 | [Sparse Attention across Multiple-context KV Cache](https://arxiv.org/abs/2508.11661v1) | 2508.11661v1 | 9 |
| 2025-08-04 | [Sparse-dLLM: Accelerating Diffusion LLMs with Dynamic Cache Eviction](https://arxiv.org/abs/2508.02558v2) | 2508.02558v2 | 6 |
| 2025-08-04 | [Trainable Dynamic Mask Sparse Attention](https://arxiv.org/abs/2508.02124v6) | 2508.02124v6 | 8 |
| 2025-08-03 | [SPARTA: Advancing Sparse Attention in Spiking Neural Networks via Spike-Timing-Based Prioritization](https://arxiv.org/abs/2508.01646v2) | 2508.01646v2 | 6 |
| 2025-07-28 | [SmallThinker: A Family of Efficient Large Language Models Natively Trained for Local Deployment](https://arxiv.org/abs/2507.20984v2) | 2507.20984v2 | 6 |
| 2025-07-26 | [HCAttention: Extreme KV Cache Compression via Heterogeneous Attention Computing for LLMs](https://arxiv.org/abs/2507.19823v1) | 2507.19823v1 | 6 |
| 2025-07-25 | [DeltaLLM: Delta-Key Sparse Attention for Edge LLMs](https://arxiv.org/abs/2507.19608v2) | 2507.19608v2 | 8 |
| 2025-07-25 | [Efficient Attention Mechanisms for Large Language Models: A Survey](https://arxiv.org/abs/2507.19595v3) | 2507.19595v3 | 10 |
| 2025-07-22 | [Scaling Linear Attention with Sparse State Expansion](https://arxiv.org/abs/2507.16577v2) | 2507.16577v2 | 8 |
| 2025-07-19 | [GRACE: Generative Recommendation via Journey-Aware Sparse Attention on Chain-of-Thought Tokenization](https://arxiv.org/abs/2507.14758v1) | 2507.14758v1 | 6 |
| 2025-07-14 | [Pimba: A Processing-in-Memory Acceleration for Post-Transformer Large Language Model Serving](https://arxiv.org/abs/2507.10178v3) | 2507.10178v3 | 6 |
| 2025-07-08 | [A Systematic Analysis of Hybrid Linear Attention](https://arxiv.org/abs/2507.06457v2) | 2507.06457v2 | 6 |
| 2025-07-06 | [Scaling Context Requires Rethinking Attention](https://arxiv.org/abs/2507.04239v1) | 2507.04239v1 | 10 |
| 2025-07-04 | [Degrees of Freedom for Linear Attention: Distilling Softmax Attention with Optimal Feature Efficiency](https://arxiv.org/abs/2507.03340v1) | 2507.03340v1 | 6 |
| 2025-07-03 | [HGCA: Hybrid GPU-CPU Attention for Long Context LLM Inference](https://arxiv.org/abs/2507.03153v1) | 2507.03153v1 | 11 |
| 2025-07-03 | [Understanding and Improving Length Generalization in Recurrent Models](https://arxiv.org/abs/2507.02782v2) | 2507.02782v2 | 8 |
| 2025-07-01 | [ZeCO: Zero Communication Overhead Sequence Parallelism for Linear Attention](https://arxiv.org/abs/2507.01004v2) | 2507.01004v2 | 6 |
| 2025-07-01 | [Rectifying Magnitude Neglect in Linear Attention](https://arxiv.org/abs/2507.00698v3) | 2507.00698v3 | 6 |
| 2025-07-01 | [Overcoming Long-Context Limitations of State-Space Models via Context-Dependent Sparse Attention](https://arxiv.org/abs/2507.00449v3) | 2507.00449v3 | 9 |
| 2025-06-26 | [Norm$\times$Direction: Restoring the Missing Query Norm in Vision Linear Attention](https://arxiv.org/abs/2506.21137v3) | 2506.21137v3 | 6 |
| 2025-06-24 | [Radial Attention: $O(n\log n)$ Sparse Attention with Energy Decay for Long Video Generation](https://arxiv.org/abs/2506.19852v2) | 2506.19852v2 | 10 |
| 2025-06-23 | [CommVQ: Commutative Vector Quantization for KV Cache Compression](https://arxiv.org/abs/2506.18879v1) | 2506.18879v1 | 9 |
| 2025-06-23 | [Make It Efficient: Dynamic Sparse Attention for Autoregressive Image Generation](https://arxiv.org/abs/2506.18226v1) | 2506.18226v1 | 8 |
| 2025-06-21 | [MDSAM:Memory-Driven Sparse Attention Matrix for LVLMs Hallucination Mitigation](https://arxiv.org/abs/2506.17664v1) | 2506.17664v1 | 6 |
| 2025-06-20 | [Cache Me If You Can: How Many KVs Do You Need for Effective Long-Context LMs?](https://arxiv.org/abs/2506.17121v1) | 2506.17121v1 | 9 |
| 2025-06-19 | [Long-Context Generalization with Sparse Attention](https://arxiv.org/abs/2506.16640v4) | 2506.16640v4 | 9 |
| 2025-06-19 | [MoiréXNet: Adaptive Multi-Scale Demoiréing with Linear Attention Test-Time Training and Truncated Flow Matching Prior](https://arxiv.org/abs/2506.15929v1) | 2506.15929v1 | 6 |
| 2025-06-18 | [RATTENTION: Towards the Minimal Sliding Window Size in Local-Global Attention Models](https://arxiv.org/abs/2506.15545v2) | 2506.15545v2 | 6 |
| 2025-06-16 | [Gated Rotary-Enhanced Linear Attention with Rank Modulation for Long-term Sequential Recommendation](https://arxiv.org/abs/2506.13315v4) | 2506.13315v4 | 6 |
| 2025-06-16 | [Multipole Attention for Efficient Long Context Reasoning](https://arxiv.org/abs/2506.13059v2) | 2506.13059v2 | 11 |
| 2025-06-14 | [BSA: Ball Sparse Attention for Large-scale Geometries](https://arxiv.org/abs/2506.12541v1) | 2506.12541v1 | 10 |
| 2025-06-13 | [Beyond Homogeneous Attention: Memory-Efficient LLMs via Fourier-Approximated KV Cache](https://arxiv.org/abs/2506.11886v1) | 2506.11886v1 | 7 |
| 2025-06-13 | [Lag-Relative Sparse Attention In Long Context Training](https://arxiv.org/abs/2506.11498v1) | 2506.11498v1 | 11 |
| 2025-06-13 | [CentroidKV: Efficient Long-Context LLM Inference via KV Cache Clustering](https://arxiv.org/abs/2506.11418v2) | 2506.11418v2 | 6 |
| 2025-06-11 | [On-the-Fly Adaptive Distillation of Transformer to Dual-State Linear Attention](https://arxiv.org/abs/2506.09316v3) | 2506.09316v3 | 8 |
| 2025-06-10 | [SeerAttention-R: Sparse Attention Adaptation for Long Reasoning](https://arxiv.org/abs/2506.08889v1) | 2506.08889v1 | 6 |
| 2025-06-10 | [Plug-and-play linear attention with provable guarantees for training-free image restoration](https://arxiv.org/abs/2506.08520v2) | 2506.08520v2 | 7 |
| 2025-06-10 | [Draft-based Approximate Inference for LLMs](https://arxiv.org/abs/2506.08373v3) | 2506.08373v3 | 8 |
| 2025-06-09 | [Efficient Seismic Data Interpolation via Sparse Attention Transformer and Diffusion Model](https://arxiv.org/abs/2506.07923v1) | 2506.07923v1 | 6 |
| 2025-06-09 | [MiniCPM4: Ultra-Efficient LLMs on End Devices](https://arxiv.org/abs/2506.07900v2) | 2506.07900v2 | 6 |
| 2025-06-06 | [DAM: Dynamic Attention Mask for Long-Context Large Language Model Inference Acceleration](https://arxiv.org/abs/2506.11104v1) | 2506.11104v1 | 7 |
| 2025-06-06 | [Cartridges: Lightweight and general-purpose long context representations via self-study](https://arxiv.org/abs/2506.06266v3) | 2506.06266v3 | 9 |
| 2025-06-06 | [MadaKV: Adaptive Modality-Perception KV Cache Eviction for Efficient Multimodal Long-Context Inference](https://arxiv.org/abs/2506.15724v1) | 2506.15724v1 | 6 |
| 2025-06-05 | [TabFlex: Scaling Tabular Learning to Millions with Linear Attention](https://arxiv.org/abs/2506.05584v1) | 2506.05584v1 | 6 |
| 2025-06-05 | [Inference-Time Hyper-Scaling with KV Cache Compression](https://arxiv.org/abs/2506.05345v2) | 2506.05345v2 | 7 |
| 2025-06-05 | [Log-Linear Attention](https://arxiv.org/abs/2506.04761v3) | 2506.04761v3 | 6 |
| 2025-06-04 | [Homogeneous Keys, Heterogeneous Values: Exploiting Local KV Cache Asymmetry for Long-Context LLMs](https://arxiv.org/abs/2506.05410v2) | 2506.05410v2 | 8 |
| 2025-06-04 | [Rectified Sparse Attention](https://arxiv.org/abs/2506.04108v2) | 2506.04108v2 | 10 |
| 2025-06-01 | [Compress, Gather, and Recompute: REFORMing Long-Context Processing in Transformers](https://arxiv.org/abs/2506.01215v2) | 2506.01215v2 | 9 |
| 2025-05-30 | [SALE : Low-bit Estimation for Efficient Sparse Attention in Long-context LLM Prefilling](https://arxiv.org/abs/2505.24179v1) | 2505.24179v1 | 9 |
| 2025-05-30 | [Learn from the Past: Fast Sparse Indexing for Large Language Model Decoding](https://arxiv.org/abs/2506.15704v1) | 2506.15704v1 | 6 |
| 2025-05-29 | [ATLAS: Learning to Optimally Memorize the Context at Test Time](https://arxiv.org/abs/2505.23735v1) | 2505.23735v1 | 6 |
| 2025-05-29 | [LoLA: Low-Rank Linear Attention With Sparse Caching](https://arxiv.org/abs/2505.23666v3) | 2505.23666v3 | 8 |
| 2025-05-29 | [AnchorAttention: Difference-Aware Sparse Attention with Stripe Granularity](https://arxiv.org/abs/2505.23520v1) | 2505.23520v1 | 8 |
| 2025-05-28 | [Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference](https://arxiv.org/abs/2505.22913v2) | 2505.22913v2 | 9 |
| 2025-05-28 | [Bayesian Attention Mechanism: A Probabilistic Framework for Positional Encoding and Context Length Extrapolation](https://arxiv.org/abs/2505.22842v4) | 2505.22842v4 | 7 |
| 2025-05-28 | [FIER: Fine-Grained and Efficient KV Cache Retrieval for Long-context LLM Inference](https://arxiv.org/abs/2508.08256v2) | 2508.08256v2 | 10 |
| 2025-05-26 | [HoPE: Hybrid of Position Embedding for Long Context Vision-Language Models](https://arxiv.org/abs/2505.20444v2) | 2505.20444v2 | 7 |
| 2025-05-26 | [TailorKV: A Hybrid Framework for Long-Context Inference via Tailored KV Cache Optimization](https://arxiv.org/abs/2505.19586v2) | 2505.19586v2 | 6 |
| 2025-05-26 | [Accelerating Prefilling for Long-Context LLMs via Sparse Pattern Sharing](https://arxiv.org/abs/2505.19578v1) | 2505.19578v1 | 7 |
| 2025-05-24 | [Sparse VideoGen2: Accelerate Video Generation with Sparse Attention via Semantic-Aware Permutation](https://arxiv.org/abs/2505.18875v5) | 2505.18875v5 | 6 |
| 2025-05-24 | [VORTA: Efficient Video Diffusion via Routing Sparse Attention](https://arxiv.org/abs/2505.18809v2) | 2505.18809v2 | 6 |
| 2025-05-23 | [QwenLong-CPRS: Towards $\infty$-LLMs with Dynamic Context Optimization](https://arxiv.org/abs/2505.18092v2) | 2505.18092v2 | 6 |
| 2025-05-23 | [The emergence of sparse attention: impact of data distribution and benefits of repetition](https://arxiv.org/abs/2505.17863v2) | 2505.17863v2 | 6 |
| 2025-05-23 | [Titanus: Enabling KV Cache Pruning and Quantization On-the-Fly for LLM Acceleration](https://arxiv.org/abs/2505.17787v1) | 2505.17787v1 | 7 |
| 2025-05-23 | [Direct3D-S2: Gigascale 3D Generation Made Easy with Spatial Sparse Attention](https://arxiv.org/abs/2505.17412v2) | 2505.17412v2 | 6 |
| 2025-05-22 | [Fast and Accurate Image Restoration and Generation with Rank Enhanced Linear Attention](https://arxiv.org/abs/2505.16157v3) | 2505.16157v3 | 6 |
| 2025-05-21 | [A Framework for Non-Linear Attention via Modern Hopfield Networks](https://arxiv.org/abs/2506.11043v1) | 2506.11043v1 | 6 |
| 2025-05-20 | [Advancing Multi-Agent RAG Systems with Minimalist Reinforcement Learning](https://arxiv.org/abs/2505.17086v4) | 2505.17086v4 | 6 |
| 2025-05-19 | [VSA: Faster Video Diffusion with Trainable Sparse Attention](https://arxiv.org/abs/2505.13389v5) | 2505.13389v5 | 6 |
| 2025-05-19 | [FreeKV: Boosting KV Cache Retrieval for Efficient LLM Inference](https://arxiv.org/abs/2505.13109v5) | 2505.13109v5 | 7 |
| 2025-05-16 | [Delta Attention: Fast and Accurate Sparse Attention Inference by Delta Correction](https://arxiv.org/abs/2505.11254v2) | 2505.11254v2 | 15 |
| 2025-05-12 | [Fused3S: Fast Sparse Attention on Tensor Cores](https://arxiv.org/abs/2505.08098v1) | 2505.08098v1 | 6 |
| 2025-05-10 | [Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free](https://arxiv.org/abs/2505.06708v1) | 2505.06708v1 | 6 |
| 2025-05-09 | [Sparse Attention Remapping with Clustering for Efficient LLM Decoding on PIM](https://arxiv.org/abs/2505.05772v2) | 2505.05772v2 | 12 |
| 2025-05-05 | [RADLADS: Rapid Attention Distillation to Linear Attention Decoders at Scale](https://arxiv.org/abs/2505.03005v4) | 2505.03005v4 | 6 |
| 2025-05-05 | [RetroInfer: A Vector Storage Engine for Scalable Long-Context LLM Inference](https://arxiv.org/abs/2505.02922v3) | 2505.02922v3 | 11 |
| 2025-05-01 | [FreqKV: Key-Value Compression in Frequency Domain for Context Window Extension](https://arxiv.org/abs/2505.00570v3) | 2505.00570v3 | 8 |
| 2025-05-01 | [Mixture of Sparse Attention: Content-Based Learnable Sparse Attention via Expert-Choice Routing](https://arxiv.org/abs/2505.00315v1) | 2505.00315v1 | 6 |
| 2025-04-30 | [RWKV-X: A Linear Complexity Hybrid Language Model](https://arxiv.org/abs/2504.21463v2) | 2504.21463v2 | 6 |
| 2025-04-26 | [Effective Length Extrapolation via Dimension-Wise Positional Embeddings Manipulation](https://arxiv.org/abs/2504.18857v1) | 2504.18857v1 | 6 |
| 2025-04-24 | [The Sparse Frontier: Sparse Attention Trade-offs in Transformer LLMs](https://arxiv.org/abs/2504.17768v3) | 2504.17768v3 | 8 |
| 2025-04-23 | [Generalized Neighborhood Attention: Multi-dimensional Sparse Attention at the Speed of Light](https://arxiv.org/abs/2504.16922v1) | 2504.16922v1 | 6 |
| 2025-04-23 | [Hardware-aligned Hierarchical Sparse Attention for Efficient Long-term Memory Access](https://arxiv.org/abs/2504.16795v2) | 2504.16795v2 | 10 |
| 2025-04-23 | [Sparsity Forcing: Reinforcing Token Sparsity of MLLMs](https://arxiv.org/abs/2504.18579v4) | 2504.18579v4 | 6 |
| 2025-04-22 | [MMInference: Accelerating Pre-filling for Long-Context VLMs via Modality-Aware Permutation Sparse Attention](https://arxiv.org/abs/2504.16083v2) | 2504.16083v2 | 9 |
| 2025-04-22 | [LongMamba: Enhancing Mamba's Long Context Capabilities via Training-Free Receptive Field Enlargement](https://arxiv.org/abs/2504.16053v1) | 2504.16053v1 | 7 |
| 2025-04-22 | [llm-jp-modernbert: A ModernBERT Model Trained on a Large-Scale Japanese Corpus with Long Context Length](https://arxiv.org/abs/2504.15544v1) | 2504.15544v1 | 8 |
| 2025-04-18 | [CacheFormer: High Attention-Based Segment Caching](https://arxiv.org/abs/2504.13981v1) | 2504.13981v1 | 6 |
| 2025-04-17 | [Scaling Instruction-Tuned LLMs to Million-Token Contexts via Hierarchical Synthetic Data Generation](https://arxiv.org/abs/2504.12637v1) | 2504.12637v1 | 6 |
| 2025-04-16 | [MOM: Memory-Efficient Offloaded Mini-Sequence Inference for Long Context Language Models](https://arxiv.org/abs/2504.12526v1) | 2504.12526v1 | 9 |
| 2025-04-16 | [Cobra: Efficient Line Art COlorization with BRoAder References](https://arxiv.org/abs/2504.12240v3) | 2504.12240v3 | 6 |
| 2025-04-14 | [AlayaDB: The Data Foundation for Efficient and Effective Long-context LLM Inference](https://arxiv.org/abs/2504.10326v1) | 2504.10326v1 | 9 |
| 2025-04-11 | [Harnessing the Unseen: The Hidden Influence of Intrinsic Knowledge in Long-Context Language Models](https://arxiv.org/abs/2504.08202v2) | 2504.08202v2 | 7 |
| 2025-04-10 | [UniCAIM: A Unified CAM/CIM Architecture with Static-Dynamic KV Cache Pruning for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2504.07479v1) | 2504.07479v1 | 6 |
| 2025-04-08 | [SPIRe: Boosting LLM Inference Throughput with Speculative Decoding](https://arxiv.org/abs/2504.06419v1) | 2504.06419v1 | 8 |
| 2025-04-08 | [From 128K to 4M: Efficient Training of Ultra-Long Context Large Language Models](https://arxiv.org/abs/2504.06214v1) | 2504.06214v1 | 7 |
| 2025-04-06 | [Gating is Weighting: Understanding Gated Linear Attention through In-context Learning](https://arxiv.org/abs/2504.04308v1) | 2504.04308v1 | 6 |
| 2025-04-04 | [Clinical ModernBERT: An efficient and long context encoder for biomedical text](https://arxiv.org/abs/2504.03964v1) | 2504.03964v1 | 9 |
| 2025-03-29 | [SPFinder: Improving the Context Length and Scalability for Tracing Known Vulnerability Patches](https://arxiv.org/abs/2503.22935v4) | 2503.22935v4 | 7 |
| 2025-03-24 | [BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache](https://arxiv.org/abs/2503.18773v3) | 2503.18773v3 | 6 |
| 2025-03-20 | [iFlame: Interleaving Full and Linear Attention for Efficient Mesh Generation](https://arxiv.org/abs/2503.16653v2) | 2503.16653v2 | 8 |
| 2025-03-20 | [XAttention: Block Sparse Attention with Antidiagonal Scoring](https://arxiv.org/abs/2503.16428v1) | 2503.16428v1 | 8 |
| 2025-03-18 | [Tiled Flash Linear Attention: More Efficient Linear RNN and xLSTM Kernels](https://arxiv.org/abs/2503.14376v3) | 2503.14376v3 | 12 |
| 2025-03-14 | [Key, Value, Compress: A Systematic Exploration of KV Cache Compression Techniques](https://arxiv.org/abs/2503.11816v3) | 2503.11816v3 | 7 |
| 2025-03-14 | [FMNet: Frequency-Assisted Mamba-Like Linear Attention Network for Camouflaged Object Detection](https://arxiv.org/abs/2503.11030v2) | 2503.11030v2 | 6 |
| 2025-03-13 | [KV-Distill: Nearly Lossless Learnable Context Compression for LLMs](https://arxiv.org/abs/2503.10337v1) | 2503.10337v1 | 6 |
| 2025-03-13 | [ZSMerge: Zero-Shot KV Cache Compression for Memory-Efficient Long-Context LLMs](https://arxiv.org/abs/2503.10714v3) | 2503.10714v3 | 6 |
| 2025-03-12 | [TabNSA: Native Sparse Attention for Efficient Tabular Data Learning](https://arxiv.org/abs/2503.09850v3) | 2503.09850v3 | 12 |
| 2025-03-12 | [Attention Reveals More Than Tokens: Training-Free Long-Context Reasoning with Attention-guided Retrieval](https://arxiv.org/abs/2503.09819v1) | 2503.09819v1 | 7 |
| 2025-03-12 | [MILLION: Mastering Long-Context LLM Inference Via Outlier-Immunized KV Product Quantization](https://arxiv.org/abs/2504.03661v2) | 2504.03661v2 | 7 |
| 2025-03-11 | [LLMs Know What to Drop: Self-Attention Guided KV Cache Eviction for Efficient Long-Context Inference](https://arxiv.org/abs/2503.08879v1) | 2503.08879v1 | 7 |
| 2025-03-11 | [Efficient Many-Shot In-Context Learning with Dynamic Block-Sparse Attention](https://arxiv.org/abs/2503.08640v2) | 2503.08640v2 | 6 |
| 2025-03-06 | [SCSA: A Plug-and-Play Semantic Continuous-Sparse Attention for Arbitrary Semantic Style Transfer](https://arxiv.org/abs/2503.04119v1) | 2503.04119v1 | 6 |
| 2025-03-05 | [PowerAttention: Exponentially Scaling of Receptive Fields for Effective Sparse Attention](https://arxiv.org/abs/2503.03588v1) | 2503.03588v1 | 12 |
| 2025-03-05 | [Conformal Transformations for Symmetric Power Transformers](https://arxiv.org/abs/2503.03269v2) | 2503.03269v2 | 6 |
| 2025-03-04 | [Q-Filters: Leveraging QK Geometry for Efficient KV Cache Compression](https://arxiv.org/abs/2503.02812v1) | 2503.02812v1 | 7 |
| 2025-03-01 | [Progressive Sparse Attention: Algorithm and System Co-design for Efficient Attention in LLM Serving](https://arxiv.org/abs/2503.00392v1) | 2503.00392v1 | 12 |
| 2025-02-28 | [Training-free and Adaptive Sparse Attention for Efficient Long Video Generation](https://arxiv.org/abs/2502.21079v1) | 2502.21079v1 | 6 |
| 2025-02-28 | [FlexPrefill: A Context-Aware Sparse Attention Mechanism for Efficient Long-Sequence Inference](https://arxiv.org/abs/2502.20766v1) | 2502.20766v1 | 6 |
| 2025-02-27 | [RAPID: Long-Context Inference with Retrieval-Augmented Speculative Decoding](https://arxiv.org/abs/2502.20330v2) | 2502.20330v2 | 7 |
| 2025-02-26 | [Sliding Window Attention Training for Efficient Large Language Models](https://arxiv.org/abs/2502.18845v2) | 2502.18845v2 | 12 |
| 2025-02-25 | [SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference](https://arxiv.org/abs/2502.18137v8) | 2502.18137v8 | 6 |
| 2025-02-24 | [MEDA: Dynamic KV Cache Allocation for Efficient Multimodal Long-Context Inference](https://arxiv.org/abs/2502.17599v2) | 2502.17599v2 | 6 |
| 2025-02-24 | [LongSpec: Long-Context Lossless Speculative Decoding with Efficient Drafting and Verification](https://arxiv.org/abs/2502.17421v4) | 2502.17421v4 | 12 |
| 2025-02-24 | [Thus Spake Long-Context Large Language Model](https://arxiv.org/abs/2502.17129v2) | 2502.17129v2 | 7 |
| 2025-02-22 | [Linear Attention for Efficient Bidirectional Sequence Modeling](https://arxiv.org/abs/2502.16249v2) | 2502.16249v2 | 7 |
| 2025-02-21 | [Self-Taught Agentic Long Context Understanding](https://arxiv.org/abs/2502.15920v2) | 2502.15920v2 | 7 |
| 2025-02-20 | [LServe: Efficient Long-sequence LLM Serving with Unified Sparse Attention](https://arxiv.org/abs/2502.14866v2) | 2502.14866v2 | 12 |
| 2025-02-20 | [ParallelComp: Parallel Long-Context Compressor for Length Extrapolation](https://arxiv.org/abs/2502.14317v2) | 2502.14317v2 | 7 |
| 2025-02-20 | [EpMAN: Episodic Memory AttentioN for Generalizing to Longer Contexts](https://arxiv.org/abs/2502.14280v1) | 2502.14280v1 | 6 |
| 2025-02-19 | [RocketKV: Accelerating Long-Context LLM Inference via Two-Stage KV Cache Compression](https://arxiv.org/abs/2502.14051v3) | 2502.14051v3 | 12 |
| 2025-02-19 | [LongPO: Long Context Self-Evolution of Large Language Models through Short-to-Long Preference Optimization](https://arxiv.org/abs/2502.13922v3) | 2502.13922v3 | 7 |
| 2025-02-19 | [Activation-aware Probe-Query: Effective Key-Value Retrieval for Long-Context LLMs Inference](https://arxiv.org/abs/2502.13542v1) | 2502.13542v1 | 9 |
| 2025-02-18 | [MoBA: Mixture of Block Attention for Long-Context LLMs](https://arxiv.org/abs/2502.13189v1) | 2502.13189v1 | 9 |
| 2025-02-18 | [HeadInfer: Memory-Efficient LLM Inference by Head-wise Offloading](https://arxiv.org/abs/2502.12574v1) | 2502.12574v1 | 6 |
| 2025-02-17 | [AdaSplash: Adaptive Sparse Flash Attention](https://arxiv.org/abs/2502.12082v2) | 2502.12082v2 | 8 |
| 2025-02-17 | [Tactic: Adaptive Sparse Attention with Clustering and Distribution Fitting for Long-Context LLMs](https://arxiv.org/abs/2502.12216v1) | 2502.12216v1 | 11 |
| 2025-02-17 | [Does RAG Really Perform Bad For Long-Context Processing?](https://arxiv.org/abs/2502.11444v1) | 2502.11444v1 | 7 |
| 2025-02-16 | [Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention](https://arxiv.org/abs/2502.11089v2) | 2502.11089v2 | 14 |
| 2025-02-14 | [MIR-Bench: Can Your LLM Recognize Complicated Patterns via Many-Shot In-Context Reasoning?](https://arxiv.org/abs/2502.09933v5) | 2502.09933v5 | 6 |
| 2025-02-13 | [InfiniteHiP: Extending Language Model Context Up to 3 Million Tokens on a Single GPU](https://arxiv.org/abs/2502.08910v1) | 2502.08910v1 | 6 |
| 2025-02-12 | [Inference-time sparse attention with asymmetric indexing](https://arxiv.org/abs/2502.08246v2) | 2502.08246v2 | 8 |
| 2025-02-11 | [LASP-2: Rethinking Sequence Parallelism for Linear Attention and Its Hybrid](https://arxiv.org/abs/2502.07563v1) | 2502.07563v1 | 6 |
| 2025-02-09 | [HyLiFormer: Hyperbolic Linear Attention for Skeleton-based Human Action Recognition](https://arxiv.org/abs/2502.05869v1) | 2502.05869v1 | 6 |
| 2025-02-09 | [Linear Attention Modeling for Learned Image Compression](https://arxiv.org/abs/2502.05741v2) | 2502.05741v2 | 6 |
| 2025-02-07 | [NoLiMa: Long-Context Evaluation Beyond Literal Matching](https://arxiv.org/abs/2502.05167v3) | 2502.05167v3 | 7 |
| 2025-02-06 | [KVTuner: Sensitivity-Aware Layer-Wise Mixed-Precision KV Cache Quantization for Efficient and Nearly Lossless LLM Inference](https://arxiv.org/abs/2502.04420v5) | 2502.04420v5 | 7 |
| 2025-02-06 | [AttentionPredictor: Temporal Patterns Matter for KV Cache Compression](https://arxiv.org/abs/2502.04077v3) | 2502.04077v3 | 6 |
| 2025-02-04 | [Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$ Pruning](https://arxiv.org/abs/2502.02770v5) | 2502.02770v5 | 8 |
| 2025-02-03 | [ReGLA: Refining Gated Linear Attention](https://arxiv.org/abs/2502.01578v3) | 2502.01578v3 | 6 |
| 2025-02-01 | [ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference](https://arxiv.org/abs/2502.00299v5) | 2502.00299v5 | 6 |
| 2025-01-31 | [Longer Attention Span: Increasing Transformer Context Length with Sparse Graph Processing Techniques](https://arxiv.org/abs/2502.01659v2) | 2502.01659v2 | 7 |
| 2025-01-27 | [Training Dynamics of In-Context Learning in Linear Attention](https://arxiv.org/abs/2501.16265v2) | 2501.16265v2 | 6 |
| 2025-01-27 | [The Linear Attention Resurrection in Vision Transformer](https://arxiv.org/abs/2501.16182v1) | 2501.16182v1 | 6 |
| 2025-01-27 | [ARFlow: Autoregressive Flow with Hybrid Linear Attention](https://arxiv.org/abs/2501.16085v2) | 2501.16085v2 | 6 |
| 2025-01-26 | [Qwen2.5-1M Technical Report](https://arxiv.org/abs/2501.15383v1) | 2501.15383v1 | 8 |
| 2025-01-25 | [PolaFormer: Polarity-aware Linear Attention for Vision Transformers](https://arxiv.org/abs/2501.15061v2) | 2501.15061v2 | 6 |
| 2025-01-25 | [RotateKV: Accurate and Robust 2-Bit KV Cache Quantization for LLMs via Outlier-Aware Adaptive Rotations](https://arxiv.org/abs/2501.16383v2) | 2501.16383v2 | 7 |
| 2025-01-12 | [MPCache: MPC-Friendly KV Cache Eviction for Efficient Private LLM Inference](https://arxiv.org/abs/2501.06807v2) | 2501.06807v2 | 7 |
| 2025-01-05 | [LeetDecoding: A PyTorch Library for Exponentially Decaying Causal Linear Attention with CUDA Implementations](https://arxiv.org/abs/2501.02573v1) | 2501.02573v1 | 6 |
| 2025-01-01 | [Adjoint sharding for very long context training of state space models](https://arxiv.org/abs/2501.00692v1) | 2501.00692v1 | 7 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-28 | [PIMphony: Overcoming Bandwidth and Capacity Inefficiency in PIM-based Long-Context LLM Inference System](https://arxiv.org/abs/2412.20166v3) | 2412.20166v3 | 9 |
| 2024-12-24 | [Multimodal joint prediction of traffic spatial-temporal data with graph sparse attention mechanism and bidirectional temporal convolutional network](https://arxiv.org/abs/2412.19842v1) | 2412.19842v1 | 6 |
| 2024-12-19 | [DynamicKV: Task-Aware Adaptive KV Cache Compression for Long Context LLMs](https://arxiv.org/abs/2412.14838v4) | 2412.14838v4 | 8 |
| 2024-12-18 | [State Space Models are Strong Text Rerankers](https://arxiv.org/abs/2412.14354v3) | 2412.14354v3 | 6 |
| 2024-12-17 | [Boosting Long-Context Management via Query-Guided Activation Refilling](https://arxiv.org/abs/2412.12486v3) | 2412.12486v3 | 7 |
| 2024-12-17 | [Core Context Aware Transformers for Long Context Language Modeling](https://arxiv.org/abs/2412.12465v3) | 2412.12465v3 | 7 |
| 2024-12-13 | [SCBench: A KV Cache-Centric Analysis of Long-Context Methods](https://arxiv.org/abs/2412.10319v2) | 2412.10319v2 | 10 |
| 2024-12-11 | [EMS: Adaptive Evict-then-Merge Strategy for Head-wise KV Cache Compression Based on Global-Local Importance](https://arxiv.org/abs/2412.08521v2) | 2412.08521v2 | 7 |
| 2024-12-10 | [Breaking the Stage Barrier: A Novel Single-Stage Approach to Long Context Extension for Large Language Models](https://arxiv.org/abs/2412.07171v1) | 2412.07171v1 | 7 |
| 2024-12-09 | [Context Clues: Evaluating Long Context Models for Clinical Prediction Tasks on EHRs](https://arxiv.org/abs/2412.16178v2) | 2412.16178v2 | 7 |
| 2024-12-09 | [Bridging the Divide: Reconsidering Softmax and Linear Attention](https://arxiv.org/abs/2412.06590v1) | 2412.06590v1 | 6 |
| 2024-12-09 | [Gated Delta Networks: Improving Mamba2 with Delta Rule](https://arxiv.org/abs/2412.06464v3) | 2412.06464v3 | 6 |
| 2024-12-09 | [SparseAccelerate: Efficient Long-Context Inference for Mid-Range GPUs](https://arxiv.org/abs/2412.06198v1) | 2412.06198v1 | 9 |
| 2024-12-08 | [XKV: Personalized KV Cache Memory Reduction for Long-Context LLM Inference](https://arxiv.org/abs/2412.05896v1) | 2412.05896v1 | 6 |
| 2024-12-06 | [Ltri-LLM: Streaming Long Context Inference for LLMs with Training-Free Dynamic Triangular Attention Pattern](https://arxiv.org/abs/2412.04757v1) | 2412.04757v1 | 7 |
| 2024-12-05 | [Exploring Real&Synthetic Dataset and Linear Attention in Image Restoration](https://arxiv.org/abs/2412.03814v2) | 2412.03814v2 | 6 |
| 2024-12-04 | [ClusterKV: Manipulating LLM KV Cache in Semantic Space for Recallable Compression](https://arxiv.org/abs/2412.03213v2) | 2412.03213v2 | 7 |
| 2024-12-03 | [UniForm: A Reuse Attention Mechanism Optimized for Efficient Vision Transformers on Edge Devices](https://arxiv.org/abs/2412.02344v1) | 2412.02344v1 | 8 |
| 2024-12-03 | [Compressing KV Cache for Long-Context LLM Inference with Inter-Layer Attention Similarity](https://arxiv.org/abs/2412.02252v2) | 2412.02252v2 | 6 |
| 2024-11-20 | [Transformers with Sparse Attention for Granger Causality](https://arxiv.org/abs/2411.13264v1) | 2411.13264v1 | 6 |
| 2024-11-14 | [Squeezed Attention: Accelerating Long Context Length LLM Inference](https://arxiv.org/abs/2411.09688v3) | 2411.09688v3 | 8 |
| 2024-11-14 | [Reducing Reasoning Costs: The Path of Optimization for Chain of Thought via Sparse Attention Mechanism](https://arxiv.org/abs/2411.09111v8) | 2411.09111v8 | 6 |
| 2024-11-12 | [Breaking the Low-Rank Dilemma of Linear Attention](https://arxiv.org/abs/2411.07635v5) | 2411.07635v5 | 6 |
| 2024-11-11 | [Anchor Attention, Small Cache: Code Generation with Large Language Models](https://arxiv.org/abs/2411.06680v1) | 2411.06680v1 | 6 |
| 2024-11-05 | [TokenSelect: Efficient Long-Context Inference and Length Extrapolation for LLMs via Dynamic Token-Level KV Cache Selection](https://arxiv.org/abs/2411.02886v4) | 2411.02886v4 | 6 |
| 2024-11-03 | [LinRec: Linear Attention Mechanism for Long-term Sequential Recommender Systems](https://arxiv.org/abs/2411.01537v1) | 2411.01537v1 | 6 |
| 2024-11-01 | [Birdie: Advancing State Space Models with Reward-Driven Objectives and Curricula](https://arxiv.org/abs/2411.01030v5) | 2411.01030v5 | 6 |
| 2024-10-31 | [MLLA-UNet: Mamba-like Linear Attention in an Efficient U-Shape Model for Medical Image Segmentation](https://arxiv.org/abs/2410.23738v1) | 2410.23738v1 | 6 |
| 2024-10-30 | [LoFLAT: Local Feature Matching using Focused Linear Attention Transformer](https://arxiv.org/abs/2410.22710v1) | 2410.22710v1 | 6 |
| 2024-10-30 | [Lina-Speech: Gated Linear Attention and Initial-State Tuning for Multi-Sample Prompting Text-To-Speech Synthesis](https://arxiv.org/abs/2410.23320v2) | 2410.23320v2 | 8 |
| 2024-10-28 | [ShadowKV: KV Cache in Shadows for High-Throughput Long-Context LLM Inference](https://arxiv.org/abs/2410.21465v3) | 2410.21465v3 | 10 |
| 2024-10-17 | [SeerAttention: Learning Intrinsic Sparse Attention in Your LLMs](https://arxiv.org/abs/2410.13276v4) | 2410.13276v4 | 8 |
| 2024-10-15 | [Holistic Reasoning with Long-Context LMs: A Benchmark for Database Operations on Massive Textual Data](https://arxiv.org/abs/2410.11996v3) | 2410.11996v3 | 7 |
| 2024-10-14 | [DuoAttention: Efficient Long-Context LLM Inference with Retrieval and Streaming Heads](https://arxiv.org/abs/2410.10819v1) | 2410.10819v1 | 9 |
| 2024-10-14 | [HSR-Enhanced Sparse Attention Acceleration](https://arxiv.org/abs/2410.10165v2) | 2410.10165v2 | 10 |
| 2024-10-14 | [Learning Linear Attention in Polynomial Time](https://arxiv.org/abs/2410.10101v4) | 2410.10101v4 | 6 |
| 2024-10-11 | [ZipVL: Efficient Large Vision-Language Models with Dynamic Token Sparsification](https://arxiv.org/abs/2410.08584v2) | 2410.08584v2 | 7 |
| 2024-10-09 | [Rodimus*: Breaking the Accuracy-Efficiency Trade-Off with Efficient Attentions](https://arxiv.org/abs/2410.06577v2) | 2410.06577v2 | 6 |
| 2024-10-07 | [Differential Transformer](https://arxiv.org/abs/2410.05258v2) | 2410.05258v2 | 6 |
| 2024-10-07 | [TidalDecode: Fast and Accurate LLM Decoding with Position Persistent Sparse Attention](https://arxiv.org/abs/2410.05076v1) | 2410.05076v1 | 8 |
| 2024-10-05 | [Correlation-Aware Select and Merge Attention for Efficient Fine-Tuning and Context Length Extension](https://arxiv.org/abs/2410.04211v1) | 2410.04211v1 | 7 |
| 2024-10-03 | [L-CiteEval: Do Long-Context Models Truly Leverage Context for Responding?](https://arxiv.org/abs/2410.02115v2) | 2410.02115v2 | 7 |
| 2024-10-02 | [Locret: Enhancing Eviction in Long-Context LLM Inference with Trained Retaining Heads on Consumer-Grade Devices](https://arxiv.org/abs/2410.01805v2) | 2410.01805v2 | 7 |
| 2024-10-02 | [Efficient Length-Generalizable Attention via Causal Retrieval for Long-Context Language Modeling](https://arxiv.org/abs/2410.01651v4) | 2410.01651v4 | 7 |
| 2024-10-02 | [A Little Goes a Long Way: Efficient Long Context Training and Inference with Partial Contexts](https://arxiv.org/abs/2410.01485v2) | 2410.01485v2 | 13 |
| 2024-09-30 | [KV-Compress: Paged KV-Cache Compression with Variable Compression Rates per Attention Head](https://arxiv.org/abs/2410.00161v2) | 2410.00161v2 | 6 |
| 2024-09-26 | [Dynamic Subframe Splitting and Spatio-Temporal Motion Entangled Sparse Attention for RGB-E Tracking](https://arxiv.org/abs/2409.17560v1) | 2409.17560v1 | 6 |
| 2024-09-25 | [Discovering the Gems in Early Layers: Accelerating Long-Context LLMs with 1000x Input Token Reduction](https://arxiv.org/abs/2409.17422v1) | 2409.17422v1 | 7 |
| 2024-09-23 | [Inference-Friendly Models With MixAttention](https://arxiv.org/abs/2409.15012v1) | 2409.15012v1 | 10 |
| 2024-09-19 | [CritiPrefill: A Segment-wise Criticality-based Approach for Prefilling Acceleration in LLMs](https://arxiv.org/abs/2409.12490v2) | 2409.12490v2 | 7 |
| 2024-09-16 | [CSKV: Training-Efficient Channel Shrinking for KV Cache in Long-Context Scenarios](https://arxiv.org/abs/2409.10593v3) | 2409.10593v3 | 6 |
| 2024-09-07 | [Untie the Knots: An Efficient Data Augmentation Strategy for Long-Context Pre-Training in Language Models](https://arxiv.org/abs/2409.04774v1) | 2409.04774v1 | 7 |
| 2024-08-30 | [MemLong: Memory-Augmented Retrieval for Long Text Modeling](https://arxiv.org/abs/2408.16967v1) | 2408.16967v1 | 6 |
| 2024-08-20 | [MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding](https://arxiv.org/abs/2408.11049v5) | 2408.11049v5 | 7 |
| 2024-08-19 | [LongVILA: Scaling Long-Context Visual Language Models for Long Videos](https://arxiv.org/abs/2408.10188v6) | 2408.10188v6 | 7 |
| 2024-08-18 | [ELASTIC: Efficient Linear Attention for Sequential Interest Compression](https://arxiv.org/abs/2408.09380v4) | 2408.09380v4 | 6 |
| 2024-08-11 | [Post-Training Sparse Attention with Double Sparsity](https://arxiv.org/abs/2408.07092v2) | 2408.07092v2 | 10 |
| 2024-08-10 | [Eigen Attention: Attention in Low-Rank Space for KV Cache Compression](https://arxiv.org/abs/2408.05646v2) | 2408.05646v2 | 7 |
| 2024-07-25 | [S2-Attention: Hardware-Aware Context Sharding Among Attention Heads](https://arxiv.org/abs/2407.17678v7) | 2407.17678v7 | 6 |
| 2024-07-24 | [Towards Robust Knowledge Tracing Models via k-Sparse Attention](https://arxiv.org/abs/2407.17097v1) | 2407.17097v1 | 6 |
| 2024-07-23 | [Evaluating Long Range Dependency Handling in Code Generation LLMs](https://arxiv.org/abs/2407.21049v2) | 2407.21049v2 | 6 |
| 2024-07-21 | [ReAttention: Training-Free Infinite Context with Finite Attention Scope](https://arxiv.org/abs/2407.15176v3) | 2407.15176v3 | 6 |
| 2024-07-18 | [Scaling Granite Code Models to 128K Context](https://arxiv.org/abs/2407.13739v1) | 2407.13739v1 | 6 |
| 2024-07-16 | [GoldFinch: High Performance RWKV/Transformer Hybrid with Linear Pre-Fill and Extreme KV-Cache Compression](https://arxiv.org/abs/2407.12077v1) | 2407.12077v1 | 6 |
| 2024-07-11 | [Model Tells You Where to Merge: Adaptive KV Cache Merging for LLMs on Long-Context Tasks](https://arxiv.org/abs/2407.08454v2) | 2407.08454v2 | 6 |
| 2024-07-06 | [Linear Attention Based Deep Nonlocal Means Filtering for Multiplicative Noise Removal](https://arxiv.org/abs/2407.05087v2) | 2407.05087v2 | 6 |
| 2024-07-03 | [M5: A Whole Genome Bacterial Encoder at Single Nucleotide Resolution](https://arxiv.org/abs/2407.03392v1) | 2407.03392v1 | 6 |
| 2024-07-02 | [MInference 1.0: Accelerating Pre-filling for Long-Context LLMs via Dynamic Sparse Attention](https://arxiv.org/abs/2407.02490v2) | 2407.02490v2 | 9 |
| 2024-07-02 | [Efficient Sparse Attention needs Adaptive Token Release](https://arxiv.org/abs/2407.02328v1) | 2407.02328v1 | 6 |
| 2024-07-01 | [KV Cache Compression, But What Must We Give in Return? A Comprehensive Benchmark of Long Context Capable Approaches](https://arxiv.org/abs/2407.01527v2) | 2407.01527v2 | 6 |
| 2024-06-29 | [Is It Really Long Context if All You Need Is Retrieval? Towards Genuinely Difficult Long Context NLP](https://arxiv.org/abs/2407.00402v4) | 2407.00402v4 | 7 |
| 2024-06-26 | [AI-native Memory: A Pathway from LLMs Towards AGI](https://arxiv.org/abs/2406.18312v4) | 2406.18312v4 | 6 |
| 2024-06-26 | [UIO-LLMs: Unbiased Incremental Optimization for Long-Context LLMs](https://arxiv.org/abs/2406.18173v3) | 2406.18173v3 | 7 |
| 2024-06-26 | [LOOK-M: Look-Once Optimization in KV Cache for Efficient Multimodal Long-Context Inference](https://arxiv.org/abs/2406.18139v1) | 2406.18139v1 | 8 |
| 2024-06-24 | [Losing Visual Needles in Image Haystacks: Vision Language Models are Easily Distracted in Short and Long Contexts](https://arxiv.org/abs/2406.16851v3) | 2406.16851v3 | 7 |
| 2024-06-24 | [Sparser is Faster and Less is More: Efficient Sparse Attention for Long-Range Transformers](https://arxiv.org/abs/2406.16747v1) | 2406.16747v1 | 6 |
| 2024-06-21 | [MedOdyssey: A Medical Domain Benchmark for Long Context Evaluation Up to 200K Tokens](https://arxiv.org/abs/2406.15019v1) | 2406.15019v1 | 7 |
| 2024-06-20 | [GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of Large Language Models](https://arxiv.org/abs/2406.14550v2) | 2406.14550v2 | 7 |
| 2024-06-17 | [SampleAttention: Near-Lossless Acceleration of Long Context LLM Inference with Adaptive Structured Sparse Attention](https://arxiv.org/abs/2406.15486v3) | 2406.15486v3 | 9 |
| 2024-06-17 | [What Kinds of Tokens Benefit from Distant Text? An Analysis on Long Context Language Modeling](https://arxiv.org/abs/2406.11238v1) | 2406.11238v1 | 7 |
| 2024-06-14 | [A Training-free Sub-quadratic Cost Transformer Model Serving Framework With Hierarchically Pruned Attention](https://arxiv.org/abs/2406.09827v3) | 2406.09827v3 | 10 |
| 2024-06-13 | [Fusion of regional and sparse attention in Vision Transformers](https://arxiv.org/abs/2406.08859v1) | 2406.08859v1 | 6 |
| 2024-06-12 | [Short-Long Convolutions Help Hardware-Efficient Linear Attention to Focus on Long Sequences](https://arxiv.org/abs/2406.08128v3) | 2406.08128v3 | 6 |
| 2024-06-11 | [When Linear Attention Meets Autoregressive Decoding: Towards More Effective and Efficient Linearized Large Language Models](https://arxiv.org/abs/2406.07368v2) | 2406.07368v2 | 6 |
| 2024-06-11 | [An Efficient Recipe for Long Context Extension via Middle-Focused Positional Encoding](https://arxiv.org/abs/2406.07138v2) | 2406.07138v2 | 7 |
| 2024-06-09 | [SinkLoRA: Enhanced Efficiency and Chat Capabilities for Long-Context Large Language Models](https://arxiv.org/abs/2406.05678v1) | 2406.05678v1 | 9 |
| 2024-06-08 | [LoCoCo: Dropping In Convolutions for Long Context Compression](https://arxiv.org/abs/2406.05317v2) | 2406.05317v2 | 7 |
| 2024-06-04 | [Loki: Low-rank Keys for Efficient Sparse Attention](https://arxiv.org/abs/2406.02542v2) | 2406.02542v2 | 6 |
| 2024-06-04 | [PyramidKV: Dynamic KV Cache Compression based on Pyramidal Information Funneling](https://arxiv.org/abs/2406.02069v4) | 2406.02069v4 | 7 |
| 2024-06-03 | [LSKSANet: A Novel Architecture for Remote Sensing Image Semantic Segmentation Leveraging Large Selective Kernel and Sparse Attention Mechanism](https://arxiv.org/abs/2406.01228v1) | 2406.01228v1 | 6 |
| 2024-05-30 | [Quest: Query-centric Data Synthesis Approach for Long-context Scaling of Large Language Model](https://arxiv.org/abs/2405.19846v7) | 2405.19846v7 | 7 |
| 2024-05-28 | [DiG: Scalable and Efficient Diffusion Models with Gated Linear Attention](https://arxiv.org/abs/2405.18428v2) | 2405.18428v2 | 6 |
| 2024-05-28 | [ViG: Linear-complexity Visual Sequence Learning with Gated Linear Attention](https://arxiv.org/abs/2405.18425v2) | 2405.18425v2 | 6 |
| 2024-05-27 | [SWAT: Scalable and Efficient Window Attention-based Transformers Acceleration on FPGAs](https://arxiv.org/abs/2405.17025v1) | 2405.17025v1 | 8 |
| 2024-05-26 | [Demystify Mamba in Vision: A Linear Attention Perspective](https://arxiv.org/abs/2405.16605v2) | 2405.16605v2 | 6 |
| 2024-05-24 | [Understanding the differences in Foundation Models: Attention, State Space Models, and Recurrent Neural Networks](https://arxiv.org/abs/2405.15731v3) | 2405.15731v3 | 6 |
| 2024-05-23 | [Base of RoPE Bounds Context Length](https://arxiv.org/abs/2405.14591v1) | 2405.14591v1 | 7 |
| 2024-05-20 | [Asymptotic theory of in-context learning by linear attention](https://arxiv.org/abs/2405.11751v3) | 2405.11751v3 | 8 |
| 2024-05-19 | [SLAB: Efficient Transformers with Simplified Linear Attention and Progressive Re-parameterized Batch Normalization](https://arxiv.org/abs/2405.11582v2) | 2405.11582v2 | 6 |
| 2024-05-14 | [Challenges in Deploying Long-Context Transformers: A Theoretical Peak Performance Analysis](https://arxiv.org/abs/2405.08944v1) | 2405.08944v1 | 7 |
| 2024-04-24 | [Retrieval Head Mechanistically Explains Long-Context Factuality](https://arxiv.org/abs/2404.15574v1) | 2404.15574v1 | 9 |
| 2024-04-16 | [Sparse Attention Regression Network Based Soil Fertility Prediction With Ummaso](https://arxiv.org/abs/2404.10274v2) | 2404.10274v2 | 6 |
| 2024-04-12 | [Megalodon: Efficient LLM Pretraining and Inference with Unlimited Context Length](https://arxiv.org/abs/2404.08801v2) | 2404.08801v2 | 7 |
| 2024-04-11 | [LLoCO: Learning Long Contexts Offline](https://arxiv.org/abs/2404.07979v2) | 2404.07979v2 | 7 |
| 2024-04-10 | [Leave No Context Behind: Efficient Infinite Context Transformers with Infini-attention](https://arxiv.org/abs/2404.07143v2) | 2404.07143v2 | 6 |
| 2024-04-03 | [Linear Attention Sequence Parallelism](https://arxiv.org/abs/2404.02882v3) | 2404.02882v3 | 6 |
| 2024-04-03 | [How Sparse Attention Approximates Exact Attention? Your Attention is Naturally $n^C$-Sparse](https://arxiv.org/abs/2404.02690v2) | 2404.02690v2 | 10 |
| 2024-03-20 | [OrthCaps: An Orthogonal CapsNet with Sparse Attention Routing and Pruning](https://arxiv.org/abs/2403.13351v1) | 2403.13351v1 | 6 |
| 2024-02-28 | [Simple linear attention language models balance the recall-throughput tradeoff](https://arxiv.org/abs/2402.18668v2) | 2402.18668v2 | 10 |
| 2024-02-27 | [Training-Free Long-Context Scaling of Large Language Models](https://arxiv.org/abs/2402.17463v2) | 2402.17463v2 | 7 |
| 2024-02-20 | [RhythmFormer: Extracting Patterned rPPG Signals based on Periodic Sparse Attention](https://arxiv.org/abs/2402.12788v3) | 2402.12788v3 | 6 |
| 2024-02-15 | [Data Engineering for Scaling Language Models to 128K Context](https://arxiv.org/abs/2402.10171v1) | 2402.10171v1 | 6 |
| 2024-02-06 | [The Hedgehog & the Porcupine: Expressive Linear Attentions with Softmax Mimicry](https://arxiv.org/abs/2402.04347v1) | 2402.04347v1 | 6 |
| 2024-01-31 | [LOCOST: State-Space Models for Long Document Abstractive Summarization](https://arxiv.org/abs/2401.17919v3) | 2401.17919v3 | 6 |
| 2024-01-15 | [Flexibly Scaling Large Language Models Contexts Through Extensible Tokenization](https://arxiv.org/abs/2401.07793v1) | 2401.07793v1 | 6 |
| 2024-01-13 | [E^2-LLM: Efficient and Extreme Length Extension of Large Language Models](https://arxiv.org/abs/2401.06951v3) | 2401.06951v3 | 6 |
| 2024-01-07 | [Long Context Compression with Activation Beacon](https://arxiv.org/abs/2401.03462v3) | 2401.03462v3 | 7 |
| 2024-01-01 | [ScatterFormer: Efficient Voxel Transformer with Scattered Linear Attention](https://arxiv.org/abs/2401.00912v2) | 2401.00912v2 | 6 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-18 | [Linear Attention via Orthogonal Memory](https://arxiv.org/abs/2312.11135v1) | 2312.11135v1 | 8 |
| 2023-12-14 | [Agent Attention: On the Integration of Softmax and Linear Attention](https://arxiv.org/abs/2312.08874v3) | 2312.08874v3 | 6 |
| 2023-12-12 | [SCCA: Shifted Cross Chunk Attention for long contextual semantic expansion](https://arxiv.org/abs/2312.07305v1) | 2312.07305v1 | 7 |
| 2023-12-11 | [Gated Linear Attention Transformers with Hardware-Efficient Training](https://arxiv.org/abs/2312.06635v6) | 2312.06635v6 | 6 |
| 2023-11-11 | [Sparse Attention-Based Neural Networks for Code Classification](https://arxiv.org/abs/2311.06575v1) | 2311.06575v1 | 6 |
| 2023-11-08 | [LooGLE: Can Long-Context Language Models Understand Long Contexts?](https://arxiv.org/abs/2311.04939v2) | 2311.04939v2 | 8 |
| 2023-10-18 | [Why Softmax Attention Outperforms Linear Attention](https://arxiv.org/abs/2310.11685v2) | 2310.11685v2 | 6 |
| 2023-10-12 | [How Many Pretraining Tasks Are Needed for In-Context Learning of Linear Regression?](https://arxiv.org/abs/2310.08391v2) | 2310.08391v2 | 6 |
| 2023-10-11 | [SparseCoder: Advancing Source Code Analysis with Sparse Attention and Learned Token Pruning](https://arxiv.org/abs/2310.07109v2) | 2310.07109v2 | 6 |
| 2023-10-09 | [HyperAttention: Long-context Attention in Near-Linear Time](https://arxiv.org/abs/2310.05869v3) | 2310.05869v3 | 7 |
| 2023-10-03 | [SEA: Sparse Linear Attention with Estimated Attention Mask](https://arxiv.org/abs/2310.01777v2) | 2310.01777v2 | 10 |
| 2023-09-21 | [LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models](https://arxiv.org/abs/2309.12307v3) | 2309.12307v3 | 11 |
| 2023-08-21 | [Giraffe: Adventures in Expanding Context Lengths in LLMs](https://arxiv.org/abs/2308.10882v1) | 2308.10882v1 | 7 |
| 2023-08-01 | [FLatten Transformer: Vision Transformer using Focused Linear Attention](https://arxiv.org/abs/2308.00442v2) | 2308.00442v2 | 6 |
| 2023-07-01 | [MobileViG: Graph-Based Sparse Attention for Mobile Vision Applications](https://arxiv.org/abs/2307.00395v1) | 2307.00395v1 | 6 |
| 2023-06-01 | [Faster Causal Attention Over Large Sequences Through Sparse Flash Attention](https://arxiv.org/abs/2306.01160v1) | 2306.01160v1 | 10 |
| 2023-02-28 | [Sampled Transformer for Point Sets](https://arxiv.org/abs/2302.14346v1) | 2302.14346v1 | 8 |

### 2022
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2022-12-15 | [DETR4D: Direct Multi-View 3D Object Detection with Sparse Attention](https://arxiv.org/abs/2212.07849v1) | 2212.07849v1 | 6 |
| 2022-12-12 | [Mortality Prediction Models with Clinical Notes Using Sparse Attention at the Word and Sentence Levels](https://arxiv.org/abs/2212.06267v1) | 2212.06267v1 | 6 |
| 2022-10-16 | [Modeling Context With Linear Attention for Scalable Document-Level Translation](https://arxiv.org/abs/2210.08431v1) | 2210.08431v1 | 6 |
| 2022-10-14 | [Hybrid Reinforced Medical Report Generation with M-Linear Attention and Repetition Penalty](https://arxiv.org/abs/2210.13729v1) | 2210.13729v1 | 6 |
| 2022-10-13 | [CPSAA: Accelerating Sparse Attention using Crossbar-based Processing-In-Memory Architecture](https://arxiv.org/abs/2210.06696v2) | 2210.06696v2 | 6 |
| 2022-10-09 | [Linear attention coupled Fourier neural operator for simulation of three-dimensional turbulence](https://arxiv.org/abs/2210.04259v2) | 2210.04259v2 | 6 |
| 2022-08-09 | [Multiple Instance Neural Networks Based on Sparse Attention for Cancer Detection using T-cell Receptor Sequences](https://arxiv.org/abs/2208.04524v1) | 2208.04524v1 | 6 |
| 2022-08-07 | [A Length Adaptive Algorithm-Hardware Co-design of Transformer on FPGA Through Sparse Attention and Dynamic Pipelining](https://arxiv.org/abs/2208.03646v2) | 2208.03646v2 | 6 |
| 2022-06-29 | [SALO: An Efficient Spatial Accelerator Enabling Hybrid Sparse Attention Mechanisms for Long Sequences](https://arxiv.org/abs/2206.14550v1) | 2206.14550v1 | 6 |
| 2022-05-29 | [EfficientViT: Multi-Scale Linear Attention for High-Resolution Dense Prediction](https://arxiv.org/abs/2205.14756v6) | 2205.14756v6 | 6 |
| 2022-05-27 | [Understanding Long Programming Languages with Structure-Aware Sparse Attention](https://arxiv.org/abs/2205.13730v1) | 2205.13730v1 | 6 |
| 2022-04-16 | [Efficient Linear Attention for Fast and Accurate Keypoint Matching](https://arxiv.org/abs/2204.07731v3) | 2204.07731v3 | 6 |
| 2022-03-29 | [Locality Matters: A Locality-Biased Linear Attention for Automatic Speech Recognition](https://arxiv.org/abs/2203.15609v1) | 2203.15609v1 | 6 |

### 2021
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2021-12-04 | [STJLA: A Multi-Context Aware Spatio-Temporal Joint Linear Attention Network for Traffic Forecasting](https://arxiv.org/abs/2112.02262v1) | 2112.02262v1 | 6 |
| 2021-11-25 | [SwinBERT: End-to-End Transformers with Sparse Attention for Video Captioning](https://arxiv.org/abs/2111.13196v4) | 2111.13196v4 | 6 |
| 2021-10-21 | [Transformer Acceleration with Dynamic Sparse Attention](https://arxiv.org/abs/2110.11299v1) | 2110.11299v1 | 6 |
| 2021-10-18 | [Energon: Towards Efficient Acceleration of Transformers Using Dynamic Sparse Attention](https://arxiv.org/abs/2110.09310v2) | 2110.09310v2 | 6 |
| 2021-10-12 | [HETFORMER: Heterogeneous Transformer with Sparse Attention for Long-Text Extractive Summarization](https://arxiv.org/abs/2110.06388v2) | 2110.06388v2 | 6 |
| 2021-08-20 | [Smart Bird: Learnable Sparse Attention for Efficient and Effective Transformer](https://arxiv.org/abs/2108.09193v3) | 2108.09193v3 | 6 |
| 2021-07-19 | [Long-term series forecasting with Query Selector -- efficient model of sparse attention](https://arxiv.org/abs/2107.08687v2) | 2107.08687v2 | 6 |
| 2021-07-15 | [STAR: Sparse Transformer-based Action Recognition](https://arxiv.org/abs/2107.07089v1) | 2107.07089v1 | 8 |
| 2021-06-17 | [Efficient Conformer with Prob-Sparse Attention Mechanism for End-to-EndSpeech Recognition](https://arxiv.org/abs/2106.09236v1) | 2106.09236v1 | 6 |
| 2021-06-03 | [Luna: Linear Unified Nested Attention](https://arxiv.org/abs/2106.01540v2) | 2106.01540v2 | 6 |
| 2021-06-02 | [Is Sparse Attention more Interpretable?](https://arxiv.org/abs/2106.01087v2) | 2106.01087v2 | 6 |
| 2021-04-14 | [Sparse Attention with Linear Units](https://arxiv.org/abs/2104.07012v2) | 2104.07012v2 | 10 |
| 2021-04-14 | [Efficient conformer-based speech recognition with linear attention](https://arxiv.org/abs/2104.06865v2) | 2104.06865v2 | 6 |
| 2021-02-14 | [Sparse Attention Guided Dynamic Value Estimation for Single-Task Multi-Scene Reinforcement Learning](https://arxiv.org/abs/2102.07266v1) | 2102.07266v1 | 6 |

### 2020
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2020-12-31 | [ERNIE-Doc: A Retrospective Long-Document Modeling Transformer](https://arxiv.org/abs/2012.15688v2) | 2012.15688v2 | 6 |
| 2020-12-20 | [Multi-Head Linear Attention Generative Adversarial Network for Thin Cloud Removal](https://arxiv.org/abs/2012.10898v1) | 2012.10898v1 | 6 |
| 2020-12-14 | [Semantic Layout Manipulation with High-Resolution Sparse Attention](https://arxiv.org/abs/2012.07288v4) | 2012.07288v4 | 6 |
| 2020-11-16 | [Reinforced Medical Report Generation with X-Linear Attention and Repetition Penalty](https://arxiv.org/abs/2011.07680v1) | 2011.07680v1 | 6 |
| 2020-10-23 | [SAHDL: Sparse Attention Hypergraph Regularized Dictionary Learning](https://arxiv.org/abs/2010.12416v1) | 2010.12416v1 | 6 |
| 2020-07-29 | [Linear Attention Mechanism: An Efficient Attention for Semantic Segmentation](https://arxiv.org/abs/2007.14902v3) | 2007.14902v3 | 6 |
| 2020-03-31 | [X-Linear Attention Networks for Image Captioning](https://arxiv.org/abs/2003.14080v1) | 2003.14080v1 | 6 |
| 2020-03-12 | [Efficient Content-Based Sparse Attention with Routing Transformers](https://arxiv.org/abs/2003.05997v5) | 2003.05997v5 | 6 |
| 2020-02-29 | [Deep differentiable forest with sparse attention for the tabular data](https://arxiv.org/abs/2003.00223v1) | 2003.00223v1 | 6 |

### 2018
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2018-08-16 | [LARNN: Linear Attention Recurrent Neural Network](https://arxiv.org/abs/1808.05578v1) | 1808.05578v1 | 6 |
| 2018-03-15 | [Aggregated Sparse Attention for Steering Angle Prediction](https://arxiv.org/abs/1803.05785v1) | 1803.05785v1 | 6 |

### 2017
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2017-09-28 | [Jointly Trained Sequential Labeling and Classification by Sparse Attention Neural Networks](https://arxiv.org/abs/1709.10191v1) | 1709.10191v1 | 6 |

### 2016
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2016-09-19 | [A Cheap Linear Attention Mechanism with Fast Lookups and Fixed-Size Representations](https://arxiv.org/abs/1609.05866v1) | 1609.05866v1 | 6 |

<!-- table:end papers -->
