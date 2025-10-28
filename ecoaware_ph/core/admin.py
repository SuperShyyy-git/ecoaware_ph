from django.contrib import admin
from django.utils.html import format_html
from .models import Tag, Category

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """Tag Admin"""
    
    list_display = ['name', 'slug', 'usage_count', 'created_at']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
 
    ordering = ['name']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'slug', 'description')
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def usage_count(self, obj):
        # Count how many articles use this tag
        count = obj.article_set.count()
        return format_html(
            '<span style="background-color: #3b82f6; color: white; padding: 2px 8px; '
            'border-radius: 12px; font-size: 11px;">{}</span>',
            count
        )
    usage_count.short_description = 'Usage'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category Admin"""
    
    list_display = [
        'name',
        'parent',
        'color_preview',
        'icon_preview',
        'order',
        'is_active',
        'created_at'
    ]
    
    list_filter = ['is_active', 'parent']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['order', 'is_active']
    ordering = ['order', 'name']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'description', 'parent')
        }),
        ('Appearance', {
            'fields': ('icon', 'color', 'order')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def color_preview(self, obj):
        return format_html(
            '<div style="width: 50px; height: 25px; background-color: {}; '
            'border: 1px solid #ccc; border-radius: 4px;"></div>',
            obj.color
        )
    color_preview.short_description = 'Color'
    
    def icon_preview(self, obj):
        if obj.icon:
            return format_html(
                '<i class="{}" style="font-size: 20px;"></i>',
                obj.icon
            )
        return '-'
    icon_preview.short_description = 'Icon'
