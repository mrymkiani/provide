from django.urls import path
from provider.views import create_Product , create_provider , show_products , show_provider


urlpatterns = [
    path("create-product/<str:porov_id>", create_Product),
    path("create-provider", create_provider),
    path("show-products", show_products),
    path("show-provider", show_provider),
]