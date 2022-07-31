#상세정보/품목별함수
from api_module import f_item__, item_func
import numpy as np

itemcode = input() #품목코드
kindcode = input()
last_week = input() #today와 last_week 를 연산을 통해 일주일 단위로 계산하려 했지만 date.today()를 사용하면 오늘 값이 포함되지 않아서 입력하는걸로 바꿈 
day = input()

df = np.array(item_func(f_item__(itemcode, kindcode, last_week, day))) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 터미널에 입력

def Detailed(df):
    return df

print(Detailed(df)) #결과 확인용

#품목코드, 품종코드, 일주일전 날짜, 날짜(오늘날짜x, 데이터가 없으니 주말이나 오늘 날짜는 제외) 입력
#ex) 111, 01, 20220722, 20220729