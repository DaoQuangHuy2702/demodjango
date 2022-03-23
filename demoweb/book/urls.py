from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name = "book"),
    path('add/', views.add_book, name="add"),
    path('save/', views.save_book, name="save")
]