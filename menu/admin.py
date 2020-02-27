from django.contrib import admin
from .models import TypeOfProduct, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'amount',
        'prize',

    ]

class TypeOfProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
  
    ]
    list_filter = [
        'name',

    ]
    search_fields = ('name',)
    # date_hierarchy = pass
    # ordering = [ pass ]




admin.site.register(TypeOfProduct, TypeOfProductAdmin)
admin.site.register(Product, ProductAdmin)