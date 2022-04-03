from django.shortcuts import render

# Create your views here.
from weavingUser.models import User
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
import json


# Create your views here.
@require_http_methods(["GET"])
def register(request):
    response = {}
    try:
        user = User(username=request.GET.get('username'),
                    password=request.GET.get('password'), phone=request.GET.get('phone'),
                    registerTime=request.GET.get('registerTime'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


@require_http_methods(["GET"])
def login(request):
    response = {}
    try:
        users = User.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", users))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response,json_dumps_params={'ensure_ascii':False})


def pagen(request, pg):
    html = "<h2>这是编号为{0}的网页!</h2>".format(pg)
    return HttpResponse(html)


def caculate(request, num1, signal, num2):
    html = "结果为:"
    if signal == "add":
        return HttpResponse(html + str(eval(num1) + eval(num2)))
    elif signal == "minus":
        return HttpResponse(html + str(eval(num1) - eval(num2)))
    elif signal == "multiply":
        return HttpResponse(html + str(eval(num1) * eval(num2)))
    elif signal == "divide":
        return HttpResponse(html + str(eval(num1) / eval(num2)))
    else:
        return HttpResponse("输入错误！")


def show_birthday(request, year, month, day):
    birthday = year + "年" + month + "月" + day + "日"
    return HttpResponse(birthday)


def test_url(request):
    url = reverse('login')
    return HttpResponseRedirect(url)
    pass
