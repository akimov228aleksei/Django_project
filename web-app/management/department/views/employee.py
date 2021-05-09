"""Module containing application logic"""

import logging
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, TemplateView, View
from department.models.employee import Employee
from department.forms.employee import EmployeeForm
from department.DAO import EmployeeDAO
from django.core.exceptions import ValidationError


logger = logging.getLogger(__name__)


class EmployeeHome(View):
    """Class for rendering the home page of employee"""

    template_name = 'employee/employee.html'

    def get(self, request):

        logger.info("Database query executed")
        employee = EmployeeDAO.get_list()

        return render(request, self.template_name, {'employee': employee})


class EmployeeAdd(View):
    """Class for adding an employee"""

    form_class = EmployeeForm
    template_name = 'employee/employee_add.html'

    def get(self, request):

        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            logger.info("Save form")
            return redirect('employee_home')


        # error = form.non_field_errors()
        # print(error)

        return render(request, self.template_name, {'form': form})


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
