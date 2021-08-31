from rest_framework import serializers
from api.models import Book

#serializerscreated

class BookSerializer(serializers.ModelSerializer):
    class Mets:
        model = Book
        fields = ['title','author','isbn','publisher']