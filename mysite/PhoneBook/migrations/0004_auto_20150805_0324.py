# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneBook', '0003_auto_20150805_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zip',
            name='zip',
            field=models.CharField(unique=True, max_length=12),
        ),
    ]
