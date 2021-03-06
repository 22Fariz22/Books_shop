from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from store.models import Book
from store.serializer import BooksSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['price']
    search_fields = ['name', 'author_name']
    ordering_filter = ['author_name', 'price']

def oauth(request):
    return render(request, 'oauth.html')


def create_book(request):
    pass

def all_books(request):
    pass

def update_book(request):
    pass

def delete_book(request):
    pass
