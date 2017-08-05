# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-05 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Name')),
                ('img', models.ImageField(upload_to='anime', verbose_name='Image')),
                ('sinopse', models.TextField(verbose_name='Sinopse')),
                ('file_size', models.CharField(max_length=50, verbose_name='File Size')),
                ('duration', models.CharField(max_length=50, verbose_name='Duration')),
                ('file_format', models.CharField(max_length=50, verbose_name='File Format')),
                ('file_audio', models.CharField(max_length=50, verbose_name='File Audio')),
                ('file_subtitles', models.CharField(max_length=50, verbose_name='File Subtitles')),
                ('url', models.URLField(unique=True, verbose_name='Link Download')),
                ('slug', models.SlugField(blank=True, max_length=140, unique=True, verbose_name='Slug')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Animes',
                'ordering': ['-created_at'],
                'verbose_name': 'Anime',
            },
        ),
    ]
