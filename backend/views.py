import json
from django.http import HttpResponse
from backend.analyse.index import start

def home(request):
    data = start()
    stringifiedData = json.dumps(data)

    return HttpResponse(data)
