# Generated by Django 3.1.5 on 2021-05-01 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_remove_doctor_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patadmit',
            name='roomcharges',
        ),
        migrations.AlterField(
            model_name='patadmit',
            name='dischargeDate',
            field=models.DateField(default=models.DateField()),
        ),
    ]
