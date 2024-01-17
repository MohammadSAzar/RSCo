from django.urls import path

from . import views


urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    # path('profile/update/', views.profile_update_view, name='profile_update'),
    path('signup/', views.select_user_type_signup_view, name='signup'),
    path('signup/customer/', views.CaseCustomerSignupView.as_view(), name='case_customer_signup'),
    path('signup/agent/', views.ServiceCustomerSignupView.as_view(), name='service_customer_signup'),
]

