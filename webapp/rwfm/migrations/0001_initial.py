# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Objects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('obj_id', models.TextField()),
                ('admin', models.TextField()),
                ('readers', models.TextField()),
                ('writers', models.TextField()),
            ],
            options={
                'ordering': ('obj_id',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_id', models.TextField()),
                ('admin', models.TextField()),
                ('readers', models.TextField()),
                ('writers', models.TextField()),
            ],
            options={
                'ordering': ('sub_id',),
            },
            bases=(models.Model,),
        ),
    ]
