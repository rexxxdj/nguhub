from django import forms
from .models import Equipment


class EquipmentCreateForm(forms.ModelForm):
    operationDate = forms.DateField(required=False, 
                                    widget=forms.DateInput(format=('%Y-%m-%d'), 
                                        attrs={'class': 'form-control', 
                                                'type': 'date', 
                                                'name': 'operationDate'}))
    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentCreateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['serialNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'serialNumber'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})
        self.fields['location'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'location'})
        self.fields['status'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'status'})
        self.fields['responsible'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible'})
        self.fields['responsible_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible_reason'})
        self.fields['fixed'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed'})
        self.fields['fixed_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed_reason'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee'})
        self.fields['employee_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee_reason'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'comment'})


class EquipmentUpdateForm(forms.ModelForm):
    operationDate = forms.DateField(required=False, 
                                    widget=forms.DateInput(format=('%Y-%m-%d'), 
                                        attrs={'class': 'form-control', 
                                                'type': 'date', 
                                                'name': 'operationDate'}))
    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['serialNumber'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'serialNumber'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})
        self.fields['location'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'location'})
        self.fields['status'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'status'})
        self.fields['responsible'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible'})
        self.fields['responsible_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'responsible_reason'})
        self.fields['fixed'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed'})
        self.fields['fixed_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'fixed_reason'})
        self.fields['employee'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee'})
        self.fields['employee_reason'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'employee_reason'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'comment'})