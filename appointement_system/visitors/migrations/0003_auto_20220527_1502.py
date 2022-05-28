# Generated by Django 2.2.5 on 2022-05-27 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0002_auto_20220527_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitors',
            old_name='Name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='visitors',
            name='Status',
        ),
        migrations.AddField(
            model_name='visitors',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
