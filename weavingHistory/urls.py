from django.urls import path, re_path, reverse
from weavingHistory import views

urlpatterns = [
    path('getEventDatas/', views.get_history, name='history')
]
