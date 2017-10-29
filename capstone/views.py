from django.shortcuts import render
from django.http import HttpResponse
from capstone.models import *

# login
def index(request):
	return render(request, "login.html")

def login(request):
	queue = Queue()
	queue.save()
	res = {'queue':queue}
	print(queue.queueID)
	return render(request, "login.html", res)

def forgotPwd(request):
	return render(request, "forgot-password.html")

def researcher(request):
	return render(request, "userMain.html")

def addResearcher(request, queueID):
	result = {'queueID':queueID}
	return render(request, "addresearcher.html",result)

def searchResult(request, queueID, faculty=None, department=None):
	params = request.GET
	res = 	{'validation':'invalid', 'queueID':queueID}
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
	return render(request, "searchresult.html", res)

def usermain(request):
	return render(request, "userMain.html")

# researcher profile
def researcherChanges(request):
	return render(request, "researcherChanges.html")

def researcherVerified(request):
	return render(request, "researcherVerified.html")

# officer search
def officerResearcherProfile(request, persNo):
	params = request.GET # possibly add researcher?
	persNum = params["persNo"] # assuming persNo is the ID (check models.py)

	# get researcher metrics by persNo
	researchers = Reseacher.objects.filter(fieldname="persNo")
	profile = researchers.values(persNum)

	# get researcher pubs
	pubs = Publication.objects.filter(researcher__in=[persNum]) # need to filter by id in researcher table
	profile["pubs"] = pubs.values()  # add pubs to profiles. {{pubs}} in front end?

	context = dict(profile) # convert profiles list to dict to render?
	return HttpResponse(template.render(request, "userMain.html", context))
