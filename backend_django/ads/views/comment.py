from rest_framework.viewsets import ModelViewSet

from ads.models import Comment
from ads.serializers import CommentSerializer


class AdViewSet(ModelViewSet):
    """
    A viewset for GET, POST
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
