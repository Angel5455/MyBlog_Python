from django.db import models

#Ckeditor
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    imagen = models.ImageField(verbose_name='Imagen', upload_to='blog')
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    descripcion = models.TextField(verbose_name="Descripcion")
    contenido = RichTextField(verbose_name="Contenido")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    fecha_act = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualizacion")

    class Meta: 
        verbose_name = "Publicacion",
        verbose_name_plural = "Publicaciones"
        ordering = ['-fecha_creacion'] 


    def __str__(self):
        return self.titulo
