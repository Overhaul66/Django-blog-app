from django.urls import path
from .views import HomePageView, IndividualPostPageView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
  path('', HomePageView.as_view(), name="home"),
  path('post/<int:pk>/', IndividualPostPageView.as_view(),
  name = "post"),
  path("post/new/", BlogCreateView.as_view(), name="new"),
  path("post/update/<int:pk>/", BlogUpdateView.as_view(), name="update"),
  path("post/delete/<int:pk>/", BlogDeleteView.as_view(), name="delete")
]