from rest_framework import serializers

from gabinetLaryngologii.blog.models import Post


class PostSerializer(serializers.HyperlinkedModelSerializer):
    published_date = serializers.DateField(format="%d-%m-%Y", input_formats=['%d-%m-%Y', 'iso-8601'])

    class Meta:
        model = Post
        fields = ['id', 'title', 'picture_url', 'long_text', 'published_date', 'published_time', 'published']
