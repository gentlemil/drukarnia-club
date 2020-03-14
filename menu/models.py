from django.db import models
from django.urls import reverse

class TypeOfProduct(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False,
        verbose_name='Type of Product',
        help_text='',
    )

    amount = models.CharField(
        max_length=15,
        blank= False, null=False,
        default="&mdash",
        verbose_name='Amount of liquor',
        help_text='In ml',
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False,
        unique=True,
        verbose_name='Name',
        help_text='',
    )

    prize = models.CharField(
        blank= False, null=False,
        verbose_name='Prize for one portion',
        help_text='In zl',
        max_length=10,
    )

    types = models.ForeignKey(
        TypeOfProduct,
        null=False, default='',
        verbose_name='Type of Product',
        on_delete=models.CASCADE, 
        )

    description = models.CharField(
        max_length=150,
        blank= False, null=False,
        unique=False, default='&nbsp;',
        verbose_name='Opis',
        help_text='Opis Produktu',
        )

    def __str__(self):
        return self.name


