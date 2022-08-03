#상세정보/품목별함수
from api_module import f_item__, item_func
from datetime import date, timedelta
import pandas as pd
import json

def Detailed(itemcode, kindcode):

    day = date.today() - timedelta(1)

    df = pd.DataFrame(item_func(f_item__(itemcode, kindcode, day, day))) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 입력

    value_name = input()
    index1 = df[df['itemname'] != value_name].index
    df_drop = df.drop(index1)

    df_json = df_drop.to_json(orient = 'records') 
    df_dict = json.loads(df_json)
    return df_dict
