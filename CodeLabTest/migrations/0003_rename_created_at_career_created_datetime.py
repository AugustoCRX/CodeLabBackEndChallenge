# Generated by Django 5.1.3 on 2024-12-06 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodeLabTest', '0002_career_delete_codelabmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='created_at',
            new_name='created_datetime',
        ),
    ]
