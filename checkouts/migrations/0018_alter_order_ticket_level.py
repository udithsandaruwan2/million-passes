# Generated by Django 5.0.6 on 2024-06-19 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkouts', '0017_order_verify_id_alter_order_email_and_more'),
        ('events', '0030_ticketlevel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ticket_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.ticketlevel'),
        ),
    ]
