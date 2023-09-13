from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book, UserProfile, Cart, BookHistory
from .serializers import BookSerializer
from django.contrib.auth.models import User
from .serializers import UserProfileSerializer, BookHistorySerializer, CartSerializer
from rest_framework.permissions import IsAuthenticated

def home(request):
    return render(request, "templates/home.html")


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

class CartView(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated] 

class BookHistoryView(generics.ListAPIView):
    queryset = BookHistory.objects.all()
    serializer_class = BookHistorySerializer
    permission_classes = [IsAuthenticated]  