# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gifts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
            ],
            options={
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='Wedding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='gifts',
            name='wedding',
            field=models.ForeignKey(related_name='gift', blank=True, to='registry.Wedding', null=True),
        ),
    ]
