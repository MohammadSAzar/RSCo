from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, HttpResponse
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Blog

class BlogListView(ListView):
    queryset = Blog.objects.select_related('blog_category', 'author').filter(status='pub')
    paginate_by = 6
    context_object_name = 'blog'
    template_name = 'blogs/blog_list.html'


# class BlogDetailView(DetailView):
#     model = Blog
#     template_name = 'blogs/blog_detail.html'
#     context_object_name = 'blog'

def blog_detail_view(request, slug):
    # blog = get_object_or_404(Blog, slug=slug)
    blog = Blog.objects.select_related('author').get(slug=slug)
    context = {'blog': blog}
    return render(request, 'blogs/blog_detail.html', context)

