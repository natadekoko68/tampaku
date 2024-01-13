import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import seaborn as sns
import numpy as np
from scipy.optimize import curve_fit

df = pd.read_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 増殖実験.csv",
                 skiprows=3)


def func(x, L, x0):
    return L / (1 + np.exp(-(x - x0)))


def func2(x, a, b):
    return a * b ** x


col_names = ['班番号',
             'Day0',
             'Day1_10^3',
             'Day1_10^4',
             'Day1_10^5',
             'Day2_10^3',
             'Day2_10^4',
             'Day2_10^5',
             'Day4_10^3',
             'Day4_10^4',
             'Day4_10^5',
             'Day6_10^3',
             'Day6_10^4',
             'Day6_10^5',
             'Day9_10^3',
             'Day9_10^4',
             'Day9_10^5', ]

df = df.dropna(how='all', axis=1)
df.columns = col_names
df_describe = df.loc[len(df) - 2:, :]
df = df.loc[:len(df) - 3, :]
df_day1 = df.dropna(subset=['Day1_10^3', 'Day1_10^4', 'Day1_10^5', ], how='all').dropna(axis=1, how="all")
df_day2 = df.dropna(subset=['Day2_10^3', 'Day2_10^4', 'Day2_10^5', ], how='all').dropna(axis=1, how="all")
df_day4 = df.dropna(subset=['Day4_10^3', 'Day4_10^4', 'Day4_10^5', ], how='all').dropna(axis=1, how="all")
df_day6 = df.dropna(subset=['Day6_10^3', 'Day6_10^4', 'Day6_10^5', ], how='all').dropna(axis=1, how="all")
df_day9 = df.dropna(subset=['Day9_10^3', 'Day9_10^4', 'Day9_10^5', ], how='all').dropna(axis=1, how="all")

lst_3 = [df_day1["Day1_10^3"].mean(), df_day2["Day2_10^3"].mean(), df_day4["Day4_10^3"].mean(),
         df_day6["Day6_10^3"].mean(), df_day9["Day9_10^3"].mean()]
lst_4 = [df_day1["Day1_10^4"].mean(), df_day2["Day2_10^4"].mean(), df_day4["Day4_10^4"].mean(),
         df_day6["Day6_10^4"].mean(), df_day9["Day9_10^4"].mean()]
lst_5 = [df_day1["Day1_10^5"].mean(), df_day2["Day2_10^5"].mean(), df_day4["Day4_10^5"].mean(),
         df_day6["Day6_10^5"].mean()]

fig = plt.figure(figsize=(5, 7))
fig.suptitle("異なる密度で播種した細胞の増殖曲線", size=15)

x = np.linspace(1, 9, 30)

# 1x10^3cells/mlで播種
ax1 = fig.add_subplot(3, 1, 1)

plt.plot([1, 2, 4, 6, 9], lst_3, marker='o', color="#00108b")

plt.title("1x$10^{3}$cells/mlで播種", size=10)
plt.ylabel("密度 (x$10^{3}$cells/ml)")
plt.xticks([1, 2, 4, 6, 9], ["Day1", "Day2", "Day4", "Day6", "Day9"])
# plt.yscale("log")


# 1x10^4cells/mlで播種
ax2 = fig.add_subplot(3, 1, 2, sharex=ax1)
plt.plot([1, 2, 4, 6, 9], lst_4, marker='o', color="#00108b")
plt.title("1x$10^{4}$cells/mlで播種", size=10)
plt.ylabel("密度 (x$10^{4}$cells/ml)")
# plt.yscale("log")

x = np.linspace(1, 6, 30)

# 1x10^5cells/mlで播種
ax3 = fig.add_subplot(3, 1, 3, sharex=ax1)
plt.plot([1, 2, 4, 6], lst_5, marker='o', color="#00108b")

plt.title("1x$10^{5}$cells/mlで播種", size=10)
plt.ylabel("密度 (x$10^{5}$cells/ml)")
# plt.yscale("log")


# 最終処理&保存
plt.tight_layout()
plt.savefig("./output/培養_fittingなし.jpg", dpi=500)
plt.savefig("/Users/kotaro/Desktop/培養_fittingなし.jpg", dpi=500)

plt.show()
