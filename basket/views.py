from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView

from api.models import ItemName

# Create your views here.

# main, sub 페이지
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

# 검색 페이지
def search(request):
    return render(request, 'basket/search.html')

# 검색결과
def searched(request): 
    name = request.GET.get("name") # 쿼리스트링 받기
    results = ItemName.objects.filter(Q(category_name__icontains = name)|Q(item_name__icontains = name)|Q(kind_name__icontains = name)) # Q 조건문, name이 ~이거나 ~인것
    count = results.count()
    return render(request, 'basket/search.html', {"results":results, "count":count, "name":name})

# 상세정보
def detailed(request,category,itemname):
    return render(request, 'basket/detailed.html', {"category":category,"itemname":itemname})

