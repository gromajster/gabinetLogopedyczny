from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from gabinetLaryngologii.blog.models import Post
from gabinetLaryngologii.blog.serializers import UserSerializer, GroupSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    http_method_names = ['get']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get']


