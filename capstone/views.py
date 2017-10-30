from django.shortcuts import render
from django.http import HttpResponse
from capstone.models import *

# login
def index(request):
	return render(request, "login.html")

def login(request):
	# create new Queue object upon login
	queue = Queue()
	queue.save()
	res = {'queue':queue}
	return render(request, "login.html", res)

def forgotPwd(request):
	return render(request, "forgot-password.html")

def addResearcher(request, queueID):
	result = {'queueID':queueID}
	return render(request, "addresearcher.html", result)

def searchResult(request, queueID, faculty=None, department=None):
	params = request.GET
	res = 	{'validation':'invalid', 'queueID':queueID}
	if params:
		res['validation'] = 'valid'
		researchers = Researcher.objects.filter(name__icontains=params['name'])

		try:
			faculty = params['faculty']
			department = params['department']
		except:
			faculty = None
			department = None

		if faculty:
			if faculty != 'Select Faculty':
				researchers = researchers.filter(faculty__icontains=faculty)
		if department:
			if department != 'Select Department':
				researchers = researchers.filter(department__icontains=department)

		res['researchers'] = researchers
	else:
		res['validation'] = "invalid"
	return render(request, "searchresult.html", res)

def officerResearcherProfile(request, queueID, persNo):
	profile = {"queueID":queueID}
	# get researcher object by persNo
	researcher = Researcher.objects.filter(persNo=persNo)
	profile["researcher"] = researcher
	# get researcher pubs objects by persNo
	pubs = Publication.objects.filter(researchers__persNo=persNo)
	profile["publications"] = pubs
	# get search history (queue items)
	profile["searched"] = QueueItems.objects.filter(queueID=queueID)
	# PLEASE CHANGE RESEARCHER.DEPARTMENT TO CONTAIN A FULL DESCRIPTION (e.g. BIOL SCI to 'Biological Sciences')
	return render(request, "userMain.html", profile)

# researcher profile
def researcherChanges(request):
	return render(request, "researcherChanges.html")

def researcherVerified(request):
	return render(request, "researcherVerified.html")
