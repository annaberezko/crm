# Generated by Django 4.0.4 on 2022-07-07 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0022_alter_babys_id_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babys',
            name='id_parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_app.clients'),
        ),
    ]