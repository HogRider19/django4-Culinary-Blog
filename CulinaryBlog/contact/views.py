from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.views.generic import CreateView
from .models import ContactLink, About


class ContactView(View):
    """Отображение страницы об авторе"""
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'contact/contact.html', {'contacts': contacts, 'form': form})


class CreateContact(CreateView):
    """Отправка формы обратной связи"""
    form_class = ContactForm
    success_url = '/'


class AboutView(View):
    """Рендер страницы обратной связи"""
    def get(self, request):
        about = About.objects.last()
        return render(request, 'contact/about.html', {'about': about})
