from .models import Employee
from django.forms import ModelForm, TextInput, DateInput

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name','dep','salary','position','date']

        widgets = {
            "name": TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Enter a name for employee... '
                                }),
            "dep": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a name for the department... '
            }),
            "salary": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary... '
            }),
            "position": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter position... '
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a date...'
            }),
        }
