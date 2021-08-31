from rest_framework import serializers
from api.models import Book

#serializerscreated

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','title','author','isbn','publisher']