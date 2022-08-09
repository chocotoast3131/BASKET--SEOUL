from django.http import JsonResponse

from api.controller.Detailed_price import Detailed, Detailed_graph, marine_products_graph
from api.controller.price import price_1

def get_price_code(request): # 부류 요청값 받아서 부류별 json데이터 
    name = request.GET.get("name") # ?name=과일
    res_json = price_1(name)
    return JsonResponse(res_json, safe=False)

def get_detail_code(request, name, kindname): # 상세정보 json 데이터
    res_json = Detailed(name, kindname)
    return JsonResponse(res_json,safe=False)

def get_detail_graph(request, value_name): # 상세정보 그래프 json 데이터
    res_json = Detailed_graph(value_name)
    return JsonResponse(res_json, safe=False)

def get_fish_graph(request, value_name): # 수산물 그래프 json 데이터
    res_json = marine_products_graph(value_name)
    return JsonResponse(res_json, safe=False)