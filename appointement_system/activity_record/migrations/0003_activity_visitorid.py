# Generated by Django 2.2.5 on 2022-05-27 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
        ('activity_record', '0002_auto_20220526_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='visitorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='visitors.Visitors'),
        ),
    ]
