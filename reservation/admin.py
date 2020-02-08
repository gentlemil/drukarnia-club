from django.contrib import admin
from .models import Reservation, Bar

class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        'term_of_reservation',
        'name',
        'bar',
        'nr_of_people',
        'phone',
        'faktura',
        'status',
        ]
    list_filter = [
        'term_of_reservation',
        'bar',
        'status',
    ]
    search_fields = ('term_of_reservation', 'bar')
    date_hierarchy = 'term_of_reservation'
    # ordering = [ pass ]

class BarAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'limit'
    ]



admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Bar, BarAdmin)

admin.site.site_header = 'RESERVATION SITE - PROJECT'
