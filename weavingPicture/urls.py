from django.urls import path, re_path, reverse
from weavingPicture import views

urlpatterns = [
    path('get_all_datas/', views.get_all_graph, name="knowledgeGraph"),
    path('get_project_datas/', views.get_project_graph, name="projectGraph"),
    path('get_search_datas/', views.getSearch_graph, name="searchGraph"),
    path('get_author/', views.get_author, name="author"),

]
