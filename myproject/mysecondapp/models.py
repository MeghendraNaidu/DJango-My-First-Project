from django.db import models
import uuid

# Create your models here.
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