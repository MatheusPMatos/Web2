from django.urls import path
from .views import UserView, UserByIdView, ProductView,ProductByIdView

urlpatterns = [
    # path('', UserView.as_view()),
    path('<int:user_id>/', UserByIdView.as_view()),
    path('products/', ProductView.as_view()),
    path('products/<int:prod_id>', ProductByIdView.as_view()),
    path('register/', UserView.as_view(), name='user-register'),
]