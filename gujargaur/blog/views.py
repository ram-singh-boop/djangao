from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from website.models import WebPage




def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, "blog/home.html", {'context':context})


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    #-----------------
    def get_context_data(self,**kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['menus'] = WebPage.objects.all()
        return context
    #-----------------
    ordering = ['-date_posted']
    paginate_by = 6


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6
    def get_context_data(self,**kwargs):
        context = super(UserPostListView, self).get_context_data(**kwargs)
        context['menus'] = WebPage.objects.all()
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['menus'] = WebPage.objects.all()
        return context


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['menus'] = WebPage.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def get_context_data(self,**kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['menus'] = WebPage.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def get_context_data(self, **kwargs):
        context = super(PostDeleteView, self).get_context_data(**kwargs)
        context['menus'] = WebPage.objects.all()
        return context

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


@login_required
def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
