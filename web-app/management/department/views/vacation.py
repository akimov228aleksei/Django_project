"""Module containing application logic"""

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, TemplateView, View
from department.models.vacation import Vacation
from department.forms.vacation import VacationForm


class VacationHome(TemplateView):
    """Class for rendering the home page of vacation"""

    template_name = 'vacation/vacation.html'

    def get_context_data(self, **kwargs):

        context = super(VacationHome, self).get_context_data(**kwargs)
        context['vacation'] = Vacation.objects.all()
        return context


class VacationAdd(View):
    """Class for adding vacation"""

    form_class = VacationForm
    template_name = 'vacation/vacation_add.html'

    def get(self, request):

        form = self.form_class()

        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacation_home')

        error = "Error validation "

        return render(request, self.template_name, {'form': form, 'error': error})


class VacationUpdateView(UpdateView):
    """Class for editing content"""

    model = Vacation
    template_name = 'vacation/vacation_add.html'
    form_class = VacationForm


class VacationDeleteView(DeleteView):
    """Class for removing content"""

    model = Vacation
    template_name = 'vacation/vacation_delete.html'
    success_url = '/vacation'
