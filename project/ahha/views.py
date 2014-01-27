from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        login=False
    else:
        login=True
    return render_to_response("index.html",
                              {'login': login}, 
                              context_instance=RequestContext(request))

def test(request):
    return render_to_response("test.html",
                              {},
                              context_instance=RequestContext(request))
            
    
def login_user(request):
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
        return render_to_response("login.html",
                                  {},
                                  context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(".")

