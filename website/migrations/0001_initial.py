# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import website.fields
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chantier',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=500)),
                ('niveau1', models.CharField(default=b'ARCHITE', max_length=7, choices=[(b'ARCHITE', b'Architecture'), (b'AMEURBA', b'Am\xc3\xa9nagement'), (b'DESIGN', b'Design'), (b'URBAPAY', b'Urbanisme et paysages')])),
            ],
            options={
                'verbose_name': 'Projet',
                'verbose_name_plural': 'Projets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nameField', models.CharField(max_length=255)),
                ('firstNameField', models.CharField(max_length=255)),
                ('descField', models.TextField(max_length=500)),
                ('phoneField', models.CharField(default=b'', max_length=14)),
                ('emailField', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('photo', website.fields.ThumbnailImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=250, blank=True)),
                ('afficher', models.CharField(default=b'oui', max_length=3, choices=[(b'oui', b'Afficher dans la page Home'), (b'non', b'Ne pas l afficher dans la page Home')])),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagesDe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('chantier', models.ForeignKey(blank=True, to='website.Chantier', null=True)),
                ('image', models.ForeignKey(to='website.Image', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('text', models.TextField(max_length=500)),
                ('niveau1', models.CharField(default=b'ARTICL', max_length=7, choices=[(b'EXPO', b'Exposition'), (b'PUBLI', b'Publications'), (b'ARTICL', b'Articles')])),
                ('images', models.ManyToManyField(to='website.Image', null=True, through='website.ImagesDe', blank=True)),
            ],
            options={
                'verbose_name': 'Arts et Artisanat',
                'verbose_name_plural': 'Arts et Artisanat',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('photo', website.fields.ThumbnailImageField(upload_to=b'', blank=True)),
                ('content', tinymce.models.HTMLField()),
                ('role', models.CharField(max_length=250, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagesde',
            name='media',
            field=models.ForeignKey(blank=True, to='website.Media', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chantier',
            name='images',
            field=models.ManyToManyField(to='website.Image', null=True, through='website.ImagesDe', blank=True),
            preserve_default=True,
        ),
    ]
