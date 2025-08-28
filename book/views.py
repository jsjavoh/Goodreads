from django.shortcuts import render
from .models import Book
from django.views import View
from django.core.paginator import Paginator


class BookView(View):

    def get(self, request):
        books = Book.objects.all().order_by('id')

        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)

        paginator = Paginator(books, 2)
        page_num = request.GET.get('page',1)

        page_obj = paginator.get_page(page_num)
        return render(request, 'book/list.html',{'page_obj':page_obj})



class BookDetailView(View):

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        return render(request, 'book/detail.html',{'book':book})

