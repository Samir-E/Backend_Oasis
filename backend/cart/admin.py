from django.contrib import admin
from .models import *
from menu.models import Positions

# Register your models here.
# admin.site.register(Orders)
# admin.site.register(InfoOrder)
admin.site.register(Cart)
admin.site.register(CartItem)
