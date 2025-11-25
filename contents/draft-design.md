Pickle 是一个针对 Point-to-Point 通信优化的 SM-free 通信库，主要有以下特点：

- 充分利用 scale-up 网络（NVLink）和 scale-out 网络（GPU Direct RDMA）传输数据
- NVLink 通过 GPU Copy Engine 实现 SM-free
- GPU Direct RDMA 通过网卡 DMA Engine 实现 SM-free

## NVLink 部分的 SM-free

https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/#memory-optimizations

节点内通过 cudaIpcOpenMemHandle 实现跨进程共享 GPU 显存

进程 A 和进程 B 首先通过共享内存，在 Host 中实现一个 SPSC Task Queue，进程 A 可以 push task，进程 B 可以 pop task

每一个 task 中存储了 ipchandle 的信息，以及拷贝内存的起始地址和长度，进程 B 收到

--- main thread ---

let event = PickleSender.send()
event.wait()

--- thread pool ---

loop {
let tasks, events = task_queue.pop()
for(task: tasks) {
    thread_local_task_enqueue.push()
}

if (thread_local_task_enqueue.front().is_some()) {
    qp.post_send(thread_local_task_enqueue.front().get_chunk())
}

}
