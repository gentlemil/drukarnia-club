# Generated by Django 2.2.10 on 2020-05-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20200516_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='catering',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='faktura',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
