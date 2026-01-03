from django.db import models
import uuid

# Create your models here.
class OrderDetails(models.Model):
    useremail=models.EmailField(unique=True)
    orderid=models.CharField(max_length=100,unique=True)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    mode=models.CharField(max_length=50)
    status=models.CharField(max_length=80)
    dateandtime=models.DateTimeField(auto_now_add=True)
    currency=models.CharField(default="INR",max_length=50)
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    
class MovieBooking(models.Model):
    moviename=models.CharField(max_length=100)
    showtime=models.CharField(max_length=100)
    screenname=models.CharField(max_length=100)
    dateandtime=models.DateTimeField(auto_now_add=True)
    transaction_id=models.UUIDField(default=uuid.uuid4,editable=False,unique=True)
    
class BookDetails(models.Model):
    Book_Name = models.CharField(max_length=150)
    Book_Author = models.CharField(max_length=150)
    Book_Price = models.IntegerField()
    Book_Type = models.CharField(max_length=30)
    
    
# {"useremail","orderid","amount","mode","status",""}


#useremail
#orderid
#payble amount
#mode
#status
#dateandtime
#currency

# uuid1-->generates a random num based on time and mac
# uuid4--->generates a random by combination of digits and characters
# uuid5--->generates a randomm num with comb of username and spl characters