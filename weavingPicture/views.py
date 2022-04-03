from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
import json
from django.core import serializers
from neomodel import db
from django.views.decorators.http import require_http_methods

# Create your views here.
from weavingPicture.models import Book, Author


def test_static(request):
    return HttpResponse("<img src='/static/imgs/qunyuan.jpg' width='200px' height='200px'/>")


def get_books(request):
    return HttpResponse(Book.nodes.all())


@require_http_methods(["GET"])
def get_author(request):
    response = {}
    authors = Author.objects.all()
    response["status"] = 200
    authors_json = json.loads(serializers.serialize("json", authors))
    authors_list = []
    for author_json in authors_json:
        authors_list.append(author_json["fields"])
    response["author_list"] = authors_list
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})


@require_http_methods(["GET"])
def get_all_graph(request):
    response = {}
    try:
        relation_list = []
        entity_list = []
        if request.GET.get("name") == '' or request.GET.get("name") is None:
            entities = db.cypher_query("MATCH (n:textileTec) RETURN n")
            relations = db.cypher_query("MATCH (n:textileRelation) RETURN n")
        else:
            relations = db.cypher_query(
                "MATCH (m:textileRelation{from:'" + str(request.GET.get("name")) + "'}) return m")
            entities = db.cypher_query(
                "MATCH (m:textileRelation{from:" + "'" + str(request.GET.get(
                    "name")) + "'" + "}) MATCH (n:textileTec) "
                                     "where n.name=m.to or n.name=m.from RETURN distinct n ")
        for entity in entities[0]:
            entity = str(entity)
            entity_list.append(eval(entity[entity.index("={") + 1:entity.index(">")]))
        for relation in relations[0]:
            relation = str(relation)
            relation_list.append(eval(relation[relation.index("={") + 1:relation.index(">")]))
        response["status"] = 200
        response["entity_list"] = entity_list
        response["relation_list"] = relation_list
        return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400})


@require_http_methods(["GET"])
def get_project_graph(request):
    knowledgeGraph = {}
    knowledgeGraph["type"] = "force"
    knowledgeGraph["categories"] = [{"name": "author"}, {"name": "project"}]
    knowledgeGraph["nodes"] = []
    knowledgeGraph["links"] = []
    try:
        authors = []
        relations = []
        if request.GET.get("name") == '' or request.GET.get("name") is None:
            authors = db.cypher_query("MATCH (n:author) RETURN n")
            projects = db.cypher_query("MATCH (n:author2) RETURN n ")
            relations = db.cypher_query("MATCH (n:projRelations2) RETURN n")
        for author in authors[0][1:]:
            author = str(author)
            author_info = eval(author[author.index("={") + 1:author.index(">")])
            author_info["category"] = "author"
            knowledgeGraph["nodes"].append(author_info)

        for project in projects[0][1:]:
            project = str(project)
            project_info = eval(project[project.index("={") + 1:project.index(">")])
            project_info["category"] = "project"
            knowledgeGraph["nodes"].append(project_info)
        for relation in relations[0][1:]:
            relation = str(relation)
            relation_info = eval(relation[relation.index("={") + 1:relation.index(">")])
            knowledgeGraph["links"].append(relation_info)

        return JsonResponse(knowledgeGraph, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        print(e)
        return JsonResponse({"status": 400})
    pass


def getSearch_graph(request, techName=None, **kwargs):
    return HttpResponse("<h1>根据搜索条件返回指定知识图谱</h1>")
    pass
