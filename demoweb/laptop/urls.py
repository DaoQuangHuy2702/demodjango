from django.urls import path
from . import views

app_name = 'laptop'
urlpatterns = [
    path('', views.index, name = "laptop"),
]