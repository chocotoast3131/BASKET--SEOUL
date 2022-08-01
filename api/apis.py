from django.http import JsonResponse
from .controller.condition import price_code_name
from .controller.Detailed_price import Detailed


def get_price_code(request): # 부류 요청값 받아서 부류별 json데이터로 출력 
    code = request.GET.get("code")
    res_json = price_code_name(code)
    return JsonResponse(res_json)

def get_detail(request):
    res_json = Detailed()
    return JsonResponse(res_json)