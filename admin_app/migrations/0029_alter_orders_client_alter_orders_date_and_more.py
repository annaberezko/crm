# Generated by Django 4.0.4 on 2022-07-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0028_rename_id_parent_babys_parent_alter_orders_client_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='client',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='orders',
            name='service',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]