#상세정보/품목별함수
from api_module import graph_func, class_func1
from condition import Detailed_graph_code, Detailed_code_name
import pandas as pd
import json

def Detailed(name, kindname): #품종별로도 볼수있어야함
    df = pd.DataFrame(class_func1(Detailed_code_name(name, kindname)))
    index1 = df[df['item_name'] != kindname].index
    df_drop = df.drop(index1)

    df_json = df_drop.to_json(orient = 'records')
    df_dict = json.loads(df_json)
    return df_dict
# print(Detailed("과일", "사과")) #확인용 #kindname에 있는데 출력되지 않는 데이터는 없는 데이터. 존재하는 데이터만 나옴


def Detailed_graph(value_name): #마켓명 하나만 출력할 수 있음/그래프용 데이터
    
    df = pd.DataFrame(graph_func(Detailed_graph_code(value_name)))

    index1 = df[df['itemname'] != value_name].index #제외한 값 전부 삭제(null값 지우려고 넣음). ex)['itemname'] : ['쌀'] -> value_name에 쌀 저장
    df_drop = df.drop(index1)
    df_del_marketname = (df_drop['marketname'] == '경동') #values는 마켓명. 입력한 값만 출력됨 / 1차적으로 값을 거름
    del_marketname = df_drop[df_del_marketname]
    del del_marketname['marketname'] #그래프를 위한 데이터는 품종명, 날짜, 가격만 필요하므로 마켓명 열을 삭제함

    df_json = del_marketname.to_json(orient = 'records')
    df_dict = json.loads(df_json)
    return df_dict

print(Detailed_graph('쌀')) #수산물 키워드는 전부 에러발생
