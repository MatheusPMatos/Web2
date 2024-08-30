
from django.urls import path
from .views import ProfessorView, ProfessorReadUpdateDeleteView

urlpatterns = [
    path('/', ProfessorView.as_view()),
    path('/<int:pk>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),
]