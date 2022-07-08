from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'create_at', 'id']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'prep_time', 'cook_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Post, PostAdmin)
