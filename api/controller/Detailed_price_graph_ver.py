#detailed_price 변형

# #상세정보/품목별함수
# from api_module import f_item__, item_func
# from datetime import date, timedelta
# import pandas as pd

# itemcode = input() #품목코드
# kindcode = input()
# day = date.today() - timedelta(1)
# week = day - timedelta(weeks=4)

# df = pd.DataFrame(item_func(f_item__(itemcode, kindcode, week, day))) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 입력

# value_name = input()
# index1 = df[df['itemname'] != value_name].index
# df_drop = df.drop(index1) #빈 값의 인덱스를 찾으려 했으나 None, '', "", [], '[]' 등 무엇을 사용해도 빈값을 찾을 수 없어서 품목명을 입력하는 방법을 사용
# #{'itemname': [], 'kindname': [], 'marketname': [], 'today': '07/25', 'price': '48,943'} <- 이와 같은 빈 항목들 제거
# #drop을 사용하기 위해 pandas 사용 / df를 데이터프레임으로 만들었음

# index_marketname = df_drop[df_drop['marketname'] != None].index
# market_drop = df_drop[df_drop['marketname'].str.contains(index_marketname)]

# # if market_drop != None:
# #     name = '경동'
# # elif market_drop == None:
# #     name = 'A-유통'

# # df_market_drop = df_drop[~market_drop]

# print(market_drop) #마켓이름 하나만 출력하기

# # def Detailed(df_drop):
# #     return df_drop

# # print(Detailed(df_drop))
# # df_json = df_drop.to_json(orient = 'records') 

# # def Detailed(df_json):
# #     return df_json

# # print(pd.read_json(Detailed(df_json))) #결과 확인용/json파일을 데이터프레임으로 출력함

# #품목코드, 품종코드 입력
# #ex) 111, 01, 쌀
