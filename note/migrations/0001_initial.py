# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(verbose_name='created_date')),
                ('published_date', models.DateTimeField(verbose_name='published_date')),
                ('content', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]
