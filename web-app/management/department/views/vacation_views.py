from django.shortcuts import render,redirect
from datetime import datetime
from ..models.vacation_models import Vacation
from ..forms.vacation_forms import VacationForm
from django.views.generic import DetailView, UpdateView, DeleteView



def vacation_home(request):

    vacation = Vacation.objects.all()
    time = datetime.now().date()
    data = {
        'time': time,
        'vacation': vacation,
    }

    return render(request, 'vacation/vacation.html', data)


def add(request):
    error = ''

    if request.method == "POST":
        form = VacationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vacation_home')
        else:
            error = "Ошибка"

    form = VacationForm()

    time = datetime.now().date()

    data = {
        'form': form,
        'error': error,
        'time': time,
    }
    return render(request,'vacation/vacation_add.html', data)

class VacationUpdateView(UpdateView):

    model = Vacation
    template_name = 'vacation/vacation_add.html'
    form_class = VacationForm


class VacationDeleteView(DeleteView):

    model = Vacation
    template_name = 'vacation/vacation_delete.html'
    success_url = '/vacation'
