from django.urls import path, re_path, include

from . import views


urlpatterns = [
    path('', views.CaseListView.as_view(), name='case_list'),
    path('add/<int:case_id>/', views.add_to_cart_view, name='cart_add'),
    path('detail/', views.cart_detail_view, name='cart_detail'),
    path('create/', views.order_create_view, name='order_create'),
    re_path(r'^case/(?P<slug>[-\w]+)/', views.CaseDetailView.as_view(), name='case_detail'),
]

