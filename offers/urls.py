from django.urls import path
from . import views

urlpatterns = [
    path('', views.offer_list, name='offer_list'),                # List all offers
    path('<int:pk>/', views.offer_detail, name='offer_detail'),   # View details of a single offer
    path('create/', views.offer_create, name='offer_create'),     # Create a new offer
    path('<int:pk>/edit/', views.offer_edit, name='offer_edit')     # Edit a single offer
]
