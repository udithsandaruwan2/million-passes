# Generated by Django 5.0.6 on 2024-06-17 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_remove_ticket_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 'Available'), (2, 'Assigned')], default=1),
        ),
    ]
