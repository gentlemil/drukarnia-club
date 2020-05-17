from django.db import models
from django.urls import reverse

class TypeOfProduct(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False,
        verbose_name='Nazwa kategorii',
        help_text='',
    )

    amount = models.CharField(
        max_length=15,
        blank= False, null=False,
        default="",
        verbose_name='Ilosc',
        help_text='In ml',
    )

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False,
        unique=True,
        verbose_name='Nazwa produktu',
        help_text='',
    )

    prize = models.CharField(
        blank= False, null=False,
        verbose_name='Cena jednostkowa',
        help_text='In zl',
        max_length=10,
    )

    types = models.ForeignKey(
        TypeOfProduct,
        null=False, default='',
        verbose_name='Rodzaj produktu',
        on_delete=models.CASCADE, 
        )

    description = models.CharField(
        max_length=150,
        blank= False, null=False,
        unique=False, default='',
        verbose_name='Opis produktu',
        help_text='Opis Produktu',
        )

    def __str__(self):
        return self.name


