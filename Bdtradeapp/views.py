from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

# def show(request):
#     return render(request, 'base/login.html')

# def signup(request):
#     return render(request, 'base/signup.html')
      