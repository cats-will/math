from django.urls import path
from . import views


urlpatterns = [
    path('1/', views.task, name='tasks')
]
