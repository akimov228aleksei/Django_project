from .models import Department
from django.forms import ModelForm, TextInput

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']

        widgets = {
            "name": TextInput(attrs={
                               'class': 'form-control',
                               'placeholder': 'Enter a name for the department... '
                                }),
        }
