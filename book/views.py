from django.shortcuts import render
from .models import Book
from django.views import View


class BookView(View):

    def get(self, request):
        books = Book.objects.all()
        return render(request, 'book/list.html',{'books':books})



class BookDetailView(View):

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        return render(request, 'book/detail.html',{'book':book})

