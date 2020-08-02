from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('welcome/<str:user>/<str:hashuser>', views.welcome, name="welcome"),
]