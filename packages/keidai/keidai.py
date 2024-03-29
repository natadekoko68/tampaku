import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja
import seaborn as sns

matplotlib_fontja.japanize()

df = pd.read_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 各自継代練習_name_erase.csv")

df = df[df["人数確認番号"].notna()].reset_index(drop=True)
df = df.drop(["Unnamed: 1"], axis=1)
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
text = f"""平均(x 10$^{{{4}}}$cells/ml):
継代前: {df["継代前"].astype(float).mean():.2f}
継代後: {df["継代後"].astype(float).mean():.3f}
継代後/継代前: {df["継代後/継代前"].astype(float).mean():.5f}"""
plt.text(-0.48,
         0.6,
         text)
plt.tight_layout()
plt.savefig("/Users/kotaro/PycharmProjects/tampaku/output/継代.jpg", dpi=500)
plt.savefig("/Users/kotaro/Desktop/継代.jpg", dpi=500)
plt.show()
