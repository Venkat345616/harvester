# Generated by Django 5.0.1 on 2024-02-29 04:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvesterapp', '0008_remove_farmers_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmers',
            name='disel',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
