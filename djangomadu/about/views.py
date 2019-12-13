from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'About',
        'subjudul' : 'Tentang Madu Lokal',
    }
    return render(request,'about/index.html',context)