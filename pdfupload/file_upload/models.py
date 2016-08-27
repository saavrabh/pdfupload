from __future__ import unicode_literals

from django.db import models
# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    Project_id =  models.IntegerField()
    has_pdfs = []

class Files(models.Model):
    associate_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_id = models.IntegerField()
    has_projects = []
  
