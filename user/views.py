from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import RegisterForm, LoginForm, ProfileForm

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'user/register.html',{'form':form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "User yaratildi hamda Login amalga oshirildi!")
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
            messages.info(request, 'Muvaffaqiyatli Login amalga oshdi.')
            return redirect('home')
        return render(request, 'user/login.html',{'form':form})



class ProfileView(LoginRequiredMixin ,View):

    def get(self, request):
        return render(request, 'user/profile.html',{'user':request.user})

class LogoutView(View, LoginRequiredMixin):

    def get(self, request):
        logout(request)
        messages.success(request,"Siz tizimdan chiqdingiz!")
        return redirect('home')


class ProfileEditView(View, LoginRequiredMixin):

    def get(self, request):
        form = ProfileForm(instance=request.user)
        return render(request, 'user/profile_edit.html', {'form':form})

    def post(self, request):
        form = ProfileForm(data=request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'User malumotlari o\'zgartirildi!')
            return redirect('user:profile')
        return render(request,'user/profile_edit.html', {'form':form})