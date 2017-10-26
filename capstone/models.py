from django.db import models

# Create your models here.
class SubjectArea(models.Model):
    subjectID = models.IntegerField(primary_key=True,default=123)
    subjectName = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):  
        return self.subjectName

class Researcher(models.Model):
    persNo = models.IntegerField(primary_key=True)
    firstName = models.TextField()
    lastName = models.TextField()
    name = models.TextField(default="potato")
    faculty = models.CharField(max_length=100, default="fac")
    department = models.CharField(max_length=100, default="dept")
    position = models.CharField(max_length=100)
    subjectArea = models.ForeignKey(SubjectArea, on_delete=models.SET_NULL, null=True)
    numberOfPubs = models.IntegerField()
    numberOfCitations = models.IntegerField()
    hIndex = models.IntegerField()

    def __str__(self):  
        return self.name

class Publication(models.Model):
    pubID = models.IntegerField(primary_key=True, default=12345)
    title = models.TextField()
    year = models.IntegerField()
    numberOfCitations = models.IntegerField()
    researchers = models.ManyToManyField(Researcher)

    def __str__(self):  
        return self.title

class Queue(models.Model):
    queueID = models.IntegerField(primary_key=True)
    researchers = models.ForeignKey(Researcher, on_delete=models.CASCADE)