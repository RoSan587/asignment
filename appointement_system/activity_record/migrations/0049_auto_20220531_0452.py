# Generated by Django 2.2.5 on 2022-05-31 04:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0048_auto_20220531_0329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 31, 4, 52, 43, 509858, tzinfo=utc)),
        ),
    ]
