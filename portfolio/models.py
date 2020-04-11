from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título") # Campo de caracteres
    description = models.TextField(verbose_name="Descripción") # Campo de caracteres muy grande
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación") # now_add se ejecuta al INS
    updated = models.DateTimeField(auto_now=True, verbose_name="FEcha de Actualización") # now se ejecuta en el UPD

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title