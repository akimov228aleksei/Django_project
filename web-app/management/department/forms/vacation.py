"""
The module describes the form that will
be displayed when adding a new vacation.
"""

from django.forms import ModelForm, Select, DateInput
from department.models.vacation import Vacation


class VacationForm(ModelForm):
    """
    The class inherits from ModelForm and creates
    fields of type equal to the fields of the model
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date1'].input_formats = ['%d %m %Y']
        self.fields['date2'].input_formats = ['%d %m %Y']

    class Meta:
        model = Vacation
        fields = ['name_vacation', 'date1', 'date2']

        widgets = {
            "name_vacation": Select(attrs={
                'class': 'form-control',
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
