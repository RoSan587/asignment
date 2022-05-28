# Generated by Django 2.2.5 on 2022-05-28 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0016_auto_20220528_1425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='id',
        ),
        migrations.AddField(
            model_name='activity',
            name='activityid',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 28, 15, 18, 24, 174768, tzinfo=utc)),
        ),
    ]