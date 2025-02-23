from celery import shared_task
from base.models.post import Post
from base.services.post_service import create_post as create_post_service
from api.serializers.post_serializer import PostAllSerializer

@shared_task
def create_post(data):
    print("Data received in Celery task:", data)
    post_data = {
        'author': data.get('author'),
        'content': data.get('content'),
        'image': data.get('image'),
        'is_news_story': data.get('is_news_story', False),
        'source': data.get('source'),
        'title': data.get('title'),
        'url': data.get('url')
    }
    post = create_post_service(post_data)
    return PostAllSerializer(post).data