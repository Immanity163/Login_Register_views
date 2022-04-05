from . import views
from django.urls import path
from .views import register,authenticated,logout_view,login_view

urlpatterns = [
    path("login/",views.login_view,name = 'login'),
    path("register/",register.as_view(),name = 'register'),
    path("authenticated/",views.authenticated,name = 'index'),
    path("logout/",views.logout_view,name = 'logout'),

]
