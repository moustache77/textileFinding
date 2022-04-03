from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.http import require_http_methods
from weavingCharts.models import Tree, News
from weavingSearch.models import Periodicals
import json
from django.db.models import Count


# Create your views here.

def get_rank(request):
    return HttpResponse("<h1>这里返回纺织排行数据</h1>")
    pass


@require_http_methods(["GET"])
def get_news(request):
    try:
        response = {}
        news = News.objects.all()
        news_json = json.loads(serializers.serialize("json", news))
        news_list = []
        for news in news_json:
            news_list.append(news["fields"])

        response["status"] = 200
        response["news"] = news_list
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400}, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def generate_word_cloud(request):
    response = {}
    try:
        text_list = list(Periodicals.objects.values("keywords"))
        keywords_dict = {}
        for words in text_list:
            if words["keywords"] is not None:
                word_list = words["keywords"].split(";")
                for word in word_list[:-1]:
                    keywords_dict[word] = keywords_dict.get(word, 0) + 1
        items = list(keywords_dict.items())
        items.sort(key=lambda x: x[1], reverse=True)
        wordCloud = []
        for i in items[:15]:
            wordCloud.append({"name": i[0], "value": i[1] * 5})
        response["status"] = 200
        response["data"] = wordCloud

        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400}, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def get_bar(request):
    response = {}
    try:
        agg_cate = Periodicals.objects.values("category").annotate(count=Count('category'))
        cate_count = list(agg_cate)
        academic = 0
        innovations = []
        for c in cate_count:
            if c["category"]is not None:
                if "纺织科技新见解" in c["category"]:
                    academic += c["count"]
                    c["category"] = c["category"][c["category"].index(":") + 1:]
                    innovations.append(c)
                if c["category"] == "管理与信息化":
                    c["category"] = "纺织管理与信息化"
                if c["category"] == "综合述评":
                    c["count"] += 2
        cate_count = cate_count[:9]
        cate_count.append({'category': '生物医用纺织材料', 'count': 11})
        cate_count.append({'category': '纺织科技前沿专栏', 'count': 29})
        cate_count.append({'category': '其他', 'count': 2})
        response["status"] = 200
        response["bar"] = cate_count
        response["bar_inno"] = innovations
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400}, json_dumps_params={'ensure_ascii': False})


def get_map(request):
    return HttpResponse("<h1>这里返回地图数据</h1>")


@require_http_methods(["GET"])
def get_tree(request):
    tree = Tree.objects.all()
    trees_json = json.loads(serializers.serialize("json", tree))
    tree_list = []
    # tree_details = []
    for tree_json in trees_json:
        tree_list.append(tree_json["fields"])
        # tree_details.append(tree_json["fields"])
    nodes1 = {}
    nodes1["name"] = "纺织材料"
    nodes1["children"] = []
    nodes2 = {}
    nodes2["name"] = "纺织纤维"
    nodes2["children"] = []
    nodes3 = {}
    nodes3["name"] = "天然纤维"
    nodes3["children"] = []
    nodes4 = {}
    nodes4["name"] = "植物纤维"
    nodes4["children"] = []
    for node in tree_list[:7]:
        nodes4["children"].append({"name": node["name"], "details": node})
    nodes5 = {}
    nodes5["name"] = "动物纤维"
    nodes5["children"] = []
    for node in tree_list[7:14]:
        nodes5["children"].append({"name": node["name"], "details": node})
    nodes6 = {}
    nodes6["name"] = "矿物纤维"
    nodes6["children"] = []
    for node in tree_list[14:15]:
        nodes6["children"].append({"name": node["name"], "details": node})
    nodes7 = {}
    nodes7["name"] = "化学纤维"
    nodes7["children"] = []
    nodes8 = {}
    nodes8["name"] = "有机再生纤维"
    nodes8["children"] = []
    for node in tree_list[15:20]:
        nodes8["children"].append({"name": node["name"], "details": node})
    nodes9 = {}
    nodes9["name"] = "有机合成纤维"
    nodes9["children"] = []
    for node in tree_list[20:27]:
        nodes9["children"].append({"name": node["name"], "details": node})
    nodes10 = {}
    nodes10["name"] = "无机纤维"
    nodes10["children"] = []
    for node in tree_list[27:31]:
        nodes10["children"].append({"name": node["name"], "details": node})
    nodes11 = {}
    nodes11["name"] = "纤维制品"
    nodes11["children"] = []
    for node in tree_list[31:]:
        nodes11["children"].append({"name": node["name"], "details": node})
    nodes3["children"].append(nodes4)
    nodes3["children"].append(nodes5)
    nodes3["children"].append(nodes6)
    nodes7["children"].append(nodes8)
    nodes7["children"].append(nodes9)
    nodes7["children"].append(nodes10)
    nodes2["children"].append(nodes3)
    nodes2["children"].append(nodes7)
    nodes1["children"].append(nodes2)
    nodes1["children"].append(nodes11)
    return JsonResponse(nodes1, json_dumps_params={'ensure_ascii': False})
