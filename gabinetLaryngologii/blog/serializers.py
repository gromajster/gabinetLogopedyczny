from django.contrib.auth.models import User, Group
from rest_framework import serializers

from gabinetLogopedyczny.blog.models import Post


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']
#
#
# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    published_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

    class Meta:
        model = Post
        fields = ['id', 'title', 'picture_url', 'long_text', 'published_date', 'published_time', 'published']
