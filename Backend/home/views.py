from django.shortcuts import render, HttpResponse, resolve_url
from home.models import signup_detail

# Create your views here.

def home(request):
    return render(request, "index.html")

def signup(request):
    return render(request, "signup.html")
    

def signup_form(request):
    Name = request.POST['Name']
    pin = request.POST['pin']
    dob = request.POST["DOB"]
    gender = request.POST['gender']
    Blood_Group = request.POST['Blood_Group']
    Vaccine = request.POST['Vaccine']    
    ins = signup_detail(Name=Name, pin=pin, dob=dob, gender=gender, Blood_Group=Blood_Group, Vaccine=Vaccine)
    ins.save()
    return render(request, 'signup.html')

def disease(request):
    return render(request, 'disease.html')

def spo(request):
    return render(request, 'spo.html')

def sym(request):
    return render(request, 'sym.html')
    

