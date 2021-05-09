"""
The module describes the form that will
be displayed when adding a new vacation.
"""

from django.forms import ModelForm, Select, DateInput
from department.models.vacation import Vacation
from django.core.exceptions import ValidationError
import logging


logger = logging.getLogger(__name__)


class VacationForm(ModelForm):
    """
    The class inherits from ModelForm and creates
    fields of type equal to the fields of the model
    """

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

    def clean_date2(self):

        date1 = self.cleaned_data["date1"]
        date2 = self.cleaned_data["date2"]

        if date2 <= date1:
            logger.info('Data has not been validated')
            raise ValidationError("End date cannot be earlier than start date")

        return date2
