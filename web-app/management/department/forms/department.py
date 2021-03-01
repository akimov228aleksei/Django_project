from department.models.department import Department
from django.forms import ModelForm, TextInput


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']

        widgets = {"name": TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Enter name of department...'
                                })}
