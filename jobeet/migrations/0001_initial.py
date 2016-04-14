# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affiliate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=255)),
                ('email', models.CharField(unique=True, max_length=255)),
                ('token', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CategoryAffiliate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('affiliate', models.ForeignKey(related_name='category_affiliates', to='jobeet.Affiliate')),
                ('category', models.ForeignKey(related_name='category_affiliates', to='jobeet.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttype', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('logo', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('how_to_apply', models.TextField()),
                ('token', models.CharField(unique=True, max_length=255)),
                ('is_public', models.NullBooleanField()),
                ('is_activated', models.NullBooleanField()),
                ('email', models.CharField(max_length=255)),
                ('expires_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(related_name='jobs', to='jobeet.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
