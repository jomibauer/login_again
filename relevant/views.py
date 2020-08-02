from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render, redirect, reverse
import crypt

from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_info = form.cleaned_data
            if login_info['password'] != 'welcome':
                return render(request, "login/login_page.html", {'form': form, 'error_message':'The password you  '
                                                                                               'entered is incorrect'})
            user = login_info['username']
            hashuser = crypt.crypt(user, salt=crypt.mksalt())

            return redirect(reverse('welcome', kwargs={'user': user, 'hashuser': hashuser}))
    else:
        form = LoginForm()

    return render(request, "login/login_page.html", {'form': form})


def welcome(request, user, hashuser):
    if crypt.crypt(user, salt=hashuser[:2]) == hashuser:
        return HttpResponse("Welcome, " + user)
    else:
        raise Http404()