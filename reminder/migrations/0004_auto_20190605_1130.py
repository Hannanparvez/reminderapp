# Generated by Django 2.2.1 on 2019-06-05 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0003_reminder_reminderstatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='reminderdescription',
            field=models.TextField(),
        ),
    ]