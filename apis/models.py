from django.db import models
from django.utils import timezone


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    image = models.ImageField(upload_to='service_images/', blank=True, null=True)
    #image

class CaseStudy(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField(default=timezone.now, blank= True, null= True)
    image = models.ImageField(upload_to='case_study_images/', blank=True, null=True)
    #image
