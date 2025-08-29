from django.urls import path
from .views import BookView, BookDetailView, AddReviewView


app_name = 'books'
urlpatterns = [
    path('list/', BookView.as_view(),name='list'),
    path('detail/<int:pk>/', BookDetailView.as_view(), name='detail'),
    path('detial/<int:pk>/review/', AddReviewView.as_view(), name='review'),
]
