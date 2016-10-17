from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^views/transfer', views.viewTransfer, name='viewTransfer'),
    url(r'^print/(?P<pkasset>[0-9]+)/$', views.printTransfer, name='printTransfer'),
]