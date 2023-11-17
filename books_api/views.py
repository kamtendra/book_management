from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

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