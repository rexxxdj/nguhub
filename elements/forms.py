from django import forms
from .models import Element

class ElementForm(forms.ModelForm):
    class Meta:
        model = Element
        fields = ('category'
                , 'name'
                , 'value'
                , 'serialNumber'
                , 'photo'
                , 'status'
                , 'equipment'
            )
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'equipment': forms.Select(attrs={'class': 'form-control'}),
        }