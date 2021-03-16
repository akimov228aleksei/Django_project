"""
The module describes the form that will
be displayed when adding a new employee.
"""

from django.forms import ModelForm, TextInput, Select, DateInput, NumberInput
from department.models.employee import Employee


class EmployeeForm(ModelForm):
    """
    The class inherits from ModelForm and creates
    fields of type equal to the fields of the model
    """

    class Meta:
        model = Employee
        fields = ['name_employee', 'dep', 'salary', 'position', 'date']

        CHOICE_POSITION = (('Position_1', 'Position_1'),
                           ('Position_2', 'Position_2'),
                           ('Position_3', 'Position_3'),
                           ('Position_4', 'Position_4'))

        widgets = {
            "name_employee": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter employee name... '
            }),
            "dep": Select(attrs={
                'class': 'form-control',
            }),
            "salary": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary... '
            }),
            "position": Select(choices=CHOICE_POSITION, attrs={
                'class': 'form-control',
                'placeholder': 'Enter position... ',
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter date... '
            })
        }
