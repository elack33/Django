from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )

    chair = models.ForeignKey('Faculty')

    def __unicode__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    room = models.CharField(
        max_length=255,
    )

    depart = models.ForeignKey('Department')

    def __unicode__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(
        max_length=255,
        null=False, blank=False,
        help_text='The first middle and last name of the student',
    )
    student_id = models.PositiveIntegerField(
        unique=True,
        null=False,
        blank=False,
    )
    address = models.CharField(
        max_length=255,
    )

    email = models.EmailField()

    teaching_assitant = models.BooleanField(
        default=False,
        )

    department = models.ForeignKey('Department')

    courses = models.ManyToManyField('Course')

    def __unicode__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    students = models.ManyToManyField('Student')
    teacher = models.ForeignKey(
        Faculty,
        null=False,
        blank=False,
        default='1'
    )

    def __unicode__(self):
        return self.name