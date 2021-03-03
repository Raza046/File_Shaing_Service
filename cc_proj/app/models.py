from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.



class Userprofile(models.Model):
    users = models.ForeignKey(User,on_delete=models.CASCADE)
    imgs = models.FileField(upload_to="static")
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

class Post(models.Model):

    MyUser = models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    Title = models.TextField()
    Description = models.TextField()
    Files = models.FileField(upload_to="static")

