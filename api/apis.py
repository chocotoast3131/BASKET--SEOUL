from django.http import JsonResponse

from api.controller.price import price_1

def get_price_code(request): # 부류 요청값 받아서 부류별 json데이터로 출력 
    name = request.GET.get("name")
    res_json = price_1(name)
    return JsonResponse(res_json, safe=False)

# def get_detail_code(request):
#     res_json = Detailed()
#     return JsonResponse(res_json)