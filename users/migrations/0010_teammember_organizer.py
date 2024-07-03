# Generated by Django 5.0.6 on 2024-07-02 14:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_teammember'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='organizer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
