import datetime
from django import forms
from django.contrib.auth.models import User
from employees.models import Category as employeeLocation
from equipment.models import Category as equipmentCategory, Status as equipmentStatus
from elements.models import Category as elementCategory, Status as elementStatus


class SignInForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-user', 
                    'type': 'username', 
                    'name': 'username', 
                    'placeholder': 'Enter UserName...'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-user', 
                    'type': 'password', 
                    'name': 'password', 
                    'placeholder': 'Password'}))


class EmployeeLocationCreateForm(forms.ModelForm):
    class Meta:
        model = employeeLocation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeLocationCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['address'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'address'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class EmployeeLocationUpdateForm(forms.ModelForm):
    class Meta:
        model = employeeLocation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EmployeeLocationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['address'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'address'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class EquipmentCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = equipmentCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentCategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class EquipmentCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = equipmentCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentCategoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class EquipmentStatusCreateForm(forms.ModelForm):
    class Meta:
        model = equipmentStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentStatusCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class EquipmentStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = equipmentStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(EquipmentStatusUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class ElementCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = elementCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ElementCategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class ElementCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = elementCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ElementCategoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class ElementStatusCreateForm(forms.ModelForm):
    class Meta:
        model = elementStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ElementStatusCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class ElementStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = elementStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ElementStatusUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})