from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf"))
font_size = 14


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
    pickle_bw = [
        0.16,
        0.53,
        2.29,
        10.57,
        40.38,
        132,
        255.58,
        348.43,
        380.91,
        383.70,
        382.75,
        389.14,
    ]
    nccl_bw = [
        0.08,
        0.35,
        1.44,
        6.08,
        21.05,
        67,
        102.28,
        300.16,
        351.58,
        372.59,
        375.53,
        373.84,
    ]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(sizes, pickle_bw, marker="o", label="Pickle")
    ax.plot(sizes, nccl_bw, marker="s", label="NCCL")

    ax.set_xscale("log", base=2)
    ax.set_xticks(sizes)
    ax.set_xticklabels(size_labels, rotation=30, ha="right")
    ax.set_xlabel("消息大小", fontsize=font_size, fontproperties=font)
    ax.set_ylabel("有效带宽 (Gbps)", fontsize=font_size, fontproperties=font)
    ax.set_ylim(0, 420)
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "p2p_rdma_bandwidth_vs_size.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.22)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
