# Generated by Django 2.2.5 on 2022-05-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0012_auto_20220528_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='addedd_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
