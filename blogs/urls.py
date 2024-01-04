from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog_list'),
    # re_path(r'^case/(?P<slug>[-\w]+)/', views.CaseDetailView.as_view(), name='case_detail'),
]

