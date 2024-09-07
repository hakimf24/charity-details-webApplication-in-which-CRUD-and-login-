from django.db import models
from django.contrib.auth.models import User


class Madrasadetails(models.Model):
  madrasaname = models.CharField(max_length=255)
  address = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  
 
  def __str__(self):
        return f"{self.madrasaname} - {self.address} - {self.phone}"

class Zakatdetails(models.Model):
    user_name = models.ForeignKey(User, null= True, on_delete=models.CASCADE,related_name='User_name')
    madrasa_name = models.ForeignKey(Madrasadetails, on_delete=models.CASCADE,related_name='madrasa')
    zakat_date = models.DateField() 
    zakat_amount = models.IntegerField(null = True)
    slip_no = models.IntegerField(null= True)
    