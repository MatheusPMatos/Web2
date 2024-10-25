from django.shortcuts import render
from .models import User,Products
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UserSerializer, ProductsSerializer, ProductsCreateUpdateSerializer
from rest_framework import status


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)
        return Response({"detail": "Invalid User."}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    


class UserByIdView(APIView):
    def get(self, request, user_id=None):
        if user_id is None:
            users = User.objects.all(pk=user_id)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            try:
                # Com ID, retorna um usuário específico
                user = User.objects.get(pk=user_id)
                serializer = UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            
    def delete(self, request, user_id=None):
        if user_id is None:
            return Response({"detail": "User ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(pk=user_id)
            user.delete()
            return Response({"detail": "User deleted successfully."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class ProductView(APIView):
    def get(self, request, ):
        prods = Products.objects.all()
        serializer = ProductsSerializer(prods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
            
    def post(self, request):
        serializer = ProductsCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)
        
        return Response({"detail": "INvalid product."}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request):
        serializer = ProductsCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_200_OK)
        
        return Response({"detail": "INvalid product."}, status=status.HTTP_400_BAD_REQUEST)
class ProductByIdView(APIView):
    def get(self, request, prod_id=None):
        if prod_id is None:
            return Response({"detail": "Invalid product Id."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                # Com ID, retorna um usuário específico
                prods = Products.objects.get(pk=prod_id)
                serializer = ProductsSerializer(prods)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Products.DoesNotExist:
                return Response({"detail": "Product not found."}, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, prod_id=None):
        if prod_id is None:
            return Response({"detail": "product ID is required for deletion."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            prods = Products.objects.get(pk=prod_id)
            prods.delete()
            return Response({"detail": "product deleted successfully."}, status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({"detail": "product not found."}, status=status.HTTP_404_NOT_FOUND)