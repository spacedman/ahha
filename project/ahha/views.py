from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template import RequestContext

# Create your views here.

def index(request):
    return render_to_response("index.html",{}, 
                              context_instance=RequestContext(request))
