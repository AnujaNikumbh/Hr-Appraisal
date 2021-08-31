from django.shortcuts import render
from rest_framework import generics
from api.models import Book
from api.serializers import BookSerializer
# Create your views here.

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView): #toupdate and del records
    queryset = Book
    serializer_class = BookSerializer


