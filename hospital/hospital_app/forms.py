from django import forms
from hospital_app.models import Doctor_table,Patient
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]
        widgets={
            "username": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Username'}),
            "email": forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Email'}),
            "password": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Password'})
            
        }
        
class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","password"]
        widgets={
            "username": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Username'}),
            "password": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Password'})
        }
        
class DoctorAddForm(forms.ModelForm):
    class Meta:
        model = Doctor_table
        fields = ['name', 'department', 'phone', 'email']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter doctor name'}),
            "department": forms.Select(attrs={'class': 'form-select'}),
            "phone": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter phone number'}),
            "email": forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter email address'}),
        }

class DoctorEditForm(forms.ModelForm):
    class Meta:
        model = Doctor_table
        fields = ['name', 'department', 'phone', 'email']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter doctor name'}),
            "department": forms.Select(attrs={'class': 'form-select'}),
            "phone": forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter phone number'}),
            "email": forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter email address'}),
        }
        
class PatientAddForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'phone', 'address', 'doctor']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient name'}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            "gender": forms.Select(attrs={'class': 'form-select'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            "address": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address', 'rows': 3}),
            "doctor": forms.Select(attrs={'class': 'form-select'}),
        }
        
class PatientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'phone', 'address', 'doctor']
        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter patient name'}),
            "age": forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            "gender": forms.Select(attrs={'class': 'form-select'}),
            "phone": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            "address": forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter address', 'rows': 3}),
            "doctor": forms.Select(attrs={'class': 'form-select'}),
        }