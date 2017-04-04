# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-13 11:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('active', models.BooleanField(default=False, help_text='Is account activated through email')),
                ('activacion_code', models.CharField(blank=True, default='', help_text='Code used to activate account with email', max_length=60, null=True)),
                ('password_hash', models.CharField(help_text='sha512 of password + salt', max_length=60)),
            ],
        ),
    ]