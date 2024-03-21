import uuid
from AUTH.models import User
from django.db import models
from django.utils import timezone

Draft = 'DF', 'Draft'
Published = 'PB', 'Published'
Python = 'Python'
Django = 'Django'
DjangoRestFramework = 'Django RestFramework'
FastApi = 'FastAPI'
Flask = 'Flask'
MySQL = 'MySQL'
Postgresql = 'PostgreSQL'
MongoDB = 'MongoDB'
Git = 'GIT'
GitHub = 'GitHUB'
Docker = 'Docker'
Backend = 'Backend'
Frontend = 'Frontend'
FullStack = 'FullStack'
Male = 'Male'
Female = 'Female'
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post_Model.Status.Published)

class Post_Model(models.Model):
    class Status(models.TextChoices):
        Draft = Draft
        Published = Published
    class Category(models.TextChoices):
        Python = Python
        Django = Django
        DjangoRestFramework = DjangoRestFramework
        FastApi = FastApi
        Flask = Flask
        MySQL = MySQL
        Postgresql = Postgresql
        MongoDB = MongoDB
        Git = Git
        GitHub = GitHub
        Docker = Docker
        Backend = Backend
        Frontend = Frontend
        FullStack = FullStack
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField()
    publish_time = models.DateTimeField(default=timezone.now)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='news/images')
    status = models.CharField(max_length=255,
                              choices=Status.choices,
                              default=Draft
                              )
    objects = models.Manager()
    published = PublishedManager()
    category = models.CharField(choices=Category.choices, max_length=255, default=Backend)
    def __str__(self):
        return self.title

class Hashtag_models(models.Model):
    post = models.ForeignKey(Post_Model, on_delete=models.CASCADE, related_name='hashtag')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Comment_models(models.Model):
    comment = models.ForeignKey(Post_Model, on_delete=models.CASCADE, related_name='comment')
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.user


class Contact_Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    def __str__(self):
        return self.message