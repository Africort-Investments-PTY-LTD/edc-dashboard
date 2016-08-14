# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-14 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django_crypto_fields.fields.firstname_field
import django_crypto_fields.fields.lastname_field
import django_extensions.db.fields
import django_revision.revision_field
import edc_base.model.fields.hostname_modification_field
import edc_base.model.fields.userfield
import edc_base.model.fields.uuid_auto_field


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('user_created', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user created')),
                ('user_modified', edc_base.model.fields.userfield.UserField(editable=False, max_length=50, verbose_name='user modified')),
                ('hostname_created', models.CharField(default='mac2-2.local', editable=False, help_text='System field. (modified on create only)', max_length=50)),
                ('hostname_modified', edc_base.model.fields.hostname_modification_field.HostnameModificationField(editable=False, help_text='System field. (modified on every save)', max_length=50)),
                ('revision', django_revision.revision_field.RevisionField(blank=True, editable=False, help_text='System field. Git repository tag:branch:commit.', max_length=75, null=True, verbose_name='Revision')),
                ('id', edc_base.model.fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False)),
                ('subject_identifier', models.CharField(max_length=25)),
                ('first_name', django_crypto_fields.fields.firstname_field.FirstnameField(help_text=' (Encryption: RSA local)', max_length=71)),
                ('last_name', django_crypto_fields.fields.lastname_field.LastnameField(help_text=' (Encryption: RSA local)', max_length=71)),
                ('initials', models.CharField(max_length=25)),
                ('dob', models.DateField()),
            ],
        ),
    ]