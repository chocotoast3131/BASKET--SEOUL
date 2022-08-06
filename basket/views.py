from django.shortcuts import render
from django.db.models import Q

from api.models import ItemName

# Create your views here.

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
    return render(request, 'basket/searched.html', {"results":results})

# 상세정보
# 과일
def fruit_apple(request): # 사과
    return render(request, 'basket/fruit-apple.html')

def fruit_pear(request): # 배
    return render(request, 'basket/fruit-pear.html')

def fruit_peach(request): # 레몬
    return render(request, 'basket/fruit-lemon.html')

def fruit_grapes(request): # 파인애플
    return render(request, 'basket/fruit-pineapple.html')

# 채소

def vegetable_cucumber(request): # 오이
    return render(request, 'basket/vegetable-cucumber.html')

def vegetable_carrot(request): # 당근
    return render(request, 'basket/vegetable-carrot.html')

def vegetable_onion(request): # 양파
    return render(request, 'basket/vegetable-onion.html')

def vegetable_greenonion(request): # 파
    return render(request, 'basket/vegetable-greenonion.html')

def vegetable_garlic(request): # 마늘
    return render(request, 'basket/vegetable-garlic.html')

# 쌀/잡곡
def rice_white(request): # 쌀
    return render(request, 'basket/rice-white.html')

def rice_sticky(request): # 찹쌀
    return render(request, 'basket/rice-sticky.html')

def rice_bean(request): # 콩
    return render(request, 'basket/rice-bean.html')

def rice_sweetpotato(request): # 고구마
    return render(request, 'basket/rice-sweetpotato.html')

def rice_potato(request): # 감자
    return render(request, 'basket/rice-potato.html')

# 수산물
def fish_mackerel(request): # 고등어
    return render(request, 'basket/fish-mackerel.html')

def fish_hairtail(request): # 갈치
    return render(request, 'basket/fish-hairtail.html')

def fish_croaker(request): # 꽁치
    return render(request, 'basket/fish-croaker.html')

def fish_squid(request): # 물오징어
    return render(request, 'basket/fish-squid.html')

def fish_shrimp(request): # 새우
    return render(request, 'basket/fish-shrimp.html')
