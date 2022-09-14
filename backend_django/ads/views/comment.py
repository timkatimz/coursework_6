from rest_framework.viewsets import ModelViewSet

from ads.models import Comment
from ads.serializers import CommentSerializer, CommentListSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    serializer_action_classes = {
        'list': CommentListSerializer,
        # 'retrieve': AdRetrieveSerializer,
        # 'create': AdCreateSerializer,
    }

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_id'])

    def get_serializer_class(self):
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()
