"""Module containing application logic"""

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, TemplateView, View
from department.forms.department import DepartmentForm
from department.models.department import Department


class DepartmentHome(TemplateView):
    template_name = 'department/department.html'

    def get_context_data(self, **kwargs):
        context = super(DepartmentHome, self).get_context_data(**kwargs)
        context['department'] = Department.objects.all()
        return context


class DepartmentAdd(View):

    form_class = DepartmentForm
    template_name = 'department/department_add.html'

    def get(self, request):
        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        error = "Error validation"

        return render(request, self.template_name, {'form': form, 'error': error})


# def add(request):
#    """Function to add a new entry"""
#
#   error = ''
#
#   if request.method == "POST":
#      form = DepartmentForm(request.POST)
#     if form.is_valid():
#        form.save()
#       return redirect('home')
#  error = "Ошибка валидации"
#
#   form = DepartmentForm()
#
#   data = {
#      'form': form,
#     'error': error,
# }
#
#   return render(request, 'department/department_add.html', data)


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
