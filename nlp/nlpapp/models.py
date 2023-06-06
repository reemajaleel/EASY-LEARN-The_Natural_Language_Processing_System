from django.db import models

# Create your models here.
class login(models.Model):
    username=models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

class user(models.Model):
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


class Complaint(models.Model):
    USERID=models.ForeignKey(user,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=500)
    date = models.CharField(max_length=50)
    reply = models.CharField(max_length=500)
    status = models.CharField(max_length=500)



