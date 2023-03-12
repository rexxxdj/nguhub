from django import forms
from .models import Employee


class EmployeeCreateForm(forms.ModelForm):
    comment = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'rows':'5',
                                                            'class': 'form-control', 
                                                            'type': 'text', 
                                                            'name': 'comment',
                                                            'style': 'border: 1px solid #2b3553;'}))
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeCreateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['rank'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'rank'})
        self.fields['firstname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'firstname'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'lastname'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'surname'})
        self.fields['position'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'position'})
        self.fields['officialPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'officialPhone'})
        self.fields['personalPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'personalPhone'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})


class EmployeeUpdateForm(forms.ModelForm):
    comment = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'rows':'5',
                                                            'class': 'form-control', 
                                                            'type': 'text', 
                                                            'name': 'comment',
                                                            'style': 'border: 1px solid #2b3553;'}))
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeUpdateForm, self).__init__(*args, **kwargs)
        self.fields['category'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'category'})
        self.fields['rank'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'rank'})
        self.fields['firstname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'firstname'})
        self.fields['lastname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'lastname'})
        self.fields['surname'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'surname'})
        self.fields['position'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'position'})
        self.fields['officialPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'officialPhone'})
        self.fields['personalPhone'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'personalPhone'})
        self.fields['photo'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'photo'})