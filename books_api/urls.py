from django.urls import path
from .views import BookList, BookDetail, UpdateTitleView, UpdateAuthorView, UpdatePublicationYearView
from rest_framework.documentation import include_docs_urls
from rest_framework.documentation import include_docs_urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your API Documentation",
        default_version='v1',
        description="Your API description",
    ),
    public=True,
)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('', include_docs_urls(title='Your API Documentation')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('books/<int:pk>/update-title/', UpdateTitleView.as_view(), name='update-title'),
    path('books/<int:pk>/update-author/', UpdateAuthorView.as_view(), name='update-author'),
    path('books/<int:pk>/update-publication-year/', UpdatePublicationYearView.as_view(), name='update-publication-year'),
]
