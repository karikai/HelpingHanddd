from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Post
from datetime import date

def wordWall_Index(request):
    context = {
        'posts': Post.objects.all()
    }

    m = request.method
    print(m)

    if m == 'POST':
        title_r = request.POST.get('title')
        content_r = request.POST.get('content')
        today = str(date.today())
        check = None

        if (request.POST.get('title') != '') and (request.POST.get('content') != ''):
            check = True
        else:
            check = False

        if check == True:
            input_data = Post(title = title_r ,content = content_r, date_posted = today)
            print(input_data.title,input_data.content,input_data.date_posted)
            input_data.save()

        return render(request, 'wordWall/wordWall_Index.html', context)
    else:
        return render(request, 'wordWall/wordWall_Index.html', context)
