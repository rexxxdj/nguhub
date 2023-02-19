from django import forms
from .models import Category

class EquipmentsFilterForm(forms.Form):
    categories = forms.MultipleChoiceField(choices=Category.objects.all().values_list('id', 'name'), 
                                            widget=forms.CheckboxSelectMultiple, required=False)