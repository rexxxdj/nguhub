from django import forms
from .models import Element

class ElementForm(forms.ModelForm):
    operationDate =forms.DateField(
        widget=forms.DateInput(
                format=('%Y-%m-%d'), 
                attrs={'class': 'form-control', 'type': 'date', 'name': 'operationDate'}))
    class Meta:
        model = Element
        fields = ('category'
                , 'name'
                , 'value'
                , 'serialNumber'
                #, 'inventoryNumber'
                , 'photo'
                , 'location'
                , 'status'
                , 'responsible'
                , 'responsible_reason'
                , 'fixed'
                , 'fixed_reason'
                , 'employee'
                , 'employee_reason'
                , 'equipment'
            )
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'serialNumber': forms.TextInput(attrs={'class': 'form-control'}),
            #'inventoryNumber': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'responsible': forms.Select(attrs={'class': 'form-control'}),
            'responsible_reason': forms.TextInput(attrs={'class': 'form-control'}),
            'fixed': forms.Select(attrs={'class': 'form-control'}),
            'fixed_reason': forms.TextInput(attrs={'class': 'form-control'}),
            'employee': forms.Select(attrs={'class': 'form-control'}),
            'employee_reason': forms.TextInput(attrs={'class': 'form-control'}),
            'equipment': forms.Select(attrs={'class': 'form-control'}),
        }