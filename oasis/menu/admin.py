from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Sections)
admin.site.register(Positions)
admin.site.register(Orders)
#admin.site.register(InfoOrder)
admin.site.register(Booking)
admin.site.register(BookFeedback)