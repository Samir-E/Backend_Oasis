from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Booking

# Create your views here.
def menu(request):
    models = Booking.objects.all()
    return render(request, 'menu/layout.html', locals())

    


