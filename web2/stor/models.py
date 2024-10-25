from django.db import models
from enum import IntEnum

# Create your models here.
class UserType(IntEnum):
    Vendedor = 1
    Comprador = 2
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    cpf = models.CharField(max_length=200)
    userType = models.IntegerField(choices=UserType.choices(), default=UserType.Comprador)
    
    def __str__(self) -> str:
        return self.name


class ProductType(IntEnum):
    Quadra = 1
    Societ = 2
    Tenis = 3
    Volei = 4
    Voleiareia =5
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
    
class Products(models.Model):
    
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    productType = models.IntegerField(choices=ProductType.choices(), default=ProductType.Quadra)
    price = models.FloatField()
    
class ProductSchedule(models.Model):

    weekDay = models.IntegerField()
    initialTime = models.TimeField()
    finalTime = models.TimeField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    
class Rent(models.Model):
    
    rentTime = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    productSchuedule = models.ForeignKey(ProductSchedule, on_delete=models.CASCADE)
    isPaid = models.BooleanField(default=False)



class PaymentMethod(IntEnum):
    
    Money = 1
    Pix = 2
    CreditCard = 3
    DebitCard = 4
    
    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

 

class Payment(models.Model):
    time = models.TimeField()
    method = models.IntegerField(choices=PaymentMethod.choices())
    rest= models.ForeignKey(Rent, on_delete=models.CASCADE)
    
    
