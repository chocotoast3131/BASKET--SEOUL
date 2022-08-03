from Detailed_price import *
import pandas as pd
import matplotlib.pyplot as plt
# import pyupbit

# df_1 = pd.read_json(Detailed(df_drop))


df_1 = Detailed(df_drop) #가져올 데이터
plt.title('물가변동률') #타이틀 설정
plt.xlabel('날짜') #x축 라벨 설정
plt.ylabel('가격') #y축 라벨 설정
plt.bar(df_1['today'], df_1['price']) #바 그래프
plt.show()