from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Blog

class BlogListView(ListView):
    queryset = Blog.objects.filter(status='pub')
    paginate_by = 12
    context_object_name = 'blogs'
    template_name = 'blogs/blog_list.html'


