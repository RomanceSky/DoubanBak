# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Usersname', models.CharField(unique=True, max_length=60, verbose_name='\u7528\u6237\u540d')),
                ('Usersemail', models.CharField(max_length=60, verbose_name='\u7528\u6237\u90ae\u7bb1')),
            ],
        ),
    ]
