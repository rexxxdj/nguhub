import datetime
from django.conf import settings # import the settings file
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import SignInForm


def user_login(request):
    ADMIN_SITE_NAME = settings.DEFAULT_SITE_NAMING
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('equipment:list')
                else:
                    return HttpResponse('Акаунт не активний')
            else:
                return HttpResponse('Невірний логін або пароль')
    else:
        form = SignInForm()

    context = {
        'form': form,
        'ADMIN_SITE_NAME': ADMIN_SITE_NAME
    }
    return render(request, 'signin.html', context)


def user_logout(request):
    logout(request)
    url = reverse('signin')
    return HttpResponseRedirect(url)

