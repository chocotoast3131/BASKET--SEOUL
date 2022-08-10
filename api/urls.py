from django.urls import path,re_path

from . import apis

urlpatterns = [
   path('price/', apis.get_price_code), # 부류별 json 데이터로 출력
   re_path(r'^price/(?P<name>[가-힣][_가-힣]+)/(?P<kindname>[(가-힣)]+)/$',apis.get_detail_code), # 품목별 상세정보 json 데이터
   # re_path(r'^price/(?P<value_name>[(가-힣)]+)/$',apis.get_detail_graph), # 품목별 그래프 json 데이터 (수산물X)  
   # re_path(r'^price/(?P<value_name>[(가-힣)]+)/$',apis.get_fish_graph), # 수산물 그래프 json 데이터   

]
