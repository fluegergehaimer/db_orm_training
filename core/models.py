from django.db import models
from django.core.validators import MinValueValidator


class Aircraft(models.Model):
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
        ordering = (models.F('model').asc(nulls_last=True),)
        verbose_name = 'Самолёт'
        verbose_name_plural = 'Самолёты'
        default_related_name = 'aircrafts'

    def __str__(self):
        return f'{self.aircraft_code} {self.model} {self.range}'