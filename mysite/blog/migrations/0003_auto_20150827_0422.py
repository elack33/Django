# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogcomment_blog_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog_article',
            field=models.ForeignKey(to='blog.BlogArticle'),
        ),
    ]
