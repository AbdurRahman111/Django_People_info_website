# Generated by Django 3.0.7 on 2021-05-26 11:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_information',
            name='Adding_Time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 26, 17, 29, 4, 367779)),
        ),
    ]
