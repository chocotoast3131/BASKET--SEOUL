#물가정보/부류별함수
from api_module import class_func
from condition import *
import numpy as np

df = np.array(class_func(price_code_name([input()], [])))

# df = np.array(class_func(code_name([input()]))) 
#식량작물, 채소류, 과일류, 수산물 중 필요한 값을 터미널에 입력/주말을 제외한 날짜 입력

def price_1(df):
    return df

print(price_1(df)) #결과 확인용