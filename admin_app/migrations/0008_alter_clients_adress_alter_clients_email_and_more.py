# Generated by Django 4.0.4 on 2022-07-06 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0007_alter_orders_date_alter_orders_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='adress',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='info',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
    ]
