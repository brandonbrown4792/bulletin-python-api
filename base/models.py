# myapp/tasks.py
from celery import shared_task
from base.models.post import Post
from base.services.post import create_post as create_post_service

@shared_task
def create_post(data):
    create_post_service(data)
