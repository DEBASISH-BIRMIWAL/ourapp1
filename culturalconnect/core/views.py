from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'profile.html')

#def signup(request):
    return render(request, 'signup.html')