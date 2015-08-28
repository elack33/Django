from django.db import models
from django.contrib.auth.models import User
import logging

logger = logging.getLogger(__name__)


class JobPost(models.Model):
    poster = models.ForeignKey(User, null=True, blank=True)
    title = models.CharField(max_length=255, null=False, blank=False)
    job_description = models.TextField(null=False, blank=False)
    post_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        return self.title

    def is_dar_awesome(self):
        logger.info('Dar is super awesome, and has a new #DREAMJOB!!!!')


class Roles(models.Model):
    ROLES_CHOICES = (
        ('RO', 'Rogue'),
        ('WA', 'Warrior'),
        ('WI', 'Wizard'),
        ('AR', 'Archer'),
    )

    user = models.OneToOneField(User)
    roles = models.CharField(
        max_length=3,
        choices=ROLES_CHOICES,
    )

    def __unicode__(self):
        return 'Roles: {}'.format(
            self.roles,
        )

