from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class AccountSignUpView(CreateView):
  form_class = UserCreationForm
  template_name = "signup.html"
  success_url = reverse_lazy('login')
  
class HomePage(TemplateView):
  template_name = "homepage.html"
