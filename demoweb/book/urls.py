from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name = "book"),
    path('<int:id>/', views.book_detail, name = "detail"),
    path('delete/<int:id>/', views.book_delete, name = "delete"),
    path('add/', views.add_book, name="add"),
    path('update/<int:id>/', views.book_update, name = "update"),
]