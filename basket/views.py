from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'basket/index.html')

def information(request):
    return render(request, 'basket/information.html')

def news(request):
    return render(request, 'basket/newspage.html')

def sale(request):
    return render(request, 'basket/sale.html')

def QnA(request):
    return render(request, 'basket/Q&A.html')

def sitemap(request):
    return render(request, 'basket/sitemap.html')