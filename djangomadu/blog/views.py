from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'Madu Lokal',
        'subjudul': 'Blog',
        'nav'   : [
            ['/','Home'],
            ['/blog/cerita', 'Cerita'],
            ['/blog/news','News'],
        ]
    }
    return render(request,'blog/index.html',context)