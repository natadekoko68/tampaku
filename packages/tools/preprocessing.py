def preprocessing(df):
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

    sample_num_3 = [len(df_day1["Day1_10^3"].dropna()), len(df_day2["Day2_10^3"].dropna()),
                    len(df_day4["Day4_10^3"].dropna()),
                    len(df_day6["Day6_10^3"].dropna()), len(df_day9["Day9_10^3"].dropna())]
    sample_num_4 = [len(df_day1["Day1_10^4"].dropna()), len(df_day2["Day2_10^4"].dropna()),
                    len(df_day4["Day4_10^4"].dropna()),
                    len(df_day6["Day6_10^4"].dropna()), len(df_day9["Day9_10^4"].dropna())]
    sample_num_5 = [len(df_day1["Day1_10^5"].dropna()), len(df_day2["Day2_10^5"].dropna()),
                    len(df_day4["Day4_10^5"].dropna()),
                    len(df_day6["Day6_10^5"].dropna()), 0]

    return lst_3, lst_4, lst_5, sample_num_3, sample_num_4, sample_num_5
