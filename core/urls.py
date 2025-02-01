from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('pdf-jobs/', views.PdfJobListView.as_view(), name='pdf-job-list'),
    path('pdf-jobs/<uuid:pk>/', views.PdfJobDetailView.as_view(), name='pdf-job-detail'),
]
