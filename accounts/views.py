from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


@method_decorator(csrf_exempt, name='dispatch')
class UserListView(LoginRequiredMixin, View):
    """
    View to list all users in the system.
    Supports API and HTML rendering.
    """

    def get(self, request):
        users = User.objects.all()
        if request.headers.get('Content-Type') == 'application/json':
            users_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users]
            return JsonResponse(users_data, safe=False)
        return render(request, 'users/user_list.html', {'users': users})


@method_decorator(csrf_exempt, name='dispatch')
class UserRegistrationView(View):
    """
    View to handle user registration.
    Supports form-based and API registration.
    """

    def get(self, request):
        form = UserCreationForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        if request.headers.get('Content-Type') == 'application/json':
            # Handle API registration
            import json
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            email = data.get('email', '')
            if username and password:
                user = User.objects.create_user(username=username, password=password, email=email)
                return JsonResponse({'message': 'User registered successfully.', 'id': user.id})
            return JsonResponse({'error': 'Invalid data.'}, status=400)

        # Handle form-based registration
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_list')
        return render(request, 'users/register.html', {'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class UserLoginView(View):
    """
    View to handle user login.
    Supports form-based and API login.
    """

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request):
        if request.headers.get('Content-Type') == 'application/json':
            # Handle API login
            import json
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return JsonResponse({'message': 'Login successful.'})
            return JsonResponse({'error': 'Invalid credentials.'}, status=400)

        # Handle form-based login
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_list')
        return render(request, 'users/login.html', {'form': form})


class UserLogoutView(View):
    """
    View to handle user logout.
    """

    def get(self, request):
        logout(request)
        return redirect('user_login')
