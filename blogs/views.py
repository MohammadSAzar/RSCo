from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Blog

class BlogListView(ListView):
    queryset = Blog.objects.filter(status='pub')
    paginate_by = 6
    context_object_name = 'blog'
    template_name = 'blogs/blog_list.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogs/blog_detail.html'
    context_object_name = 'blog'


