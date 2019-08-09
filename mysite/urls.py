from django.urls import path
from . import views

app_name='mysite'

urlpatterns = [
    path('', views.input, name='input'),
    path('result', views.result, name='result')
]