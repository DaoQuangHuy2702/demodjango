from django import forms
from .models import bookModel

class bookForm(forms.ModelForm):
    class Meta:
        model = bookModel
        fields = ('title', 'barcode', 'coverType', 'price', 'discount', 'image', 'description',)