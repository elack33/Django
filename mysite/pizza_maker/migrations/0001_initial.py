# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('pizza_size', models.IntegerField(default=0)),
                ('toppings', models.CharField(default=b'Cheese', max_length=1, choices=[(b'B', b'Bacon'), (b'C', b'Cheese'), (b'D', b'Dried tomatoes'), (b'E', b'Extra Cheese'), (b'G', b'Green peppers'), (b'S', b'Sausage'), (b'GC', b'Grilled Chicken')])),
                ('extra_sauce', models.BooleanField(default=True)),
            ],
        ),
    ]
