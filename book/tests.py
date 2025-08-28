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
        book1 = Book.objects.create(title='utgan kunlar',discription='muallif:Abdulla Qodiriy',isbn=1234567890123)
        book2 = Book.objects.create(title='utgan kunlar1', discription='muallif: Qodiriy', isbn=2234567890123)
        book3 = Book.objects.create(title='utgan kunlar3', discription='muallif: Abdulla', isbn=3234567890123)


        response = self.client.get(reverse('books:list'))

        books = Book.objects.all()
        for book in [book1, book2]:
            self.assertContains(response, book.title)

        response = self.client.get(reverse('books:list') + '?page=2')

        self.assertContains(response, book3.title)


    def test_search_books(self):
        book1 = Book.objects.create(title='sport', discription='muallif:Abdulla Qodiriy', isbn=1234567890123)
        book2 = Book.objects.create(title='local', discription='muallif: Qodiriy', isbn=2234567890123)
        book3 = Book.objects.create(title='global', discription='muallif: Abdulla', isbn=3234567890123)

        response = self.client.get(reverse('books:list')+'?q=sport')
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('books:list') + '?q=local')
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse('books:list') + '?q=global')
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book1.title)

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


