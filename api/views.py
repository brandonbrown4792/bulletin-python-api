from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.serializers.post_serializer import PostAllSerializer
from base.models.post import Post
from base.tasks.post.create_task import create_post as create_post_task
from base.services.post_service import create_post as create_post_service

@api_view(['GET'])
def getData():
    posts = Post.objects.all()
    serializer = PostAllSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPost(request):
    serializer = PostAllSerializer(data=request.data)
    if serializer.is_valid():
        response = create_post_service(serializer.data)
        return Response(PostAllSerializer(response).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def addCeleryPost(request):
    serializer = PostAllSerializer(data=request.data)
    if serializer.is_valid():
        create_post_task.delay(serializer.validated_data)
        return Response('Added to celery')
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
