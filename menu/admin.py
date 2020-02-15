from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'kind',
        'amount',
        'prize',

        ]

    list_filter = [
        'name',
        'kind',

    ]

    search_fields = ('name', 'kind',)

    # date_hierarchy = pass

    # ordering = [ pass ]

admin.site.register(Menu, MenuAdmin)