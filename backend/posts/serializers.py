from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'body',)
        model = models.Post

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = ['id', 'owner', 'comment']
