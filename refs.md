# References with verification pointers

### `vaswani2017attention` — Attention is all you need (2017)
- **Authors**: Vaswani, Ashish, Shazeer, Noam, Parmar, Niki, Uszkoreit, Jakob, Jones, Llion, Gomez, Aidan N, Kaiser, \Lukasz, Polosukhin, Illia
- **Venue/Type**: Advances in neural information processing systems
- **arXiv**: 1706.03762
- **Link**: https://arxiv.org/abs/1706.03762
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / Transformer架构
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 张量并行（TP）中的 All-Reduce 通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `及专家并行（Expert Parallelism, EP）。 TP 将注意力头（Attention Head）切分到多个设备上协同计算，并引入集合通信规约（AllReduce）不同注意力头的结果，通信密集但可降低单设备的计算和内存压力； P`
  - `r{相关技术背景}  \section{大模型推理}  \subsection{Transformer架构}  大语言模型（Large Language Models, LLMs）的重大突破始于 Transformer 架构的提出。 该架构`

### `kalia2016rdma_design_guidelines` — Design Guidelines for High Performance RDMA Systems (2016)
- **Authors**: Anuj Kalia, Michael Kaminsky, David G. Andersen
- **Venue/Type**: 2016 USENIX Annual Technical Conference (USENIX ATC 16)
- **Link**: https://www.usenix.org/conference/atc16/technical-sessions/presentation/kalia
- **Used / Suggested insertion in thesis**:
  - **TODO**: 未在旧 `references.md` 中找到对应条目；请根据正文实际引用位置补充。

### `kaplan2020scalinglaws` — Scaling laws for neural language models (2020)
- **Authors**: Kaplan, Jared, McCandlish, Sam, Henighan, Tom, Brown, Tom B, Chess, Benjamin, Child, Rewon, Gray, Scott, Radford, Alec, Wu, Jeffrey, Amodei, Dario
- **Venue/Type**: arXiv preprint arXiv:2001.08361
- **arXiv**: 2001.08361
- **Link**: https://arxiv.org/abs/2001.08361
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `研究背景}  近年来，以大语言模型（Large Language Model, LLM）为代表的新兴人工智能技术飞速发展，正深刻重塑科技产业格局。 LLM 凭借强大的自然语言理解与生成能力，在代码生成、内容创作、知识问答乃至复杂推理等任务中展现出前所未有的性能。 缩放定律（Scaling Law）是这一技术进步的核心驱动力： 大量实证研究表明，模型性能随参数量、训练数据量以及计算量的增加而持续提升，呈现出可预测的幂律关系。 这一规律不仅...`

### `hoffmann2022computeoptimal` — Training compute-optimal large language models (2022)
- **Authors**: Hoffmann, Jordan, Borgeaud, Sebastian, Mensch, Arthur, Buchatskaya, Elena, Cai, Trevor, Rutherford, Eliza, Casas, Diego de Las, Hendricks, Lisa Anne, et al.
- **Venue/Type**: arXiv preprint arXiv:2203.15556
- **arXiv**: 2203.15556
- **Link**: https://arxiv.org/abs/2203.15556
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 张量并行（TP）中的 All-Reduce 通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 预填充-解码分离（Prefill-Decode Disaggregation）中的 KV Cache 传输需求
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / CUDA IPC Memory Handle 性能优化
- **Thesis snippet(s) to verify**:
  - `研究表明，模型性能随参数量、训练数据量以及计算量的增加而持续提升，呈现出可预测的幂律关系。 这一规律不仅指导了模型架构与训练策略的设计，也推动了基础设施层面的系统性演进。  受 Scaling Law 驱动，模型参数量呈指数级增长。早期模型`
  - `Law）是这一技术进步的核心驱动力： 大量实证研究表明，模型性能随参数量、训练数据量以及计算量的增加而持续提升，呈现出可预测的幂律关系。 这一规律不仅指导了模型架构与训练策略的设计，也推动了基础设施层面的系统性演进。  受 Scaling`

### `shoeybi2019megatron` — Megatron-lm: Training multi-billion parameter language models using model parallelism (2019)
- **Authors**: Shoeybi, Mohammad, Patwary, Mostofa, Puri, Raul, LeGresley, Patrick, Casper, Jared, Catanzaro, Bryan
- **Venue/Type**: arXiv preprint arXiv:1909.08053
- **arXiv**: 1909.08053
- **Link**: https://arxiv.org/abs/1909.08053
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 张量并行（TP）中的 All-Reduce 通信需求
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `为部署如此大规模的模型，分布式推理已成为必要手段。当前主流的并行策略主要包括张量并行（Tensor Parallelism, TP）、 流水线并行（Pipeline Parallelism, PP）、数据并行（Data Parallel`
  - `如此大规模的模型，分布式推理已成为必要手段。当前主流的并行策略主要包括张量并行（Tensor Parallelism, TP）、 流水线并行（Pipeline Parallelism, PP）、数据并行（Data Parallelism,`

### `rajbhandari2020zero` — Zero: Memory optimizations toward training trillion parameter models (2020)
- **Authors**: Rajbhandari, Samyam, Rasley, Jeff, Ruwase, Olatunji, He, Yuxiong
- **Venue/Type**: SC20: International Conference for High Performance Computing, Networking, Storage and Analysis
- **arXiv**: 1910.02054
- **Link**: https://arxiv.org/abs/1910.02054
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
- **Thesis snippet(s) to verify**:
  - `RDMA Write / RDMA Read）直接访问该区域，实现“零拷贝”（zero-copy）的 GPU-to-GPU 通信。  GDR 的实现依赖于多个软硬件组件的紧密协同： \begin{itemize}     \item \t`

### `rasley2020deepspeed` — Deepspeed: System optimizations enable training deep learning models with over 100 billion parameters (2020)
- **Authors**: Rasley, Jeff, Rajbhandari, Samyam, Ruwase, Olatunji, He, Yuxiong
- **Venue/Type**: Proceedings of the 26th ACM SIGKDD international conference on knowledge discovery \& data mining
- **Link**: https://dl.acm.org/doi/10.1145/3394486.3406703
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
- **Thesis snippet(s) to verify**:
  - `研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadc...`

### `aminabadi2022deepspeedinference` — Deepspeed-inference: enabling efficient inference of transformer models at unprecedented scale (2022)
- **Authors**: Aminabadi, Reza Yazdani, Rajbhandari, Samyam, Awan, Ammar Ahmad, Li, Cheng, Li, Du, Zheng, Elton, Ruwase, Olatunji, Smith, Shaden, et al.
- **Venue/Type**: arXiv
- **arXiv**: 2207.00032
- **Link**: https://arxiv.org/abs/2207.00032
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
- **Thesis snippet(s) to verify**:
  - `大模型推理系统}  Transformer架构在推理阶段存在显著的性能瓶颈。 首先，标准注意力机制的计算复杂度随序列长度n呈平方方增长，即$O(n^2)$，当处理长文本时，计算成本会急剧上升， 导致推理速度变慢。其次，Transformer在推理过程中会产生的巨大内存消耗： 为了加速逐个生成新词元的自回归过程，避免重复计算先前已处理过的词元的K和V向量，通常采用空间换取时间的方式， 推理系统系统会将这些K和V矩阵缓存起来，形成所谓的“键...`

### `yu2022orca` — Orca: A distributed serving system for $\$Transformer-Based$\$ generative models (2022)
- **Authors**: Yu, Gyeong-In, Jeong, Joo Seong, Kim, Geon-Woo, Kim, Soojeong, Chun, Byung-Gon
- **Venue/Type**: 16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22)
- **Link**: https://www.usenix.org/system/files/osdi22-yu.pdf
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
- **Thesis snippet(s) to verify**:
  - `大模型推理系统}  Transformer架构在推理阶段存在显著的性能瓶颈。 首先，标准注意力机制的计算复杂度随序列长度n呈平方方增长，即$O(n^2)$，当处理长文本时，计算成本会急剧上升， 导致推理速度变慢。其次，Transformer在推理过程中会产生的巨大内存消耗： 为了加速逐个生成新词元的自回归过程，避免重复计算先前已处理过的词元的K和V向量，通常采用空间换取时间的方式， 推理系统系统会将这些K和V矩阵缓存起来，形成所谓的“键...`

### `kwon2023pagedattention` — Efficient Memory Management for Large Language Model Serving with PagedAttention (2023)
- **Authors**: Kwon, Woosuk, Li, Zhuohan, Zhuang, Siyuan, Sheng, Ying, Zheng, Lianmin, Yu, Cody Hao, Gonzalez, Joseph, Zhang, Hao, Stoica, Ion
- **Venue/Type**: arXiv
- **arXiv**: 2309.06180
- **DOI**: 10.1145/3600006.3613165
- **Link**: https://doi.org/10.1145/3600006.3613165
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 预填充-解码分离（Prefill-Decode Disaggregation）中的 KV Cache 传输需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 端到端测试 / 测试场景与系统设置
- **Thesis snippet(s) to verify**:
  - `）阶段，并将它们分离到不同的硬件资源上， 在预填充完成后，需要将产生的键值缓存（KV Cache）从预填充节点传输到解码节点，从而实现对两个阶段的独立优化。 PD 分离系统相比于 PD 混合（PD-Colocation）系统降低了首个令牌时`
  - `，提升了系统的令牌吞吐（Token Throughput）。 然而，PD分离中 KV Cache 的跨界点迁移对于网络传输性能提出了更高的要求，尤其依赖于高带宽、低时延的通信机制。  此外，在模型即服务(Model-as-a-Service`

### `zhong2024distserve` — DistServe: disaggregating prefill and decoding for goodput-optimized large language model serving (2024)
- **Authors**: Zhong, Yinmin, Liu, Shengyu, Chen, Junda, Hu, Jianbo, Zhu, Yibo, Liu, Xuanzhe, Jin, Xin, Zhang, Hao
- **Venue/Type**: Proceedings of the 18th USENIX Conference on Operating Systems Design and Implementation
- **arXiv**: 2401.09670
- **Link**: https://arxiv.org/abs/2401.09670
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 张量并行（TP）中的 All-Reduce 通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 预填充-解码分离（Prefill-Decode Disaggregation）中的 KV Cache 传输需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 3-design.tex :: \sysname 系统架构与设计 / RDMA 链路执行器设计 / SM-free 的跨节点通信
  - 3-design.tex :: \sysname 系统架构与设计 / 系统概述
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计 / 非阻塞任务提交
  - 4-implementation.tex :: \sysname 系统实现 / RDMA 链路执行器实现 / 运行阶段
  - 4-implementation.tex :: \sysname 系统实现 / 总体实现概述
  - 4-implementation.tex :: \sysname 系统实现 / 控制面事件机制
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `与延迟的关键瓶颈。  随着推理系统的不断演进，又进一步演进出了预填充-解码分离（Prefill-Decode Disaggregaton）推理架构。 该架构将推理流程分为计算密集型的预填充（Prefill）阶段和内存密集型的解码（Decod`
  - `Disaggregaton）推理架构。 该架构将推理流程分为计算密集型的预填充（Prefill）阶段和内存密集型的解码（Decode）阶段，并将它们分离到不同的硬件资源上， 在预填充完成后，需要将产生的键值缓存（KV Cache）从预填充节`

### `dao2022flashattention` — Flashattention: Fast and memory-efficient exact attention with io-awareness (2022)
- **Authors**: Dao, Tri, Fu, Dan, Ermon, Stefano, Rudra, Atri, R\'e, Christopher
- **Venue/Type**: Advances in neural information processing systems
- **arXiv**: 2205.14135
- **Link**: https://arxiv.org/abs/2205.14135
- **Used / Suggested insertion in thesis**:
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响
- **Thesis snippet(s) to verify**:
  - `置作为参数模拟真实推理场景， 并且设定较大批处理数量以确保计算负载充足； 选取 FlashAttention3 作为 Attention 算子实现，以获得 SOTA 的计算性能； 采用相对计算性能作为指标，即“通信并发下计算性能 / 无通信`

### `dao2023flashattention2` — Flashattention-2: Faster attention with better parallelism and work partitioning (2023)
- **Authors**: Dao, Tri
- **Venue/Type**: arXiv preprint arXiv:2307.08691
- **arXiv**: 2307.08691
- **Link**: https://arxiv.org/abs/2307.08691
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
- **Thesis snippet(s) to verify**:
  - `大模型推理系统}  Transformer架构在推理阶段存在显著的性能瓶颈。 首先，标准注意力机制的计算复杂度随序列长度n呈平方方增长，即$O(n^2)$，当处理长文本时，计算成本会急剧上升， 导致推理速度变慢。其次，Transformer在推理过程中会产生的巨大内存消耗： 为了加速逐个生成新词元的自回归过程，避免重复计算先前已处理过的词元的K和V向量，通常采用空间换取时间的方式， 推理系统系统会将这些K和V矩阵缓存起来，形成所谓的“键...`

### `shazeer2017moe` — Outrageously large neural networks: The sparsely-gated mixture-of-experts layer (2017)
- **Authors**: Shazeer, Noam, Mirhoseini, Azalia, Maziarz, Krzysztof, Davis, Andy, Le, Quoc, Hinton, Geoffrey, Dean, Jeff
- **Venue/Type**: arXiv preprint arXiv:1701.06538
- **arXiv**: 1701.06538
- **Link**: https://arxiv.org/abs/1701.06538
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
- **Thesis snippet(s) to verify**:
  - `行度； EP 则专为稀疏激活的混合专家（Mixture of Experts, MoE）架构设计，仅路由激活部分专家，需高效通信机制支持。 这些并行策略常组合使用，以在计算、内存与通信之间取得平衡。 然而，无论采用何种并行方式，设备间频繁的`
  - `Dispatch-Combine 通信需求}  专家并行（EP）针对混合专家（MoE）模型设计，将模型的 FFN 层拆分为多个独立“专家”（Expert），并分配至不同设备， 核心通信操作体现为“Dispatch（分发）”与“Combin`

### `lepikhin2020gshard` — Gshard: Scaling giant models with conditional computation and automatic sharding (2020)
- **Authors**: Lepikhin, Dmitry, Lee, HyoukJoong, Xu, Yuanzhong, Chen, Dehao, Firat, Orhan, Huang, Yanping, Krikun, Maxim, Shazeer, Noam, Chen, Zhifeng
- **Venue/Type**: arXiv preprint arXiv:2006.16668
- **arXiv**: 2006.16668
- **Link**: https://arxiv.org/abs/2006.16668
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / GPU 通信 / NVLink
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
- **Thesis snippet(s) to verify**:
  - `理的通信需求}  \todo{详细讲一下 TP 中 All-Reduce、EP Dispatch-Combine、以及Prefill-Decode Disaggregation 传 KV Cache 推理的通信需求。}  大模型推理的分布式`
  - `end{itemize}  \subsubsection{专家并行（EP）中的 Dispatch-Combine 通信需求}  专家并行（EP）针对混合专家（MoE）模型设计，将模型的 FFN 层拆分为多个独立“专家”（Expert），并分`

### `fedus2022switch` — Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity (2022)
- **Authors**: Fedus, William, Zoph, Barret, Shazeer, Noam
- **Venue/Type**: Journal of Machine Learning Research
- **arXiv**: 2101.03961
- **Link**: https://arxiv.org/abs/2101.03961
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / GPU 通信 / NVLink
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
- **Thesis snippet(s) to verify**:
  - `模型副本，不同请求路由到不同模型副本进行推理，提高了系统的并行度； EP 则专为稀疏激活的混合专家（Mixture of Experts, MoE）架构设计，仅路由激活部分专家，需高效通信机制支持。 这些并行策略常组合使用，以在计算、内存与`
  - `因此单 GPU 的 NVLink 总聚合带宽可达 900 GB/s。 当与 NVSwitch 交换芯片协同工作时，NVIDIA 构建了全连接（all-to-all）通信拓扑结构。 例如在 DGX H100 系统中，8 个 H100 GPU`

### `he2021fastmoe` — Fastmoe: A fast mixture-of-expert training system (2021)
- **Authors**: He, Jiaao, Qiu, Jiezhong, Zeng, Aohan, Yang, Zhilin, Zhai, Jidong, Tang, Jie
- **Venue/Type**: arXiv preprint arXiv:2103.13262
- **arXiv**: 2103.13262
- **Link**: https://arxiv.org/abs/2103.13262
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
- **Thesis snippet(s) to verify**:
  - `专家并行（EP）中的 Dispatch-Combine 通信需求}  专家并行（EP）针对混合专家（MoE）模型设计，将模型的 FFN 层拆分为多个独立“专家”（Expert），并分配至不同设备， 核心通信操作体现为“Dispatch（分发）”与“Combine（合并）”两个阶段，其需求与专家选择机制深度绑定。  MoE 模型的推理流程中，通信操作的逻辑如下：  \begin{enumerate}     \item Dispatch ...`

### `hwang2023tutel` — Tutel: Adaptive mixture-of-experts at scale (2023)
- **Authors**: Hwang, Changho, Cui, Wei, Xiong, Yifan, Yang, Ziyue, Liu, Ze, Hu, Han, Wang, Zilong, Salas, Rafael, et al.
- **Venue/Type**: Proceedings of Machine Learning and Systems
- **Link**: https://yzygitzh.github.io/assets/papers/hwang_mlsys_2023.pdf
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
- **Thesis snippet(s) to verify**:
  - `专家并行（EP）中的 Dispatch-Combine 通信需求}  专家并行（EP）针对混合专家（MoE）模型设计，将模型的 FFN 层拆分为多个独立“专家”（Expert），并分配至不同设备， 核心通信操作体现为“Dispatch（分发）”与“Combine（合并）”两个阶段，其需求与专家选择机制深度绑定。  MoE 模型的推理流程中，通信操作的逻辑如下：  \begin{enumerate}     \item Dispatch ...`

### `deepseek2025deepep` — DeepEP: High-Performance Expert-Parallel Communication Library (2025)
- **Authors**: DeepSeek-AI
- **Venue/Type**: \url{https://github.com/deepseek-ai/DeepEP}
- **Link**: https://github.com/deepseek-ai/DeepEP
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
- **Thesis snippet(s) to verify**:
  - `m, PP）、数据并行（Data Parallelism, DP）以及专家并行（Expert Parallelism, EP）。 TP 将注意力头（Attention Head）切分到多个设备上协同计算，并引入集合通信规约（AllReduc`
  - `理的通信需求}  \todo{详细讲一下 TP 中 All-Reduce、EP Dispatch-Combine、以及Prefill-Decode Disaggregation 传 KV Cache 推理的通信需求。}  大模型推理的分布式`

### `nvidia2025nccl` — NVIDIA Collective Communications Library (NCCL) Documentation (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/}
- **Link**: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 5-evaluation.tex :: 实验与评测
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 节点内 NVLink 通信
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 跨节点 RDMA 通信
  - 5-evaluation.tex :: 实验与评测 / 端到端测试 / 实验结果与分析
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 节点内通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `中的各种不同的通信需求，学术界和工业界提出了多种不同的 GPU 通信方案，包括 NCCL、NVSHMEM、UCCL-P2P、Mooncake 等。 在大模型推理系统中，通信库一方面需要对开发者提供易用的编程接口，另一方面需要针对不同的硬件拓`
  - `型推理系统的整体性能。  \section{研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多`

### `hu2024demystifyingnccl` — Demystifying NCCL: An In-Depth Analysis of GPU Communication Protocols and Algorithms (2025)
- **Authors**: Zhiyi Hu, Siyuan Shen, Tommaso Bonato, Sylvain Jeaugey, Cedell Alexander, Eric Spada, James Dinan, Jeff Hammond, Torsten Hoefler
- **Venue/Type**: 2025 IEEE Symposium on High-Performance Interconnects (HOTI)
- **Link**: https://api.semanticscholar.org/CorpusID:280048347
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 3-design.tex :: \sysname 系统架构与设计 / RDMA 链路执行器设计 / SM-free 的跨节点通信
  - 3-design.tex :: \sysname 系统架构与设计 / 系统概述
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计 / 最大在途量约束与粗粒度抢占
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / CUDA IPC Memory Handle 性能优化
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 跨进程通信内存访问机制
  - 4-implementation.tex :: \sysname 系统实现 / RDMA 链路执行器实现 / 初始化阶段
  - 4-implementation.tex :: \sysname 系统实现 / RDMA 链路执行器实现 / 运行阶段
  - 4-implementation.tex :: \sysname 系统实现 / 总体实现概述
  - 4-implementation.tex :: \sysname 系统实现 / 控制面事件机制
  - 4-implementation.tex :: \sysname 系统实现 / 运行时实现
  - 5-evaluation.tex :: 实验与评测
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 节点内 NVLink 通信
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 跨节点 RDMA 通信
  - 5-evaluation.tex :: 实验与评测 / 端到端测试 / 实验结果与分析
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 节点内通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `中的各种不同的通信需求，学术界和工业界提出了多种不同的 GPU 通信方案，包括 NCCL、NVSHMEM、UCCL-P2P、Mooncake 等。 在大模型推理系统中，通信库一方面需要对开发者提供易用的编程接口，另一方面需要针对不同的硬件拓`
  - `型推理系统的整体性能。  \section{研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多`

### `weingram2023xcclsurvey` — xCCL: A Survey of Industry-Led Collective Communication Libraries for Deep Learning (2023)
- **Authors**: Adam Weingram, Yuke Li, Hao Qi, Darren Ng, Liuyao Dai, Xiaoyi Lu
- **Venue/Type**: Journal of Computer Science and Technology
- **Link**: https://api.semanticscholar.org/CorpusID:257839221
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 主要研究内容
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 3-design.tex :: \sysname 系统架构与设计
  - 3-design.tex :: \sysname 系统架构与设计 / 设计目标
  - 4-implementation.tex :: \sysname 系统实现 / 应用接口和链路执行器封装
- **Thesis snippet(s) to verify**:
  - `ion{研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训`
  - `学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadcast 等操作，从而降低通`

### `sergeev2018horovod` — Horovod: fast and easy distributed deep learning in TensorFlow (2018)
- **Authors**: Alexander Sergeev, Mike Del Balso
- **Venue/Type**: ArXiv
- **arXiv**: 1802.05799
- **Link**: https://api.semanticscholar.org/CorpusID:3398835
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 3-design.tex :: \sysname 系统架构与设计 / RDMA 链路执行器设计 / SM-free 的跨节点通信
  - 3-design.tex :: \sysname 系统架构与设计 / 系统概述
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计 / 最大在途量约束与粗粒度抢占
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / CUDA IPC Memory Handle 性能优化
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 跨进程通信内存访问机制
  - 4-implementation.tex :: \sysname 系统实现 / RDMA 链路执行器实现 / 初始化阶段
  - 4-implementation.tex :: \sysname 系统实现 / RDMA 链路执行器实现 / 运行阶段
  - 4-implementation.tex :: \sysname 系统实现 / 总体实现概述
  - 4-implementation.tex :: \sysname 系统实现 / 控制面事件机制
  - 4-implementation.tex :: \sysname 系统实现 / 运行时实现
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 节点内 NVLink 通信
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 跨节点 RDMA 通信
  - 5-evaluation.tex :: 实验与评测 / 端到端测试 / 实验结果与分析
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 节点内通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `景中发挥着关键作用。  \begin{figure}[h]     \centering     \includegraphics[width=0.8\linewidth]{figures/nccl_rdma.png}     \capti`
  - `CE 的充分利用。  \begin{figure}[h]     \centering     \includegraphics[width=0.8\linewidth]{figures/nccl_nvlink.png}     \cap`

### `wang2020blink` — Blink: Fast and Generic Collectives for Distributed ML (2020)
- **Authors**: Wang, Guanhua, Venkataraman, Shivaram, Phanishayee, Amar, Devanur, Nikhil, Thelin, Jorgen, Stoica, Ion
- **Venue/Type**: Proceedings of Machine Learning and Systems
- **arXiv**: 1910.04940
- **Link**: https://proceedings.mlsys.org/paper_files/paper/2020/file/cd3a9a55f7f3723133fa4a13628cdf03-Paper.pdf
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `ion{研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训`
  - `学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadcast 等操作，从而降低通`

### `zhou2025uccl` — An Extensible Software Transport Layer for GPU Networking (2025)
- **Authors**: Yang Zhou, Zhongjie Chen, Ziming Mao, ChonLam Lao, Shuo Yang, Pravein G. Kannan, Jiaqi Gao, Yilong Zhao, et al.
- **Venue/Type**: ArXiv
- **arXiv**: 2504.17307
- **Link**: https://api.semanticscholar.org/CorpusID:278032890
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 主要研究内容
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
  - 3-design.tex :: \sysname 系统架构与设计 / 系统概述
  - 5-evaluation.tex :: 实验与评测 / 端到端测试 / 实验结果与分析
- **Thesis snippet(s) to verify**:
  - `术界和工业界提出了多种不同的 GPU 通信方案，包括 NCCL、NVSHMEM、UCCL-P2P、Mooncake 等。 在大模型推理系统中，通信库一方面需要对开发者提供易用的编程接口，另一方面需要针对不同的硬件拓扑和通信模式进行优化，以最`
  - `nvshmem-ibgda} \end{figure}  \paragraph{UCCL-P2P}  UCCL-P2P 项目是加州大学伯克利分校的 Sky Computing Lab 提出的高性能 KV Cache 传输引擎， 提供了 SM`

### `ucclproject2025repo` — UCCL: GPU Communication Library (Project Repository) (2025)
- **Authors**: uccl-project
- **Venue/Type**: \url{https://github.com/uccl-project/uccl}
- **Link**: https://github.com/uccl-project/uccl
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `术界和工业界提出了多种不同的 GPU 通信方案，包括 NCCL、NVSHMEM、UCCL-P2P、Mooncake 等。 在大模型推理系统中，通信库一方面需要对开发者提供易用的编程接口，另一方面需要针对不同的硬件拓扑和通信模式进行优化，以最`
  - `nvshmem-ibgda} \end{figure}  \paragraph{UCCL-P2P}  UCCL-P2P 项目是加州大学伯克利分校的 Sky Computing Lab 提出的高性能 KV Cache 传输引擎， 提供了 SM`

### `gloo2025repo` — Gloo: Collective Communications Library (2025)
- **Authors**: PyTorch Contributors
- **Venue/Type**: \url{https://github.com/pytorch/gloo}
- **Link**: https://github.com/pytorch/gloo
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
- **Thesis snippet(s) to verify**:
  - `研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadc...`

### `intel2024oneccl` — Intel oneAPI Collective Communications Library (oneCCL) Documentation (2024)
- **Authors**: Intel
- **Venue/Type**: \url{https://www.intel.com/content/www/us/en/developer/tools/oneapi/oneccl.html}
- **Link**: https://www.intel.com/content/www/us/en/developer/tools/oneapi/oneccl.html
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
- **Thesis snippet(s) to verify**:
  - `研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadc...`

### `amd2025rccl` — ROCm Communication Collectives Library (RCCL) Documentation (2025)
- **Authors**: AMD
- **Venue/Type**: \url{https://rocmdocs.amd.com/projects/rccl/en/latest/}
- **Link**: https://rocmdocs.amd.com/projects/rccl/en/latest/
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
- **Thesis snippet(s) to verify**:
  - `研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadc...`

### `shamis2015ucx` — UCX: An Open Source Framework for HPC Network APIs and Beyond (2015)
- **Authors**: Pavel Shamis, Manjunath Gorentla Venkata, M Graham Lopez, Matthew B. Baker, Oscar R. Hernandez, Yossi Itigin, Mike Dubman, Gilad Shainer, et al.
- **Venue/Type**: 2015 IEEE 23rd Annual Symposium on High-Performance Interconnects
- **Link**: https://api.semanticscholar.org/CorpusID:15710374
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
- **Thesis snippet(s) to verify**:
  - `作系统配置， 以及应用程序或通信库对 GDR API 的显式或隐式调用。 随着 UCX（Unified Communication X）等统一通信框架的普及，GDR 的部署门槛正逐步降低，已成为现代 AI 集群的标配通信能力。  GPU D`

### `papadopoulou2017ucxib` — A Performance Study of UCX over InfiniBand (2017)
- **Authors**: Nikela Papadopoulou, Lena Oden, Pavan Balaji
- **Venue/Type**: 2017 17th IEEE/ACM International Symposium on Cluster, Cloud and Grid Computing (CCGRID)
- **Link**: https://api.semanticscholar.org/CorpusID:1376678
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 跨节点 RDMA 通信
- **Thesis snippet(s) to verify**:
  - `称内存区域。  在跨节点 RDMA 场景下，NVSHMEM 引入了 IBGDA（InfiniBand GPU Direct Async） 以实现“GPU 直驱网卡”的通信关键路径。 图 ~\ref{fig:nvshmem-ibgda} 展示`
  - `系统通信效率而推出的一项关键技术。 它允许远程网络适配器（支持 RDMA 的 InfiniBand 或 RoCE 网卡）直接读写 GPU 显存，无需通过主机 CPU 或系统内存中转数据， 从而显著降低通信延迟、减少 CPU 负载，并提升整`

### `mpiforum2024mpi41` — MPI: A Message-Passing Interface Standard, Version 4.1 (2024)
- **Authors**: MPI Forum
- **Venue/Type**: MPI Forum Standard
- **Link**: https://www.mpi-forum.org/docs/mpi-4.1/mpi41-report.pdf
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
- **Thesis snippet(s) to verify**:
  - `GPU Direct RDMA, GDR）技术， 实现了纵向扩展（scale-up）网络与横向扩展（scale-out）网络的超高通信性能。  \subsection{NVLink}  NVLink 是 NVIDIA 开发的一种高性能芯片间互连技术， 专为在 GPU 之间以及 GPU 与支持 NVLink 的 CPU（例如基于 IBM POWER 架构的处理器）之间提供高带宽、低延迟的数据传输而设计。 相较于传统基于 PCIe 的通信机...`

### `sur2006rdmaread` — RDMA read based rendezvous protocol for MPI over InfiniBand: design alternatives and benefits (2006)
- **Authors**: Sayantan Sur, Hyun-Wook Jin, Lei Chai, Dhabaleswar Kumar Panda
- **Venue/Type**: ACM SIGPLAN Symposium on Principles \& Practice of Parallel Programming
- **Link**: https://api.semanticscholar.org/CorpusID:9250769
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / Sender-Initiated 控制模式与 Receiver 侧匹配
  - 3-design.tex :: \sysname 系统架构与设计 / RDMA 链路执行器设计 / Receiver-Initiated 控制模式
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 跨节点 RDMA 通信
- **Thesis snippet(s) to verify**:
  - `称内存区域。  在跨节点 RDMA 场景下，NVSHMEM 引入了 IBGDA（InfiniBand GPU Direct Async） 以实现“GPU 直驱网卡”的通信关键路径。 图 ~\ref{fig:nvshmem-ibgda} 展示`
  - `系统通信效率而推出的一项关键技术。 它允许远程网络适配器（支持 RDMA 的 InfiniBand 或 RoCE 网卡）直接读写 GPU 显存，无需通过主机 CPU 或系统内存中转数据， 从而显著降低通信延迟、减少 CPU 负载，并提升整`

### `nvidia2025gpudirectrdma` — GPUDirect RDMA (2025)
- **Authors**: NVIDIA
- **Venue/Type**: NVIDIA CUDA Documentation
- **Link**: https://docs.nvidia.com/cuda/pdf/GPUDirect_RDMA.pdf
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计
- **Thesis snippet(s) to verify**:
  - `铃”，触发 RNIC 工作流程。 RNIC 在收到 doorbell 后，利用 GPUDirect RDMA 直接从 GPU 内存中读取 WQ/WQE 与待传输数据， 完成跨节点传输，并将完成信息写回到位于（或可被映射到）GPU 内存的完成`
  - `行的拷贝任务（copy task）交由硬件进行数据传输。 尽管不同物理链路（如 GPUDirect RDMA、NVLink）具有完全不同的硬件特性与操作方式， 链路执行层在调度语义上保持严格统一： 所有链路执行器均遵循同一套抽象模型，而差异`

### `agostini2018gpudirectasync` — GPUDirect Async: Exploring GPU synchronous communication techniques for InfiniBand clusters (2018)
- **Authors**: Elena Agostini, Davide Rossetti, Sreeram Potluri
- **Venue/Type**: J. Parallel Distributed Comput.
- **Link**: https://api.semanticscholar.org/CorpusID:4650454
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
- **Thesis snippet(s) to verify**:
  - `PE 的对称内存区域。  在跨节点 RDMA 场景下，NVSHMEM 引入了 IBGDA（InfiniBand GPU Direct Async） 以实现“GPU 直驱网卡”的通信关键路径。 图 ~\ref{fig:nvshmem-ibg`
  - `现“GPU 直驱网卡”的通信关键路径。 图 ~\ref{fig:nvshmem-ibgda} 展示了 NVSHMEM IBGDA 跨节点 RDMA 通信流程。 与传统由 CPU 代理线程（proxy）提交/敲门铃不同，IBGDA 将控制面与`

### `nvidia2025cudipc` — CUDA Interprocess Communication (IPC) (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/inter-process-communication.html}
- **Link**: https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/inter-process-communication.html
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 主要研究内容
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / CUDA IPC Memory Handle 性能优化
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / 拷贝线程执行流程
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 请求匹配与提交
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 跨进程通信内存访问机制
  - 4-implementation.tex :: \sysname 系统实现 / 应用接口和链路执行器封装
  - 4-implementation.tex :: \sysname 系统实现 / 总体实现概述
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 节点内 NVLink 通信
- **Thesis snippet(s) to verify**:
  - `操作。 在实现节点内通信时，\sysname 利用基于 Cuda 进程间通信 （Cuda IPC）的 cudaMemcpy， 通过 GPU 的拷贝引擎（Copy Engine，CE）避免了直接 Load/Store 带来的 SM 资源占用。`
  - `ine}  在支持 NVLink 的单机多卡环境中，不同 GPU 之间可以通过 CUDA IPC 和 Peer Access 直接访问其他 GPU 内存。 \sysname 在初始化阶段为参与通信的 GPU 开启 Peer Access，并`

### `nvidia2025nvlink` — NVIDIA NVLink Interconnect (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://www.nvidia.com/en-us/data-center/nvlink/}
- **Link**: https://www.nvidia.com/en-us/data-center/nvlink/
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 2-background.tex :: 相关技术背景 / GPU 通信
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 2-background.tex :: 相关技术背景 / GPU 通信 / NVLink
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 预填充-解码分离（Prefill-Decode Disaggregation）中的 KV Cache 传输需求
  - 3-design.tex :: \sysname 系统架构与设计
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / Sender-Initiated 控制模式与 Receiver 侧匹配
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 后台拷贝线程与可扩展性
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 异步化与进一步优化
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 请求匹配算法在 NVLink 上的特化
  - 3-design.tex :: \sysname 系统架构与设计 / 应用接口层设计
  - 3-design.tex :: \sysname 系统架构与设计 / 系统概述
  - 3-design.tex :: \sysname 系统架构与设计 / 设计目标
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / CUDA IPC Memory Handle 性能优化
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / 拷贝线程执行流程
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 请求匹配与提交
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 跨进程通信内存访问机制
  - 4-implementation.tex :: \sysname 系统实现 / 应用接口和链路执行器封装
  - 4-implementation.tex :: \sysname 系统实现 / 总体实现概述
  - 4-implementation.tex :: \sysname 系统实现 / 运行时实现
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 节点内 NVLink 通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 节点内通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `IDIA GPU 架构进行了深度优化，充分利用 GPU 之间的高速互联技术（如 NVLink）、网络互联技术（如 RDMA、GPU Direct RDMA）， 实现数据在 GPU 内存之间的直接传输，显著减少冗余数据拷贝带来的性能损失。 此`
  - `多 GPU 通信时，存在大量的计算资源浪费， 图 ~\ref{fig:nccl-nvlink} 展示了 NCCL 节点内 NVLink 通信的控制流和数据流。 其通过 NVLink 进行多 GPU 通信时，启动大量 GPU 线程执行 Loa`

### `nvidia2018nvswitch` — NVIDIA NVSwitch Technical Overview (2018)
- **Authors**: NVIDIA
- **Venue/Type**: NVIDIA Whitepaper
- **Link**: https://images.nvidia.com/content/pdf/nvswitch-technical-overview.pdf
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / GPU 通信 / NVLink
- **Thesis snippet(s) to verify**:
  - `宽，因此单 GPU 的 NVLink 总聚合带宽可达 900 GB/s。 当与 NVSwitch 交换芯片协同工作时，NVIDIA 构建了全连接（all-to-all）通信拓扑结构。 例如在 DGX H100 系统中，8 个 H100 GP`
  - `例如在 DGX H100 系统中，8 个 H100 GPU 通过 6 个第二代 NVSwitch 芯片互连， 为任意两个 GPU 提供高达单向 225 GB/s、双向 450 GB/s 的通信带宽，有效消除了通信瓶颈。  在最新的 NVID`

### `maltenberger2022sortinginterconnects` — Evaluating Multi-GPU Sorting with Modern Interconnects (2022)
- **Authors**: Tobias Maltenberger, Ivan Ilic, Ilin Tolovski, Tilmann Rabl
- **Venue/Type**: Proceedings of the 2022 International Conference on Management of Data
- **Link**: https://api.semanticscholar.org/CorpusID:249578819
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 2-background.tex :: 相关技术背景 / GPU 通信
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 2-background.tex :: 相关技术背景 / GPU 通信 / NVLink
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 预填充-解码分离（Prefill-Decode Disaggregation）中的 KV Cache 传输需求
  - 3-design.tex :: \sysname 系统架构与设计
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / Sender-Initiated 控制模式与 Receiver 侧匹配
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 后台拷贝线程与可扩展性
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 异步化与进一步优化
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 请求匹配算法在 NVLink 上的特化
  - 3-design.tex :: \sysname 系统架构与设计 / 应用接口层设计
  - 3-design.tex :: \sysname 系统架构与设计 / 系统概述
  - 3-design.tex :: \sysname 系统架构与设计 / 设计目标
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / CUDA IPC Memory Handle 性能优化
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / 拷贝线程执行流程
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 请求匹配与提交
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 跨进程通信内存访问机制
  - 4-implementation.tex :: \sysname 系统实现 / RDMA 链路执行器实现 / 初始化阶段
  - 4-implementation.tex :: \sysname 系统实现 / 应用接口和链路执行器封装
  - 4-implementation.tex :: \sysname 系统实现 / 总体实现概述
  - 4-implementation.tex :: \sysname 系统实现 / 运行时实现
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 节点内 NVLink 通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 节点内通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `存）， 随后对映射到 CUDA 地址空间的 RNIC Doorbell 寄存器（PCIe BAR/MMIO）执行写操作以“敲门铃”，触发 RNIC 工作流程。 RNIC 在收到 doorbell 后，利用 GPUDirect RDMA 直接`
  - `IDIA GPU 架构进行了深度优化，充分利用 GPU 之间的高速互联技术（如 NVLink）、网络互联技术（如 RDMA、GPU Direct RDMA）， 实现数据在 GPU 内存之间的直接传输，显著减少冗余数据拷贝带来的性能损失。 此`

### `yang2025qwen3techreport` — Qwen3 Technical Report (2025)
- **Authors**: An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao, et al.
- **Venue/Type**: ArXiv
- **Link**: https://api.semanticscholar.org/CorpusID:278602855
- **Used / Suggested insertion in thesis**:
  - **TODO**: 未在旧 `references.md` 中找到对应条目；请根据正文实际引用位置补充。

### `deepseek2025r1modelcard` — DeepSeek-R1 Model Card (2025)
- **Authors**: DeepSeek-AI
- **Venue/Type**: \url{https://huggingface.co/deepseek-ai/DeepSeek-R1}
- **Link**: https://huggingface.co/deepseek-ai/DeepSeek-R1
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `卡 GPU 上完成推理； 而如今主流开源模型已普遍迈入百亿乃至千亿量级——例如 DeepSeek-R1-671B 包含 6710 亿参数，Qwen3-235B 也达到 2350 亿参数规模。 如此庞大的参数体量使得模型无法被单个 GPU 的`
  - `而如今主流开源模型已普遍迈入百亿乃至千亿量级——例如 DeepSeek-R1-671B 包含 6710 亿参数，Qwen3-235B 也达到 2350 亿参数规模。 如此庞大的参数体量使得模型无法被单个 GPU 的高带宽内存（High-B`

### `deepseekr1techreport2025` — DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning (2025)
- **Authors**: DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Jun-Mei Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, et al.
- **Venue/Type**: ArXiv
- **Link**: https://api.semanticscholar.org/CorpusID:275789950
- **Used / Suggested insertion in thesis**:
  - **TODO**: 未在旧 `references.md` 中找到对应条目；请根据正文实际引用位置补充。

### `devlin2019bert` — BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2019)
- **Authors**: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- **Venue/Type**: North American Chapter of the Association for Computational Linguistics
- **arXiv**: 1810.04805
- **Link**: https://api.semanticscholar.org/CorpusID:52967399
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `演进。  受 Scaling Law 驱动，模型参数量呈指数级增长。早期模型如 BERT（约 0.34B 参数）和 GPT-2（1.5B）尚可在单卡 GPU 上完成推理； 而如今主流开源模型已普遍迈入百亿乃至千亿量级——例如 DeepSee`

### `radford2019language` — Language models are unsupervised multitask learners (2019)
- **Authors**: Radford, Alec, Wu, Jeffrey, Child, Rewon, Luan, David, Amodei, Dario, Sutskever, Ilya, others
- **Venue/Type**: OpenAI blog
- **Link**: https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `驱动，模型参数量呈指数级增长。早期模型如 BERT（约 0.34B 参数）和 GPT-2（1.5B）尚可在单卡 GPU 上完成推理； 而如今主流开源模型已普遍迈入百亿乃至千亿量级——例如 DeepSeek-R1-671B 包含 6710`

### `nvidia2023tensorrtllmblog` — NVIDIA TensorRT-LLM Supercharges Large Language Model Inference on NVIDIA H100 GPUs (2023)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://developer.nvidia.com/blog/nvidia-tensorrt-llm-supercharges-large-language-model-inference-on-nvidia-h100-gpus/}
- **Link**: https://developer.nvidia.com/blog/nvidia-tensorrt-llm-supercharges-large-language-model-inference-on-nvidia-h100-gpus/
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
- **Thesis snippet(s) to verify**:
  - `大模型推理系统}  Transformer架构在推理阶段存在显著的性能瓶颈。 首先，标准注意力机制的计算复杂度随序列长度n呈平方方增长，即$O(n^2)$，当处理长文本时，计算成本会急剧上升， 导致推理速度变慢。其次，Transformer在推理过程中会产生的巨大内存消耗： 为了加速逐个生成新词元的自回归过程，避免重复计算先前已处理过的词元的K和V向量，通常采用空间换取时间的方式， 推理系统系统会将这些K和V矩阵缓存起来，形成所谓的“键...`

### `nvidia2025tensorrtllmrepo` — TensorRT-LLM: Open-source library for optimizing LLM inference (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://github.com/NVIDIA/TensorRT-LLM}
- **Link**: https://github.com/NVIDIA/TensorRT-LLM
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
- **Thesis snippet(s) to verify**:
  - `大模型推理系统}  Transformer架构在推理阶段存在显著的性能瓶颈。 首先，标准注意力机制的计算复杂度随序列长度n呈平方方增长，即$O(n^2)$，当处理长文本时，计算成本会急剧上升， 导致推理速度变慢。其次，Transformer在推理过程中会产生的巨大内存消耗： 为了加速逐个生成新词元的自回归过程，避免重复计算先前已处理过的词元的K和V向量，通常采用空间换取时间的方式， 推理系统系统会将这些K和V矩阵缓存起来，形成所谓的“键...`

### `nvidia2025tensorrtllmdocs` — TensorRT-LLM Documentation (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://nvidia.github.io/TensorRT-LLM/}
- **Link**: https://nvidia.github.io/TensorRT-LLM/
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
- **Thesis snippet(s) to verify**:
  - `大模型推理系统}  Transformer架构在推理阶段存在显著的性能瓶颈。 首先，标准注意力机制的计算复杂度随序列长度n呈平方方增长，即$O(n^2)$，当处理长文本时，计算成本会急剧上升， 导致推理速度变慢。其次，Transformer在推理过程中会产生的巨大内存消耗： 为了加速逐个生成新词元的自回归过程，避免重复计算先前已处理过的词元的K和V向量，通常采用空间换取时间的方式， 推理系统系统会将这些K和V矩阵缓存起来，形成所谓的“键...`

### `nvidia2025fastertransformer` — FasterTransformer (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://github.com/NVIDIA/FasterTransformer}
- **Link**: https://github.com/NVIDIA/FasterTransformer
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理系统
- **Thesis snippet(s) to verify**:
  - `大模型推理系统}  Transformer架构在推理阶段存在显著的性能瓶颈。 首先，标准注意力机制的计算复杂度随序列长度n呈平方方增长，即$O(n^2)$，当处理长文本时，计算成本会急剧上升， 导致推理速度变慢。其次，Transformer在推理过程中会产生的巨大内存消耗： 为了加速逐个生成新词元的自回归过程，避免重复计算先前已处理过的词元的K和V向量，通常采用空间换取时间的方式， 推理系统系统会将这些K和V矩阵缓存起来，形成所谓的“键...`

### `nvidia2025nvshmem` — NVSHMEM Documentation (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://docs.nvidia.com/nvshmem/api/index.html}
- **Link**: https://docs.nvidia.com/nvshmem/
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `同的通信需求，学术界和工业界提出了多种不同的 GPU 通信方案，包括 NCCL、NVSHMEM、UCCL-P2P、Mooncake 等。 在大模型推理系统中，通信库一方面需要对开发者提供易用的编程接口，另一方面需要针对不同的硬件拓扑和通信模`
  - `g:nccl-nvlink} \end{figure}  \paragraph{NVSHMEM} NVSHMEM 是一种面向 GPU 的、基于 OpenSHMEM 标准的单边通信库， 旨在为大规模异构系统中的 GPU 间通信提供高效、可扩展`

### `openshmem2020` — OpenSHMEM Application Programming Interface, Version 1.5 (2020)
- **Authors**: OpenSHMEM
- **Venue/Type**: OpenSHMEM Org
- **Link**: http://openshmem.org/site/sites/default/site_files/OpenSHMEM-1.5.pdf
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
- **Thesis snippet(s) to verify**:
  - `ragraph{NVSHMEM} NVSHMEM 是一种面向 GPU 的、基于 OpenSHMEM 标准的单边通信库， 旨在为大规模异构系统中的 GPU 间通信提供高效、可扩展的编程抽象。 其核心遵循 Partitioned Global`

### `ucx2025tagapi` — UCX UCT Tag Matching API Documentation (2025)
- **Authors**: UCX Project
- **Venue/Type**: \url{https://openucx.github.io/ucx/api/latest/html/group___u_c_t___t_a_g.html}
- **Link**: https://openucx.github.io/ucx/api/latest/html/group___u_c_t___t_a_g.html
- **Used / Suggested insertion in thesis**:
  - 3-design.tex :: \sysname 系统架构与设计 / 控制平面设计 / 消息匹配模块设计

### `rashti2008mpi_overlap` — Improving Communication Progress and Overlap in MPI Rendezvous Protocol over RDMA-enabled Interconnects (2008)
- **Authors**: Rashti, Mohammad J., Afsahi, Ahmad
- **Venue/Type**: 2008 22nd International Symposium on High Performance Computing Systems and Applications
- **DOI**: 10.1109/HPCS.2008.10
- **Link**: https://doi.org/10.1109/HPCS.2008.10
- **Used / Suggested insertion in thesis**:
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计 / 非阻塞任务提交
- **Thesis snippet(s) to verify**:
  - `的一个核心设计目标， 是确保链路执行器在高并发推理场景中始终保持“可推进性”（progress guarantee）， 即调度器在任何时刻都不因单个通道或单个大任务而阻塞整体调度过程。 非阻塞语义有三个重要性质：  \begin{enum`

### `parekh1993gps` — A generalized processor sharing approach to flow control in integrated services networks: the single-node case (1993)
- **Authors**: Parekh, Abhay K., Gallager, Robert G.
- **Venue/Type**: IEEE/ACM Trans. Netw.
- **DOI**: 10.1109/90.234856
- **Link**: https://doi.org/10.1109/90.234856
- **Used / Suggested insertion in thesis**:
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 请求匹配算法在 NVLink 上的特化
  - 3-design.tex :: \sysname 系统架构与设计 / 应用接口层设计
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计 / 最大在途量约束与粗粒度抢占
- **Thesis snippet(s) to verify**:
  - `这样的设计不仅使系统能够满足多种通信模式的不同性能需求，还为实现服务质量控制（QoS）奠定了关键基础。 相比仅依赖物理链路级别的调度策略，以逻辑通道为中心的优先级表达能够提供更细粒度的控制能力， 更适合现代大模型推理中高度动态且层次丰富的`
  - `的分层设计使系统在异构链路环境下保持高度一致性， 并为未来调度策略、流量控制和 QoS 机制的扩展奠定基础。  \section{链路执行层设计}  链路执行层是 \sysname 的核心，其功能是将应用接口层提交的抽象通信请求在逻辑上进行`

### `shah2025msccpp` — MSCCL++: Rethinking GPU Communication Abstractions for Cutting-edge AI Applications (2025)
- **Authors**: Aashaka Shah, Abhinav Jangda, Binyang Li, Caio Rocha, Changho Hwang, Jithin Jose, Madan Musuvathi, Olli Saarikivi, et al.
- **Venue/Type**: ArXiv
- **arXiv**: 2504.09014
- **Link**: https://api.semanticscholar.org/CorpusID:277781058
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
- **Thesis snippet(s) to verify**:
  - `研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadc...`

### `chen2025iccl` — An Efficient, Reliable and Observable Collective Communication Library in Large-scale GPU Training Clusters (2025)
- **Authors**: Ziteng Chen, Xiaohe Hu, Menghao Zhang, Yanmin Jia, Yan Zhang, Mingjun Zhang, Da Liu, Fangzheng Jiao, et al.
- **Venue/Type**: ArXiv
- **arXiv**: 2510.00991
- **Link**: https://api.semanticscholar.org/CorpusID:281706430
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / Sender-Initiated 控制模式与 Receiver 侧匹配
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 异步化与进一步优化
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 请求匹配算法在 NVLink 上的特化
  - 3-design.tex :: \sysname 系统架构与设计 / RDMA 链路执行器设计 / SM-free 的跨节点通信
  - 3-design.tex :: \sysname 系统架构与设计 / RDMA 链路执行器设计 / 请求匹配算法在 RDMA 上的特化
- **Thesis snippet(s) to verify**:
  - `Computing Lab 提出的高性能 KV Cache 传输引擎， 提供了 SM-free 的特性，轻量级的项目代码，以及易用性强的编程接口。 UCCL-P2P 使用 GPU Direct RDMA 技术实现高性能的跨节点 KV Cac`
  - `竞争，从而提升了大模型推理系统的整体性能。 但是 UCCL-P2P 目前仅支持 SM-free 的 RDMA 通信模式，目前不支持节点内多 GPU 之间通过 NVLink 进行 SM-free 的高带宽通信， 存在一定局限性，限制了其在大模`

### `nvidia2025nccl223blog` — New Scaling Algorithm and Initialization with NVIDIA Collective Communications Library 2.23 (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://developer.nvidia.com/blog/new-scaling-algorithm-and-initialization-with-nvidia-collective-communications-library-2-23/}
- **Link**: https://developer.nvidia.com/blog/new-scaling-algorithm-and-initialization-with-nvidia-collective-communications-library-2-23/
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
- **Thesis snippet(s) to verify**:
  - `研究现状}  \paragraph{NCCL} NCCL（NVIDIA Collective Communication Library）是 NVIDIA 推出的 GPU 集合通信库， 主要面向多 GPU 与多节点环境下的深度学习训练与高性能计算任务。 其核心目标是为分布式系统提供高效、可扩展的集合通信（Collective Communication）原语， 包括 All-Reduce、All-Gather、Reduce、Broadc...`

### `mpiprogress2024` — MPI Progress For All (2024)
- **Authors**: Hui Zhou, Robert Latham, Kenneth Raffenetti, Yanfei Guo, Rajeev Thakur
- **Venue/Type**: SC24-W: Workshops of the International Conference for High Performance Computing, Networking, Storage and Analysis
- **arXiv**: 2405.13807
- **Link**: https://api.semanticscholar.org/CorpusID:269983572
- **Used / Suggested insertion in thesis**:
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计 / 非阻塞任务提交
- **Thesis snippet(s) to verify**:
  - `的一个核心设计目标， 是确保链路执行器在高并发推理场景中始终保持“可推进性”（progress guarantee）， 即调度器在任何时刻都不因单个通道或单个大任务而阻塞整体调度过程。 非阻塞语义有三个重要性质：  \begin{enum`

### `zhai2023smartmoe` — SmartMoE: Efficiently Training Sparsely-Activated Models through Combining Offline and Online Parallelization (2023)
- **Authors**: Mingshu Zhai, Jiaao He, Zixuan Ma, Zan Zong, Runqing Zhang, Jidong Zhai
- **Venue/Type**: 2023 USENIX Annual Technical Conference (USENIX ATC 23)
- **Link**: https://www.usenix.org/conference/atc23/presentation/zhai
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 1-intro.tex :: 绪论 / 研究背景
  - 2-background.tex :: 相关技术背景 / 大模型推理 / Transformer架构
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 专家并行（EP）中的 Dispatch-Combine 通信需求
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 张量并行（TP）中的 All-Reduce 通信需求
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 异步化与进一步优化
  - 3-design.tex :: \sysname 系统架构与设计 / RDMA 链路执行器设计 / SM-free 的跨节点通信
  - 3-design.tex :: \sysname 系统架构与设计 / 应用接口层设计
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 跨节点 RDMA 通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `行度； EP 则专为稀疏激活的混合专家（Mixture of Experts, MoE）架构设计，仅路由激活部分专家，需高效通信机制支持。 这些并行策略常组合使用，以在计算、内存与通信之间取得平衡。 然而，无论采用何种并行方式，设备间频繁的`
  - `力提出更高要求。  为部署如此大规模的模型，分布式推理已成为必要手段。当前主流的并行策略主要包括张量并行（Tensor Parallelism, TP）、 流水线并行（Pipeline Parallelism, PP）、数据并行（Data`

### `temucin2022interconnectawareucx` — Accelerating Deep Learning Using Interconnect-Aware UCX Communication for MPI Collectives (2022)
- **Authors**: Temuçin, Yiltan Hassan, Sojoodi, Amir Hossein, Alizadeh, Pedram, Kitor, Benjamin, Afsahi, Ahmad
- **Venue/Type**: IEEE Micro
- **DOI**: 10.1109/MM.2022.3148670
- **Link**: https://doi.org/10.1109/MM.2022.3148670
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 2-background.tex :: 相关技术背景 / GPU 通信
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 2-background.tex :: 相关技术背景 / GPU 通信 / NVLink
  - 2-background.tex :: 相关技术背景 / 大模型推理 / 大模型推理的通信需求 / 预填充-解码分离（Prefill-Decode Disaggregation）中的 KV Cache 传输需求
  - 3-design.tex :: \sysname 系统架构与设计
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / SM-free 的单机多 GPU 通信：GPU Copy Engine
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / Sender-Initiated 控制模式与 Receiver 侧匹配
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 后台拷贝线程与可扩展性
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 异步化与进一步优化
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 请求匹配算法在 NVLink 上的特化
  - 3-design.tex :: \sysname 系统架构与设计 / 应用接口层设计
  - 3-design.tex :: \sysname 系统架构与设计 / 系统概述
  - 3-design.tex :: \sysname 系统架构与设计 / 设计目标
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / CUDA IPC Memory Handle 性能优化
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 数据面的实现 / 拷贝线程执行流程
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 请求匹配与提交
  - 4-implementation.tex :: \sysname 系统实现 / NVLink 链路执行器实现 / 跨进程通信内存访问机制
  - 4-implementation.tex :: \sysname 系统实现 / 应用接口和链路执行器封装
  - 4-implementation.tex :: \sysname 系统实现 / 总体实现概述
  - 4-implementation.tex :: \sysname 系统实现 / 运行时实现
  - 5-evaluation.tex :: 实验与评测 / 测试环境
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试
  - 5-evaluation.tex :: 实验与评测 / 点对点通信测试 / 节点内 NVLink 通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 节点内通信
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
  - 5-evaluation.tex :: 实验与评测 / 集合通信 AllGather 对计算的影响
- **Thesis snippet(s) to verify**:
  - `IDIA GPU 架构进行了深度优化，充分利用 GPU 之间的高速互联技术（如 NVLink）、网络互联技术（如 RDMA、GPU Direct RDMA）， 实现数据在 GPU 内存之间的直接传输，显著减少冗余数据拷贝带来的性能损失。 此`
  - `多 GPU 通信时，存在大量的计算资源浪费， 图 ~\ref{fig:nccl-nvlink} 展示了 NCCL 节点内 NVLink 通信的控制流和数据流。 其通过 NVLink 进行多 GPU 通信时，启动大量 GPU 线程执行 Loa`

### `nvidia2025gdrdoc` — GPUDirect RDMA Documentation (2025)
- **Authors**: NVIDIA
- **Venue/Type**: \url{https://docs.nvidia.com/cuda/gpudirect-rdma/}
- **Link**: https://docs.nvidia.com/cuda/gpudirect-rdma/
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计
- **Thesis snippet(s) to verify**:
  - `铃”，触发 RNIC 工作流程。 RNIC 在收到 doorbell 后，利用 GPUDirect RDMA 直接从 GPU 内存中读取 WQ/WQE 与待传输数据， 完成跨节点传输，并将完成信息写回到位于（或可被映射到）GPU 内存的完成`
  - `行的拷贝任务（copy task）交由硬件进行数据传输。 尽管不同物理链路（如 GPUDirect RDMA、NVLink）具有完全不同的硬件特性与操作方式， 链路执行层在调度语义上保持严格统一： 所有链路执行器均遵循同一套抽象模型，而差异`

### `nvidia2025gds` — GPUDirect Storage Overview Guide (2025)
- **Authors**: NVIDIA
- **Venue/Type**: NVIDIA Magnum IO
- **Link**: https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究现状
  - 3-design.tex :: \sysname 系统架构与设计 / 链路执行层设计
- **Thesis snippet(s) to verify**:
  - `铃”，触发 RNIC 工作流程。 RNIC 在收到 doorbell 后，利用 GPUDirect RDMA 直接从 GPU 内存中读取 WQ/WQE 与待传输数据， 完成跨节点传输，并将完成信息写回到位于（或可被映射到）GPU 内存的完成`
  - `行的拷贝任务（copy task）交由硬件进行数据传输。 尽管不同物理链路（如 GPUDirect RDMA、NVLink）具有完全不同的硬件特性与操作方式， 链路执行层在调度语义上保持严格统一： 所有链路执行器均遵循同一套抽象模型，而差异`

### `watanabe2024ucx_tofu` — Design and performance evaluation of UCX for the Tofu Interconnect D on Fugaku towards efficient multithreaded communication (2024)
- **Authors**: Watanabe, Yutaka, Tsuji, Miwako, Murai, Hitoshi, Boku, Taisuke, Sato, Mitsuhisa
- **Venue/Type**: J. Supercomput.
- **DOI**: 10.1007/s11227-024-06201-x
- **Link**: https://doi.org/10.1007/s11227-024-06201-x
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 主要研究内容
  - 1-intro.tex :: 绪论 / 研究现状
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
  - 3-design.tex :: \sysname 系统架构与设计 / NVLink 链路执行器设计 / 后台拷贝线程与可扩展性
  - 4-implementation.tex :: \sysname 系统实现 / 运行时实现
  - 5-evaluation.tex :: 实验与评测 / 通信对计算任务的影响 / 跨节点通信
- **Thesis snippet(s) to verify**:
  - `A 通信示意图}     \label{fig:nccl-rdma-proxy-thread} \end{figure}  然而 NCCL 在进行跨节点 RDMA 通信时，采用代理线程模式，引入不必要的同步开销。 图 ~\ref{fig:n`
  - `引入不必要的同步开销。 图 ~\ref{fig:nccl-rdma-proxy-thread} 展示了 NCCL 跨节点 RDMA 通信的控制流和数据流， 由于 NCCL 不支持 GPU 直接访问网卡资源，其进行跨节点 RDMA 通信时，`

### `mpiucx2024multipath` — Enhancing Intra-Node GPU-to-GPU Performance in MPI+UCX through Multi-Path Communication (2024)
- **Authors**: Sojoodi, Amirhossein, Temucin, Yiltan H., Afsahi, Ahmad
- **Venue/Type**: Proceedings of the 3rd International Workshop on Extreme Heterogeneity Solutions
- **DOI**: 10.1145/3642961.3643800
- **Link**: https://dl.acm.org/doi/10.1145/3642961.3643800
- **Used / Suggested insertion in thesis**:
  - 2-background.tex :: 相关技术背景 / GPU 通信 / GPU Direct RDMA
- **Thesis snippet(s) to verify**:
  - `GPU Direct RDMA, GDR）技术， 实现了纵向扩展（scale-up）网络与横向扩展（scale-out）网络的超高通信性能。  \subsection{NVLink}  NVLink 是 NVIDIA 开发的一种高性能芯片间互连技术， 专为在 GPU 之间以及 GPU 与支持 NVLink 的 CPU（例如基于 IBM POWER 架构的处理器）之间提供高带宽、低延迟的数据传输而设计。 相较于传统基于 PCIe 的通信机...`

### `deepseek2024v3modelcard` — DeepSeek-V3 Model Card (2024)
- **Authors**: DeepSeek-AI
- **Venue/Type**: \url{https://huggingface.co/deepseek-ai/DeepSeek-V3}
- **Link**: https://huggingface.co/deepseek-ai/DeepSeek-V3
- **Used / Suggested insertion in thesis**:
  - 1-intro.tex :: 绪论 / 研究背景
- **Thesis snippet(s) to verify**:
  - `研究背景}  近年来，以大语言模型（Large Language Model, LLM）为代表的新兴人工智能技术飞速发展，正深刻重塑科技产业格局。 LLM 凭借强大的自然语言理解与生成能力，在代码生成、内容创作、知识问答乃至复杂推理等任务中展现出前所未有的性能。 缩放定律（Scaling Law）是这一技术进步的核心驱动力： 大量实证研究表明，模型性能随参数量、训练数据量以及计算量的增加而持续提升，呈现出可预测的幂律关系。 这一规律不仅...`

### `deepseekai2024deepseekv3techreport` — DeepSeek-V3 Technical Report (2024)
- **Authors**: DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bing-Li Wang, Bochao Wu, Chengda Lu, Chenggang Zhao, et al.
- **Venue/Type**: ArXiv
- **Link**: https://api.semanticscholar.org/CorpusID:275118643
- **Used / Suggested insertion in thesis**:
  - **TODO**: 未在旧 `references.md` 中找到对应条目；请根据正文实际引用位置补充。
