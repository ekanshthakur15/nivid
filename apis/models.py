from django.db import models
from django.utils import timezone


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)


    def __str__(self):
        return self.name

class CaseStudy(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField(default=timezone.now, blank= True, null= True)
    image = models.ImageField(upload_to='case_study_images/', blank=True, null=True)


    def __str__(self):
        return self.name
    
class Company(models.Model):

    image = models.ImageField(upload_to="companies/")


class Segment(models.Model):

    case_study = models.ForeignKey(CaseStudy, on_delete= models.CASCADE)
    segment_no = models.IntegerField()
    title = models.TextField()
    image = models.ImageField(blank= True , null= True)
    content = models.TextField(blank=True, null= True)

    def __str__(self):
        return f"{self.case_study.name} : Segment {self.segment_no}"

