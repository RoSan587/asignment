# Generated by Django 2.2.5 on 2022-05-31 05:24

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0010_auto_20220531_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workdays',
            name='workday_from',
        ),
        migrations.RemoveField(
            model_name='workdays',
            name='workday_to',
        ),
        migrations.AddField(
            model_name='workdays',
            name='workdays',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Sunday', 'Sunday'), ('Mondays', 'Mondays'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Sunday', max_length=10),
        ),
    ]