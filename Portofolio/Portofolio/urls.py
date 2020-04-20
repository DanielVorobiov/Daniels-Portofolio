from . import views,settings
from django.contrib import admin
from django.urls import path, include
from registration import views as regviews
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from gallery import views as galviews
from django.contrib.auth.models import User

urlpatterns = [
    path('',views.home, name="index"),
    path('home/',views.home, name="index"),
    path('gallery/', galviews.gallery,name="gallery"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('signup/', regviews.registration, name="registration"),
    path('admin/', admin.site.urls),
    #path('test/',galviews.gallery,name="gallery"),
    path('', include("django.contrib.auth.urls")),
]
admin.site.site_header = 'Daniels Portofolio Admin Page'
admin.site.index_title = 'Features area'


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
