from django.shortcuts import render,redirect
from datetime import datetime
from ..models.employee_models import Employee
from ..forms.employee_forms import EmployeeForm
from django.views.generic import DetailView, UpdateView, DeleteView


def salary():
    employee = Employee.objects.all()
    new_list = ''  # Вычисление средней ЗП
    list_sum = 0  #
    k = 0  #
    for i in employee:  #
        list_sum += int(i.salary[:-1])  #
        k += 1  #

    if list_sum:
        new_list = str(round(list_sum / k)) + " $"
    else:
        new_list = '-'
    return new_list

def employee_home(request):

    employee = Employee.objects.all()
    time = datetime.now().date()

    new_list = ''                         # Вычисление средней ЗП
    list_sum = 0                         #
    k = 0                                #
    for i in employee:                   #
        list_sum += int(i.salary[:-1])   #
        k += 1                           #

    if list_sum:
        new_list = str(round(list_sum/k)) + " $"


    data = {
        'time': time,
        'employee': employee,
    }

    return render(request, 'employee/employee.html', data)


def add(request):
    error = ''

    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_home')
        else:
            error = "Ошибка"

    form = EmployeeForm()

    time = datetime.now().date()

    data = {
        'form': form,
        'error': error,
        'time': time,
    }
    return render(request,'employee/employee_add.html', data)

class EmployeeUpdateView(UpdateView):

    model = Employee
    template_name = 'employee/employee_add.html'
    form_class = EmployeeForm


class EmployeeDeleteView(DeleteView):

    model = Employee
    template_name = 'employee/employee_delete.html'
    success_url = '/employee'
