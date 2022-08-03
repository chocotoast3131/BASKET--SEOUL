#상세정보/품목별함수
from api_module import f_item__, item_func
from datetime import date, timedelta
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

def Detailed_graph(itemcode, kindcode, value_name):

    day = date.today() - timedelta(1)

    df = pd.DataFrame(item_func(f_item__(itemcode, kindcode, day, day))) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 입력

    index1 = df[df['itemname'] != value_name].index #이걸 제외한 값 전부 삭제(null값 지우려고 넣음). ex)쌀
    df_drop = df.drop(index1)

    df_del_marketname = df_drop['marketname'] == '경동'
    # if df_drop['marketname'] == 

    del_marketname = df_drop[df_del_marketname]

    df_json = del_marketname.to_json(orient = 'records')
    df_dict = json.loads(df_json)
    return df_dict

# print(Detailed_graph('111', '01', '쌀'))