# This is used in the paper
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_size = 14
font = FontProperties(
    fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf"), size=font_size
)


def main() -> None:
    qps = [1, 2, 3, 4]
    pickle_bw = [271.77, 353.84, 375.74, 383.48]
    nccl_bw = [241.83, 323.54, 336.00, 371.20]

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(qps, pickle_bw, marker="o", label="Pickle")
    ax.plot(qps, nccl_bw, marker="s", label="NCCL")

    ax.set_xlabel("QP 数量", fontsize=font_size, fontproperties=font)
    ax.set_ylabel("有效带宽 (Gbps)", fontsize=font_size, fontproperties=font)
    ax.tick_params(axis="both", which="both", labelsize=font_size)
    ax.set_xticks(qps)
    ax.set_ylim(0, 420)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(prop=font)
    fig.tight_layout()

    output_path = (
        Path(__file__).resolve().parent.parent
        / "figures"
        / "p2p_rdma_bandwidth_vs_qp.png"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.subplots_adjust(bottom=0.14)
    fig.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")


if __name__ == "__main__":
    main()
