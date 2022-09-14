from rest_framework.viewsets import ModelViewSet

from ads.models import Comment
from ads.serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(ad_id=self.kwargs['ad_id'])
