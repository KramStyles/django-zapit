from rest_framework import serializers

from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        author = serializers.ReadOnlyField(source='author.username')
        author_id = serializers.ReadOnlyField(source='author.id')

        model = Post
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id']
        model = Vote
