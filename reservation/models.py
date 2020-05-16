from django.db import models
from django.utils import timezone
from django.urls import reverse

class Bar(models.Model):
    name = models.CharField(max_length=100)
    limit = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Reservation(models.Model):

    STATUS_CHOICES = (
            ('draft', 'WSTĘPNA'),
            ('confirmed', 'POTWIERDZONA'),
            ('rejected', 'ODRZUCONA')
        )
    
    title = models.CharField(
        max_length=50,
        )

    name = models.CharField(max_length=200)

    email = models.EmailField(
        max_length=200,
        )
    phone = models.CharField(max_length=20)

    term_of_reservation = models.DateTimeField(default=timezone.now)

    bar = models.ForeignKey(
        Bar,
        null=False, default='',
        verbose_name='BAR',
        on_delete=models.CASCADE)

    nr_of_people = models.PositiveIntegerField(default=2)

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
        default='draft',
    )

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('reservation_details', args=[self.pk])

