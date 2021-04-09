# Generated by Django 3.0.5 on 2021-04-09 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_auto_20210328_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], default='Cardiologist', max_length=50),
        ),
        migrations.AddField(
            model_name='patient',
            name='symptoms',
            field=models.CharField(default='fever', max_length=100),
        ),
    ]
