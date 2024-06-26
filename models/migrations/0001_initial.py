# Generated by Django 5.0.3 on 2024-03-16 13:02

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255)),
                ('body', models.TextField()),
                ('publish_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='news/images')),
                ('status', models.CharField(choices=[('DF', 'Draft'), ('PB', 'Published')], default=('DF', 'Draft'), max_length=255)),
                ('category', models.CharField(choices=[('Python', 'Python'), ('Django', 'Django'), ('Django RestFramework', 'Djangorestframework'), ('FastAPI', 'Fastapi'), ('Flask', 'Flask'), ('MySQL', 'Mysql'), ('PostgreSQL', 'Postgresql'), ('MongoDB', 'Mongodb'), ('GIT', 'Git'), ('GitHUB', 'Github'), ('Docker', 'Docker'), ('Backend', 'Backend'), ('Frontend', 'Frontend'), ('FullStack', 'Fullstack')], default='Backend', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Contact_Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hashtag', to='models.post_model')),
            ],
        ),
        migrations.CreateModel(
            name='Comment_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='models.post_model')),
            ],
        ),
    ]
