from django.db import models


class City(models.Model):
    name = models.CharField('Город', max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Address(models.Model):
    name = models.CharField('Улица', max_length=255)
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        verbose_name='Город'
    )
    number = models.CharField('Номер', max_length=20)

    def __str__(self):
        return f'город {self.city}, улица {self.name}, дом {self.number}'

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'


class Shop(models.Model):
    name = models.CharField('Магазин', max_length=255)
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        verbose_name='Адрес'
    )
    opening_time = models.TimeField('Время открытия')
    closing_time = models.TimeField('Время закрытия')

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
