from django.urls import path
from . import views
#urls for app login
urlpatterns=[
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login")
]