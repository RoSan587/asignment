# Generated by Django 2.2.5 on 2022-05-30 18:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0045_auto_20220530_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 30, 18, 3, 55, 45251, tzinfo=utc)),
        ),
    ]