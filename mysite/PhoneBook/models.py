from django.db import models

# Create your models here.
# Phone book that keeps track of all the contact information for everyone that lives on your street


class Entry(models.Model):
    def __unicode__(self):
        return self.nickname

    nickname = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )

    first_name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )

    home_phone = models.CharField(
        max_length=12,
        unique=True,
        null=True,
        blank=True,
    )

    cell_phone = models.CharField(
        max_length=12,
        unique=True,
        null=True,
        blank=True,
    )

    address1 = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )

    address2 = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )

    city = models.ForeignKey('City')

    state = models.ForeignKey('State')

    zip = models.ForeignKey('Zip')


class City(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(
        max_length=255,
        unique=True,
    )


class State(models.Model):
    def __unicode__(self):
        return self.name

    name = models.CharField(
        max_length=255,
        unique=True,
    )


class Zip(models.Model):
    def __unicode__(self):
        return self.zip

    zip = models.CharField(
        max_length=12,
        unique=True,
    )
