from django.shortcuts import render

from .models import Photo


def gallery(request):
    photos1= Photo.objects.all()[0:3]
    photos2=Photo.objects.all()[3:6]
    photos3=Photo.objects.all()[6:9]
    photos4 = Photo.objects.all()[9:13]
    return render(request, 'Gallery.html', {"photos1": photos1,"photos2":photos2,"photos3":photos3, "photos4":photos4})
