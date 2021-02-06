from django.shortcuts import render,redirect
from datetime import datetime
from .models import Department
from .forms import DepartmentForm
from django.views.generic import DetailView, UpdateView, DeleteView

def department_home(request):

    department = Department.objects.all()
    time = datetime.now().date()


    data = {
        'time': time,
        'department': department,
    }

    return render(request, 'department/department.html', data)


class DepartmentUpdateView(UpdateView):

    model = Department
    template_name = 'department/department_add.html'
    form_class = DepartmentForm


class DepartmentDeleteView(DeleteView):

    model = Department
    template_name = 'department/department_delete.html'
    success_url = '/'


def add(request):
    error = ''

    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Ошибка"

    form = DepartmentForm()

    time = datetime.now().date()

    data = {
        'form': form,
        'error': error,
        'time': time,
    }
    return render(request,'department/department_add.html', data)
