# Generated by Django 2.2.1 on 2019-06-04 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reminder',
            old_name='user',
            new_name='reminder_user',
        ),
    ]