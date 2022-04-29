from rest_framework import generics

from .models import Post, Vote
from . import serializers


class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
