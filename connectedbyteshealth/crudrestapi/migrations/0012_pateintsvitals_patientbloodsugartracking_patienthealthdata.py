# Generated by Django 3.2.7 on 2021-10-01 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudrestapi', '0011_auto_20211001_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pateintsvitals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_vitalsdatetime', models.DateTimeField(default=datetime.datetime.now)),
                ('patient_systolic', models.IntegerField(default=0)),
                ('patient_diastolic', models.IntegerField(default=0)),
                ('patient_temperature', models.FloatField(default=None)),
                ('patient_pulse', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'patientvitals',
            },
        ),
        migrations.CreateModel(
            name='Patientbloodsugartracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_bloodsugarreadingdatetime', models.DateTimeField(default=datetime.datetime.now)),
                ('patient_bloodsugarreading', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'patientBloodSugarreading',
            },
        ),
        migrations.CreateModel(
            name='Patienthealthdata',
            fields=[
                ('id', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('patient_profession', models.CharField(default='', max_length=30)),
                ('patient_smoking', models.CharField(default='', max_length=30)),
                ('patient_drinking', models.CharField(default='', max_length=30)),
                ('patient_diet', models.CharField(default='', max_length=30)),
                ('patient_allergy', models.CharField(default='', max_length=30)),
                ('patient_chronicillness', models.CharField(default='', max_length=30)),
                ('patient_majorinjury', models.CharField(default='', max_length=30)),
                ('patient_majorsurgery', models.CharField(default='', max_length=30)),
                ('patient_regularphysicalactivity', models.CharField(default='', max_length=30)),
                ('patient_eyepower', models.CharField(default='', max_length=30)),
                ('patient_temperature', models.FloatField(default=None)),
            ],
            options={
                'db_table': 'patientshealthdata',
            },
        ),
    ]