from pathlib import Path

import matplotlib.pyplot as plt


def main() -> None:
    sizes = [
        4 * 1024,
        16 * 1024,
        64 * 1024,
        256 * 1024,
        1 * 1024**2,
        4 * 1024**2,
        16 * 1024**2,
        64 * 1024**2,
        256 * 1024**2,
        1 * 1024**3,
        4 * 1024**3,
        16 * 1024**3,
    ]
    size_labels = [
        "4 KB",
        "16 KB",
        "64 KB",
        "256 KB",
        "1 MB",
        "4 MB",
        "16 MB",
        "64 MB",
        "256 MB",
        "1 GB",
        "4 GB",
        "16 GB",
    ]
    pickle_perf = [
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        1.00,
        0.996,
        0.996,
        0.996,
    ]
    nccl_perf = [
        0.995,
        0.999,
        1.00,
        0.996,
        0.995,
        0.997,
        0.992,
        0.996,
        0.985,
        0.919,
        0.844,
        0.834,
    ]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axhline(1.0, color="gray", linestyle="--", linewidth=1, label="No communication")
    ax.plot(sizes, pickle_perf, marker="o", label="Pickle")
    ax.plot(sizes, nccl_perf, marker="s", label="NCCL")

    ax.set_xscale("log", base=2)
    ax.set_xticks(sizes)
    ax.set_xticklabels(size_labels, rotation=30, ha="right")
    ax.set_xlabel("Message size")
    ax.set_ylabel("Relative compute throughput")
    ax.set_ylim(bottom=0, top=1.02)
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "p2p_nvlink_compute_impact_vs_size.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
