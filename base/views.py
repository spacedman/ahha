""" Views for the base application """

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse

from jsonview.decorators import json_view

from . import models

import calendar
import datetime

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
    
    month=int(month)
    year = int(year)

    fields = ["MedActual","MedPredict","MedTCI",
              "SurgActual","SurgPredict","SurgTCI"]

    
    days = calendar.monthrange(year,month)[1]

    records = list()
    for d in range(days+1)[1:]:
        e = {'date': str(datetime.date(year,month,d))}
        for f in fields:
            e[f]=None
        records.append(e)

    counts = models.DailyRecord.objects.filter(date__month=month, date__year=year)
    for r in counts:
        d = r.date.day - 1
        for f in fields:
            records[d][f]=getattr(r,f)
    return records

def ajaxtest(request):
    return render(request,"base/ajaxtest.html")
