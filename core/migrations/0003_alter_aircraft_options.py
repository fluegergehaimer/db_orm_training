# Generated by Django 5.1.4 on 2024-12-15 19:16

import django.db.models.expressions
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_aircraft_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aircraft',
            options={'default_related_name': 'aircrafts', 'ordering': (django.db.models.expressions.F.asc,), 'verbose_name': 'Самолёт', 'verbose_name_plural': 'Самолёты'},
        ),
    ]