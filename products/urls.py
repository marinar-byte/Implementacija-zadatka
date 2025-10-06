from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),           # List all products
    path('<int:pk>/', views.product_detail, name='product_detail'),  # View details of a single product
    path('create/', views.product_create, name='product_create'),    # Create a new product
    path('<int:pk>/update/', views.product_update, name='product_update'),  # Update an existing product
]
