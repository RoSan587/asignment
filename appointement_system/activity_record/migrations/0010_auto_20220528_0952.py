# Generated by Django 2.2.5 on 2022-05-28 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0009_auto_20220528_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='visitorid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='visitors.Visitors'),
        ),
    ]
