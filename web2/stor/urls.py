from django.urls import path
from .views import UserView

urlpatterns = [
    path('<int:user_id>/', UserView.as_view()),
    #path('user/<int:user_id>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),
]