#상세정보/품목별함수
from api_module import item_func
from condition import *
import numpy as np

df = np.array(item_func(Detailed_code_name([input()], [], []))) #식량작물, 채소류, 과일류, 수산물 중 필요한 값을 터미널에 입력
print(len(df)) #dataframe이 몇행인지 계산하고 그 범위 내에서 num 입력

def Detailed(df):
    num = int(input())
    return df[num]

print(Detailed(df)) #결과 확인용