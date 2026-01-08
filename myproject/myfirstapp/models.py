from django.db import models

# Create your models here.
class userProfile(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    city=models.CharField(max_length=100)
    
class Employee(models.Model):
    emp_name=models.CharField(max_length=150)
    emp_salary=models.IntegerField()
    emp_email=models.EmailField(unique=True)
    
class SignUp(models.Model):
    User_Name = models.CharField(max_length=150, unique=True)
    User_Email = models.EmailField(unique=True)
    User_Password = models.CharField(max_length=12, unique=True)
    


#create product model with fields produ_name,price and quantity,totalprice
