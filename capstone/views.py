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

def researcher(request):
    return render(request, "researcher.html")

def addResearcher(request):
    return render(request, "addresearcher.html")

# researcher profile
def researcherChanges(request):
    return render(request, "researcherChanges.html")

def researcherVerified(request):
    return render(request, "researcherVerified.html")

# officer search
def officerResearcherProfile(request):
    params = request.GET  # possibly add researcher?
    persNum = params["persNo"]  # assuming persNo is the ID (check models.py)

    # get researcher metrics by persNo
    researchers = Reseacher.objects.filter(fieldname="persNo")
    profile = researchers.values(persNum)

    # get researcher pubs
    # need to filter by id in researcher table
    pubs = Publication.objects.filter(researcher__in=[persNum])
    # add pubs to profiles. {{pubs}} in front end?
    profile["pubs"] = pubs.values()

    context = dict(profile)  # convert profiles list to dict to render?
    return HttpResponse(template.render(request, "userMain.html", context))
