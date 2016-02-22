# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='postcategory',
            field=models.CharField(default='python', choices=[('python', 'python'), ('django', 'django'), ('frontend', 'frontend'), ('more', 'more')], max_length=10),
        ),
    ]
