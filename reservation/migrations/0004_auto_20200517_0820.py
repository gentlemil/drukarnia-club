# Generated by Django 2.2.10 on 2020-05-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20200517_0817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='catering',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='faktura',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
