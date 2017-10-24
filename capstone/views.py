from django.shortcuts import render
from django.http import HttpResponse

def index(request):
 return HttpResponse("hello! this is our app")
# Create your views here.


def tomato(request):
 params = request.GET
 name = params["scopus_name"]
 ## get their information

 return HttpResponse("{}".format(dict(params)))
