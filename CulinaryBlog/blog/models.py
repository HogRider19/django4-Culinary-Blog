from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name='past')
    create_at = models.DateTimeField(auto_now_add=True)


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(blank=True, null=True)
    cook_time = models.PositiveIntegerField(blank=True, null=True)
    ingredients = models.TextField()
    directions = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )


class Comment(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    message = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name = 'comment',
        on_delete=models.CASCADE
    )
