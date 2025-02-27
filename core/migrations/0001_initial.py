# Generated by Django 5.1.5 on 2025-02-01 08:39

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PdfJob',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pdf_files', models.JSONField(default=list, help_text='List of PDF file paths or URLs')),
                ('pulse_studio_response', models.JSONField(default=dict, help_text='Response data from Pulse Studio API')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
