from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('information/', views.information, name='information'),
    path('news/', views.news, name='news'),
    path('sale/', views.sale, name='sale'),
    path('QnA/', views.QnA, name='QnA'),
    path('sitemap/', views.sitemap, name='sitemap'),
]
