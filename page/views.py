from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

# Create your views here.
media2_dir=settings.MEDIA2_ROOT

def sayHello(response):
    image_ext=('.jpg','svg','png')
    images=[]
    pornstars=[]
    try:
        if os.path.exists(media2_dir):
            for file in os.listdir(media2_dir):
                realpath=os.path.join(media2_dir,file)
                if os.path.isfile(realpath) and realpath.endswith(image_ext):
                    images.append(file)
                    
                elif os.path.isdir(realpath):
                    pornstars.append(file)
    except  e:
        pass
    return render(response,'page/index.html',{'images':images,'pornstars':pornstars})

def porn(request):
    pornstar=request.GET.get('value')
    realpath_pornstar=os.path.join(media2_dir,pornstar)
    image_ext=('.jpg','svg','png')
    images=[]
    directories=[]
    try:
        if os.path.exists(realpath_pornstar):
            for file in os.listdir(realpath_pornstar):
                realpath=os.path.join(realpath_pornstar,file)
                if os.path.isfile(realpath) and realpath.endswith(image_ext):
                    images.append(os.path.join(pornstar,file))
                elif os.path.isdir(realpath):
                    directories.append(os.path.join(pornstar,file))
        else:
            raise
    except  e:
        return HttpResponse(f'{pornstar } not found')
    return render(request,'page/porn.html',{'images':images,'directories':directories})




def pornpics(response):
    return render(response,'page/pornpics.html')
    
def xnxx(response):
    return render(response,'page/xnxx.html')

def anal(response):
    return render(response,'page/anal.html')
