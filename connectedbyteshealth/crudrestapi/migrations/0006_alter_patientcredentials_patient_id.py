# Generated by Django 3.2.7 on 2021-09-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudrestapi', '0005_auto_20210930_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientcredentials',
            name='patient_id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
