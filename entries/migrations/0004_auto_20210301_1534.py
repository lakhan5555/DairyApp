# Generated by Django 3.1.3 on 2021-03-01 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0003_auto_20210301_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='person',
            new_name='user',
        ),
    ]
