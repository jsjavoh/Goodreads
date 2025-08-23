from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html',{'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'user/register.html',{'form':form})

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'user/login.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('home')
        return render(request, 'user/login.html',{'form':form})