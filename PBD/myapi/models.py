from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User

#modele, co tu dużo mówić
class Category(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=25)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# author jest rozszerzeniem defaultowej tabeli USER django którą wykorzystujemy do logowania i trzymania danych użytkowników 
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Role(models.TextChoices):
        ADMIN = 'ADMIN'
        EDITOR = 'EDITOR'
        USER = 'USER'
    role = models.TextField(
        max_length=6,
        choices=Role.choices,
        default=Role.USER
    )

    def __str__(self):
        return self.user.username


class Post(models.Model):
    post_title = models.CharField(max_length=255)
    content = models.TextField()
    categories = models.ManyToManyField(
        'Category', related_name='category_posts')
    tags = models.ManyToManyField('Tag', related_name='tag_posts')
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='author_posts')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
