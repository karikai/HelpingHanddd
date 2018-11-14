from django.shortcuts import render


def learn(request):
    return render(request, 'education/learn.html')