from django.urls import path, re_path, include

from . import views


urlpatterns = [
    # path('', views.PostListView.as_view(), name='post_list'),
    # path('create/', views.PostCreateView.as_view(), name='post_create'),
    # path(r'^case/(?P<slug>[-\w]+)/update/', views.PostUpdateView.as_view(), name='post_update'),
    # path(r'^case/(?P<slug>[-\w]+)/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    # re_path(r'^case/(?P<slug>[-\w]+)/', views.CaseDetailView.as_view(), name='post_detail'),
]

