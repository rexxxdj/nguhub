import datetime
from django import forms
from django.contrib.auth.models import User
from .models import Location, Placement

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


class LocationCreateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LocationCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['address'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})


class LocationUpdateForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(LocationUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['address'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'address'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})


class PlacementCreateForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PlacementCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['location'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})


class PlacementUpdateForm(forms.ModelForm):
    class Meta:
        model = Placement
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PlacementUpdateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'name'})
        self.fields['location'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'address'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control ', 'type': 'text', 'name': 'notes'})
