from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from weavingHistory.models import HistoryEvent
from django.core import serializers
import json


# Create your views here.
@require_http_methods(["POST"])
def get_history(request):
    response = {}
    history = HistoryEvent.objects.all()
    response["status"] = 200
    events_json = json.loads(serializers.serialize("json", history))
    events_list = []
    for event_json in events_json:
        events_list.append(event_json["fields"])
    response["event_list"] = events_list
    return JsonResponse(response, json_dumps_params={'ensure_ascii': False})
