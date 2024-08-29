from django.shortcuts import render , HttpResponse
from django.http.response import JsonResponse
from provider.models import Provider , Product
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_provider(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        Provider.objects.create(
            name= body['input_name'],
            phone= body['input_phone'],
        )
        return HttpResponse("new Provider created")

    
@csrf_exempt
def create_Product(request , porov_id):
    prov = Provider.objects.get(id = porov_id)
    if request.method == 'POST':
        body = json.loads(request.body)
        Provider.objects.create(
            name= body['input_name'],
            price= body['input_price'],
            Provider = prov
        )
        return HttpResponse("new product created")


def show_products(request):
    prods = Product.objects.all()
    my_prod_list = []
    for item in prods:
        pro_dictionary = {
            "name" : item.name,
            "price" : item.price,
        }
        my_prod_list.append(pro_dictionary)
    prodss = my_prod_list.dump()
    return FileResponse (prodss)


def show_provider(request):
    provs = Provider.objects.all()
    my_prov_list = []
    for item in provs:
        if item.active == True:
            prov_dictionary = {
                "name" : item.name,
                "phone" : item.price,
            }
            my_prov_list.append(prov_dictionary)
    provss = my_prov_list.dump()
    return FileResponse (provss)
# Create your views here.
