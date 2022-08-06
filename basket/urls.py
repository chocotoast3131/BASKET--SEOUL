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
    # path('searched/', views.searched, name="searched"), # 검색결과
    re_path(r'^search/\?[a-z]{4}\=[/가-힣]{1,7}/$', views.searched, name="searched"),

    # 상세정보
    # 과일
    path('information/과일/사과/', views.fruit_apple, name='fruit-apple'),
    path('information/과일/배/', views.fruit_pear, name='fruit-pear'),
    path('information/과일/레몬/', views.fruit_peach, name='fruit-lemon'),
    path('information/과일/파인애플/', views.fruit_grapes, name='fruit-pineapple'),
    # 채소
    path('information/채소/오이/', views.vegetable_cucumber, name='vegetable-cucumber'),
    path('information/채소/당근/', views.vegetable_carrot, name='vegetable-carrot'),
    path('information/채소/양파/', views.vegetable_onion, name='vegetable-onion'),
    path('information/채소/파/', views.vegetable_greenonion, name='vegetable-greenonion'),
    path('information/채소/깐마늘(국산)/', views.vegetable_garlic, name='vegetable-garlic'),
    # 쌀/잡곡
    path('information/쌀_잡곡/쌀/', views.rice_white, name='rice-white'),
    path('information/쌀_잡곡/찹쌀/', views.rice_sticky, name='rice-sticky'),
    path('information/쌀_잡곡/콩/', views.rice_bean, name='rice-bean'),
    path('information/쌀_잡곡/고구마/', views.rice_sweetpotato, name='rice-sweetpotato'),
    path('information/쌀_잡곡/감자/', views.rice_potato, name='rice-potato'),
    # 수산물
    path('information/수산물/고등어/', views.fish_mackerel, name='fish-mackerel'),
    path('information/수산물/갈치/', views.fish_hairtail, name='fish-hairtail'),
    path('information/수산물/꽁치/', views.fish_croaker, name='fish-croaker'),
    path('information/수산물/물오징어/', views.fish_squid, name='fish-squid'),
    path('information/수산물/새우/', views.fish_shrimp, name='fish-shrimp'),
    
]
