# Generated by Django 5.1.5 on 2025-02-01 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_pdfjob_pdf_files_pdffile'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdffile',
            name='pulse_data',
            field=models.JSONField(blank=True, default=dict, help_text='Data from Pulse Studio API', null=True),
        ),
    ]
