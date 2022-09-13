from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.serializers import AdSerializer, AdListSerializer, AdRetrieveSerializer


class AdViewSet(ModelViewSet):
    """
    A viewset for GET, POST
    """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    serializer_action_classes = {
        'list': AdListSerializer,
        'retrieve': AdRetrieveSerializer,
    }

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
