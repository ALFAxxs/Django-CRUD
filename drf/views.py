from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import viewsets, permissions

from .serializers import BookSerializer
from .models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'