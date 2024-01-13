import pandas as pd

def name_eraser(path):
    df = pd.read_csv(path)
    df = df[['人数確認番号', 'Unnamed: 1', '継代前の細胞数カウント', '継代後の細胞数カウント']]
    print(df)
    df.to_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 各自継代練習_name_erase.csv")

if __name__ == "__main__":
    name_eraser("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 各自継代練習.csv")