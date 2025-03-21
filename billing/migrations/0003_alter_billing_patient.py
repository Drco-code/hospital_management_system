# Generated by Django 5.1.7 on 2025-03-16 03:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_initial'),
        ('patients', '0003_remove_patient_medical_history'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='patients.patient', verbose_name='Patient'),
        ),
    ]
