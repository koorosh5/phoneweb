from ..models import Phone,PhoneSearch
from django import forms

class phoneform(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'

class SearchForm(forms.Form):
    brand = forms.ChoiceField(choices=[
        ('', 'Select a brand'),
        ('Samsung', 'Samsung'),
        ('Apple', 'Apple'),
        ('Google', 'Google'),
    ])
class SearchForm2(forms.ModelForm):
    class Meta:
        model = PhoneSearch
        fields = ('brand_name', 'brand_nationality', 'country_of_manufacture','flag')
        widgets = {
            'brand_name': forms.Select(),
            'brand_nationality': forms.Select(),
            'country_of_manufacture': forms.Select(),
            'flag': forms.CheckboxInput()
        }