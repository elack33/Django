from django.db import models

# Create your models here.


class Gifts(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=8,
        null=False, blank=False
    )
    wedding = models.ForeignKey(
        'Wedding',
        related_name='gift',
        null=True, blank=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['price']


class Wedding(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
    )
    date = models.DateTimeField(
        null=False, blank=False,
    )

    def __unicode__(self):
        return self.name
