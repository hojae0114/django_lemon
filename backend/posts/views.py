from django.shortcuts import render
from .models import Photo
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import PhotoSerializer
from rest_framework.response import Response
from . import models
from . import serializers


@api_view(['GET'])
def photo_list(request):
    photos = Photo.objects.all()
    serializer = PhotoSerializer(photos, many=True)
    return Response(serializer.data)


class PostList(generics.ListAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
