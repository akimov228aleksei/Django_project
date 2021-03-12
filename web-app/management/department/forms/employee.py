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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].input_formats = ['%d.%m.%Y']

    class Meta:
        model = Employee
        fields = ['name', 'dep', 'salary', 'position', 'date']

        widgets = {
            "name": TextInput(attrs={
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
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter position... '
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter date (dd mm yyyy)... '
            })
        }
