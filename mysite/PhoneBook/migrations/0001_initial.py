# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('first_name', models.CharField(unique=True, max_length=255)),
                ('last_name', models.CharField(unique=True, max_length=255)),
                ('home_phone', models.CharField(max_length=12, unique=True, null=True, blank=True)),
                ('cell_phone', models.CharField(max_length=12, unique=True, null=True, blank=True)),
                ('address1', models.CharField(unique=True, max_length=255)),
                ('address2', models.CharField(max_length=255, unique=True, null=True, blank=True)),
                ('city', models.ForeignKey(to='PhoneBook.City')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Zip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zip', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='state',
            field=models.ForeignKey(to='PhoneBook.State'),
        ),
        migrations.AddField(
            model_name='entry',
            name='zip',
            field=models.ForeignKey(to='PhoneBook.Zip'),
        ),
    ]
