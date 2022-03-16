from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Услуги'
        verbose_name = 'Услуга'
        ordering = ['id']

    def __str__(self):
        return self.title
