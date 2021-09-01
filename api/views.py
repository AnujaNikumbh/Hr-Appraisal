from django.http import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
#from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
# Create your views here.


'''@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/book-list/',
        'Detail view': '/book-detail/<int:id>/', 
        'Create':'/product-create/',
        'Update': '/book-update/<int:id>/', 
        'Delete': '/book-detail/<int:id>/',


    }   

    return Response(api_urls)'''
    
@api_view(['GET'])
def ShowAll(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewBook(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(book, many=False)
    return Response(serializer.data)

    
@api_view(['POST'])
def CreateBook(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateBook(request,pk):
    book = Book.objects.get(id=pk)
    serializer = BookSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)   


@api_view(['GET'])
def deleteBook(request,pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return Response('Items deleted successfully')      


   