from django.shortcuts import render
from django.views.generic.edit import (
    FormView,
)
from django.views.generic import(
    ListView,
)

from .forms import NewDepartamentoForm
from applications.empleados.models import Empleado
from .models import Departamento

class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = "departamentos"


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        #import pdb; pdb.set_trace()
        print('****estamos en el form valid*****')

        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shorname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        return super().form_valid(form)
    


