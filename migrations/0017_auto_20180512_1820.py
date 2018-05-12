# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-12 08:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('NearBeach', '0016_list_of_quote_stages_quote_closed'),
    ]

    operations = [
        migrations.CreateModel(
            name='email_contact',
            fields=[
                ('email_contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_contact_change_user', to=settings.AUTH_USER_MODEL)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.customers')),
            ],
            options={
                'db_table': 'email_contact',
            },
        ),
        migrations.CreateModel(
            name='email_content',
            fields=[
                ('email_content_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_subject', models.CharField(max_length=255)),
                ('email_content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.CharField(choices=[('TRUE', 'TRUE'), ('FALSE', 'FALSE')], default='FALSE', max_length=5)),
                ('change_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_content_change_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'email_content',
            },
        ),
        migrations.AddField(
            model_name='email_contact',
            name='email_content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.email_content'),
        ),
        migrations.AddField(
            model_name='email_contact',
            name='organisations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NearBeach.organisations'),
        ),
    ]
