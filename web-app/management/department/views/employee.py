"""Module containing application logic"""

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from department.models.employee import Employee
from department.forms.employee import EmployeeForm


def employee_home(request):
    """Function to display the home page"""

    employee = Employee.objects.all()

    data = {
        'employee': employee,
    }

    return render(request, 'employee/employee.html', data)


def employee_add(request):
    """Function to add a new entry"""

    error = ''
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_home')
        error = "Data entry error"

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'employee/employee_add.html', data)


class EmployeeUpdateView(UpdateView):
    """Class for editing content"""

    model = Employee
    template_name = 'employee/employee_add.html'
    form_class = EmployeeForm


class EmployeeDeleteView(DeleteView):
    """Class for removing content"""

    model = Employee
    template_name = 'employee/employee_delete.html'
    success_url = '/employee'
