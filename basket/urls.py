from . import views
from django.urls import path,re_path

urlpatterns = [
    
    # main,sub 페이지
    path('', views.index, name='index'),
    path('information/', views.information, name='information'),
    path('news/', views.news, name='news'),
    path('QnA/', views.QnA, name='QnA'),
    path('sitemap/', views.sitemap, name='sitemap'),

    # 편의점 할인정보
    path('sale/GS25/', views.GS25, name='sale'), # sale.html == GS25
    path('sale/7-Eleven/', views.SevenEleven, name='7-Eleven'),
    path('sale/CU/', views.CU, name="CU"),

    # 검색
    path('search/', views.search, name='search'), # 검색페이지
    re_path(r'^search/\?[a-z]{4}\=[/가-힣]{1,7}/$', views.searched, name="searched"),

    # 상세정보
    re_path(r'^information/(?P<category>(과일|채소|쌀_잡곡|수산물))/(?P<itemname>[가-힣]+)/$', views.detailed, name="detailed"), 
]
