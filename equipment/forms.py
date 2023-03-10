from django import forms
from .models import Equipment


class EquipmentCreateForm(forms.ModelForm):
    operationDate = forms.DateField(required=False, 
                                    widget=forms.DateInput(format=('%Y-%m-%d'), 
                                        attrs={'class': 'form-control', 
                                                'type': 'date', 
                                                'name': 'operationDate'}))
    comment = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'rows':'5',
                                                            'class': 'form-control', 
                                                            'type': 'text', 
                                                            'name': 'comment',
                                                            'style': 'border: 1px solid #2b3553;'}))
    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'unit'})
        self.fields['value'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'value'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'cost'})
        self.fields['serialNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'serialNumber'})
        self.fields['internalNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'internalNumber'})
        self.fields['inventoryNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'inventoryNumber'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})
        self.fields['location'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'location'})
        self.fields['currentLocation'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'currentLocation'})
        self.fields['status'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'status'})
        self.fields['responsible'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible'})
        self.fields['responsible_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible_reason'})
        self.fields['fixed'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed'})
        self.fields['fixed_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed_reason'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee'})
        self.fields['employee_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee_reason'})


class EquipmentUpdateForm(forms.ModelForm):
    operationDate = forms.DateField(required=False, 
                                    widget=forms.DateInput(format=('%Y-%m-%d'), 
                                        attrs={'class': 'form-control', 
                                                'type': 'date', 
                                                'name': 'operationDate'}))
    comment = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'rows':'5',
                                                            'class': 'form-control', 
                                                            'type': 'text', 
                                                            'name': 'comment',
                                                            'style': 'border: 1px solid #2b3553;'}))
    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['unit'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'unit'})
        self.fields['value'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'value'})
        self.fields['cost'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'cost'})
        self.fields['serialNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'serialNumber'})
        self.fields['internalNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'internalNumber'})
        self.fields['inventoryNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'inventoryNumber'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})
        self.fields['location'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'location'})
        self.fields['currentLocation'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'currentLocation'})
        self.fields['status'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'status'})
        self.fields['responsible'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible'})
        self.fields['responsible_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible_reason'})
        self.fields['fixed'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed'})
        self.fields['fixed_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed_reason'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee'})
        self.fields['employee_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee_reason'})