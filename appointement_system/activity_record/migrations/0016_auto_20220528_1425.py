# Generated by Django 2.2.5 on 2022-05-28 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0015_auto_20220528_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 14, 25, 41, 63821, tzinfo=utc)),
        ),
    ]