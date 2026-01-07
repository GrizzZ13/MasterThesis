# This is used in the paper
from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.gridspec import GridSpec

font_size = 14
repo_root = Path(__file__).resolve().parent.parent

TTFT_PICKLE_CSV = repo_root / "data" / "ttft_cdf_pickle.csv"
TTFT_NCCL_CSV = repo_root / "data" / "ttft_cdf_nccl.csv"
TBT_PICKLE_CSV = repo_root / "data" / "tbt_cdf_pickle.csv"
TBT_NCCL_CSV = repo_root / "data" / "tbt_cdf_nccl.csv"

OUTPUT_PATH = repo_root / "figures" / "ttft_tbt_cdf_pickle_vs_nccl.png"


@dataclass(frozen=True)
class CdfPoint:
    x_ms: float
    cdf: float


def _load_cdf_points(
    path: Path, lib: str, *, x_col: str, factor: float = 1.0
) -> list[CdfPoint]:
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        missing = {"lib", x_col, "cdf"} - set(reader.fieldnames)
        if missing:
            raise ValueError(
                f"CSV missing columns: {sorted(missing)}; got: {reader.fieldnames}"
            )

        points: list[CdfPoint] = []
        available_libs: set[str] = set()
        for row in reader:
            row_lib = row["lib"].strip()
            available_libs.add(row_lib)
            if row_lib != lib:
                continue
            points.append(
                CdfPoint(x_ms=float(row[x_col]) * factor, cdf=float(row["cdf"]))
            )

    if not points:
        raise ValueError(
            f'No rows found for lib="{lib}" in {path}. Available: {sorted(available_libs)}'
        )

    points.sort(key=lambda p: (p.x_ms, p.cdf))
    return points


def _plot_cdf(ax, points: list[CdfPoint], *, label: str, color: str) -> None:
    ax.step(
        [p.x_ms for p in points],
        [p.cdf for p in points],
        where="post",
        linewidth=1.8,
        label=label,
        color=color,
    )


def main() -> None:
    font = FontProperties(fname=str(repo_root / "SimHei.ttf"), size=font_size)
    ttft_factor = 0.5
    tbt_factor = 0.25
    ttft_pickle_points = _load_cdf_points(
        TTFT_PICKLE_CSV, "pickle", x_col="ttft_ms", factor=ttft_factor
    )
    ttft_nccl_points = _load_cdf_points(
        TTFT_NCCL_CSV, "nccl", x_col="ttft_ms", factor=ttft_factor
    )
    tbt_pickle_points = _load_cdf_points(
        TBT_PICKLE_CSV, "pickle", x_col="tbt_ms", factor=tbt_factor
    )
    tbt_nccl_points = _load_cdf_points(
        TBT_NCCL_CSV, "nccl", x_col="tbt_ms", factor=tbt_factor
    )
    fig = plt.figure(figsize=(12, 4))
    gs = GridSpec(1, 2, figure=fig, wspace=0.28)
    ax_ttft = fig.add_subplot(gs[0, 0])
    ax_tbt = fig.add_subplot(gs[0, 1], sharey=ax_ttft)

    colors = {
        "pickle": "#4C78A8",
        "nccl": "#F58518",
    }

    _plot_cdf(
        ax_ttft,
        ttft_pickle_points,
        label="Pickle",
        color=colors["pickle"],
    )
    _plot_cdf(
        ax_ttft,
        ttft_nccl_points,
        label="NCCL",
        color=colors["nccl"],
    )
    ax_ttft.set_title("TTFT CDF", fontsize=font_size, fontproperties=font)
    ax_ttft.set_xlabel(
        "首 Token 延迟 TTFT (ms)", fontsize=font_size, fontproperties=font
    )
    ax_ttft.set_ylabel("CDF", fontsize=font_size, fontproperties=font)
    ax_ttft.tick_params(axis="both", which="both", labelsize=font_size)
    ax_ttft.set_ylim(0, 1.0)
    ax_ttft.grid(True, linestyle="--", alpha=0.5)
    ax_ttft.legend(prop=font)

    _plot_cdf(
        ax_tbt,
        tbt_pickle_points,
        label="Pickle",
        color=colors["pickle"],
    )
    _plot_cdf(
        ax_tbt,
        tbt_nccl_points,
        label="NCCL",
        color=colors["nccl"],
    )
    ax_tbt.set_title("TBT CDF", fontsize=font_size, fontproperties=font)
    ax_tbt.set_xlabel(
        "Token 间隔延迟 TBT (ms)", fontsize=font_size, fontproperties=font
    )
    ax_tbt.tick_params(axis="both", which="both", labelsize=font_size)
    ax_tbt.grid(True, linestyle="--", alpha=0.5)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.16)
    fig.savefig(OUTPUT_PATH, dpi=300)
    print(f"Saved plot to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
