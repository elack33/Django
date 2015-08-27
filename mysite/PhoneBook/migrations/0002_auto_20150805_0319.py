# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PhoneBook', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zip',
            old_name='zip',
            new_name='name',
        ),
    ]
