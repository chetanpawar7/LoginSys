from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class NewUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    dob = models.DateField(max_length=8,null=True,blank=True)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=8)


    def __str__(self):
        return self.first_name + " " + self.last_name

    

