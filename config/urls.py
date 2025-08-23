from django.contrib import admin
from django.urls import path, include
from .view import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('users/', include('user.urls')),
]
