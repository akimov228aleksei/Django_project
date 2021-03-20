"""Module containing application logic"""

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, TemplateView, View
from department.models.employee import Employee
from department.forms.employee import EmployeeForm


class EmployeeHome(TemplateView):

    template_name = 'employee/employee.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeHome, self).get_context_data(**kwargs)
        context['employee'] = Employee.objects.all()
        return context


class EmployeeAdd(View):

    form_class = EmployeeForm
    template_name = 'employee/employee_add.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_home')
        error = "Error validation"

        return render(request, self.template_name, {'form': form, 'error': error})


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
