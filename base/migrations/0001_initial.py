# Generated by Django 5.1.6 on 2025-02-23 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('image', models.TextField()),
                ('is_news_story', models.BooleanField(default=False)),
                ('source', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.TextField()),
            ],
        ),
    ]
