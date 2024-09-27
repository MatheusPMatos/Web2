from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


#importando modelos e serializers
from .models import Professor, Curso, Disciplina
from .serializer import ProfessorSerializer, CursoSerializer, DisciplinaSerializer, DisciplinaCreateUpdateSerializer, DisciplinaConteudoCreateUpdateSerializer

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



class CursoListCreateAPIView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DisciplinaListCreateAPIView(APIView):
    def get(self, request):
        disciplinas = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplinas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DisciplinaCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DisciplinaRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DisciplinaCreateUpdateSerializer(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            disciplina = Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            return Response({'detail': 'Disciplina não encontrada.'}, status=status.HTTP_404_NOT_FOUND)
        
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DisciplinaConteudoCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DisciplinaConteudoCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)