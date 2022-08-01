from api_module import f_class__

def price_code_name(code):
    global today 
    today = '20220729' #필요한 날로 수정가능
    match(code):
        case "쌀/곡물":
            code_print = f_class__('100', today)
        case "채소":
            code_print = f_class__('200', today)
        case "과일":
            code_print = f_class__('400', today)
        case "수산물":
            code_print = f_class__('600', today)
    return code_print