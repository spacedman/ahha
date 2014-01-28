""" Views for the base application """

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def home(request):
    """ Default view for the root """
    return render(request, 'base/home.html')

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(".")
            else:
                messages.add_message(request,messages.INFO, "Account disabled")
                return HttpResponseRedirect("login")
        else:
            messages.add_message(request,messages.INFO, "Invalid login/pass")
            return HttpResponseRedirect("login")
    else:
        return render(request,"base/login.html")

def logout(request):
    logout(request)
    return HttpResponseRedirect(".")

