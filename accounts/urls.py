from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.select_user_type_signup_view, name='signup'),
    path('signup/customer/', views.CustomerSignupView.as_view(), name='customer_signup'),
    path('signup/agent/', views.AgentSignupView.as_view(), name='agent_signup'),
]

