from rest_framework import viewsets

from gabinetLaryngologii.blog.models import Post
from gabinetLaryngologii.blog.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get']


