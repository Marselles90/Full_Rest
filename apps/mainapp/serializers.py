from rest_framework import serializers
from .models import Author, Book
import re


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

    # Валидация даты
    def validate_birth_date(self, value):
        dates = '\d{4}-\d{2}-\d{2}'
        if not re.findall(dates):
            raise serializers.ValidationError("")
        return value


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'

    # Валидация даты
    def validate_publication_date(self, value):
        dates = '\d{4}-\d{2}-\d{2}'
        if not re.findall(dates):
            raise serializers.ValidationError("")
        return value
