from django.urls import path

from .views import *

urlpatterns = [
    path(r'', RetrieveDestroyCartView.as_view(), name='retrieve_destroy_cart'),
    path(r'add/', AddItemToCartView.as_view(), name='add_cart_item'),
    path(r'delete/', RemoteItemFromCartView.as_view(), name='remove_cart_item'),
    path(r'total/', CartTotalPriceView.as_view(), name='total_cart_price')
]


