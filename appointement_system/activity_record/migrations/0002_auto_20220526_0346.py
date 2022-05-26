# Generated by Django 2.2.5 on 2022-05-26 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='visitorID',
        ),
        migrations.AlterField(
            model_name='activity',
            name='officerID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='officer.Officer'),
        ),
    ]
