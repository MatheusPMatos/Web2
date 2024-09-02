from django.urls import path
from .views import UserView, UserByIdView, ProductView,ProductByIdView

urlpatterns = [
    path('', UserView.as_view()),
    path('<int:user_id>/', UserByIdView.as_view()),
    path('product/', ProductView.as_view()),
    path('product/<int:prod_id>', ProductByIdView.as_view()),


]