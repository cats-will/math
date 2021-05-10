from django.contrib import admin
from django.urls import path, include

from users.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("task/", include("tasks.urls")),

]

handler404 = pageNotFound
