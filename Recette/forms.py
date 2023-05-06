from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = recipe
        # fields = ['title', 'difficulty', 'ingredients', 'instructions', 'image','created_date']
        fields = '__all__'

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField(max_length='63')
    password = forms.CharField(max_length='63', widget=forms.PasswordInput())
