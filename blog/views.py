from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from .models import Post

# Create your views here.
class HomePageView(ListView):
  model = Post
  template_name = "home.html"
  
class IndividualPostPageView(DetailView):
  model = Post
  template_name = "post.html"
  
class BlogCreateView(CreateView):
  model = Post
  template_name = "new.html"
  fields = "__all__"
  
class BlogUpdateView(UpdateView):
  model = Post
  template_name = "update.html"
  fields = ["title", "content"]
  
class BlogDeleteView(DeleteView):
  model = Post
  template_name = "delete.html"
  success_url = reverse_lazy("home")