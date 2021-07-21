from .views import product_list, product_create, product_delete
from django.urls import path

urlpatterns = [
   path('product_create', product_create, name='product_create'),
   path('list/', product_list, name='product_list'),
   path('list/<int:pk>/delete', product_delete, name='product_delete'),

]
