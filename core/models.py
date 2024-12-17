from django.db import models
from django.core.validators import MinValueValidator


class Aircraft(models.Model):
    '''Модель самолета.'''
    aircraft_code = models.CharField(
        primary_key=True,
        max_length=3,
        null=False,
        verbose_name='Код самолета, IATA'
    )
    model = models.TextField(
        null=False,
        verbose_name='Модель самолета'
    )
    range = models.IntegerField(
        validators=[
            MinValueValidator(1)
        ],
        null=False,
        verbose_name='Максимальная дальность полета,км'
    )

    class Meta:
        ordering = ['aircraft_code']
        verbose_name = 'Самолёт'
        verbose_name_plural = 'Самолёты'
        default_related_name = 'aircrafts'

    def __str__(self):
        return f'{self.aircraft_code}'


class Seat(models.Model):
    '''Модель мест самолета.'''
    CLASS_CHOICES = (
        ('economy', 'Economy'),
        ('comfort', 'Comfort'),
        ('buisness', 'Buisness'),
    )
    aircraft_code = models.ForeignKey(
        'Aircraft',
        verbose_name='Код самолета, IATA',
        on_delete=models.CASCADE,
        to_field='aircraft_code',
    )
    seat_no = models.CharField(
        max_length=4,
        null=False,
    )
    fare_conditions = models.CharField(
        max_length=10,
        null=False,
        choices=CLASS_CHOICES
    )

    class Meta:
        ordering = ['aircraft_code']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        default_related_name = 'seats'

    def __str__(self):
        return f'{self.aircraft_code} {self.seat_no} {self.fare_conditions}'

