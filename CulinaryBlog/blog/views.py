from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView
from blog.models import Post, Comment
from .forms import CommentForm


class HomeView(ListView):
    """Отображение постов на главной странице"""
    model = Post
    paginate_by = 9
    template_name = 'blog/home.html'


class PostListView(ListView):
    """Отображение постов в конкретной категории"""
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get('slug')).select_related('category')


class PostDetailView(DeleteView):
    """Отображение одного поста"""
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class CreateComment(CreateView):
    """Отображение комментариев к посту"""
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()
