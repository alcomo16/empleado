from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)

#models
from .models import Empleado

#Formularios
from .forms import EmpleadoForm
# Create your views here.

class InicioView(TemplateView):
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'empleado/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    #model = Empleado
    context_object_name = 'empleados'
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            full_name__icontains = palabra_clave
        )
        return lista


class ListaEmpleadosAdmin(ListView):
    template_name = 'empleado/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    

class ListByAreaEmpleado(ListView):
    template_name = 'empleado/list_by_area.html'
    context_object_name = 'empleados'
    """queryset = Empleado.objects.filter(
        departamento__shor_name = 'Contabilidad'
    )"""

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter(
        departamento__shor_name = area
        )
        return lista


class ListByJobEmpleado(ListView):
    template_name = 'empleado/list_by_job.html'
    def get_queryset(self):
        empleo = self.kwargs['job']
        lista = Empleado.objects.filter(
            job = empleo
        )
        print(empleo)
        return lista
    

class ListEmpleadosByKword(ListView):
    #lista empleado por palabra clave
    template_name = 'empleado/by_kword.html'
    context_object_name = 'empleado'

    def get_queryset(self):
        print('**************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'empleado/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(
            id = 1
        )
        return empleado.habilidades.all()
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "empleado/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Empleado del mes"
        return context

class SuccessView(TemplateView):
    template_name = "empleado/success.html"


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "empleado/add.html"
    #fields = ['first_name','last_name','job']
    """fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'image'
    ]"""
    form_class= EmpleadoForm
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def form_valid(self, form):
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "empleado/update.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('empleado_app:empleados_admin')

    def post(self, request, *args, **kwargs):
        print('*******Metodo POST*******')
        print('**************')
        print(request.POST)
        print(request.POST['last_name'])
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
        print('*******Form Valid*******')
        print('**************')
        return super(EmpleadoUpdateView, self).form_valid(form)
    
class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "empleado/delete.html"
    success_url = reverse_lazy('empleado_app:empleados_admin')
