from django.contrib import admin
from .models import ContactModel


class ContactModelAdmin(admin.ModelAdmin):
    model = ContactModel
    list_display = ['id', 'name', 'create_at']
    list_display_links = ('name')


admin.site.register(ContactModel, ContactModelAdmin)
