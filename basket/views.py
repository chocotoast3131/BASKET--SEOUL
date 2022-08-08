from unicodedata import category
from django.shortcuts import render
from django.db.models import Q

from api.models import ItemName

# Create your views here.

# itemname_map={
#     "category":{
#         "fruit":"과일",
#         "rice":"쌀_잡곡",
#         "vegetable":"채소",
#         "fish":"수산물",
#     },
#     "itemname":{
#         "apple":"사과",
#         "pear":"배",
#         "lemon":"레몬",
#         "fineapple":"파인애플",
#         "cucumber":"오이",
#         "carrot":"당근",
#         "onion":"양파",
#         "greenonion":"파",
#         "garlic":"깐마늘(국산)",
#         "white":"쌀",
#         "sticky":"찹쌀",
#         "bean":"콩",
#         "sweetpotato":"고구마",
#         "potato":"감자",
#         "mackerel":"고등어",
#         "hairtail":"갈치",
#         "croaker":"꽁치",
#         "squid":"물오징어",
#         "shrimp":"새우",


#     }
# }


def index(request):
    return render(request,'basket/index.html')

def information(request):
    return render(request, 'basket/information.html')

def news(request):
    return render(request, 'basket/newspage.html')


def QnA(request):
    return render(request, 'basket/Q&A.html')

def sitemap(request):
    return render(request, 'basket/sitemap.html')

# 편의점 할인정보 
def GS25(request): 
    return render(request, 'basket/sale.html')

def SevenEleven(request):
    return render(request, 'basket/7-Eleven.html')

def CU(request):
    return render(request, 'basket/CU.html')


# 검색
def search(request):
    return render(request, 'basket/search.html')


def searched(request): # 검색결과
    name = request.GET.get("name") # 쿼리스트링 받기
    results = ItemName.objects.filter(Q(category_name__icontains = name)|Q(item_name__icontains = name)|Q(kind_name__icontains = name)) # Q 조건문, name이 ~이거나 ~인것
    return render(request, 'basket/search.html', {"results":results})

# 상세정보
def detailed(request,category,itemname):
    return render(request, 'basket/detailed.html', {"category":category,"itemname":itemname})
