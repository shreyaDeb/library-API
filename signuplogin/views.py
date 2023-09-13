from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from django.contrib.auth.views import LoginView
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth.models import User

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    template_name = 'registration_form.html'


class UserLoginView(LoginView):
    template_name = 'login_form.html'

