# Generated by Django 5.0.6 on 2024-06-11 23:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_ticketprice_initial_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='uuid',
            new_name='id',
        ),
    ]
