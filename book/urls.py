from django.urls import path
from .views import BookView, BookDetailView


app_name = 'books'
urlpatterns = [
    path('list/', BookView.as_view(),name='list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
]
