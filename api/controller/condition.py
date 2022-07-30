from datetime import date, timedelta
from api_module import f_class__

# get_get -> 바꾼 이름
def price_code_name(code, today): # 함수 이름 바꾸기, 부류별 쓰기, 인자 추가 (최소 2개)
    # 오늘 날짜 기본 값으로 넣어주기
    # 현재 시간 date 객체 만들기
    # date 객체의 날짜를 형식대로 출력하기 formatting date(2022, 7, 29) -> "2022-07-29"
    today = date.today()
    match(code):
        case ["식량작물"]:
            code = f_class__('100', today)
            # name = 부류별('100', )
        case ["채소류"]:
            code = f_class__('200', today)
        case ["과일류"]:
            code = f_class__('400', today)
        case ["수산물"]:
            code = f_class__('600', today)
    return code

def Detailed_code_name(code1, today, last_week): 
    today = date.today()
    one_week = timedelta(weeks=1)
    last_week = today - one_week
    match(code1):
        case ["식량작물"]:
            code1 = f_class__('100', last_week, today)
            # name = 부류별('100', )
        case ["채소류"]:
            code1 = f_class__('200', last_week, today)
        case ["과일류"]:
            code1 = f_class__('400', last_week, today)
        case ["수산물"]:
            code1 = f_class__('600', last_week, today)
    return code1