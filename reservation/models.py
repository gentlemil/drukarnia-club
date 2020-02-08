#WSTEPNY MODEL MOJEJ STRONY REZERWACYJNEJ
#DO OBEJRZENIA, PRZEMYSLENIA, POPRAWIENIA


from django.db import models
from django.utils import timezone
from django.urls import reverse

class Bar(models.Model):
    name = models.CharField(max_length=100)
    limit = models.PositiveIntegerField()

    class Meta:
        pass

    def __str__(self):
        return self.name

#
  #   
    # 'bar2' = 'sala balowa z lozami'
    # 'bar3' = 'sala biesiadna, koncertowa'
    # 'bar4' = 'gorny bar'
  #
#  

class Reservation(models.Model):

    # YESNO_CHOICES = (
    #     ('Y', 'Tak'),
    #     ('N', 'Nie')
    # )

    STATUS_CHOICES = (
            ('draft', 'wstepna'),
            ('confirmed', 'potwierdzona'),
            ('rejected', 'odrzucona')
        )
    
    name = models.CharField(max_length=200)

    email = models.EmailField(
        max_length=200,
        )
    phone = models.CharField(max_length=20)

    term_of_reservation = models.DateTimeField(default=timezone.now)

    bar = models.ForeignKey(Bar, on_delete=models.PROTECT)

    nr_of_people = models.PositiveIntegerField(default=1)

    catering = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )

    faktura = models.BooleanField(
        blank=False,
        null=False,
        default=False
    ) 

    additional_information = models.TextField(max_length=500)

    created = models.DateTimeField(auto_now_add=timezone.now)

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
    )

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reservation-details', args=[self.pk])

