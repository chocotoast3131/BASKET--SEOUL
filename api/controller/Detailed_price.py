#상세정보/품목별함수
from .api_module import graph_func, class_func1
from .condition import Detailed_graph_code, Detailed_code_name
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
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
    index2 = del_marketname[del_marketname['price'] == '-'].index
    del_marketname2 = del_marketname.drop(index2)
    del_marketname2['price'] = del_marketname2['price'].apply(lambda x: x.replace(',', ''))
    del_marketname2['price'] = pd.to_numeric(del_marketname2['price'])
    
    months =  del_marketname2['today']
    price = del_marketname2['price']

    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize=(14.5, 5))
    plt.plot(months, price, color='#ff7f0e')
    plt.xlabel('날짜', loc='right')
    plt.ylabel('가격', loc='top', rotation=360)
    plt.savefig('basket/static/logo,img/graph.png', transparent=True)
    
    graph_img = Image.open('basket/static/logo,img/graph.png')

    return graph_img

# print(Detailed_graph('사과'))

def marine_products_graph(value_name): #수산물 그래프용 함수
    
    m_df = pd.DataFrame(graph_func(Detailed_graph_code(value_name)))    

    m_index1 = m_df[m_df['itemname'] != value_name].index
    m_df_drop = m_df.drop(m_index1)
    m_df_del_marketname = (m_df_drop['marketname'] == 'A-유통') #values는 마켓명. 입력한 값만 출력됨 / 1차적으로 값을 거름
    m_del_marketname = m_df_drop[m_df_del_marketname]
    del m_del_marketname['marketname'] #그래프를 위한 데이터는 품종명, 날짜, 가격만 필요하므로 마켓명 열을 삭제함
    m_index2 = m_del_marketname[m_del_marketname['price'] == '-'].index
    m_del_marketname2 = m_del_marketname.drop(m_index2)
    m_del_marketname2['price'] = m_del_marketname2['price'].apply(lambda x: x.replace(',', ''))
    m_del_marketname2['price'] = pd.to_numeric(m_del_marketname2['price'])

    months =  m_del_marketname2['today']
    price = m_del_marketname2['price']

    plt.rc('font', family='Malgun Gothic')
    plt.figure(figsize=(14.5, 5))
    plt.plot(months, price, color='#ff7f0e')
    plt.xlabel('날짜', loc='right')
    plt.ylabel('가격', loc='top', rotation=360)
    plt.savefig('basket/static/logo,img/m_graph.png')
    
    m_graph_img = Image.open('basket/static/logo,img/m_graph.png')

    return m_graph_img

# print(marine_products_graph('새우'))