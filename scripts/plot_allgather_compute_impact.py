from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    transports = ["NVLink", "RDMA"]
    nccl_perf = [0.858, 0.89]
    pickle_perf = [0.858, 0.99]
    positions = list(range(len(transports)))
    bar_width = 0.35

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.axhline(1.0, color="gray", linestyle="--", linewidth=1, label="Baseline compute")

    nccl_positions = [p - bar_width / 2 for p in positions]
    pickle_positions = [p + bar_width / 2 for p in positions]

    ax.bar(nccl_positions, nccl_perf, width=bar_width, label="NCCL")
    ax.bar(pickle_positions, pickle_perf, width=bar_width, label="Pickle")

    ax.set_xticks(positions)
    ax.set_xticklabels(transports)
    ax.set_ylabel("Relative compute throughput")
    ax.set_ylim(bottom=0, top=1.05)
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "allgather_compute_impact.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
