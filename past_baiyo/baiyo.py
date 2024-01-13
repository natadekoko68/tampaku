import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import numpy as np
from scipy.optimize import curve_fit
from tools.preprocessing import preprocessing
from tools.funcs import func, func2, display_func, display_func2


def graph_baiyo(df):
    lst_3, lst_4, lst_5, _, _, _ = preprocessing(df)

    fig = plt.figure(figsize=(5, 7))
    fig.suptitle("異なる密度で播種した細胞の増殖曲線", size=15)

    x = np.linspace(1, 9, 30)

    # 1x10^3cells/mlで播種
    ax1 = fig.add_subplot(3, 1, 1)
    par3, cov3 = curve_fit(f=func, xdata=[1, 2, 4, 6, 9], ydata=lst_3)
    par3_2, cov3_2 = curve_fit(f=func2, xdata=[1, 2, 4, 6, 9], ydata=lst_3)

    plt.plot([1, 2, 4, 6, 9], lst_3, marker='o', color="#00108b")
    plt.plot(x, func(x, *par3), color="red", alpha=0.1, label="sigmoid")
    plt.plot(x, func2(x, *par3_2), color="forestgreen", alpha=0.9, label="exponential")

    plt.title("1x$10^{3}$cells/mlで播種", size=10)
    plt.ylabel("密度 (x$10^{3}$cells/ml)")
    plt.xticks([1, 2, 4, 6, 9], ["Day1", "Day2", "Day4", "Day6", "Day9"])
    plt.legend()
    # plt.yscale("log")


    # 1x10^4cells/mlで播種
    ax2 = fig.add_subplot(3, 1, 2, sharex=ax1)

    par4, cov4 = curve_fit(f=func, xdata=[1, 2, 4, 6, 9], ydata=lst_4)
    par4_2, cov4_2 = curve_fit(f=func2, xdata=[1, 2, 4, 6, 9], ydata=lst_4)

    plt.plot([1, 2, 4, 6, 9], lst_4, marker='o', color="#00108b")
    plt.plot(x, func(x, *par4), color="red", alpha=0.7, label="sigmoid")
    plt.plot(x, func2(x, *par4_2), color="forestgreen", alpha=0.1, label="exponential")

    plt.title("1x$10^{4}$cells/mlで播種", size=10)
    plt.ylabel("密度 (x$10^{4}$cells/ml)")
    plt.legend()
    # plt.yscale("log")

    x = np.linspace(1, 6, 30)

    # 1x10^5cells/mlで播種
    ax3 = fig.add_subplot(3, 1, 3, sharex=ax1)

    par5, cov5 = curve_fit(f=func, xdata=[1, 2, 4, 6], ydata=lst_5)
    par5_2, cov5_2 = curve_fit(f=func2, xdata=[1, 2, 4, 6], ydata=lst_5)

    plt.plot([1, 2, 4, 6], lst_5, marker='o', color="#00108b")
    plt.plot(x, func(x, *par5), color="red", alpha=0.7, label="sigmoid")
    plt.plot(x, func2(x, *par5_2), color="forestgreen", alpha=0.1, label="exponential")

    plt.title("1x$10^{5}$cells/mlで播種", size=10)
    plt.ylabel("密度 (x$10^{5}$cells/ml)")
    plt.legend(loc="upper left")
    # plt.yscale("log")


    # 最終処理&保存
    plt.tight_layout()
    plt.savefig("/Users/kotaro/PycharmProjects/tampaku/output/培養.jpg", dpi=500)
    plt.savefig("/Users/kotaro/Desktop/培養.jpg", dpi=500)

    plt.show()
    return "/Users/kotaro/PycharmProjects/tampaku/output/培養.jpg"

if __name__ == "__main__":
    df = pd.read_csv("/input/2024蛋白質代謝学生実習細胞増殖実験 - 増殖実験.csv",
                     skiprows=3)
    graph_baiyo(df)

