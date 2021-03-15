"""Module containing application logic"""

from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from department.forms.department import DepartmentForm
from department.models.department import Department



def department_home(request):
    """Function to display the home page"""

    time = datetime.now().date()
    department = Department.objects.all()

    data = {
        'time': time,
        'department': department,

    }

    return render(request, 'department/department.html', data)


def add(request):
    """Function to add a new entry"""

    error = ''

    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        error = "Ошибка валидации"

    form = DepartmentForm()

    time = datetime.now().date()

    data = {
        'time': time,
        'form': form,
        'error': error,

    }
    return render(request, 'department/department_add.html', data)


class DepartmentUpdateView(UpdateView):
    """Class for editing content"""

    model = Department
    template_name = 'department/department_add.html'
    form_class = DepartmentForm


class DepartmentDeleteView(DeleteView):
    """Class for removing content"""

    model = Department
    template_name = 'department/department_delete.html'
    success_url = '/'
