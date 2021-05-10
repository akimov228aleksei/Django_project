"""Module containing application logic"""

import logging
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, TemplateView, View
from department.forms.department import DepartmentForm
from department.models.department import Department
from department.DAO import DepartmentDAO


logger = logging.getLogger(__name__)


class DepartmentHome(View):
    """Class for rendering the home page of departments"""

    template_name = 'department/department.html'

    def get(self, request):

        logger.info("Database query executed")
        department = DepartmentDAO.get_list()

        return render(request, self.template_name, {'department': department})


class DepartmentAdd(View):
    """Class for adding a department"""

    form_class = DepartmentForm
    template_name = 'department/department_add.html'

    def get(self, request):

        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            logger.info("Save form")
            return redirect('home')

        return render(request, self.template_name, {'form': form})


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
