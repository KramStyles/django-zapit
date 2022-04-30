from rest_framework import (generics, permissions, exceptions, mixins,
                            response, status)

from .models import Post, Vote
from . import serializers


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class VoteView(generics.ListCreateAPIView, mixins.DestroyModelMixin):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = serializers.VoteSerializer

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise exceptions.ValidationError('You cannot vote for the same post twice :-|')

        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(voter=self.request.user, post=post)

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return response.Response('Vote deleted', status= status.HTTP_204_NO_CONTENT)
        return response.Response('You have no vote to cancel', status=status.HTTP_400_BAD_REQUEST)
