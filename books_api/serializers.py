from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    
        def validate_title(self, value):
            """
            Validate that the title is not empty and has a maximum length of 100 characters.
            """
            if not value:
                raise serializers.ValidationError("Title cannot be empty.")
            if len(value) > 100:
                raise serializers.ValidationError("Title cannot exceed 100 characters.")
            return value

        def validate_author(self, value):
            """
            Validate that the author is not empty and has a maximum length of 100 characters.
            """
            if not value:
                raise serializers.ValidationError("Author cannot be empty.")
            if len(value) > 100:
                raise serializers.ValidationError("Author cannot exceed 100 characters.")
            return value

        def validate_publication_year(self, value):
            """
            Validate that the publication year is a positive integer.
            """
            if not isinstance(value, int) or value <= 0:
                raise serializers.ValidationError("Publication year must be a positive integer.")
            return value