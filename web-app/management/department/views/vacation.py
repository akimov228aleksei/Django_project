"""Module containing application logic"""

import logging
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, TemplateView, View
from department.models.vacation import Vacation
from department.forms.vacation import VacationForm
from department.DAO import VacationDAO


logger = logging.getLogger(__name__)


class VacationHome(View):
    """Class for rendering the home page of vacation"""

    template_name = 'vacation/vacation.html'

    def get(self, request):

        logger.info("Database query executed")
        vacation = VacationDAO.get_list()

        return render(request, self.template_name, {'vacation': vacation})


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
            logger.info("Database query executed")
            return redirect('vacation_home')

        return render(request, self.template_name, {'form': form})


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
