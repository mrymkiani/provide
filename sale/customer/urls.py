from django.urls import path
from customer.views import create_customer , sale


urlpatterns = [
    path("create-customer", create_customer),
    path("sale/<str:prod_id>", sale),
]