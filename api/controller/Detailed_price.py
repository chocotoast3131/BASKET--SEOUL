#상세정보/품목별함수
from api_module import f_item__, item_func
from datetime import date, timedelta
import pandas as pd

itemcode = input() #품목코드
kindcode = input()
day = date.today() - timedelta(1)
last_week = day - timedelta(weeks=1)

df = pd.DataFrame(item_func(f_item__(itemcode, kindcode, last_week, day))) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 터미널에 입력

value_name = input()
index1 = df[df['itemname'] != value_name].index
df = df.drop(index1) #빈 값의 인덱스를 찾으려 했으나 None, '', "", [], '[]' 등 무엇을 사용해도 빈값을 찾을 수 없어서 품목명을 입력하는 방법을 사용
#{'itemname': [], 'kindname': [], 'marketname': [], 'today': '07/25', 'price': '48,943'} <- 이와 같은 빈 항목들 제거
#drop을 사용하기 위해 pandas 사용 / df를 데이터프레임으로 만들었음

def Detailed(df):
    return df

print(Detailed(df)) #결과 확인용

#품목코드, 품종코드 입력. 날짜는 일주일 간격으로 출력됨
#ex) 111, 01