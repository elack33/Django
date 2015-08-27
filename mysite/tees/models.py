from django.db import models

# Create your models here.
# An application that saves information on all the styles of shirts in a t-shirt store

class Tee(models.Model):
    def __unicode__(self):
        return self.nickname

    nickname = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True,
    )