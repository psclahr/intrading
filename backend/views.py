import json
from django.http import HttpResponse
from backend.analyse.courses.chartRepository import ChartRepository
from backend.analyse.bootstrap import bootstrap

def historicalDax(request):
    bootstrap()

    chart = ChartRepository().getHistoricalDax()

    return HttpResponse(json.dumps(chart, sort_keys=True, indent=4))

def historicalDaxRecognition(request):
    bootstrap()

    chart = ChartRepository().getHistoricalDaxRecognition()

    return HttpResponse(json.dumps(chart, sort_keys=True, indent=4))


