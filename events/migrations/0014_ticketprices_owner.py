# Generated by Django 5.0.6 on 2024-06-11 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_ticketprices_amount_alter_ticketprices_name'),
        ('users', '0008_remove_profile_social_github_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketprices',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
