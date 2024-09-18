from dataclasses import replace

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy import ndarray
from pandas.core.methods.selectn import SelectNSeries

Data_frame = pd.read_csv('cs448b_ipasn.csv', encoding='shift-jis')

#Match_data = Data_frame[Data_frame[date[sum("f")]]].sort_values("date")

'''
07/01~09/30{
    Match_data = (Data_frame[Data_frame['date'] == "その日の日付"]).sort_values("r_asn")
}
にしたい。
07/01~09/30まで。
'''
Start_str = "2006-07-01"
Start_int = int(Start_str.replace("-", ""))

End_str = "2006-09-31"
End_int = int(End_str.replace("-", ""))
"""
for day in range(Start_int, End_int): ###スタートからエンドまで繰り返す。エンド自体は含まれないので07-32で作成した
    day_str = str(day) #文字型に変換
    day_str = day_str[:4] + "-" + day_str[4:6] + "-" + day_str[6:8] #-を入れる
    print((Data_frame[Data_frame['date'] == day_str])["f"].sum())
"""

#違った場合、何かしらの処理でday_str[4:6]に+1してStart_strから始める
"""
for day in range(Start_int, End_int): ###スタートからエンドまで繰り返す。エンド自体は含まれないので07-32で作成した
    if Start_int <= day < 20060732:
        print(day)
        day_str = str(day)  # 文字型に変換
        day_str = day_str[:4] + "-" + day_str[4:6] + "-" + day_str[6:8]  # -を入れる
        print((Data_frame[Data_frame['date'] == day_str])["f"].sum())
    elif 20060801 <= day <  20060832:
        print(day)
        day_str = str(day)  # 文字型に変換
        day_str = day_str[:4] + "-" + day_str[4:6] + "-" + day_str[6:8]  # -を入れる
        print((Data_frame[Data_frame['date'] == day_str])["f"].sum())
    elif 20060901 <= day <  20060931:
        print(day)
        day_str = str(day)  # 文字型に変換
        day_str = day_str[:4] + "-" + day_str[4:6] + "-" + day_str[6:8]  # -を入れる
        print((Data_frame[Data_frame['date'] == day_str])["f"].sum())

これでも出るけど、何回も変換したりしてなんかいや。どうにかしたい
"""
"""
for day in range(Start_int, End_int):
    if Start_int <= day < 20060732 or 20060801 <= day <  20060832 or 20060901 <= day < End_int:
        day_str = str(day)  # 文字型に変換
        day_str = day_str[:4] + "-" + day_str[4:6] + "-" + day_str[6:8]  # -を入れる
        print(day_str)
        print((Data_frame[Data_frame['date'] == day_str])["f"].sum())

どうにかした。次はグラフの生成
"""
"""
出したfの数をその都度保存したい
リストとかつくって入れてあげるとよさそう
for文の中に yylist = [] を入れると、for文内の繰り返し処理に巻き込まれて毎回リストの中身が空になる
だから外に出しておいて、for文内で求めたsumを都度入れてあげる(これがappend)
リストの中に保存するのはこれでできたので、グラフのXとYを決める
Xは日付毎がいいので Data_frame["date"] 

"""
xxlist = []
yylist = []
for day in range(Start_int, End_int):
    if Start_int <= day < 20060732 or 20060801 <= day <  20060832 or 20060901 <= day < End_int:
        day_str = str(day)  # 文字型に変換
        day_str = day_str[:4] + "-" + day_str[4:6] + "-" + day_str[6:8]  # -を入れる
        #print(day_str)
        #print((Data_frame[Data_frame['date'] == day_str])["f"].sum())
        xxlist.append(day_str)
        yylist.append((Data_frame[Data_frame['date'] == day_str])["f"].sum())

XGraph = pd.Series(xxlist)
YGraph = pd.Series(yylist)

print(XGraph.dtypes)
print(YGraph.dtypes)

plt.plot(XGraph,YGraph)
plt.show()
#グラフ描画

#Series（シリーズ）が1次元のデータ、DataFrame（データフレーム）が2次元のデータ
#今回Seriesにしたのは、pd.DataFrameでX軸を作成しようとしたらグラフ可するときにtypeerror unhashable type 'numpy.ndarray'ってでた。
#NumPy ndarrayはハッシュできない型。1次元のデータの場合ハッシュできるので1次元にした。
#どうやらlistはハッシュできないっぽい→https://www.educative.io/answers/typeerror-unhashable-type-numpyndarray

"""
GraphX = Data_frame["date"]
GraphY = y
plt.plot(GraphX, GraphY)
#Match_data = (Data_frame[Data_frame['date'] == day_str])["f"].sum():
"""

"""
GraphX = Match_data["day_str"]
GraphY = y
#X軸がr_asn,Y軸がf(セッション数)

plt.plot(GraphX,GraphY)
"""



