# Generated by Django 5.0.6 on 2024-06-17 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0027_remove_ticket_order_id_remove_ticket_owner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.IntegerField(choices=[(1, 'Available'), (2, 'Assigned'), (3, 'Used')], default=1),
        ),
    ]
