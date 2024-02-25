from django.db import models

# Create your models here.

class Employyes(models.Model):
    name=models.CharField(max_length=50)
    checkIn=models.DateTimeField(auto_now_add=True)
    checkOut=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

class Diabetes(models.Model):
    glocos=models.FloatField(max_length=10)
    bmi=models.FloatField(max_length=10)
    prusser=models.FloatField(max_length=10)
    
    def __str__(self):
        return self.glocos
    

class Clothes(models.Model):
    name=models.CharField(max_length=50)
    price=models.FloatField(max_length=10)
    description=models.TextField()
    
    
    def __str__(self):
        return self.name
    