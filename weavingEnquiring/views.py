from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect


# Create your views here.


def get_articles(request):
    return HttpResponse("<h1>这里返回指定数量的文献，ajax请求加载更多</h1>")
    pass


def get_search(request, **kwargs):
    return HttpResponse("<h1>返回文献、专利搜索结果</h1>")
    pass
