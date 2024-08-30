from django.urls import path
from .views import UserView

urlpatterns = [
    path('/', UserView.as_view()),
    #path('<int:user_id>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),
]