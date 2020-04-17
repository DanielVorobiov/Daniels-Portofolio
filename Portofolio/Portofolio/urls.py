from . import views
from django.contrib import admin
from django.urls import path, include
from registration import views as regviews
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.home, name="index"),
    path('home/',views.home, name="index"),
    path('gallery/', views.gallery,name="gallery"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('signup/', regviews.registration, name="registration"),
    path('admin/', admin.site.urls),
    path('', include("django.contrib.auth.urls")),
]
admin.site.site_header = 'Daniels Portofolio Admin Page'
admin.site.index_title = 'Features area'

