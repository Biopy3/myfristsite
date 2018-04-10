from django.db import models

# Create your models here.

class Records(models.Model):
    user = models.CharField(max_length=200)
    inputfile = models.FileField(upload_to ='species_tree/recordsfile/')
    access_code = models.CharField(max_length=15)
    resultfile = models.FileField()
    email = models.EmailField()

class clustalx_model(models.Model):
    user = models.CharField(max_length=200)
    inputfile = models.FileField(upload_to ='species_tree/recordsfile/')
    access_code = models.CharField(max_length=15)
    output_file = models.FileField()
    email = models.EmailField()
