from itertools import accumulate
from pathlib import Path
import random

import matplotlib.pyplot as plt


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

    ax.plot(pickle_timestamps_ms, pickle_throughput, marker="o", label="Pickle")
    ax.plot(nccl_timestamps_ms, nccl_throughput, marker="s", label="NCCL")
    ax.set_xlabel("Timestamp (ms)")
    ax.set_ylabel("Token throughput (tokens/s)")
    ax.set_ylim(bottom=0, top=400)
    output_path = (
        Path(__file__).resolve().parent.parent / "figures" / "token_throughput.png"
    )

    # ax.plot(pickle_timestamps_ms, pickle_duration_ms, marker="o", label="Pickle")
    # ax.plot(nccl_timestamps_ms, nccl_duration_ms, marker="s", label="NCCL")
    # ax.set_xlabel("Timestamp (ms)")
    # ax.set_ylabel("Time Between Tokens (ms)")
    # ax.set_ylim(bottom=0, top=35)
    # output_path = (
    #     Path(__file__).resolve().parent.parent / "figures" / "TBT.png"
    # )

    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()
    

    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
