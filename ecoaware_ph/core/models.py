from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = CKEditor5Field('Description', blank=True, config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = CKEditor5Field('Description', blank=True, config_name='extends')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    color = models.CharField(max_length=7)  # e.g., #FFFFFF
    icon = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
