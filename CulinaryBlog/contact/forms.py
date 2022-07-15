from django import forms
from .models import ContactModel


class ContactForm(forms.ModelForm):
    """Форма обратной связи с автором"""
    class Meta:
        model = ContactModel
        fields = '__all__'