from django.http import JsonResponse
from .controller.condition import price_code_name


def get_price_code(request):
    code = request.GET.get("code")
    res_json = price_code_name(code)
    return JsonResponse(res_json)
