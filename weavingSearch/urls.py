"""weavingSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from weavingSearch import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    re_path(r'^$', TemplateView.as_view(template_name='index.html')),
    path('api/searching/get_periodical', views.get_periodical, name='periodical'),
    path('api/searching/get_patent', views.get_patent, name="patent"),
    path('api/searching/lda_analysis', views.lda_analysis, name='lda'),
    path('api/user/', include('weavingUser.urls')),
    path('api/graph/', include('weavingPicture.urls')),
    path('api/chart/', include('weavingCharts.urls')),
    path('api/history/', include('weavingHistory.urls')),
    path('api/get_patent_statistics/', views.get_patent_statistics, name="patent_statistics")
    # path('test/', include('weavingUser.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
