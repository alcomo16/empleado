from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField

from applications.departamento.models import Departamento
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    
    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad 

class Empleado(models.Model):
    """Model para tabla empleado"""

    JOB_CHOICES = (
        ('0','CONTADOR'),
        ('1','ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3','OTRO'),
    )
    # contador
    # administrador
    # economista
    # otro
    first_name = models.CharField("Nombre", max_length=60)
    last_name = models.CharField("Apellidos", max_length=60)
    full_name = models.CharField('Nombres completos', max_length=120, blank=True)
    job = models.CharField("Trabajo", max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Muchos empleados'
    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name + '-' + self.job 
    