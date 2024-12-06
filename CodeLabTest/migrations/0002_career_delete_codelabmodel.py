# Generated by Django 5.1.3 on 2024-12-06 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeLabTest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='CodeLabModel',
        ),
    ]
