from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Madu Lokal',
        'subjudul' : 'Selamat datang',
        'nav' : [
            ['/','Home'],
            ['/blog','Blog']
        ]
    }
    return render(request,'index.html',context)