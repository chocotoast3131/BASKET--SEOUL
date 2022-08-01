from . import views
from django.urls import path
from . import apis

urlpatterns = [
   path('get/', apis.get_price_code), # 부류별 json 데이터로 출력
   path('getdetail/', apis.get_detail),
]
