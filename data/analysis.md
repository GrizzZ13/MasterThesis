## microbenchmark 测试

### 计划

1. 
p2p rdma 的带宽折线图，横轴 number qps，纵轴 bandwidth，qp 少的时候 pickle 优于 nccl，qp 数量上去基本一致
横轴 qp 数量 1 2 3 4
1. 
p2p rdma 的带宽折线图，横轴 msg size，纵轴 bandwidth：
横轴 msg size：4k，16k，64k，256k，1M，16M，64M，256M，1G，4G，16G
3.
p2p nvlink 的带宽画一个 size vs bw 的折线图，pickle 优于 nccl
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
 

### 结果整理

1) RDMA P2P 带宽 vs QP（消息 1GB）
QP	 Pickle (Gbps)	 NCCL (Gbps)
1	 271.77	 241.83
2	 353.84	 323.54
3	 375.74	 336.00
4	 383.48	 371.20
提示：QP 少时 Pickle 领先约 12%，QP≥3 后两者差距收敛在 ~3% 以内。

2) RDMA P2P 带宽 vs 消息大小（QP=4，消息从 4KB~16GB）
Size	 Pickle (Gbps)	 NCCL (Gbps)
4 KB	 0.16	 0.08
16 KB	 0.53	 0.35
64 KB	 2.29	 1.44
256 KB	 10.57	 6.08
1 MB	 40.38	 21.05
16 MB	 255.58	 72.28
64 MB	 348.43	 300.16
256 MB	 380.91	 351.58
1 GB	 383.70	 372.59
4 GB	 379.75	 375.53
16 GB	 389.14	 373.84
提示：64KB 以上 Pickle 全程高于 NCCL，1GB 附近差距已很小。

3) NVLink P2P BW vs 消息大小
Size	 Pickle Bw(Gbps)	 NCCL Bw(Gbps)
4 KB	 0.73	 0.4
64 KB	 10.5	 5.5
1 MB	 158	 47
16 MB	 1564	 640
256 MB	 2986	 2600
4 GB	 3181	 3000
64 GB    3200    3000

Pickle 性能优于 NCCL

4) RDMA P2P 对计算的影响 vs QP（相对计算性能，越接近 1 越好）
QP	 Pickle	 NCCL
1	 0.996	 0.986
2	 0.997	 0.986
3	 0.996	 0.986
4	 0.991	 0.984
提示：NCCL 由于只用两个 thread block，QP 提升对计算干扰几乎不变；Pickle 全程干扰更小。

5) NVLink P2P 对计算的影响 vs 消息大小（相对计算性能）
Size	 Pickle	 NCCL
4 KB	 1.004	 0.995
16 KB	 1.004	 0.999
64 KB	 1.002	 1.001
256 KB	 1.001	 0.989
1 MB	 1.004	 0.997
16 MB	 1.001	 0.992
64 MB	 1.003	 0.996
256 MB	 1.003	 0.985
1 GB	 0.996	 0.919
4 GB	 0.996	 0.844
16 GB	 0.996	 0.834
提示：Pickle 在所有尺寸下几乎不拖慢计算；NCCL 随消息增大 thread block 占用升高，计算性能显著掉到 0.84 左右（4GB+）。

6) Allgather 对计算的影响（8 进程/8 GPU，每 GPU 1GB）
- Baseline（无通信）计算性能：~751.6 TFLOPs/s
- Nvlink NCCL allgather 相对计算性能：0.858（8 个 rank 平均），计算下降约 14.2%
- Nvlink Pickle allgather 相对计算性能：0.858（单次测得），与 NCCL 相当
- RDMA NCCL allgather 相对计算性能：0.99
- RDMA Pickle allgather 相对计算性能：0.99（基本无影响）

## 附纯 cudaMemcpyAsync 性能

这里的 overhead 指的是 dst gpu open & close cudaIpcMemHandle_t 的开销

```csv
Chunk Size (Bytes), Async Without Overhead (ms), Async Without Overhead (GB/s), Sync Without Overhead (ms), Sync Without Overhead (GB/s), Sync With Overhead (ms), Sync With Overhead (GB/s)
4.00 KB, 0.0136128, 0.300893, 0.0193393, 0.211796, 8.42462, 0.000486194
16.00 KB, 0.014743, 1.1113, 0.0251432, 0.651627, 8.70093, 0.00188302
64.00 KB, 0.0115382, 5.6799, 0.0194492, 3.36961, 7.97466, 0.00821803
256.00 KB, 0.0127555, 20.5514, 0.0208738, 12.5585, 10.11, 0.0259293
1.00 MB, 0.0143203, 73.2229, 0.0190275, 55.1083, 8.26675, 0.126843
4.00 MB, 0.022112, 189.685, 0.030229, 138.751, 8.70646, 0.481746
16.00 MB, 0.0534982, 313.603, 0.0581128, 288.701, 7.98528, 2.10102
64.00 MB, 0.180696, 371.391, 0.187669, 357.591, 9.13961, 7.34264
256.00 MB, 0.684124, 392.378, 0.68881, 389.709, 8.41792, 31.8886
1.00 GB, 2.70833, 396.459, 2.70686, 396.674, 12.6076, 85.1665
4.00 GB, 10.7755, 398.586, 10.7781, 398.489, 19.1973, 223.728
16.00 GB, 43.2531, 397.194, 43.2576, 397.152, 51.6834, 332.406
64.00 GB, 173.152, 396.873, 173.155, 396.866, 181.93, 377.724
```

## cudaIpcMemHandle 的 overhead

(venv) root@k8s-172-31-70-8:/nvme/wht/projects/evaluation# CUDA_VISIBLE_DEVICES=6,7 mpirun -n 2 --allow-run-as-root ./build/bench_cudamemcpy 
Buffe size: 4.00 KB
Average cudaIpcOpenMemHandle time: 1016.29 us
Average cudaIpcCloseMemHandle time: 134.671 us
Buffe size: 16.00 KB
Average cudaIpcOpenMemHandle time: 1061.16 us
Average cudaIpcCloseMemHandle time: 171.285 us
Buffe size: 64.00 KB
Average cudaIpcOpenMemHandle time: 1222.82 us
Average cudaIpcCloseMemHandle time: 311.016 us
Buffe size: 256.00 KB
Average cudaIpcOpenMemHandle time: 1108.97 us
Average cudaIpcCloseMemHandle time: 213.109 us
Buffe size: 1.00 MB
Average cudaIpcOpenMemHandle time: 1003.53 us
Average cudaIpcCloseMemHandle time: 133.93 us
Buffe size: 4.00 MB
Average cudaIpcOpenMemHandle time: 1284.14 us
Average cudaIpcCloseMemHandle time: 388.161 us
Buffe size: 16.00 MB
Average cudaIpcOpenMemHandle time: 1137.87 us
Average cudaIpcCloseMemHandle time: 212.994 us
Buffe size: 64.00 MB
Average cudaIpcOpenMemHandle time: 993.391 us
Average cudaIpcCloseMemHandle time: 123.157 us
Buffe size: 256.00 MB
Average cudaIpcOpenMemHandle time: 994.39 us
Average cudaIpcCloseMemHandle time: 123.515 us
Buffe size: 1.00 GB
Average cudaIpcOpenMemHandle time: 8042.55 us
Average cudaIpcCloseMemHandle time: 776.98 us
Buffe size: 4.00 GB
Average cudaIpcOpenMemHandle time: 7493.73 us
Average cudaIpcCloseMemHandle time: 427.6 us
Buffe size: 16.00 GB
Average cudaIpcOpenMemHandle time: 7464.48 us
Average cudaIpcCloseMemHandle time: 395.062 us
(venv) root@k8s-172-31-70-8:/nvme/wht/projects/evaluation# 