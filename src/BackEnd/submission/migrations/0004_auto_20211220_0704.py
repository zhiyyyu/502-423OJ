# Generated by Django 3.1.5 on 2021-12-20 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_auto_20211219_1349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'ordering': ['submit_time']},
        ),
    ]