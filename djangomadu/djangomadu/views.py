from django.shortcuts import render

def index(request):
    context = {
        'judul' : 'Madu Lokal',
        'subjudul' : 'Selamat datang',
        'banner': 'img/home.jpg',
       # 'nav' : [
       #     ['/','Home'],
        #    ['/blog','Blog']]
    }
    return render(request,'index.html',context)