# campaigns/admin.py

from django.contrib import admin
from .models import Campaign

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    """Campaign Admin"""
    
    list_display = ['title', 'start_date', 'end_date', 'is_active', 'created_at']
    list_filter = ['is_active', 'start_date', 'end_date']
    search_fields = ['title', 'description']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Campaign Information', {
            'fields': ('title', 'description', 'image')
        }),
        ('Schedule', {
            'fields': ('start_date', 'end_date', 'is_active')
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
