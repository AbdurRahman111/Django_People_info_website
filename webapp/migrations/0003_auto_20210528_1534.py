# Generated by Django 3.0.7 on 2021-05-28 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20210526_1729'),
    ]

    operations = [
        migrations.AddField(
            model_name='person_information',
            name='Description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person_information',
            name='Adding_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 28, 15, 34, 18, 537735)),
        ),
    ]
