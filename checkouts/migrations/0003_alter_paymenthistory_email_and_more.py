# Generated by Django 5.0.6 on 2024-06-11 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkouts', '0002_paymenthistory_ticket_price'),
        ('events', '0014_ticketprices_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenthistory',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='id_verification',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='ticket_price',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='events.ticketprices'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='total_amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
