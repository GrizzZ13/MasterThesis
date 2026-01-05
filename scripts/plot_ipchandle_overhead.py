# This is used in the paper
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator

font_size = 14
font = FontProperties(
    fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf"), size=font_size
)


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

    open_us = [
        1016.29,
        1061.16,
        1222.82,
        1108.97,
        1003.53,
        1284.14,
        1137.87,
        993.391,
        994.39,
        7493.73,
        7464.48,
        8042.55,
    ]

    close_us = [
        134.671,
        171.285,
        311.016,
        213.109,
        133.93,
        388.161,
        212.994,
        123.157,
        123.515,
        427.6,
        395.062,
        776.98,
    ]

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(sizes, open_us, marker="o", label="cudaIpcOpenMemHandle")
    ax.plot(sizes, close_us, marker="s", label="cudaIpcCloseMemHandle")

    ax.set_xscale("log", base=2)
    ax.set_xticks(sizes)
    ax.set_xticklabels(
        size_labels, rotation=30, ha="right", fontsize=font_size, fontproperties=font
    )

    ax.set_xlabel("缓冲区大小", fontsize=font_size, fontproperties=font)
    ax.set_ylabel("延迟 (微秒)", fontsize=font_size, fontproperties=font)
    ax.tick_params(axis="both", which="both", labelsize=font_size)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_locator(MultipleLocator(2000))

    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.legend(prop=font)

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "cuda_ipc_open_close_overhead_vs_size.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.22)
    fig.savefig(output_path, dpi=300)

    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
