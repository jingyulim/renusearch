from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# login
 	return HttpResponse("hello! this is our app")
# Create your views here.

def search(request):
	## take in name faculty department
	## return 
	params = request.GET
	name = params['name']
	fac = params['faculty']
	dept = params['department']
	profile = Researcher.get_all(name).filter
	return HttpResponse("{}".format(dict(params)))

def searchResults(request):
	return ("hello")
