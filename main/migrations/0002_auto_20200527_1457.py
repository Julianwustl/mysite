# Generated by Django 3.0.6 on 2020-05-27 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turnkey',
            name='cost_station',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]