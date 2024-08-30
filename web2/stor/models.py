from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    userType = models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    
    
    
class ProductSchuedule(models.Model):
    
    WeekDay = models.IntegerField()
    InitialTime = models.TimeField()
    FinalTime = models.TimeField()
    Product = models.ForeignKey(Products)    

    
class Rent(models.Model):
    
    RentTime = models.TimeField()
    User = models.ForeignKey(User)
    ProductSchuedule = models.ForeignKey(ProductSchuedule)
    

    
    