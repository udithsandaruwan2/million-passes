# Generated by Django 5.0.6 on 2024-06-08 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_featured_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='date_time',
        ),
    ]
