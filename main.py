import pandas as pd
from packages.past_baiyo.baiyo_sushiki_samplenum import graph_baiyo_sushiki_num
from packages.baiyo.baiyo_sushiki_oneplate import graph_baiyo_oneplate
from packages.tools.merge_img import merge_img

if __name__ == "__main__":
    df = pd.read_csv("/Users/kotaro/PycharmProjects/tampaku/input/2024蛋白質代謝学生実習細胞増殖実験 - 増殖実験.csv",
                     skiprows=3)
    path1 = graph_baiyo_sushiki_num(df)
    path2 = graph_baiyo_oneplate(df)
    merge_img(path1, path2, "graph_new")


