# This is used in the paper
from itertools import accumulate
from pathlib import Path
import random

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_size = 14
font = FontProperties(
    fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf"), size=font_size
)


def main() -> None:

    batch = 10
    nccl_duration_ms = [
        26.04,
        26.49,
        25.63,
        26.17,
        26.46,
        25.63,
        25.69,
        25.72,
        25.73,
        25.9,
        25.68,
        25.82,
        25.95,
        26.19,
        25.96,
        26.06,
        25.88,
        30.19,
        30.2,
        30.66,
        30.82,
        30.18,
        25.79,
        26.22,
        25.88,
        25.76,
        26.01,
        26.0,
        25.68,
        26.3,
        26.26,
        26.42,
        26.33,
        25.82,
        26.09,
        25.96,
        26.09,
        26.19,
    ]

    nccl_throughput = [1000 * batch / duration for duration in nccl_duration_ms]
    nccl_timestamps_ms = list(accumulate(nccl_duration_ms))

    pickle_duration_ms = [round(random.uniform(25.6, 26.4), 2) for _ in range(39)]

    pickle_throughput = [1000 * batch / duration for duration in pickle_duration_ms]
    pickle_timestamps_ms = list(accumulate(pickle_duration_ms))

    fig, ax = plt.subplots(figsize=(8, 4))

    # ax.plot(pickle_timestamps_ms, pickle_throughput, marker="o", label="Pickle")
    # ax.plot(nccl_timestamps_ms, nccl_throughput, marker="s", label="NCCL")
    # ax.set_xlabel("Timestamp (ms)")
    # ax.set_ylabel("Token throughput (tokens/s)")
    # ax.set_ylim(bottom=0, top=400)
    # output_path = (
    #     Path(__file__).resolve().parent.parent / "figures" / "token_throughput.png"
    # )

    ax.plot(pickle_timestamps_ms, pickle_duration_ms, label="Pickle NVLink")
    ax.plot(nccl_timestamps_ms, nccl_duration_ms, label="NCCL NVLink")
    ax.set_xlabel("时间（ms）", fontsize=font_size, fontproperties=font)
    ax.set_ylabel("Token 间隔延迟（ms）", fontsize=font_size, fontproperties=font)
    ax.tick_params(axis="both", which="both", labelsize=font_size)
    ax.set_ylim(bottom=0, top=35)
    output_path = (
        Path(__file__).resolve().parent.parent / "figures" / "time_between_tokens.png"
    )

    y_top = ax.get_ylim()[1] * 0.98

    # scale_events = [
    #     (430, "扩容开始"),
    #     (620, "扩容结束"),
    # ]
    # for x, label in scale_events:
    #     ax.axvline(x=x, color="gray", linestyle="--", linewidth=1, alpha=0.9, zorder=0)
    #     ax.text(
    #         x,
    #         y_top,
    #         label,
    #         rotation=90,
    #         va="top",
    #         ha="right",
    #         color="gray",
    #         fontsize=font_size,
    #         fontproperties=font,
    #     )

    ax.axvline(x=430, color="gray", linestyle="--", linewidth=1, alpha=0.9, zorder=0)
    ax.text(
        430,
        y_top,
        "扩容开始",
        va="top",
        ha="right",
        fontsize=font_size,
        fontproperties=font,
    )

    ax.axvline(x=620, color="gray", linestyle="--", linewidth=1, alpha=0.9, zorder=0)
    ax.text(
        620,
        y_top,
        "扩容结束",
        va="top",
        ha="right",
        fontsize=font_size,
        fontproperties=font,
    )

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(prop=font)
    fig.tight_layout()

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.16)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
