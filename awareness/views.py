from django.shortcuts import render


# Create your views here.

def awareness(request):
    return render(request, 'awareness/stats.html')
