from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'about',
        'subjudul': 'about Madu Lokal',
        'banner': 'about/img/about.jpg',
    }
    return render(request,'index.html',context)