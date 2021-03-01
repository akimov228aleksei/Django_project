from django.forms import ModelForm, TextInput, Select, DateInput
from department.models.employee import Employee



class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'dep', 'salary', 'position', 'date']
        widgets = {
            "name": TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Enter a name for employee... '
                                }),
            "dep": Select(attrs={
                'class': 'form-control',
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
