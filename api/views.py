from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers.post import PostAllSerializer
from base.models.post import Post
# from base.tasks import create_post
from base.services.post import create_post as create_post_service

@api_view(['GET'])
def getData(request):
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

# @api_view(['POST'])
# def addCeleryPost(request):
#     serializer = PostAllSerializer(data=request.data)
#     if serializer.is_valid():
#         create_post.delay(serializer.data)
#         return Response('Added to celery')
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
