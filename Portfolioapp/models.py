from django.db import models
from Authenticationapp.models import Profile



class Project(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_title = models.CharField(max_length=100)
    project_description = models.TextField(max_length=500)
    project_imageone = models.ImageField(upload_to='project_images/')
    project_imagetwo = models.ImageField(upload_to='project_images/')
    project_imagethree = models.ImageField(upload_to='project_images/')
    project_link = models.URLField(blank=True)
    skillsone = models.CharField(max_length=200)
    skill_descriptionone = models.TextField(max_length=500)
    skillstwo = models.CharField(max_length=200)
    skill_descriptiontwo = models.TextField(max_length=500)
    skillsthree = models.CharField(max_length=200)
    skill_descriptionthree = models.TextField(max_length=500)
    skillsfour = models.CharField(max_length=200)
    skill_descriptionfour = models.TextField(max_length=500)
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    experience_description = models.TextField(max_length=500)
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    course_duration = models.CharField(max_length=50)
    education_description = models.TextField(max_length=500)
    certification_name = models.CharField(max_length=100)
    issuing_institution = models.CharField(max_length=100)
    certification_year = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






