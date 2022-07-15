from ckeditor.fields import RichTextField
from django.db import models


class ContactModel(models.Model):
    """Класс модели обратной связи"""
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"


class ContactLink(models.Model):
    """Класс модели контактов"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class About(models.Model):
    """Класс модели об авторе"""
    name = models.CharField(max_length=50, default='')
    text = RichTextField()
    mini_text = RichTextField()


class ImageAbout(models.Model):
    """Класс модели изображений в блоке об авторе"""
    image = models.ImageField(upload_to='about/')
    alt = models.CharField(max_length=100, null=True, blank=True)
    page = models.ForeignKey(
        About,
        on_delete=models.CASCADE,
        related_name='images'
    )


class Social(models.Model):
    """Класс модели социальный сетей в блоке об авторе"""
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.name
