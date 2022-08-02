from api_module import f_class__
from datetime import date, timedelta

def price_code_name(code):
    global day
    day = date.today() - timedelta(1) #당일 데이터는 없기 때문에 전날을 기준으로 함.
    
    if day.weekday() == 5: #오늘이 토(5), 일(6)이라면 day를 금(4)요일로 만든다
        day -= timedelta(1)
    elif day.weekday() == 6:
        day -= timedelta(2)

    match(code):
        case "쌀/잡곡":
            code_print = f_class__('100', day)
        case "채소":
            code_print = f_class__('200', day)
        case "과일":
            code_print = f_class__('400', day)
        case "수산물":
            code_print = f_class__('600', day)
    return code_print