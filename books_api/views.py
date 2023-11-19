from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import viewsets, status

class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 10

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'author', 'publication_year']
    pagination_class = CustomPageNumberPagination

    def perform_create(self, serializer):
        cover_image = self.request.data.get('cover_image')

        # File size validation (adjust max_size as needed)
        max_size = 2 * 1024 * 1024  # 2 MB
        if cover_image and cover_image.size > max_size:
            return Response({'error': 'File size exceeds the limit'}, status=status.HTTP_400_BAD_REQUEST)

        # File type validation (adjust allowed_types as needed)
        allowed_types = ['image/jpeg', 'image/png']
        if cover_image and cover_image.content_type not in allowed_types:
            return Response({'error': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.validated_data['cover_image'] = cover_image
        serializer.save()

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({'message': 'Book created successfully'}, status=status.HTTP_201_CREATED)
    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    partial_update = True

class UpdateTitleView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        partial_data = {'title': request.data.get('title')}
        return super().update(request, *args, partial=True, **kwargs)

class UpdateAuthorView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        partial_data = {'author': request.data.get('author')}
        return super().update(request, *args, partial=True, **kwargs)

class UpdatePublicationYearView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        partial_data = {'publication_year': request.data.get('publication_year')}
        return super().update(request, *args, partial=True, **kwargs)