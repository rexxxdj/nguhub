from django import forms
from .models import Equipment

class EquipmentForm(forms.ModelForm):
    operationDate =forms.DateField(
        widget=forms.DateInput(
                format=('%Y-%m-%d'), 
                attrs={'class': 'form-control', 'type': 'date', 'name': 'operationDate'}))
            
    class Meta:
        model = Equipment
        fields = ('category'
                , 'name'
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
            )
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
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
        }