#상세정보/품목별함수
from api_module import f_item__, item_func
from datetime import date, timedelta

itemcode = input() #품목코드
kindcode = input()
day = date.today() - timedelta(1)
last_week = day - timedelta(weeks=1)

df = item_func(f_item__(itemcode, kindcode, last_week, day)) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 터미널에 입력

def Detailed(df):
    return df

print(Detailed(df)) #결과 확인용

#품목코드, 품종코드 입력. 날짜는 일주일 간격으로 출력됨
#ex) 111, 01