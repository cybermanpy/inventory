# coding=utf-8

from django.http import HttpResponse
from django.template import loader
from assets.models import Asset

# Create your views here.


def viewAsset(request):
    title = 'Lista de Equipos'
    template = loader.get_template('view_asset.html')
    listAsset = Asset.objects.all()
    context = {
        'listAsset': listAsset,
        'title': title,
    }
    return HttpResponse(template.render(context, request))