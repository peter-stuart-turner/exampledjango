from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PdfJob

# Create your views here.

class PdfJobListView(ListView):
    model = PdfJob
    template_name = 'core/pdf_job_list.html'
    context_object_name = 'pdf_jobs'
    ordering = ['-created_at']

class PdfJobDetailView(DetailView):
    model = PdfJob
    template_name = 'core/pdf_job_detail.html'
    context_object_name = 'pdf_job'
