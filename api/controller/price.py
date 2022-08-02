#물가정보/부류별함수
from api_module import class_func
from condition import price_code_name
import pandas as pd

code = input()
df = pd.DataFrame(class_func(price_code_name(code)))

# index1 = df[df['today'] == '-'].index
# index2 = df[df['past_month'] == '-'].index
# df.loc[index1, 'today'] = '0'
# df.loc[index2, 'past_month'] = '0'

def price_1(df):
    return df

print(price_1(df)) #결과 확인용
#쌀/곡물, 채소, 과일, 수산물 중 필요한 값 입력
#ex)쌀/곡물