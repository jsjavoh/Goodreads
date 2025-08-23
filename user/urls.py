from django.urls import path
from .views import RegisterView

app_name = 'user'
urlpatterns = [
    path('signup/', RegisterView.as_view(), name='register'),
]