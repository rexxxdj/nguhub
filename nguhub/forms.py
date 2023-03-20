import datetime
from django import forms
from django.contrib.auth.models import User
from employees.models import Category as employeeLocation
from equipment.models import Category as equipmentCategory, Status as equipmentStatus
from departmentEquipment.models import Category as departmentEquipmentCategory, Status as departmentEquipmentStatus
from .models import Location, CurrentLocation


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


class DepartmentEquipmentCategoryCreateForm(forms.ModelForm):
    class Meta:
        model = departmentEquipmentCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DepartmentEquipmentCategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class DepartmentEquipmentCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = departmentEquipmentCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DepartmentEquipmentCategoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class DepartmentEquipmentStatusCreateForm(forms.ModelForm):
    class Meta:
        model = departmentEquipmentStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DepartmentEquipmentStatusCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class DepartmentEquipmentStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = departmentEquipmentStatus
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(DepartmentEquipmentStatusUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class OtherLocationCreateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OtherLocationCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})


class OtherLocationUpdateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OtherLocationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})


class OtherCurrentLocationCreateForm(forms.ModelForm):
    class Meta:
        model = CurrentLocation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OtherCurrentLocationCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})


class OtherCurrentLocationUpdateForm(forms.ModelForm):
    class Meta:
        model = CurrentLocation
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(OtherCurrentLocationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})