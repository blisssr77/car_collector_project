from django.contrib import admin
from .models import Car, Rental, Option

# Register your models here.
admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(Option)
