#물가정보/부류별함수
from api_module import class_func
from condition import price_code_name

df = class_func(price_code_name(input()))

def price_1(df):
    return df

print(price_1(df)) #결과 확인용

#쌀/곡물, 채소, 과일, 수산물 중 필요한 값 입력
#ex)쌀/곡물