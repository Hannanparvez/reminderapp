# Generated by Django 2.2.1 on 2019-06-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reminder', '0002_auto_20190604_0906'),
    ]

    operations = [
        migrations.AddField(
            model_name='reminder',
            name='reminderstatus',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]