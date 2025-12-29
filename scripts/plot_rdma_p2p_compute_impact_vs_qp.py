from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator

font = FontProperties(fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf"))
font_size = 14


def main() -> None:
    qps = [1, 2, 3, 4]
    pickle_perf = [0.996, 0.997, 0.996, 0.991]
    nccl_perf = [0.986, 0.986, 0.986, 0.984]

    fig, (ax_top, ax_bot) = plt.subplots(
        2,
        1,
        sharex=True,
        figsize=(6, 4),
        gridspec_kw={"height_ratios": [2, 1], "hspace": 0.1},
    )

    ax_top.axhline(
        1.0, color="gray", linestyle="--", linewidth=1, label="No communication"
    )
    for ax in (ax_top, ax_bot):
        ax.plot(qps, pickle_perf, marker="o", label="Pickle" if ax is ax_top else None)
        ax.plot(qps, nccl_perf, marker="s", label="NCCL" if ax is ax_top else None)
        ax.yaxis.set_major_locator(MultipleLocator(0.04))
        ax.grid(True, linestyle="--", alpha=0.5)

    ax_top.set_ylim(0.9, 1.01)
    ax_bot.set_ylim(0.0, 0.05)

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

    ax_bot.set_xlabel("QP 数量", fontsize=font_size, fontproperties=font)
    ax_top.set_ylabel("相对计算性能", fontsize=font_size, fontproperties=font)
    ax_bot.set_ylabel("")
    ax_bot.set_xticks(qps)
    ax_top.legend()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "p2p_rdma_compute_impact_vs_qp.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.14)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
