from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from django.conf import settings
from .models import Pornstar
from django.core.files import File
import os
import random
from django.core.cache import cache
from .forms import PornstarForm

# Create your views here.


media2_dir = settings.MEDIA2_ROOT


def limit_requests(max_requests=100,timeout=60):
    def decorator(view_func):
        def wrapper(request, *args,**kargs):
            ip_adderss=request.META.get("REMOTE_ADDR")
            cache_key = f"requests_{ip_adderss}"
            cache_key_value=cache.get(cache_key,0)
            if cache.get(cache_key)["count"]>=max_requests:
                
                return HttpResponseBadRequest("Too many requests")
            else:
                cache.set(cache_key,{'count':1},timeout)

def index(request):
    pornstar = request.GET.get("pornstar")
    pornstar_realpath = os.path.join(settings.MEDIA2_ROOT)
    if not os.path.isdir(pornstar_realpath):
        return HttpResponse(f"{pornstar} not exists")
    content = {
        "pornstar": pornstar,
    }
    return render(request, "pornstars/index.html", content)


def pornstars(request):
    pornstar = request.GET.get("pornstar")
    if pornstar is None:
        return render(
            request, "pornstars/index.html", {
                "pornstars": Pornstar.objects.all()}
        )
    realpath_pornstar = os.path.join(media2_dir, pornstar)
    image_ext = (".jpg", "svg", "png")
    images = []
    directories = []
    try:
        if os.path.exists(realpath_pornstar):
            for file in os.listdir(realpath_pornstar):
                realpath = os.path.join(realpath_pornstar, file)
                if os.path.isfile(realpath) and realpath.endswith(image_ext):
                    images.append(os.path.join(pornstar, file))
                elif os.path.isdir(realpath):
                    directories.append(os.path.join(pornstar, file))
        else:
            raise
    except:
        return HttpResponse(f"{pornstar} not found")
    pornstar = Pornstar.objects.get(name=pornstar)
    images.sort()
    return render(
        request,
        "pornstars/profile.html",
        {"images": images, "pornstar": pornstar,
            "categories": pornstar.get_list()},
    )


def add(request):
    if request.method == "POST":
        new_row = PornstarForm(request.POST)
        # if new_row.is_valid:
        #     new_row.save()
    # name=request.POST.get('name')
    # age=request.POST.get('age')
    # height=request.POST.get('height')
    # image=request.POST.get('image_url')
    # eye_color=request.POST.get('eye_color')
    # hair_color=request.POST.get('eye_color')
    # catigories=request.POST.get('catigories')
    # relative_catigories=request.POST.get('relative_catigories')
    # sex=request.POST.get('sex')
    # isalive=bool(request.POST.get('isalive'))
    # new_row=Pornstar(name=name,age=age,height=height,eye_color=eye_color,hair_color=hair_color,sex=sex,isalive=isalive)
    # new_row.set_list(catigories)
    # # with open(image ,'rb') as file:
    #     # new_row.image_link.save(os.path.basename(image),File(image),save=True)
    # if name:
    #     new_row.save()

    return render(request, "pornstars/add.html", {"form": PornstarForm})


def getLink(link):
    if os.path.islink(link):
        newPath = os.readlink(link)
        return getLink(newPath)
    else:
        return link


def slide(request):
    if os.path.exists(media2_dir):
        media_extensions = (".png", ".jpg", ".jpg")
        media_files = []

        for filename in random.sample(os.listdir(media2_dir), 7):
            filename = os.path.join(media2_dir, filename)

            if os.path.islink(filename) and filename.lower().endswith(media_extensions):
                newPath = getLink(filename)
                newFilename = "/".join(newPath.split("/")[-2:])
                media_files.append(newPath)
            elif os.path.isfile(filename) and filename.lower().endswith(media_extensions):
                media_files.append(os.path.join(media2_dir, filename))
            elif os.path.isdir(filename):
                media_files.extend(
                    [
                        "/".join(
                            getLink(os.path.join(media2_dir, filename, i)).split("/")[
                                -2:
                            ]
                        )
                        for i in os.listdir(filename)
                    ]
                )
        random.shuffle(media_files)
        context = {
            "media_files": media_files,
            "first_image": media_files[0],
        }
        return render(request, "pornstars/slide.html", context)
    return HttpResponse("not work well....")
