from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import permission_classes
from .permissions import IsAdminEmployeeOrReadOnly

# Create your views here.
@permission_classes([IsAdminEmployeeOrReadOnly])
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer