from django import forms
from .models import Element


class ElementCreateForm(forms.ModelForm):
    operationDate = forms.DateField(required=False, 
                                    widget=forms.DateInput(format=('%Y-%m-%d'), 
                                        attrs={'class': 'form-control', 
                                                'type': 'date', 
                                                'name': 'operationDate'}))
    class Meta:
        model = Element
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ElementCreateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['value'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'value'})
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
        self.fields['equipment'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'equipment'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'comment'})


class ElementUpdateForm(forms.ModelForm):
    operationDate = forms.DateField(required=False, 
                                    widget=forms.DateInput(format=('%Y-%m-%d'), 
                                        attrs={'class': 'form-control', 
                                                'type': 'date', 
                                                'name': 'operationDate'}))
    class Meta:
        model = Element
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ElementUpdateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['value'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'value'})
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
        self.fields['equipment'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'equipment'})
        self.fields['comment'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'comment'})