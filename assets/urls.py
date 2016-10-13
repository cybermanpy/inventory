from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bienes', views.viewAsset, name='viewAsset'),
]