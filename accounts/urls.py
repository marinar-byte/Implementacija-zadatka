from django.urls import path
from .views import UserListView, UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
]
