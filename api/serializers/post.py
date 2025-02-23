from rest_framework import serializers
from base.models.post import Post

class PostAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
