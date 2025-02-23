from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('add', views.addPost, name='addPost'),
    path('add-celery', views.addCeleryPost, name='addCeleryPost'),
]
