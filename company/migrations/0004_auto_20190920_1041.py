# Generated by Django 2.2.5 on 2019-09-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20190920_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='phone_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]