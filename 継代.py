import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import seaborn as sns

df = pd.read_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 各自継代練習.csv")

df = df[df["人数確認番号"].notna()].reset_index(drop=True)
df = df.drop(["Unnamed: 1", "Unnamed: 2"], axis=1)
df["人数確認番号"] = df["人数確認番号"].astype(int)
df = df.rename(columns={"人数確認番号": "番号",
                        "継代前の細胞数カウント": "継代前",
                        "継代後の細胞数カウント": "継代後"})
df = df.dropna(subset=["継代前"])
df = df.dropna(subset=["継代後"])
df["継代後/継代前"] = df["継代後"].astype(float)/df["継代前"].astype(float)
fig = plt.figure(figsize=(4, 6))
sns.violinplot(data=df, y="継代後/継代前", inner='quartile', color="white")
sns.swarmplot(data=df, y="継代後/継代前", color="skyblue")
plt.title("継代実験の結果")
plt.tick_params(bottom=False)
plt.text(-0.48, 0.6, f"Ave\n継代前:{df["継代前"].astype(float).mean():.2f}\n継代後:{df["継代後"].astype(float).mean():.3f}\n継代後/継代前:{df["継代後/継代前"].astype(float).mean():.5f}")
plt.tight_layout()
plt.savefig("./output/継代.jpg", dpi=300)
plt.show()
