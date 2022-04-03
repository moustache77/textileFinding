from django.urls import path, reverse, re_path
from weavingEnquiring import views

urlpatterns = [
    path('getArticleDatas/', views.get_articles),
    path('searchParticularDatas/', views.get_search),
]
