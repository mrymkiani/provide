from django.shortcuts import render , HttpResponse
from django.http.response import JsonResponse
from customer.models import Customer , Sale
from provider.models import Product
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_customer(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        Customer.objects.create(
            name= body['input_name'],
            phone= body['input_phone'],
            wallet= 100
        )
        return HttpResponse("new Customer created")
    
def sale(request , prod_id):
    selected_prod = Product.objects.get(id=prod_id)
    if Customer.wallet >= selected_prod.price:
        new_sale = Sale.objects.create(
            name= Customer.name,
            phone= Customer.phone,
            product = selected_prod
        )
        
        Customer.wallet -= selected_prod.price
        Customer.wallet.save()
    else:
        return HttpResponse("error")
        return HttpResponse("new prod with name: {}".format(new_sale.name))
    
    
# Create your views here.
