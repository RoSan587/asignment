# Generated by Django 2.2.5 on 2022-05-27 03:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0002_auto_20220526_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='workdays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workdays', models.CharField(max_length=50)),
                ('OfficerID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='officer.Officer')),
            ],
        ),
    ]
