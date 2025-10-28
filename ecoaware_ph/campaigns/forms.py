from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = [
            'title',
            'description',
            'goal',
            'image',
            'start_date',
            'end_date',
            'is_active',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter campaign title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe your campaign'}),
            'goal': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter fundraising goal'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
