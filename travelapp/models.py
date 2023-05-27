from django.db import models
from django.contrib.auth.models import User
from datetime import datetime



class Register_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=10)
    age = models.CharField(max_length=2)
    add = models.TextField(max_length=250,null=True,blank=True)
    pin = models.CharField(max_length=6)
  
    def __str__(self):
        return str(self.user.username)
    


class PackageDetails(models.Model):
    pname=models.CharField(max_length=20,primary_key=True)
    amount=models.IntegerField()
    images=models.ImageField(upload_to='travelimages/',blank=True)

    def __str__(self):
        return str(self.pname)

class Places(models.Model):
    place=models.CharField(max_length=200,primary_key=True)
    img=models.ImageField(upload_to='travelimages/',blank=True)
      
    def __str__(self):
        return str(self.place)
class Book(models.Model):
    user=models.ForeignKey(Register_table, on_delete=models.CASCADE, related_name='bookings')
    package=models.ForeignKey(PackageDetails,on_delete=models.CASCADE)
    checkIN=models.DateField(null=True,blank=True)
    checkOut=models.DateField(null=True,blank=True)
    adult=models.IntegerField(null=True,blank=True)
    kid=models.IntegerField(null=True,blank=True)
    women=models.IntegerField(null=True,blank=True)
    men=models.IntegerField(null=True,blank=True)
    confirm=models.BooleanField(default=False)
    def _str_(self):
        return f"Booking for {self.user} at {self.package} on {self.date}"
  
class Feedback(models.Model):
    user=models.ForeignKey(Register_table,on_delete=models.CASCADE)
    suggestion=models.CharField(max_length=500)

class Payment(models.Model):
    payment_id=models.IntegerField()
    user=models.ForeignKey(Register_table,on_delete=models.CASCADE)
    amount=models.CharField(max_length=25)


class Rating(models.Model):
     package = models.ForeignKey(PackageDetails, on_delete=models.CASCADE, related_name='ratings')
     user = models.ForeignKey(Register_table, on_delete=models.CASCADE)
     review=models.CharField(max_length=300)
class Blog(models.Model):
    topic=models.ForeignKey(PackageDetails,on_delete=models.CASCADE,null=True,blank=True)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to='travelimages/')