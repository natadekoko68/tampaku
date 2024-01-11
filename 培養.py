import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import seaborn as sns
import numpy as np
from scipy.optimize import curve_fit

df = pd.read_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 増殖実験.csv",
                 skiprows=3)


# def sigmoid(x, a):
#     return 1.0 / (1.0 + np.exp(-a * x))
# def func_sigmoid(x,a,b,c):
#     return a * sigmoid(x-b, c)

def func_sigmoid(x,a,b):
    return a*b**x

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
             'Day9_10^5',]
df = df.dropna(how='all', axis=1)
df.columns = col_names
df_describe = df.loc[len(df)-2:,:]
# print(df_describe)
df = df.loc[:len(df)-3,:]
df_day1 = df.dropna(subset=['Day1_10^3', 'Day1_10^4', 'Day1_10^5',], how='all').dropna(axis=1, how="all")
df_day2 = df.dropna(subset=['Day2_10^3', 'Day2_10^4', 'Day2_10^5',], how='all').dropna(axis=1, how="all")
df_day4 = df.dropna(subset=['Day4_10^3', 'Day4_10^4', 'Day4_10^5',], how='all').dropna(axis=1, how="all")
df_day6 = df.dropna(subset=['Day6_10^3', 'Day6_10^4', 'Day6_10^5',], how='all').dropna(axis=1, how="all")
df_day9 = df.dropna(subset=['Day9_10^3', 'Day9_10^4', 'Day9_10^5',], how='all').dropna(axis=1, how="all")

lst_3 = [df_day1["Day1_10^3"].mean(), df_day2["Day2_10^3"].mean(), df_day4["Day4_10^3"].mean(), df_day6["Day6_10^3"].mean(), df_day9["Day9_10^3"].mean()]
lst_4 = [df_day1["Day1_10^4"].mean(), df_day2["Day2_10^4"].mean(), df_day4["Day4_10^4"].mean(), df_day6["Day6_10^4"].mean(), df_day9["Day9_10^4"].mean()]
lst_5 = [df_day1["Day1_10^5"].mean(), df_day2["Day2_10^5"].mean(), df_day4["Day4_10^5"].mean(), df_day6["Day6_10^5"].mean()]

fig = plt.figure(figsize=(5,7))

ax1 = fig.add_subplot(3, 1, 1)
plt.title("1x$10^{3}$/mlで播種well")
par3, cov3 = curve_fit(f=func_sigmoid, xdata=[1,2,4,6,9], ydata=lst_3)
x = np.linspace(1,9,30)
plt.plot(x, func_sigmoid(x, *par3), color="red")
plt.plot([1,2,4,6,9], lst_3, marker='o')
plt.xticks([1,2,4,6,9],["Day1","Day2","Day4","Day6","Day9"])
# plt.yscale("log")

ax2 = fig.add_subplot(3, 1, 2, sharex=ax1)
par4, cov4 = curve_fit(f=func_sigmoid, xdata=[1,2,4,6,9], ydata=lst_4)
plt.plot(x, func_sigmoid(x, *par4), color="red")
plt.title("1x$10^{4}$/mlで播種well")
plt.plot([1,2,4,6,9], lst_4, marker='o')
# plt.yscale("log")

ax3 = fig.add_subplot(3, 1, 3, sharex=ax1)
plt.title("1x$10^{5}$/mlで播種well")
par5, cov5 = curve_fit(f=func_sigmoid, xdata=[1,2,4,6], ydata=lst_5)
x = np.linspace(1,6,30)
plt.plot(x, func_sigmoid(x, *par5), color="red")
plt.plot([1,2,4,6], lst_5, marker='o')
# plt.yscale("log")

plt.tight_layout()
plt.savefig("./output/培養.jpg", dpi=300)
plt.show()
