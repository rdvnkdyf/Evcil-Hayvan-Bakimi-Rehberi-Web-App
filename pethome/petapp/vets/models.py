from django.db import models

# Create your models here.

class Vets(models.Model):
    number=models.DecimalField(max_digits=3,decimal_places=0,unique=True)
    name=models.CharField(max_length=100,unique=False)
    surname=models.CharField(max_length=120)
    department=models.CharField(max_length=80)
    description=models.TextField()
    clinic_address=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')
    
    
