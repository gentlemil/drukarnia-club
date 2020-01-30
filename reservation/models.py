#WSTEPNY MODEL MOJEJ STRONY REZERWACYJNEJ
#DO OBEJRZENIA, PRZEMYSLENIA, POPRAWIENIA


from django.db import models
from django.utils import timezone

class Reservation(models.Model):
    CHOICES = (
        ('1', 'Tak'),
        ('0', 'Nie')
    )
    
    BAR_CHOICES = (
        ('2 BAR', 'sala balowa z lozami'),
        ('3 BAR', 'sala biesiadna, koncertowa'),
        ('4 BAR', 'gorny bar'),
    )

    STATUS_CHOICES = (
            ('draft', 'wstepna'),
            ('confirmed', 'potwierdzona'),
        )
    
    name = models.CharField(max_length=200)
    slug = models.SlugField(
        max_length=200,
        unique_for_date= 'term_of_reservation',
        default='dupa',
        )
    email = models.EmailField(
        max_length=200,
        unique_for_date='term_of_reservation')
    phone = models.DecimalField(
        decimal_places=9,
        max_digits=9
        )
        # nie wiem jaki Field tutaj dac zeby ograniczyc do wpisania
        # nie mniej, nie wiecej cyfr niz 9
        
    term_of_reservation = models.DateTimeField(default=timezone.now)
    bar = models.CharField(
        max_length=10,
        choices=BAR_CHOICES,
    )
        # trzeba jeszcze stworzyc warunek, ze bar 2 i 3 jest czynny
        # tylko w piatki i soboty, chyba, ze chce sie zrobic impreze
        # zamknieta (wynajac cala sale)

    nr_of_people = models.IntegerField(default=2)
    catering = models.CharField(
        max_length=5,
        choices=CHOICES,
        default=False,
    )
    faktura = models.CharField(
        max_length=5,
        choices=CHOICES,
        default=False,
    ) 
    additional_information = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=timezone.now)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )

    # class Meta:
    #     pass

    # def __str__(self):
    #     return self.term_of_reservation

