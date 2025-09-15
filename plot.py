import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np


if __name__ == '__main__':
    
    dataset = "deep1m256"

    iter = 100

    all_list = []

    with open("lid_weight_rank_"+dataset+".txt", "r") as f:
        cnt = int(f.readline().strip())
        for j in range(iter):
            results = []
            for i in range(cnt):
                line = f.readline()
                results.append(float(line.strip()))
            all_list.append(results)

    final_result = []
    for i in range(cnt):
        sum = 0
        for j in range(iter):
            sum += all_list[j][i]
        final_result.append(sum / iter)

    x = np.arange(0,len(final_result))
    y = np.array(final_result)

    # 绘制散点图
    plt.figure(figsize=(6,4))
    plt.scatter(x, y, c='blue', marker='o', s=1, alpha=0.7, label="Samples")

    plt.gca().xaxis.set_major_formatter(ScalarFormatter(useOffset=False))
    # 坐标轴和标签
    plt.xlabel("Rank", fontsize=12)
    plt.ylabel("Average sum of weight", fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)

    # 网格
    plt.grid(True, linestyle=":", alpha=0.6)

    # 图例
    plt.legend(fontsize=10)

    # 紧凑排版
    plt.tight_layout()

    # 保存
    plt.savefig("scatter"+dataset+".png", dpi=300)
    plt.show()
