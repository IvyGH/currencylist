from django.db import models


class Cryptocurrency(models.Model):
    """ Cryptocurrency model class """
    abbreviation = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=120, unique=True)
    price = models.FloatField()
    change = models.CharField(max_length=120)

    class Meta:
        verbose_name = 'Cryptocurrency'
        verbose_name_plural = 'Cryptocurrencies'

    def __str__(self):
        return self.abbreviation


class Currency(models.Model):
    """ Currency model class """
    abbreviation = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=120, unique=True)
    price = models.FloatField()
    unit = models.IntegerField()

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'

    def __str__(self):
        return self.abbreviation
