from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class UserView():
    def get(self, request):
        users = User.objects.all()
        serializer = Userserializer(users, many=true)
        return Response(serializer.data, satus=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  satus=status.HTTP_200_OK)



def lista_usuarios(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': User})


