# Generated by Django 5.0.4 on 2024-04-07 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applet', '0002_prize_event_coins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='signup_date',
            field=models.DateTimeField(),
        ),
    ]
