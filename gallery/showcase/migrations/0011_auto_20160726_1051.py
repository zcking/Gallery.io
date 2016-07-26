# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 15:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('showcase', '0010_auto_20160721_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='art/placeholder.jpg', upload_to='')),
                ('join_date', models.DateField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('bio', models.TextField(default='', max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.ArtistProfile'),
        ),
    ]