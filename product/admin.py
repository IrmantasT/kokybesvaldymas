from django.contrib import admin
from .models import ErrorCodesForProduct, Line, ProductsToRepair


admin.site.register(ErrorCodesForProduct)
admin.site.register(Line)
admin.site.register(ProductsToRepair)


