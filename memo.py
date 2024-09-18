import matplotlib.pyplot as plt #グラフを作成するやつ。asは名前つける
import pandas as pd #csvとかのデータを操作(取り出したり並び変えたり変換したり)するやつ
from pandas.core.interchange.dataframe_protocol import DataFrame

#csvデータはここから引用
#https://www.kaggle.com/datasets/crawford/computer-network-traffic/data

Data_frame = pd.read_csv('cs448b_ipasn.csv', encoding='shift-jis')
#pd内にあるread_csvって機能を使って操作できる形にする(pandas.DataFrame)。文字コードはshift-jis

Match_data = (Data_frame[Data_frame['date'] == "2006-07-01"]).sort_values("r_asn")
'''
[df['date'] == "2006-07-01"] は、df['Data']が2006-07-01と同じ(True)か違う(False)かだけを判別
df[df['date'] == "2006-07-01"] で、↑の内容がTrueだった時だけ、データを返す.pandaデータフレーム
sort_values("r_asn") って機能を使って、↑で返されたデータをr_asn順に並べ替える(降順にしたいときは、第二引数にascending=Falseと記載)
→sort_values("r_asn", "ascending=False") って感じ
sort_valuesのデフォルト設定は以下から(sort_value以外の機能も見れる。pandasを使ってできること全部記載してある)
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html
'''

GraphX = Match_data["r_asn"]
GraphY = Match_data["f"]
#X軸がr_asn,Y軸がf(セッション数)

plt.plot(GraphX,GraphY)
plt.show()
#グラフ描画