from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from weavingSearch.models import Periodicals, Periodical, Periodical_details, Patent
from django.core import serializers
from django.views.decorators.http import require_http_methods
from weavingSearch.json_utils import *
from django.core.paginator import Paginator
from weavingSearch.lda_analysis import *
# from mongoengine.queryset.visitor import Q
from django.db.models import Q


def get_guiding(request):
    keywords = request.GET.get("keywords", "优化")
    print(train_lad(keywords))
    return JsonResponse({'status': 200})


@require_http_methods(["GET"])
def get_periodical(request):
    # response = {}
    # try:
    #     keywords = request.GET.get("keywords")
    #     page = request.GET.get("page", 1)
    #     if keywords is None or keywords == '':
    #         response["status"] = 200
    #         response["list"] = None
    #         return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    #     periodicals = Periodical.objects(title__icontains=keywords).exclude('_id')
    #     periodical_details = Periodical_details.objects(title__icontains=keywords). \
    #         exclude('_id').exclude('title').exclude('author_bh').exclude('article_id')
    #     periodicals_json = eval(json.dumps(json.loads(periodicals.to_json()), ensure_ascii=False))
    #     periodicals_details_json = eval(json.dumps(json.loads(periodical_details.to_json()), ensure_ascii=False))
    #     for i in range(len(periodicals_json)):
    #         periodicals_details_json[i]['title'] = periodicals_json[i]['title']
    #         periodicals_details_json[i]['authors'] = periodicals_json[i]['authors']
    #         periodicals_details_json[i]['article_url'] = periodicals_json[i]['article_url']
    #         periodicals_details_json[i]['category'] = periodicals_json[i]['category']
    #     page_obj = Paginator(periodicals_details_json, 8)
    #     response["status"] = 200
    #     response["list"] = list(page_obj.get_page(page))
    #     response["num_pages"] = page_obj.num_pages if len(response["list"]) > 0 else 0
    #     response["count"] = page_obj.count
    #     response["page_range"] = int(page) if int(page) < (int(page_obj.count) / 8 + 1) else -1
    #     return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, encoder=NbJSONEncoder)
    # except Exception as e:
    #     print(e)
    #     return JsonResponse({"status": 400}, json_dumps_params={'ensure_ascii': False})
    response = {}
    try:
        keywords = request.GET.get("keywords")
        page = request.GET.get("page", 1)
        if keywords is None or keywords == '':
            response["status"] = 200
            response["list"] = None
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        periodicals = Periodicals.objects.filter(Q(title__icontains=keywords) | Q(keywords__icontains=keywords))
        periodicals_json = json.loads(serializers.serialize("json", periodicals))
        periodicals_list = []
        for periodical_json in periodicals_json:
            periodicals_list.append(periodical_json["fields"])
        page_obj = Paginator(periodicals_list, 8)
        response["status"] = 200
        response["list"] = list(page_obj.get_page(page))
        response["num_pages"] = page_obj.num_pages if len(response["list"]) > 0 else 0
        response["count"] = page_obj.count
        response["page_range"] = int(page) if int(page) < (int(page_obj.count) / 8 + 1) else -1
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, encoder=NbJSONEncoder)
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400}, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def lda_analysis(request):
    response = {}
    try:
        category = request.GET.get("category")
        keywords = request.GET.get("keywords")
        if keywords is None or keywords == '':
            response["status"] = 200
            response["topic"] = None
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        response["status"] = 200
        if process_text(keywords, category)[1] <= 0:
            response["topic"] = None
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, encoder=NbJSONEncoder)
        topic_tags, num_topics, words_list = train_lad(keywords, category)
        topic_tag_list = []
        for i in range(0, num_topics):
            topic_count = 0
            for topic_tag in topic_tags:
                if topic_tag == i:
                    topic_count += 1
            topic_tag_list.append({"category": "主题" + str(i + 1), "count": topic_count, "words": words_list[i]})

        response["topic_statistics"] = topic_tag_list
        response["num_topics"] = num_topics
        keywords_dict = {}
        for words in words_list:
            word_list = words.split(" ")
            for word in word_list:
                keywords_dict[word] = keywords_dict.get(word, 0) + 1
        items = list(keywords_dict.items())
        items.sort(key=lambda x: x[1], reverse=True)
        wordCloud = []
        for i in items:
            wordCloud.append({"name": i[0], "value": i[1] * 50})
        response["words_cloud"] = wordCloud
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, encoder=NbJSONEncoder)
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400}, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def get_patent(request):
    response = {}
    try:
        keywords = request.GET.get("keywords")
        page = request.GET.get("page", 1)
        if keywords is None or keywords == '':
            response["status"] = 200
            response["list"] = None
            return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
        patents = Patent.objects.filter(Q(name__icontains=keywords))
        patents_json = json.loads(serializers.serialize("json", patents))
        patents_list = []
        for patent_json in patents_json:
            patents_list.append(patent_json["fields"])
        page_obj = Paginator(patents_list, 10)
        response["status"] = 200
        response["list"] = list(page_obj.get_page(page))
        response["num_pages"] = page_obj.num_pages if len(response["list"]) > 0 else 0
        response["count"] = page_obj.count
        response["page_range"] = int(page) if int(page) < (int(page_obj.count) / 10 + 1) else -1
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False}, encoder=NbJSONEncoder)
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400}, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def get_patent_statistics(request):
    patent = Patent.objects.all()
    patents_json = json.loads(serializers.serialize("json", patent))
    patents_list = []
    for patent_json in patents_json:
        patents_list.append(patent_json["fields"])
    return JsonResponse(patents_list, json_dumps_params={'ensure_ascii': False})
