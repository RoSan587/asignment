# Generated by Django 2.2.5 on 2022-05-27 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0003_workdays'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='Status',
            field=models.CharField(choices=[('A', 'active'), ('I', 'inactive')], default='active', max_length=50),
        ),
    ]