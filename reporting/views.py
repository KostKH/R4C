import datetime as dt

from django.http import HttpResponse
from django.shortcuts import render

from .reports import ProductionReport


def index(request):
    data = {
        'week': dt.datetime.now().isocalendar().week,
        'year': dt.datetime.now().year
    }
    return render(request, 'reporting/index.html', data)


def production_report(request, year, week):
    xlsx_content_type = ('application/vnd.openxmlformats-'
                         'officedocument.spreadsheetml.sheet')
    response = HttpResponse(content_type=xlsx_content_type)
    response['Content-Disposition'] = f'filename=report_{week}_week.xlsx'
    ProductionReport(week=week, year=year).write_report(response)
    return response
