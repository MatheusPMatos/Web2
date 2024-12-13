from django.urls import path
from .views import UserView, UserByIdView, ProductView,ProductByIdView, UserRegisterAPIView, UserProductsView

urlpatterns = [
    # path('', UserView.as_view()),
    path('<int:user_id>/', UserByIdView.as_view()),
    path('products/', ProductView.as_view()),
    path('products/<int:prod_id>', ProductByIdView.as_view()),
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('user/<int:user_id>/products/', UserProductsView.as_view(), name='user-products'),
]