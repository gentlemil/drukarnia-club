from django.contrib import admin
from .models import TypeOfProduct, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'prize',

    ]

class TypeOfProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'amount',
    ]
    list_filter = [
        'name',
        'amount',
    ]
    search_fields = ('name',)
    # date_hierarchy = pass
    # ordering = [ pass ]




admin.site.register(TypeOfProduct, TypeOfProductAdmin)
admin.site.register(Product, ProductAdmin)