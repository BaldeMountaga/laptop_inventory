# Generated by Django 4.2.7 on 2023-11-22 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptop_inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='sold',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
