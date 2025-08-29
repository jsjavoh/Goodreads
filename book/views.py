from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Book, BookReview
from django.views import View
from django.core.paginator import Paginator
from .forms import BookReviewForm



class BookView(LoginRequiredMixin,View):

    def get(self, request):
        books = Book.objects.all().order_by('id')

        search_query = request.GET.get('q')
        if search_query:
            books = books.filter(title__icontains=search_query)

        paginator = Paginator(books, 2)
        page_num = request.GET.get('page',1)

        page_obj = paginator.get_page(page_num)
        return render(request, 'book/list.html',{'page_obj':page_obj})



class BookDetailView(LoginRequiredMixin, View):

    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        review_form = BookReviewForm()
        return render(request, 'book/detail.html',{'book':book,'review_form':review_form})


class AddReviewView(LoginRequiredMixin, View):

    def post(self, request, pk):
        review_form = BookReviewForm(request.POST)
        user = request.user
        book = Book.objects.get(id=pk)
        if review_form.is_valid():
            BookReview.objects.create(
                book = book,
                user = user,
                star_given = review_form.cleaned_data['star_given'],
                commit = review_form.cleaned_data['commit']
            )
            return redirect(reverse('books:detail', kwargs={'pk':book.id}))
        return render(request, 'book/detail.html',{'book':book,'review_form':review_form})


