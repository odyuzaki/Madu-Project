from django.shortcuts import render

#

def index(request):
    context = {
        'judul' : 'Blog',
        'subjudul': 'Blog Madu Lokal',
        'banner': 'about/img/about.jpg',
    }
    return render(request,'index.html',context)