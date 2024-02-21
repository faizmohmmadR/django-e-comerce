from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','quantity','category']
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            'description': forms.Textarea(attrs= {'class': 'form-control'}),
            'price': forms.NumberInput(attrs= {'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs= {'class': 'form-control'}),
            'category': forms.Select(attrs= {'class': 'form-control'}),
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','address','gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'})
        }
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer','products','quantity','total_price','status']
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'products': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={})
        }
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }