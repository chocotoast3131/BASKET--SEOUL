from .api_module import f_class__, f_item__
from datetime import date, timedelta

def price_code_name(name):
    
    day = date.today() - timedelta(1) #당일 데이터는 없기 때문에 전날을 기준으로 함
    
    if day.weekday() == 5: #오늘이 토(5), 일(6)이라면 day를 금(4)요일로 만든다
        day -= timedelta(1)
    elif day.weekday() == 6:
        day -= timedelta(2)
    
    match(name):
        case "쌀/잡곡":
            code_print = f_class__('100', day)
        case "채소":
            code_print = f_class__('200', day)
        case "과일":
            code_print = f_class__('400', day)
        case "수산물":
            code_print = f_class__('600', day)
    return code_print

def Detailed_code_name(name, kindname): #Detailed_price
    
    day = date.today() - timedelta(1) #당일 데이터는 없기 때문에 전날을 기준으로 함
    
    if day.weekday() == 5: #오늘이 토(5), 일(6)이라면 day를 금(4)요일로 만든다
        day -= timedelta(1)
    elif day.weekday() == 6:
        day -= timedelta(2)
    
    match(name, kindname):
        case "쌀_잡곡", "쌀":
            Detailed_print = f_class__('100', day)
        case "쌀_잡곡", "찹쌀":
            Detailed_print = f_class__('100', day)
        case "쌀_잡곡", "콩":
            Detailed_print = f_class__('100', day)
        case "쌀_잡곡", "고구마":
            Detailed_print = f_class__('100', day)
        case "쌀_잡곡", "감자":
            Detailed_print = f_class__('100', day)

        case "채소", "오이":
            Detailed_print = f_class__('200', day)
        case "채소", "당근":
            Detailed_print = f_class__('200', day)
        case "채소", "양파":
            Detailed_print = f_class__('200', day)
        case "채소", "파":
            Detailed_print = f_class__('200', day)
        case "채소", "깐마늘(국산)":
            Detailed_print = f_class__('200', day)

        case "과일", "사과":
            Detailed_print = f_class__('400', day)
        case "과일", "배":
            Detailed_print = f_class__('400', day)
        case "과일", "레몬":
            Detailed_print = f_class__('400', day)
        case "과일", "파인애플":
            Detailed_print = f_class__('400', day)

        case "수산물", "고등어":
            Detailed_print = f_class__('600', day)
        case "수산물", "갈치":
            Detailed_print = f_class__('600', day)
        case "수산물", "꽁치":
            Detailed_print = f_class__('600', day)
        case "수산물", "물오징어":
            Detailed_print = f_class__('600', day)
        case "수산물", "새우":
            Detailed_print = f_class__('600', day)

    return Detailed_print #쌀_잡곡, 채소, 과일, 수산물

def Detailed_graph_code(value_name):
    
    day = date.today() - timedelta(1)
    months = "2022-01-01"

    match(value_name):
        case '쌀':
            graph_print = f_item__('111', '01', months, day, '04')
        case '찹쌀':
            graph_print = f_item__('112', '01', months, day, '04')
        case '콩':
            graph_print = f_item__('141', '01', months, day, '04')
        case '고구마':
            graph_print = f_item__('151', '00', months, day, '04')
        case '감자':
            graph_print = f_item__('152', '01', months, day, '04')

        case '오이':
            graph_print = f_item__('223', '02', months, day, '04')
        case '당근':
            graph_print = f_item__('232', '01', months, day, '04')
        case '양파':
            graph_print = f_item__('245', '00', months, day, '04')
        case '파':
            graph_print = f_item__('246', '00', months, day, '04')
        case '깐마늘(국산)':
            graph_print = f_item__('258', '01', months, day, '04')

        case '사과':
            graph_print = f_item__('411', '05', months, day, '04')
        case '배':
            graph_print = f_item__('412', '01', months, day, '04')
        case '레몬':
            graph_print = f_item__('424', '00', months, day, '04')
        case '파인애플':
            graph_print = f_item__('420', '02', months, day, '04')

        case '고등어':
            graph_print = f_item__('611', '03', months, day, '05')
        case '갈치':
            graph_print = f_item__('613', '02', months, day, '05')
        case '꽁치':
            graph_print = f_item__('612', '01', months, day, '05')
        case '물오징어':
            graph_print = f_item__('619', '01', months, day, '05')
        case '새우':
            graph_print = f_item__('654', '01', months, day, '05')

    return graph_print