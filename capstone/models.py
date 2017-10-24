from django.db import models

# Create your models here.
class Researcher(models.Model):
    persNo = models.IntegerField()
    firstName = models.TextField()
    lastName = models.TextField()
    position = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=100)
    numberOfPubs = models.IntegerField()
    numberOfCitations = models.IntegerField()
    hIndex = models.IntegerField()

class Publication(models.Model):
    title = models.TextField()
    year = models.IntegerField()
    numberOfCitations = models.IntegerField()
    researchers = models.ManyToManyField(Researcher)

class SubjectArea(models.Model):
    subjectName = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    researchers = models.ManyToManyField(Researcher)
