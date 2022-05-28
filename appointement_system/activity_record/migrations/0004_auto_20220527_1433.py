# Generated by Django 2.2.5 on 2022-05-27 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity_record', '0003_activity_visitorid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='Status',
            field=models.CharField(choices=[('A', 'active'), ('I', 'inactive')], default='active', max_length=50),
        ),
        migrations.AlterField(
            model_name='activity',
            name='Type',
            field=models.CharField(choices=[('L', 'Leave'), ('ap', 'appointmnet'), ('b', 'break')], default='appointmnet', max_length=50),
        ),
    ]
