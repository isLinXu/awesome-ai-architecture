# 🧩 分词与输入侧（Tokenization & Input）

> 模型看到世界的第一道工序——也是最经常被当作"已解决的问题"而忽视的模块。

tokenizer 决定了词表大小、序列长度、多语言公平性，甚至模型能不能做算术。
这条赛道收录子词分词的经典算法（BPE/SentencePiece）与"去分词化"路线：
字符级、字节级、动态 patch——输入侧的革命一直在暗流涌动。

## 奠基与必读

| 论文 | arXiv | 年份 | 一句话贡献 |
| :-- | :-- | --: | :-- |
| Neural Machine Translation of Rare Words with Subword Units (BPE) | [1508.07909](https://arxiv.org/abs/1508.07909) | 2015 | 子词 BPE 进入 NMT，现代 tokenizer 的起点 |
| SentencePiece | [1808.06226](https://arxiv.org/abs/1808.06226) | 2018 | 语言无关的 subword 工具，Llama/Qwen 词表事实标准 |
| CANINE: Pre-training an Efficient Tokenization-Free Encoder | [2103.06874](https://arxiv.org/abs/2103.06874) | 2021 | 免分词编码器：直接在字符序列上预训练 |
| ByT5: Towards a token-free future with pre-trained byte-to-byte models | [2105.13626](https://arxiv.org/abs/2105.13626) | 2021 | 字节到字节，彻底摆脱词表 |
| Charformer: Fast Character Transformers via Gradient-based Subword Tokenization | [2106.12672](https://arxiv.org/abs/2106.12672) | 2021 | GBST：可学习的梯度子词切分 |
| MEGABYTE: Predicting Million-byte Sequences with Multiscale Transformers | [2305.07185](https://arxiv.org/abs/2305.07185) | 2023 | 多尺度 patch 让字节级序列可达百万长度 |
| MambaByte: Token-free Selective State Space Model | [2401.13660](https://arxiv.org/abs/2401.13660) | 2024 | 免分词与 SSM 的天然合拍 |
| Byte Latent Transformer: Patches Scale Better Than Tokens | [2412.09871](https://arxiv.org/abs/2412.09871) | 2024 | BLT：动态熵 patch，字节级首次追平 token 级 |

## 最新论文

<!-- table:start papers -->
### 2026
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2026-11-12 | [Optimal Single-History Tokenization Disambiguation for Provably Secure Linguistic Steganography](https://arxiv.org/abs/2611.17091v1) | 2611.17091v1 | 8 |
| 2026-11-12 | [EvenVLM: A Text and Multimodal Dataset for the Even Language with Vision-Language Fine-Tuning](https://arxiv.org/abs/2611.16500v1) | 2611.16500v1 | 12 |
| 2026-11-11 | [Vocabulary-Free Next-Event Prediction on Temporal Graphs](https://arxiv.org/abs/2611.16063v1) | 2611.16063v1 | 7 |
| 2026-11-11 | [ActionCodec2: A Streaming Action Tokenizer](https://arxiv.org/abs/2611.15490v1) | 2611.15490v1 | 8 |
| 2026-11-11 | [MIGRO: A Decoupled and Portable Long-Term Memory System for Language Models](https://arxiv.org/abs/2611.15315v1) | 2611.15315v1 | 6 |
| 2026-11-11 | [Tokenization: Hardness and Bicriteria Approximation Algorithms](https://arxiv.org/abs/2611.15074v1) | 2611.15074v1 | 8 |
| 2026-11-11 | [Speech Tokenizers are Vulnerable: Transferable Semantic Attack and Robust Tokenizer](https://arxiv.org/abs/2611.14929v1) | 2611.14929v1 | 6 |
| 2026-11-10 | [ScaleBrain: A Scale-Consistent Framework for EEG Foundation Models](https://arxiv.org/abs/2611.14035v1) | 2611.14035v1 | 7 |
| 2026-11-10 | [Post-OCR Correction of Mixed-Script Uzbek Text: Byte-Level ByT5 with an Empirical Homoglyph Noise Matrix](https://arxiv.org/abs/2611.13609v1) | 2611.13609v1 | 6 |
| 2026-11-10 | [One Byte, One Token: Byteifying a 27B Hybrid-Attention LLM with Self-Generated Data](https://arxiv.org/abs/2611.13607v1) | 2611.13607v1 | 16 |
| 2026-11-10 | [Inherited Weights: Measuring the Tokenization Premium and the Sovereignty Cost of Language Models for the Global South](https://arxiv.org/abs/2611.13441v1) | 2611.13441v1 | 12 |
| 2026-11-10 | [What Do Tokenizer Comparisons Measure? Disentangling Granularity, Root Assignment, and Word-Level Readout across Amharic and Hausa](https://arxiv.org/abs/2611.14818v1) | 2611.14818v1 | 8 |
| 2026-11-10 | [One Byte, One Token: Byteifying a 27B Hybrid-Attention LLM with Self-Generated Data](https://arxiv.org/abs/2611.13607v2) | 2611.13607v2 | 16 |
| 2026-11-09 | [Adapting Small Language Models to Romanized Nepali: Tokenizer Fertility, Reference Likelihood, and Generation Metrics](https://arxiv.org/abs/2611.12628v1) | 2611.12628v1 | 6 |
| 2026-11-09 | [Phrase-Level Speculative Decoding on a Frozen Target](https://arxiv.org/abs/2611.12464v1) | 2611.12464v1 | 8 |
| 2026-11-09 | [dNaViT: Discrete Codes are General-Purpose Visual Representations](https://arxiv.org/abs/2611.12426v1) | 2611.12426v1 | 6 |
| 2026-11-09 | [The Left Ripple of Byte-Pair Encoding: Certified Lookbehind for Every Dictionary](https://arxiv.org/abs/2611.13061v1) | 2611.13061v1 | 8 |
| 2026-11-09 | [A Multi-Word Tokenizer for 204 Languages That Needs Fewer Tokens Than GPT-4o's, Including on English](https://arxiv.org/abs/2611.13059v1) | 2611.13059v1 | 18 |
| 2026-11-09 | [The Indic Token Tax in 2026: Measuring Tokenizer. Disparity and Its Cost for the Languages of India](https://arxiv.org/abs/2611.13058v1) | 2611.13058v1 | 6 |
| 2026-11-08 | [Brain-Aligned Latent Actions: Imposing Premotor Cortex Geometry on a Robot's Action Vocabulary](https://arxiv.org/abs/2611.11674v1) | 2611.11674v1 | 7 |
| 2026-11-08 | [Does Pose Encoding Matter? Analyzing Geometric Representations for Discrete Motion Vocabulary Learning](https://arxiv.org/abs/2611.11093v1) | 2611.11093v1 | 12 |
| 2026-11-08 | [A Hierarchical Tokenization Framework for Voxel-Level fMRI Representation Learning](https://arxiv.org/abs/2611.11081v1) | 2611.11081v1 | 10 |
| 2026-11-08 | [Differentiable Virtual-Slot Partitioning for Adaptive Tokenization in Vision Transformers](https://arxiv.org/abs/2611.11058v1) | 2611.11058v1 | 6 |
| 2026-11-08 | [MoTo: Mixture of Tokenizers Towards Fair Multilingual Language Modeling](https://arxiv.org/abs/2611.11027v1) | 2611.11027v1 | 18 |
| 2026-11-06 | [PhysioWave-T: Token-Efficient Wavelet Foundation Models for Biosignals](https://arxiv.org/abs/2611.08969v1) | 2611.08969v1 | 7 |
| 2026-11-06 | [Compact Greek Language Models from Scratch: Pretraining 500M- and 1B-Parameter Decoder-Only Transformers](https://arxiv.org/abs/2611.10209v1) | 2611.10209v1 | 10 |
| 2026-11-06 | [Improving the Diffusability of Motion Tokenizer](https://arxiv.org/abs/2611.10160v1) | 2611.10160v1 | 6 |
| 2026-11-05 | [Towards Practical 20 kbps Generative Video Compression via Adaptive Tokenization and Entropy Modeling](https://arxiv.org/abs/2611.08099v1) | 2611.08099v1 | 10 |
| 2026-11-05 | [OptST: Optimizing Semantic Tokenization for LLM-Enhanced Recommendation](https://arxiv.org/abs/2611.07523v1) | 2611.07523v1 | 10 |
| 2026-11-05 | [FFMT: Frequency-Factorized Multi-Rate Tokenization for Music-to-Dance Generation](https://arxiv.org/abs/2611.07384v1) | 2611.07384v1 | 6 |
| 2026-11-05 | [GreedTok is a Constant-Factor Approximation for Partition-Cover Tokenization](https://arxiv.org/abs/2611.07346v1) | 2611.07346v1 | 12 |
| 2026-11-05 | [Scale as a Modality: Multi-Scale Pixel-Space Diffusion Transformers](https://arxiv.org/abs/2611.08802v1) | 2611.08802v1 | 6 |
| 2026-11-05 | [GreedTok Is a 0.3287-Approximation for Tokenization, Within 3% of the Best Possible Constant](https://arxiv.org/abs/2611.07346v2) | 2611.07346v2 | 12 |
| 2026-11-04 | [AssameseLM-E2B: An Open-Weight Assamese Language Model for Efficient Consumer-Grade Deployment](https://arxiv.org/abs/2611.06170v1) | 2611.06170v1 | 12 |
| 2026-11-03 | [Learning Hierarchical Patch Splitting Policies for Faster Vision Transformers](https://arxiv.org/abs/2611.05742v1) | 2611.05742v1 | 7 |
| 2026-11-03 | [SPADE: Spatiotemporal Preference Alignment and Diversity Enhancement for Local Search](https://arxiv.org/abs/2611.04662v1) | 2611.04662v1 | 12 |
| 2026-11-03 | [TEMPO: Time Series Understanding via Discrete Tokenization](https://arxiv.org/abs/2611.04482v1) | 2611.04482v1 | 15 |
| 2026-11-03 | [Tokenizer Myths and Where To Find Them](https://arxiv.org/abs/2611.04215v1) | 2611.04215v1 | 12 |
| 2026-11-02 | [Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models](https://arxiv.org/abs/2611.04028v1) | 2611.04028v1 | 6 |
| 2026-11-02 | [A Common Language for Dynamic Graphs: Interaction Tokenization Enables Foundation Models](https://arxiv.org/abs/2611.03246v1) | 2611.03246v1 | 10 |
| 2026-11-02 | [Utility-Aware Generative Recommendation: Utility-Enriched Semantic Codes and Utility-Guided Decoding](https://arxiv.org/abs/2611.02981v1) | 2611.02981v1 | 7 |
| 2026-11-02 | [PixelBench: Can LLMs Understand and Generate Images Pixel by Pixel?](https://arxiv.org/abs/2611.02540v1) | 2611.02540v1 | 6 |
| 2026-11-02 | [PixelBench: Can LLMs Understand and Generate Images Pixel by Pixel?](https://arxiv.org/abs/2611.02540v2) | 2611.02540v2 | 6 |
| 2026-10-31 | [A Token Is Not a Unit of Difficulty: Segmentation Controls Where Adaptive Computation Goes Inside a Word](https://arxiv.org/abs/2611.00983v1) | 2611.00983v1 | 6 |
| 2026-10-30 | [Evaluating SAM-based and Convolutional Architectures in Thin Retinal Vessel Segmentation: Model Capacity, Computational Cost and Foundation Pre-training](https://arxiv.org/abs/2611.00396v1) | 2611.00396v1 | 6 |
| 2026-10-30 | [MoETok: Sparse Expert Routing for 1D Visual Tokenizers](https://arxiv.org/abs/2610.41992v1) | 2610.41992v1 | 6 |
| 2026-10-30 | [ID2Pattern: Pretraining Generalizable Identity Behavior Patterns for Transaction Risk Foundation Models](https://arxiv.org/abs/2610.41988v1) | 2610.41988v1 | 6 |
| 2026-10-29 | [Read, Allocate, Route: Role-Coupled Tokenization for Pixel-Space Generative Transformers](https://arxiv.org/abs/2610.40647v1) | 2610.40647v1 | 8 |
| 2026-10-29 | [Tokenizer Tokens Tell Training Tales](https://arxiv.org/abs/2610.39919v1) | 2610.39919v1 | 10 |
| 2026-10-27 | [RankFormer: Rethinking Time Series Transformers through Representation Capacity Analysis and Progressive Decoding](https://arxiv.org/abs/2610.36703v1) | 2610.36703v1 | 7 |
| 2026-10-27 | [Whole-Body Humanoid Control via Stochastic Motion Tokenization](https://arxiv.org/abs/2610.36452v1) | 2610.36452v1 | 10 |
| 2026-10-27 | [No Tokenizer, Still a Gap: Cross-Lingual Fairness of Homoglyph and Invisible-Character Watermarking](https://arxiv.org/abs/2610.36432v1) | 2610.36432v1 | 6 |
| 2026-10-26 | [MedVTok: A General-Purpose Medical Visual Tokenizer](https://arxiv.org/abs/2610.35842v1) | 2610.35842v1 | 6 |
| 2026-10-26 | [DriveUniTok: A Unified Multimodal Tokenizer for Driving World-Action Models](https://arxiv.org/abs/2610.35044v1) | 2610.35044v1 | 6 |
| 2026-10-25 | [QECGBERT: A Scalable ECG Foundation Model Based on Self-Supervised Language Learning via VQ-VAE Waveform Tokenization](https://arxiv.org/abs/2610.33964v1) | 2610.33964v1 | 6 |
| 2026-10-24 | [TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens](https://arxiv.org/abs/2610.33857v2) | 2610.33857v2 | 12 |
| 2026-10-24 | [Patch-Derived or Register Tokens? Comparing Variable-Length Image Tokenizers](https://arxiv.org/abs/2610.33540v1) | 2610.33540v1 | 9 |
| 2026-10-24 | [A Comprehensive Framework for All Stages of Large-Model Training: From Data and Tokenization, through Pretraining, to Post-Training Alignment](https://arxiv.org/abs/2610.33451v1) | 2610.33451v1 | 10 |
| 2026-10-24 | [TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens](https://arxiv.org/abs/2610.33857v3) | 2610.33857v3 | 12 |
| 2026-10-24 | [TrackTok: Semantically Persistent Tokens for Latent Video Generation](https://arxiv.org/abs/2610.33857v4) | 2610.33857v4 | 10 |
| 2026-10-23 | [Adaptive Frequency Threshold Byte Pair Encoding for Mixed Natural Language and Structured Symbolic Corpora](https://arxiv.org/abs/2610.32921v1) | 2610.32921v1 | 12 |
| 2026-10-23 | [EMG Tokenization Preserves Movement Information at a Fraction of the Bitrate](https://arxiv.org/abs/2610.32674v1) | 2610.32674v1 | 10 |
| 2026-10-23 | [AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents](https://arxiv.org/abs/2610.32092v1) | 2610.32092v1 | 8 |
| 2026-10-23 | [NUViT: Vision Transformers for Fourier Space Data](https://arxiv.org/abs/2610.32041v1) | 2610.32041v1 | 6 |
| 2026-10-22 | [Multi-Token Prediction and Alternative Tokenization Improve Learning Latent Multi-Hop Graph Search at Scale](https://arxiv.org/abs/2610.31439v1) | 2610.31439v1 | 6 |
| 2026-10-22 | [Same Entity, Different Script: Diagnosing Cross-Script Entity Matching Failures in Language Models](https://arxiv.org/abs/2610.31407v1) | 2610.31407v1 | 6 |
| 2026-10-22 | [LAMB: A Modern Contextual Language Model for Latin](https://arxiv.org/abs/2610.31723v1) | 2610.31723v1 | 8 |
| 2026-10-22 | [Learning from Next-Frame Prediction: Towards Unified and Scalable Visual World Modeling](https://arxiv.org/abs/2610.30724v2) | 2610.30724v2 | 7 |
| 2026-10-21 | [Climbing the Ladder: Automating Data Pipelines and Reproducing Baselines in Low-Resource Settings](https://arxiv.org/abs/2610.30374v1) | 2610.30374v1 | 8 |
| 2026-10-21 | [GoiBERT: Compact Vietnamese Language Models via Two-Stage Knowledge Distillation](https://arxiv.org/abs/2610.30067v2) | 2610.30067v2 | 6 |
| 2026-10-21 | [RubatoCodec: Budgeted Adaptive Speech Tokenization with Streaming Decoding](https://arxiv.org/abs/2610.29434v1) | 2610.29434v1 | 6 |
| 2026-10-21 | [Rethinking One Gene, One Token: Transcriptome-Aware Tokenization for Single-Cell Foundation Models](https://arxiv.org/abs/2611.05410v1) | 2611.05410v1 | 13 |
| 2026-10-21 | [Progressive Learning from Content to Relevance to Personalization for CTR Prediction](https://arxiv.org/abs/2610.29138v1) | 2610.29138v1 | 9 |
| 2026-10-21 | [Character-Level Prosody Control for Mandarin Speech Synthesis:An Architecture-Preserving Approach](https://arxiv.org/abs/2610.29123v2) | 2610.29123v2 | 9 |
| 2026-10-21 | [Rethinking One Gene, One Token: Transcriptome-Aware Tokenization for Single-Cell Foundation Models](https://arxiv.org/abs/2611.05410v2) | 2611.05410v2 | 13 |
| 2026-10-20 | [Rethinking Time Series Tokenization from a Frequency Perspective](https://arxiv.org/abs/2610.28997v2) | 2610.28997v2 | 10 |
| 2026-10-20 | [CSD: Common-Support Distillation for Cross-Tokenizer Knowledge Transfer](https://arxiv.org/abs/2610.28895v1) | 2610.28895v1 | 8 |
| 2026-10-20 | [Turning TS2Vec into a Foundation Model for Time Series Classification](https://arxiv.org/abs/2610.28602v1) | 2610.28602v1 | 6 |
| 2026-10-19 | [Discrete Neural Interlingua for Ontology-Agnostic EHR Modeling](https://arxiv.org/abs/2610.27047v1) | 2610.27047v1 | 10 |
| 2026-10-19 | [Rethinking BPE: Merge Selection as Model Selection](https://arxiv.org/abs/2610.26225v1) | 2610.26225v1 | 17 |
| 2026-10-19 | [Token-Set Choice Confounds POPE: A Systematic Audit of Yes/No Extraction in VLM Hallucination Evaluation](https://arxiv.org/abs/2610.25964v3) | 2610.25964v3 | 6 |
| 2026-10-18 | [ViMoLa: Discrete Motion Tokens for Language-Guided Video Generation](https://arxiv.org/abs/2610.25595v1) | 2610.25595v1 | 6 |
| 2026-10-17 | [CARTA: Self-Supervised Reusable Transaction Embeddings via Heterogeneous Tokenization and Cross-Attention](https://arxiv.org/abs/2610.24920v1) | 2610.24920v1 | 7 |
| 2026-10-17 | [Efficiency Measured in English: Tokeniser Coverage Bounds Small Language Models on Indic Scripts](https://arxiv.org/abs/2610.24818v1) | 2610.24818v1 | 6 |
| 2026-10-16 | [Beyond Clean Accuracy: The Practical Challenges and Benefits of Pixel-Based Language Models](https://arxiv.org/abs/2610.24290v1) | 2610.24290v1 | 10 |
| 2026-10-16 | [Finitely Verifiable Segmentation: Decidability for Every Tokenizer with a Finite-State Verifier](https://arxiv.org/abs/2610.30168v2) | 2610.30168v2 | 6 |
| 2026-10-16 | [ADT: All-Atom Diffusion Tokenizer for 3D Molecular Structures](https://arxiv.org/abs/2610.23265v1) | 2610.23265v1 | 10 |
| 2026-10-16 | [Query-adaptive Recurrent Tokenization](https://arxiv.org/abs/2610.22957v2) | 2610.22957v2 | 10 |
| 2026-10-16 | [FederatedBytes: Tokenizer-Free, Byte-Level Small Language Models for Efficient Multimodal Federated Learning](https://arxiv.org/abs/2610.22906v1) | 2610.22906v1 | 12 |
| 2026-10-15 | [Thunder-DeID+: Boundary-Aware Korean De-identification from Court Judgments to Broader Sensitive Documents](https://arxiv.org/abs/2610.22733v1) | 2610.22733v1 | 8 |
| 2026-10-15 | [Thinking from Above: Efficient Spatial Reasoning with Bird's-Eye-View Visual Tokens](https://arxiv.org/abs/2610.22700v1) | 2610.22700v1 | 6 |
| 2026-10-15 | [Pearl-Chat: Engineering a native Luganda language model from first principles in JAX and Flax NNX](https://arxiv.org/abs/2610.22529v1) | 2610.22529v1 | 14 |
| 2026-10-15 | [Patch where the text is new: a compression view of where byte-level models should spend compute](https://arxiv.org/abs/2610.22100v1) | 2610.22100v1 | 13 |
| 2026-10-15 | [The Right Byte First: How UTF-16 Helps Multilingual Boundary Prediction](https://arxiv.org/abs/2610.22071v1) | 2610.22071v1 | 14 |
| 2026-10-15 | [FeaTok: Feature-Loss Tokenization for Image Generation](https://arxiv.org/abs/2610.22060v1) | 2610.22060v1 | 10 |
| 2026-10-15 | [No Single Tokenizer Feature Reliably Predicts Downstream Language Model Performance](https://arxiv.org/abs/2610.21679v2) | 2610.21679v2 | 10 |
| 2026-10-15 | [CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models](https://arxiv.org/abs/2610.21143v1) | 2610.21143v1 | 10 |
| 2026-10-14 | [Does Morphological Correctness Matter for Tokenization? A Scrambled Control Study in Tagalog](https://arxiv.org/abs/2610.20859v1) | 2610.20859v1 | 12 |
| 2026-10-14 | [Generative Representation Learning for Scalable Latent Tokenization](https://arxiv.org/abs/2610.20533v1) | 2610.20533v1 | 10 |
| 2026-10-14 | [NeuroDETR: Multiscale Discrete Spatiotemporal Tokenization for Asynchronous EEG Event Detection](https://arxiv.org/abs/2610.20349v1) | 2610.20349v1 | 6 |
| 2026-10-14 | [ActionOPD: Distilling Decisions, Not Tokens](https://arxiv.org/abs/2610.19820v1) | 2610.19820v1 | 8 |
| 2026-10-14 | [Delta Tokenizer: Reference-Identical Tokenization of Session Deltas and Segment-Parallelism for Long Prompts on Multicore CPUs](https://arxiv.org/abs/2610.19801v1) | 2610.19801v1 | 12 |
| 2026-10-14 | [Q-MAGIC: Quad-only Mesh Autoregressive Generation via Singularity-Aware Circular Relative Offset Tokenization](https://arxiv.org/abs/2610.19777v1) | 2610.19777v1 | 6 |
| 2026-10-14 | [ixi-sLM: On-Device sLM for AI Call Agent Service](https://arxiv.org/abs/2610.19382v1) | 2610.19382v1 | 7 |
| 2026-10-13 | [Online Tokenization with Optimal Delay in Linear Time](https://arxiv.org/abs/2610.19139v1) | 2610.19139v1 | 12 |
| 2026-10-13 | [Just Respect the Semantics: Image-Token Compression via Pre-LLM Semantic Variable-Resolution Tokenization and In-LLM Relevance Pruning](https://arxiv.org/abs/2610.18690v2) | 2610.18690v2 | 6 |
| 2026-10-13 | [ProTok: Unified Protein Tokenization via Modular Multi-Codebook Quantization](https://arxiv.org/abs/2610.18481v1) | 2610.18481v1 | 14 |
| 2026-10-12 | [WeGR: Towards Unified Generative Retrieval via Behavior-aware Tokenization and Preference Alignment](https://arxiv.org/abs/2610.16979v3) | 2610.16979v3 | 10 |
| 2026-10-12 | [Image Tokenizers Should Be Trained Between Images](https://arxiv.org/abs/2610.16759v2) | 2610.16759v2 | 6 |
| 2026-10-12 | [The Language of Looking: Motion Tokens Reveal Domain-Dependent Local Structure in Gaze Sequences](https://arxiv.org/abs/2610.16565v1) | 2610.16565v1 | 6 |
| 2026-10-12 | [FOAdapter: A Plug-and-Play Spatial Tokenizer for Low-Bitrate FOA Speech Coding](https://arxiv.org/abs/2610.16202v1) | 2610.16202v1 | 6 |
| 2026-10-11 | [Semantically Steerable Image Tokenization](https://arxiv.org/abs/2610.15515v1) | 2610.15515v1 | 10 |
| 2026-10-11 | [Riemannian Graph Tokenizer for Structural Knowledge Transfer](https://arxiv.org/abs/2610.15427v1) | 2610.15427v1 | 8 |
| 2026-10-11 | [In-Place Indic Tokenizer Expansion and Continual Pretraining of Nemotron-3-Nano-30B-A3B](https://arxiv.org/abs/2610.15373v1) | 2610.15373v1 | 8 |
| 2026-10-10 | [SemiCodec: Bridging Speech Tokenization and High-fidelity Reconstruction with Semi-discrete Representations](https://arxiv.org/abs/2610.14834v1) | 2610.14834v1 | 6 |
| 2026-10-10 | [One-Way Coupling via Patchwise Adaptive Normalization in Transformer Surrogates](https://arxiv.org/abs/2610.14687v1) | 2610.14687v1 | 8 |
| 2026-10-10 | [ByteMark: A Unified Byte-Level Watermark for Detection Across Language Models](https://arxiv.org/abs/2610.14427v1) | 2610.14427v1 | 11 |
| 2026-10-09 | [Tokenization-Invariant Watermarking: A Byte-Local Method for LLM Text](https://arxiv.org/abs/2610.14378v1) | 2610.14378v1 | 10 |
| 2026-10-09 | [ClothCode: Generative Modeling for Garment State Estimation and Dynamics Prediction](https://arxiv.org/abs/2610.14200v1) | 2610.14200v1 | 6 |
| 2026-10-09 | [Precision Tokenization for Multi-Modal Data in High Energy Physics](https://arxiv.org/abs/2610.13876v1) | 2610.13876v1 | 10 |
| 2026-10-09 | [Taking Tokenization off the Host for Agentic LLM Serving](https://arxiv.org/abs/2610.13325v1) | 2610.13325v1 | 12 |
| 2026-10-09 | [CAST: Credit Alignment for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/abs/2610.13257v1) | 2610.13257v1 | 10 |
| 2026-10-09 | [MixTok: Adaptive Visual Tokenization with Global 1D Tokens and Sparse 2D Refinement](https://arxiv.org/abs/2610.13181v1) | 2610.13181v1 | 10 |
| 2026-10-09 | [Neurograf v1: An End-to-End Romanian-First Language Model Family](https://arxiv.org/abs/2610.13134v1) | 2610.13134v1 | 15 |
| 2026-10-09 | [ReAT: Residual Action Tokenization for Autoregressive Robot Policies](https://arxiv.org/abs/2610.13093v2) | 2610.13093v2 | 10 |
| 2026-10-08 | [Trainable Quantum-Native Language Models: Dissipative Memory, Capacity Limits, and Hardware Validation](https://arxiv.org/abs/2610.12806v1) | 2610.12806v1 | 6 |
| 2026-10-08 | [Latent Core Tokenizer: Compress, but Meaningfully](https://arxiv.org/abs/2610.12376v2) | 2610.12376v2 | 14 |
| 2026-10-08 | [BudgetPix: Compute-Adaptive Tokenization for Pixel-Space Image Diffusion](https://arxiv.org/abs/2610.12307v1) | 2610.12307v1 | 8 |
| 2026-10-08 | [Language-Specific Effects of Tokenizer Choice in Multilingual Language Models](https://arxiv.org/abs/2610.12144v1) | 2610.12144v1 | 8 |
| 2026-10-08 | [Instruction-Conditioned Electromagnetic Spectrum Understanding via Budget-Adaptive Signal Tokenization](https://arxiv.org/abs/2610.12142v1) | 2610.12142v1 | 11 |
| 2026-10-08 | [AdaptTok-Indic: Script-Aware Adaptive Tokenization for Indic Languages](https://arxiv.org/abs/2610.33017v1) | 2610.33017v1 | 16 |
| 2026-10-08 | [Merge-Based Vocabulary Extension Stalls at the Pre-Tokenizer: An English-Preserving Repair for Nepali, Tested in Continued Pretraining](https://arxiv.org/abs/2610.33016v1) | 2610.33016v1 | 9 |
| 2026-10-08 | [Easy to anticipate, hard to compute: boundary dependence finds the computed outputs that entropy patching misses](https://arxiv.org/abs/2610.11790v1) | 2610.11790v1 | 11 |
| 2026-10-08 | [Phonologically Informed Tokenization for German Speech Recognition: A Cross-Domain Study](https://arxiv.org/abs/2610.11646v1) | 2610.11646v1 | 14 |
| 2026-10-07 | [QuadTok: Quadtree Visual Tokenizer for Autoregressive Image Generation](https://arxiv.org/abs/2610.10497v1) | 2610.10497v1 | 10 |
| 2026-10-07 | [Coverage-Aware Reasoning with Medical Tokens for Diagnosis Prediction](https://arxiv.org/abs/2610.10641v1) | 2610.10641v1 | 6 |
| 2026-10-06 | [CAP: Codebook-Aligned Prediction for Tokenized Robot Policies](https://arxiv.org/abs/2610.09178v1) | 2610.09178v1 | 8 |
| 2026-10-06 | [Beyond Reconstruction: What Matters in Action Tokenization for Robot Policies?](https://arxiv.org/abs/2610.09170v1) | 2610.09170v1 | 10 |
| 2026-10-06 | [PrimitiveCAD: An LLM-Based Point-to-CAD Reconstruction with Primitive-Aware Tokenization and Operation Alignment](https://arxiv.org/abs/2610.08698v1) | 2610.08698v1 | 6 |
| 2026-10-06 | [CNet: A Complex-Valued Deep Learning Framework with Wirtinger Autodifferentiation and FFT--Hadamard Convolution](https://arxiv.org/abs/2610.08592v3) | 2610.08592v3 | 7 |
| 2026-10-06 | [Rethinking Cross-Tokenizer On-Policy Distillation: From Alignment Coverage to Supervision Reliability](https://arxiv.org/abs/2610.08448v1) | 2610.08448v1 | 8 |
| 2026-10-05 | [SpecBraM: What Should an EEG Foundation Model Predict? Masked Band-Power Prediction versus Waveform Reconstruction](https://arxiv.org/abs/2610.07484v1) | 2610.07484v1 | 6 |
| 2026-10-05 | [Rethinking Semantic ID Construction for Generative Recommendation: SimHash with Parallel Decoding and Semantic Alignment](https://arxiv.org/abs/2610.07402v1) | 2610.07402v1 | 8 |
| 2026-10-05 | [TranScope: What the Software Hides About LLM Training Data, the Hardware Reveals at Scale, and Accelerators Magnify](https://arxiv.org/abs/2610.06848v1) | 2610.06848v1 | 6 |
| 2026-10-05 | [Trajectory-Guided Tokenization of Complex CSI for Wi-Fi Sensing](https://arxiv.org/abs/2610.06288v1) | 2610.06288v1 | 9 |
| 2026-10-05 | [MoCAR: Motion-code Coordinate-aware AutoRegression for Continuous Trajectory Forecasting](https://arxiv.org/abs/2610.06210v1) | 2610.06210v1 | 8 |
| 2026-10-05 | [Byte Language Models: Scaling, Emergent Abstractions, and Information Allocation](https://arxiv.org/abs/2610.05978v1) | 2610.05978v1 | 13 |
| 2026-10-05 | [Generate What You Can Trust: Content Credibility in Generative Recommenders](https://arxiv.org/abs/2610.05670v2) | 2610.05670v2 | 8 |
| 2026-10-04 | [More Than Words: Compositional Tokenization for Efficient Language Models](https://arxiv.org/abs/2610.05597v1) | 2610.05597v1 | 13 |
| 2026-10-04 | [Certified Splitting: Decidability and Anchor Supply for Maximal-Munch Tokenization](https://arxiv.org/abs/2610.08854v2) | 2610.08854v2 | 6 |
| 2026-10-04 | [LLBPE: Linked-List Based GPU-Parallel BPE Tokenizer](https://arxiv.org/abs/2610.04951v1) | 2610.04951v1 | 13 |
| 2026-10-03 | [Saying, Not Knowing: Aggressively GGUF-Quantized Small Language Models Still Write Rare Words They Can No Longer Define](https://arxiv.org/abs/2610.04403v1) | 2610.04403v1 | 6 |
| 2026-10-03 | [GlitchPatch: Repairing Glitch Tokens in Frozen Language Models via Local Retokenization](https://arxiv.org/abs/2610.04399v1) | 2610.04399v1 | 17 |
| 2026-10-03 | [QuanLing: Cross-Branch Validation of Language Distance Quantification on Western Romance](https://arxiv.org/abs/2610.08851v1) | 2610.08851v1 | 9 |
| 2026-10-02 | [Dynamic Quadtree Tokenization and Transformer for Adaptive Mesh PDE Forecasting](https://arxiv.org/abs/2610.04044v3) | 2610.04044v3 | 9 |
| 2026-10-02 | [Do Language Models Need a Trainable Input Embedding Table? Fixed Minimal Token Codes at 1.7B-Class Scale](https://arxiv.org/abs/2610.04002v1) | 2610.04002v1 | 7 |
| 2026-10-02 | [SyntaxBench: A Statistical Diagnostic Framework for Character-Level Reasoning in Large Language Models](https://arxiv.org/abs/2610.03329v1) | 2610.03329v1 | 7 |
| 2026-10-02 | [OncoNoteBERT: A Foundation Representation Model for Natural Language Processing of Real-World Outpatient Oncology Notes](https://arxiv.org/abs/2610.03829v1) | 2610.03829v1 | 8 |
| 2026-10-02 | [Neural Data Needs Semantic Tokenization: Behavioral Events as Boundaries of Session-Transferable Tokens](https://arxiv.org/abs/2610.03001v1) | 2610.03001v1 | 11 |
| 2026-10-01 | [Universal Byte-Level Encoding: UTF-8/UTF-16 Routing to Reduce Cross-Script Token-Budget Disparities](https://arxiv.org/abs/2610.01984v2) | 2610.01984v2 | 12 |
| 2026-10-01 | [Q-SPT: Learnable Query-Based Compression for Low-Frame-Rate Speech Tokenization](https://arxiv.org/abs/2610.01492v1) | 2610.01492v1 | 10 |
| 2026-10-01 | [Counting and Min-Cost Encoding for Tokenization in Large Language Models](https://arxiv.org/abs/2610.01127v1) | 2610.01127v1 | 14 |
| 2026-10-01 | [TOAST: Stochastic Robot Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2610.00899v1) | 2610.00899v1 | 6 |
| 2026-09-30 | [Component-Weighted Centroid Search for Exact Incremental BPE](https://arxiv.org/abs/2609.40016v2) | 2609.40016v2 | 11 |
| 2026-09-30 | [Generative End-to-end Ad Retrieval at Douyin](https://arxiv.org/abs/2609.39327v1) | 2609.39327v1 | 8 |
| 2026-09-30 | [The Invisible Language Tax: Token Premiums of French and Regional Languages in 2026 LLM Tokenizers, and a French-Optimized Prototype](https://arxiv.org/abs/2609.39001v1) | 2609.39001v1 | 14 |
| 2026-09-29 | [LEMON-ZEST: Evolution-Informed Tokenization for Efficient Protein Language Modeling](https://arxiv.org/abs/2609.37675v1) | 2609.37675v1 | 9 |
| 2026-09-29 | [GraphVQ: Structure-Aware Autoregressive Decoding over Context-Quantized Graph Tokens](https://arxiv.org/abs/2609.37604v1) | 2609.37604v1 | 6 |
| 2026-09-29 | [Geometry-Conditioned Fixed-Scaffold Encoders for Time-Warp Robust Sequence Retrieval](https://arxiv.org/abs/2609.36809v1) | 2609.36809v1 | 7 |
| 2026-09-29 | [NesTok: Nested Self-Aligned 1D Tokenizer for Autoregressive Image Generation](https://arxiv.org/abs/2609.36756v3) | 2609.36756v3 | 6 |
| 2026-09-28 | [Concept Direction Reliability Across Languages with Different Tokenizer Fertility](https://arxiv.org/abs/2609.36194v1) | 2609.36194v1 | 6 |
| 2026-09-28 | [Humanoid Loco-Manipulation With Discrete VLA Model](https://arxiv.org/abs/2609.35709v1) | 2609.35709v1 | 10 |
| 2026-09-28 | [Rethinking Causal Action Tokenization with Conditional Annealing in Flow Matching](https://arxiv.org/abs/2609.35469v1) | 2609.35469v1 | 10 |
| 2026-09-28 | [Semantic Prefix Oracles for LLM Decoding: Contracts and Differential Validation](https://arxiv.org/abs/2609.35425v1) | 2609.35425v1 | 8 |
| 2026-09-28 | [Same Bytes, Different Authority: Reserved-Token Representations in Chat-Template Prompt Injection](https://arxiv.org/abs/2609.35932v1) | 2609.35932v1 | 13 |
| 2026-09-28 | [Beyond Token Alignment: Event Completion for Cross-Tokenizer On-Policy Distillation](https://arxiv.org/abs/2609.34738v1) | 2609.34738v1 | 8 |
| 2026-09-28 | [Do Motion Tokenizers for Co-Speech Gesture Generation Encode Gesture Semantics?](https://arxiv.org/abs/2610.03765v1) | 2610.03765v1 | 7 |
| 2026-09-28 | [Quantitative Measurement of Language Distance among Closely Related Indo-European Languages Using Pretrained Language Models: A Case Study on the North Germanic Branch](https://arxiv.org/abs/2609.34152v1) | 2609.34152v1 | 8 |
| 2026-09-28 | [Who Gets a Token, and What Does It Carry? Unequal Name Support and Concept Access in Large Language Models](https://arxiv.org/abs/2609.34065v1) | 2609.34065v1 | 10 |
| 2026-09-27 | [High-Level Text Preprocessing for Semantic Similarity Analysis of Discursive Texts: A Framework and Empirical Demonstration](https://arxiv.org/abs/2609.33983v1) | 2609.33983v1 | 6 |
| 2026-09-27 | [Dual-Vocabulary Language Model for Cross-Tokenizer Distillation](https://arxiv.org/abs/2609.33816v1) | 2609.33816v1 | 13 |
| 2026-09-27 | [Preserving Morphemes: Morphology-Guided Pre-Tokenization for Nepali](https://arxiv.org/abs/2609.33395v1) | 2609.33395v1 | 18 |
| 2026-09-27 | [Flow-Matching-Based Protein Structure Tokenizer Made Efficient and Easy](https://arxiv.org/abs/2609.33129v1) | 2609.33129v1 | 10 |
| 2026-09-26 | [X-Tree: Tokenizing Reusable Experience for Efficient Agent Generalization](https://arxiv.org/abs/2609.32993v1) | 2609.32993v1 | 6 |
| 2026-09-26 | [Predicting the Financial Impact of Supply Chain Risk for Major AI-Related Semiconductor Firms: A Heterogeneous Graph Patch Transformer Approach](https://arxiv.org/abs/2609.32741v1) | 2609.32741v1 | 7 |
| 2026-09-26 | [MotionMaestro: Masked Tokenization for Unified Motion Generation](https://arxiv.org/abs/2609.37495v1) | 2609.37495v1 | 10 |
| 2026-09-26 | [Masking Frequent Tokens Sharpens Direct Preference Optimization](https://arxiv.org/abs/2609.32445v1) | 2609.32445v1 | 6 |
| 2026-09-26 | [Curv-Tail: Lightweight Long-Tailed Encrypted Traffic Classification with Discrete Packet-Length Encoding and Lorentz Prototypes](https://arxiv.org/abs/2609.32242v2) | 2609.32242v2 | 8 |
| 2026-09-26 | [A Priority-Aware Dual-Channel Feature Fusion Method for Urban Rail Service Traffic Classification](https://arxiv.org/abs/2609.32168v1) | 2609.32168v1 | 6 |
| 2026-09-25 | [TokenScanner: Detecting Backdoors and Discovering Triggers in Text-to-Image LoRAs via Full Vocabulary Scanning](https://arxiv.org/abs/2609.31878v1) | 2609.31878v1 | 7 |
| 2026-09-25 | [FragToken: Amplifying LLM Inference Costs through Noncanonical Token Generation](https://arxiv.org/abs/2609.31552v1) | 2609.31552v1 | 6 |
| 2026-09-25 | [Where a Model Sends Its Own Repeated Token](https://arxiv.org/abs/2609.31181v1) | 2609.31181v1 | 6 |
| 2026-09-25 | [Breaking the Black Box: Byte-Level Boundary Inference of Real-World Antivirus Systems](https://arxiv.org/abs/2609.31012v1) | 2609.31012v1 | 6 |
| 2026-09-25 | [Structure-Guided Masked Autoencoders for Ultra-High Resolution Scientific Image Understanding](https://arxiv.org/abs/2609.30682v1) | 2609.30682v1 | 8 |
| 2026-09-24 | [Atelier: Learning Local Self-Supervised Features for CryoEM Volumes via Hypernetworks](https://arxiv.org/abs/2609.30569v1) | 2609.30569v1 | 6 |
| 2026-09-24 | [A Hybrid CNN--State-Space--Attention Backbone with Joint-Embedding Predictive Pretraining for 12-Lead ECG Classification](https://arxiv.org/abs/2609.29376v1) | 2609.29376v1 | 7 |
| 2026-09-24 | [The Tokens Remember: When Tokenization Bypasses Knowledge Editing and Unlearning](https://arxiv.org/abs/2609.29045v1) | 2609.29045v1 | 6 |
| 2026-09-24 | [Direction-Scale Decomposition in Action Representation: Rethinking What to Tokenize for Vision-Language-Action Models](https://arxiv.org/abs/2609.28865v1) | 2609.28865v1 | 8 |
| 2026-09-23 | [Motif-Vocab: StatisticallyCalibrated Transcription-Factor-Identity Tokenization forGenomic Language Models](https://arxiv.org/abs/2609.28386v1) | 2609.28386v1 | 16 |
| 2026-09-23 | [UNITE-AUDIO: Joint Learning of Continuous Tokenization and Latent Flow Matching for Text-to-Audio Generation](https://arxiv.org/abs/2609.28206v2) | 2609.28206v2 | 10 |
| 2026-09-23 | [Behavior-Aligned Action Tokenization for Robot Policy Learning](https://arxiv.org/abs/2609.27513v1) | 2609.27513v1 | 10 |
| 2026-09-22 | [StableVQ: Practical Guidelines for Stable Vector-Quantized Tokenizer Training](https://arxiv.org/abs/2609.26774v1) | 2609.26774v1 | 6 |
| 2026-09-22 | [Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2609.25820v1) | 2609.25820v1 | 6 |
| 2026-09-21 | [What Makes a Good Medical Image Tokenizer? Rethinking Reconstruction and Generation in Medical Image Tokenization](https://arxiv.org/abs/2609.24691v1) | 2609.24691v1 | 12 |
| 2026-09-21 | [Direction-Aware Masked Pretraining on 3D Seismic Data with Transfer to Cross-Area Acoustic Impedance Inversion](https://arxiv.org/abs/2609.24615v2) | 2609.24615v2 | 6 |
| 2026-09-21 | [Brain-Token Learning: Microstate-Based Tokenization and Multi-Scale Interaction for Long-Horizon EEG Sequence Modeling](https://arxiv.org/abs/2609.24324v1) | 2609.24324v1 | 8 |
| 2026-09-20 | [A discrete generative model of neuronal spiking activity on microelectrode arrays](https://arxiv.org/abs/2609.23907v1) | 2609.23907v1 | 6 |
| 2026-09-20 | [Can't Find Waldo: Evaluating VLMs' Sensitivity to Image Resolution and Detail Level](https://arxiv.org/abs/2609.31706v1) | 2609.31706v1 | 6 |
| 2026-09-20 | [MDL-Calibrated Significance-Gain Pair Encoding: Replication-Aware Automatic Stopping for Subword Tokenization](https://arxiv.org/abs/2609.31705v1) | 2609.31705v1 | 20 |
| 2026-09-18 | [ufakzeka-1: Building and Evaluating a 151M-Parameter Turkish Language Model from Scratch](https://arxiv.org/abs/2609.25081v1) | 2609.25081v1 | 9 |
| 2026-09-18 | [Beyond Atomic Tokens: Factorizing Syllables for Language Model Pretraining](https://arxiv.org/abs/2609.21362v2) | 2609.21362v2 | 13 |
| 2026-09-18 | [Rethinking Music Tokenization: A Semantic Codec toward High-Fidelity LLM Music Generation](https://arxiv.org/abs/2609.21240v1) | 2609.21240v1 | 10 |
| 2026-09-16 | [ActionPiece: Rethinking Action Tokenization for Autoregressive Vision-Language-Action Models](https://arxiv.org/abs/2609.18487v1) | 2609.18487v1 | 10 |
| 2026-09-16 | [M2Tok: Multi-head Multi-codebook Discrete Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2609.18259v2) | 2609.18259v2 | 10 |
| 2026-09-16 | [A Lightweight CNN Integrated Compact Convolutional Transformer for Multi-Scale Feature Learning and reducing computational complexity for breast cancer mammography image detection and classification](https://arxiv.org/abs/2609.18212v1) | 2609.18212v1 | 11 |
| 2026-09-15 | [Right Tool, Right Job: Native-Language Evaluation, Tokenizer Sensitivity, and Methodological Findings from a French-Only BabyLM](https://arxiv.org/abs/2609.17435v1) | 2609.17435v1 | 7 |
| 2026-09-15 | [Nameless Tokenization: A Lossless Tokenizer-Level Defense Against Control-Token Forgery in Open-Weight LLMs](https://arxiv.org/abs/2609.16984v1) | 2609.16984v1 | 12 |
| 2026-09-14 | [A prelude to the theory of Real-World Asset (RWA) Tokenization](https://arxiv.org/abs/2609.15797v1) | 2609.15797v1 | 6 |
| 2026-09-14 | [To Each Language Its Tokenizer: Modular Tokenizers for Efficient Multilingual LLMs](https://arxiv.org/abs/2609.15528v1) | 2609.15528v1 | 11 |
| 2026-09-14 | [On the role of the tokenizer in ECG transformer models](https://arxiv.org/abs/2609.15433v1) | 2609.15433v1 | 12 |
| 2026-09-14 | [Parameter-Efficient Adaptation of Pretrained Language Models for Time-Series Forecasting](https://arxiv.org/abs/2609.15344v1) | 2609.15344v1 | 7 |
| 2026-09-14 | [MoVT: Video-Augmented Motion Tokenizer for Text-to-Motion Generation](https://arxiv.org/abs/2609.14965v1) | 2609.14965v1 | 6 |
| 2026-09-11 | [Fewer Words, Not Fewer Tokens: Measuring the Sanskrit Tokenization Penalty per Proposition](https://arxiv.org/abs/2609.12960v1) | 2609.12960v1 | 20 |
| 2026-09-11 | [VideoTok4D: A 4D-Aware Video Tokenizer for Compact World Representation](https://arxiv.org/abs/2609.12874v1) | 2609.12874v1 | 10 |
| 2026-09-11 | [TokenMapper: A Step Toward Interoperable Speech Token Translation](https://arxiv.org/abs/2609.12563v1) | 2609.12563v1 | 6 |
| 2026-09-11 | [Breaking the Token Ceiling: Distilling Smaller, Stronger Byte Models](https://arxiv.org/abs/2609.12303v1) | 2609.12303v1 | 6 |
| 2026-09-10 | [How Robust Are Neural Audio Codecs for African Speech? A Multi-Task Benchmark and the Limits of Perceptual Quality](https://arxiv.org/abs/2610.00154v1) | 2610.00154v1 | 8 |
| 2026-09-10 | [LoopVAE: Recurrent Depth Across Scales for Visual Tokenization](https://arxiv.org/abs/2609.11516v1) | 2609.11516v1 | 10 |
| 2026-09-09 | [StreamAlign: Streaming Text-Aligned Speech Tokenization](https://arxiv.org/abs/2609.09719v1) | 2609.09719v1 | 18 |
| 2026-09-09 | [BuzzASR: A Swarm of 100+ Monolingual Speech Recognition Models](https://arxiv.org/abs/2609.09554v2) | 2609.09554v2 | 6 |
| 2026-09-08 | [Studying Image Tokenizers as Visual Languages in Unified Multimodal Models](https://arxiv.org/abs/2609.09143v1) | 2609.09143v1 | 8 |
| 2026-09-08 | [TASTE2: Text-Aligned Speech Modeling and Deployment toward Full-Duplex Voice Interaction](https://arxiv.org/abs/2609.08956v1) | 2609.08956v1 | 11 |
| 2026-09-07 | [Unified Vision-Centric Pedestrian Crossing Action Prediction via Adaptive Patch Projection and Proactive Spatial Rectification](https://arxiv.org/abs/2609.07420v1) | 2609.07420v1 | 7 |
| 2026-09-07 | [Dynamic-Programming-Guided Hierarchical BPE and Empirical Analysis of Vocabulary Pruning](https://arxiv.org/abs/2609.06898v1) | 2609.06898v1 | 10 |
| 2026-09-06 | [A Grapheme-Aware Indic Tokenizer for Tamil: Large-Scale Training and Intrinsic Evaluation](https://arxiv.org/abs/2609.06690v1) | 2609.06690v1 | 14 |
| 2026-09-06 | [Detokenization Leaks: Reconstructing Local LLM Outputs From Cache Traces](https://arxiv.org/abs/2609.06674v1) | 2609.06674v1 | 10 |
| 2026-09-05 | [Branch-Centric Tokenization and Test-Time Augmentation for Skeleton Generation](https://arxiv.org/abs/2609.06218v2) | 2609.06218v2 | 6 |
| 2026-09-04 | [Technical Manual for a Toolkit for Measuring Contextual Individuation in Transformer Language Models](https://arxiv.org/abs/2609.05333v1) | 2609.05333v1 | 9 |
| 2026-09-04 | [MoirfEolas and CríochScore: Developing Resources for and the Evaluation of Tokenization Alignment with Irish Morphology](https://arxiv.org/abs/2609.05022v1) | 2609.05022v1 | 8 |
| 2026-09-02 | [Low-Latency Spell Correction for Japanese Music Search Queries](https://arxiv.org/abs/2609.04262v1) | 2609.04262v1 | 12 |
| 2026-09-01 | [ZipTok3D: High-Fidelity 3D Tokenization with Compact Token Prefixes](https://arxiv.org/abs/2609.01740v1) | 2609.01740v1 | 10 |
| 2026-09-01 | [When Tokenization is Secretly Output Supervision](https://arxiv.org/abs/2609.01386v1) | 2609.01386v1 | 11 |
| 2026-09-01 | [Advanced Pixel Diffusion Model with Guided Sparse Global Refinement](https://arxiv.org/abs/2609.00798v1) | 2609.00798v1 | 6 |
| 2026-09-01 | [BiMTokenizer: Preserving Semantic-Acoustic Balance in Low-Bitrate Speech Tokenization via Bidirectional State-Space Modeling](https://arxiv.org/abs/2609.00562v1) | 2609.00562v1 | 12 |
| 2026-08-31 | [Toppling the Hierarchy in Byte-level Language Modeling](https://arxiv.org/abs/2609.00463v1) | 2609.00463v1 | 8 |
| 2026-08-31 | [Location-Aware Language Models via Secondary Embeddings](https://arxiv.org/abs/2609.00454v1) | 2609.00454v1 | 6 |
| 2026-08-31 | [LightNav-0: Eliciting VLM Spatial Intelligence for Generalist Embodied Navigation](https://arxiv.org/abs/2608.30935v2) | 2608.30935v2 | 6 |
| 2026-08-31 | [Beat-Synchronous Tokenization for ECG Transformers](https://arxiv.org/abs/2608.30367v1) | 2608.30367v1 | 12 |
| 2026-08-31 | [Quantifying and Mitigating Korean Jamo-Level Typographical Vulnerabilities in Large Language Models](https://arxiv.org/abs/2608.30229v1) | 2608.30229v1 | 6 |
| 2026-08-31 | [Manacá-1B: An Open, Reproducible Brazilian-Portuguese Language Model and a Tokenizer-Aware, Paired Evaluation](https://arxiv.org/abs/2608.30114v1) | 2608.30114v1 | 6 |
| 2026-08-30 | [Arkios: An Open Bilingual English-Nepali Language Model Trained From Scratch, with a Devanagari-Aware Tokenizer](https://arxiv.org/abs/2608.30092v2) | 2608.30092v2 | 12 |
| 2026-08-30 | [Token Counts Are Not Model Lineage: A Frozen-Threshold Holdout Study of Black-Box LLM API Fingerprinting](https://arxiv.org/abs/2608.29930v1) | 2608.29930v1 | 8 |
| 2026-08-30 | [ACTD: Anchor-Based Cross-Tokenizer Distillation with Residual Regularization](https://arxiv.org/abs/2608.29662v1) | 2608.29662v1 | 8 |
| 2026-08-29 | [APPSolver: Adaptive Patch Partitioning for Point-Wise Ship Flow Prediction on Unstructured Meshes](https://arxiv.org/abs/2608.29355v1) | 2608.29355v1 | 7 |
| 2026-08-28 | [Nested Byte-Level Vocabularies Are Cheap to Deploy and Expensive to Share: A Pre-Registered Negative Result](https://arxiv.org/abs/2608.28151v1) | 2608.28151v1 | 15 |
| 2026-08-28 | [GAAT: Geometry-Aware Alignment Transformer for Multimodal UAV Perception](https://arxiv.org/abs/2608.27971v3) | 2608.27971v3 | 6 |
| 2026-08-28 | [Not to Break, but to Attest: Adversarial Probes for Privacy-Preserving LLM Verification](https://arxiv.org/abs/2608.27954v2) | 2608.27954v2 | 7 |
| 2026-08-27 | [When Tokenizers Fail: Byte-Level Chunking for Zero-Shot Transfer to Low-Resource Languages](https://arxiv.org/abs/2608.27658v1) | 2608.27658v1 | 21 |
| 2026-08-27 | [Variable-Granularity Tokenization for High-Resolution Object Detection](https://arxiv.org/abs/2608.28706v1) | 2608.28706v1 | 12 |
| 2026-08-27 | [Double Trouble: Bilingual Pretraining Leaves Language-Conditioned Effects in Shared-Language Representations](https://arxiv.org/abs/2608.26576v2) | 2608.26576v2 | 6 |
| 2026-08-26 | [Vowel Signs Are Not Letters: A Pre-tokenization Ceiling on Multilingual Tokenizer Fertility](https://arxiv.org/abs/2608.26449v1) | 2608.26449v1 | 20 |
| 2026-08-26 | [When Is Noise Response Universal? Tokenization as the Hidden Variable in Language Models](https://arxiv.org/abs/2608.26319v1) | 2608.26319v1 | 13 |
| 2026-08-26 | [What Does Chain-of-Thought Entropy Measure? A Channel Audit of Scaffolding, Routing, and Content](https://arxiv.org/abs/2609.25039v1) | 2609.25039v1 | 6 |
| 2026-08-26 | [GeoFormer: Geometry-Aware Transformer and its application to 5D First-Arrival Picking](https://arxiv.org/abs/2608.25668v1) | 2608.25668v1 | 6 |
| 2026-08-26 | [An Event is Worth One Token: Event Tokenization for Industrial-scale LLM Recommendation](https://arxiv.org/abs/2608.25546v3) | 2608.25546v3 | 10 |
| 2026-08-25 | [Apples to Apples? Towards Comparable Crosslingual Language Model Evaluation](https://arxiv.org/abs/2608.25089v2) | 2608.25089v2 | 10 |
| 2026-08-25 | [VIVAS: Vitalizing Visual Perception in VLM Pre-training via Vision-language Unified Autoregressive Supervision](https://arxiv.org/abs/2609.27948v1) | 2609.27948v1 | 6 |
| 2026-08-25 | [Keep-or-Drop? Adaptive Tokenizer for Compact Video Representation](https://arxiv.org/abs/2608.24293v2) | 2608.24293v2 | 10 |
| 2026-08-25 | [PRQ-KMeans: Projection Residual Quantization for Semantic ID Tokenization](https://arxiv.org/abs/2608.24207v2) | 2608.24207v2 | 10 |
| 2026-08-25 | [Tlow: Flow-based Item Tokenizer for Recommendation](https://arxiv.org/abs/2608.24176v1) | 2608.24176v1 | 11 |
| 2026-08-25 | [GaussVLA: Geometry-Aware Spatial Reasoning for Vision-Language-Action Model](https://arxiv.org/abs/2608.24959v1) | 2608.24959v1 | 6 |
| 2026-08-25 | [TAGR: Temporally Adaptive Generative Recommendation for Industrial Live-Streaming Advertising](https://arxiv.org/abs/2608.24034v2) | 2608.24034v2 | 6 |
| 2026-08-24 | [The Dialect Tax: Dialectal Biases Persist throughout the Language Modeling Pipeline](https://arxiv.org/abs/2608.24952v1) | 2608.24952v1 | 14 |
| 2026-08-24 | [AffineTok: Semantic Affine Consistency for Diffusion-Friendly Visual Tokenizer](https://arxiv.org/abs/2608.23864v1) | 2608.23864v1 | 6 |
| 2026-08-24 | [Motion-Based Tokenization for Cross-Dataset Egocentric Gaze Modeling](https://arxiv.org/abs/2608.22926v1) | 2608.22926v1 | 8 |
| 2026-08-24 | [HelaBERT: Enhancing Sinhala Language Understanding with Dual Pooling Classification Head](https://arxiv.org/abs/2608.22922v1) | 2608.22922v1 | 6 |
| 2026-08-24 | [Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms to Semantic Subwords](https://arxiv.org/abs/2608.22734v1) | 2608.22734v1 | 12 |
| 2026-08-22 | [Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Diversion](https://arxiv.org/abs/2608.22140v1) | 2608.22140v1 | 10 |
| 2026-08-21 | [Type-Driven Tokenization for Brahmic Scripts](https://arxiv.org/abs/2609.22125v1) | 2609.22125v1 | 12 |
| 2026-08-20 | [Listening Forward: Next Patch Embedding Prediction Enables Scalable Audio Learners](https://arxiv.org/abs/2608.19863v1) | 2608.19863v1 | 8 |
| 2026-08-19 | [Compress and Forget: bitsandbytes Quantization Amplifies Proactive Interference in LLMs](https://arxiv.org/abs/2608.18578v2) | 2608.18578v2 | 6 |
| 2026-08-18 | [TokEval: A Tokenizer Evaluation Suite](https://arxiv.org/abs/2608.18062v3) | 2608.18062v3 | 10 |
| 2026-08-18 | [How Far Should Tokenization Go? Predictive Effectiveness and Relational Losslessness](https://arxiv.org/abs/2608.18025v2) | 2608.18025v2 | 12 |
| 2026-08-18 | [GSToken: Geometry-Structured Gaussian Tokens for Compact 3D Medical Image Representation](https://arxiv.org/abs/2608.17425v1) | 2608.17425v1 | 6 |
| 2026-08-18 | [What Tokens are Learned when Tokenization is Optimized Jointly with Language Modeling?](https://arxiv.org/abs/2608.17325v1) | 2608.17325v1 | 18 |
| 2026-08-17 | [PXDepth: Pixel-Space Modeling for Structure Preserving Monocular Depth Estimation](https://arxiv.org/abs/2608.16984v2) | 2608.16984v2 | 6 |
| 2026-08-17 | [Does the LM Head Create a Harmful Gradient Bottleneck? A Causal Test](https://arxiv.org/abs/2608.16671v1) | 2608.16671v1 | 8 |
| 2026-08-17 | [GaussianDWM++: Language-Grounded 3D Gaussian Driving World Model for Unified Scene Understanding, Editing, and Multi-Modal Generation](https://arxiv.org/abs/2608.16234v1) | 2608.16234v1 | 6 |
| 2026-08-16 | [Dynamic Multi-Byte Prediction With Hierarchical Language Models](https://arxiv.org/abs/2608.15454v2) | 2608.15454v2 | 12 |
| 2026-08-15 | [A Pilot Study of Autocompleting Tokenizers](https://arxiv.org/abs/2608.15080v1) | 2608.15080v1 | 18 |
| 2026-08-14 | [MegaParts: Scaling Part-Aware 3D Object Generation to 300 Parts via Token-Efficient Autoregressive Modeling](https://arxiv.org/abs/2608.14783v1) | 2608.14783v1 | 8 |
| 2026-08-14 | [SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Reasoning](https://arxiv.org/abs/2608.14277v1) | 2608.14277v1 | 6 |
| 2026-08-14 | [PPOM: Marginalizing Patch-Grid Phase for CLIP-Based Generalizable Vision-Language Prompt Tuning](https://arxiv.org/abs/2608.13969v1) | 2608.13969v1 | 7 |
| 2026-08-13 | [Into the ORBIT for Time Series: Training Regimes for Foundation Models](https://arxiv.org/abs/2608.13262v1) | 2608.13262v1 | 6 |
| 2026-08-13 | [STAR: Structured Tokenization and Target-Aware Interest Representation for PCVR Prediction](https://arxiv.org/abs/2608.12986v3) | 2608.12986v3 | 6 |
| 2026-08-13 | [FastThaiG2P: Lightning-fast Thai Grapheme-to-phoneme Conversion for Voice Agent Pipelines](https://arxiv.org/abs/2608.12814v1) | 2608.12814v1 | 6 |
| 2026-08-13 | [ReconSpan: Reconstruction-Guided Adaptive Latent Tokenization](https://arxiv.org/abs/2608.12756v1) | 2608.12756v1 | 6 |
| 2026-08-12 | [Trie Automata for Constrained Decoding over Large Finite Sets](https://arxiv.org/abs/2608.12574v1) | 2608.12574v1 | 6 |
| 2026-08-12 | [G0.5: One Autoregressive Stream for Robot Reasoning and Action](https://arxiv.org/abs/2608.11739v1) | 2608.11739v1 | 6 |
| 2026-08-12 | [Phoenix TTS: High-Fidelity Synthesis and Voice Conversion via Flow-Matching-Driven Speech Tokenization](https://arxiv.org/abs/2608.11737v1) | 2608.11737v1 | 10 |
| 2026-08-11 | [Lifecycle-Optimal Tokenization: Vocabulary Size as a Deployment-Regime-Dependent Infrastructure Parameter](https://arxiv.org/abs/2608.11361v1) | 2608.11361v1 | 14 |
| 2026-08-11 | [Pitch Contour Tokenization using VQ-VAE and Its Application on Korean Traditional Music Analysis](https://arxiv.org/abs/2608.10979v1) | 2608.10979v1 | 8 |
| 2026-08-11 | [FedCGR: Federated Cross-Domain Generative Recommendation](https://arxiv.org/abs/2608.10929v1) | 2608.10929v1 | 7 |
| 2026-08-11 | [Can Released LLM Vocabularies Support Token-Level Estimation of Hidden Corpora?](https://arxiv.org/abs/2608.10690v2) | 2608.10690v2 | 6 |
| 2026-08-11 | [Auditing Chinese Web-scale Corpora via Sampled BPE Token Statistics](https://arxiv.org/abs/2608.10678v2) | 2608.10678v2 | 7 |
| 2026-08-11 | [MedUP: Awakening Unified Understanding and Perception in Medical Vision-Language Models](https://arxiv.org/abs/2608.10635v1) | 2608.10635v1 | 6 |
| 2026-08-11 | [Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models](https://arxiv.org/abs/2608.10484v1) | 2608.10484v1 | 8 |
| 2026-08-10 | [Measuring the Tokenization Premium: A Cost Audit for Underserved Language Communities](https://arxiv.org/abs/2608.09046v1) | 2608.09046v1 | 10 |
| 2026-08-09 | [Explicit Boundary Markers for Subword Vocabularies](https://arxiv.org/abs/2608.08847v2) | 2608.08847v2 | 17 |
| 2026-08-08 | [TokenPrint: A Calibrated Token-Space Fingerprint for Language-Model Provenance](https://arxiv.org/abs/2608.08139v1) | 2608.08139v1 | 6 |
| 2026-08-07 | [Evaluating Dedicated Monolingual and Joint Multilingual Causal Models for Dravidian Languages](https://arxiv.org/abs/2608.07727v1) | 2608.07727v1 | 10 |
| 2026-08-07 | [Tokenizer-Generator Coupling in Medical Image Generation](https://arxiv.org/abs/2608.07713v2) | 2608.07713v2 | 8 |
| 2026-08-07 | [The Quantum Shortcut: Complex Phase-State Dynamics Reduce the Optimization Steps of Sequence Models](https://arxiv.org/abs/2608.14691v1) | 2608.14691v1 | 6 |
| 2026-08-07 | [Bend the Basics: Degradation-Aware Deformable Tokenization for All-in-One Image Restoration](https://arxiv.org/abs/2608.06832v1) | 2608.06832v1 | 9 |
| 2026-08-06 | [KVAE: Family of Tokenizers for Multimodal Generative Models](https://arxiv.org/abs/2608.05798v1) | 2608.05798v1 | 6 |
| 2026-08-05 | [GVC-RT: Towards Real-Time Generative Video Compression at Ultra-Low Bitrates](https://arxiv.org/abs/2608.04891v1) | 2608.04891v1 | 8 |
| 2026-08-05 | [Kathleen Writes: Autoregressive Generation and Data Scaling Without Attention](https://arxiv.org/abs/2608.04678v1) | 2608.04678v1 | 8 |
| 2026-08-04 | [Large Language Models for Low-Resource Languages: A Conceptual Framework for an Electronic Explanatory Dictionary of the Tajik Language](https://arxiv.org/abs/2608.04186v3) | 2608.04186v3 | 8 |
| 2026-08-04 | [Agogic: Performance-Timed Music Tokens for LLM-Native Text-to-Symbolic-Music Generation](https://arxiv.org/abs/2608.03999v1) | 2608.03999v1 | 10 |
| 2026-08-04 | [Disentangling Language Modeling and Boundaries](https://arxiv.org/abs/2608.03599v1) | 2608.03599v1 | 12 |
| 2026-08-04 | [Beyond Initialization Loss: A Systematic Study of Token Embedding Initialization Strategies for LLM Vocabulary Extension](https://arxiv.org/abs/2608.03494v1) | 2608.03494v1 | 8 |
| 2026-08-04 | [Hi-Token: Hierarchical Coordinate Tokenization for Generative Visual Grounding](https://arxiv.org/abs/2608.03471v3) | 2608.03471v3 | 6 |
| 2026-08-04 | [DigitCode: Symbolic Tokenization of Hand Motion by Anatomical Units](https://arxiv.org/abs/2608.03127v1) | 2608.03127v1 | 10 |
| 2026-08-03 | [Character Iconicity vs. Arbitrariness: An Arabic NLP Perspective](https://arxiv.org/abs/2608.02935v1) | 2608.02935v1 | 8 |
| 2026-08-03 | [Unpaired Modality-Agnostic Generative Recommendation](https://arxiv.org/abs/2608.02477v1) | 2608.02477v1 | 8 |
| 2026-08-03 | [Token-Native Storage: Read and Write in your Agent's Language](https://arxiv.org/abs/2608.02376v2) | 2608.02376v2 | 8 |
| 2026-08-03 | [TELLER: Non-intrusive Cross-Layer Root-Cause Analysis for LLM Inference](https://arxiv.org/abs/2608.01975v1) | 2608.01975v1 | 6 |
| 2026-08-02 | [Slot2Text: Object-Centric Visual Tokenization for Efficient and Spatially Traceable Surgical MLLMs](https://arxiv.org/abs/2608.01473v2) | 2608.01473v2 | 6 |
| 2026-08-02 | [Morphology Aware Reversible Semantic Tokenization and Hierarchical Word Composition for Tamil Language Models](https://arxiv.org/abs/2608.01153v1) | 2608.01153v1 | 14 |
| 2026-08-01 | [Pruned BPE: Post-training Visibility Pruning and Token Reallocation for Byte Pair Encoding](https://arxiv.org/abs/2608.00837v3) | 2608.00837v3 | 13 |
| 2026-08-01 | [P2Voxel: Pyramid Pivot Voxelization for 3D Mesh Tokenization](https://arxiv.org/abs/2608.07549v1) | 2608.07549v1 | 6 |
| 2026-08-01 | [Can Perplexity Serve as a Cognitive Signal for Code Understandability?](https://arxiv.org/abs/2608.00624v1) | 2608.00624v1 | 10 |
| 2026-08-01 | [Writing-System-Level Tokenizer Adaptation for Byte-Level BPE](https://arxiv.org/abs/2608.00582v1) | 2608.00582v1 | 18 |
| 2026-08-01 | [TI-StegoAlign: Channel-Guided Post-Training for Generative Text Steganography under Tokenization Inconsistency](https://arxiv.org/abs/2608.00382v1) | 2608.00382v1 | 7 |
| 2026-07-31 | [TokTier: Exact Stateful CPU+GPU Tokenization for Agentic LLM Serving](https://arxiv.org/abs/2607.29678v3) | 2607.29678v3 | 12 |
| 2026-07-31 | [pico-type: A 1.5M-Parameter Byte-Level Multi-Head Content Classifier](https://arxiv.org/abs/2608.14658v1) | 2608.14658v1 | 17 |
| 2026-07-31 | [Tokenizer-Agnostic Engram Module](https://arxiv.org/abs/2607.29065v1) | 2607.29065v1 | 7 |
| 2026-07-30 | [LLM-Based Generative Retrieval for Snapchat Content Recommendation](https://arxiv.org/abs/2607.28895v4) | 2607.28895v4 | 7 |
| 2026-07-30 | [PCAP-LM: An LLM-Native Text Representation for TLS Bulk Traffic Analysis](https://arxiv.org/abs/2607.28100v1) | 2607.28100v1 | 8 |
| 2026-07-29 | [Language Models are not Equally Robust to Non-Canonical Tokenization across Languages](https://arxiv.org/abs/2607.26831v1) | 2607.26831v1 | 10 |
| 2026-07-29 | [Explicit Note-Event Tokenization and Pitch-Validity Constrained Decoding for MIDI-to-Tablature Transcription](https://arxiv.org/abs/2607.26440v1) | 2607.26440v1 | 6 |
| 2026-07-29 | [H+ Embedding: Harmonizing Global and Token-Level Retrieval with Context-Dependent Phrases](https://arxiv.org/abs/2608.00065v3) | 2608.00065v3 | 9 |
| 2026-07-28 | [MoMo: Dial Motion Mode in Robot Manipulation with Spatiotemporal Action Tokenization](https://arxiv.org/abs/2607.26315v1) | 2607.26315v1 | 10 |
| 2026-07-28 | [Grevo: A Unified Generative Recommendation Framework with Evolutionary Item Indexing](https://arxiv.org/abs/2607.25329v1) | 2607.25329v1 | 6 |
| 2026-07-28 | [TopoGR: Revealing and Preserving Latent Structure of Semantic ID in Generative Recommendation](https://arxiv.org/abs/2607.25216v1) | 2607.25216v1 | 8 |
| 2026-07-27 | [Mage-VL: An Efficient Codec-Native Streaming Multimodal Foundation Model](https://arxiv.org/abs/2607.24904v1) | 2607.24904v1 | 6 |
| 2026-07-27 | [Physics Transformer: Tailoring Transformer for General PDE Prediction](https://arxiv.org/abs/2607.24513v1) | 2607.24513v1 | 6 |
| 2026-07-27 | [The Tokenizer Tax: Quantifying and Explaining the Cross-Lingual Cost of Subword Tokenization for Indian Languages](https://arxiv.org/abs/2607.24276v1) | 2607.24276v1 | 18 |
| 2026-07-27 | [Training a Language Model End-to-End in Rust: An Experience Report](https://arxiv.org/abs/2609.25008v1) | 2609.25008v1 | 12 |
| 2026-07-25 | [Explaining BiomedCLIP with Weighted Banzhaf Interactions Supported by Tree-Gram Parsing](https://arxiv.org/abs/2607.23368v1) | 2607.23368v1 | 12 |
| 2026-07-25 | [Joint Optimization for Greedy Longest-match Tokenization](https://arxiv.org/abs/2607.23362v1) | 2607.23362v1 | 14 |
| 2026-07-25 | [BHARATI: Morphology-Aware Tokenizers for Classical Indian Languages with Subword Fertility Analysis](https://arxiv.org/abs/2607.23319v1) | 2607.23319v1 | 24 |
| 2026-07-25 | [CAPT: A Multi-task Continuous Autoregressive Transformer enabling Cross-dataset and Cross-species Transfer for Calcium Population Dynamics](https://arxiv.org/abs/2607.23258v3) | 2607.23258v3 | 7 |
| 2026-07-24 | [CHiPS: Character Histograms and Positional Signals for Lightweight Authorship Attribution in Romanian Texts](https://arxiv.org/abs/2607.22884v1) | 2607.22884v1 | 6 |
| 2026-07-24 | [Cross-Tokenizer On-Policy Distillation via Byte-Prefix Marginalization](https://arxiv.org/abs/2607.22334v1) | 2607.22334v1 | 8 |
| 2026-07-24 | [Industrial Tokenization for LLM-Based Health Intelligence: A Federated Architecture for Industrial Evidence Integration](https://arxiv.org/abs/2607.22153v1) | 2607.22153v1 | 6 |
| 2026-07-23 | [Ordered Action Tokens for Visuomotor Policy Learning](https://arxiv.org/abs/2607.21670v1) | 2607.21670v1 | 8 |
| 2026-07-22 | [TINY_SCHILLER: A Drop-In German Drama Corpus for Small Language Models](https://arxiv.org/abs/2607.19992v1) | 2607.19992v1 | 6 |
| 2026-07-22 | [A Unified Tokenization Framework for Pain Recognition using Heterogeneous 3D Modalities](https://arxiv.org/abs/2607.19716v2) | 2607.19716v2 | 6 |
| 2026-07-21 | [VQ-Transplant: Efficient VQ-Module Integration for Pre-trained Visual Tokenizers](https://arxiv.org/abs/2607.19575v2) | 2607.19575v2 | 10 |
| 2026-07-21 | [Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation and Editing](https://arxiv.org/abs/2607.19064v2) | 2607.19064v2 | 8 |
| 2026-07-21 | [Content is What Remains: Invariant Speech Tokenization from Parallel Utterances](https://arxiv.org/abs/2607.19033v1) | 2607.19033v1 | 10 |
| 2026-07-21 | [Empowering Cross-Domain Sequential Recommendation with Hybrid Tokenization and Serial-Parallel Decoding](https://arxiv.org/abs/2607.28659v1) | 2607.28659v1 | 6 |
| 2026-07-21 | [Topology-Aware Tokenization for Generative Recommendation](https://arxiv.org/abs/2607.18600v1) | 2607.18600v1 | 11 |
| 2026-07-20 | [Tokenizing Crosslingual Homographs](https://arxiv.org/abs/2607.17689v1) | 2607.17689v1 | 16 |
| 2026-07-18 | [InLiER: Learning-Free Heterogeneous LiDAR Place Recognition via Intermediate Mixed-Radix Structural Keypoint Tokenization](https://arxiv.org/abs/2607.16862v2) | 2607.16862v2 | 8 |
| 2026-07-18 | [RoleMix: Unifying Sequential and Non-Sequential Features via Semantic Tokenization for Post-Click Conversion Rate Prediction](https://arxiv.org/abs/2607.22700v1) | 2607.22700v1 | 6 |
| 2026-07-17 | [The Limits of BPE Tokenization in Polish: Segmentation-Flexional Forms, Grammatical Anchoring, and First-Person Stability in Inflectional Language Models](https://arxiv.org/abs/2609.17553v1) | 2609.17553v1 | 13 |
| 2026-07-17 | [Removable and Irreducible: A Token-Cost Ledger for the Multilingual Tokenization Tax](https://arxiv.org/abs/2609.00378v1) | 2609.00378v1 | 10 |
| 2026-07-17 | [Beyond Two Bytes per Letter: Tokenization Overhead in Cyrillic AI Systems](https://arxiv.org/abs/2608.21384v1) | 2608.21384v1 | 18 |
| 2026-07-16 | [qZACH-ViT: Quantization-Aware Intrinsic Explanations with Recursive Attribution-Stabilized Optimization](https://arxiv.org/abs/2607.15421v1) | 2607.15421v1 | 6 |
| 2026-07-16 | [In-Place Tokenizer Expansion for Pre-trained LLMs](https://arxiv.org/abs/2607.15232v1) | 2607.15232v1 | 11 |
| 2026-07-16 | [Expanding the Lexicon of Ge'ez Based African Languages: A Comparative Study of Amharic and Tigrinya](https://arxiv.org/abs/2607.15209v4) | 2607.15209v4 | 15 |
| 2026-07-15 | [Privacy Leakage in Federated Learning in Radiology Reports: A Comparative Evaluation of Tokenizer-Driven Privacy Risks](https://arxiv.org/abs/2607.14205v1) | 2607.14205v1 | 8 |
| 2026-07-15 | [GMoT: Gated Motion-Aware Tokenization for Fine-Grained Micro-Gesture Video Reasoning with Multimodal LLMs](https://arxiv.org/abs/2607.16322v1) | 2607.16322v1 | 6 |
| 2026-07-15 | [Discrete Diffusion Models: A Unified Framework from Tokenization to Generation](https://arxiv.org/abs/2607.13431v2) | 2607.13431v2 | 8 |
| 2026-07-11 | [GRID: Grammar-Railed Decoding for Enterprise SQL Generation](https://arxiv.org/abs/2607.11951v1) | 2607.11951v1 | 8 |
| 2026-07-10 | [Tokenizer Transplantation: Mitigating Autoregressive Collapse in Edge-Efficient Bengali ASR](https://arxiv.org/abs/2607.09598v2) | 2607.09598v2 | 13 |
| 2026-07-10 | [FreyaTTS: A Compact Tokenizer-Free Flow-Matching Transformer for Turkish-First Speech Synthesis](https://arxiv.org/abs/2607.09530v2) | 2607.09530v2 | 8 |
| 2026-07-10 | [Subtoken Vision Transformer for Fine-grained Recognition](https://arxiv.org/abs/2607.09086v2) | 2607.09086v2 | 6 |
| 2026-07-09 | [VocaDet: Sample-Driven Open-Vocabulary Object Detection and Segmentation via Visual Tokenization and Vector Database Retrieval](https://arxiv.org/abs/2607.08541v1) | 2607.08541v1 | 9 |
| 2026-07-09 | [Echoes Across Vietnam's Highlands, Delta, and Coast: A Multilingual Corpus for Cham, Khmer, and Tay-Nung](https://arxiv.org/abs/2607.08362v4) | 2607.08362v4 | 6 |
| 2026-07-09 | [LUMI: Tokenizer-Agnostic LLM-Based Lossless Image Compression](https://arxiv.org/abs/2607.08221v1) | 2607.08221v1 | 15 |
| 2026-07-07 | [The Functionalizer: Lossless Functional Decomposition for Subword Tokenization](https://arxiv.org/abs/2609.15991v2) | 2609.15991v2 | 19 |
| 2026-07-07 | [XRFormer: Multiscale Tokenization for XRF Representation Learning](https://arxiv.org/abs/2607.06424v1) | 2607.06424v1 | 11 |
| 2026-07-07 | [BlueMagpie-TTS: A Token-Efficient Tokenizer, Language Model, and TTS for Taiwanese-Accent Code-Switching Speech](https://arxiv.org/abs/2607.06054v1) | 2607.06054v1 | 14 |
| 2026-07-06 | [Where to cut, how deep: BPE and Unigram-LM on chemistry SMILES](https://arxiv.org/abs/2607.05691v1) | 2607.05691v1 | 18 |
| 2026-07-05 | [Cross-Subject Modeling for Widefield Calcium Imaging via Atlas-Aligned Spatiotemporal Tokenization](https://arxiv.org/abs/2607.09754v1) | 2607.09754v1 | 6 |
| 2026-07-05 | [Speaker-Disentangled Chunk-Wise Regression for Syllabic Tokenization](https://arxiv.org/abs/2607.04064v1) | 2607.04064v1 | 10 |
| 2026-07-04 | [One Image, No Tokens: A Controlled Study of Glyph-Based Chinese Language Modeling](https://arxiv.org/abs/2607.03994v2) | 2607.03994v2 | 6 |
| 2026-07-04 | [Beyond Item Order: Temporal Gap Tokenization for Generative Recommendation with Semantic IDs](https://arxiv.org/abs/2607.03918v1) | 2607.03918v1 | 6 |
| 2026-07-03 | [STELLA: Efficient Sensor-to-LLM Translation for On-Device Human Activity Recognition](https://arxiv.org/abs/2607.03089v1) | 2607.03089v1 | 9 |
| 2026-07-02 | [PointDiT: Pixel-Space Diffusion for Monocular Geometry Estimation](https://arxiv.org/abs/2607.02515v1) | 2607.02515v1 | 6 |
| 2026-07-02 | [SAMoR: Motion Modelling for Articulated Objects of Any Skeleton and Topology](https://arxiv.org/abs/2607.02148v1) | 2607.02148v1 | 7 |
| 2026-07-01 | [BudgetBench: A Budget-Tiered Protocol and Pilot Harness for Memory Strategy Evaluation in Local Large Language Model Agents](https://arxiv.org/abs/2609.13149v1) | 2609.13149v1 | 8 |
| 2026-07-01 | [SpiralFovea: Input-Adaptive Foveated Tokenization as a Third Lever of Resource-Adaptive Inference](https://arxiv.org/abs/2607.00780v2) | 2607.00780v2 | 8 |
| 2026-06-30 | [Steal the Patch Size: Adversarially Manipulate Vision-Language Models](https://arxiv.org/abs/2607.00174v1) | 2607.00174v1 | 11 |
| 2026-06-30 | [ALEE: Any-Language Evaluation of Embeddings via English-Centric Minimal Pairs](https://arxiv.org/abs/2607.00171v2) | 2607.00171v2 | 9 |
| 2026-06-30 | [GEAR: Guided End-to-End AutoRegression for Image Synthesis](https://arxiv.org/abs/2606.32039v1) | 2606.32039v1 | 6 |
| 2026-06-30 | [GR2 Technical Report](https://arxiv.org/abs/2606.31984v3) | 2606.31984v3 | 6 |
| 2026-06-29 | [AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation](https://arxiv.org/abs/2606.30811v1) | 2606.30811v1 | 10 |
| 2026-06-29 | [DNA Language Models: An Assessment of Pre-Training for Fine-Tuning Tasks](https://arxiv.org/abs/2606.30140v1) | 2606.30140v1 | 6 |
| 2026-06-29 | [SA-VLA: State-aware tokenizer for improving Vision-Language-Action Models' performance](https://arxiv.org/abs/2606.30113v1) | 2606.30113v1 | 10 |
| 2026-06-29 | [Nemotron-Labs-Diffusion-Image: Advancing Masked Discrete Diffusion for High-Resolution Image Synthesis](https://arxiv.org/abs/2606.29814v2) | 2606.29814v2 | 7 |
| 2026-06-28 | [Scenes as Objects, Not Primitives: Instance-Structured 3D Tokenization from Unposed Views](https://arxiv.org/abs/2606.29513v1) | 2606.29513v1 | 8 |
| 2026-06-28 | [GPC: Large-Scale Generative Pretraining for Transferable Motor Control](https://arxiv.org/abs/2606.29148v1) | 2606.29148v1 | 6 |
| 2026-06-26 | [Parallel Rollout Approximation for Pixel-Space Autoregressive Image Generation](https://arxiv.org/abs/2606.27978v1) | 2606.27978v1 | 10 |
| 2026-06-25 | [Beyond MoCap: Scaling Motion Tokenizers with Synthetic Human Motion for Generative Modeling](https://arxiv.org/abs/2606.27547v1) | 2606.27547v1 | 8 |
| 2026-06-25 | [How Surprising Is Historical Italian to Language Models? Tokenization Tax, Comprehension Tax, and a Simple Mitigation](https://arxiv.org/abs/2606.27275v1) | 2606.27275v1 | 7 |
| 2026-06-25 | [The Geometry of Updates: Fisher Alignment at Vocabulary Scale](https://arxiv.org/abs/2606.27242v1) | 2606.27242v1 | 8 |
| 2026-06-25 | [MinGram: A Minimalist Unigram Tokenizer with High Compression and Competitive Morphological Alignment](https://arxiv.org/abs/2606.27019v2) | 2606.27019v2 | 10 |
| 2026-06-25 | [wav2tok 2.0: Scalable Audio Tokenization Maintaining Explicit Pairwise Token Alignment for Efficient Audio Retrieval](https://arxiv.org/abs/2606.26824v1) | 2606.26824v1 | 10 |
| 2026-06-24 | [The Galaxy's Guide to the Tokenizer: A Benchmark for Scientific Foundation Models](https://arxiv.org/abs/2606.25610v1) | 2606.25610v1 | 10 |
| 2026-06-23 | [CANDLE: CTC-based Arabic Noisy-character Deduplication using a Lightweight Encoder](https://arxiv.org/abs/2606.24758v2) | 2606.24758v2 | 6 |
| 2026-06-23 | [The African Language Tax: Quantifying the Cost, Latency, and Context Penalty of Tokenizing African Languages in Frontier LLMs](https://arxiv.org/abs/2606.24460v1) | 2606.24460v1 | 14 |
| 2026-06-22 | [QuechuaTok: Morphological Boundary Accuracy as a Necessary Metric for Tokenizer Evaluation in Agglutinative Low-Resource Languages](https://arxiv.org/abs/2606.23943v2) | 2606.23943v2 | 12 |
| 2026-06-22 | [Teaching LLMs String Matching, Backtracking, and Error Recovery to Deduce Bases and Truth Tables for the Combinatorially Exploding Bit Manipulation Puzzles](https://arxiv.org/abs/2606.23672v3) | 2606.23672v3 | 8 |
| 2026-06-22 | [LangMAP: A Language-Adaptive Approach to Tokenization](https://arxiv.org/abs/2606.23566v3) | 2606.23566v3 | 12 |
| 2026-06-19 | [Structural Assessment for Understanding and Guiding Dataset Distillation in Discrete Token Space](https://arxiv.org/abs/2606.21705v1) | 2606.21705v1 | 6 |
| 2026-06-19 | [NAC: Neural Action Codec for Vision-Language-Action Models](https://arxiv.org/abs/2606.21372v2) | 2606.21372v2 | 8 |
| 2026-06-18 | [Phonemes to the Rescue: Multilingual Tokenization Based on International Phonetic Alphabet](https://arxiv.org/abs/2606.20993v1) | 2606.20993v1 | 15 |
| 2026-06-18 | [B[FM]$^2$: Brain Foundation Model via Flow Matching with SplitUNet](https://arxiv.org/abs/2606.20812v2) | 2606.20812v2 | 6 |
| 2026-06-18 | [IHUBERT: Vector-Based Semantic Deduplication and Domain-Balanced Pretraining for Persian Resources](https://arxiv.org/abs/2606.20089v1) | 2606.20089v1 | 16 |
| 2026-06-18 | [Variable-Length Tokenization via Learnable Global Merging for Diffusion Transformers](https://arxiv.org/abs/2606.20076v1) | 2606.20076v1 | 10 |
| 2026-06-17 | [BrainG3N: A Dual-Purpose Tokenizer for Controllable 3D Brain MRI Generation](https://arxiv.org/abs/2606.19651v2) | 2606.19651v2 | 7 |
| 2026-06-17 | [Toten: A Knowledge-Based System For Structure-Preserving Representation Of Physical Quantities And Technical Notation In Brazilian Portuguese](https://arxiv.org/abs/2606.19626v2) | 2606.19626v2 | 11 |
| 2026-06-17 | [FrequencyFormer: A Co-Designed Sensor-to-Processor Pipeline for Frequency-Domain Vision Transformer Inference](https://arxiv.org/abs/2606.19574v1) | 2606.19574v1 | 11 |
| 2026-06-17 | [Beyond Tokenization: Direct Timestep Embedding and Contrastive Alignment for Time-Series Question Answering](https://arxiv.org/abs/2606.18986v2) | 2606.18986v2 | 9 |
| 2026-06-17 | [Morpheus: A Morphology-Aware Neural Tokenizer and Word Embedder for Turkish](https://arxiv.org/abs/2606.18717v2) | 2606.18717v2 | 13 |
| 2026-06-16 | [Unified Multimodal Autoregressive Modeling with Shared Context-Visual Tokenizer is Key to Unification](https://arxiv.org/abs/2606.18249v2) | 2606.18249v2 | 8 |
| 2026-06-16 | [TivTok: Broadcasting Time-Invariant Tokens for Scalable Video Tokenization](https://arxiv.org/abs/2606.17590v1) | 2606.17590v1 | 10 |
| 2026-06-15 | [OTRO: Oblivious Tokenization Path with Square-Root ORAM](https://arxiv.org/abs/2606.17358v3) | 2606.17358v3 | 10 |
| 2026-06-15 | [XL-ChannelDiff: An Efficient Diffusion-Based Multi-Domain Near-Field Channel Extrapolation Framework for XL-MIMO Systems](https://arxiv.org/abs/2606.16628v2) | 2606.16628v2 | 6 |
| 2026-06-14 | [Koshur Diacritizer: A Byte-Level Sequence-to-Sequence Model for Kashmiri Diacritic Restoration](https://arxiv.org/abs/2606.15883v2) | 2606.15883v2 | 6 |
| 2026-06-14 | [Emergent retokenization symmetry in large language models: phenomenology and applications](https://arxiv.org/abs/2606.15521v1) | 2606.15521v1 | 13 |
| 2026-06-13 | [Show the Signal, Hide the Noise: Spectral Forcing for Pixel-Space Diffusion](https://arxiv.org/abs/2606.15236v2) | 2606.15236v2 | 6 |
| 2026-06-13 | [PACUTE: Phonology-, Affix-, and Character-level Understanding of Tokens for Filipino](https://arxiv.org/abs/2606.15144v1) | 2606.15144v1 | 11 |
| 2026-06-13 | [MotionVLA: Vision-Language-Action Model for Humanoid Motion](https://arxiv.org/abs/2606.15142v1) | 2606.15142v1 | 6 |
| 2026-06-13 | [Equity with Efficiency: An Empirical Study of Tokenizers for Multilingual Large Language Models](https://arxiv.org/abs/2606.15044v1) | 2606.15044v1 | 24 |
| 2026-06-12 | [Beyond Perplexity: UTF-8 Validity in Byte-aware Language Models](https://arxiv.org/abs/2606.14122v2) | 2606.14122v2 | 8 |
| 2026-06-11 | [RepWAM: World Action Modeling with Representation Visual-Action Tokenizers](https://arxiv.org/abs/2606.13674v2) | 2606.13674v2 | 10 |
| 2026-06-11 | [HYDRA-X: Native Unified Multimodal Models with Holistic Visual Tokenizers](https://arxiv.org/abs/2606.13289v1) | 2606.13289v1 | 11 |
| 2026-06-10 | [Augmenting Molecular Language Models with Local $n$-gram Memory](https://arxiv.org/abs/2606.12113v1) | 2606.12113v1 | 11 |
| 2026-06-10 | [MoGeFlow: Flowing Through Motion Codebook Geometry for Text-to-Motion Generation](https://arxiv.org/abs/2606.11656v3) | 2606.11656v3 | 7 |
| 2026-06-09 | [UniDexTok: A Unified Dexterous Hand Tokenizer from Real Data](https://arxiv.org/abs/2606.10683v2) | 2606.10683v2 | 10 |
| 2026-06-09 | [SIDInspector: A Mapping-First Diagnostic Resource for Semantic-ID Tokenizers](https://arxiv.org/abs/2606.10375v2) | 2606.10375v2 | 6 |
| 2026-06-08 | [Invisible to humans, visible to machines: a preregistered audit of Unicode fidelity across four biomedical bibliographic APIs](https://arxiv.org/abs/2606.24897v1) | 2606.24897v1 | 6 |
| 2026-06-08 | [Breaking the Tokenizer Barrier: On-Policy Distillation across Model Families](https://arxiv.org/abs/2606.09456v1) | 2606.09456v1 | 6 |
| 2026-06-07 | [NE-BERT: A Multilingual Language Model for Nine Northeast Indian Languages](https://arxiv.org/abs/2608.18094v1) | 2608.18094v1 | 10 |
| 2026-06-07 | [X-Tokenizer: A Multimodal Action Tokenizer for Vision-Language-Action Pretraining](https://arxiv.org/abs/2606.14752v2) | 2606.14752v2 | 10 |
| 2026-06-07 | [A Taxonomy of Real-World Asset Tokenization for Blockchain-Based Financial Infrastructure](https://arxiv.org/abs/2606.08534v2) | 2606.08534v2 | 6 |
| 2026-06-06 | [Neural Field Tokenizations with Hierarchy and Spatial Locality Priors](https://arxiv.org/abs/2606.08204v2) | 2606.08204v2 | 6 |
| 2026-06-05 | [AdaTok: Self-Budgeting Image Tokenization with Quality-Preserving Dynamic Tokens](https://arxiv.org/abs/2606.07185v1) | 2606.07185v1 | 10 |
| 2026-06-05 | [SuTRA : Structurally-Unified Tokenization with Root Awareness](https://arxiv.org/abs/2608.18087v2) | 2608.18087v2 | 16 |
| 2026-06-05 | [DREAM: Dynamic Refinement of Early Assignment Mappings](https://arxiv.org/abs/2606.06947v1) | 2606.06947v1 | 8 |
| 2026-06-04 | [F3-Tokenizer: Taming Audio Autoencoder Latents for Understanding and Generation](https://arxiv.org/abs/2606.06357v1) | 2606.06357v1 | 6 |
| 2026-06-04 | [English-to-Prakrit Machine Translation via Multilingual Transfer Learning](https://arxiv.org/abs/2606.06038v1) | 2606.06038v1 | 6 |
| 2026-06-04 | [OPRD: On-Policy Representation Distillation](https://arxiv.org/abs/2606.06021v4) | 2606.06021v4 | 6 |
| 2026-06-04 | [Balancing Image Compression and Generation with Bootstrapped Tokenization](https://arxiv.org/abs/2606.05552v2) | 2606.05552v2 | 10 |
| 2026-06-03 | [GOTabPFN: From Feature Ordering to Compact Tokenization for Tabular Foundation Models on High-Dimensional Data](https://arxiv.org/abs/2606.05441v2) | 2606.05441v2 | 6 |
| 2026-06-03 | [LDARNet: DNA Adaptive Representation Network with Learnable Tokenization for Genomic Modeling](https://arxiv.org/abs/2606.04552v2) | 2606.04552v2 | 8 |
| 2026-06-03 | [ChannelTok: Efficient Flexible-Length Vision Tokenization](https://arxiv.org/abs/2606.04461v1) | 2606.04461v1 | 10 |
| 2026-06-03 | [CleanCodec: Efficient and Robust Speech Tokenization via Perceptually Guided Encoding](https://arxiv.org/abs/2606.04418v1) | 2606.04418v1 | 6 |
| 2026-06-03 | [MeshTok: Efficient Multi-Scale Tokenization for Scalable PDE Transformers](https://arxiv.org/abs/2606.04366v1) | 2606.04366v1 | 8 |

### 2025
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2025-12-31 | [When the Same Coefficients Reach Different Places: Asymmetric Realizability in Transplanting Tokenizers across Large Language Models](https://arxiv.org/abs/2601.00065v3) | 2601.00065v3 | 9 |
| 2025-12-27 | [Pose-Guided Residual Refinement for Interpretable Text-to-Motion Generation and Editing](https://arxiv.org/abs/2512.22464v1) | 2512.22464v1 | 8 |
| 2025-12-26 | [Broken Words, Broken Performance: Effect of Tokenization on Performance of LLMs](https://arxiv.org/abs/2512.21933v1) | 2512.21933v1 | 12 |
| 2025-12-26 | [GQ-VAE: A gated quantized VAE for learning variable length tokens](https://arxiv.org/abs/2512.21913v1) | 2512.21913v1 | 12 |
| 2025-12-26 | [DPAR: Dynamic Patchification for Efficient Autoregressive Visual Generation](https://arxiv.org/abs/2512.21867v1) | 2512.21867v1 | 7 |
| 2025-12-23 | [TokSuite: Measuring the Impact of Tokenizer Choice on Language Model Behavior](https://arxiv.org/abs/2512.20757v2) | 2512.20757v2 | 10 |
| 2025-12-23 | [QuarkAudio Technical Report](https://arxiv.org/abs/2512.20151v1) | 2512.20151v1 | 8 |
| 2025-12-22 | [CETCAM: Camera-Controllable Video Generation via Consistent and Extensible Tokenization](https://arxiv.org/abs/2512.19020v1) | 2512.19020v1 | 6 |
| 2025-12-20 | [AraToken: Optimizing Arabic Tokenization with Normalization Pipeline and Language Extension for Qwen3](https://arxiv.org/abs/2512.18399v1) | 2512.18399v1 | 14 |
| 2025-12-19 | [Any-Optical-Model: A Universal Foundation Model for Optical Remote Sensing](https://arxiv.org/abs/2512.17224v1) | 2512.17224v1 | 7 |
| 2025-12-18 | [DNAMotifTokenizer: Towards Biologically Informed Tokenization of Genomic Sequences](https://arxiv.org/abs/2512.17126v2) | 2512.17126v2 | 16 |
| 2025-12-18 | [SFTok: Bridging the Performance Gap in Discrete Tokenizers](https://arxiv.org/abs/2512.16910v1) | 2512.16910v1 | 10 |
| 2025-12-18 | [InfoTok: Adaptive Discrete Video Tokenizer via Information-Theoretic Compression](https://arxiv.org/abs/2512.16975v3) | 2512.16975v3 | 10 |
| 2025-12-18 | [BEST-STD2.0: Balanced and Efficient Speech Tokenizer for Spoken Term Detection](https://arxiv.org/abs/2512.16395v2) | 2512.16395v2 | 6 |
| 2025-12-17 | [Bolmo: Byteifying the Next Generation of Language Models](https://arxiv.org/abs/2512.15586v2) | 2512.15586v2 | 14 |
| 2025-12-16 | [Cross-Tokenizer Likelihood Scoring Algorithms for Language Model Distillation](https://arxiv.org/abs/2512.14954v2) | 2512.14954v2 | 10 |
| 2025-12-16 | [Spherical Leech Quantization for Visual Tokenization and Generation](https://arxiv.org/abs/2512.14697v1) | 2512.14697v1 | 6 |
| 2025-12-16 | [Towards Nepali-language LLMs: Efficient GPT training with a Nepali BPE tokenizer](https://arxiv.org/abs/2512.14585v1) | 2512.14585v1 | 10 |
| 2025-12-16 | [SELECT: Detecting Label Errors in Real-world Scene Text Data](https://arxiv.org/abs/2512.14050v1) | 2512.14050v1 | 6 |
| 2025-12-15 | [Towards Scalable Pre-training of Visual Tokenizers for Generation](https://arxiv.org/abs/2512.13687v2) | 2512.13687v2 | 6 |
| 2025-12-15 | [Temporal Tokenization Strategies for Event Sequence Modeling with Large Language Models](https://arxiv.org/abs/2512.13618v3) | 2512.13618v3 | 14 |
| 2025-12-14 | [Lemon: A Unified and Scalable 3D Multimodal Model for Universal Spatial Understanding](https://arxiv.org/abs/2512.12822v1) | 2512.12822v1 | 6 |
| 2025-12-14 | [Which Pieces Does Unigram Tokenization Really Need?](https://arxiv.org/abs/2512.12641v2) | 2512.12641v2 | 6 |
| 2025-12-12 | [Do We Need Reformer for Vision? An Experimental Comparison with Vision Transformers](https://arxiv.org/abs/2512.11260v2) | 2512.11260v2 | 6 |
| 2025-12-11 | [Grounding Everything in Tokens for Multimodal Large Language Models](https://arxiv.org/abs/2512.10554v2) | 2512.10554v2 | 7 |
| 2025-12-08 | [A Simple Method to Enhance Pre-trained Language Models with Speech Tokens for Classification](https://arxiv.org/abs/2512.07571v3) | 2512.07571v3 | 7 |
| 2025-12-08 | [JEPA as a Neural Tokenizer: Learning Robust Speech Representations with Density Adaptive Attention](https://arxiv.org/abs/2512.07168v1) | 2512.07168v1 | 11 |
| 2025-12-05 | [Morphologically-Informed Tokenizers for Languages with Non-Concatenative Morphology: A case study of Yoloxóchtil Mixtec ASR](https://arxiv.org/abs/2512.06169v1) | 2512.06169v1 | 12 |
| 2025-12-04 | [Rethinking Tokenization for Clinical Time Series: When Less is More](https://arxiv.org/abs/2512.05217v1) | 2512.05217v1 | 7 |
| 2025-12-04 | [FASTer: Toward Efficient Autoregressive Vision Language Action Modeling via Neural Action Tokenization](https://arxiv.org/abs/2512.04952v2) | 2512.04952v2 | 10 |
| 2025-12-04 | [BIM-Native Tokenization for Constraint-Aware Room Layout Synthesis](https://arxiv.org/abs/2512.04832v3) | 2512.04832v3 | 7 |
| 2025-12-04 | [DeRA: Decoupled Representation Alignment for Video Tokenization](https://arxiv.org/abs/2512.04483v1) | 2512.04483v1 | 10 |
| 2025-12-03 | [Teaching Old Tokenizers New Words: Efficient Tokenizer Adaptation for Pre-trained Models](https://arxiv.org/abs/2512.03989v2) | 2512.03989v2 | 14 |
| 2025-12-02 | [On the Problem of Consistent Anomalies in Zero-Shot Anomaly Detection](https://arxiv.org/abs/2512.02520v1) | 2512.02520v1 | 6 |
| 2025-12-01 | [Feature Selection Empowered BERT for Detection of Hate Speech with Vocabulary Augmentation](https://arxiv.org/abs/2512.02141v1) | 2512.02141v1 | 7 |
| 2025-11-28 | [Accent Placement Models for Rigvedic Sanskrit Text](https://arxiv.org/abs/2511.23088v1) | 2511.23088v1 | 8 |
| 2025-11-28 | [AtomDisc: An Atom-level Tokenizer that Boosts Molecular LLMs and Reveals Structure--Property Associations](https://arxiv.org/abs/2512.03080v1) | 2512.03080v1 | 10 |
| 2025-11-27 | [CoFiRec: Coarse-to-Fine Tokenization for Generative Recommendation](https://arxiv.org/abs/2511.22707v2) | 2511.22707v2 | 11 |
| 2025-11-27 | [Binary-30K: A Heterogeneous Dataset for Deep Learning in Binary Analysis and Malware Detection](https://arxiv.org/abs/2511.22095v1) | 2511.22095v1 | 10 |
| 2025-11-26 | [TeleViT1.0: Teleconnection-aware Vision Transformers for Subseasonal to Seasonal Wildfire Pattern Forecasts](https://arxiv.org/abs/2512.00089v1) | 2512.00089v1 | 6 |
| 2025-11-26 | [Scenes as Tokens: Multi-Scale Normal Distributions Transform Tokenizer for General 3D Vision-Language Understanding](https://arxiv.org/abs/2511.21191v1) | 2511.21191v1 | 10 |
| 2025-11-26 | [Orthographic Constraint Satisfaction and Human Difficulty Alignment in Large Language Models](https://arxiv.org/abs/2511.21086v2) | 2511.21086v2 | 6 |
| 2025-11-25 | [Length-MAX Tokenizer for Language Models](https://arxiv.org/abs/2511.20849v2) | 2511.20849v2 | 11 |
| 2025-11-25 | [MSTN: A Lightweight and Fast Model for General TimeSeries Analysis](https://arxiv.org/abs/2511.20577v5) | 2511.20577v5 | 6 |
| 2025-11-25 | [DINO-Tok: Adapting DINO for Visual Tokenizers](https://arxiv.org/abs/2511.20565v2) | 2511.20565v2 | 6 |
| 2025-11-25 | [DuoTok: Source-Aware Dual-Track Music Tokenization for Vocal-Accompaniment Generation](https://arxiv.org/abs/2511.20224v3) | 2511.20224v3 | 10 |
| 2025-11-24 | [STORE: Semantic Tokenization, Orthogonal Rotation and Efficient Attention for Scaling Up Ranking Models](https://arxiv.org/abs/2511.18805v1) | 2511.18805v1 | 7 |
| 2025-11-18 | [On the Difficulty of Token-Level Modeling of Dysfluency and Fluency Shaping Artifacts](https://arxiv.org/abs/2512.02027v1) | 2512.02027v1 | 8 |
| 2025-11-18 | [Subword Tokenization Strategies for Kurdish Word Embeddings](https://arxiv.org/abs/2511.14696v1) | 2511.14696v1 | 15 |
| 2025-11-18 | [The Tokenization Bottleneck: How Vocabulary Extension Improves Chemistry Representation Learning in Pretrained Language Models](https://arxiv.org/abs/2511.14365v1) | 2511.14365v1 | 13 |
| 2025-11-18 | [LLM-Aligned Geographic Item Tokenization for Local-Life Recommendation](https://arxiv.org/abs/2511.14221v1) | 2511.14221v1 | 6 |
| 2025-11-18 | [GloTok: Global Perspective Tokenizer for Image Reconstruction and Generation](https://arxiv.org/abs/2511.14184v3) | 2511.14184v3 | 10 |
| 2025-11-18 | [AdaTok: Adaptive Token Compression with Object-Aware Representations for Efficient Multimodal LLMs](https://arxiv.org/abs/2511.14169v2) | 2511.14169v2 | 6 |
| 2025-11-17 | [MergeDNA: Context-aware Genome Modeling with Dynamic Tokenization through Token Merging](https://arxiv.org/abs/2511.14806v1) | 2511.14806v1 | 12 |
| 2025-11-17 | [Back to Basics: Let Denoising Generative Models Denoise](https://arxiv.org/abs/2511.13720v2) | 2511.13720v2 | 6 |
| 2025-11-17 | [Tokenize Once, Recommend Anywhere: Unified Item Tokenization for Multi-domain LLM-based Recommendation](https://arxiv.org/abs/2511.12922v1) | 2511.12922v1 | 6 |
| 2025-11-16 | [Backdoor Attacks on Open Vocabulary Object Detectors via Multi-Modal Prompt Tuning](https://arxiv.org/abs/2511.12735v2) | 2511.12735v2 | 6 |
| 2025-11-14 | [Binary BPE: A Family of Cross-Platform Tokenizers for Binary Analysis](https://arxiv.org/abs/2511.17573v1) | 2511.17573v1 | 17 |
| 2025-11-14 | [Seeing the Forest and the Trees: Query-Aware Tokenizer for Long-Video Multimodal Language Models](https://arxiv.org/abs/2511.11910v3) | 2511.11910v3 | 6 |
| 2025-11-14 | [Fast and Expressive Multi-Byte Prediction with Probabilistic Circuits](https://arxiv.org/abs/2511.11346v2) | 2511.11346v2 | 8 |
| 2025-11-14 | [Beyond Flatlands: Unlocking Spatial Intelligence by Decoupling 3D Reasoning from Numerical Regression](https://arxiv.org/abs/2511.11239v2) | 2511.11239v2 | 7 |
| 2025-11-13 | [Protein Structure Tokenization via Geometric Byte Pair Encoding](https://arxiv.org/abs/2511.11758v2) | 2511.11758v2 | 15 |
| 2025-11-13 | [VocalNet-M2: Advancing Low-Latency Spoken Language Modeling via Integrated Multi-Codebook Tokenization and Multi-Token Prediction](https://arxiv.org/abs/2511.10232v1) | 2511.10232v1 | 10 |
| 2025-11-13 | [From Static Structures to Ensembles: Studying and Harnessing Protein Structure Tokenization](https://arxiv.org/abs/2511.10056v1) | 2511.10056v1 | 9 |
| 2025-11-12 | [Contextual morphologically-guided tokenization for Latin encoder models](https://arxiv.org/abs/2511.09709v1) | 2511.09709v1 | 6 |
| 2025-11-11 | [From IDs to Semantics: A Generative Framework for Cross-Domain Recommendation with Adaptive Semantic Tokenization](https://arxiv.org/abs/2511.08006v2) | 2511.08006v2 | 8 |
| 2025-11-10 | [CAE: Character-Level Autoencoder for Non-Semantic Relational Data Grouping](https://arxiv.org/abs/2511.07657v1) | 2511.07657v1 | 6 |
| 2025-11-10 | [VAEVQ: Enhancing Discrete Visual Tokenization through Variational Modeling](https://arxiv.org/abs/2511.06863v1) | 2511.06863v1 | 6 |
| 2025-11-10 | [CAST-LUT: Tokenizer-Guided HSV Look-Up Tables for Purple Flare Removal](https://arxiv.org/abs/2511.06764v2) | 2511.06764v2 | 6 |
| 2025-11-07 | [Evaluating Subword Tokenization Techniques for Bengali: A Benchmark Study with BengaliBPE](https://arxiv.org/abs/2511.05324v1) | 2511.05324v1 | 19 |
| 2025-11-07 | [LoPT: Lossless Parallel Tokenization Acceleration for Long Context Inference of Large Language Model](https://arxiv.org/abs/2511.04952v1) | 2511.04952v1 | 6 |
| 2025-11-06 | [Small Vocabularies, Big Gains: Pretraining and Tokenization in Time Series Models](https://arxiv.org/abs/2511.11622v1) | 2511.11622v1 | 12 |
| 2025-11-05 | [How Different Tokenization Algorithms Impact LLMs and Transformer Models for Binary Code Analysis](https://arxiv.org/abs/2511.03825v1) | 2511.03825v1 | 12 |
| 2025-11-05 | [Segmentation Beyond Defaults: Asymmetrical Byte Pair Encoding for Optimal Machine Translation Performance](https://arxiv.org/abs/2511.03383v2) | 2511.03383v2 | 6 |
| 2025-11-05 | [MUTANT: A Recipe for Multilingual Tokenizer Design](https://arxiv.org/abs/2511.03237v2) | 2511.03237v2 | 18 |
| 2025-11-05 | [UTF-8 Plumbing: Byte-level Tokenizers Unavoidably Enable LLMs to Generate Ill-formed UTF-8](https://arxiv.org/abs/2511.05578v1) | 2511.05578v1 | 22 |
| 2025-11-04 | [AgriTrust: a Federated Semantic Governance Framework for Trusted Agricultural Data Sharing](https://arxiv.org/abs/2511.05572v1) | 2511.05572v1 | 6 |
| 2025-11-04 | [Differentiable Hierarchical Visual Tokenization](https://arxiv.org/abs/2511.02652v1) | 2511.02652v1 | 12 |
| 2025-11-03 | [Wave-Particle (Continuous-Discrete) Dualistic Visual Tokenization for Unified Understanding and Generation](https://arxiv.org/abs/2511.01593v1) | 2511.01593v1 | 10 |
| 2025-11-03 | [Fast, memory-efficient genomic interval tokenizers for modern machine learning](https://arxiv.org/abs/2511.01555v1) | 2511.01555v1 | 12 |
| 2025-10-31 | [Languages are Modalities: Cross-Lingual Alignment via Encoder Injection](https://arxiv.org/abs/2510.27254v1) | 2510.27254v1 | 9 |
| 2025-10-30 | [Spiking Patches: Asynchronous, Sparse, and Efficient Tokens for Event Cameras](https://arxiv.org/abs/2510.26614v2) | 2510.26614v2 | 11 |
| 2025-10-30 | [Broken-Token: Filtering Obfuscated Prompts by Counting Characters-Per-Token](https://arxiv.org/abs/2510.26847v1) | 2510.26847v1 | 8 |
| 2025-10-29 | [Modular Linear Tokenization (MLT)](https://arxiv.org/abs/2510.25952v1) | 2510.25952v1 | 7 |
| 2025-10-28 | [Resi-VidTok: An Efficient and Decomposed Progressive Tokenization Framework for Ultra-Low-Rate and Lightweight Video Transmission](https://arxiv.org/abs/2510.25002v1) | 2510.25002v1 | 6 |
| 2025-10-28 | [Open Korean Historical Corpus: A Millennia-Scale Diachronic Collection of Public Domain Texts](https://arxiv.org/abs/2510.24541v2) | 2510.24541v2 | 6 |
| 2025-10-27 | [Lost in Tokenization: Context as the Key to Unlocking Biomolecular Understanding in Scientific LLMs](https://arxiv.org/abs/2510.23127v2) | 2510.23127v2 | 6 |
| 2025-10-27 | [Measuring Teaching with LLMs](https://arxiv.org/abs/2510.22968v1) | 2510.22968v1 | 9 |
| 2025-10-26 | [Transformers from Compressed Representations](https://arxiv.org/abs/2510.23665v2) | 2510.23665v2 | 8 |
| 2025-10-26 | [Contextual Tokenization for Graph Inverted Indices](https://arxiv.org/abs/2510.22479v2) | 2510.22479v2 | 8 |
| 2025-10-25 | [FOA Tokenizer: Low-bitrate Neural Codec for First Order Ambisonics with Spatial Consistency Loss](https://arxiv.org/abs/2510.22241v1) | 2510.22241v1 | 6 |
| 2025-10-24 | [Model-Aware Tokenizer Transfer](https://arxiv.org/abs/2510.21954v2) | 2510.21954v2 | 7 |
| 2025-10-24 | [Explaining and Mitigating Crosslingual Tokenizer Inequities](https://arxiv.org/abs/2510.21909v1) | 2510.21909v1 | 12 |
| 2025-10-24 | [HalleluBERT: Let Every Token That Has Meaning Bear Its Weight](https://arxiv.org/abs/2510.21372v2) | 2510.21372v2 | 12 |
| 2025-10-24 | [Pctx: Tokenizing Personalized Context for Generative Recommendation](https://arxiv.org/abs/2510.21276v1) | 2510.21276v1 | 8 |
| 2025-10-24 | [Bi-Level Optimization for Generative Recommendation: Bridging Tokenization and Generation](https://arxiv.org/abs/2510.21242v2) | 2510.21242v2 | 10 |
| 2025-10-23 | [Decoding-Free Sampling Strategies for LLM Marginalization](https://arxiv.org/abs/2510.20208v1) | 2510.20208v1 | 14 |
| 2025-10-22 | [Beyond Hearing: Learning Task-Agnostic ExG Representations from Earphones via Physiology-Informed Tokenization](https://arxiv.org/abs/2510.20853v2) | 2510.20853v2 | 6 |
| 2025-10-21 | [See the Text: From Tokenization to Visual Reading](https://arxiv.org/abs/2510.18840v2) | 2510.18840v2 | 16 |
| 2025-10-21 | [VFM-VAE: Vision Foundation Models Can Be Good Tokenizers for Latent Diffusion Models](https://arxiv.org/abs/2510.18457v3) | 2510.18457v3 | 6 |
| 2025-10-21 | [DiffGRM: Diffusion-based Generative Recommendation Model](https://arxiv.org/abs/2510.21805v2) | 2510.21805v2 | 8 |
| 2025-10-20 | [Is Multilingual LLM Watermarking Truly Multilingual? Scaling Robustness to 100+ Languages via Back-Translation](https://arxiv.org/abs/2510.18019v3) | 2510.18019v3 | 6 |
| 2025-10-20 | [Universal Spectral Tokenization via Self-Supervised Panchromatic Representation Learning](https://arxiv.org/abs/2510.17959v2) | 2510.17959v2 | 10 |
| 2025-10-20 | [AION-1: Omnimodal Foundation Model for Astronomical Sciences](https://arxiv.org/abs/2510.17960v1) | 2510.17960v1 | 8 |
| 2025-10-19 | [Vocab Diet: Reshaping the Vocabulary of LLMs via Vector Arithmetic](https://arxiv.org/abs/2510.17001v2) | 2510.17001v2 | 8 |
| 2025-10-19 | [Back to Bytes: Revisiting Tokenization Through UTF-8](https://arxiv.org/abs/2510.16987v1) | 2510.16987v1 | 15 |
| 2025-10-18 | [MuseTok: Symbolic Music Tokenization for Generation and Semantic Understanding](https://arxiv.org/abs/2510.16273v1) | 2510.16273v1 | 6 |
| 2025-10-17 | [From Characters to Tokens: Dynamic Grouping with Hierarchical BPE](https://arxiv.org/abs/2510.15517v1) | 2510.15517v1 | 18 |
| 2025-10-17 | [LongCat-Audio-Codec: An Audio Tokenizer and Detokenizer Solution Designed for Speech Large Language Models](https://arxiv.org/abs/2510.15227v1) | 2510.15227v1 | 6 |
| 2025-10-16 | [TokDrift: When LLM Speaks in Subwords but Code Speaks in Grammar](https://arxiv.org/abs/2510.14972v1) | 2510.14972v1 | 17 |
| 2025-10-16 | [Understanding the Ability of LLMs to Handle Character-Level Perturbation](https://arxiv.org/abs/2510.14365v4) | 2510.14365v4 | 7 |
| 2025-10-15 | [NeuroRVQ: Multi-Scale Biosignal Tokenization for Generative Foundation Models](https://arxiv.org/abs/2510.13068v4) | 2510.13068v4 | 10 |
| 2025-10-14 | [IP-Augmented Multi-Modal Malicious URL Detection Via Token-Contrastive Representation Enhancement and Multi-Granularity Fusion](https://arxiv.org/abs/2510.12395v1) | 2510.12395v1 | 7 |
| 2025-10-14 | [Tokenization Disparities as Infrastructure Bias: How Subword Systems Create Inequities in LLM Access and Efficiency](https://arxiv.org/abs/2510.12389v1) | 2510.12389v1 | 14 |
| 2025-10-14 | [A Hierarchical Quantized Tokenization Framework for Task-Adaptive Graph Representation Learning](https://arxiv.org/abs/2510.12369v4) | 2510.12369v4 | 10 |
| 2025-10-14 | [Chinese ModernBERT with Whole-Word Masking](https://arxiv.org/abs/2510.12285v1) | 2510.12285v1 | 13 |
| 2025-10-12 | [Happiness is Sharing a Vocabulary: A Study of Transliteration Methods](https://arxiv.org/abs/2510.10827v2) | 2510.10827v2 | 7 |
| 2025-10-12 | [UniFlow: A Unified Pixel Flow Tokenizer for Visual Understanding and Generation](https://arxiv.org/abs/2510.10575v2) | 2510.10575v2 | 8 |
| 2025-10-11 | [PANTHER: Generative Pretraining Beyond Language for Sequential User Behavior Modeling](https://arxiv.org/abs/2510.10102v2) | 2510.10102v2 | 7 |
| 2025-10-11 | [Beyond Fertility: Analyzing STRR as a Metric for Multilingual Tokenization Evaluation](https://arxiv.org/abs/2510.09947v2) | 2510.09947v2 | 10 |
| 2025-10-10 | [Neural Codecs as Biosignal Tokenizers](https://arxiv.org/abs/2510.09095v1) | 2510.09095v1 | 11 |
| 2025-10-10 | [ReaLM: Residual Quantization Bridging Knowledge Graph Embeddings and Large Language Models](https://arxiv.org/abs/2510.09711v2) | 2510.09711v2 | 7 |
| 2025-10-09 | [Lossless Vocabulary Reduction for Auto-Regressive Language Models](https://arxiv.org/abs/2510.08102v2) | 2510.08102v2 | 11 |
| 2025-10-08 | [OmniSAT: Compact Action Token, Faster Auto Regression](https://arxiv.org/abs/2510.09667v1) | 2510.09667v1 | 8 |
| 2025-10-08 | [Ming-UniVision: Joint Image Understanding and Generation with a Unified Continuous Tokenizer](https://arxiv.org/abs/2510.06590v1) | 2510.06590v1 | 10 |
| 2025-10-07 | [Linguistically Informed Tokenization Improves ASR for Underresourced Languages](https://arxiv.org/abs/2510.06461v1) | 2510.06461v1 | 6 |
| 2025-10-07 | [Parallel Tokenizers: Rethinking Vocabulary Design in Cross-Lingual Transfer of Low-Resource Languages](https://arxiv.org/abs/2510.06128v3) | 2510.06128v3 | 14 |
| 2025-10-07 | [Membership Inference Attacks on Tokenizers of Large Language Models](https://arxiv.org/abs/2510.05699v4) | 2510.05699v4 | 6 |
| 2025-10-07 | [Context Matters: Learning Global Semantics via Object-Centric Representation](https://arxiv.org/abs/2510.05674v2) | 2510.05674v2 | 6 |
| 2025-10-06 | [SSDD: Single-Step Diffusion Decoder for Efficient Image Tokenization](https://arxiv.org/abs/2510.04961v2) | 2510.04961v2 | 10 |
| 2025-10-06 | [REAR: Rethinking Visual Autoregressive Models via Generator-Tokenizer Consistency Regularization](https://arxiv.org/abs/2510.04450v1) | 2510.04450v1 | 7 |
| 2025-10-02 | [MelTok: 2D Tokenization for Single-Codebook Audio Compression](https://arxiv.org/abs/2510.01903v3) | 2510.01903v3 | 10 |
| 2025-09-30 | [Flow Autoencoders are Effective Protein Tokenizers](https://arxiv.org/abs/2510.00351v1) | 2510.00351v1 | 10 |
| 2025-09-30 | [BigBang-Proton Technical Report: Next-Word-Prediction is Scientific Multitask Learner](https://arxiv.org/abs/2510.00129v1) | 2510.00129v1 | 8 |
| 2025-09-30 | [Scaling Spoken Language Models with Syllabic Speech Tokenization](https://arxiv.org/abs/2509.26634v2) | 2509.26634v2 | 6 |
| 2025-09-30 | [Event Tokenization and Masked-Token Prediction for Anomaly Detection at the Large Hadron Collider](https://arxiv.org/abs/2509.26218v2) | 2509.26218v2 | 6 |
| 2025-09-30 | [VietBinoculars: A Zero-Shot Approach for Detecting Vietnamese LLM-Generated Text](https://arxiv.org/abs/2509.26189v2) | 2509.26189v2 | 10 |
| 2025-09-30 | [Vocabulary Customization for Efficient Domain-Specific LLM Deployment](https://arxiv.org/abs/2509.26124v1) | 2509.26124v1 | 11 |
| 2025-09-30 | [Kairos: Toward Adaptive and Parameter-Efficient Time Series Foundation Models](https://arxiv.org/abs/2509.25826v4) | 2509.25826v4 | 11 |
| 2025-09-29 | [AlignTok: Aligning Visual Foundation Encoders to Tokenizers for Diffusion Models](https://arxiv.org/abs/2509.25162v2) | 2509.25162v2 | 6 |
| 2025-09-29 | [VoxCPM: Tokenizer-Free TTS for Context-Aware Speech Generation and True-to-Life Voice Cloning](https://arxiv.org/abs/2509.24650v1) | 2509.24650v1 | 6 |
| 2025-09-28 | [DNABERT-2: Fine-Tuning a Genomic Language Model for Colorectal Gene Enhancer Classification](https://arxiv.org/abs/2509.25274v1) | 2509.25274v1 | 8 |
| 2025-09-28 | [HieraTok: Multi-Scale Visual Tokenizer Improves Image Reconstruction and Generation](https://arxiv.org/abs/2509.23736v1) | 2509.23736v1 | 6 |
| 2025-09-28 | [Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action models](https://arxiv.org/abs/2509.23655v1) | 2509.23655v1 | 6 |
| 2025-09-27 | [RHYTHM: Reasoning with Hierarchical Temporal Tokenization for Human Mobility](https://arxiv.org/abs/2509.23115v3) | 2509.23115v3 | 7 |
| 2025-09-26 | [GaussianVision: Vision-Language Alignment from Compressed Image Representations using 2D Gaussian Splatting](https://arxiv.org/abs/2509.22615v2) | 2509.22615v2 | 6 |
| 2025-09-26 | [StableToken: A Noise-Robust Semantic Speech Tokenizer for Resilient SpeechLLMs](https://arxiv.org/abs/2509.22220v2) | 2509.22220v2 | 6 |
| 2025-09-26 | [A High-Capacity and Secure Disambiguation Algorithm for Neural Linguistic Steganography](https://arxiv.org/abs/2510.02332v1) | 2510.02332v1 | 9 |
| 2025-09-25 | [WAVECLIP: Wavelet Tokenization for Adaptive-Resolution CLIP](https://arxiv.org/abs/2509.21153v1) | 2509.21153v1 | 9 |
| 2025-09-25 | [CAD-Tokenizer: Towards Text-based CAD Prototyping via Modality-Specific Tokenization](https://arxiv.org/abs/2509.21150v2) | 2509.21150v2 | 12 |
| 2025-09-24 | [Low-Resource English-Tigrinya MT: Leveraging Multilingual Models, Custom Tokenizers, and Clean Evaluation Benchmarks](https://arxiv.org/abs/2509.20209v1) | 2509.20209v1 | 11 |
| 2025-09-24 | [Tokenization and Representation Biases in Multilingual Models on Dialectal NLP Tasks](https://arxiv.org/abs/2509.20045v1) | 2509.20045v1 | 12 |
| 2025-09-23 | [Adversarially-Refined VQ-GAN with Dense Motion Tokenization for Spatio-Temporal Heatmaps](https://arxiv.org/abs/2509.19252v1) | 2509.19252v1 | 8 |
| 2025-09-23 | [Computational Social Linguistics for Telugu Cultural Preservation: Novel Algorithms for Chandassu Metrical Pattern Recognition](https://arxiv.org/abs/2510.01233v2) | 2510.01233v2 | 8 |
| 2025-09-23 | [False Friends Are Not Foes: Investigating Vocabulary Overlap in Multilingual Language Models](https://arxiv.org/abs/2509.18750v2) | 2509.18750v2 | 12 |
| 2025-09-22 | [GraDeT-HTR: A Resource-Efficient Bengali Handwritten Text Recognition System utilizing Grapheme-based Tokenizer and Decoder-only Transformer](https://arxiv.org/abs/2509.18081v1) | 2509.18081v1 | 10 |
| 2025-09-22 | [MLLM-Driven Semantic Identifier Generation for Generative Cross-Modal Retrieval](https://arxiv.org/abs/2509.17359v2) | 2509.17359v2 | 6 |
| 2025-09-21 | [TSGym: Design Choices for Deep Multivariate Time-Series Forecasting](https://arxiv.org/abs/2509.17063v1) | 2509.17063v1 | 6 |
| 2025-09-20 | [Domain-Adaptive Pre-Training for Arabic Aspect-Based Sentiment Analysis: A Comparative Study of Domain Adaptation and Fine-Tuning Strategies](https://arxiv.org/abs/2509.16788v1) | 2509.16788v1 | 8 |
| 2025-09-19 | [MANZANO: A Simple and Scalable Unified Multimodal Model with a Hybrid Vision Tokenizer](https://arxiv.org/abs/2509.16197v1) | 2509.16197v1 | 7 |
| 2025-09-18 | [OpenViGA: Video Generation for Automotive Driving Scenes by Streamlining and Fine-Tuning Open Source Models with Public Data](https://arxiv.org/abs/2509.15479v1) | 2509.15479v1 | 8 |
| 2025-09-18 | [Mind the Gap: A Closer Look at Tokenization for Multiple-Choice Question Answering with LLMs](https://arxiv.org/abs/2509.15020v1) | 2509.15020v1 | 6 |
| 2025-09-18 | [Comparative Analysis of Tokenization Algorithms for Low-Resource Language Dzongkha](https://arxiv.org/abs/2509.15255v1) | 2509.15255v1 | 16 |
| 2025-09-17 | [Dense Video Understanding with Gated Residual Tokenization](https://arxiv.org/abs/2509.14199v2) | 2509.14199v2 | 6 |
| 2025-09-17 | [Re-purposing SAM into Efficient Visual Projectors for MLLM-Based Referring Image Segmentation](https://arxiv.org/abs/2509.13676v1) | 2509.13676v1 | 7 |
| 2025-09-16 | [Efficient Cold-Start Recommendation via BPE Token-Level Embedding Initialization with LLM](https://arxiv.org/abs/2509.13179v1) | 2509.13179v1 | 14 |
| 2025-09-16 | [WLFM: A Well-Logs Foundation Model for Multi-Task and Cross-Well Geological Interpretation](https://arxiv.org/abs/2509.18152v1) | 2509.18152v1 | 8 |
| 2025-09-15 | [Image Tokenizer Needs Post-Training](https://arxiv.org/abs/2509.12474v1) | 2509.12474v1 | 6 |
| 2025-09-15 | [Knowledge Graph Tokenization for Behavior-Aware Generative Next POI Recommendation](https://arxiv.org/abs/2509.12350v1) | 2509.12350v1 | 10 |
| 2025-09-14 | [FuseCodec: Semantic-Contextual Fusion and Supervision for Neural Codecs](https://arxiv.org/abs/2509.11425v2) | 2509.11425v2 | 8 |
| 2025-09-12 | [URL2Graph++: Unified Semantic-Structural-Character Learning for Malicious URL Detection](https://arxiv.org/abs/2509.10287v1) | 2509.10287v1 | 7 |
| 2025-09-11 | [Character-Level Perturbations Disrupt LLM Watermarks](https://arxiv.org/abs/2509.09112v2) | 2509.09112v2 | 7 |
| 2025-09-10 | [MoVoC: Morphology-Aware Subword Construction for Geez Script Languages Corrected version](https://arxiv.org/abs/2509.08812v2) | 2509.08812v2 | 18 |
| 2025-09-08 | [H$_{2}$OT: Hierarchical Hourglass Tokenizer for Efficient Video Pose Transformers](https://arxiv.org/abs/2509.06956v1) | 2509.06956v1 | 6 |
| 2025-09-06 | [Leveraging Vision-Language Large Models for Interpretable Video Action Recognition with Semantic Tokenization](https://arxiv.org/abs/2509.05695v1) | 2509.05695v1 | 6 |
| 2025-09-05 | [The Token Tax: Systematic Bias in Multilingual Tokenization](https://arxiv.org/abs/2509.05486v1) | 2509.05486v1 | 6 |
| 2025-09-04 | [Say More with Less: Variable-Frame-Rate Speech Tokenization via Adaptive Clustering and Implicit Duration Coding](https://arxiv.org/abs/2509.04685v3) | 2509.04685v3 | 10 |
| 2025-09-03 | [RecBase: Generative Foundation Model Pretraining for Zero-Shot Recommendation](https://arxiv.org/abs/2509.03131v1) | 2509.03131v1 | 6 |
| 2025-09-01 | [chDzDT: Word-level morphology-aware language model for Algerian social media text](https://arxiv.org/abs/2509.01772v1) | 2509.01772v1 | 10 |
| 2025-09-01 | [GPSToken: Gaussian Parameterized Spatially-adaptive Tokenization for Image Representation and Generation](https://arxiv.org/abs/2509.01109v2) | 2509.01109v2 | 6 |
| 2025-08-31 | [ASCENDgpt: A Phenotype-Aware Transformer Model for Cardiovascular Risk Prediction from Electronic Health Records](https://arxiv.org/abs/2509.04485v1) | 2509.04485v1 | 6 |
| 2025-08-30 | [Training Text-to-Molecule Models with Context-Aware Tokenization](https://arxiv.org/abs/2509.04476v2) | 2509.04476v2 | 6 |
| 2025-08-28 | [Enhancing Robustness of Autoregressive Language Models against Orthographic Attacks via Pixel-based Approach](https://arxiv.org/abs/2508.21206v1) | 2508.21206v1 | 11 |
| 2025-08-28 | [Addressing Tokenization Inconsistency in Steganography and Watermarking Based on Large Language Models](https://arxiv.org/abs/2508.20718v1) | 2508.20718v1 | 6 |
| 2025-08-27 | [Tokenization Strategies for Low-Resource Agglutinative Languages in Word2Vec: Case Study on Turkish and Finnish](https://arxiv.org/abs/2509.14238v1) | 2509.14238v1 | 15 |
| 2025-08-22 | [TaDiCodec: Text-aware Diffusion Speech Tokenizer for Speech Language Modeling](https://arxiv.org/abs/2508.16790v1) | 2508.16790v1 | 6 |
| 2025-08-22 | [Learning Decomposed Contextual Token Representations from Pretrained and Collaborative Signals for Generative Recommendation](https://arxiv.org/abs/2509.10468v2) | 2509.10468v2 | 9 |
| 2025-08-21 | [Exploiting Vocabulary Frequency Imbalance in Language Model Pre-training](https://arxiv.org/abs/2508.15390v3) | 2508.15390v3 | 7 |
| 2025-08-21 | [HeartLLM: Discretized ECG Tokenization for LLM-Based Diagnostic Reasoning](https://arxiv.org/abs/2508.15338v2) | 2508.15338v2 | 9 |
| 2025-08-21 | [MMQ: Multimodal Mixture-of-Quantization Tokenization for Semantic ID Generation and User Behavioral Adaptation](https://arxiv.org/abs/2508.15281v1) | 2508.15281v1 | 10 |
| 2025-08-21 | [SemToken: Semantic-Aware Tokenization for Efficient Long-Context Language Modeling](https://arxiv.org/abs/2508.15190v1) | 2508.15190v1 | 9 |
| 2025-08-20 | [The Digital Sous Chef -- A Comparative Study on Fine-Tuning Language Models for Recipe Generation](https://arxiv.org/abs/2508.14718v1) | 2508.14718v1 | 10 |
| 2025-08-19 | [Tokens with Meaning: A Hybrid Tokenization Approach for Turkish](https://arxiv.org/abs/2508.14292v3) | 2508.14292v3 | 17 |
| 2025-08-19 | [2D Gaussians Meet Visual Tokenizer](https://arxiv.org/abs/2508.13515v2) | 2508.13515v2 | 8 |
| 2025-08-18 | [Doğal Dil İşlemede Tokenizasyon Standartları ve Ölçümü: Türkçe Üzerinden Büyük Dil Modellerinin Karşılaştırmalı Analizi](https://arxiv.org/abs/2508.13058v1) | 2508.13058v1 | 10 |
| 2025-08-16 | [QuickMerge++: Fast Token Merging with Autoregressive Prior](https://arxiv.org/abs/2508.13204v1) | 2508.13204v1 | 6 |
| 2025-08-16 | [SupraTok: Cross-Boundary Tokenization for Enhanced Language Model Performance](https://arxiv.org/abs/2508.11857v3) | 2508.11857v3 | 14 |
| 2025-08-15 | [Versatile Video Representation via Feed-Forward 2D Gaussian Splatting Tokenization](https://arxiv.org/abs/2508.11183v2) | 2508.11183v2 | 9 |
| 2025-08-14 | [Vocabulary Expansion of Large Language Models via Kullback-Leibler-Based Self-Distillation](https://arxiv.org/abs/2508.15807v2) | 2508.15807v2 | 8 |
| 2025-08-14 | [BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model](https://arxiv.org/abs/2508.10327v2) | 2508.10327v2 | 8 |
| 2025-08-13 | [Specialised or Generic? Tokenization Choices for Radiology Language Models](https://arxiv.org/abs/2508.09952v1) | 2508.09952v1 | 12 |
| 2025-08-12 | [SinLlama -- A Large Language Model for Sinhala](https://arxiv.org/abs/2508.09115v5) | 2508.09115v5 | 6 |
| 2025-08-12 | [Closing the Performance Gap in Generative Recommenders with Collaborative Tokenization and Efficient Modeling](https://arxiv.org/abs/2508.14910v1) | 2508.14910v1 | 6 |
| 2025-08-12 | [DualSpeechLM: Towards Unified Speech Understanding and Generation via Dual Speech Token Modeling with Large Language Models](https://arxiv.org/abs/2508.08961v3) | 2508.08961v3 | 8 |
| 2025-08-12 | [Classifier Language Models: Unifying Sparse Finetuning and Adaptive Tokenization for Specialized Classification Tasks](https://arxiv.org/abs/2508.08635v1) | 2508.08635v1 | 6 |
| 2025-08-11 | [Rethinking Tokenization for Rich Morphology: The Dominance of Unigram over BPE and Morphological Alignment](https://arxiv.org/abs/2508.08424v3) | 2508.08424v3 | 13 |
| 2025-08-08 | [Train It and Forget It: Merge Lists are Unnecessary for BPE Inference in Language Models](https://arxiv.org/abs/2508.06621v1) | 2508.06621v1 | 9 |
| 2025-08-07 | [H-Net++: Hierarchical Dynamic Chunking for Tokenizer-Free Language Modelling in Morphologically-Rich Languages](https://arxiv.org/abs/2508.05628v1) | 2508.05628v1 | 12 |
| 2025-08-07 | [WeTok: Powerful Discrete Tokenization for High-Fidelity Visual Reconstruction](https://arxiv.org/abs/2508.05599v3) | 2508.05599v3 | 10 |
| 2025-08-06 | [Parity-Aware Byte-Pair Encoding: Improving Cross-lingual Fairness in Tokenization](https://arxiv.org/abs/2508.04796v3) | 2508.04796v3 | 12 |
| 2025-08-04 | [CharBench: Evaluating the Role of Tokenization in Character-Level Tasks](https://arxiv.org/abs/2508.02591v3) | 2508.02591v3 | 13 |
| 2025-08-04 | [SoK: Stablecoins for Digital Transformation -- Design, Metrics, and Application with Real World Asset Tokenization as a Case Study](https://arxiv.org/abs/2508.02403v1) | 2508.02403v1 | 6 |
| 2025-08-04 | [ByteGen: A Tokenizer-Free Generative Model for Orderbook Events in Byte Space](https://arxiv.org/abs/2508.02247v2) | 2508.02247v2 | 14 |
| 2025-08-03 | [The Art of Breaking Words: Rethinking Multilingual Tokenizer Design](https://arxiv.org/abs/2508.06533v1) | 2508.06533v1 | 12 |
| 2025-08-03 | [Innovative tokenisation of structured data for LLM training](https://arxiv.org/abs/2508.01685v1) | 2508.01685v1 | 8 |
| 2025-08-01 | [FOUNDv2: Learning Unified User Quantized Tokenizers for User Representation](https://arxiv.org/abs/2508.00956v3) | 2508.00956v3 | 7 |
| 2025-07-31 | [Script Fragmentation and Format: What Drives the English-Bengali Performance Gap in Open LLMs?](https://arxiv.org/abs/2507.23248v2) | 2507.23248v2 | 10 |
| 2025-07-31 | [Efficient Real-Time Aircraft ETA Prediction via Feature Tokenization Transformer](https://arxiv.org/abs/2508.09144v1) | 2508.09144v1 | 6 |
| 2025-07-30 | [Pre-trained Models Perform the Best When Token Distributions Follow Zipf's Law](https://arxiv.org/abs/2507.22543v1) | 2507.22543v1 | 6 |
| 2025-07-24 | [Hybrid Tokenization Strategy for DNA Language Model using Byte Pair Encoding and K-MER Methods](https://arxiv.org/abs/2507.18570v1) | 2507.18570v1 | 10 |
| 2025-07-24 | [Sticking to the Mean: Detecting Sticky Tokens in Text Embedding Models](https://arxiv.org/abs/2507.18171v1) | 2507.18171v1 | 11 |
| 2025-07-21 | [Latent Denoising Makes Good Tokenizers](https://arxiv.org/abs/2507.15856v2) | 2507.15856v2 | 7 |
| 2025-07-21 | [Look, Focus, Act: Efficient and Robust Robot Learning via Human Gaze and Foveated Vision Transformers](https://arxiv.org/abs/2507.15833v3) | 2507.15833v3 | 6 |
| 2025-07-21 | [Discrete Tokenization for Multimodal LLMs: A Comprehensive Survey](https://arxiv.org/abs/2507.22920v2) | 2507.22920v2 | 6 |
| 2025-07-19 | [What do Large Language Models know about materials?](https://arxiv.org/abs/2507.14586v1) | 2507.14586v1 | 6 |
| 2025-07-19 | [On the Effect of Token Merging on Pre-trained Models for Code](https://arxiv.org/abs/2507.14423v1) | 2507.14423v1 | 8 |
| 2025-07-18 | [Efficient Temporal Tokenization for Mobility Prediction with Large Language Models](https://arxiv.org/abs/2507.14017v1) | 2507.14017v1 | 7 |
| 2025-07-18 | [Learning Deformable Body Interactions With Adaptive Spatial Tokenization](https://arxiv.org/abs/2507.13707v1) | 2507.13707v1 | 7 |
| 2025-07-17 | [Synergy: End-to-end Concept Model](https://arxiv.org/abs/2507.12769v1) | 2507.12769v1 | 10 |
| 2025-07-17 | [FLEXITOKENS: Flexible Tokenization for Evolving Language Models](https://arxiv.org/abs/2507.12720v4) | 2507.12720v4 | 20 |
| 2025-07-16 | [PARAM-1 BharatGen 2.9B Model](https://arxiv.org/abs/2507.13390v1) | 2507.13390v1 | 9 |
| 2025-07-16 | [BlockBPE: Parallel BPE Tokenization](https://arxiv.org/abs/2507.11941v1) | 2507.11941v1 | 13 |
| 2025-07-13 | [VDInstruct: Zero-Shot Key Information Extraction via Content-Aware Vision Tokenization](https://arxiv.org/abs/2507.09531v1) | 2507.09531v1 | 6 |
| 2025-07-12 | [Overtone: Cyclic Patch Modulation for Clean, Efficient, and Flexible Physics Emulators](https://arxiv.org/abs/2507.09264v2) | 2507.09264v2 | 7 |
| 2025-07-12 | [$I^{2}$-World: Intra-Inter Tokenization for Efficient Dynamic 4D Scene Forecasting](https://arxiv.org/abs/2507.09144v2) | 2507.09144v2 | 10 |
| 2025-07-11 | [Vision Foundation Models as Effective Visual Tokenizers for Autoregressive Image Generation](https://arxiv.org/abs/2507.08441v2) | 2507.08441v2 | 6 |
| 2025-07-10 | [MGVQ: Could VQ-VAE Beat VAE? A Generalizable Tokenizer with Multi-group Quantization](https://arxiv.org/abs/2507.07997v2) | 2507.07997v2 | 6 |
| 2025-07-10 | [Single-pass Adaptive Image Tokenization for Minimum Program Search](https://arxiv.org/abs/2507.07995v1) | 2507.07995v1 | 10 |
| 2025-07-10 | [Dynamic Chunking for End-to-End Hierarchical Sequence Modeling](https://arxiv.org/abs/2507.07955v2) | 2507.07955v2 | 8 |
| 2025-07-10 | [Conditional Unigram Tokenization with Parallel Data](https://arxiv.org/abs/2507.07824v1) | 2507.07824v1 | 12 |
| 2025-07-09 | [Speech Tokenizer is Key to Consistent Representation](https://arxiv.org/abs/2507.06802v1) | 2507.06802v1 | 10 |
| 2025-07-08 | [Evaluating Morphological Alignment of Tokenizers in 70 Languages](https://arxiv.org/abs/2507.06378v1) | 2507.06378v1 | 14 |
| 2025-07-08 | [DS@GT at CheckThat! 2025: Evaluating Context and Tokenization Strategies for Numerical Fact Verification](https://arxiv.org/abs/2507.06195v1) | 2507.06195v1 | 6 |
| 2025-07-07 | [DC-AR: Efficient Masked Autoregressive Image Generation with Deep Compression Hybrid Tokenizer](https://arxiv.org/abs/2507.04947v1) | 2507.04947v1 | 6 |
| 2025-07-03 | [RefTok: Reference-Based Tokenization for Video Generation](https://arxiv.org/abs/2507.02862v1) | 2507.02862v1 | 10 |
| 2025-07-03 | [Hita: Holistic Tokenizer for Autoregressive Image Generation](https://arxiv.org/abs/2507.02358v4) | 2507.02358v4 | 12 |
| 2025-07-02 | [A Survey on Vision-Language-Action Models: An Action Tokenization Perspective](https://arxiv.org/abs/2507.01925v1) | 2507.01925v1 | 6 |
| 2025-07-02 | [SPoT: Subpixel Placement of Tokens in Vision Transformers](https://arxiv.org/abs/2507.01654v2) | 2507.01654v2 | 6 |
| 2025-07-02 | [Adapting Language Models to Indonesian Local Languages: An Empirical Study of Language Transferability on Zero-Shot Settings](https://arxiv.org/abs/2507.01645v1) | 2507.01645v1 | 10 |
| 2025-07-01 | [VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://arxiv.org/abs/2507.01016v1) | 2507.01016v1 | 6 |
| 2025-06-30 | [$μ^2$Tokenizer: Differentiable Multi-Scale Multi-Modal Tokenizer for Radiology Report Generation](https://arxiv.org/abs/2507.00316v2) | 2507.00316v2 | 6 |
| 2025-06-30 | [AI-Governed Agent Architecture for Web-Trustworthy Tokenization of Alternative Assets](https://arxiv.org/abs/2507.00096v1) | 2507.00096v1 | 6 |
| 2025-06-29 | [XY-Tokenizer: Mitigating the Semantic-Acoustic Conflict in Low-Bitrate Speech Codecs](https://arxiv.org/abs/2506.23325v2) | 2506.23325v2 | 6 |
| 2025-06-29 | [Region-Aware Multimodal Large Language Model via SlowFast Tokenization and Pseudo-Mask Guidance for 3D CT Report Generation](https://arxiv.org/abs/2506.23102v3) | 2506.23102v3 | 10 |
| 2025-06-27 | [DiffSoundStream: Efficient Speech Tokenization via Diffusion Decoding](https://arxiv.org/abs/2506.22362v1) | 2506.22362v1 | 6 |
| 2025-06-25 | [scMamba: A Scalable Foundation Model for Single-Cell Multi-Omics Integration Beyond Highly Variable Feature Selection](https://arxiv.org/abs/2506.20697v1) | 2506.20697v1 | 6 |
| 2025-06-23 | [Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations](https://arxiv.org/abs/2506.19004v2) | 2506.19004v2 | 14 |
| 2025-06-23 | [Vision as a Dialect: Unifying Visual Understanding and Generation via Text-Aligned Representations](https://arxiv.org/abs/2506.18898v1) | 2506.18898v1 | 6 |
| 2025-06-23 | [Is There a Case for Conversation Optimized Tokenizers in Large Language Models?](https://arxiv.org/abs/2506.18674v1) | 2506.18674v1 | 10 |
| 2025-06-23 | [ByteSpan: Information-Driven Subword Tokenisation](https://arxiv.org/abs/2506.18639v1) | 2506.18639v1 | 16 |
| 2025-06-22 | [PlanMoGPT: Flow-Enhanced Progressive Planning for Text to Motion Synthesis](https://arxiv.org/abs/2506.17912v1) | 2506.17912v1 | 8 |
| 2025-06-21 | [Multilingual Tokenization through the Lens of Indian Languages: Challenges and Insights](https://arxiv.org/abs/2506.17789v3) | 2506.17789v3 | 18 |
| 2025-06-20 | [LM-SPT: LM-Aligned Semantic Distillation for Speech Tokenization](https://arxiv.org/abs/2506.16738v2) | 2506.16738v2 | 10 |
| 2025-06-20 | [A Simple Contrastive Framework Of Item Tokenization For Generative Recommendation](https://arxiv.org/abs/2506.16683v1) | 2506.16683v1 | 7 |
| 2025-06-19 | [Advanced Sign Language Video Generation with Compressed and Quantized Multi-Condition Tokenization](https://arxiv.org/abs/2506.15980v2) | 2506.15980v2 | 7 |
| 2025-06-18 | [Entropy-Driven Pre-Tokenization for Byte-Pair Encoding](https://arxiv.org/abs/2506.15889v1) | 2506.15889v1 | 12 |
| 2025-06-18 | [Architecture is All You Need: Improving LLM Recommenders by Dropping the Text](https://arxiv.org/abs/2506.15833v1) | 2506.15833v1 | 10 |
| 2025-06-18 | [Factorized RVQ-GAN For Disentangled Speech Tokenization](https://arxiv.org/abs/2506.15456v1) | 2506.15456v1 | 6 |
| 2025-06-18 | [Less Is More: Reducing Token Counts Without Compromising Performance](https://arxiv.org/abs/2506.15138v2) | 2506.15138v2 | 16 |
| 2025-06-17 | [From Bytes to Ideas: Language Modeling with Autoregressive U-Nets](https://arxiv.org/abs/2506.14761v1) | 2506.14761v1 | 10 |
| 2025-06-17 | [Sampling from Your Language Model One Byte at a Time](https://arxiv.org/abs/2506.14123v3) | 2506.14123v3 | 16 |
| 2025-06-15 | [DuoFormer: Leveraging Hierarchical Representations by Local and Global Attention Vision Transformer](https://arxiv.org/abs/2506.12982v1) | 2506.12982v1 | 6 |
| 2025-06-15 | [Forecasting Time Series with LLMs via Patch-Based Prompting and Decomposition](https://arxiv.org/abs/2506.12953v1) | 2506.12953v1 | 7 |
| 2025-06-14 | [What Makes a Good Speech Tokenizer for LLM-Centric Speech Generation? A Systematic Study](https://arxiv.org/abs/2506.12537v3) | 2506.12537v3 | 10 |
| 2025-06-13 | [Efficient Multi-Camera Tokenization with Triplanes for End-to-End Driving](https://arxiv.org/abs/2506.12251v2) | 2506.12251v2 | 8 |
| 2025-06-12 | [SpectralAR: Spectral Autoregressive Visual Generation](https://arxiv.org/abs/2506.10962v1) | 2506.10962v1 | 6 |
| 2025-06-12 | [One Tokenizer To Rule Them All: Emergent Language Plasticity via Multilingual Tokenizers](https://arxiv.org/abs/2506.10766v1) | 2506.10766v1 | 6 |
| 2025-06-12 | [Spelling-out is not Straightforward: LLMs' Capability of Tokenization from Token to Characters](https://arxiv.org/abs/2506.10641v1) | 2506.10641v1 | 9 |
| 2025-06-12 | [DART: Differentiable Dynamic Adaptive Region Tokenizer for Vision Foundation Models](https://arxiv.org/abs/2506.10390v4) | 2506.10390v4 | 12 |
| 2025-06-12 | [Discrete Audio Tokens: More Than a Survey!](https://arxiv.org/abs/2506.10274v3) | 2506.10274v3 | 8 |
| 2025-06-10 | [Segment This Thing: Foveated Tokenization for Efficient Point-Prompted Segmentation](https://arxiv.org/abs/2506.11131v1) | 2506.11131v1 | 8 |
| 2025-06-10 | [CodeBrain: Bridging Decoupled Tokenizer and Multi-Scale Architecture for EEG Foundation Model](https://arxiv.org/abs/2506.09110v4) | 2506.09110v4 | 6 |
| 2025-06-10 | [Towards Secure and Private Language Models for Nuclear Power Plants](https://arxiv.org/abs/2506.08746v1) | 2506.08746v1 | 6 |
| 2025-06-09 | [Highly Compressed Tokenizer Can Generate Without Training](https://arxiv.org/abs/2506.08257v1) | 2506.08257v1 | 6 |
| 2025-06-09 | [TokenBreak: Bypassing Text Classification Models Through Token Manipulation](https://arxiv.org/abs/2506.07948v1) | 2506.07948v1 | 8 |
| 2025-06-09 | [Event-Priori-Based Vision-Language Model for Efficient Visual Understanding](https://arxiv.org/abs/2506.07627v1) | 2506.07627v1 | 6 |
| 2025-06-09 | [Bit-level BPE: Below the byte boundary](https://arxiv.org/abs/2506.07541v1) | 2506.07541v1 | 15 |
| 2025-06-09 | [Incorporating Domain Knowledge into Materials Tokenization](https://arxiv.org/abs/2506.11115v1) | 2506.11115v1 | 6 |
| 2025-06-08 | [Enhancing Large Language Models for Mobility Analytics with Semantic Location Tokenization](https://arxiv.org/abs/2506.11109v1) | 2506.11109v1 | 6 |
| 2025-06-07 | [Training-Free Tokenizer Transplantation via Orthogonal Matching Pursuit](https://arxiv.org/abs/2506.06607v1) | 2506.06607v1 | 13 |
| 2025-06-06 | [Tokenization Multiplicity Leads to Arbitrary Price Variation in LLM-as-a-service](https://arxiv.org/abs/2506.06446v2) | 2506.06446v2 | 6 |
| 2025-06-06 | [Joint-GCG: Unified Gradient-Based Poisoning Attacks on Retrieval-Augmented Generation Systems](https://arxiv.org/abs/2506.06151v2) | 2506.06151v2 | 7 |
| 2025-06-06 | [BEAST: Efficient Tokenization of B-Splines Encoded Action Sequences for Imitation Learning](https://arxiv.org/abs/2506.06072v3) | 2506.06072v3 | 10 |
| 2025-06-05 | [Towards Sequence Modeling Alignment between Tokenizer and Autoregressive Model](https://arxiv.org/abs/2506.05289v3) | 2506.05289v3 | 10 |
| 2025-06-05 | [Multi-scale Image Super Resolution with a Single Auto-Regressive Model](https://arxiv.org/abs/2506.04990v1) | 2506.04990v1 | 8 |
| 2025-06-05 | [DualX-VSR: Dual Axial Spatial$\times$Temporal Transformer for Real-World Video Super-Resolution without Motion Compensation](https://arxiv.org/abs/2506.04830v2) | 2506.04830v2 | 6 |
| 2025-06-04 | [TokAlign: Efficient Vocabulary Adaptation via Token Alignment](https://arxiv.org/abs/2506.03523v1) | 2506.03523v1 | 12 |
| 2025-06-03 | [Beyond Text Compression: Evaluating Tokenizers Across Scales](https://arxiv.org/abs/2506.03101v1) | 2506.03101v1 | 6 |
| 2025-06-03 | [FuseLIP: Multimodal Embeddings via Early Fusion of Discrete Tokens](https://arxiv.org/abs/2506.03096v2) | 2506.03096v2 | 7 |
| 2025-06-02 | [StochasTok: Improving Fine-Grained Subword Understanding in LLMs](https://arxiv.org/abs/2506.01687v3) | 2506.01687v3 | 12 |
| 2025-06-02 | [Dictionaries to the Rescue: Cross-Lingual Vocabulary Transfer for Low-Resource Languages Using Bilingual Dictionaries](https://arxiv.org/abs/2506.01535v1) | 2506.01535v1 | 14 |
| 2025-06-01 | [zip2zip: Inference-Time Adaptive Tokenization via Online Compression](https://arxiv.org/abs/2506.01084v2) | 2506.01084v2 | 13 |
| 2025-06-01 | [CLAP-ART: Automated Audio Captioning with Semantic-rich Audio Representation Tokenizer](https://arxiv.org/abs/2506.00800v1) | 2506.00800v1 | 6 |
| 2025-05-30 | [BPE Stays on SCRIPT: Structured Encoding for Robust Multilingual Pretokenization](https://arxiv.org/abs/2505.24689v1) | 2505.24689v1 | 13 |
| 2025-05-29 | [Computational Algebra with Attention: Transformer Oracles for Border Basis Algorithms](https://arxiv.org/abs/2505.23696v2) | 2505.23696v2 | 6 |
| 2025-05-29 | [One Trajectory, One Token: Grounded Video Tokenization via Panoptic Sub-object Trajectory](https://arxiv.org/abs/2505.23617v3) | 2505.23617v3 | 8 |
| 2025-05-29 | [Knowledge Distillation for Reservoir-based Classifier: Human Activity Recognition](https://arxiv.org/abs/2505.22985v1) | 2505.22985v1 | 6 |
| 2025-05-27 | [Is Your LLM Overcharging You? Tokenization, Transparency, and Incentives](https://arxiv.org/abs/2505.21627v4) | 2505.21627v4 | 6 |
| 2025-05-27 | [Evaluation of LLMs in Medical Text Summarization: The Role of Vocabulary Adaptation in High OOV Settings](https://arxiv.org/abs/2505.21242v1) | 2505.21242v1 | 7 |
| 2025-05-26 | [Token Distillation: Attention-aware Input Embeddings For New Tokens](https://arxiv.org/abs/2505.20133v3) | 2505.20133v3 | 7 |
| 2025-05-26 | [Inconsistent Tokenizations Cause Language Models to be Perplexed by Japanese Grammar](https://arxiv.org/abs/2505.19599v1) | 2505.19599v1 | 6 |
| 2025-05-25 | [Unified Medical Image Tokenizer for Autoregressive Synthesis and Understanding](https://arxiv.org/abs/2505.19225v2) | 2505.19225v2 | 6 |
| 2025-05-24 | [Image Tokens Matter: Mitigating Hallucination in Discrete Tokenizer-based Large Vision-Language Models via Latent Editing](https://arxiv.org/abs/2505.21547v1) | 2505.21547v1 | 7 |
| 2025-05-23 | [TokBench: Evaluating Your Visual Tokenizer before Visual Generation](https://arxiv.org/abs/2505.18142v2) | 2505.18142v2 | 6 |
| 2025-05-23 | [Slot-MLLM: Object-Centric Visual Tokenization for Multimodal LLM](https://arxiv.org/abs/2505.17726v3) | 2505.17726v3 | 12 |
| 2025-05-23 | [Exploring the Effect of Segmentation and Vocabulary Size on Speech Tokenization for Speech Language Models](https://arxiv.org/abs/2505.17446v2) | 2505.17446v2 | 9 |
| 2025-05-22 | [Learning Adaptive and Temporally Causal Video Tokenization in a 1D Latent Space](https://arxiv.org/abs/2505.17011v2) | 2505.17011v2 | 10 |
| 2025-05-22 | [Comparative analysis of subword tokenization approaches for Indian languages](https://arxiv.org/abs/2505.16868v1) | 2505.16868v1 | 20 |
| 2025-05-22 | [LLM-Based Emulation of the Radio Resource Control Layer: Towards AI-Native RAN Protocols](https://arxiv.org/abs/2505.16821v5) | 2505.16821v5 | 6 |
| 2025-05-22 | [ALTo: Adaptive-Length Tokenizer for Autoregressive Mask Generation](https://arxiv.org/abs/2505.16495v2) | 2505.16495v2 | 6 |
| 2025-05-22 | [Date Fragments: A Hidden Bottleneck of Tokenization for Temporal Reasoning](https://arxiv.org/abs/2505.16088v3) | 2505.16088v3 | 12 |
| 2025-05-21 | [Moonbeam: A MIDI Foundation Model Using Both Absolute and Relative Music Attributes](https://arxiv.org/abs/2505.15559v1) | 2505.15559v1 | 8 |
| 2025-05-21 | [BanglaByT5: Byte-Level Modelling for Bangla](https://arxiv.org/abs/2505.17102v1) | 2505.17102v1 | 12 |
| 2025-05-21 | [Discrete Audio Representations for Automated Audio Captioning](https://arxiv.org/abs/2505.14989v1) | 2505.14989v1 | 8 |
| 2025-05-20 | [PAST: Phonetic-Acoustic Speech Tokenizer](https://arxiv.org/abs/2505.14470v2) | 2505.14470v2 | 10 |
| 2025-05-20 | [Byte Pair Encoding for Efficient Time Series Forecasting](https://arxiv.org/abs/2505.14411v4) | 2505.14411v4 | 6 |
| 2025-05-20 | [Phonetic Perturbations Reveal Tokenizer-Rooted Safety Gaps in LLMs](https://arxiv.org/abs/2505.14226v5) | 2505.14226v5 | 11 |
| 2025-05-20 | [Tokenization Constraints in LLMs: A Study of Symbolic and Arithmetic Reasoning Limits](https://arxiv.org/abs/2505.14178v1) | 2505.14178v1 | 12 |
| 2025-05-20 | [The Strawberry Problem: Emergence of Character-level Understanding in Tokenized Language Models](https://arxiv.org/abs/2505.14172v3) | 2505.14172v3 | 11 |
| 2025-05-20 | [Impact of Frame Rates on Speech Tokenizer: A Case Study on Mandarin and English](https://arxiv.org/abs/2505.17076v3) | 2505.17076v3 | 10 |
| 2025-05-19 | [VTBench: Evaluating Visual Tokenizers for Autoregressive Image Generation](https://arxiv.org/abs/2505.13439v2) | 2505.13439v2 | 10 |
| 2025-05-19 | [FreeMesh: Boosting Mesh Generation with Coordinates Merging](https://arxiv.org/abs/2505.13573v1) | 2505.13573v1 | 8 |
| 2025-05-19 | [FireFly-T: High-Throughput Sparsity Exploitation for Spiking Transformer Acceleration with Dual-Engine Overlay Architecture](https://arxiv.org/abs/2505.12771v1) | 2505.12771v1 | 6 |
| 2025-05-19 | [Adaptive Tokenization: On the Hop-Overpriority Problem in Tokenized Graph Learning Models](https://arxiv.org/abs/2505.15845v1) | 2505.15845v1 | 6 |
| 2025-05-19 | [Duluth at SemEval-2025 Task 7: TF-IDF with Optimized Vector Dimensions for Multilingual Fact-Checked Claim Retrieval](https://arxiv.org/abs/2505.12616v1) | 2505.12616v1 | 6 |
| 2025-05-18 | [LLM-Based Evaluation of Low-Resource Machine Translation: A Reference-less Dialect Guided Approach with a Refined Sylheti-English Benchmark](https://arxiv.org/abs/2505.12273v1) | 2505.12273v1 | 6 |
| 2025-05-18 | [Distribution Prompting: Understanding the Expressivity of Language Models Through the Next-Token Distributions They Can Produce](https://arxiv.org/abs/2505.12244v2) | 2505.12244v2 | 6 |
| 2025-05-15 | [End-to-End Vision Tokenizer Tuning](https://arxiv.org/abs/2505.10562v1) | 2505.10562v1 | 11 |
| 2025-05-15 | [MMLongBench: Benchmarking Long-Context Vision-Language Models Effectively and Thoroughly](https://arxiv.org/abs/2505.10610v3) | 2505.10610v3 | 6 |
| 2025-05-15 | [MTVCraft: Tokenizing 4D Motion for Arbitrary Character Animation](https://arxiv.org/abs/2505.10238v5) | 2505.10238v5 | 8 |
| 2025-05-14 | [Achieving Tokenizer Flexibility in Language Models through Heuristic Adaptation and Supertoken Learning](https://arxiv.org/abs/2505.09738v2) | 2505.09738v2 | 17 |
| 2025-05-13 | [When repeats drive the vocabulary: a Byte-Pair Encoding analysis of T2T primate genomes](https://arxiv.org/abs/2505.08918v1) | 2505.08918v1 | 13 |
| 2025-05-13 | [Towards Foundation Models for Experimental Readout Systems Combining Discrete and Continuous Data](https://arxiv.org/abs/2505.08736v2) | 2505.08736v2 | 7 |
| 2025-05-12 | [A Comparative Study of Transformer-Based Models for Multi-Horizon Blood Glucose Prediction](https://arxiv.org/abs/2505.08821v1) | 2505.08821v1 | 7 |
| 2025-05-12 | [MedEIR: A Specialized Medical Embedding Model for Enhanced Information Retrieval](https://arxiv.org/abs/2505.13482v1) | 2505.13482v1 | 11 |
| 2025-05-08 | [OWT: A Foundational Organ-Wise Tokenization Framework for Medical Imaging](https://arxiv.org/abs/2505.04899v2) | 2505.04899v2 | 7 |
| 2025-05-08 | [Symbolic Analysis of Grover Search Algorithm via Chain-of-Thought Reasoning and Quantum-Native Tokenization](https://arxiv.org/abs/2505.04880v2) | 2505.04880v2 | 6 |
| 2025-05-04 | [CASA: CNN Autoencoder-based Score Attention for Efficient Multivariate Long-term Time-series Forecasting](https://arxiv.org/abs/2505.02011v1) | 2505.02011v1 | 6 |
| 2025-05-03 | [ResiTok: A Resilient Tokenization-Enabled Framework for Ultra-Low-Rate and Robust Image Transmission](https://arxiv.org/abs/2505.01870v1) | 2505.01870v1 | 6 |
| 2025-05-02 | [Token-free Models for Sarcasm Detection](https://arxiv.org/abs/2505.01006v1) | 2505.01006v1 | 12 |
| 2025-04-24 | [Tokenizing Stock Prices for Enhanced Multi-Step Forecast and Prediction](https://arxiv.org/abs/2504.17313v1) | 2504.17313v1 | 6 |
| 2025-04-23 | [Tokenization Matters: Improving Zero-Shot NER for Indic Languages](https://arxiv.org/abs/2504.16977v1) | 2504.16977v1 | 14 |
| 2025-04-23 | [T-VEC: A Telecom-Specific Vectorization Model with Enhanced Semantic Understanding via Deep Triplet Loss Fine-Tuning](https://arxiv.org/abs/2504.16460v2) | 2504.16460v2 | 7 |
| 2025-04-21 | [HYPEROFA: Expanding LLM Vocabulary to New Languages via Hypernetwork-Based Embedding Initialization](https://arxiv.org/abs/2504.21018v2) | 2504.21018v2 | 8 |
| 2025-04-16 | [Diffusion Generative Recommendation with Continuous Tokens](https://arxiv.org/abs/2504.12007v5) | 2504.12007v5 | 8 |
| 2025-04-16 | [GT-SNT: A Linear-Time Transformer for Large-Scale Graphs via Spiking Node Tokenization](https://arxiv.org/abs/2504.11840v2) | 2504.11840v2 | 7 |
| 2025-04-14 | [ALMTokenizer: A Low-bitrate and Semantic-rich Audio Codec Tokenizer for Audio Language Modeling](https://arxiv.org/abs/2504.10344v1) | 2504.10344v1 | 10 |
| 2025-04-14 | [MorphTok: Morphologically Grounded Tokenization for Indian Languages](https://arxiv.org/abs/2504.10335v2) | 2504.10335v2 | 12 |
| 2025-04-11 | [GigaTok: Scaling Visual Tokenizers to 3 Billion Parameters for Autoregressive Image Generation](https://arxiv.org/abs/2504.08736v2) | 2504.08736v2 | 6 |
| 2025-04-11 | [MedRep: Medical Concept Representation for General Electronic Health Record Foundation Models](https://arxiv.org/abs/2504.08329v3) | 2504.08329v3 | 6 |
| 2025-04-09 | [TASTE: Text-Aligned Speech Tokenization and Embedding for Spoken Language Modeling](https://arxiv.org/abs/2504.07053v3) | 2504.07053v3 | 7 |
| 2025-04-09 | [From Tokenizer Bias to Backbone Capability: A Controlled Study of LLMs for Time Series Forecasting](https://arxiv.org/abs/2504.08818v2) | 2504.08818v2 | 8 |
| 2025-04-09 | [Classifying the Unknown: In-Context Learning for Open-Vocabulary Text and Symbol Recognition](https://arxiv.org/abs/2504.06841v1) | 2504.06841v1 | 7 |
| 2025-04-07 | [Regional Tiny Stories: Using Small Models to Compare Language Learning and Tokenizer Performance](https://arxiv.org/abs/2504.07989v2) | 2504.07989v2 | 10 |
| 2025-04-07 | [SapiensID: Foundation for Human Recognition](https://arxiv.org/abs/2504.04708v1) | 2504.04708v1 | 6 |
| 2025-04-06 | [Universal Item Tokenization for Transferable Generative Recommendation](https://arxiv.org/abs/2504.04405v3) | 2504.04405v3 | 10 |
| 2025-04-06 | [Pre-training Generative Recommender with Multi-Identifier Item Tokenization](https://arxiv.org/abs/2504.04400v3) | 2504.04400v3 | 10 |
| 2025-04-04 | [BabyLM's First Words: Word Segmentation as a Phonological Probing Task](https://arxiv.org/abs/2504.03338v3) | 2504.03338v3 | 9 |
| 2025-04-03 | [Efficient Autoregressive Shape Generation via Octree-Based Adaptive Tokenization](https://arxiv.org/abs/2504.02817v2) | 2504.02817v2 | 6 |
| 2025-04-02 | [Overcoming Vocabulary Constraints with Pixel-level Fallback](https://arxiv.org/abs/2504.02122v2) | 2504.02122v2 | 20 |
| 2025-04-02 | [ILLUME+: Illuminating Unified MLLM with Dual Visual Tokenization and Diffusion Refinement](https://arxiv.org/abs/2504.01934v2) | 2504.01934v2 | 10 |
| 2025-04-02 | [From Smør-re-brød to Subwords: Training LLMs on Danish, One Morpheme at a Time](https://arxiv.org/abs/2504.01540v1) | 2504.01540v1 | 16 |
| 2025-03-31 | [Boundless Byte Pair Encoding: Breaking the Pre-tokenization Barrier](https://arxiv.org/abs/2504.00178v2) | 2504.00178v2 | 8 |
| 2025-03-28 | [Make Some Noise: Towards LLM audio reasoning and generation using sound tokens](https://arxiv.org/abs/2503.22275v1) | 2503.22275v1 | 8 |
| 2025-03-28 | [Tokenization of Gaze Data](https://arxiv.org/abs/2503.22145v1) | 2503.22145v1 | 10 |
| 2025-03-25 | [Universal Cross-Tokenizer Distillation via Approximate Likelihood Matching](https://arxiv.org/abs/2503.20083v4) | 2503.20083v4 | 15 |
| 2025-03-25 | [TokenHSI: Unified Synthesis of Physical Human-Scene Interactions through Task Tokenization](https://arxiv.org/abs/2503.19901v2) | 2503.19901v2 | 10 |
| 2025-03-25 | [AdaptiVocab: Enhancing LLM Efficiency in Focused Domains through Lightweight Vocabulary Adaptation](https://arxiv.org/abs/2503.19693v2) | 2503.19693v2 | 8 |
| 2025-03-24 | [AlphaSpace: Enabling Robotic Actions through Semantic Tokenization and Symbolic Reasoning](https://arxiv.org/abs/2503.18769v2) | 2503.18769v2 | 7 |
| 2025-03-22 | [CODA: Repurposing Continuous VAEs for Discrete Tokenization](https://arxiv.org/abs/2503.17760v2) | 2503.17760v2 | 10 |
| 2025-03-21 | [KL3M Tokenizers: A Family of Domain-Specific and Character-Level Tokenizers for Legal, Financial, and Preprocessing Applications](https://arxiv.org/abs/2503.17247v1) | 2503.17247v1 | 17 |
| 2025-03-19 | [Cube: A Roblox View of 3D Intelligence](https://arxiv.org/abs/2503.15475v3) | 2503.15475v3 | 8 |
| 2025-03-18 | [Splintering Nonconcatenative Languages for Better Tokenization](https://arxiv.org/abs/2503.14433v2) | 2503.14433v2 | 16 |
| 2025-03-18 | [Panoramic Distortion-Aware Tokenization for Person Detection and Localization in Overhead Fisheye Images](https://arxiv.org/abs/2503.14228v4) | 2503.14228v4 | 6 |
| 2025-03-17 | [SuperBPE: Space Travel for Language Models](https://arxiv.org/abs/2503.13423v3) | 2503.13423v3 | 17 |
| 2025-03-17 | [Triad: Empowering LMM-based Anomaly Detection with Vision Expert-guided Visual Tokenizer and Manufacturing Process](https://arxiv.org/abs/2503.13184v2) | 2503.13184v2 | 6 |
| 2025-03-17 | [HiMTok: Learning Hierarchical Mask Tokens for Image Segmentation with Large Multimodal Model](https://arxiv.org/abs/2503.13026v2) | 2503.13026v2 | 8 |
| 2025-03-14 | [HiTVideo: Hierarchical Tokenizers for Enhancing Text-to-Video Generation with Autoregressive Large Language Models](https://arxiv.org/abs/2503.11513v1) | 2503.11513v1 | 6 |
| 2025-03-14 | [Flow to the Mode: Mode-Seeking Diffusion Autoencoders for State-of-the-Art Image Tokenization](https://arxiv.org/abs/2503.11056v3) | 2503.11056v3 | 10 |
| 2025-03-12 | [PerCoV2: Ultra-Low Bit-Rate Perceptual Image Compression via Query-Based 1D Multimodal Image Tokens](https://arxiv.org/abs/2503.09368v2) | 2503.09368v2 | 8 |
| 2025-03-12 | [Global Position Aware Group Choreography using Large Language Model](https://arxiv.org/abs/2503.09645v1) | 2503.09645v1 | 8 |
| 2025-03-11 | [PUMA: Learning a Mutation-Aware Vocabulary of Protein Units](https://arxiv.org/abs/2503.08838v3) | 2503.08838v3 | 8 |
| 2025-03-11 | ["Principal Components" Enable A New Language of Images](https://arxiv.org/abs/2503.08685v2) | 2503.08685v2 | 8 |
| 2025-03-11 | [Layton: Latent Consistency Tokenizer for 1024-pixel Image Reconstruction and Generation by 256 Tokens](https://arxiv.org/abs/2503.08377v3) | 2503.08377v3 | 10 |
| 2025-03-11 | [ProtTeX: Structure-In-Context Reasoning and Editing of Proteins with Large Language Models](https://arxiv.org/abs/2503.08179v3) | 2503.08179v3 | 8 |
| 2025-03-11 | [Boundary Prompting: Elastic Urban Region Representation via Graph-based Spatial Tokenization](https://arxiv.org/abs/2503.07991v1) | 2503.07991v1 | 6 |
| 2025-03-10 | [V2Flow: Unifying Visual Tokenization and Large Language Model Vocabularies for Autoregressive Image Generation](https://arxiv.org/abs/2503.07493v1) | 2503.07493v1 | 13 |
| 2025-03-09 | [SemHiTok: A Unified Image Tokenizer via Semantic-Guided Hierarchical Codebook for Multimodal Understanding and Generation](https://arxiv.org/abs/2503.06764v5) | 2503.06764v5 | 6 |
| 2025-03-05 | [Rethinking Video Tokenization: A Conditioned Diffusion-based Approach](https://arxiv.org/abs/2503.03708v3) | 2503.03708v3 | 10 |
| 2025-03-04 | [Adversarial Tokenization](https://arxiv.org/abs/2503.02174v2) | 2503.02174v2 | 10 |
| 2025-03-03 | [Annotating and Inferring Compositional Structures in Numeral Systems Across Languages](https://arxiv.org/abs/2503.01625v2) | 2503.01625v2 | 8 |
| 2025-03-03 | [Action Tokenizer Matters in In-Context Imitation Learning](https://arxiv.org/abs/2503.01206v3) | 2503.01206v3 | 6 |
| 2025-03-03 | [Exploration on Real World Assets and Tokenization](https://arxiv.org/abs/2503.01111v2) | 2503.01111v2 | 6 |
| 2025-02-28 | [À la recherche du sens perdu: your favourite LLM might have more to say than you can understand](https://arxiv.org/abs/2503.00224v1) | 2503.00224v1 | 6 |
| 2025-02-28 | [Token-level Ensembling of Models with Different Vocabularies](https://arxiv.org/abs/2502.21265v1) | 2502.21265v1 | 6 |
| 2025-02-28 | [Protein Structure Tokenization: Benchmarking and New Recipe](https://arxiv.org/abs/2503.00089v2) | 2503.00089v2 | 10 |
| 2025-02-27 | [UniTok: A Unified Tokenizer for Visual Generation and Understanding](https://arxiv.org/abs/2502.20321v3) | 2502.20321v3 | 8 |
| 2025-02-27 | [How Much is Enough? The Diminishing Returns of Tokenization Training Data](https://arxiv.org/abs/2502.20273v4) | 2502.20273v4 | 14 |
| 2025-02-25 | [Escaping The Big Data Paradigm in Self-Supervised Representation Learning](https://arxiv.org/abs/2502.18056v2) | 2502.18056v2 | 9 |
| 2025-02-25 | [Scaling LLM Pre-training with Vocabulary Curriculum](https://arxiv.org/abs/2502.17910v1) | 2502.17910v1 | 7 |
| 2025-02-24 | [CoT2Align: Cross-Chain of Thought Distillation via Optimal Transport Alignment for Language Models with Different Tokenizers](https://arxiv.org/abs/2502.16806v3) | 2502.16806v3 | 8 |
| 2025-02-22 | [Tokenizing Single-Channel EEG with Time-Frequency Motif Learning](https://arxiv.org/abs/2502.16060v5) | 2502.16060v5 | 10 |
| 2025-02-21 | [Tokenization is Sensitive to Language Variation](https://arxiv.org/abs/2502.15343v2) | 2502.15343v2 | 12 |
| 2025-02-19 | [FlexTok: Resampling Images into 1D Token Sequences of Flexible Length](https://arxiv.org/abs/2502.13967v2) | 2502.13967v2 | 10 |
| 2025-02-19 | [TALKPLAY: Multimodal Music Recommendation with Large Language Models](https://arxiv.org/abs/2502.13713v5) | 2502.13713v5 | 6 |
| 2025-02-18 | [How does a Language-Specific Tokenizer affect LLMs?](https://arxiv.org/abs/2502.12560v2) | 2502.12560v2 | 6 |
| 2025-02-18 | [From Principles to Applications: A Comprehensive Survey of Discrete Tokenizers in Generation, Comprehension, Recommendation, and Information Retrieval](https://arxiv.org/abs/2502.12448v1) | 2502.12448v1 | 6 |
| 2025-02-16 | [Enhancing Cross-Tokenizer Knowledge Distillation with Contextual Dynamical Mapping](https://arxiv.org/abs/2502.11104v1) | 2502.11104v1 | 12 |
| 2025-02-15 | [Order-agnostic Identifier for Large Language Model-based Generative Recommendation](https://arxiv.org/abs/2502.10833v2) | 2502.10833v2 | 9 |
| 2025-02-15 | [Reading Your Heart: Learning ECG Words and Sentences via Pre-training ECG Language Model](https://arxiv.org/abs/2502.10707v1) | 2502.10707v1 | 6 |
| 2025-02-12 | [Enhancing LLM Character-Level Manipulation via Divide and Conquer](https://arxiv.org/abs/2502.08180v2) | 2502.08180v2 | 7 |
| 2025-02-11 | [RoMA: Robust Malware Attribution via Byte-level Adversarial Training with Global Perturbations and Adversarial Consistency Regularization](https://arxiv.org/abs/2502.07492v2) | 2502.07492v2 | 6 |
| 2025-02-11 | [Vevo: Controllable Zero-Shot Voice Imitation with Self-Supervised Disentanglement](https://arxiv.org/abs/2502.07243v1) | 2502.07243v1 | 6 |
| 2025-02-10 | [Tokenization Standards for Linguistic Integrity: Turkish as a Benchmark](https://arxiv.org/abs/2502.07057v2) | 2502.07057v2 | 12 |
| 2025-02-10 | [Blockchain-Powered Asset Tokenization Platform](https://arxiv.org/abs/2502.06752v1) | 2502.06752v1 | 6 |
| 2025-02-09 | [Investigating Compositional Reasoning in Time Series Foundation Models](https://arxiv.org/abs/2502.06037v2) | 2502.06037v2 | 6 |
| 2025-02-08 | [TOKON: TOKenization-Optimized Normalization for time series analysis with a large language model](https://arxiv.org/abs/2502.05701v1) | 2502.05701v1 | 6 |
| 2025-02-07 | [QLIP: Text-Aligned Visual Tokenization Unifies Auto-Regressive Multimodal Understanding and Generation](https://arxiv.org/abs/2502.05178v1) | 2502.05178v1 | 10 |
| 2025-02-07 | [Flexible and Efficient Grammar-Constrained Decoding](https://arxiv.org/abs/2502.05111v2) | 2502.05111v2 | 8 |
| 2025-02-07 | [Learning the Language of NVMe Streams for Ransomware Detection](https://arxiv.org/abs/2502.05011v1) | 2502.05011v1 | 7 |
| 2025-02-06 | [Multimodal Medical Code Tokenizer](https://arxiv.org/abs/2502.04397v3) | 2502.04397v3 | 12 |
| 2025-02-06 | [Scaling Laws in Patchification: An Image Is Worth 50,176 Tokens And More](https://arxiv.org/abs/2502.03738v2) | 2502.03738v2 | 7 |
| 2025-02-05 | [Masked Autoencoders Are Effective Tokenizers for Diffusion Models](https://arxiv.org/abs/2502.03444v2) | 2502.03444v2 | 6 |
| 2025-02-05 | [Rethinking the Global Knowledge of CLIP in Training-Free Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2502.06818v4) | 2502.06818v4 | 6 |
| 2025-02-03 | [Improving Transformer World Models for Data-Efficient RL](https://arxiv.org/abs/2502.01591v3) | 2502.01591v3 | 10 |
| 2025-02-02 | [MorphBPE: A Morpho-Aware Tokenizer Bridging Linguistic Complexity for Efficient LLM Training Across Morphologies](https://arxiv.org/abs/2502.00894v1) | 2502.00894v1 | 17 |
| 2025-02-02 | [Sundial: A Family of Highly Capable Time Series Foundation Models](https://arxiv.org/abs/2502.00816v4) | 2502.00816v4 | 6 |
| 2025-02-01 | [Transformer-Based Vector Font Classification Using Different Font Formats: TrueType versus PostScript](https://arxiv.org/abs/2502.00250v1) | 2502.00250v1 | 7 |
| 2025-01-31 | [Token-Level Entropy Reveals Demographic Disparities in Large Language Models](https://arxiv.org/abs/2501.19337v5) | 2501.19337v5 | 6 |
| 2025-01-30 | [Diffusion Autoencoders are Scalable Image Tokenizers](https://arxiv.org/abs/2501.18593v1) | 2501.18593v1 | 6 |
| 2025-01-28 | [Attribution analysis of legal language as used by LLM](https://arxiv.org/abs/2501.17330v1) | 2501.17330v1 | 8 |
| 2025-01-28 | [Over-Tokenized Transformer: Vocabulary is Generally Worth Scaling](https://arxiv.org/abs/2501.16975v2) | 2501.16975v2 | 11 |
| 2025-01-27 | [Weight-based Analysis of Detokenization in Language Models: Understanding the First Stage of Inference Without Inference](https://arxiv.org/abs/2501.15754v3) | 2501.15754v3 | 14 |
| 2025-01-26 | [GaussianToken: An Effective Image Tokenizer with 2D Gaussian Splatting](https://arxiv.org/abs/2501.15619v1) | 2501.15619v1 | 10 |
| 2025-01-18 | [CEReBrO: Compact Encoder for Representations of Brain Oscillations Using Efficient Alternating Attention](https://arxiv.org/abs/2501.10885v4) | 2501.10885v4 | 6 |
| 2025-01-17 | [Adapting Large Language Models for Character-based Augmentative and Alternative Communication](https://arxiv.org/abs/2501.10582v3) | 2501.10582v3 | 8 |
| 2025-01-17 | [Hierarchical Autoregressive Transformers: Combining Byte- and Word-Level Processing for Robust, Adaptable Language Models](https://arxiv.org/abs/2501.10322v2) | 2501.10322v2 | 17 |
| 2025-01-17 | [One-D-Piece: Image Tokenizer Meets Quality-Controllable Compression](https://arxiv.org/abs/2501.10064v1) | 2501.10064v1 | 10 |
| 2025-01-16 | [Learnings from Scaling Visual Tokenizers for Reconstruction and Generation](https://arxiv.org/abs/2501.09755v1) | 2501.09755v1 | 10 |
| 2025-01-16 | [FAST: Efficient Action Tokenization for Vision-Language-Action Models](https://arxiv.org/abs/2501.09747v1) | 2501.09747v1 | 10 |
| 2025-01-16 | [Delayed Fusion: Integrating Large Language Models into First-Pass Decoding in End-to-end Speech Recognition](https://arxiv.org/abs/2501.09258v1) | 2501.09258v1 | 6 |
| 2025-01-13 | [Democratizing Text-to-Image Masked Generative Models with Compact Text-Aware One-Dimensional Tokens](https://arxiv.org/abs/2501.07730v2) | 2501.07730v2 | 8 |
| 2025-01-09 | [OmniJet-$α_C$: Learning point cloud calorimeter simulations using generative transformers](https://arxiv.org/abs/2501.05534v2) | 2501.05534v2 | 8 |
| 2025-01-09 | [Progressive Growing of Video Tokenizers for Temporally Compact Latent Spaces](https://arxiv.org/abs/2501.05442v2) | 2501.05442v2 | 6 |
| 2025-01-09 | [V2C-CBM: Building Concept Bottlenecks with Vision-to-Concept Tokenizer](https://arxiv.org/abs/2501.04975v1) | 2501.04975v1 | 8 |
| 2025-01-08 | [Evaluating Interval-based Tokenization for Pitch Representation in Symbolic Music Analysis](https://arxiv.org/abs/2501.04630v1) | 2501.04630v1 | 6 |
| 2025-01-08 | [A Partition Cover Approach to Tokenization](https://arxiv.org/abs/2501.06246v3) | 2501.06246v3 | 14 |
| 2025-01-06 | [CAT: Content-Adaptive Image Tokenization](https://arxiv.org/abs/2501.03120v1) | 2501.03120v1 | 12 |
| 2025-01-05 | [Prune or Retrain: Optimizing the Vocabulary of Multilingual Models for Estonian](https://arxiv.org/abs/2501.02631v1) | 2501.02631v1 | 8 |
| 2025-01-03 | [METAGENE-1: Metagenomic Foundation Model for Pandemic Monitoring](https://arxiv.org/abs/2501.02045v1) | 2501.02045v1 | 7 |
| 2025-01-02 | [TabTreeFormer: Tabular Data Generation Using Hybrid Tree-Transformer](https://arxiv.org/abs/2501.01216v7) | 2501.01216v7 | 6 |

### 2024
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2024-12-29 | [MATEY: multiscale adaptive foundation models for spatiotemporal physical systems](https://arxiv.org/abs/2412.20601v1) | 2412.20601v1 | 6 |
| 2024-12-27 | [Enhancing Whisper's Accuracy and Speed for Indian Languages through Prompt-Tuning and Tokenization](https://arxiv.org/abs/2412.19785v1) | 2412.19785v1 | 10 |
| 2024-12-23 | [An Experimental Evaluation of Japanese Tokenizers for Sentiment-Based Text Classification](https://arxiv.org/abs/2412.17361v1) | 2412.17361v1 | 10 |
| 2024-12-23 | [DiffFormer: a Differential Spatial-Spectral Transformer for Hyperspectral Image Classification](https://arxiv.org/abs/2412.17350v1) | 2412.17350v1 | 7 |
| 2024-12-22 | [Enhancing Item Tokenization for Generative Recommendation through Self-Improvement](https://arxiv.org/abs/2412.17171v1) | 2412.17171v1 | 6 |
| 2024-12-21 | [L3TC: Leveraging RWKV for Learned Lossless Low-Complexity Text Compression](https://arxiv.org/abs/2412.16642v2) | 2412.16642v2 | 6 |
| 2024-12-21 | [ImagePiece: Content-aware Re-tokenization for Efficient Image Recognition](https://arxiv.org/abs/2412.16491v1) | 2412.16491v1 | 8 |
| 2024-12-20 | [When Worse is Better: Navigating the compression-generation tradeoff in visual tokenization](https://arxiv.org/abs/2412.16326v2) | 2412.16326v2 | 10 |
| 2024-12-19 | [Why Do Large Language Models (LLMs) Struggle to Count Letters?](https://arxiv.org/abs/2412.18626v1) | 2412.18626v1 | 6 |
| 2024-12-19 | [Next Patch Prediction for Autoregressive Visual Generation](https://arxiv.org/abs/2412.15321v3) | 2412.15321v3 | 7 |
| 2024-12-19 | [ScaMo: Exploring the Scaling Law in Autoregressive Motion Generation Model](https://arxiv.org/abs/2412.14559v1) | 2412.14559v1 | 6 |
| 2024-12-19 | [Multi-Level Optimal Transport for Universal Cross-Tokenizer Knowledge Distillation on Language Models](https://arxiv.org/abs/2412.14528v2) | 2412.14528v2 | 6 |
| 2024-12-18 | [ECG-Byte: A Tokenizer for End-to-End Generative Electrocardiogram Language Modeling](https://arxiv.org/abs/2412.14373v3) | 2412.14373v3 | 8 |
| 2024-12-18 | [Incorporating Feature Pyramid Tokenization and Open Vocabulary Semantic Segmentation](https://arxiv.org/abs/2412.14145v1) | 2412.14145v1 | 11 |
| 2024-12-18 | [Semantic Convergence: Harmonizing Recommender Systems via Two-Stage Alignment and Behavioral Semantic Tokenization](https://arxiv.org/abs/2412.13771v1) | 2412.13771v1 | 6 |
| 2024-12-18 | [Model Decides How to Tokenize: Adaptive DNA Sequence Tokenization with MxDNA](https://arxiv.org/abs/2412.13716v1) | 2412.13716v1 | 6 |
| 2024-12-18 | [Reverse Region-to-Entity Annotation for Pixel-Level Visual Entity Linking](https://arxiv.org/abs/2412.13614v1) | 2412.13614v1 | 6 |
| 2024-12-17 | [VidTok: A Versatile and Open-Source Video Tokenizer](https://arxiv.org/abs/2412.13061v1) | 2412.13061v1 | 10 |
| 2024-12-16 | [Second Language (Arabic) Acquisition of LLMs via Progressive Vocabulary Expansion](https://arxiv.org/abs/2412.12310v2) | 2412.12310v2 | 13 |
| 2024-12-16 | [The Impact of Token Granularity on the Predictive Power of Language Model Surprisal](https://arxiv.org/abs/2412.11940v2) | 2412.11940v2 | 6 |
| 2024-12-14 | [SoftVQ-VAE: Efficient 1-Dimensional Continuous Tokenizer](https://arxiv.org/abs/2412.10958v3) | 2412.10958v3 | 10 |
| 2024-12-14 | [Tokens, the oft-overlooked appetizer: Large language models, the distributional hypothesis, and meaning](https://arxiv.org/abs/2412.10924v11) | 2412.10924v11 | 10 |
| 2024-12-13 | [VQTalker: Towards Multilingual Talking Avatars through Facial Motion Tokenization](https://arxiv.org/abs/2412.09892v2) | 2412.09892v2 | 10 |
| 2024-12-13 | [Byte Latent Transformer: Patches Scale Better Than Tokens](https://arxiv.org/abs/2412.09871v1) | 2412.09871v1 | 19 |
| 2024-12-12 | [Spectral Image Tokenizer](https://arxiv.org/abs/2412.09607v2) | 2412.09607v2 | 6 |
| 2024-12-11 | [SweetTok: Semantic-Aware Spatial-Temporal Tokenizer for Compact Video Discretization](https://arxiv.org/abs/2412.10443v3) | 2412.10443v3 | 12 |
| 2024-12-09 | [When Every Token Counts: Optimal Segmentation for Low-Resource Language Models](https://arxiv.org/abs/2412.06926v5) | 2412.06926v5 | 14 |
| 2024-12-08 | [Language-Guided Image Tokenization for Generation](https://arxiv.org/abs/2412.05796v2) | 2412.05796v2 | 10 |
| 2024-12-06 | [Enhancing Foundation Models for Time Series Forecasting via Wavelet-based Tokenization](https://arxiv.org/abs/2412.05244v1) | 2412.05244v1 | 12 |
| 2024-12-06 | [Superpixel Tokenization for Vision Transformers: Preserving Semantic Integrity in Visual Tokens](https://arxiv.org/abs/2412.04680v3) | 2412.04680v3 | 8 |
| 2024-12-05 | [Divot: Diffusion Powers Video Tokenizer for Comprehension and Generation](https://arxiv.org/abs/2412.04432v1) | 2412.04432v1 | 6 |
| 2024-12-05 | [Infinity: Scaling Bitwise AutoRegressive Modeling for High-Resolution Image Synthesis](https://arxiv.org/abs/2412.04431v2) | 2412.04431v2 | 6 |
| 2024-12-04 | [From Language Models over Tokens to Language Models over Characters](https://arxiv.org/abs/2412.03719v2) | 2412.03719v2 | 6 |
| 2024-12-04 | [Byte BPE Tokenization as an Inverse string Homomorphism](https://arxiv.org/abs/2412.03160v1) | 2412.03160v1 | 13 |
| 2024-12-04 | [TokenFlow: Unified Image Tokenizer for Multimodal Understanding and Generation](https://arxiv.org/abs/2412.03069v2) | 2412.03069v2 | 6 |
| 2024-12-03 | [Scalable Image Tokenization with Index Backpropagation Quantization](https://arxiv.org/abs/2412.02692v2) | 2412.02692v2 | 11 |
| 2024-12-03 | [Scaling Image Tokenizers with Grouped Spherical Quantization](https://arxiv.org/abs/2412.02632v2) | 2412.02632v2 | 6 |
| 2024-12-03 | [3D representation in 512-Byte:Variational tokenizer is the key for autoregressive 3D generation](https://arxiv.org/abs/2412.02202v1) | 2412.02202v1 | 8 |
| 2024-12-02 | [XQ-GAN: An Open-source Image Tokenization Framework for Autoregressive Generation](https://arxiv.org/abs/2412.01762v1) | 2412.01762v1 | 10 |
| 2024-11-30 | [LLaMA-Gene: A General-purpose Gene Task Large Language Model Based on Instruction Fine-tuning](https://arxiv.org/abs/2412.00471v1) | 2412.00471v1 | 8 |
| 2024-11-28 | [Scaling Particle Collision Data Analysis](https://arxiv.org/abs/2412.00129v2) | 2412.00129v2 | 6 |
| 2024-11-27 | [Retrofitting Large Language Models with Dynamic Tokenization](https://arxiv.org/abs/2411.18553v3) | 2411.18553v3 | 15 |
| 2024-11-26 | [Enhancing Character-Level Understanding in LLMs through Token Internal Structure Learning](https://arxiv.org/abs/2411.17679v5) | 2411.17679v5 | 15 |
| 2024-11-26 | [Linguistic Laws Meet Protein Sequences: A Comparative Analysis of Subword Tokenization Methods](https://arxiv.org/abs/2411.17669v1) | 2411.17669v1 | 20 |
| 2024-11-25 | [Factorized Visual Tokenization and Generation](https://arxiv.org/abs/2411.16681v2) | 2411.16681v2 | 12 |
| 2024-11-25 | [UniPose: A Unified Multimodal Framework for Human Pose Comprehension, Generation and Editing](https://arxiv.org/abs/2411.16781v2) | 2411.16781v2 | 6 |
| 2024-11-23 | [Visual-Word Tokenizer: Beyond Fixed Sets of Tokens in Vision Transformers](https://arxiv.org/abs/2411.15397v4) | 2411.15397v4 | 12 |
| 2024-11-22 | [Efficient Long Video Tokenization via Coordinate-based Patch Reconstruction](https://arxiv.org/abs/2411.14762v4) | 2411.14762v4 | 13 |
| 2024-11-21 | [Why do language models perform worse for morphologically complex languages?](https://arxiv.org/abs/2411.14198v1) | 2411.14198v1 | 8 |
| 2024-11-19 | [Arabic-Nougat: Fine-Tuning Vision Transformers for Arabic OCR and Markdown Extraction](https://arxiv.org/abs/2411.17835v1) | 2411.17835v1 | 8 |
| 2024-11-19 | [Evaluating Tokenizer Performance of Large Language Models Across Official Indian Languages](https://arxiv.org/abs/2411.12240v2) | 2411.12240v2 | 10 |
| 2024-11-15 | [Xmodel-1.5: An 1B-scale Multilingual LLM](https://arxiv.org/abs/2411.10083v3) | 2411.10083v3 | 6 |
| 2024-11-13 | [CamemBERT 2.0: A Smarter French Language Model Aged to Perfection](https://arxiv.org/abs/2411.08868v1) | 2411.08868v1 | 8 |
| 2024-11-13 | [Theoretical Analysis of Byte-Pair Encoding](https://arxiv.org/abs/2411.08671v2) | 2411.08671v2 | 10 |
| 2024-11-11 | [TempCharBERT: Keystroke Dynamics for Continuous Access Control Based on Pre-trained Language Models](https://arxiv.org/abs/2411.07224v1) | 2411.07224v1 | 11 |
| 2024-11-11 | [Scaling Mesh Generation via Compressive Tokenization](https://arxiv.org/abs/2411.07025v1) | 2411.07025v1 | 8 |
| 2024-11-09 | [Hardware-Friendly Diffusion Models with Fixed-Size Reusable Structures for On-Device Image Generation](https://arxiv.org/abs/2411.06119v2) | 2411.06119v2 | 9 |
| 2024-11-08 | [LBPE: Long-token-first Tokenization to Improve Large Language Models](https://arxiv.org/abs/2411.05504v1) | 2411.05504v1 | 15 |
| 2024-11-07 | [Don't Look Twice: Faster Video Transformers with Run-Length Tokenization](https://arxiv.org/abs/2411.05222v1) | 2411.05222v1 | 8 |
| 2024-11-07 | [Tomato, Tomahto, Tomate: Do Multilingual Language Models Understand Based on Subword-Level Semantic Concepts?](https://arxiv.org/abs/2411.04530v2) | 2411.04530v2 | 11 |
| 2024-11-07 | [Image Understanding Makes for A Good Tokenizer for Image Generation](https://arxiv.org/abs/2411.04406v1) | 2411.04406v1 | 6 |
| 2024-11-05 | [Character-level Tokenizations as Powerful Inductive Biases for RNA Foundational Models](https://arxiv.org/abs/2411.11808v1) | 2411.11808v1 | 9 |
| 2024-11-04 | [Adaptive Length Image Tokenization via Recurrent Allocation](https://arxiv.org/abs/2411.02393v1) | 2411.02393v1 | 10 |
| 2024-11-03 | [MoCE: Adaptive Mixture of Contextualization Experts for Byte-based Neural Machine Translation](https://arxiv.org/abs/2411.01474v2) | 2411.01474v2 | 14 |
| 2024-10-31 | [A Recipe for Geometry-Aware 3D Mesh Transformers](https://arxiv.org/abs/2411.00164v1) | 2411.00164v1 | 7 |
| 2024-10-31 | [DC-Spin: A Speaker-invariant Speech Tokenizer for Spoken Language Models](https://arxiv.org/abs/2410.24177v1) | 2410.24177v1 | 10 |
| 2024-10-31 | [Improbable Bigrams Expose Vulnerabilities of Incomplete Tokens in Byte-Level Tokenizers](https://arxiv.org/abs/2410.23684v2) | 2410.23684v2 | 18 |
| 2024-10-31 | [Morphological Typology in BPE Subword Productivity and Language Modeling](https://arxiv.org/abs/2410.23656v1) | 2410.23656v1 | 13 |
| 2024-10-29 | [Spatio-temporal Transformers for Action Unit Classification with Event Cameras](https://arxiv.org/abs/2410.21958v1) | 2410.21958v1 | 6 |
| 2024-10-28 | [MultiTok: Variable-Length Tokenization for Efficient LLMs Adapted from LZW Compression](https://arxiv.org/abs/2410.21548v3) | 2410.21548v3 | 10 |
| 2024-10-28 | [LARP: Tokenizing Videos with a Learned Autoregressive Generative Prior](https://arxiv.org/abs/2410.21264v2) | 2410.21264v2 | 10 |
| 2024-10-28 | [MrT5: Dynamic Token Merging for Efficient Byte-level Language Models](https://arxiv.org/abs/2410.20771v3) | 2410.20771v3 | 16 |
| 2024-10-25 | [Counting Ability of Large Language Models and Impact of Tokenization](https://arxiv.org/abs/2410.19730v2) | 2410.19730v2 | 18 |
| 2024-10-23 | [Exploring Tokenization Methods for Multitrack Sheet Music Generation](https://arxiv.org/abs/2410.17584v1) | 2410.17584v1 | 10 |
| 2024-10-22 | [Audio-to-Score Conversion Model Based on Whisper methodology](https://arxiv.org/abs/2410.17209v1) | 2410.17209v1 | 6 |
| 2024-10-22 | [Continuous Speech Tokenizer in Text To Speech](https://arxiv.org/abs/2410.17081v2) | 2410.17081v2 | 6 |
| 2024-10-22 | [DNAHLM -- DNA sequence and Human Language mixed large language Model](https://arxiv.org/abs/2410.16917v2) | 2410.16917v2 | 6 |
| 2024-10-21 | [Elucidating the design space of language models for image generation](https://arxiv.org/abs/2410.16257v1) | 2410.16257v1 | 6 |
| 2024-10-21 | [From Tokens to Materials: Leveraging Language Models for Scientific Discovery](https://arxiv.org/abs/2410.16165v2) | 2410.16165v2 | 9 |
| 2024-10-21 | [Tokenization as Finite-State Transduction](https://arxiv.org/abs/2410.15696v1) | 2410.15696v1 | 18 |
| 2024-10-19 | [DM-Codec: Distilling Multimodal Representations for Speech Tokenization](https://arxiv.org/abs/2410.15017v2) | 2410.15017v2 | 10 |
| 2024-10-19 | [Team Ryu's Submission to SIGMORPHON 2024 Shared Task on Subword Tokenization](https://arxiv.org/abs/2410.17094v1) | 2410.17094v1 | 18 |
| 2024-10-17 | [Learning Graph Quantized Tokenizers](https://arxiv.org/abs/2410.13798v2) | 2410.13798v2 | 6 |
| 2024-10-17 | [Representation Learning of Structured Data for Medical Foundation Models](https://arxiv.org/abs/2410.13351v1) | 2410.13351v1 | 8 |
| 2024-10-16 | [ERAS: Evaluating the Robustness of Chinese NLP Models to Morphological Garden Path Errors](https://arxiv.org/abs/2410.13057v1) | 2410.13057v1 | 6 |
| 2024-10-16 | [Qtok: A Comprehensive Framework for Evaluating Multilingual Tokenizer Quality in Large Language Models](https://arxiv.org/abs/2410.12989v1) | 2410.12989v1 | 10 |
| 2024-10-16 | [Stabilize the Latent Space for Image Autoregressive Modeling: A Unified Perspective](https://arxiv.org/abs/2410.12490v2) | 2410.12490v2 | 8 |
| 2024-10-15 | [Tokenization and Morphology in Multilingual Language Models: A Comparative Analysis of mT5 and ByT5](https://arxiv.org/abs/2410.11627v2) | 2410.11627v2 | 12 |
| 2024-10-14 | [From Anchors to Answers: A Novel Node Tokenizer for Integrating Graph Structure into Large Language Models](https://arxiv.org/abs/2410.10743v2) | 2410.10743v2 | 7 |
| 2024-10-11 | [Exact Byte-Level Probabilities from Tokenized Language Models for FIM-Tasks and Model Ensembles](https://arxiv.org/abs/2410.09303v2) | 2410.09303v2 | 16 |
| 2024-10-10 | [ElasticTok: Adaptive Tokenization for Image and Video](https://arxiv.org/abs/2410.08368v2) | 2410.08368v2 | 6 |
| 2024-10-10 | [Low Bitrate High-Quality RVQGAN-based Discrete Speech Tokenizer](https://arxiv.org/abs/2410.08325v1) | 2410.08325v1 | 10 |
| 2024-10-08 | [From Tokens to Words: On the Inner Lexicon of LLMs](https://arxiv.org/abs/2410.05864v4) | 2410.05864v4 | 10 |
| 2024-10-06 | [Empowering Backbone Models for Visual Text Generation with Input Granularity Control and Glyph-Aware Training](https://arxiv.org/abs/2410.04439v1) | 2410.04439v1 | 6 |
| 2024-10-06 | [ReTok: Replacing Tokenizer to Enhance Representation Efficiency in Large Language Model](https://arxiv.org/abs/2410.04335v1) | 2410.04335v1 | 6 |
| 2024-10-06 | [OD-Stega: LLM-Based Relatively Secure Steganography via Optimized Distributions](https://arxiv.org/abs/2410.04328v2) | 2410.04328v2 | 6 |
| 2024-10-05 | [Toxic Subword Pruning for Dialogue Response Generation on Large Language Models](https://arxiv.org/abs/2410.04155v2) | 2410.04155v2 | 8 |
| 2024-10-04 | [Towards Linguistically-Aware and Language-Independent Tokenization for Large Language Models (LLMs)](https://arxiv.org/abs/2410.03568v1) | 2410.03568v1 | 15 |
| 2024-10-04 | [Gradient-based Jailbreak Images for Multimodal Fusion Models](https://arxiv.org/abs/2410.03489v2) | 2410.03489v2 | 8 |
| 2024-10-04 | [Adaptive BPE Tokenization for Enhanced Vocabulary Adaptation in Finetuning Pretrained Language Models](https://arxiv.org/abs/2410.03258v1) | 2410.03258v1 | 12 |
| 2024-10-03 | [On the Proper Treatment of Tokenization in Psycholinguistics](https://arxiv.org/abs/2410.02691v3) | 2410.02691v3 | 8 |
| 2024-10-03 | [Morphological evaluation of subwords vocabulary used by BETO language model](https://arxiv.org/abs/2410.02283v1) | 2410.02283v1 | 19 |
| 2024-10-03 | [From Pixels to Tokens: Byte-Pair Encoding on Quantized Visual Modalities](https://arxiv.org/abs/2410.02155v3) | 2410.02155v3 | 10 |
| 2024-10-02 | [FARM: Enhancing Molecular Representations with Functional Group Awareness](https://arxiv.org/abs/2410.02082v4) | 2410.02082v4 | 7 |
| 2024-10-02 | [PerTok: Expressive Encoding and Modeling of Symbolic Musical Ideas and Variations](https://arxiv.org/abs/2410.02060v1) | 2410.02060v1 | 7 |
| 2024-10-02 | [Small Language Models Also Work With Small Vocabularies: Probing the Linguistic Abilities of Grapheme- and Phoneme-Based Baby Llamas](https://arxiv.org/abs/2410.01487v2) | 2410.01487v2 | 10 |
| 2024-09-29 | [When Molecular GAN Meets Byte-Pair Encoding](https://arxiv.org/abs/2409.19740v1) | 2409.19740v1 | 8 |
| 2024-09-28 | [Performance Evaluation of Tokenizers in Large Language Models for the Assamese Language](https://arxiv.org/abs/2410.03718v1) | 2410.03718v1 | 6 |
| 2024-09-20 | [One Model is All You Need: ByT5-Sanskrit, a Unified Model for Sanskrit NLP Tasks](https://arxiv.org/abs/2409.13920v1) | 2409.13920v1 | 8 |
| 2024-09-19 | [Is Tokenization Needed for Masked Particle Modelling?](https://arxiv.org/abs/2409.12589v2) | 2409.12589v2 | 6 |
| 2024-09-19 | [Tokenization for Molecular Foundation Models](https://arxiv.org/abs/2409.15370v3) | 2409.15370v3 | 12 |
| 2024-09-17 | [Egalitarian Language Representation in Language Models: It All Begins with Tokenizers](https://arxiv.org/abs/2409.11501v1) | 2409.11501v1 | 16 |
| 2024-09-15 | [Towards understanding evolution of science through language model series](https://arxiv.org/abs/2409.09636v2) | 2409.09636v2 | 8 |
| 2024-09-11 | [Learning Multi-Aspect Item Palette: A Semantic Tokenization Framework for Generative Recommendation](https://arxiv.org/abs/2409.07276v3) | 2409.07276v3 | 7 |
| 2024-09-10 | [SubRegWeigh: Effective and Efficient Annotation Weighing with Subword Regularization](https://arxiv.org/abs/2409.06216v2) | 2409.06216v2 | 10 |
| 2024-09-09 | [Generative Recommender with End-to-End Learnable Item Tokenization](https://arxiv.org/abs/2409.05546v3) | 2409.05546v3 | 10 |
| 2024-09-06 | [BPE Gets Picky: Efficient Vocabulary Refinement During Tokenizer Training](https://arxiv.org/abs/2409.04599v1) | 2409.04599v1 | 16 |
| 2024-09-06 | [Open-MAGVIT2: An Open-Source Project Toward Democratizing Auto-regressive Visual Generation](https://arxiv.org/abs/2409.04410v3) | 2409.04410v3 | 6 |
| 2024-09-05 | [LAST: Language Model Aware Speech Tokenization](https://arxiv.org/abs/2409.03701v2) | 2409.03701v2 | 12 |
| 2024-09-05 | [OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving](https://arxiv.org/abs/2409.03272v1) | 2409.03272v1 | 6 |
| 2024-09-04 | [StyleTokenizer: Defining Image Style by a Single Instance for Controlling Diffusion Models](https://arxiv.org/abs/2409.02543v1) | 2409.02543v1 | 7 |
| 2024-09-04 | [STAB: Speech Tokenizer Assessment Benchmark](https://arxiv.org/abs/2409.02384v1) | 2409.02384v1 | 10 |
| 2024-09-02 | [Multi-Modal Multi-Granularity Tokenizer for Chu Bamboo Slip Scripts](https://arxiv.org/abs/2409.01011v1) | 2409.01011v1 | 6 |
| 2024-08-29 | [SALSA: Speedy ASR-LLM Synchronous Aggregation](https://arxiv.org/abs/2408.16542v1) | 2408.16542v1 | 8 |
| 2024-08-29 | [WavTokenizer: an Efficient Acoustic Discrete Codec Tokenizer for Audio Language Modeling](https://arxiv.org/abs/2408.16532v3) | 2408.16532v3 | 6 |
| 2024-08-28 | [Language Adaptation on a Tight Academic Compute Budget: Tokenizer Swapping Works and Pure bfloat16 Is Enough](https://arxiv.org/abs/2408.15793v1) | 2408.15793v1 | 10 |
| 2024-08-27 | [Human-Centric Video Anomaly Detection Through Spatio-Temporal Pose Tokenization and Transformer](https://arxiv.org/abs/2408.15185v2) | 2408.15185v2 | 6 |
| 2024-08-27 | [Unifying Symbolic Music Arrangement: Track-Aware Reconstruction and Structured Tokenization](https://arxiv.org/abs/2408.15176v5) | 2408.15176v5 | 6 |
| 2024-08-22 | [Positional Description for Numerical Normalization](https://arxiv.org/abs/2408.12430v1) | 2408.12430v1 | 8 |
| 2024-08-21 | [Distributional Properties of Subword Regularization](https://arxiv.org/abs/2408.11443v1) | 2408.11443v1 | 16 |
| 2024-08-19 | [Geometry Informed Tokenization of Molecules for Language Model Generation](https://arxiv.org/abs/2408.10120v1) | 2408.10120v1 | 6 |
| 2024-08-16 | [Where is the signal in tokenization space?](https://arxiv.org/abs/2408.08541v2) | 2408.08541v2 | 10 |
| 2024-08-14 | [A Spitting Image: Modular Superpixel Tokenization in Vision Transformers](https://arxiv.org/abs/2408.07680v2) | 2408.07680v2 | 9 |
| 2024-08-14 | [LiPCoT: Linear Predictive Coding based Tokenizer for Self-supervised Learning of Time Series Data via Language Models](https://arxiv.org/abs/2408.07292v1) | 2408.07292v1 | 8 |
| 2024-08-13 | [Fingerspelling within Sign Language Translation](https://arxiv.org/abs/2408.07065v1) | 2408.07065v1 | 10 |
| 2024-08-13 | [FlatFusion: Delving into Details of Sparse Transformer-based Camera-LiDAR Fusion for Autonomous Driving](https://arxiv.org/abs/2408.06832v2) | 2408.06832v2 | 6 |
| 2024-08-09 | [FUSE-ing Language Models: Zero-Shot Adapter Discovery for Prompt Optimization Across Tokenizers](https://arxiv.org/abs/2408.04816v1) | 2408.04816v1 | 7 |
| 2024-08-08 | [Trans-Tokenization and Cross-lingual Vocabulary Transfers: Language Adaptation of LLMs for Low-Resource NLP](https://arxiv.org/abs/2408.04303v1) | 2408.04303v1 | 10 |
| 2024-08-08 | [Semantics or spelling? Probing contextual word embeddings with orthographic noise](https://arxiv.org/abs/2408.04162v1) | 2408.04162v1 | 9 |
| 2024-08-05 | [MeshAnything V2: Artist-Created Mesh Generation With Adjacent Mesh Tokenization](https://arxiv.org/abs/2408.02555v3) | 2408.02555v3 | 6 |
| 2024-08-05 | [Batching BPE Tokenization Merges](https://arxiv.org/abs/2408.04653v1) | 2408.04653v1 | 15 |
| 2024-08-05 | [DRFormer: Multi-Scale Transformer Utilizing Diverse Receptive Fields for Long Time-Series Forecasting](https://arxiv.org/abs/2408.02279v1) | 2408.02279v1 | 6 |
| 2024-08-01 | [UniMoT: Unified Molecule-Text Language Model with Discrete Token Representation](https://arxiv.org/abs/2408.00863v2) | 2408.00863v2 | 6 |
| 2024-07-27 | [FarSSiBERT: A Novel Transformer-based Model for Semantic Similarity Measurement of Persian Social Networks Informal Texts](https://arxiv.org/abs/2407.19173v1) | 2407.19173v1 | 8 |
| 2024-07-26 | [GraphBPE: Molecular Graphs Meet Byte-Pair Encoding](https://arxiv.org/abs/2407.19039v1) | 2407.19039v1 | 11 |
| 2024-07-23 | [Data Mixture Inference: What do BPE Tokenizers Reveal about their Training Data?](https://arxiv.org/abs/2407.16607v4) | 2407.16607v4 | 9 |
| 2024-07-22 | [dMel: Speech Tokenization made Simple](https://arxiv.org/abs/2407.15835v3) | 2407.15835v3 | 6 |
| 2024-07-18 | [DuoFormer: Leveraging Hierarchical Visual Representations by Local and Global Attention](https://arxiv.org/abs/2407.13920v1) | 2407.13920v1 | 6 |
| 2024-07-18 | [Scaling Laws with Vocabulary: Larger Models Deserve Larger Vocabularies](https://arxiv.org/abs/2407.13623v3) | 2407.13623v3 | 7 |
| 2024-07-17 | [Krutrim LLM: A Novel Tokenization Strategy for Multilingual Indic Languages with Petabyte-Scale Data Processing](https://arxiv.org/abs/2407.12481v2) | 2407.12481v2 | 10 |
| 2024-07-16 | [The Foundations of Tokenization: Statistical and Computational Concerns](https://arxiv.org/abs/2407.11606v4) | 2407.11606v4 | 12 |
| 2024-07-13 | [Bilingual Adaptation of Monolingual Foundation Models](https://arxiv.org/abs/2407.12869v2) | 2407.12869v2 | 7 |
| 2024-07-12 | [On the Role of Discrete Tokenization in Visual Representation Learning](https://arxiv.org/abs/2407.09087v1) | 2407.09087v1 | 10 |
| 2024-07-11 | [MAGNET: Improving the Multilingual Fairness of Language Models with Adaptive Gradient-Based Tokenization](https://arxiv.org/abs/2407.08818v2) | 2407.08818v2 | 18 |
| 2024-07-08 | [An Empirical Comparison of Vocabulary Expansion and Initialization Approaches for Language Models](https://arxiv.org/abs/2407.05841v2) | 2407.05841v2 | 8 |
| 2024-07-05 | [Romanization Encoding For Multilingual ASR](https://arxiv.org/abs/2407.04368v2) | 2407.04368v2 | 6 |
| 2024-07-04 | [Improving Self Consistency in LLMs through Probabilistic Tokenization](https://arxiv.org/abs/2407.03678v1) | 2407.03678v1 | 10 |
| 2024-07-03 | [HoloHisto: End-to-end Gigapixel WSI Segmentation with 4K Resolution Sequential Tokenization](https://arxiv.org/abs/2407.03307v1) | 2407.03307v1 | 12 |
| 2024-07-03 | [Multiple-Resolution Tokenization for Time Series Forecasting with an Application to Pricing](https://arxiv.org/abs/2407.03185v2) | 2407.03185v2 | 8 |
| 2024-06-28 | [Token Erasure as a Footprint of Implicit Vocabulary Items in LLMs](https://arxiv.org/abs/2406.20086v3) | 2406.20086v3 | 7 |
| 2024-06-27 | [Efficient World Models with Context-Aware Tokenization](https://arxiv.org/abs/2406.19320v1) | 2406.19320v1 | 6 |
| 2024-06-27 | [T-FREE: Subword Tokenizer-Free Generative LLMs via Sparse Representations for Memory-Efficient Embeddings](https://arxiv.org/abs/2406.19223v2) | 2406.19223v2 | 15 |
| 2024-06-27 | [OmniJARVIS: Unified Vision-Language-Action Tokenization Enables Open-World Instruction Following Agents](https://arxiv.org/abs/2407.00114v2) | 2407.00114v2 | 8 |
| 2024-06-25 | [CharED: Character-wise Ensemble Decoding for Large Language Models](https://arxiv.org/abs/2407.11009v1) | 2407.11009v1 | 6 |
| 2024-06-24 | [Vaporetto: Efficient Japanese Tokenization Based on Improved Pointwise Linear Classification](https://arxiv.org/abs/2406.17185v1) | 2406.17185v1 | 6 |
| 2024-06-24 | [Understanding and Mitigating Tokenization Bias in Language Models](https://arxiv.org/abs/2406.16829v2) | 2406.16829v2 | 16 |
| 2024-06-24 | [C-LLM: Learn to Check Chinese Spelling Errors Character by Character](https://arxiv.org/abs/2406.16536v2) | 2406.16536v2 | 6 |
| 2024-06-21 | [Unsupervised Morphological Tree Tokenizer](https://arxiv.org/abs/2406.15245v2) | 2406.15245v2 | 16 |
| 2024-06-20 | [HIGHT: Hierarchical Graph Tokenization for Molecule-Language Alignment](https://arxiv.org/abs/2406.14021v2) | 2406.14021v2 | 10 |
| 2024-06-19 | [Lexically Grounded Subword Segmentation](https://arxiv.org/abs/2406.13560v2) | 2406.13560v2 | 11 |
| 2024-06-18 | [GPT Czech Poet: Generation of Czech Poetic Strophes with Language Models](https://arxiv.org/abs/2407.12790v1) | 2407.12790v1 | 8 |
| 2024-06-17 | [LiLiuM: eBay's Large Language Models for e-commerce](https://arxiv.org/abs/2406.12023v1) | 2406.12023v1 | 6 |
| 2024-06-17 | [Tokenization Falling Short: On Subword Robustness in Large Language Models](https://arxiv.org/abs/2406.11687v3) | 2406.11687v3 | 16 |
| 2024-06-17 | [How Can We Effectively Expand the Vocabulary of LLMs with 0.01GB of Target Language Text?](https://arxiv.org/abs/2406.11477v3) | 2406.11477v3 | 8 |
| 2024-06-17 | [Problematic Tokens: Tokenizer Bias in Large Language Models](https://arxiv.org/abs/2406.11214v3) | 2406.11214v3 | 12 |
| 2024-06-16 | [NAST: Noise Aware Speech Tokenization for Speech Language Models](https://arxiv.org/abs/2406.11037v1) | 2406.11037v1 | 6 |
| 2024-06-16 | [Leading Whitespaces of Language Models' Subword Vocabulary Pose a Confound for Calculating Word Probabilities](https://arxiv.org/abs/2406.10851v2) | 2406.10851v2 | 9 |
| 2024-06-15 | [TokenRec: Learning to Tokenize ID for LLM-based Generative Recommendation](https://arxiv.org/abs/2406.10450v3) | 2406.10450v3 | 8 |
| 2024-06-14 | [BEACON: Benchmark for Comprehensive RNA Tasks and Language Models](https://arxiv.org/abs/2406.10391v2) | 2406.10391v2 | 8 |
| 2024-06-14 | [Optimizing Byte-level Representation for End-to-end ASR](https://arxiv.org/abs/2406.09676v2) | 2406.09676v2 | 6 |
| 2024-06-13 | [OmniTokenizer: A Joint Image-Video Tokenizer for Visual Generation](https://arxiv.org/abs/2406.09399v1) | 2406.09399v1 | 10 |
| 2024-06-11 | [An Image is Worth 32 Tokens for Reconstruction and Generation](https://arxiv.org/abs/2406.07550v1) | 2406.07550v1 | 8 |
| 2024-06-11 | [Image and Video Tokenization with Binary Spherical Quantization](https://arxiv.org/abs/2406.07548v1) | 2406.07548v1 | 11 |
| 2024-06-08 | [Autoregressive Diffusion Transformer for Text-to-Speech Synthesis](https://arxiv.org/abs/2406.05551v1) | 2406.05551v1 | 8 |
| 2024-06-08 | [Exploring the Benefits of Tokenization of Discrete Acoustic Units](https://arxiv.org/abs/2406.05547v1) | 2406.05547v1 | 8 |
| 2024-06-08 | [VP-LLM: Text-Driven 3D Volume Completion with Large Language Models through Patchification](https://arxiv.org/abs/2406.05543v1) | 2406.05543v1 | 7 |
| 2024-06-07 | [Behavior Structformer: Learning Players Representations with Structured Tokenization](https://arxiv.org/abs/2406.05274v1) | 2406.05274v1 | 6 |
| 2024-06-07 | [Towards Semantic Equivalence of Tokenization in Multimodal LLM](https://arxiv.org/abs/2406.05127v4) | 2406.05127v4 | 10 |
| 2024-06-05 | [Addressing Index Collapse of Large-Codebook Speech Tokenizer with Dual-Decoding Product-Quantized Variational Auto-Encoder](https://arxiv.org/abs/2406.02940v1) | 2406.02940v1 | 6 |
| 2024-06-04 | [An Independence-promoting Loss for Music Generation with Language Models](https://arxiv.org/abs/2406.02315v2) | 2406.02315v2 | 6 |
| 2024-05-30 | [Heidelberg-Boston @ SIGTYP 2024 Shared Task: Enhancing Low-Resource Language Analysis With Character-Aware Hierarchical Transformers](https://arxiv.org/abs/2405.20145v1) | 2405.20145v1 | 6 |
| 2024-05-29 | [Integrating Multi-scale Contextualized Information for Byte-based Neural Machine Translation](https://arxiv.org/abs/2405.19290v3) | 2405.19290v3 | 10 |
| 2024-05-29 | [Large Brain Model for Learning Generic Representations with Tremendous EEG Data in BCI](https://arxiv.org/abs/2405.18765v1) | 2405.18765v1 | 6 |
| 2024-05-28 | [Wavelet-Based Image Tokenizer for Vision Transformers](https://arxiv.org/abs/2405.18616v1) | 2405.18616v1 | 8 |
| 2024-05-27 | [Tokenization Matters! Degrading Large Language Models through Challenging Their Tokenization](https://arxiv.org/abs/2405.17067v2) | 2405.17067v2 | 10 |
| 2024-05-25 | [M$^3$GPT: An Advanced Multimodal, Multitask Framework for Motion Comprehension and Generation](https://arxiv.org/abs/2405.16273v5) | 2405.16273v5 | 6 |
| 2024-05-23 | [Super Tiny Language Models](https://arxiv.org/abs/2405.14159v2) | 2405.14159v2 | 12 |
| 2024-05-22 | [Vikhr: The Family of Open-Source Instruction-Tuned Large Language Models for Russian](https://arxiv.org/abs/2405.13929v8) | 2405.13929v8 | 6 |
| 2024-05-22 | [Contextualized Automatic Speech Recognition with Dynamic Vocabulary](https://arxiv.org/abs/2405.13344v2) | 2405.13344v2 | 8 |
| 2024-05-16 | [TransMI: A Framework to Create Strong Baselines from Multilingual Pretrained Language Models for Transliterated Data](https://arxiv.org/abs/2405.09913v2) | 2405.09913v2 | 11 |
| 2024-05-16 | [IGOT: Information Gain Optimized Tokenizer on Domain Adaptive Pretraining](https://arxiv.org/abs/2405.09857v1) | 2405.09857v1 | 6 |
| 2024-05-16 | [Synthesizing Proteins on the Graphics Card. Protein Folding and the Limits of Critical AI Studies](https://arxiv.org/abs/2405.09788v2) | 2405.09788v2 | 9 |
| 2024-05-15 | [Enhancing Function Name Prediction using Votes-Based Name Tokenization and Multi-Task Learning](https://arxiv.org/abs/2405.09112v1) | 2405.09112v1 | 6 |
| 2024-05-13 | [VQDNA: Unleashing the Power of Vector Quantization for Multi-Species Genomic Sequence Modeling](https://arxiv.org/abs/2405.10812v2) | 2405.10812v2 | 7 |
| 2024-05-13 | [Zero-Shot Tokenizer Transfer](https://arxiv.org/abs/2405.07883v2) | 2405.07883v2 | 9 |
| 2024-05-13 | [Constructing a BPE Tokenization DFA](https://arxiv.org/abs/2405.07671v2) | 2405.07671v2 | 11 |
| 2024-05-13 | [MaskFuser: Masked Fusion of Joint Multi-Modal Tokenization for End-to-End Autonomous Driving](https://arxiv.org/abs/2405.07573v1) | 2405.07573v1 | 6 |
| 2024-05-12 | [Learnable Item Tokenization for Generative Recommendation](https://arxiv.org/abs/2405.07314v3) | 2405.07314v3 | 10 |
| 2024-05-08 | [Fishing for Magikarp: Automatically Detecting Under-trained Tokens in Large Language Models](https://arxiv.org/abs/2405.05417v2) | 2405.05417v2 | 6 |
| 2024-05-03 | [Tokenization of Real Estate Assets Using Blockchain](https://arxiv.org/abs/2405.01852v1) | 2405.01852v1 | 6 |
| 2024-04-30 | [MoST: Multi-modality Scene Tokenization for Motion Prediction](https://arxiv.org/abs/2404.19531v1) | 2404.19531v1 | 9 |
| 2024-04-30 | [Revisiting N-Gram Models: Their Impact in Modern Neural Networks for Handwritten Text Recognition](https://arxiv.org/abs/2404.19317v1) | 2404.19317v1 | 8 |
| 2024-04-29 | [Unknown Script: Impact of Script on Cross-Lingual Transfer](https://arxiv.org/abs/2404.18810v2) | 2404.18810v2 | 8 |
| 2024-04-29 | [A cost minimization approach to fix the vocabulary size in a tokenizer for an End-to-End ASR system](https://arxiv.org/abs/2406.02563v1) | 2406.02563v1 | 15 |
| 2024-04-28 | [Can Perplexity Predict Fine-tuning Performance? An Investigation of Tokenization Effects on Sequential Language Models for Nepali](https://arxiv.org/abs/2404.18071v2) | 2404.18071v2 | 16 |
| 2024-04-27 | [Scaffold-BPE: Enhancing Byte Pair Encoding for Large Language Models with Simple and Effective Scaffold Token Removal](https://arxiv.org/abs/2404.17808v3) | 2404.17808v3 | 9 |
| 2024-04-23 | [Breaking Walls: Pioneering Automatic Speech Recognition for Central Kurdish: End-to-End Transformer Paradigm](https://arxiv.org/abs/2406.02561v3) | 2406.02561v3 | 6 |
| 2024-04-23 | [CoST: Contrastive Quantization based Semantic Tokenization for Generative Recommendation](https://arxiv.org/abs/2404.14774v2) | 2404.14774v2 | 7 |
| 2024-04-22 | [SpaceByte: Towards Deleting Tokenization from Large Language Modeling](https://arxiv.org/abs/2404.14408v3) | 2404.14408v3 | 16 |
| 2024-04-22 | [PARAMANU-GANITA: Can Small Math Language Models Rival with Large Language Models on Mathematical Reasoning?](https://arxiv.org/abs/2404.14395v2) | 2404.14395v2 | 6 |
| 2024-04-20 | [Evaluating Subword Tokenization: Alien Subword Composition and OOV Generalization Challenge](https://arxiv.org/abs/2404.13292v1) | 2404.13292v1 | 20 |
| 2024-04-19 | [Groma: Localized Visual Tokenization for Grounding Multimodal Large Language Models](https://arxiv.org/abs/2404.13013v1) | 2404.13013v1 | 7 |
| 2024-04-15 | [Glitch Tokens in Large Language Models: Categorization Taxonomy and Effective Detection](https://arxiv.org/abs/2404.09894v3) | 2404.09894v3 | 9 |
| 2024-04-15 | [Tokenization, Fusion, and Augmentation: Towards Fine-grained Multi-modal Entity Representation](https://arxiv.org/abs/2404.09468v2) | 2404.09468v2 | 6 |
| 2024-04-12 | [Toward a Theory of Tokenization in LLMs](https://arxiv.org/abs/2404.08335v2) | 2404.08335v2 | 6 |
| 2024-04-06 | [VTR: An Optimized Vision Transformer for SAR ATR Acceleration on FPGA](https://arxiv.org/abs/2404.04527v1) | 2404.04527v1 | 6 |
| 2024-04-04 | [Training LLMs over Neurally Compressed Text](https://arxiv.org/abs/2404.03626v3) | 2404.03626v3 | 12 |
| 2024-04-04 | [EASSE-DE: Easier Automatic Sentence Simplification Evaluation for German](https://arxiv.org/abs/2404.03563v2) | 2404.03563v2 | 8 |
| 2024-04-03 | [Revisiting subword tokenization: A case study on affixal negation in large language models](https://arxiv.org/abs/2404.02421v2) | 2404.02421v2 | 16 |
| 2024-04-03 | [Low-resource neural machine translation with morphological modeling](https://arxiv.org/abs/2404.02392v1) | 2404.02392v1 | 6 |
| 2024-03-30 | [An Analysis of BPE Vocabulary Trimming in Neural Machine Translation](https://arxiv.org/abs/2404.00397v1) | 2404.00397v1 | 14 |
| 2024-03-27 | [Homogeneous Tokenizer Matters: Homogeneous Visual Tokenizer for Remote Sensing Image Understanding](https://arxiv.org/abs/2403.18593v2) | 2403.18593v2 | 12 |
| 2024-03-26 | [Introducing Syllable Tokenization for Low-resource Languages: A Case Study with Swahili](https://arxiv.org/abs/2406.15358v1) | 2406.15358v1 | 17 |
| 2024-03-26 | [Fingerprinting web servers through Transformer-encoded HTTP response headers](https://arxiv.org/abs/2404.00056v1) | 2404.00056v1 | 6 |
| 2024-03-20 | [Different Tokenization Schemes Lead to Comparable Performance in Spanish Number Agreement](https://arxiv.org/abs/2403.13754v1) | 2403.13754v1 | 7 |
| 2024-03-19 | [RT-NeRV: Rethinking Hybrid Neural Representations for Video via Residual Tokenization](https://arxiv.org/abs/2403.12401v2) | 2403.12401v2 | 11 |
| 2024-03-17 | [Exploring Tokenization Strategies and Vocabulary Sizes for Enhanced Arabic Language Models](https://arxiv.org/abs/2403.11130v2) | 2403.11130v2 | 15 |
| 2024-03-16 | [Pointer-Generator Networks for Low-Resource Machine Translation: Don't Copy That!](https://arxiv.org/abs/2403.10963v3) | 2403.10963v3 | 8 |
| 2024-03-13 | [Token Alignment via Character Matching for Subword Completion](https://arxiv.org/abs/2403.08688v1) | 2403.08688v1 | 10 |
| 2024-03-13 | [Discrete Semantic Tokenization for Deep CTR Prediction](https://arxiv.org/abs/2403.08206v2) | 2403.08206v2 | 7 |
| 2024-03-12 | [Beyond Text: Frozen Large Language Models in Visual Signal Comprehension](https://arxiv.org/abs/2403.07874v1) | 2403.07874v1 | 6 |
| 2024-03-10 | [Unpacking Tokenization: Evaluating Text Compression and its Correlation with Model Performance](https://arxiv.org/abs/2403.06265v2) | 2403.06265v2 | 12 |
| 2024-03-09 | [$\textbf{S}^2$IP-LLM: Semantic Space Informed Prompt Learning with LLM for Time Series Forecasting](https://arxiv.org/abs/2403.05798v2) | 2403.05798v2 | 7 |
| 2024-03-08 | [Cost-Performance Optimization for Processing Low-Resource Language Tasks Using Commercial LLMs](https://arxiv.org/abs/2403.05434v2) | 2403.05434v2 | 6 |
| 2024-03-06 | [Temporal Cross-Attention for Dynamic Embedding and Tokenization of Multimodal Electronic Health Records](https://arxiv.org/abs/2403.04012v2) | 2403.04012v2 | 7 |
| 2024-03-02 | [Greed is All You Need: An Evaluation of Tokenizer Inference Methods](https://arxiv.org/abs/2403.01289v2) | 2403.01289v2 | 14 |
| 2024-03-01 | [Rethinking Tokenization: Crafting Better Tokenizers for Large Language Models](https://arxiv.org/abs/2403.00417v1) | 2403.00417v1 | 20 |
| 2024-02-28 | [Generalizability Under Sensor Failure: Tokenization + Transformers Enable More Robust Latent Spaces](https://arxiv.org/abs/2402.18546v3) | 2402.18546v3 | 10 |
| 2024-02-28 | [Tokenization Is More Than Compression](https://arxiv.org/abs/2402.18376v2) | 2402.18376v2 | 14 |
| 2024-02-27 | [Vision Transformers with Natural Language Semantics](https://arxiv.org/abs/2402.17863v1) | 2402.17863v1 | 6 |
| 2024-02-27 | [SongComposer: A Large Language Model for Lyric and Melody Generation in Song Composition](https://arxiv.org/abs/2402.17645v2) | 2402.17645v2 | 6 |
| 2024-02-27 | [Information Flow Routes: Automatically Interpreting Language Models at Scale](https://arxiv.org/abs/2403.00824v2) | 2403.00824v2 | 6 |
| 2024-02-26 | [TOTEM: TOkenized Time Series EMbeddings for General Time Series Analysis](https://arxiv.org/abs/2402.16412v2) | 2402.16412v2 | 7 |
| 2024-02-22 | [How Important Is Tokenization in French Medical Masked Language Models?](https://arxiv.org/abs/2402.15010v2) | 2402.15010v2 | 16 |
| 2024-02-22 | [Tokenization counts: the impact of tokenization on arithmetic in frontier LLMs](https://arxiv.org/abs/2402.14903v1) | 2402.14903v1 | 6 |
| 2024-02-22 | [Efficient and Effective Vocabulary Expansion Towards Multilingual Large Language Models](https://arxiv.org/abs/2402.14714v1) | 2402.14714v1 | 12 |
| 2024-02-22 | [Two Counterexamples to Tokenization and the Noiseless Channel](https://arxiv.org/abs/2402.14614v2) | 2402.14614v2 | 12 |
| 2024-02-22 | [Subobject-level Image Tokenization](https://arxiv.org/abs/2402.14327v3) | 2402.14327v3 | 17 |
| 2024-02-19 | [Towards Cross-Tokenizer Distillation: the Universal Logit Distillation Loss for LLMs](https://arxiv.org/abs/2402.12030v3) | 2402.12030v3 | 6 |
| 2024-02-16 | [An Empirical Study on Cross-lingual Vocabulary Adaptation for Efficient Language Model Inference](https://arxiv.org/abs/2402.10712v3) | 2402.10712v3 | 7 |
| 2024-02-16 | [PRISE: LLM-Style Sequence Compression for Learning Temporal Action Abstractions in Control](https://arxiv.org/abs/2402.10450v3) | 2402.10450v3 | 6 |
| 2024-02-15 | [Multi-word Tokenization for Sequence Compression](https://arxiv.org/abs/2402.09949v2) | 2402.09949v2 | 10 |
| 2024-02-13 | [Pixel Sentence Representation Learning](https://arxiv.org/abs/2402.08183v1) | 2402.08183v1 | 8 |
| 2024-02-12 | [EvoGPT-f: An Evolutionary GPT Framework for Benchmarking Formal Math Languages](https://arxiv.org/abs/2402.16878v1) | 2402.16878v1 | 8 |
| 2024-02-08 | [Spirit LM: Interleaved Spoken and Written Language Model](https://arxiv.org/abs/2402.05755v2) | 2402.05755v2 | 6 |
| 2024-02-05 | [CLIP Can Understand Depth](https://arxiv.org/abs/2402.03251v2) | 2402.03251v2 | 7 |
| 2024-02-05 | [Video-LaVIT: Unified Video-Language Pre-training with Decoupled Visual-Motional Tokenization](https://arxiv.org/abs/2402.03161v3) | 2402.03161v3 | 10 |
| 2024-02-03 | [Zero-shot sketch-based remote sensing image retrieval based on multi-level and attention-guided tokenization](https://arxiv.org/abs/2402.02141v3) | 2402.02141v3 | 6 |
| 2024-02-02 | [Todyformer: Towards Holistic Dynamic Graph Transformers with Structure-Aware Tokenization](https://arxiv.org/abs/2402.05944v1) | 2402.05944v1 | 8 |
| 2024-02-02 | [Neural Slot Interpreters: Grounding Object Semantics in Emergent Slot Representations](https://arxiv.org/abs/2403.07887v4) | 2403.07887v4 | 6 |
| 2024-02-01 | [Getting the most out of your tokenizer for pre-training and domain adaptation](https://arxiv.org/abs/2402.01035v2) | 2402.01035v2 | 10 |
| 2024-01-28 | [Byte Pair Encoding Is All You Need For Automatic Bengali Speech Recognition](https://arxiv.org/abs/2401.15532v1) | 2401.15532v1 | 12 |
| 2024-01-26 | [Taiyi-Diffusion-XL: Advancing Bilingual Text-to-Image Generation with Large Vision-Language Model Support](https://arxiv.org/abs/2401.14688v3) | 2401.14688v3 | 7 |
| 2024-01-26 | [MaLLaM -- Malaysia Large Language Model](https://arxiv.org/abs/2401.14680v2) | 2401.14680v2 | 6 |
| 2024-01-19 | [Accelerating Multilingual Language Model for Excessively Tokenized Languages](https://arxiv.org/abs/2401.10660v2) | 2401.10660v2 | 6 |
| 2024-01-15 | [Word Boundary Information Isn't Useful for Encoder Language Models](https://arxiv.org/abs/2401.07923v2) | 2401.07923v2 | 6 |
| 2024-01-07 | [RoBERTurk: Adjusting RoBERTa for Turkish](https://arxiv.org/abs/2401.03515v1) | 2401.03515v1 | 6 |
| 2024-01-07 | [CharPoet: A Chinese Classical Poetry Generation System Based on Token-free LLM](https://arxiv.org/abs/2401.03512v3) | 2401.03512v3 | 6 |

### 2023
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2023-12-26 | [Dotless Representation of Arabic Text: Analysis and Modeling](https://arxiv.org/abs/2312.16104v1) | 2312.16104v1 | 6 |
| 2023-12-19 | [Tokenization Matters: Navigating Data-Scarce Tokenization for Gender Inclusive Language Technologies](https://arxiv.org/abs/2312.11779v3) | 2312.11779v3 | 12 |
| 2023-12-07 | [Trajeglish: Traffic Modeling as Next-Token Prediction](https://arxiv.org/abs/2312.04535v2) | 2312.04535v2 | 6 |
| 2023-12-05 | [Impact of Tokenization on LLaMa Russian Adaptation](https://arxiv.org/abs/2312.02598v1) | 2312.02598v1 | 8 |
| 2023-12-03 | [On Significance of Subword tokenization for Low Resource and Efficient Named Entity Recognition: A case study in Marathi](https://arxiv.org/abs/2312.01306v1) | 2312.01306v1 | 16 |
| 2023-11-30 | [Unnatural Error Correction: GPT-4 Can Almost Perfectly Handle Unnatural Scrambled Text](https://arxiv.org/abs/2311.18805v1) | 2311.18805v1 | 6 |
| 2023-11-30 | [Perceptual Group Tokenizer: Building Perception with Iterative Grouping](https://arxiv.org/abs/2311.18296v2) | 2311.18296v2 | 6 |
| 2023-11-28 | [E-ViLM: Efficient Video-Language Model via Masked Video Modeling with Semantic Vector-Quantized Tokenizer](https://arxiv.org/abs/2311.17267v1) | 2311.17267v1 | 6 |
| 2023-11-21 | [PhayaThaiBERT: Enhancing a Pretrained Thai Language Model with Unassimilated Loanwords](https://arxiv.org/abs/2311.12475v2) | 2311.12475v2 | 6 |
| 2023-11-20 | [Hourglass Tokenizer for Efficient Transformer-Based 3D Human Pose Estimation](https://arxiv.org/abs/2311.12028v2) | 2311.12028v2 | 6 |
| 2023-11-15 | [Toucan: Token-Aware Character Level Language Modeling](https://arxiv.org/abs/2311.08620v1) | 2311.08620v1 | 12 |
| 2023-11-14 | [Learning Mutually Informed Representations for Characters and Subwords](https://arxiv.org/abs/2311.07853v2) | 2311.07853v2 | 12 |
| 2023-11-07 | [Improving Korean NLP Tasks with Linguistically Informed Subword Tokenization and Sub-character Decomposition](https://arxiv.org/abs/2311.03928v1) | 2311.03928v1 | 14 |
| 2023-11-04 | [Understanding the Natural Language of DNA using Encoder-Decoder Foundation Models with Byte-level Precision](https://arxiv.org/abs/2311.02333v3) | 2311.02333v3 | 10 |
| 2023-11-01 | [Text Rendering Strategies for Pixel Language Models](https://arxiv.org/abs/2311.00522v1) | 2311.00522v1 | 10 |
| 2023-10-26 | [Words, Subwords, and Morphemes: What Really Matters in the Surprisal-Reading Time Relationship?](https://arxiv.org/abs/2310.17774v1) | 2310.17774v1 | 12 |
| 2023-10-26 | [PETA: Evaluating the Impact of Protein Transfer Learning with Sub-word Tokenization on Downstream Applications](https://arxiv.org/abs/2310.17415v1) | 2310.17415v1 | 8 |
| 2023-10-26 | [miditok: A Python package for MIDI file tokenization](https://arxiv.org/abs/2310.17202v1) | 2310.17202v1 | 10 |
| 2023-10-23 | [Rethinking Tokenizer and Decoder in Masked Graph Modeling for Molecules](https://arxiv.org/abs/2310.14753v2) | 2310.14753v2 | 6 |
| 2023-10-23 | [SpEL: Structured Prediction for Entity Linking](https://arxiv.org/abs/2310.14684v1) | 2310.14684v1 | 6 |
| 2023-10-20 | [Analyzing Cognitive Plausibility of Subword Tokenization](https://arxiv.org/abs/2310.13348v1) | 2310.13348v1 | 18 |
| 2023-10-19 | [Character-level Chinese Backpack Language Models](https://arxiv.org/abs/2310.12751v1) | 2310.12751v1 | 12 |
| 2023-10-17 | [Learn Your Tokens: Word-Pooled Tokenization for Language Modeling](https://arxiv.org/abs/2310.11628v1) | 2310.11628v1 | 16 |
| 2023-10-16 | [Optimized Tokenization for Transcribed Error Correction](https://arxiv.org/abs/2310.10704v1) | 2310.10704v1 | 14 |
| 2023-10-16 | [Personalization of CTC-based End-to-End Speech Recognition Using Pronunciation-Driven Subword Tokenization](https://arxiv.org/abs/2310.09988v1) | 2310.09988v1 | 12 |
| 2023-10-12 | [Tokenizer Choice For LLM Training: Negligible or Crucial?](https://arxiv.org/abs/2310.08754v4) | 2310.08754v4 | 12 |
| 2023-10-12 | [Impact of time and note duration tokenizations on deep learning symbolic music modeling](https://arxiv.org/abs/2310.08497v1) | 2310.08497v1 | 6 |
| 2023-10-12 | [To token or not to token: A Comparative Study of Text Representations for Cross-Lingual Transfer](https://arxiv.org/abs/2310.08078v1) | 2310.08078v1 | 6 |
| 2023-10-11 | [Vec-Tok Speech: speech vectorization and tokenization for neural speech generation](https://arxiv.org/abs/2310.07246v2) | 2310.07246v2 | 8 |
| 2023-10-11 | [Multiview Transformer: Rethinking Spatial Information in Hyperspectral Image Classification](https://arxiv.org/abs/2310.07186v1) | 2310.07186v1 | 6 |
| 2023-10-09 | [Estimating Numbers without Regression](https://arxiv.org/abs/2310.06204v1) | 2310.06204v1 | 10 |
| 2023-10-09 | [Language Model Beats Diffusion -- Tokenizer is Key to Visual Generation](https://arxiv.org/abs/2310.05737v3) | 2310.05737v3 | 8 |
| 2023-10-09 | [Task-Adaptive Tokenization: Enhancing Long-Form Text Generation Efficacy in Mental Health and Beyond](https://arxiv.org/abs/2310.05317v5) | 2310.05317v5 | 12 |
| 2023-10-06 | [Sub-token ViT Embedding via Stochastic Resonance Transformers](https://arxiv.org/abs/2310.03967v2) | 2310.03967v2 | 7 |
| 2023-10-04 | [xVal: A Continuous Numerical Tokenization for Scientific Language Models](https://arxiv.org/abs/2310.02989v2) | 2310.02989v2 | 6 |
| 2023-10-02 | [Pre-training Contextual Location Embeddings in Personal Trajectories via Efficient Hierarchical Location Representations](https://arxiv.org/abs/2310.01252v1) | 2310.01252v1 | 7 |
| 2023-10-02 | [Making LLaMA SEE and Draw with SEED Tokenizer](https://arxiv.org/abs/2310.01218v1) | 2310.01218v1 | 8 |
| 2023-09-23 | [Hindi to English: Transformer-Based Neural Machine Translation](https://arxiv.org/abs/2309.13222v1) | 2309.13222v1 | 12 |
| 2023-09-22 | [Masking Improves Contrastive Self-Supervised Learning for ConvNets, and Saliency Tells You Where](https://arxiv.org/abs/2309.12757v2) | 2309.12757v2 | 6 |
| 2023-09-21 | [Exploring the Impact of Training Data Distribution and Subword Tokenization on Gender Bias in Machine Translation](https://arxiv.org/abs/2309.12491v2) | 2309.12491v2 | 19 |
| 2023-09-20 | [Revisiting Kernel Temporal Segmentation as an Adaptive Tokenizer for Long-form Video Understanding](https://arxiv.org/abs/2309.11569v1) | 2309.11569v1 | 6 |
| 2023-09-19 | [Discrete Audio Representation as an Alternative to Mel-Spectrograms for Speaker and Speech Recognition](https://arxiv.org/abs/2309.10922v1) | 2309.10922v1 | 8 |
| 2023-09-19 | [Language Modeling Is Compression](https://arxiv.org/abs/2309.10668v2) | 2309.10668v2 | 6 |
| 2023-09-15 | [Formalizing BPE Tokenization](https://arxiv.org/abs/2309.08715v1) | 2309.08715v1 | 13 |
| 2023-09-09 | [Unified Language-Vision Pretraining in LLM with Dynamic Discrete Visual Tokenization](https://arxiv.org/abs/2309.04669v3) | 2309.04669v3 | 10 |
| 2023-09-08 | [Subwords as Skills: Tokenization for Sparse-Reward Reinforcement Learning](https://arxiv.org/abs/2309.04459v2) | 2309.04459v2 | 12 |
| 2023-08-31 | [RepCodec: A Speech Representation Codec for Speech Tokenization](https://arxiv.org/abs/2309.00169v3) | 2309.00169v3 | 6 |
| 2023-08-31 | [SpeechTokenizer: Unified Speech Tokenizer for Speech Large Language Models](https://arxiv.org/abs/2308.16692v2) | 2308.16692v2 | 6 |
| 2023-08-23 | [Generative AI for End-to-End Limit Order Book Modelling: A Token-Level Autoregressive Generative Model of Message Flow Using a Deep State Space Network](https://arxiv.org/abs/2309.00638v1) | 2309.00638v1 | 8 |
| 2023-08-23 | [Cabrita: closing the gap for foreign languages](https://arxiv.org/abs/2308.11878v1) | 2308.11878v1 | 8 |
| 2023-08-16 | [Mitigating the Exposure Bias in Sentence-Level Grapheme-to-Phoneme (G2P) Transduction](https://arxiv.org/abs/2308.08442v1) | 2308.08442v1 | 8 |
| 2023-08-10 | [Proximal Policy Optimization Actual Combat: Manipulating Output Tokenizer Length](https://arxiv.org/abs/2308.05585v1) | 2308.05585v1 | 6 |
| 2023-07-16 | [Planting a SEED of Vision in Large Language Model](https://arxiv.org/abs/2307.08041v2) | 2307.08041v2 | 6 |
| 2023-07-14 | [MorphPiece : A Linguistic Tokenizer for Large Language Models](https://arxiv.org/abs/2307.07262v2) | 2307.07262v2 | 11 |
| 2023-07-11 | [Self-supervised adversarial masking for 3D point cloud representation learning](https://arxiv.org/abs/2307.05325v1) | 2307.05325v1 | 6 |
| 2023-07-05 | [MSViT: Dynamic Mixed-Scale Tokenization for Vision Transformers](https://arxiv.org/abs/2307.02321v2) | 2307.02321v2 | 8 |
| 2023-06-30 | [Should you marginalize over possible tokenizations?](https://arxiv.org/abs/2306.17757v1) | 2306.17757v1 | 6 |
| 2023-06-30 | [Biomedical Language Models are Robust to Sub-optimal Tokenization](https://arxiv.org/abs/2306.17649v3) | 2306.17649v3 | 10 |
| 2023-06-29 | [Tokenization and the Noiseless Channel](https://arxiv.org/abs/2306.16842v1) | 2306.16842v1 | 14 |
| 2023-06-26 | [DNABERT-2: Efficient Foundation Model and Benchmark For Multi-Species Genome](https://arxiv.org/abs/2306.15006v2) | 2306.15006v2 | 10 |
| 2023-06-25 | [Revolutionizing Cyber Threat Detection with Large Language Models: A privacy-preserving BERT-based Lightweight Model for IoT/IIoT Devices](https://arxiv.org/abs/2306.14263v2) | 2306.14263v2 | 10 |
| 2023-06-16 | [How do different tokenizers perform on downstream tasks in scriptio continua languages?: A case study in Japanese](https://arxiv.org/abs/2306.09572v1) | 2306.09572v1 | 10 |
| 2023-06-14 | [Unified model for code-switching speech recognition and language identification based on a concatenated tokenizer](https://arxiv.org/abs/2306.08753v3) | 2306.08753v3 | 6 |
| 2023-06-13 | [Tokenization with Factorized Subword Encoding](https://arxiv.org/abs/2306.07764v1) | 2306.07764v1 | 15 |
| 2023-06-12 | [Learning to Mask and Permute Visual Tokens for Vision Transformer Pre-Training](https://arxiv.org/abs/2306.07346v2) | 2306.07346v2 | 6 |
| 2023-06-06 | [Diversifying Joint Vision-Language Tokenization Learning](https://arxiv.org/abs/2306.03421v2) | 2306.03421v2 | 6 |
| 2023-06-04 | [RadLing: Towards Efficient Radiology Report Understanding](https://arxiv.org/abs/2306.02492v1) | 2306.02492v1 | 6 |
| 2023-06-02 | [Assessing the Importance of Frequency versus Compositionality for Subword-based Tokenization in NMT](https://arxiv.org/abs/2306.01393v3) | 2306.01393v3 | 14 |
| 2023-05-29 | [Byte-Level Grammatical Error Correction Using Synthetic and Curated Corpora](https://arxiv.org/abs/2305.17906v1) | 2305.17906v1 | 12 |
| 2023-05-26 | [Im-Promptu: In-Context Composition from Image Prompts](https://arxiv.org/abs/2305.17262v3) | 2305.17262v3 | 6 |
| 2023-05-26 | [Tokenization Impacts Multilingual Language Modeling: Assessing Vocabulary Allocation and Overlap Across Languages](https://arxiv.org/abs/2305.17179v1) | 2305.17179v1 | 13 |
| 2023-05-26 | [Nichelle and Nancy: The Influence of Demographic Attributes and Tokenization Length on First Name Biases](https://arxiv.org/abs/2305.16577v1) | 2305.16577v1 | 6 |
| 2023-05-25 | [Making Vision Transformers Truly Shift-Equivariant](https://arxiv.org/abs/2305.16316v2) | 2305.16316v2 | 6 |
| 2023-05-24 | [The Role of Output Vocabulary in T2T LMs for SPARQL Semantic Parsing](https://arxiv.org/abs/2305.15108v1) | 2305.15108v1 | 7 |
| 2023-05-23 | [From Characters to Words: Hierarchical Pre-trained Language Model for Open-vocabulary Language Understanding](https://arxiv.org/abs/2305.14571v2) | 2305.14571v2 | 7 |
| 2023-05-23 | [CompoundPiece: Evaluating and Improving Decompounding Performance of Language Models](https://arxiv.org/abs/2305.14214v2) | 2305.14214v2 | 12 |
| 2023-05-23 | [Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models](https://arxiv.org/abs/2305.13707v1) | 2305.13707v1 | 6 |
| 2023-05-22 | [TADA: Efficient Task-Agnostic Domain Adaptation for Transformers](https://arxiv.org/abs/2305.12717v1) | 2305.12717v1 | 6 |
| 2023-05-22 | [FIT: Far-reaching Interleaved Transformers](https://arxiv.org/abs/2305.12689v2) | 2305.12689v2 | 6 |
| 2023-05-20 | [What Makes for Good Visual Tokenizers for Large Language Models?](https://arxiv.org/abs/2305.12223v2) | 2305.12223v2 | 8 |
| 2023-05-17 | [Language Model Tokenizers Introduce Unfairness Between Languages](https://arxiv.org/abs/2305.15425v2) | 2305.15425v2 | 20 |
| 2023-05-15 | [Comparing Variation in Tokenizer Outputs Using a Series of Problematic and Challenging Biomedical Sentences](https://arxiv.org/abs/2305.08787v1) | 2305.08787v1 | 10 |
| 2023-05-12 | [MEGABYTE: Predicting Million-byte Sequences with Multiscale Transformers](https://arxiv.org/abs/2305.07185v2) | 2305.07185v2 | 14 |
| 2023-05-09 | [What is the best recipe for character-level encoder-only modelling?](https://arxiv.org/abs/2305.05461v1) | 2305.05461v1 | 7 |
| 2023-05-09 | [Robust Acoustic and Semantic Contextual Biasing in Neural Transducers for Speech Recognition](https://arxiv.org/abs/2305.05271v1) | 2305.05271v1 | 8 |
| 2023-05-05 | [Now It Sounds Like You: Learning Personalized Vocabulary On Device](https://arxiv.org/abs/2305.03584v3) | 2305.03584v3 | 8 |
| 2023-05-05 | [Optimized Table Tokenization for Table Structure Recognition](https://arxiv.org/abs/2305.03393v1) | 2305.03393v1 | 8 |
| 2023-04-28 | [Training and Evaluation of a Multilingual Tokenizer for GPT-SW3](https://arxiv.org/abs/2304.14780v1) | 2304.14780v1 | 10 |
| 2023-04-24 | [Semantic Tokenizer for Enhanced Natural Language Processing](https://arxiv.org/abs/2304.12404v1) | 2304.12404v1 | 13 |
| 2023-04-21 | [Tokenization Preference for Human and Machine Learning Model: An Annotation Study](https://arxiv.org/abs/2304.10813v3) | 2304.10813v3 | 10 |
| 2023-04-21 | [Downstream Task-Oriented Neural Tokenizer Optimization with Vocabulary Restriction as Post Processing](https://arxiv.org/abs/2304.10808v1) | 2304.10808v1 | 13 |
| 2023-04-20 | [Does Manipulating Tokenization Aid Cross-Lingual Transfer? A Study on POS Tagging for Non-Standardized Languages](https://arxiv.org/abs/2304.10158v1) | 2304.10158v1 | 14 |
| 2023-04-18 | [From Words to Music: A Study of Subword Tokenization Techniques in Symbolic Music Generation](https://arxiv.org/abs/2304.08953v2) | 2304.08953v2 | 14 |
| 2023-04-18 | [Romanization-based Large-scale Adaptation of Multilingual Language Models](https://arxiv.org/abs/2304.08865v1) | 2304.08865v1 | 6 |
| 2023-04-15 | [TagCLIP: Improving Discrimination Ability of Open-Vocabulary Semantic Segmentation](https://arxiv.org/abs/2304.07547v2) | 2304.07547v2 | 6 |
| 2023-04-03 | [End-to-End Models for Chemical-Protein Interaction Extraction: Better Tokenization and Span-Based Pipeline Strategies](https://arxiv.org/abs/2304.01344v1) | 2304.01344v1 | 6 |
| 2023-04-01 | [Vision Transformers with Mixed-Resolution Tokenization](https://arxiv.org/abs/2304.00287v2) | 2304.00287v2 | 12 |
| 2023-03-30 | [TreePiece: Faster Semantic Parsing via Tree Tokenization](https://arxiv.org/abs/2303.17161v1) | 2303.17161v1 | 6 |
| 2023-03-27 | [An Information Extraction Study: Take In Mind the Tokenization!](https://arxiv.org/abs/2303.15100v2) | 2303.15100v2 | 14 |
| 2023-03-25 | [Fine-Tashkeel: Finetuning Byte-Level Models for Accurate Arabic Text Diacritization](https://arxiv.org/abs/2303.14588v1) | 2303.14588v1 | 10 |
| 2023-03-25 | [Zero-Shot Everything Sketch-Based Image Retrieval, and in Explainable Style](https://arxiv.org/abs/2303.14348v1) | 2303.14348v1 | 6 |
| 2023-03-16 | [StylerDALLE: Language-Guided Style Transfer Using a Vector-Quantized Tokenizer of a Large-Scale Generative Model](https://arxiv.org/abs/2303.09268v2) | 2303.09268v2 | 6 |
| 2023-03-08 | [Centroid-centered Modeling for Efficient Vision Transformer Pre-training](https://arxiv.org/abs/2303.04664v2) | 2303.04664v2 | 6 |
| 2023-03-04 | [Self-tuning hyper-parameters for unsupervised cross-lingual tokenization](https://arxiv.org/abs/2303.02427v2) | 2303.02427v2 | 6 |
| 2023-03-01 | [A Systematic Analysis of Vocabulary and BPE Settings for Optimal Fine-tuning of NMT: A Case Study of In-domain Translation](https://arxiv.org/abs/2303.00722v1) | 2303.00722v1 | 14 |
| 2023-02-28 | [Are Character-level Translations Worth the Wait? Comparing ByT5 and mT5 for Machine Translation](https://arxiv.org/abs/2302.14220v3) | 2302.14220v3 | 11 |
| 2023-02-27 | [Elementwise Language Representation](https://arxiv.org/abs/2302.13475v1) | 2302.13475v1 | 9 |
| 2023-02-10 | [BEST: BERT Pre-Training for Sign Language Recognition with Coupling Tokenization](https://arxiv.org/abs/2302.05075v3) | 2302.05075v3 | 6 |
| 2023-01-27 | [Byte Pair Encoding for Symbolic Music](https://arxiv.org/abs/2301.11975v3) | 2301.11975v3 | 9 |
| 2023-01-25 | [A Study on FGSM Adversarial Training for Neural Retrieval](https://arxiv.org/abs/2301.10576v1) | 2301.10576v1 | 6 |
| 2023-01-25 | [XLM-V: Overcoming the Vocabulary Bottleneck in Multilingual Masked Language Models](https://arxiv.org/abs/2301.10472v2) | 2301.10472v2 | 7 |
| 2023-01-21 | [Stress Test for BERT and Deep Models: Predicting Words from Italian Poetry](https://arxiv.org/abs/2302.09303v1) | 2302.09303v1 | 6 |
| 2023-01-17 | [Syllable Subword Tokens for Open Vocabulary Speech Recognition in Malayalam](https://arxiv.org/abs/2301.06736v1) | 2301.06736v1 | 9 |
| 2023-01-10 | [Unsupervised Mandarin-Cantonese Machine Translation](https://arxiv.org/abs/2301.03971v1) | 2301.03971v1 | 7 |

### 2022
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2022-12-21 | [What Makes for Good Tokenizers in Vision Transformer?](https://arxiv.org/abs/2212.11115v1) | 2212.11115v1 | 10 |
| 2022-12-20 | [ByGPT5: End-to-End Style-conditioned Poetry Generation with Token-free Language Models](https://arxiv.org/abs/2212.10474v2) | 2212.10474v2 | 10 |
| 2022-12-19 | [Tokenization Consistency Matters for Generative Models on Extractive NLP Tasks](https://arxiv.org/abs/2212.09912v2) | 2212.09912v2 | 10 |
| 2022-12-19 | [Inducing Character-level Structure in Subword-based Language Models with Type-level Interchange Intervention Training](https://arxiv.org/abs/2212.09897v2) | 2212.09897v2 | 9 |
| 2022-12-18 | [BEATs: Audio Pre-Training with Acoustic Tokenizers](https://arxiv.org/abs/2212.09058v1) | 2212.09058v1 | 6 |
| 2022-12-17 | [Beyond the C: Retargetable Decompilation using Neural Machine Translation](https://arxiv.org/abs/2212.08950v1) | 2212.08950v1 | 8 |
| 2022-12-14 | [MANTa: Efficient Gradient-Based Tokenization for Robust End-to-End Language Modeling](https://arxiv.org/abs/2212.07284v1) | 2212.07284v1 | 18 |
| 2022-12-09 | [Open Vocabulary Semantic Segmentation with Patch Aligned Contrastive Learning](https://arxiv.org/abs/2212.04994v1) | 2212.04994v1 | 6 |
| 2022-12-08 | [EPCL: Frozen CLIP Transformer is An Efficient Point Cloud Encoder](https://arxiv.org/abs/2212.04098v3) | 2212.04098v3 | 7 |
| 2022-12-06 | [Rethinking the Objectives of Vector-Quantized Tokenizers for Image Synthesis](https://arxiv.org/abs/2212.03185v2) | 2212.03185v2 | 6 |
| 2022-11-29 | [Extending the Subwording Model of Multilingual Pretrained Models for New Languages](https://arxiv.org/abs/2211.15965v1) | 2211.15965v1 | 12 |
| 2022-11-23 | [Word-Level Representation From Bytes For Language Modeling](https://arxiv.org/abs/2211.12677v1) | 2211.12677v1 | 9 |
| 2022-11-17 | [Efficient Transformers with Dynamic Token Pooling](https://arxiv.org/abs/2211.09761v2) | 2211.09761v2 | 10 |
| 2022-11-10 | [Massively Multilingual ASR on 70 Languages: Tokenization, Architecture, and Generalization Capabilities](https://arxiv.org/abs/2211.05756v1) | 2211.05756v1 | 7 |
| 2022-11-04 | [Dealing with Abbreviations in the Slovenian Biographical Lexicon](https://arxiv.org/abs/2211.02429v1) | 2211.02429v1 | 6 |
| 2022-11-01 | [T5lephone: Bridging Speech and Text Self-supervised Models for Spoken Language Understanding via Phoneme level T5](https://arxiv.org/abs/2211.00586v1) | 2211.00586v1 | 8 |
| 2022-10-31 | [Character-level White-Box Adversarial Attacks against Transformers via Attachable Subwords Substitution](https://arxiv.org/abs/2210.17004v1) | 2210.17004v1 | 17 |
| 2022-10-26 | [Exploring Data-Driven Chemical SMILES Tokenization Approaches to Identify Key Protein-Ligand Binding Moieties](https://arxiv.org/abs/2210.14642v2) | 2210.14642v2 | 12 |
| 2022-10-21 | [Audio-to-Intent Using Acoustic-Textual Subword Representations from End-to-End ASR](https://arxiv.org/abs/2210.12134v1) | 2210.12134v1 | 8 |
| 2022-10-21 | [TransLIST: A Transformer-Based Linguistically Informed Sanskrit Tokenizer](https://arxiv.org/abs/2210.11753v1) | 2210.11753v1 | 8 |
| 2022-10-18 | [Towards Personalization of CTC Speech Recognition Models with Contextual Adapters and Adaptive Boosting](https://arxiv.org/abs/2210.09510v3) | 2210.09510v3 | 6 |
| 2022-10-13 | [A Multi-dimensional Evaluation of Tokenizer-free Multilingual Pretrained Models](https://arxiv.org/abs/2210.07111v1) | 2210.07111v1 | 10 |
| 2022-10-13 | [Incorporating Context into Subword Vocabularies](https://arxiv.org/abs/2210.07095v2) | 2210.07095v2 | 12 |
| 2022-10-12 | [FCT-GAN: Enhancing Table Synthesis via Fourier Transform](https://arxiv.org/abs/2210.06239v1) | 2210.06239v1 | 8 |
| 2022-10-11 | [Better Than Whitespace: Information Retrieval for Languages without Custom Tokenizers](https://arxiv.org/abs/2210.05481v1) | 2210.05481v1 | 10 |
| 2022-09-28 | [Multilingual Search with Subword TF-IDF](https://arxiv.org/abs/2209.14281v2) | 2209.14281v2 | 10 |
| 2022-09-28 | [TVLT: Textless Vision-Language Transformer](https://arxiv.org/abs/2209.14156v2) | 2209.14156v2 | 6 |
| 2022-09-22 | [MonoByte: A Pool of Monolingual Byte-level Language Models](https://arxiv.org/abs/2209.11035v2) | 2209.11035v2 | 15 |
| 2022-09-21 | [Generating Tokenizers with Flat Automata](https://arxiv.org/abs/2209.10313v1) | 2209.10313v1 | 6 |
| 2022-09-09 | [MaxMatch-Dropout: Subword Regularization for WordPiece](https://arxiv.org/abs/2209.04126v1) | 2209.04126v1 | 12 |
| 2022-09-07 | [AudioLM: a Language Modeling Approach to Audio Generation](https://arxiv.org/abs/2209.03143v2) | 2209.03143v2 | 8 |
| 2022-08-25 | [Pix4Point: Image Pretrained Standard Transformers for 3D Point Cloud Understanding](https://arxiv.org/abs/2208.12259v3) | 2208.12259v3 | 7 |
| 2022-08-12 | [BEiT v2: Masked Image Modeling with Vector-Quantized Visual Tokenizers](https://arxiv.org/abs/2208.06366v2) | 2208.06366v2 | 8 |
| 2022-08-03 | [Benchmarking zero-shot and few-shot approaches for tokenization, tagging, and dependency parsing of Tagalog text](https://arxiv.org/abs/2208.01814v2) | 2208.01814v2 | 7 |
| 2022-08-02 | [Lost in Space Marking](https://arxiv.org/abs/2208.01561v1) | 2208.01561v1 | 8 |
| 2022-08-01 | [Video Question Answering with Iterative Video-Text Co-Tokenization](https://arxiv.org/abs/2208.00934v1) | 2208.00934v1 | 6 |
| 2022-07-27 | [Boosting Point-BERT by Multi-choice Tokens](https://arxiv.org/abs/2207.13226v2) | 2207.13226v2 | 10 |
| 2022-07-16 | [Blockchain-enabled tokenization for sustainable and inclusive infrastructure investment](https://arxiv.org/abs/2208.04709v1) | 2208.04709v1 | 6 |
| 2022-07-16 | [The future of blockchain-enabled tokenization in infrastructure investment and development: A Delphi-based scenario analysis](https://arxiv.org/abs/2208.04710v2) | 2208.04710v2 | 6 |
| 2022-06-15 | [The SIGMORPHON 2022 Shared Task on Morpheme Segmentation](https://arxiv.org/abs/2206.07615v1) | 2206.07615v1 | 10 |
| 2022-06-07 | [Searching for Optimal Subword Tokenization in Cross-domain NER](https://arxiv.org/abs/2206.03352v1) | 2206.03352v1 | 12 |
| 2022-06-06 | [What do tokens know about their characters and how do they know it?](https://arxiv.org/abs/2206.02608v1) | 2206.02608v1 | 11 |
| 2022-05-27 | [Patching Leaks in the Charformer for Efficient Character-Level Generation](https://arxiv.org/abs/2205.14086v1) | 2205.14086v1 | 14 |
| 2022-05-23 | [Local Byte Fusion for Neural Machine Translation](https://arxiv.org/abs/2205.11490v3) | 2205.11490v3 | 12 |
| 2022-05-23 | [Unsupervised Tokenization Learning](https://arxiv.org/abs/2205.11443v4) | 2205.11443v4 | 6 |
| 2022-05-20 | [Visual Concepts Tokenization](https://arxiv.org/abs/2205.10093v2) | 2205.10093v2 | 6 |
| 2022-05-19 | [Masked Image Modeling with Denoising Contrast](https://arxiv.org/abs/2205.09616v2) | 2205.09616v2 | 6 |
| 2022-05-19 | [Twist Decoding: Diverse Generators Guide Each Other](https://arxiv.org/abs/2205.09273v2) | 2205.09273v2 | 6 |
| 2022-05-10 | [Richer Countries and Richer Representations](https://arxiv.org/abs/2205.05093v1) | 2205.05093v1 | 7 |
| 2022-05-01 | [Bilingual End-to-End ASR with Byte-Level Subwords](https://arxiv.org/abs/2205.00485v1) | 2205.00485v1 | 16 |
| 2022-04-29 | [How Robust is Neural Machine Translation to Language Imbalance in Multilingual Tokenizer Training?](https://arxiv.org/abs/2204.14268v2) | 2204.14268v2 | 6 |
| 2022-04-26 | [MILES: Visual BERT Pre-training with Injected Language Semantics for Video-text Retrieval](https://arxiv.org/abs/2204.12408v1) | 2204.12408v1 | 6 |
| 2022-04-22 | [A Vocabulary-Free Multilingual Neural Tokenizer for End-to-End Task Learning](https://arxiv.org/abs/2204.10815v1) | 2204.10815v1 | 17 |
| 2022-04-19 | [Impact of Tokenization on Language Models: An Analysis for Turkish](https://arxiv.org/abs/2204.08832v1) | 2204.08832v1 | 14 |
| 2022-04-13 | [A Natural Language Processing Approach for Instruction Set Architecture Identification](https://arxiv.org/abs/2204.06624v1) | 2204.06624v1 | 6 |
| 2022-04-10 | [Breaking Character: Are Subwords Good Enough for MRLs After All?](https://arxiv.org/abs/2204.04748v1) | 2204.04748v1 | 10 |
| 2022-04-08 | [Improving Tokenisation by Alternative Treatment of Spaces](https://arxiv.org/abs/2204.04058v2) | 2204.04058v2 | 6 |
| 2022-04-03 | [POS-BERT: Point Cloud One-Stage BERT Pre-Training](https://arxiv.org/abs/2204.00989v1) | 2204.00989v1 | 6 |
| 2022-04-01 | [CharacterBERT and Self-Teaching for Improving the Robustness of Dense Retrievers on Queries with Typos](https://arxiv.org/abs/2204.00716v2) | 2204.00716v2 | 9 |
| 2022-03-31 | [Multimodal Fusion Transformer for Remote Sensing Image Classification](https://arxiv.org/abs/2203.16952v2) | 2203.16952v2 | 6 |
| 2022-03-29 | [mc-BEiT: Multi-choice Discretization for Image BERT Pre-training](https://arxiv.org/abs/2203.15371v4) | 2203.15371v4 | 8 |
| 2022-03-22 | [PaCa-ViT: Learning Patch-to-Cluster Attention in Vision Transformers](https://arxiv.org/abs/2203.11987v2) | 2203.11987v2 | 8 |
| 2022-03-21 | [Neural Token Segmentation for High Token-Internal Complexity](https://arxiv.org/abs/2203.10845v1) | 2203.10845v1 | 6 |
| 2022-03-18 | [Towards Lithuanian grammatical error correction](https://arxiv.org/abs/2203.09963v1) | 2203.09963v1 | 8 |
| 2022-03-16 | [KinyaBERT: a Morphology-aware Kinyarwanda Language Model](https://arxiv.org/abs/2203.08459v2) | 2203.08459v2 | 6 |
| 2022-03-15 | [Training a Tokenizer for Free with Private Federated Learning](https://arxiv.org/abs/2203.09943v1) | 2203.09943v1 | 9 |
| 2022-03-03 | [Overlap-based Vocabulary Generation Improves Cross-lingual Transfer Among Related Languages](https://arxiv.org/abs/2203.01976v2) | 2203.01976v2 | 6 |
| 2022-03-01 | ["Is Whole Word Masking Always Better for Chinese BERT?": Probing on Chinese Grammatical Error Correction](https://arxiv.org/abs/2203.00286v2) | 2203.00286v2 | 6 |
| 2022-02-24 | [Oolong: Investigating What Makes Transfer Learning Hard with Controlled Studies](https://arxiv.org/abs/2202.12312v2) | 2202.12312v2 | 7 |
| 2022-02-24 | [Pretraining without Wordpieces: Learning Over a Vocabulary of Millions of Words](https://arxiv.org/abs/2202.12142v1) | 2202.12142v1 | 11 |
| 2022-02-22 | [A New Generation of Perspective API: Efficient Multilingual Character-level Transformers](https://arxiv.org/abs/2202.11176v1) | 2202.11176v1 | 11 |
| 2022-02-22 | [Evaluating Persian Tokenizers](https://arxiv.org/abs/2202.10879v1) | 2202.10879v1 | 10 |
| 2022-02-22 | [Korean Tokenization for Beam Search Rescoring in Speech Recognition](https://arxiv.org/abs/2203.03583v2) | 2203.03583v2 | 6 |

### 2021
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2021-12-29 | [Fine-Tuning Transformers: Vocabulary Transfer](https://arxiv.org/abs/2112.14569v2) | 2112.14569v2 | 7 |
| 2021-12-27 | [Vision Transformer for Small-Size Datasets](https://arxiv.org/abs/2112.13492v1) | 2112.13492v1 | 6 |
| 2021-12-25 | [FMViz: Visualizing Tests Generated by AFL at the Byte-level](https://arxiv.org/abs/2112.13207v1) | 2112.13207v1 | 6 |
| 2021-12-20 | [Between words and characters: A Brief History of Open-Vocabulary Modeling and Tokenization in NLP](https://arxiv.org/abs/2112.10508v1) | 2112.10508v1 | 21 |
| 2021-12-13 | [WECHSEL: Effective initialization of subword embeddings for cross-lingual transfer of monolingual language models](https://arxiv.org/abs/2112.06598v2) | 2112.06598v2 | 15 |
| 2021-12-10 | [AtteSTNet -- An attention and subword tokenization based approach for code-switched text hate speech detection](https://arxiv.org/abs/2112.11479v4) | 2112.11479v4 | 16 |
| 2021-11-29 | [Point-BERT: Pre-training 3D Point Cloud Transformers with Masked Point Modeling](https://arxiv.org/abs/2111.14819v2) | 2111.14819v2 | 6 |
| 2021-11-26 | [SWAT: Spatial Structure Within and Among Tokens](https://arxiv.org/abs/2111.13677v3) | 2111.13677v3 | 6 |
| 2021-11-18 | [SimMIM: A Simple Framework for Masked Image Modeling](https://arxiv.org/abs/2111.09886v2) | 2111.09886v2 | 6 |
| 2021-11-15 | [iBOT: Image BERT Pre-Training with Online Tokenizer](https://arxiv.org/abs/2111.07832v3) | 2111.07832v3 | 8 |
| 2021-10-28 | [Blending Anti-Aliasing into Vision Transformer](https://arxiv.org/abs/2110.15156v1) | 2110.15156v1 | 6 |
| 2021-10-26 | [AVocaDo: Strategy for Adapting Vocabulary to Downstream Domain](https://arxiv.org/abs/2110.13434v1) | 2110.13434v1 | 8 |
| 2021-10-22 | [SOFT: Softmax-free Transformer with Linear Complexity](https://arxiv.org/abs/2110.11945v3) | 2110.11945v3 | 6 |
| 2021-10-08 | [Hierarchical Conditional End-to-End ASR with CTC and Multi-Granular Subword Units](https://arxiv.org/abs/2110.04109v2) | 2110.04109v2 | 8 |
| 2021-09-15 | [Efficient Domain Adaptation of Language Models via Adaptive Tokenization](https://arxiv.org/abs/2109.07460v1) | 2109.07460v1 | 15 |
| 2021-09-13 | [Wine is Not v i n. -- On the Compatibility of Tokenizations Across Languages](https://arxiv.org/abs/2109.05772v1) | 2109.05772v1 | 15 |
| 2021-09-07 | [FuseFormer: Fusing Fine-Grained Information in Transformers for Video Inpainting](https://arxiv.org/abs/2109.02974v1) | 2109.02974v1 | 6 |
| 2021-08-25 | [Models In a Spelling Bee: Language Models Implicitly Learn the Character Composition of Tokens](https://arxiv.org/abs/2108.11193v2) | 2108.11193v2 | 7 |
| 2021-08-24 | [More Than Words: Collocation Tokenization for Latent Dirichlet Allocation Models](https://arxiv.org/abs/2108.10755v1) | 2108.10755v1 | 10 |
| 2021-08-19 | [Fast Passage Re-ranking with Contextualized Exact Term Matching and Efficient Passage Expansion](https://arxiv.org/abs/2108.08513v2) | 2108.08513v2 | 6 |
| 2021-08-02 | [LICHEE: Improving Language Model Pre-training with Multi-grained Tokenization](https://arxiv.org/abs/2108.00801v2) | 2108.00801v2 | 6 |
| 2021-08-01 | [Learning to Look Inside: Augmenting Token-Based Encoders with Character-Level Information](https://arxiv.org/abs/2108.00391v1) | 2108.00391v1 | 18 |
| 2021-07-29 | [Local Structure Matters Most: Perturbation Study in NLU](https://arxiv.org/abs/2107.13955v2) | 2107.13955v2 | 8 |
| 2021-07-27 | [gaBERT -- an Irish Language Model](https://arxiv.org/abs/2107.12930v4) | 2107.12930v4 | 6 |
| 2021-07-14 | [TGIF: Tree-Graph Integrated-Format Parser for Enhanced UD with Two-Stage Generic- to Individual-Language Finetuning](https://arxiv.org/abs/2107.06907v1) | 2107.06907v1 | 6 |
| 2021-06-24 | [byteSteady: Fast Classification Using Byte-Level n-Gram Embeddings](https://arxiv.org/abs/2106.13302v1) | 2106.13302v1 | 8 |
| 2021-06-23 | [Charformer: Fast Character Transformers via Gradient-based Subword Tokenization](https://arxiv.org/abs/2106.12672v3) | 2106.12672v3 | 20 |
| 2021-06-23 | [NodePiece: Compositional and Parameter-Efficient Representations of Large Knowledge Graphs](https://arxiv.org/abs/2106.12144v2) | 2106.12144v2 | 11 |
| 2021-06-14 | [Evaluating Various Tokenizers for Arabic Text Classification](https://arxiv.org/abs/2106.07540v2) | 2106.07540v2 | 16 |
| 2021-06-11 | [Bridging Subword Gaps in Pretrain-Finetune Paradigm for Natural Language Generation](https://arxiv.org/abs/2106.06125v1) | 2106.06125v1 | 9 |
| 2021-06-10 | [CAT: Cross Attention in Vision Transformer](https://arxiv.org/abs/2106.05786v1) | 2106.05786v1 | 6 |
| 2021-06-01 | [Sub-Character Tokenization for Chinese Pretrained Language Models](https://arxiv.org/abs/2106.00400v3) | 2106.00400v3 | 12 |
| 2021-05-29 | [Korean-English Machine Translation with Multiple Tokenization Strategy](https://arxiv.org/abs/2105.14274v3) | 2105.14274v3 | 8 |
| 2021-05-28 | [ResT: An Efficient Transformer for Visual Recognition](https://arxiv.org/abs/2105.13677v5) | 2105.13677v5 | 7 |
| 2021-05-28 | [ByT5: Towards a token-free future with pre-trained byte-to-byte models](https://arxiv.org/abs/2105.13626v3) | 2105.13626v3 | 14 |
| 2021-05-26 | [Joint Optimization of Tokenization and Downstream Model](https://arxiv.org/abs/2105.12410v1) | 2105.12410v1 | 10 |
| 2021-05-20 | [KLUE: Korean Language Understanding Evaluation](https://arxiv.org/abs/2105.09680v4) | 2105.09680v4 | 6 |
| 2021-04-17 | [Decrypting Cryptic Crosswords: Semantically Complex Wordplay Puzzles as a Target for NLP](https://arxiv.org/abs/2104.08620v4) | 2104.08620v4 | 6 |
| 2021-03-22 | [Incorporating Convolution Designs into Visual Transformers](https://arxiv.org/abs/2103.11816v2) | 2103.11816v2 | 6 |
| 2021-03-20 | [The Effectiveness of Morphology-aware Segmentation in Low-Resource Neural Machine Translation](https://arxiv.org/abs/2103.11189v1) | 2103.11189v1 | 6 |
| 2021-03-15 | [Multi-view Subword Regularization](https://arxiv.org/abs/2103.08490v2) | 2103.08490v2 | 8 |
| 2021-03-14 | [Crowdsourced Phrase-Based Tokenization for Low-Resourced Neural Machine Translation: The Case of Fon Language](https://arxiv.org/abs/2103.08052v2) | 2103.08052v2 | 8 |
| 2021-03-12 | [Dynamic Acoustic Unit Augmentation With BPE-Dropout for Low-Resource End-to-End Speech Recognition](https://arxiv.org/abs/2103.07186v1) | 2103.07186v1 | 9 |
| 2021-03-11 | [CANINE: Pre-training an Efficient Tokenization-Free Encoder for Language Representation](https://arxiv.org/abs/2103.06874v4) | 2103.06874v4 | 16 |
| 2021-03-11 | [Learning Word-Level Confidence For Subword End-to-End ASR](https://arxiv.org/abs/2103.06716v1) | 2103.06716v1 | 12 |
| 2021-02-26 | [CURE: Code-Aware Neural Machine Translation for Automatic Program Repair](https://arxiv.org/abs/2103.00073v4) | 2103.00073v4 | 10 |
| 2021-02-22 | [Subword Pooling Makes a Difference](https://arxiv.org/abs/2102.10864v2) | 2102.10864v2 | 10 |
| 2021-01-28 | [VX2TEXT: End-to-End Learning of Video-Based Text Generation From Multimodal Inputs](https://arxiv.org/abs/2101.12059v2) | 2101.12059v2 | 9 |
| 2021-01-24 | [WangchanBERTa: Pretraining transformer-based Thai Language Models](https://arxiv.org/abs/2101.09635v2) | 2101.09635v2 | 8 |
| 2021-01-23 | [Training Multilingual Pre-trained Language Model with Byte-level Subwords](https://arxiv.org/abs/2101.09469v2) | 2101.09469v2 | 16 |
| 2021-01-02 | [Superbizarre Is Not Superb: Derivational Morphology Improves BERT's Interpretation of Complex Words](https://arxiv.org/abs/2101.00403v3) | 2101.00403v3 | 6 |

### 2020
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2020-12-31 | [How Good is Your Tokenizer? On the Monolingual Performance of Multilingual Language Models](https://arxiv.org/abs/2012.15613v2) | 2012.15613v2 | 8 |
| 2020-12-31 | [Fast WordPiece Tokenization](https://arxiv.org/abs/2012.15524v3) | 2012.15524v3 | 12 |
| 2020-12-05 | [Pre-training Protein Language Models with Label-Agnostic Binding Pairs Enhances Performance in Downstream Tasks](https://arxiv.org/abs/2012.03084v1) | 2012.03084v1 | 8 |
| 2020-11-18 | [Master Thesis: Neural Sign Language Translation by Learning Tokenization](https://arxiv.org/abs/2011.09289v1) | 2011.09289v1 | 6 |
| 2020-11-17 | [MVP-BERT: Redesigning Vocabularies for Chinese BERT and Multi-Vocab Pretraining](https://arxiv.org/abs/2011.08539v1) | 2011.08539v1 | 10 |
| 2020-11-16 | [Evaluating Sentence Segmentation and Word Tokenization Systems on Estonian Web Texts](https://arxiv.org/abs/2011.07868v1) | 2011.07868v1 | 6 |
| 2020-11-03 | [CharBERT: Character-aware Pre-trained Language Model](https://arxiv.org/abs/2011.01513v1) | 2011.01513v1 | 7 |
| 2020-10-24 | [Char2Subword: Extending the Subword Embedding Space Using Robust Character Compositionality](https://arxiv.org/abs/2010.12730v3) | 2010.12730v3 | 21 |
| 2020-10-20 | [CharacterBERT: Reconciling ELMo and BERT for Word-Level Open-Vocabulary Representations From Characters](https://arxiv.org/abs/2010.10392v3) | 2010.10392v3 | 11 |
| 2020-10-15 | [Tokenization Repair in the Presence of Spelling Errors](https://arxiv.org/abs/2010.07878v2) | 2010.07878v2 | 6 |
| 2020-10-14 | [fugashi, a Tool for Tokenizing Japanese in Python](https://arxiv.org/abs/2010.06858v1) | 2010.06858v1 | 8 |
| 2020-10-06 | [An Empirical Study of Tokenization Strategies for Various Korean NLP Tasks](https://arxiv.org/abs/2010.02534v1) | 2010.02534v1 | 8 |
| 2020-09-22 | [Investigating Machine Learning Methods for Language and Dialect Identification of Cuneiform Texts](https://arxiv.org/abs/2009.10794v1) | 2009.10794v1 | 6 |
| 2020-09-09 | [Central Yup'ik and Machine Translation of Low-Resource Polysynthetic Languages](https://arxiv.org/abs/2009.04087v1) | 2009.04087v1 | 8 |
| 2020-08-27 | [AMBERT: A Pre-trained Language Model with Multi-Grained Tokenization](https://arxiv.org/abs/2008.11869v4) | 2008.11869v4 | 6 |
| 2020-08-21 | [Neural Machine Translation without Embeddings](https://arxiv.org/abs/2008.09396v2) | 2008.09396v2 | 11 |
| 2020-08-10 | [KR-BERT: A Small-Scale Korean-Specific Language Model](https://arxiv.org/abs/2008.03979v2) | 2008.03979v2 | 13 |
| 2020-07-14 | [Deep Transformer based Data Augmentation with Subword Units for Morphologically Rich Online ASR](https://arxiv.org/abs/2007.06949v3) | 2007.06949v3 | 14 |
| 2020-06-09 | [HausaMT v1.0: Towards English-Hausa Neural Machine Translation](https://arxiv.org/abs/2006.05014v2) | 2006.05014v2 | 10 |
| 2020-05-03 | [Dynamic Programming Encoding for Subword Segmentation in Neural Machine Translation](https://arxiv.org/abs/2005.06606v2) | 2005.06606v2 | 8 |
| 2020-04-30 | [Mind Your Inflections! Improving NLP for Non-Standard Englishes with Base-Inflection Encoding](https://arxiv.org/abs/2004.14870v4) | 2004.14870v4 | 10 |
| 2020-04-29 | [Towards Reasonably-Sized Character-Level Transformer NMT by Finetuning Subword Systems](https://arxiv.org/abs/2004.14280v2) | 2004.14280v2 | 9 |
| 2020-04-16 | [Kvistur 2.0: a BiLSTM Compound Splitter for Icelandic](https://arxiv.org/abs/2004.07776v1) | 2004.07776v1 | 10 |
| 2020-04-07 | [Byte Pair Encoding is Suboptimal for Language Model Pretraining](https://arxiv.org/abs/2004.03720v2) | 2004.03720v2 | 10 |
| 2020-02-25 | [Language-Independent Tokenisation Rivals Language-Specific Tokenisation for Word Similarity Prediction](https://arxiv.org/abs/2002.11004v1) | 2002.11004v1 | 7 |
| 2020-02-24 | [Sketchformer: Transformer-based Representation for Sketched Structure](https://arxiv.org/abs/2002.10381v1) | 2002.10381v1 | 6 |
| 2020-02-02 | [Neural Sign Language Translation by Learning Tokenization](https://arxiv.org/abs/2002.00479v2) | 2002.00479v2 | 6 |

### 2019
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2019-11-15 | [A Subword Level Language Model for Bangla Language](https://arxiv.org/abs/1911.07613v1) | 1911.07613v1 | 6 |
| 2019-10-30 | [Mixture factorized auto-encoder for unsupervised hierarchical deep factorization of speech signal](https://arxiv.org/abs/1911.01806v1) | 1911.01806v1 | 9 |
| 2019-10-30 | [ON-TRAC Consortium End-to-End Speech Translation Systems for the IWSLT 2019 Shared Task](https://arxiv.org/abs/1910.13689v1) | 1910.13689v1 | 6 |
| 2019-10-29 | [BPE-Dropout: Simple and Effective Subword Regularization](https://arxiv.org/abs/1910.13267v2) | 1910.13267v2 | 11 |
| 2019-10-02 | [Neural Word Decomposition Models for Abusive Language Detection](https://arxiv.org/abs/1910.01043v1) | 1910.01043v1 | 6 |
| 2019-09-07 | [Neural Machine Translation with Byte-Level Subwords](https://arxiv.org/abs/1909.03341v2) | 1909.03341v2 | 17 |
| 2019-08-27 | [Bridging the Gap for Tokenizer-Free Language Models](https://arxiv.org/abs/1908.10322v1) | 1908.10322v1 | 10 |
| 2019-08-18 | [Parsimonious Morpheme Segmentation with an Application to Enriching Word Embeddings](https://arxiv.org/abs/1908.07832v2) | 1908.07832v2 | 7 |
| 2019-08-14 | [Raw-to-End Name Entity Recognition in Social Media](https://arxiv.org/abs/1908.05344v1) | 1908.05344v1 | 9 |
| 2019-07-26 | [DLGNet: A Transformer-based Model for Dialogue Response Generation](https://arxiv.org/abs/1908.01841v2) | 1908.01841v2 | 8 |
| 2019-07-05 | [Improving Chemical Named Entity Recognition in Patents with Contextualized Word Embeddings](https://arxiv.org/abs/1907.02679v1) | 1907.02679v1 | 7 |
| 2019-07-01 | [Semantic Product Search](https://arxiv.org/abs/1907.00937v1) | 1907.00937v1 | 6 |
| 2019-06-27 | [The Impact of Preprocessing on Arabic-English Statistical and Neural Machine Translation](https://arxiv.org/abs/1906.11751v1) | 1906.11751v1 | 6 |
| 2019-04-29 | [On the Effect of Low-Frequency Terms on Neural-IR Models](https://arxiv.org/abs/1904.12683v2) | 1904.12683v2 | 7 |
| 2019-04-26 | [Copy mechanism and tailored training for character-based data-to-text generation](https://arxiv.org/abs/1904.11838v4) | 1904.11838v4 | 6 |
| 2019-04-14 | [Rare Words: A Major Problem for Contextualized Embeddings And How to Fix it by Attentive Mimicking](https://arxiv.org/abs/1904.06707v4) | 1904.06707v4 | 9 |
| 2019-04-03 | [Subword-Level Language Identification for Intra-Word Code-Switching](https://arxiv.org/abs/1904.01989v1) | 1904.01989v1 | 6 |
| 2019-03-27 | [Initial Crypto-asset Offerings (ICOs), tokenization and corporate governance](https://arxiv.org/abs/1905.03340v1) | 1905.03340v1 | 6 |
| 2019-03-13 | [Maybe Deep Neural Networks are the Best Choice for Modeling Source Code](https://arxiv.org/abs/1903.05734v1) | 1903.05734v1 | 6 |

### 2018
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2018-12-20 | [How Much Does Tokenization Affect Neural Machine Translation?](https://arxiv.org/abs/1812.08621v4) | 1812.08621v4 | 17 |
| 2018-11-19 | [ACTT: Automotive CAN Tokenization and Translation](https://arxiv.org/abs/1811.07897v1) | 1811.07897v1 | 6 |
| 2018-10-24 | [Universal Language Model Fine-Tuning with Subword Tokenization for Polish](https://arxiv.org/abs/1810.10222v1) | 1810.10222v1 | 12 |
| 2018-09-22 | [A Byte-sized Approach to Named Entity Recognition](https://arxiv.org/abs/1809.08386v1) | 1809.08386v1 | 14 |
| 2018-09-10 | [Towards JointUD: Part-of-speech Tagging and Lemmatization using Recurrent Neural Networks](https://arxiv.org/abs/1809.03211v1) | 1809.03211v1 | 6 |
| 2018-08-19 | [SentencePiece: A simple and language independent subword tokenizer and detokenizer for Neural Text Processing](https://arxiv.org/abs/1808.06226v1) | 1808.06226v1 | 12 |
| 2018-08-13 | [Neural Semi-Markov Conditional Random Fields for Robust Character-Based Part-of-Speech Tagging](https://arxiv.org/abs/1808.04208v3) | 1808.04208v3 | 8 |
| 2018-07-25 | [Finding Better Subword Segmentation for Neural Machine Translation](https://arxiv.org/abs/1807.09639v1) | 1807.09639v1 | 10 |
| 2018-07-23 | [Deep Dialog Act Recognition using Multiple Token, Segment, and Context Information Representations](https://arxiv.org/abs/1807.08587v2) | 1807.08587v2 | 7 |
| 2018-05-18 | [A Study on Dialog Act Recognition using Character-Level Tokenization](https://arxiv.org/abs/1805.07231v2) | 1805.07231v2 | 9 |
| 2018-02-06 | [Byte-Level Recursive Convolutional Auto-Encoder for Text](https://arxiv.org/abs/1802.01817v1) | 1802.01817v1 | 6 |

### 2017
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2017-10-17 | [CASICT Tibetan Word Segmentation System for MLWS2017](https://arxiv.org/abs/1710.06112v1) | 1710.06112v1 | 6 |
| 2017-10-05 | [BPEmb: Tokenization-free Pre-trained Subword Embeddings in 275 Languages](https://arxiv.org/abs/1710.02187v1) | 1710.02187v1 | 16 |
| 2017-09-20 | [De-identification of medical records using conditional random fields and long short-term memory networks](https://arxiv.org/abs/1709.06901v2) | 1709.06901v2 | 6 |
| 2017-08-08 | [Which Encoding is the Best for Text Classification in Chinese, English, Japanese and Korean?](https://arxiv.org/abs/1708.02657v2) | 1708.02657v2 | 7 |
| 2017-03-22 | [Topic Identification for Speech without ASR](https://arxiv.org/abs/1703.07476v2) | 1703.07476v2 | 6 |

### 2016
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2016-10-10 | [Fully Character-Level Neural Machine Translation without Explicit Segmentation](https://arxiv.org/abs/1610.03017v3) | 1610.03017v3 | 7 |
| 2016-09-25 | [Large-Scale Machine Translation between Arabic and Hebrew: Available Corpora and Initial Results](https://arxiv.org/abs/1609.07701v1) | 1609.07701v1 | 6 |
| 2016-09-01 | [Several Proofs of Security for a Tokenization Algorithm](https://arxiv.org/abs/1609.00151v3) | 1609.00151v3 | 6 |
| 2016-03-09 | [Unsupervised word segmentation and lexicon discovery using acoustic word embeddings](https://arxiv.org/abs/1603.02845v1) | 1603.02845v1 | 7 |

### 2015
| 日期 | 标题 | arXiv | 分数 |
| :-- | :-- | :-- | --: |
| 2015-12-01 | [Multilingual Language Processing From Bytes](https://arxiv.org/abs/1512.00103v2) | 1512.00103v2 | 6 |

<!-- table:end papers -->
