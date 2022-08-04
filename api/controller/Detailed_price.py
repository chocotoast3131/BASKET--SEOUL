#상세정보/품목별함수
from .api_module import f_item__, item_func
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import pandas as pd
import json
import plotly.express as px

def Detailed(itemcode, kindcode, value_name): #상세정보

    day = date.today() - timedelta(1)

    df = pd.DataFrame(item_func(f_item__(itemcode, kindcode, day, day))) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 입력

    index1 = df[df['itemname'] != value_name].index
    df_drop = df.drop(index1)

    df_json = df_drop.to_json(orient = 'records') 
    df_dict = json.loads(df_json)
    return df_dict
print(Detailed('111', '01', '쌀'))

def Detailed_graph(itemcode, kindcode, value_name, values): #마켓명 하나만 출력할 수 있음/그래프용 데이터

    day = date.today() - timedelta(1)
    months = day - relativedelta(months=1) #한달치 데이터

    df = pd.DataFrame(item_func(f_item__(itemcode, kindcode, months, day)))

    index1 = df[df['itemname'] != value_name].index #이걸 제외한 값 전부 삭제(null값 지우려고 넣음). ex)쌀
    df_drop = df.drop(index1)

    df_del_marketname = (df_drop['marketname'] == values) #values는 마켓명. 입력한 값만 출력됨

    del_marketname = df_drop[df_del_marketname]

    df_json = del_marketname.to_json(orient = 'records')
    df_dict = json.loads(df_json)
    return df_dict

# print(Detailed_graph('111', '01', '쌀', '경동')) #그래프 데이터 입력방식
# print(Detailed_graph('223', '01', '오이', 'A-유통'))