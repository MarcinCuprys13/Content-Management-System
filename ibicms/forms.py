from django import forms
from .models import ProfileNewsletter

class ProfileNewsletterForm(forms.ModelForm):
    class Meta:
        model = ProfileNewsletter
        fields = [
            'title', 'name', 'promo_text',
            'project_text',
            'head_color', 'body_color', 'footer_color',
            'phone', 'email',
            'user_photo', 'website_photo'
        ]
        widgets = {
            'head_color': forms.TextInput(attrs={'type': 'color'}),
            'body_color': forms.TextInput(attrs={'type': 'color'}),
            'footer_color': forms.TextInput(attrs={'type': 'color'}),
        }
