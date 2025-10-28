from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='USER')
    
    def is_admin(self):
        return self.role == 'ADMIN'
    
    def is_regular_user(self):
        return self.role == 'USER'

    # ----------------------------
    # URL properties for templates
    # ----------------------------
    @property
    def get_edit_url(self):
        return reverse('users:user_edit', args=[self.id])

    @property
    def get_delete_url(self):
        return reverse('users:delete_user', args=[self.id])

    class Meta:
        db_table = 'users'
