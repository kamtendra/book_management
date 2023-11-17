from django.urls import path
from .views import BookList, BookDetail, UpdateTitleView, UpdateAuthorView, UpdatePublicationYearView
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('', include_docs_urls(title='Your API Documentation')),
    path('books/<int:pk>/update-title/', UpdateTitleView.as_view(), name='update-title'),
    path('books/<int:pk>/update-author/', UpdateAuthorView.as_view(), name='update-author'),
    path('books/<int:pk>/update-publication-year/', UpdatePublicationYearView.as_view(), name='update-publication-year'),
]
