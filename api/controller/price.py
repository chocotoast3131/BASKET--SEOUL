#물가정보/부류별함수
from api_module import class_func
from condition import price_code_name
import pandas as pd

code = input()
# Detailed_price.py에서 pd.DataFrame을 사용해서 관리하기 편하도록 price도 DateFrame 활용

df = pd.DataFrame(class_func(price_code_name(code)))

df1 = df.drop_duplicates(['item_name']) #메인 키워드(itemname) 하나만 남기고 중복값 제거(상품/중품 등)

def price_1(df1):
    return df1

print(price_1(df1)) #결과 확인용
#쌀/잡곡, 채소, 과일, 수산물 중 필요한 값 입력
#ex)쌀/잡곡