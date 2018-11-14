from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def index(request):
    return render(request, 'basicPages/index.html')

def aboutUs(request):
    return render(request, 'basicPages/aboutUs.html')