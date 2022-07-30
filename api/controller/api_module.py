import requests
import json
import numpy as np

def open_api(**kwargs): #함수 정의할 때 사용.
    url = 'http://www.kamis.or.kr/service/price/xml.do'
    params = { \
        'p_cert_key' : '31a006ec-20bb-4816-b495-f21ad9140c28', \
        'p_cert_id' : '222', \
        'p_convert_kg_yn' : 'N', \
        'p_returntype' : 'json', \
        **kwargs \
    }
    res = requests.get(url, params=params)
    print(res.status_code) ################################ status 코드는 api 문서에 기술한 에러 코드 이외에 통신과 관련한 응답을 나타내는 코드입니다.
    if res.status_code == 500: ############################ 500: open api 시스템 내부 오류 발생, 그 결과 응답 json이 없습니다.
        return {"data": ["500"]} ########################## 에러 처리용 객체 반환
    contents = res.text
    res_json = json.loads(contents)
    return res_json

def class_func(res_json): # 함수 이름 바꾸기(부류별, 품목별로 써야해서 이름이 달라야 알아보기 쉬움)
    res_class_f = list() #새로운 dict 생성 dict() 대신 list로 캐스팅
    if type(res_json['data']) is list:
        if res_json['data'][0] == "001": #에러처리. 001은 no data라는 에러코드 / type이 list이면 [0]에 접근이 가능, 001이면 데이터가 없다. ############## 500 오류에 대해서도 에러 처리 해보세요.
            print('no data')
            return res_class_f #빈 배열(line 30)
        
    for class_ in res_json['data']['item']: #사용할 key만 가져옴
        res_class_ = { \
            "item_name": class_["item_name"], \
            "kind_name": class_["kind_name"], \
            "unit": class_["unit"], \
            "today": class_["dpr1"], \
            # "diff_month": (class_["dpr1"] - class_["dpr5"]), \
            "past_month": class_["dpr5"] \
        } # 형 변환 diff_month
        res_class_f.append(res_class_)
    return res_class_f

def item_func(res_json): # 품목별
    res_item_f = list()
    if type(res_json['data']) is list:
        if res_json['data'][0] == "001":
            print('no data')
            return res_item_f
        
    for item_ in res_json['data']['item']: #사용할 key만 가져옴
        res_item_ = { \
            "itemname": item_["itemname"], \
            "kindname": item_["kindname"], \
            "marketname": item_["marketname"], \
            "today": item_["regday"], \
            "price": item_["price"]
        }
        res_item_f.append(res_item_)
    return res_item_f

def f_class__(p_item_category_code, p_regday, p_product_cls_code='01', p_country_code='1101'): #고정값은 = 사용해서 코드 입력 (값이 명시된것을 기본값이 있다고 함)
    return open_api(p_regday=p_regday, p_item_category_code=p_item_category_code, \
        p_product_cls_code=p_product_cls_code, p_country_code=p_country_code, \
        action='dailyPriceByCategoryList')
    
def f_item__(p_itemcode, p_kindcode, p_startday, p_endday, p_productclscode='01', p_countrycode='1101', p_productrankcode='04'): ########################### 파라미터 위치가 함수 호출과 일치해야 합니다. p_itemcode, p_startday, p_endday, p_kindcode -> p_itemcode, p_kindcode, p_startday, p_endday
    return open_api(p_itemcode=p_itemcode, p_startday=p_startday, p_endday=p_endday, p_kindcode=p_kindcode, \
        p_productclscode=p_productclscode, p_countrycode=p_countrycode, p_productrankcode=p_productrankcode, \
        action='periodProductList')
    
# print(np.array(class_func(f_class__('100', '20220701')))) #p_item_category_code, p_regday
# print(np.array(item_func(f_item__('111', '01', '2022-07-01', '2022-07-04')))) ######################################################## 오류가 난 이유 "농축수산물 품목 및 등급 코드표.xlsx"를 참고해서 문서에 존재하는 품종/품목 코드를 사용해야 합니다. 분류/품목/품종 코드는 엄연히 다릅니다.
