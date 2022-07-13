from django.contrib import admin
from .models import ContactModel, ContactLink, About, Social, ImageAbout


class ContactModelAdmin(admin.ModelAdmin):
    model = ContactModel
    list_display = ['id', 'name', 'create_at']
    list_display_links = ['name']


class ImageAboutInLine(admin.StackedInline):
    model = ImageAbout
    extra = 3


class AboutAdmin(admin.ModelAdmin):
    model = About
    inlines = [ImageAboutInLine]


admin.site.register(ContactModel, ContactModelAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(ContactLink)
admin.site.register(Social)