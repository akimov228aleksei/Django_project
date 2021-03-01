from department.models.vacation import Vacation
from django.forms import ModelForm, TextInput, DateInput

class VacationForm(ModelForm):
    class Meta:
        model = Vacation
        fields = ['name','date1','date2']

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
