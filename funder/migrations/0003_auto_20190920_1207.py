# Generated by Django 2.2.5 on 2019-09-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funder', '0002_history_funder'),
    ]

    operations = [
        migrations.AddField(
            model_name='funder',
            name='total_help',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='funder',
            name='total_investment',
            field=models.IntegerField(default=0),
        ),
    ]