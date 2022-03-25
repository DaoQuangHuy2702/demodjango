from django.urls import path
from . import views

app_name = 'phone'
urlpatterns = [
    path('', views.index, name = "phone"),
    path('<int:id>/', views.phone_detail, name = "detail"),
    path('delete/<int:id>/', views.phone_delete, name = "delete"),
    path('add/', views.add_phone, name="add"),
    path('update/<int:id>/', views.phone_update, name = "update"),
]