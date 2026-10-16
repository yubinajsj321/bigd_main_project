import pandas as pd
import matplotlib.pyplot as plt

test_watchlist_df = pd.read_csv("watchlist.csv")
print(test_watchlist_df["code"].tolist())

watchlist_df = pd.read_csv("watchlist.csv", dtype={"code": str})
print(watchlist_df["code"].tolist())
['005930', '000660', '005380']

check_dict = dict(zip(watchlist_df["code"], watchlist_df["name"]))
{'005930': '삼성전자', '000660': 'SK하이닉스', '005380': '현대자동차'}

print(check_dict)