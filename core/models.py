from django.db import models
import uuid


class PdfJob(models.Model):
    """
    Abstract base model for PDF processing jobs with multiple files
    """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pulse_studio_response = models.JSONField(default=dict, help_text="Response data from Pulse Studio API", blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('completed', 'Completed'),
            ('failed', 'Failed')
        ],
        default='pending'
    )

    class Meta:
        ordering = ['-created_at']
        
    def process_pdf_files(self):
        pass


class PdfFile(models.Model):
    """
    Model to store individual PDF files associated with a job
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(PdfJob, on_delete=models.CASCADE, related_name='pdf_files')
    file = models.FileField(upload_to='pdfs/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    pulse_data = models.JSONField(default=dict, help_text="Data from Pulse Studio API", blank=True, null=True)
    
    class Meta:
        ordering = ['created_at']
        
        
    def get_data_from_pulse_studio(self):
        pass


    