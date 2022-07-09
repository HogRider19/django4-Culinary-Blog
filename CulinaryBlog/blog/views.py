from django.shortcuts import render
from django.views.generic import ListView, DeleteView
from blog.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'


def home(request):
    return render(request, 'base.html', {})
