from django.shortcuts import render

def index(request):
    context = {
        'title' : 'Madu Lokal',
        'heading' : 'Selamat datang',
        'subheading': 'di madu lokal',
    }
    return render(request,'index.html',context)