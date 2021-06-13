# Generated by Django 3.0.7 on 2021-05-26 11:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=1000)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='person_information',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='uploads/Profile_image')),
                ('Full_name', models.CharField(max_length=500)),
                ('Other_name', models.CharField(max_length=500)),
                ('State_of_Origin', models.CharField(max_length=500)),
                ('Sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Progressing', max_length=100)),
                ('Spoken_languages', models.CharField(max_length=500)),
                ('Complexion', models.CharField(choices=[('Dark', 'Dark'), ('Chocolate', 'Chocolate'), ('Bleached', 'Bleached'), ('Light', 'Light')], default='Progressing', max_length=100)),
                ('Adding_Time', models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 26, 17, 28, 49, 826732))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Person Information',
            },
        ),
        migrations.CreateModel(
            name='EmailConfirmed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=500)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'User Email-Confirmed',
            },
        ),
    ]