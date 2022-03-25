from django import forms
from .models import phoneModel

class phoneForm(forms.ModelForm):
    class Meta:
        model = phoneModel
        fields = ('name', 'code', 'price', 'discount', 'image', 'description',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'style': 'margin-bottom: 15px;'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'id': 'code', 'style': 'margin-bottom: 15px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price', 'style': 'margin-bottom: 15px;'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'discount', 'style': 'margin-bottom: 15px;'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'image', 'style': 'margin-bottom: 15px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'rows': '5', 'style': 'margin-bottom: 30px;'}),
        }