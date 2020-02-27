from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False, default='',
        unique=True,
        verbose_name='Name',
        help_text='',
    )
    
    amount = models.CharField(
        max_length=8,
        blank= False, null=False,
        verbose_name='Amount of liquor',
        help_text='In ml',
    )

    prize = models.CharField(
        blank= False, null=False,
        verbose_name='Prize for one portion',
        help_text='In zl',
        max_length=10,
    )

    def __str__(self):
        return  "%s %s %s" % (
            self.name,
            self.amount,
            self.prize,
        )

class TypeOfProduct(models.Model):
    name = models.CharField(
        max_length=100,
        blank= False, null=False, default='',
        verbose_name='Type of Product',
        help_text='',
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return "%s (%s)" % (
            self.name,
            self.product,
        )
