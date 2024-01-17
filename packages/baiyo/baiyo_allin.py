import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import numpy as np
from scipy.optimize import curve_fit
from packages.tools.preprocessing import preprocessing
from packages.tools.funcs import func, func2, display_func, display_func2

matplotlib_fontja.japanize()

def graph(data: list, num: int, sample_num: list=[], curve=None, log: bool = False, sample_num_pos=-30):
    # fool proof
    if (not curve == "sigmoid") and (not curve == "exponential") and (not curve == None):
        raise ValueError("curve must be one of sigmoid, exponential, or None")
    if not 3 <= num <= 5:
        raise ValueError("num must be between 3 and 5")
    if len(data) == 5:
        x = np.linspace(1, 9, 30)
        xticks = [1, 2, 4, 6, 9]
    if len(data) == 4:
        x = np.linspace(1, 6, 30)
        xticks = [1, 2, 4, 6]

    # plot data
    plt.plot(xticks, data, marker='o', color="#00108b")

    # plot curve
    if curve == "sigmoid":
        par, _ = curve_fit(f=func, xdata=xticks, ydata=data)
        plt.plot(x, func(x, *par), color="red", alpha=0.8, label=f"sigmoid ({display_func(*par)})")
        plt.legend(loc="upper left")
    if curve == "exponential":
        par_2, _ = curve_fit(f=func2, xdata=xticks, ydata=data)
        plt.plot(x, func2(x, *par_2), color="forestgreen", alpha=0.9, label=f"exponential ({display_func2(*par_2)})")
        plt.legend(loc="upper left")

    # other
    plt.title(f"1x$10^{num}$cells/mlで播種", size=10)
    plt.xlabel("時間(Day)")
    plt.ylabel(f"密度 (x$10^{num}$cells/ml)")
    if log == True:
        plt.yscale("log")

    # print the number of samples
    if len(sample_num) > 0:
        for i in range(5):
            plt.text([1,2,4,6,9][i], sample_num_pos, f"n={sample_num[i]}", ha="center")




def graph_baiyo_sushiki_num(df: pd.DataFrame,
                            suptitle="初期密度ごとの細胞増殖曲線",
                            suptitle_size=15,
                            size=(6, 9.3)) -> str:
    """params
    :param df: pd.DataFrame 前処理を加えない状態
    :suptitle: str タイトル
    :suptitle_size: int タイトルの文字サイズ
    :size: tuple figureのサイズ
    :return: 仮想環境上での画像のPATH
    """
    lst_3, lst_4, lst_5, sample_num_3, sample_num_4, sample_num_5 = preprocessing(df)

    fig = plt.figure(figsize=size)
    fig.suptitle(suptitle, size=15)

    x = np.linspace(1, 9, 30)

    # 1x10^3cells/mlで播種
    ax1 = fig.add_subplot(3, 1, 1)
    graph(lst_3, 3, sample_num_3, log=False)#, curve="exponential"

    # 1x10^4cells/mlで播種
    ax2 = fig.add_subplot(3, 1, 2, sharex=ax1)
    graph(lst_4, 4, sample_num_4, log=False, sample_num_pos=-40)#, curve="sigmoid"

    x = np.linspace(1, 6, 30)

    # 1x10^5cells/mlで播種
    ax3 = fig.add_subplot(3, 1, 3, sharex=ax1)
    graph(lst_5, 5, sample_num_5, log=False, sample_num_pos=-15)#, curve="sigmoid"

    # 最終処理&保存
    plt.xticks([1, 2, 4, 6, 9], [1, 2, 4, 6, 9])
    plt.tight_layout()
    plt.savefig(f"/Users/kotaro/PycharmProjects/tampaku/output/{suptitle}.jpg", dpi=500)
    plt.savefig(f"/Users/kotaro/Desktop/{suptitle}.jpg", dpi=500)

    plt.show()
    return f"/Users/kotaro/PycharmProjects/tampaku/output/{suptitle}.jpg"


if __name__ == "__main__":
    df = pd.read_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 増殖実験.csv",
                     skiprows=3)
    graph_baiyo_sushiki_num(df, suptitle="初期密度ごとの細胞増殖曲線")
