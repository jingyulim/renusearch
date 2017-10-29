from django.shortcuts import render
from django.http import HttpResponse
from capstone.models import *

# login
def index(request):
	return render(request, "login.html")

def login(request):
	return render(request, "login.html")

def forgotPwd(request):
	return render(request, "forgot-password.html")

def addResearcher(request):
	return render(request, "addresearcher.html")

def searchResult(request, faculty=None, department=None):
	params = request.GET
	res = 	{'validation':'invalid'}
	if params:
		res['validation'] = 'valid'
		researchers = Researcher.objects.filter(name__icontains=params['name'])
		# try:
		# 	faculty = params['faculty']
		# 	department = params['department']

		# if faculty:
		# 	researchers = researchers.filter(faculty=faculty)
		# if department:
		# 	researchers = researchers.filter(department=department)
		res['researchers'] = researchers
	else:
		res['validation'] = "invalid"
	return render(request, "search.html", res)

def usermain(request):
	return render(request, "userMain.html")

# researcher profile
def researcherChanges(request):
	return render(request, "researcherChanges.html")

def researcherVerified(request):
	return render(request, "researcherVerified.html")

# officer search
def officerResearcherProfile(request, persNo):
	# get researcher metrics by persNo
	researcher = Reseacher.objects.filter(persNo=persNo)
	# get researcher pubs
	pubs = Publication.objects.filter(researcher__in=[persNo]) 
	return HttpResponse(template.render(request, "userMain.html", researcher, pubs))
