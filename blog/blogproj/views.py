from django.http import HttpResponse
from django.http.response import HttpResponseRedirect

def home(req):
    return HttpResponseRedirect('/blog')

#def index(req):
 #   return HttpResponse("ishan's Project")