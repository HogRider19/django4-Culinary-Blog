from django.utils import timezone
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(MPTTModel):
    """Модель категорий"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Tag(models.Model):
    """Модель тегов к посту"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """Модель постов"""
    slug = models.SlugField(max_length=200, default='', unique=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/')
    tags = models.ManyToManyField(Tag, related_name='post')
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        related_name='post',
        on_delete=models.SET_NULL,
        null=True
    )
    author = models.ForeignKey(
        User,
        related_name='posts',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_comments(self):
        return self.comments.all()

    def get_absolute_url(self):
        return reverse('post_single', kwargs={'slug':self.category.slug, 'post_slug':self.slug})


class Recipe(models.Model):
    """Модель рецептов"""
    name = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(blank=True, null=True)
    cook_time = models.PositiveIntegerField(blank=True, null=True)
    ingredients = RichTextField()
    directions = RichTextField()
    post = models.ForeignKey(
        Post,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Comment(models.Model):
    """Модель комментариев к постам"""
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    website = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    create_at = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
