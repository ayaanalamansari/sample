from django.conf.urls import include, url

from region_management.views import api_root
from django.urls import path

urlpatterns = [
    path('', api_root, name='api_root'),
    path('', include('region_management.apps.region.routers'))
]
