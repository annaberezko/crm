# Generated by Django 4.0.4 on 2022-07-06 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0011_clients_temp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='temp',
        ),
    ]