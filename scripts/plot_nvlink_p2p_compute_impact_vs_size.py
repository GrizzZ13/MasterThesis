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

    fig, (ax_top, ax_bot) = plt.subplots(
        2,
        1,
        sharex=True,
        figsize=(8, 4),
        gridspec_kw={"height_ratios": [3, 1], "hspace": 0.15},
    )

    ax_top.axhline(
        1.0, color="gray", linestyle="--", linewidth=1, label="No communication"
    )
    for ax in (ax_top, ax_bot):
        ax.plot(
            sizes, pickle_perf, marker="o", label="Pickle" if ax is ax_top else None
        )
        ax.plot(sizes, nccl_perf, marker="s", label="NCCL" if ax is ax_top else None)

    for ax in (ax_top, ax_bot):
        ax.set_xscale("log", base=2)
        ax.yaxis.set_major_locator(MultipleLocator(0.1))
        ax.grid(True, which="both", linestyle="--", alpha=0.5)
        ax.tick_params(axis="both", which="both", labelsize=font_size)

    ax_top.set_ylim(0.8, 1.02)
    ax_bot.set_ylim(0.0, 0.1)

    ax_top.spines["bottom"].set_visible(False)
    ax_bot.spines["top"].set_visible(False)
    ax_top.tick_params(labeltop=False)
    ax_bot.xaxis.tick_bottom()

    d = 0.008  # size of break marks
    kwargs = dict(transform=ax_top.transAxes, color="k", clip_on=False)
    ax_top.plot((-d, +d), (-d, +d), **kwargs)  # top-left
    ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right

    kwargs.update(transform=ax_bot.transAxes)
    ax_bot.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left
    ax_bot.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right

    ax_bot.set_xticks(sizes)
    ax_bot.set_xticklabels(
        size_labels, rotation=30, ha="right", fontsize=font_size, fontproperties=font
    )
    ax_bot.set_xlabel("消息大小", fontsize=font_size, fontproperties=font)
    ax_top.set_ylabel("相对计算性能", fontsize=font_size, fontproperties=font)

    ax_top.legend(
        loc="upper left", bbox_to_anchor=(0.02, 0.82), borderaxespad=0.0, prop=font
    )

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "p2p_nvlink_compute_impact_vs_size.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.22)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
