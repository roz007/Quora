# Generated by Django 2.1.1 on 2018-09-01 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questans', '0003_auto_20180902_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questions',
            old_name='que',
            new_name='question',
        ),
    ]
