from django.db import models

# Create your models here.
class Publicacion(models.Model): #Tabla que contiene campo llamado texto python manage.py makemigrations publicaciones
    texto = models.TextField()

    def __str__(self):
        return self.texto[:50]
