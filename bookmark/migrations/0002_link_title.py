# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(default=datetime.datetime(2015, 7, 20, 8, 26, 46, 219971, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
