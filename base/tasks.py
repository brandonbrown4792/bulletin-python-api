# # myapp/tasks.py
# from celery import shared_task
# from base.models.post import Post
# from base.services.post import create_post as create_post_service

# @shared_task
# def create_post(data):
#     Post.objects.create(title='New Post from Celery')
from celery import Celery

# Create a Celery app instance and set the broker URL
app = Celery('mysite')

@app.task
def test_redis_task():
    print("Redis connection is working!")