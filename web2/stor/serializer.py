from rest_framework import serializers
from .models import User, Products, ProductSchedule
from datetime import datetime, timedelta
import pytz

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

class ProductsCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','name', 'description', 'active', 'productType', 'price', 'user_id']
        read_only_fields = ['id']
        
    def create(self, validated_data):
         user_id = validated_data.pop('user_id')
         user = User.objects.get(id=user_id)
         product = Products.objects.create(user=user, **validated_data) 
         create_schedule(product=product)
    

def create_schedule(product):
 
    timezone = pytz.timezone('America/Sao_Paulo')  # UTC-3
    for i in range(7):  # Para cada dia da semana
        for j in range(24):  # Para cada hora do dia
            initial_time = timezone.localize(datetime(1899, 12, 30, j, 0, 0))
            final_time = timezone.localize(datetime(1899, 12, 30, j, 59, 0))
            schedule = ProductSchedule(
                weekDay=i,
                initialTime=initial_time,
                finalTime=final_time,
                product=product
            )
            schedule.save() 

