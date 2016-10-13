# coding=utf-8

from django.http import HttpResponse
from django.template import loader
from transfers.models import Transfer
from assets.models import DetailFeature

# Create your views here.


def viewAsset(request):
    template = loader.get_template('view_asset.html')
    listTransfer = Transfer.objects.filter(fkasset__id=1)
    # listSon = DetailFeature.objects.filter(fkasset__id=1)
    listDetail = DetailFeature.objects.filter(fkasset__assetfather=1)
    # listAsset = Asset.objects.exclude(fkdescription__description="CPU").filter(assetfather=1)
    title = 'Formulario de Entrega de Equipos'
    context = {
        'listTransfer': listTransfer,
        'listDetail': listDetail,
        # 'listAsset': listAsset,
        # 'listSon': listSon,
        'title': title,
    }
    return HttpResponse(template.render(context, request))