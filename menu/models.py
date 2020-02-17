from django.db import models
from django.urls import reverse

class Kind(models.Model):
    name = models.CharField(max_length=100)

    amount = models.PositiveIntegerField(
        blank= False, null=False,
        verbose_name='Amount of liquor',
        help_text='In ml',
    )

    def __str__(self):
        return self.name

class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False, default='',
        unique=True,
        verbose_name='Name',
        help_text='',
    )
    
    kind = models.ForeignKey(Kind, on_delete=models.PROTECT)

    prize = models.PositiveIntegerField(
        blank= False, null=False,
        verbose_name='Prize for one portion',
        help_text='In zl',
    )

    def __str__(self):
        return self.name

