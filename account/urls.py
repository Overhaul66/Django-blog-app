from django.urls import path
from .views import AccountSignUpView, HomePage

urlpatterns = [
  path("account/signup", AccountSignUpView.as_view(), name="signup"),
  path("", HomePage.as_view(), name="homepage")
 ]