# Generated by Django 2.2.10 on 2020-02-27 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0009_auto_20200227_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeofproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.Product'),
        ),
    ]
