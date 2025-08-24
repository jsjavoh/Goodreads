from django.test import TestCase
from django.urls import reverse
from .models import Book

class BooksTestCase(TestCase):

    def test_no_books(self):
        response = self.client.get(
            reverse("books:list")
        )

        self.assertContains(response, "No books found.")

    def test_books_list(self):
        Book.objects.create(title='utgan kunlar',discription='muallif:Abdulla Qodiriy',isbn=1234567890123)

        response = self.client.get(reverse('books:list'))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

class DetailTestCase(TestCase):

    def setUp(self):
        Book.objects.create(
            title='Utgan kunlar',
            discription='muallif:Abdulla Qodiriy',
            isbn = '1234567890123'
        )


    def test_detail(self):
        book = Book.objects.get(title='Utgan kunlar')

        response = self.client.get(reverse('books:detail', kwargs={'pk':book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.isbn)
        self.assertContains(response, book.discription)