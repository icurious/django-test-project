from nsapp.models import Author,Books
from rest_framework import serializers


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BooksSerializer(many=True,read_only=True)
    class Meta:
        model = Author
        fields = '__all__'