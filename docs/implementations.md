# 🛠️ 实现、Kernel 与教学（Implementations，横切赛道）

> 从一行公式到一颗 kernel：所有设计最终都要落地成代码。

读十篇论文不如写一遍注意力。这条横切赛道收录学习底层架构的最佳代码入口：
最小可读实现、逐行注解、高性能 kernel、以及模块化实验框架。
顺序建议：Annotated Transformer → nanoGPT → x-transformers → FlashAttention 源码。

## 必读路径

| 资源 | 类型 | 一句话 |
| :-- | :-- | :-- |
| [The Annotated Transformer](https://nlp.seas.harvard.edu/annotated-transformer/) | 教程 | Harvard NLP 逐行注解原始 Transformer |
| [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) | 博客 | 最经典的图解，入门第一页 |
| [nanoGPT](https://github.com/karpathy/nanoGPT) | 代码 | 约 300 行训练 + 模型的 GPT 最小复现 |
| [llm.c](https://github.com/karpathy/llm.c) | 代码 | 纯 C/CUDA 复现 GPT-2 训练，理解底层没有框架挡着 |
| [llama2.c](https://github.com/karpathy/llama2.c) | 代码 | 一个 C 文件跑 Llama 2 推理 |

## 模块与算子库

- [huggingface/transformers](https://github.com/huggingface/transformers) — 所有架构变体的工业标准实现库。
- [lucidrains/x-transformers](https://github.com/lucidrains/x-transformers) — 实验性注意力/模块的一站式试验田。
- [Dao-AILab/flash-attention](https://github.com/Dao-AILab/flash-attention) — FlashAttention 官方 kernel。
- [facebookresearch/xformers](https://github.com/facebookresearch/xformers) — 内存高效注意力构建块。
- [fla-org/flash-linear-attention](https://github.com/fla-org/flash-linear-attention) — 线性注意力 Triton kernel 库。
- [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) — 纯 C/C++ 推理，看 KV cache 与量化如何落地。

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-09-29 | [Parameterized Stripe Attention for Efficient Video Generation](https://arxiv.org/abs/2609.37001v1) | 2609.37001v1 | 0 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-08-02 | [C3D-AD: Toward Continual 3D Anomaly Detection via Kernel Attention with Learnable Advisor](https://arxiv.org/abs/2508.01311v1) | 2508.01311v1 | 6 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-08-23 | [Reproduction of scan B-statistic for kernel change-point detection algorithm](https://arxiv.org/abs/2408.13146v1) | 2408.13146v1 | 6 |

<!-- table:end papers -->
