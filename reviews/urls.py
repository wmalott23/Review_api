from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews_list), 
    path ('<int:pk>', views.names_detail),
    path('', views.products_list), 
    path ('<int:pk>', views.products_detail),
]
