from django.urls import path, re_path, reverse
from weavingUser import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login,name='login'),
    path('page/<int:pg>', views.pagen),
    # path('<int:num1>/<str:signal>/<int:num2>', views.caculate),
    re_path(r'^(?P<num1>\d{1,2})/(?P<signal>\w+)/(?P<num2>\d{1,2})$', views.caculate),
    re_path(r'^birthday/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})$', views.show_birthday),
    path('test_url/', views.test_url),
]
