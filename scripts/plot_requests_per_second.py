# This is used in the paper
from __future__ import annotations

import csv
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

font_size = 16
repo_root = Path(__file__).resolve().parent.parent

# ======= Input / output paths (edit here) =======
REQUEST_CSV = repo_root / "data" / "request.csv"
OUTPUT_PATH = repo_root / "figures" / "requests_per_second.png"


@dataclass(frozen=True)
class RequestBin:
    t: datetime
    count: int


def _parse_request_csv(path: Path) -> list[RequestBin]:
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row")
        missing = {"s_time", "request_count"} - set(reader.fieldnames)
        if missing:
            raise ValueError(
                f"CSV missing columns: {sorted(missing)}; got: {reader.fieldnames}"
            )

        rows: list[RequestBin] = []
        for row in reader:
            t = datetime.strptime(row["s_time"].strip(), "%Y-%m-%d %H:%M:%S")
            count = int(float(row["request_count"]))
            rows.append(RequestBin(t=t, count=count))
        rows.sort(key=lambda r: r.t)
        return rows


def main() -> None:
    try:
        import matplotlib.pyplot as plt
        from matplotlib.font_manager import FontProperties
        from matplotlib.ticker import MultipleLocator
    except ModuleNotFoundError as e:
        if e.name == "matplotlib" or (e.name and e.name.startswith("matplotlib.")):
            raise SystemExit(
                "Missing dependency: matplotlib. Install with: python3 -m pip install matplotlib"
            ) from e
        raise

    font = FontProperties(
        fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf")
    )

    rows = _parse_request_csv(REQUEST_CSV)
    if not rows:
        raise ValueError(f"No data rows found in {REQUEST_CSV}")

    t0 = rows[0].t
    counts_by_second: dict[int, int] = {}
    for r in rows:
        s = int((r.t - t0).total_seconds())
        counts_by_second[s] = counts_by_second.get(s, 0) + r.count

    max_s = max(counts_by_second)
    xs = list(range(max_s + 1))
    ys = [counts_by_second.get(s, 0) / 2 for s in xs]

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.bar(xs, ys, width=1.0, align="edge", color="#4C78A8", edgecolor="none")

    ax.set_xlabel("时间 (分钟)", fontsize=font_size, fontproperties=font)
    ax.set_ylabel("请求速率（请求/秒）", fontsize=font_size, fontproperties=font)
    ax.tick_params(axis="both", which="both", labelsize=font_size)
    ax.set_xlim(0, 300)
    ax.set_ylim(bottom=0)

    ax.set_xticks(
        [60, 120, 180, 240, 300],
        ["1:00", "2:00", "3:00", "4:00", "5:00"],
        fontproperties=font,
        fontsize=font_size,
    )
    ax.xaxis.set_minor_locator(MultipleLocator(10))

    ax.grid(True, axis="y", linestyle="--", alpha=0.4)
    fig.tight_layout()

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.18)
    fig.savefig(OUTPUT_PATH, dpi=300)
    print(f"Saved plot to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
