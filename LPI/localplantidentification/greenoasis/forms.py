from django import forms
from .models import Image, Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['username', 'email', 'message']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'padding: 8px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'padding: 8px;'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'style': 'padding: 8px;'}),
        }

class ImageForm(forms.ModelForm):
    
    class Meta:
        model = Image
        fields = ['title', 'description', 'tags', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'padding: 8px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'padding: 8px;'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'style': 'padding: 8px;'}),
            
        }