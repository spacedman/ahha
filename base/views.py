""" Views for the base application """

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from jsonview.decorators import json_view

from . import models

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

@login_required
@json_view
def hospital(request, year, month):
    records = models.DailyRecord.objects.filter(date__month=month, date__year=year)
    MedActual = [record.MedActual for record in records]
    SurgActual = [record.SurgActual for record in records]
    #return render(request, 'base/home.html')
    return {
        'date': [str(record.date) for record in records],
        'MedActual': MedActual,
        'SurgActual': SurgActual}

