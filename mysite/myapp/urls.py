from django.urls import path

from . import views

urlpatterns = [
    path('', views.loginPage, name = 'index'),
    path('search', views.search, name='search'),
]