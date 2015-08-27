from django.db import models


class Pizza(models.Model):

    TOPPING_CHOICES = (
        ('B', 'Bacon'),
        ('C', 'Cheese'),
        ('D', 'Dried tomatoes'),
        ('E', 'Extra Cheese'),
        ('G', 'Green peppers'),
        ('S', 'Sausage'),
        ('GC', 'Grilled Chicken'),
    )

    title = models.CharField(max_length=255, null=False, blank=False)
    pizza_size = models.IntegerField(default=0)
    toppings = models.CharField(
        max_length=1, choices=TOPPING_CHOICES, default='Cheese')
    extra_sauce = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title
