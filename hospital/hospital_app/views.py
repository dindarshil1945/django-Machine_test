from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from hospital_app.forms import RegisterForm,LoginForm,DoctorAddForm,DoctorEditForm,PatientAddForm,PatientEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from hospital_app.models import Doctor_table,Patient
# Create your views here.

class RegisterView(View):
    def get(self,request):
        form=RegisterForm()
        return render(request,"register.html",{"form":form})
    def post(self,request):
        form=RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"User registered Succesfully")
            return redirect("login")
        else:
            messages.warning(request,"Invalid")
            return redirect("register")
        
class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        username=request.POST.get("username")
        password=request.POST.get("password")
        
        res= authenticate(request,username=username,password=password)
        
        if res:
            login(request,res)
            messages.success(request,"Login Succesful")
            return redirect("home")
        else:
            messages.warning(request,"Invalid")
            return redirect("login") 

class HomeView(View):
    def get(self,request):
        if request.user.is_authenticated:
            doctor=Doctor_table.objects.all()
            patients=Patient.objects.all()
            return render(request,"home.html",{"doctors":doctor,"patients":patients})
        else:
            messages.warning(request,"You Must Login First")
            return redirect("login")
        
class AddDoctorView(View):
    def get(self,request):
        form=DoctorAddForm()
        return render(request,"add_doctor.html",{"form":form})
    def post(self,request):
        form=DoctorAddForm(request.POST)
        if form.is_valid():
            Doctor_table.objects.create(**form.cleaned_data)
            messages.success(request,"added succesfully")
            return redirect("home")
        else:
            messages.warning(request,"Invalid")
            return redirect("add_doctor")
        
class DoctorEditView(View):
    def get(self,request,*args, **kwargs):
        doctor=Doctor_table.objects.get(id=kwargs.get("id"))
        form=DoctorEditForm(instance=doctor)
        return render(request,"edit_doctor.html",{"form":form})
    def post(self,request,*args, **kwargs):
        doctor=Doctor_table.objects.get(id=kwargs.get("id"))
        form=DoctorEditForm(request.POST,instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated succesfully")
            return redirect("home")
        
class DoctorDeleteView(View):
    def get(self,request,*args, **kwargs):
        doctor=Doctor_table.objects.get(id=kwargs.get("id"))
        doctor.delete()
        messages.success(request,"Deleted Succesfully")
        return redirect("home")
    
class AddPatientView(View):
    def get(self,request):
        form=PatientAddForm()
        return render(request,"add_patient.html",{"form":form})
    def post(self,request):
        form=PatientAddForm(request.POST)
        if form.is_valid():
            Patient.objects.create(**form.cleaned_data)
            messages.success(request,"added succesfully")
            return redirect("home")
        else:
            messages.warning(request,"Invalid")
            return redirect("add_patient")

class PatientEditView(View):
    def get(self,request,*args, **kwargs):
        patient=Patient.objects.get(id=kwargs.get("id"))
        form=PatientEditForm(instance=patient)
        return render(request,"edit_patient.html",{"form":form})
    def post(self,request,*args, **kwargs):
        patient=Patient.objects.get(id=kwargs.get("id"))
        form=PatientEditForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request,"Updated succesfully")
            return redirect("home")

class PatientDeleteView(View):
    def get(self,request,*args, **kwargs):
        patient=Patient.objects.get(id=kwargs.get("id"))
        patient.delete()
        messages.success(request,"Deleted Succesfully")
        return redirect("home")

class LogoutView(View):
    def get(self,request):
        logout(request)
        messages.success(request,"Logged Out Succesfully")
        return redirect("login")