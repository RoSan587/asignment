# Generated by Django 2.2.5 on 2022-05-28 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0008_auto_20220528_0946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='Comment',
            new_name='comment',
        ),
    ]