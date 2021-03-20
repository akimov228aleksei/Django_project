"""Module containing application logic"""

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, TemplateView, View
from department.forms.department import DepartmentForm
from department.models.department import Department


class DepartmentHome(TemplateView):
    """Class for rendering the home page of departments"""

    template_name = 'department/department.html'

    def get_context_data(self, **kwargs):

        context = super(DepartmentHome, self).get_context_data(**kwargs)
        context['department'] = Department.objects.all()
        return context


class DepartmentAdd(View):
    """Class for adding a department"""

    form_class = DepartmentForm
    template_name = 'department/department_add.html'

    def get(self, request):

        form = self.form_class()

        return render(request, self.template_name, {'form': form, 'temp': 'Hello'})

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

        error = "Error validation"

        return render(request, self.template_name, {'form': form, 'error': error})


class DepartmentUpdateView(UpdateView):
    """Class for editing content"""

    model = Department
    template_name = 'department/department_add.html'
    form_class = DepartmentForm

    def get_context_data(self, **kwargs):

        context = super(DepartmentUpdateView, self).get_context_data(**kwargs)
        context['temp'] = 'Department.objects.all()'
        return context


class DepartmentDeleteView(DeleteView):
    """Class for removing content"""

    model = Department
    template_name = 'department/department_delete.html'
    success_url = '/'
