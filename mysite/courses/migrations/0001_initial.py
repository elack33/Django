# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('depart', models.ForeignKey(to='courses.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'The first middle and last name of the student', max_length=255)),
                ('student_id', models.PositiveIntegerField(unique=True)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('teaching_assitant', models.BooleanField(default=False)),
                ('courses', models.ManyToManyField(to='courses.Course')),
                ('department', models.ForeignKey(to='courses.Department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='chair',
            field=models.ForeignKey(to='courses.Faculty'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(to='courses.Student'),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default=b'1', to='courses.Faculty'),
        ),
    ]
