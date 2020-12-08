from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.
def login(request):
  return render(request, 'login.html')

@login_required()
def home(request):
  return render(request, 'home.html')


def viewdemo(request):
  return render(request,'dashboard.html')

def viewlist(request):
  return render(request,'de.html')

