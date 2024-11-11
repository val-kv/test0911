from django.shortcuts import render
from .models import SliderImage


def index(request):
    images = SliderImage.objects.all()
    return render(request, 'slider/index.html', {'images': images})
