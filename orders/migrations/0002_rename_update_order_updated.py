# Generated by Django 3.2.6 on 2021-09-09 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='update',
            new_name='updated',
        ),
    ]
