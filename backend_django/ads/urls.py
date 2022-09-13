from django.urls import path, include

from ads.views import AdViewSet
from rest_framework import routers

ads_router = routers.SimpleRouter()
ads_router.register('ads', AdViewSet)

urlpatterns = [
    path('', include(ads_router.urls)),
]
