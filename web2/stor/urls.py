from django.urls import path
from views import User

urlpatterns = [
    path('<int:user_id>/', User.as_view()),
    #path('user/<int:user_id>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),
]