# Generated by Django 4.0.4 on 2022-07-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0017_alter_clients_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='adress',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
    ]