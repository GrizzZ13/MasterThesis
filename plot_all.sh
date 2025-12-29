#!/usr/bin/env bash
set -euo pipefail

run_cmd() {
    echo ""
    echo ">>> $*"
    "$@"
}

run_cmd python scripts/plot_nvlink_p2p_compute_impact_vs_size.py
run_cmd python scripts/plot_nvlink_p2p_bandwidth_vs_size.py
run_cmd python scripts/plot_rdma_p2p_bandwidth_vs_qp.py
run_cmd python scripts/plot_rdma_p2p_bandwidth_vs_size.py
run_cmd python scripts/plot_rdma_p2p_compute_impact_vs_qp.py
run_cmd python scripts/plot_token_throughput.py
run_cmd python scripts/plot_allgather_size_vs_impact.py
run_cmd python scripts/plot_ipchandle_overhead.py