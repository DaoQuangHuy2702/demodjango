from django.urls import path
from . import views

app_name = 'laptop'
urlpatterns = [
    path('', views.index, name = "laptop"),
    path('<int:id>/', views.laptop_detail, name = "detail"),
    path('delete/<int:id>/', views.laptop_delete, name = "delete"),
    path('add/', views.add_laptop, name="add"),
    path('update/<int:id>/', views.laptop_update, name = "update"),
]