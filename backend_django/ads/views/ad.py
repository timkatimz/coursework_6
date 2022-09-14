from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad
from ads.serializers import AdSerializer, AdListSerializer, AdRetrieveSerializer, AdCreateSerializer

from users.models import User


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    serializer_action_classes = {
        'list': AdListSerializer,
        'retrieve': AdRetrieveSerializer,
        'create': AdCreateSerializer,
    }

    @action(detail=False, methods=['get'], name='Ads for authorized user', url_path=r'me')
    def user_ads(self, request, *args, **kwargs):
        current_user = self.request.user
        queryset = Ad.objects.filter(author=current_user)

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
