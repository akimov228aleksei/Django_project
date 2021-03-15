"""
The module describes the form that will
be displayed when adding a new department.
"""

from django.forms import ModelForm, TextInput
from department.models.department import Department


class DepartmentForm(ModelForm):
    """
    The class inherits from ModelForm and creates
    fields of type equal to the fields of the model
    """

    class Meta:
        model = Department
        fields = ['name']

        widgets = {"name": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter name of department...'
        })}
