# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_delete_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='postcategory',
            field=models.CharField(max_length=10, default='python', choices=[('python', 'python'), ('django', 'django'), ('frontend', 'frontend')]),
        ),
    ]
