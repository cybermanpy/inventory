# coding=utf-8

from django.http import HttpResponse
from django.template import loader
from transfers.models import Transfer
from assets.models import DetailFeature

# Create your views here.

def viewTransfer(request):
    title = "Lista de equipos trasladados"
    template = loader.get_template('view_transfer.html')
    listTransfer = Transfer.objects.filter(last=True)
    context = {
        'title':  title,
        'listTransfer': listTransfer,
    }
    return HttpResponse(template.render(context, request))


def printTransfer(request, pkasset):
    title = 'Formulario de Entrega de Equipos'
    template = loader.get_template('print_transfer.html')
    listTransfer = Transfer.objects.filter(fkasset__id=pkasset, last=True)
    listDetail = DetailFeature.objects.filter(fkasset__assetfather=pkasset)
    context = {
        'title': title,
        'listTransfer': listTransfer,
        'listDetail': listDetail,
    }
    return HttpResponse(template.render(context, request))
    

    # listSon = DetailFeature.objects.filter(fkasset__id=1)
    # listAsset = Asset.objects.exclude(fkdescription__description="CPU").filter(assetfather=1)