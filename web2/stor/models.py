from django.db import models
from enum import IntEnum

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
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    productType = models.IntegerField()
    

class ProductType(IntEnum):
    Quadra = 1
    Societ = 2
    Tenis = 3
    Volei = 4
    Voleiareia =5
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
class ProductSchuedule(models.Model):
    
    WeekDay = models.IntegerField()
    InitialTime = models.TimeField()
    FinalTime = models.TimeField()
    Product = models.ForeignKey(Products, on_delete=models.CASCADE)
    Type = models.IntegerField(choices=ProductType.choices(), default=ProductType.Quadra)
    

    
class Rent(models.Model):
    
    RentTime = models.TimeField()
    User = models.ForeignKey(User)
    ProductSchuedule = models.ForeignKey(ProductSchuedule, on_delete=models.CASCADE)


class PaymentMethod(IntEnum):
    
    Money = 1
    Pix = 2
    CreditCard = 3
    DebitCard = 4
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

 

class Payment(models.Model):
    
    Time = models.TimeField()
    method = models.CharField(choices=PaymentMethod.choices())
    Rest= models.ForeignKey(Rent, on_delete=models.CASCADE)
    
    
