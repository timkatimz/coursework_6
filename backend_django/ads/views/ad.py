from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.serializers import AdSerializer


class AdViewSet(ModelViewSet):
    """
    A viewset for GET, POST
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
