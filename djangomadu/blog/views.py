from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul' : 'Blog',
        'subjudul': 'Blog Madu Lokal',
        'banner': 'about/img/about.jpg',
  #      'nav'   : [
   #         ['/','Home'],
    ###  ]
    }
    return render(request,'index.html',context)