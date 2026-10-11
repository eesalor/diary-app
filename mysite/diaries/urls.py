from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

app_name = 'diaries'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:userid>', views.UserView, name='user'),
    path('login/', auth_views.LoginView.as_view(template_name='diaries/login.html'), name='login'),
    path('register/', views.RegisterView, name='register'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('delete-', views.CsrfView, name='csrf'),
]