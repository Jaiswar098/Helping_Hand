from django.urls import re_path ,path
from .views import index,about,contact,viewproduct

urlpatterns =  [
    path(' ', index, name = 'home'),
    path('aboutus/',about, name='aboutus'),
    path('contact/', contact, name='contact'),
# path('products/', viewproduct, name='view_product'),
]