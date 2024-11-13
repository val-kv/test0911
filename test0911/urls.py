from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('slider.urls')),
    path('filer/', include('filer.urls')),
]
