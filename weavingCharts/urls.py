from django.urls import path, re_path, reverse
from weavingCharts import views

urlpatterns = [
    path('getBarData/', views.get_bar),
    path('generateWordCloud/', views.generate_word_cloud),
    path('getIndustryNews/', views.get_news),
    path('getTreeChart/', views.get_tree)
]
