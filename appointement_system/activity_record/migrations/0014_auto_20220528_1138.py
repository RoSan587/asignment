# Generated by Django 2.2.5 on 2022-05-28 11:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0013_auto_20220528_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 11, 38, 0, 991049, tzinfo=utc)),
        ),
    ]