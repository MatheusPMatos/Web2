
from django.urls import path
from .views import ProfessorView, ProfessorReadUpdateDeleteView

urlpatterns = [
    path('professor/', ProfessorView.as_view()),
    path('professor/<int:pk>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),

]