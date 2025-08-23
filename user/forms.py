from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class RegisterForm(forms.ModelForm):

    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class':'input',
            'placeholder':'Password Confirm'
        })
    )

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','password_confirm']

        widgets = {
            'username':forms.TextInput(attrs={
                'class':'input',
                'placeholder':'Username'
            }),
            'first_name':forms.TextInput(attrs={
                'class':'input',
                'placeholder':'First name'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'input',
                'placeholder': 'Last name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input',
                'placeholder': 'Email'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'input',
                'placeholder': 'Password'
            }),
        }


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            self.add_error("password_confirm", "Parol maydonlariga bir xil qiymat kiritilishi shart!")
        return cleaned_data

    def save(self, commit = True):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user


