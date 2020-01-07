from rest_framework import serializers

from gabinetLaryngologii.material.models import Media


class MediaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Media
        fields = ['id', 'media_name', 'media_description', 'media_url', 'extension']
