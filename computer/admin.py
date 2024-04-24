from django.contrib import admin
from .models import ComputerBrand, ComputerSpecification, Computer

admin.site.register(ComputerBrand)
admin.site.register(ComputerSpecification)
admin.site.register(Computer)
