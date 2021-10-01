from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomBaseUser 

class RegisterForms(UserCreationForm):	
	class Meta:
		model = CustomBaseUser
		fields = ['email','password1','password2','address']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')

class UserUpdateForms(forms.ModelForm):
	class Meta:
		model = CustomBaseUser
		fields = ['email','address']