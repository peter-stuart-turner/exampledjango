from django.contrib import admin
from .models import PdfJob, PdfFile

# Register your models here.

class PdfFileInline(admin.TabularInline):
    """
    Inline admin class for PdfFile model
    """
    model = PdfFile
    readonly_fields = ('id', 'created_at')
    extra = 0  # Don't show extra empty forms

class PdfJobAdmin(admin.ModelAdmin):
    """
    Admin class for PdfJob model
    """
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_display = ('id', 'created_at', 'updated_at', 'status', 'pulse_studio_response')
    ordering = ('-created_at',)
    inlines = [PdfFileInline]  # Add the inline class here
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('id',)
        return self.readonly_fields

# Register the model with the admin site
admin.site.register(PdfJob, PdfJobAdmin)


class PdfFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'job', 'file', 'created_at')
    ordering = ('-created_at',)

admin.site.register(PdfFile, PdfFileAdmin)
