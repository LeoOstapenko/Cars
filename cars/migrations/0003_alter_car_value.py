# Generated by Django 5.1.2 on 2024-11-07 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_brand_alter_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='value',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
