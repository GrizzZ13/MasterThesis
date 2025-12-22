from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    qps = [1, 2, 3, 4]
    pickle_perf = [0.996, 0.997, 0.996, 0.991]
    nccl_perf = [0.986, 0.986, 0.986, 0.984]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axhline(1.0, color="gray", linestyle="--", linewidth=1, label="No communication")
    ax.plot(qps, pickle_perf, marker="o", label="Pickle")
    ax.plot(qps, nccl_perf, marker="s", label="NCCL")

    ax.set_xlabel("QP count")
    ax.set_ylabel("Relative compute throughput")
    ax.set_xticks(qps)
    ax.set_ylim(bottom=0, top=1.02)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "p2p_rdma_compute_impact_vs_qp.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
