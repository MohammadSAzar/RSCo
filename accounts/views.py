from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from .models import CustomUser
from .forms import CustomerSignUpForm, AgentSignUpForm

def select_user_type_signup_view(request):
    return render(request, 'registration/signup_select.html')


class CustomerSignupView(CreateView):
    model = CustomUser
    form_class = CustomerSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('case_list')

class AgentSignupView(CreateView):
    model = CustomUser
    form_class = AgentSignUpForm
    template_name = 'registration/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'agent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('case_list')


