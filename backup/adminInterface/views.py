from django.shortcuts import render, render_to_response, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from .models import Image
from authentication.models import User
from home.views import home


@login_required()
def newimage(request):
    if request.POST:
        post = Image()

        post.title = request.POST['title']
        post.country = request.POST['country']
        post.category = request.POST['category']
        post.which_user = request.user

        if request.FILES:
            post.image = request.FILES['image']

        post.save()

        return redirect(reverse(home))

    c = {"request": request}
    c.update(csrf(request))

    return render_to_response("admininterface/new-image.html",c)