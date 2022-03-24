from django import forms
from .models import bookModel

class bookForm(forms.ModelForm):
    class Meta:
        model = bookModel
        fields = ('title', 'barcode', 'coverType', 'price', 'discount', 'image', 'description',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'style': 'margin-bottom: 15px;'}),
            'barcode': forms.TextInput(attrs={'class': 'form-control', 'id': 'barcode', 'style': 'margin-bottom: 15px;'}),
            'coverType': forms.TextInput(attrs={'class': 'form-control', 'id': 'coverType', 'style': 'margin-bottom: 15px;'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'price', 'style': 'margin-bottom: 15px;'}),
            'discount': forms.NumberInput(attrs={'class': 'form-control', 'id': 'discount', 'style': 'margin-bottom: 15px;'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'image', 'style': 'margin-bottom: 15px;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description', 'rows': '5', 'style': 'margin-bottom: 30px;'}),
        }