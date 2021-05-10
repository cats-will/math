from django.urls import path
from django.contrib.auth import views as logView

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', logView.LoginView.as_view(), name='login'),
]
