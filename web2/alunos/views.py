from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


#importando modelos e serializers
from .models import Professor
from .serializer import ProfessorSerializer

class ProfessorView(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer = ProfessorSerializer(data=request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        professors = Professor.objects.all()
        serializer = ProfessorSerializer(professors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProfessorReadUpdateDeleteView(APIView):
    """
    View para recuperar, atualizar ou deletar um professor específico.
    """

    def get(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)

        '''
        try:
            professor = Professor.objects.get(pk=pk)
        except Professor.DoesNotExist:
            return Response({'detail': 'Professor não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        '''

        serializer = ProfessorSerializer(professor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)
        serializer = ProfessorSerializer(professor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        professor = get_object_or_404(Professor, pk=pk)
        professor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)