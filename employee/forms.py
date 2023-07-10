from django import forms
from .models import Employee, ActionPost


class EmployeeCreateForm(forms.ModelForm):
    notes = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'rows':'5',
                                                            'class': 'form-control', 
                                                            'type': 'text', 
                                                            'name': 'comment',
                                                            'style': 'border: 1px solid #2b3553;'}))
    is_operator = forms.BooleanField(required=False,
                                        widget=forms.CheckboxInput())
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        self.fields['placement'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'placement'})
        self.fields['rank'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'rank'})
        self.fields['firstname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'firstname'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'lastname'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'surname'})
        self.fields['position'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'position'})
        self.fields['officialPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'officialPhone'})
        self.fields['personalPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'personalPhone'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})
        self.fields['actionPost'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'actionPost'})


class EmployeeUpdateForm(forms.ModelForm):
    notes = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'rows':'5',
                                                            'class': 'form-control', 
                                                            'type': 'text', 
                                                            'name': 'comment',
                                                            'style': 'border: 1px solid #2b3553;'}))
    is_operator = forms.BooleanField(required=False)
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
        self.fields['placement'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'placement'})
        self.fields['rank'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'rank'})
        self.fields['firstname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'firstname'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'lastname'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'surname'})
        self.fields['position'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'position'})
        self.fields['officialPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'officialPhone'})
        self.fields['personalPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'personalPhone'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})
        self.fields['actionPost'].widget.attrs.update({'class': 'form-control ', 'type': 'check-box', 'name': 'actionPost'})


class ActionPostCreateForm(forms.ModelForm):
    class Meta:
        model = ActionPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActionPostCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})


class ActionPostUpdateForm(forms.ModelForm):
    class Meta:
        model = ActionPost
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActionPostUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})