# Generated by Django 2.2.5 on 2022-05-30 17:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0042_auto_20220530_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 17, 59, 12, 670835, tzinfo=utc)),
        ),
    ]