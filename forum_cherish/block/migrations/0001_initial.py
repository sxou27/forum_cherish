# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 10:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='\u540d\u5b57')),
                ('desc', models.CharField(max_length=150, verbose_name='\u63cf\u8ff0')),
                ('sex', models.IntegerField(choices=[(1, '\u7537'), (2, '\u5973')], default=b'')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
            ],
            options={
                'verbose_name': '\u677f\u5757',
                'verbose_name_plural': '\u677f\u5757',
            },
        ),
    ]
