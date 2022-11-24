from django.db import models

# Create your models here.
class Project(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")

    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creacion")
    fecha_act = models.DateTimeField(auto_now=True, verbose_name = "Fecha Actualizacion")

    class Meta: 
        verbose_name = "Proyecto",
        verbose_name_plural = "Proyectos"
        ordering = ['-fecha_creacion'] 


    def __str__(self):
        return self.titulo

