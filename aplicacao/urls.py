from django.urls import path
from . import views

app_name = 'aplicacao'

urlpatterns = [
    path('', views.MainHomeView.as_view(), name='main_home')
]