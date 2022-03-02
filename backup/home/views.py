from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from adminInterface.models import Image


def home(request):
    all_images = Image.objects.all()

    c = {'request': request,
         'all_images': all_images}

    c.update(csrf(request))

    return render_to_response("home/index.html", c)