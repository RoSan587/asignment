# Generated by Django 2.2.5 on 2022-05-30 17:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0038_auto_20220530_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 17, 48, 29, 128140, tzinfo=utc)),
        ),
    ]
