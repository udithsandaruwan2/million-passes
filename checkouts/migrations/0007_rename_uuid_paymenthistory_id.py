# Generated by Django 5.0.6 on 2024-06-11 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkouts', '0006_rename_id_paymenthistory_uuid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymenthistory',
            old_name='uuid',
            new_name='id',
        ),
    ]
