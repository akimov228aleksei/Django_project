from django.shortcuts import render, redirect
from datetime import datetime
from department.models.employee import Employee
from department.forms.employee import EmployeeForm
from django.views.generic import UpdateView, DeleteView



def employee_home(request):

    employee = Employee.objects.all()
    time = datetime.now().date()


    data = {
        'time': time,
        'employee': employee,
    }

    return render(request, 'employee/employee.html', data)


def employee_add(request):
    error = ''
    form = EmployeeForm()

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_home')
        else:
            error = "Ошибка"


    time = datetime.now().date()

    data = {
        'form': form,
        'error': error,
        'time': time,
    }
    return render(request, 'employee/employee_add.html', data)

class EmployeeUpdateView(UpdateView):

    model = Employee
    template_name = 'employee/employee_add.html'
    form_class = EmployeeForm


class EmployeeDeleteView(DeleteView):

    model = Employee
    template_name = 'employee/employee_delete.html'
    success_url = '/employee'
