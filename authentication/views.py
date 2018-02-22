from django.shortcuts import redirect, render, render_to_response
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from .forms import UserCreateForm
from django.utils.translation import ugettext as _
from django.core.context_processors import csrf

from utils.token_generator import tokens_email, tokens_expire_date
from utils.mail_sender import mail_sender
from .models import User

import datetime


def register(request, template_name="adminInterface/register.html"):
    form = UserCreateForm(request.POST or None)

    if request.POST:
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse(login_function))

    c = {"form": form,
         "request": request}

    c.update(csrf(request))

    return render_to_response(template_name, c)