"""
The module describes the form that will
be displayed when adding a new vacation.
"""

from department.models.vacation import Vacation
from django.forms import ModelForm, TextInput, DateInput


class VacationForm(ModelForm):
    """
    The class inherits from ModelForm and creates
    fields of type equal to the fields of the model
    """

    class Meta:
        model = Vacation
        fields = ['name', 'date1', 'date2']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name for employee... '
            }),
            "date1": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a date of start...'
            }),
            "date2": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a date of end...'
            }),
        }
