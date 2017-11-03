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

def getNewQueueNumber(queueID):
	try:
		number = QueueItems.objects.filter(queueID=queueID).order_by('-queueNum')[0].queueNum
		number += 1
	except:
		number = 1
	return number

def getQueue(queueID):
	inqueue = QueueItems.objects.filter(queueID=queueID).order_by('queueNum')
	return inqueue

def addToQueue(researcher, queueID):
	num = getNewQueueNumber(queueID)
	queue = getQueue(queueID)
	for r in queue:
		if researcher.persNo == r.researchers.persNo:
			return()
	newRinqueue = QueueItems()
	newRinqueue.queueID = queueID
	newRinqueue.queueNum = num
	newRinqueue.researchers = researcher
	newRinqueue.save()

def addResearcher(request, queueID):
	result = {'queueID':queueID, "queue":getQueue(queueID)}
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
		res['queue'] = getQueue(queueID)
	else:
		res['validation'] = "invalid"
	return render(request, "searchresult.html", res)

def officerResearcherProfile(request, queueID, persNo):
	profile = {"queueID":queueID}

	# get researcher object by persNo
	researcher = Researcher.objects.get(persNo=persNo)
	profile["researcher"] = researcher

	# get researcher pubs objects by persNo
	pubs = Publication.objects.filter(researchers__persNo=persNo)
	profile["publications"] = pubs

	addToQueue(researcher,queueID)

	# get search history (queue items)
	profile['queue'] = getQueue(queueID)

	# PLEASE CHANGE RESEARCHER.DEPARTMENT TO CONTAIN A FULL DESCRIPTION (e.g. BIOL SCI to 'Biological Sciences')
	return render(request, "userMain.html", profile)

# researcher profile
def researcherVerify(request):
	return render(request, "researcher.html")

def researcherChanges(request):
	return render(request, "researcherChanges.html")

def researcherVerified(request):
	return render(request, "researcherVerified.html")
