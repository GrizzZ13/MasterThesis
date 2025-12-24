出发点：sm-free 的 p2p 通信
- gpu direct rdma
- copy engine based nvlink

对比 baseline：nccl

核心卖点：不影响计算任务，并且带宽高

rdma p2p microbenchmark：
- [x] qp 数量比较少的情况下性能好，峰值带宽略高 390 Gbps vs 380 Gbps
- [ ] 对于「计算资源的占用」这一个比较没有显著优势：nccl 的 p2p 只 launch 两个 thread block，占两个 sm，影响计算kernel约 2-3%

nvlink p2p microbenchmark：
- [x] 带宽基本持平 375 GBps
- [x] 「计算资源占用显著减少」，nccl p2p 在大数据量下 launch 32 thread block，导致计算任务性能下降 15%

all-gather：
- [x] nccl RDMA 场景的 all gather 导致计算性能降低 10%
- [x] sm-free 预计性能基本持平的基础上没有影响

e2e：
- [ ] 基于 blitzscale 的数据，在使用 nvlink 进行 p2p 传输的时候不影响 p2p 性能（应该只影响 p99）
- [x] 使用 sm-free 的带宽聚合进行多源 multicast，相比于直接 nccl 的 broadcast 性能会好些

## Update

### microbenchmark

1. 
p2p rdma 的带宽折线图，横轴 number qps，纵轴 bandwidth，qp 少的时候 pickle 优于 nccl，qp 数量上去基本一致
横轴 qp 数量 1 2 3 4
1. 
p2p rdma 的带宽折线图，横轴 msg size，纵轴 bandwidth：？
横轴 msg size：4k，16k，64k，256k，1M，16M，64M，256M，1G，4G，16G
3.
p2p nvlink 的带宽画一个 size vs latency 的折线图，msg size 比较小的时候 pickle 比不过 nccl ，后边基本持平
横轴 msg size：4k，64k，1M，16M，256M，4G
4.
对比 nccl 和 pickle p2p rdma 对于计算的影响，折线图，由于 NCCL 默认只会使用两个 thread block 进行 rdma p2p，即使增大 qp 数量这里影响也不大
横轴 qp 数量，纵轴是相对计算性能（0 - 1）
5.
p2p nvlink 对于计算的影响，折线图，随着 msg size 增大，NCCL 使用的 thread block 最多占用到 32，对计算的影响比较大
横轴 msg size：4k，16k，64k，256k，1M，16M，64M，256M，1G，4G，16G，纵轴是相对计算性能（0 - 1）
6.
allgather 对于计算的影响，柱状图，两组四个bar，第一组是 normal 计算性能和 nccl allgather 影响下的计算性能，第二是 pickle allgather 影响下的计算性能
mpirun 启动八个进程进行测试，每个进程对应一个 gpu，每个 gpu 数据大小 1GB，后台跑一直跑 all gather
前台跑 batch size = 8, head num = 64,seq len = 4096,head_dim = 128 的 attention 进行计算测试当作 baseline，iters 统一 100，warmup 20轮
所有 all gather 的测试，都直接使用 world rank 当作 本地 gpu device，这里可以不用校验

### e2e

比较传模型参数时候对于 decode latency 的影响，画一个 timeline 图
