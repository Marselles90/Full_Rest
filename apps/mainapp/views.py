from .models import Author, Book
from rest_framework.viewsets  import ModelViewSet
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import viewsets, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Пагинация книги
class PaginationBook(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    
# ViewsBook
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['author', 'publication_date']
    search_fields = ['title', 'publication_date']
    ordering = ['-publication_date']
    pagination_class = PaginationBook
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    
# Пагинация Автора
class PaginationAuthor(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 50
    
# ViewsAuthor 
class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'birth_date']
    search_fields = ['name', 'birth_date']
    ordering = ['-birth_date']
    pagination_class = PaginationAuthor
    permission_classes = [IsAuthenticatedOrReadOnly]
