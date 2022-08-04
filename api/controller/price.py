#물가정보/부류별함수
from .api_module import class_func
from .condition import price_code_name
import pandas as pd
import json

def price_1(name):
    df = pd.DataFrame(class_func(price_code_name(name)))

    df_drop = df.drop_duplicates(['item_name']) #메인 키워드(itemname) 하나만 남기고 중복값 제거(상품/중품 등)

    df_json = df_drop.to_json(orient = 'records')
    df_dict = json.loads(df_json)
    return df_dict
