# This is used in the paper
"""
transport,payload_bytes,relative_attn_perf,bandwidth_GBps
NVLink,4096,0.993401,1.1113
NVLink,16384,0.983883,6.53252
NVLink,65536,0.954558,20.0408
NVLink,262144,0.941737,14.3112
NVLink,1048576,0.939078,165.312
NVLink,4194304,0.920972,236.682
NVLink,16777216,0.904525,298.526
NVLink,67108864,0.896627,337.235
NVLink,268435456,0.884254,353.711
NVLink,1073741824,0.859989,361.024
NVLink,4294967296,0.849420,365.012
RDMA,4096,0.993894,0.488459
RDMA,16384,0.993491,0.417469
RDMA,65536,0.992760,0.751783
RDMA,262144,0.990437,3.22429
RDMA,1048576,0.989951,14.5908
RDMA,4194304,0.976744,37.5509
RDMA,16777216,0.960025,45.9593
RDMA,67108864,0.919375,47.9408
RDMA,268435456,0.904075,48.8201
RDMA,1073741824,0.899794,49.0838
RDMA,4294967296,0.899082,49.1684
"""

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator
from pathlib import Path
import random

# ======================
# Font config
# ======================
font_size = 14
font = FontProperties(
    fname=str(Path(__file__).resolve().parent.parent / "SimHei.ttf"), size=font_size
)

# ======================
# Data (pure Python list)
# ======================
nccl_nvlink_perf = [
    {"payload_bytes": 4096, "relative_attn_perf": 0.993401, "bandwidth_GBps": 1.1113},
    {"payload_bytes": 16384, "relative_attn_perf": 0.983883, "bandwidth_GBps": 6.53252},
    {"payload_bytes": 65536, "relative_attn_perf": 0.954558, "bandwidth_GBps": 20.0408},
    {
        "payload_bytes": 262144,
        "relative_attn_perf": 0.941737,
        "bandwidth_GBps": 14.3112,
    },
    {
        "payload_bytes": 1048576,
        "relative_attn_perf": 0.939078,
        "bandwidth_GBps": 165.312,
    },
    {
        "payload_bytes": 4194304,
        "relative_attn_perf": 0.920972,
        "bandwidth_GBps": 236.682,
    },
    {
        "payload_bytes": 16777216,
        "relative_attn_perf": 0.904525,
        "bandwidth_GBps": 298.526,
    },
    {
        "payload_bytes": 67108864,
        "relative_attn_perf": 0.896627,
        "bandwidth_GBps": 337.235,
    },
    {
        "payload_bytes": 268435456,
        "relative_attn_perf": 0.884254,
        "bandwidth_GBps": 353.711,
    },
    {
        "payload_bytes": 1073741824,
        "relative_attn_perf": 0.859989,
        "bandwidth_GBps": 361.024,
    },
    {
        "payload_bytes": 4294967296,
        "relative_attn_perf": 0.849420,
        "bandwidth_GBps": 365.012,
    },
]

nccl_rdma_perf = [
    {"payload_bytes": 4096, "relative_attn_perf": 0.993894, "bandwidth_GBps": 0.488459},
    {
        "payload_bytes": 16384,
        "relative_attn_perf": 0.993491,
        "bandwidth_GBps": 0.417469,
    },
    {
        "payload_bytes": 65536,
        "relative_attn_perf": 0.992760,
        "bandwidth_GBps": 0.751783,
    },
    {
        "payload_bytes": 262144,
        "relative_attn_perf": 0.990437,
        "bandwidth_GBps": 3.22429,
    },
    {
        "payload_bytes": 1048576,
        "relative_attn_perf": 0.989951,
        "bandwidth_GBps": 14.5908,
    },
    {
        "payload_bytes": 4194304,
        "relative_attn_perf": 0.976744,
        "bandwidth_GBps": 37.5509,
    },
    {
        "payload_bytes": 16777216,
        "relative_attn_perf": 0.960025,
        "bandwidth_GBps": 45.9593,
    },
    {
        "payload_bytes": 67108864,
        "relative_attn_perf": 0.919375,
        "bandwidth_GBps": 47.9408,
    },
    {
        "payload_bytes": 268435456,
        "relative_attn_perf": 0.904075,
        "bandwidth_GBps": 48.8201,
    },
    {
        "payload_bytes": 1073741824,
        "relative_attn_perf": 0.899794,
        "bandwidth_GBps": 49.0838,
    },
    {
        "payload_bytes": 4294967296,
        "relative_attn_perf": 0.899082,
        "bandwidth_GBps": 49.1684,
    },
]


# ======================
# Helper
# ======================
def bytes_to_label(n: int) -> str:
    if n < 1024:
        return f"{n} B"
    if n < 1024**2:
        return f"{n//1024} KB"
    if n < 1024**3:
        mb = n / (1024**2)
        if abs(mb - round(mb)) < 1e-9:
            return f"{int(round(mb))} MB"
        return f"{mb:.1f} MB"
    gb = n / (1024**3)
    if abs(gb - round(gb)) < 1e-9:
        return f"{int(round(gb))} GB"
    return f"{gb:.1f} GB"


# ======================
# Prepare plot data
# ======================
nvlink_sizes = [d["payload_bytes"] for d in nccl_nvlink_perf]
nvlink_perf = [d["relative_attn_perf"] for d in nccl_nvlink_perf]

rdma_sizes = [d["payload_bytes"] for d in nccl_rdma_perf]
rdma_perf = [d["relative_attn_perf"] for d in nccl_rdma_perf]

sizes = nvlink_sizes
size_labels = [bytes_to_label(s) for s in sizes]

# Placeholder pickle data (to be replaced later)
pickle_nvlink_perf = [random.uniform(0.99, 1.002) for _ in nvlink_sizes]
pickle_rdma_perf = [random.uniform(0.99, 1.002) for _ in rdma_sizes]

# ======================
# Plot
# ======================
fig, (ax_top, ax_bot) = plt.subplots(
    2,
    1,
    sharex=True,
    figsize=(7, 4),
    gridspec_kw={"height_ratios": [3, 1.2], "hspace": 0.15},
)

# ---- No communication ----
ax_top.axhline(
    1.0, color="gray", linestyle="--", linewidth=1, label="No communication"
)

# ---- Pickle NVLink ----
ax_top.plot(
    nvlink_sizes,
    pickle_nvlink_perf,
    marker="^",
    label="Pickle NVLink",
)
ax_bot.plot(
    nvlink_sizes,
    pickle_nvlink_perf,
    marker="^",
)

# ---- NVLink ----
ax_top.plot(
    nvlink_sizes,
    nvlink_perf,
    marker="o",
    label="NCCL NVLink",
)
ax_bot.plot(
    nvlink_sizes,
    nvlink_perf,
    marker="o",
)

# ---- Pickle RDMA ----
ax_top.plot(
    rdma_sizes,
    pickle_rdma_perf,
    marker="D",
    label="Pickle RDMA",
)
ax_bot.plot(
    rdma_sizes,
    pickle_rdma_perf,
    marker="D",
)

# ---- RDMA ----
ax_top.plot(
    rdma_sizes,
    rdma_perf,
    marker="s",
    label="NCCL RDMA",
)
ax_bot.plot(
    rdma_sizes,
    rdma_perf,
    marker="s",
)

# ======================
# Axes config
# ======================
for ax in (ax_top, ax_bot):
    ax.set_xscale("log", base=2)
    ax.yaxis.set_major_locator(MultipleLocator(0.1))
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.tick_params(axis="both", which="both", labelsize=font_size)

ax_top.set_ylim(0.8, 1.02)
ax_bot.set_ylim(0.0, 0.1)

# Hide spines between axes
ax_top.spines["bottom"].set_visible(False)
ax_bot.spines["top"].set_visible(False)
ax_top.tick_params(labeltop=False)
ax_bot.xaxis.tick_bottom()

# Diagonal break marks
d = 0.008
kwargs = dict(transform=ax_top.transAxes, color="k", clip_on=False)
ax_top.plot((-d, +d), (-d, +d), **kwargs)
ax_top.plot((1 - d, 1 + d), (-d, +d), **kwargs)

kwargs.update(transform=ax_bot.transAxes)
ax_bot.plot((-d, +d), (1 - d, 1 + d), **kwargs)
ax_bot.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)

# X ticks / labels
ax_bot.set_xticks(sizes)
ax_bot.set_xticklabels(
    size_labels, rotation=30, ha="right", fontsize=font_size, fontproperties=font
)

# Labels
ax_bot.set_xlabel("消息大小", fontsize=font_size, fontproperties=font)
ax_top.set_ylabel("相对计算性能", fontsize=font_size, fontproperties=font)

handles, labels = ax_top.get_legend_handles_labels()
fig.legend(
    handles,
    labels,
    loc="upper center",
    bbox_to_anchor=(0.5, 0.99),
    ncol=3,
    frameon=False,
    prop=font,
)

# ======================
# Save
# ======================
output_path = (
    Path(__file__).resolve().parent.parent
    / "figures"
    / "relative_perf_vs_msg_size_broken_y.png"
)
fig.subplots_adjust(bottom=0.22, top=0.82)
fig.savefig(output_path, dpi=300)
print(f"Saved plot to {output_path}")
