import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import numpy as np
from scipy.optimize import curve_fit
from packages.tools.preprocessing import preprocessing
from packages.tools.funcs import func, func2, display_func, display_func2


def graph_baiyo_oneplate(df: pd.DataFrame) -> str:
    lst_3, lst_4, lst_5, _, _, _ = preprocessing(df)

    fig = plt.figure(figsize=(6, 9.3))
    fig.suptitle("初期密度ごとの細胞増殖曲線", size=15)

    x = np.linspace(1, 9, 30)

    # 1x10^3cells/mlで播種
    par3_2, cov3_2 = curve_fit(f=func2, xdata=[1, 2, 4, 6, 9], ydata=np.array(lst_3))

    plt.plot([1, 2, 4, 6, 9], np.array(lst_3) * 1000, marker='o', color="#00108b")
    plt.plot(x, func2(x, *par3_2) * 1000, color="forestgreen", alpha=0.9,
             label=f"exponential ({display_func2(*par3_2)})")

    # 1x10^4cells/mlで播種
    par4, cov4 = curve_fit(f=func, xdata=[1, 2, 4, 6, 9], ydata=np.array(lst_4))

    plt.plot([1, 2, 4, 6, 9], np.array(lst_4) * 10000, marker='o', color="#00108b")
    plt.plot(x, func(x, *par4) * 10000, color="red", alpha=0.7, label=f"sigmoid ({display_func(*par4)})")

    x = np.linspace(1, 6, 30)

    par5, cov5 = curve_fit(f=func, xdata=[1, 2, 4, 6], ydata=np.array(lst_5))

    plt.plot([1, 2, 4, 6], np.array(lst_5) * 100000, marker='o', color="#00108b")
    plt.plot(x, func(x, *par5) * 100000, color="red", alpha=0.7, label=f"sigmoid ({display_func(*par5)})")

    plt.xlabel("時間(Day)")
    plt.ylabel("密度 (xcells/ml)")
    plt.xticks([1, 2, 4, 6, 9], [1, 2, 4, 6, 9])
    plt.legend(loc="upper left")
    plt.yscale("log")
    plt.ylim([10 ** 2, 10 ** 8])

    # 最終処理&保存
    plt.tight_layout()
    plt.savefig("/Users/kotaro/PycharmProjects/tampaku/output/培養_数式_oneplate.jpg", dpi=500)
    plt.savefig("/Users/kotaro/Desktop/培養_数式_oneplate.jpg", dpi=500)

    plt.show()
    return "/Users/kotaro/PycharmProjects/tampaku/output/培養_数式_oneplate.jpg"


if __name__ == "__main__":
    df = pd.read_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 増殖実験.csv",
                     skiprows=3)
    graph_baiyo_oneplate(df)
