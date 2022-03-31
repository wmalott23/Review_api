from django.urls import path
from . import views

urlpatterns = [
    path('reviews/', views.reviews_list), 
    path ('reviews/<int:pk>', views.reviews_detail),
    path('products/', views.products_list), 
    path ('products/<int:pk>', views.products_detail),
]
