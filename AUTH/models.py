import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

male = 'erkak'
female = 'ayol'
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    class genders(models.TextChoices):
        male = male
        female = female
    first_name = models.CharField(max_length=255, default="first_name")
    last_name = models.CharField(max_length=255, default="last_name")
    email = models.EmailField(max_length=255, default="email@gmail.com")
    address = models.CharField(max_length=255, default="anywhere")
    gender = models.CharField(max_length=15, choices=genders.choices, default=male)
    image = models.ImageField(upload_to='users/avatar/', default="static/static_images/none.png")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)