from django.forms import ModelForm
from django import forms

from .models import Employees, Color, Department

#we want to change only the senior and color
class EmployeeForm(ModelForm):

    class Meta:
        model = Employees
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'readonly': True, 'class': 'form-control'}),
            'age' : forms.NumberInput(attrs={'readonly': True, 'class': 'form-control'}),
            'is_senior' : forms.CheckboxInput(attrs={'class':'ml-4'}),
            'favorite_color': forms.Select(attrs={'class': ''}),
        }
    
    # class Meta:
    #     model = Employees
    #     fields = '__all__'

    #     widgets = {
    #         'name': forms.TextInput(attrs={'readonly': True, 'class': 'form-control'}),
    #         'age' : forms.NumberInput(attrs={'readonly': True, 'class': 'form-control'}),
    #         'is_senior' : forms.CheckboxInput(attrs={'class':'ml-4'}),
    #         'favorite_color': forms.Select(attrs={'class': ''}),
    #         'department': forms.HiddenInput(),
    #         'id': forms.HiddenInput(),
    #     }
        # alot of redundant widgets because had problems with hidden inputs