from django.contrib import admin
from .models import Menu, Kind

class MenuAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'kind',
        'prize',

    ]
    list_filter = [
        'name',
        'kind',

    ]
    search_fields = ('name', 'kind',)
    # date_hierarchy = pass
    # ordering = [ pass ]

class KindAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'amount'
    ]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Kind, KindAdmin)