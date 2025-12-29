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
    


#create product model with fields produ_name,price and quantity,totalprice
