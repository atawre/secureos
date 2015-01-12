# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwfm', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Objects',
            new_name='Object',
        ),
        migrations.RenameModel(
            old_name='Subjects',
            new_name='Subject',
        ),
    ]
