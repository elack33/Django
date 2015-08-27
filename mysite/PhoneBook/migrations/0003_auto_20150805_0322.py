# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneBook', '0002_auto_20150805_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zip',
            name='name',
        ),
        migrations.AddField(
            model_name='zip',
            name='zip',
            field=models.CharField(default=b'00000', unique=True, max_length=12),
        ),
    ]
