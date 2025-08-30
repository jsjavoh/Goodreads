
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Book(models.Model):

    title = models.CharField(max_length=200)
    discription = models.TextField()
    isbn = models.CharField(max_length=13, unique=True)
    cover_picture = models.ImageField(default='book/download.png')

    def __str__(self):
        return self.title

class Author(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class BookAuthor(models.Model):

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.last_name}'s {self.book.title} book"

class BookReview(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    commit = models.TextField()
    star_given = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    created_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s commit"

