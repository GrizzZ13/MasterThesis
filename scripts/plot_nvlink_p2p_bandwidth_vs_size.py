from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf"))
font_size = 14


def main() -> None:
    sizes = [
        4 * 1024,
        64 * 1024,
        1 * 1024**2,
        # 4 * 1024**2,
        16 * 1024**2,
        256 * 1024**2,
        4 * 1024**3,
        64 * 1024**3,
    ]
    size_labels = [
        "4 KB",
        "64 KB",
        "1 MB",
        "16 MB",
        "256 MB",
        "4 GB",
        "64 GB",
    ]
    pickle_bw = [
        0.73,
        10.52,
        158.02,
        1564.72,
        2986,
        3181,
        3200,
    ]
    nccl_bw = [
        0.4,
        5.5,
        47,
        640,
        2600,
        3000,
        3000,
    ]

    pickle_wo_opt_bw = [
        0.004,
        0.067,
        1,
        16,
        233,
        1800,
        3016,
    ]

    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(sizes, pickle_bw, marker="o", label="Pickle")
    ax.plot(sizes, nccl_bw, marker="s", label="NCCL")
    ax.plot(sizes, pickle_wo_opt_bw, marker="^", label="Pickle w/o caching")

    ax.set_xscale("log", base=2)
    ax.set_xticks(sizes)
    ax.set_xticklabels(size_labels, rotation=30, ha="right")
    ax.set_xlabel("消息大小", fontsize=font_size, fontproperties=font)
    ax.set_ylabel("有效带宽 (Gbps)", fontsize=font_size, fontproperties=font)
    ax.set_ylim(0, 3500)
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "p2p_nvlink_bandwidth_vs_size.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.22)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
