"""Module containing application logic"""

from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from department.models.vacation import Vacation
from department.forms.vacation import VacationForm


def vacation_home(request):
    """Function to display the home page"""

    vacation = Vacation.objects.all()

    data = {
        'vacation': vacation,
    }

    return render(request, 'vacation/vacation.html', data)


def vacation_add(request):
    """Function to add a new entry"""

    error = ''

    if request.method == "POST":
        form = VacationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacation_home')
        error = "Ошибка"

    form = VacationForm()

    data = {
        'error': error,
        'form': form,
    }

    return render(request, 'vacation/vacation_add.html', data)


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
