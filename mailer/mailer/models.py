from django.db import models


class Subscriber(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='Name of subscriber'
    )
    email = models.EmailField(
        verbose_name='Email of subscriber'
    )
    birthday = models.DateField(
        verbose_name='birthday',
        null=True,
        blank=False
    )

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)
