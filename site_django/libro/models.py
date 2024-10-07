from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

# Declaramos el nuevo modelo con el nombte de Book"
class Book(models.Model):
 # Campos del modelo
 titulo = models.CharField(max_length = 200)
 descripcion = models.TextField()
 modificado = models.DateTimeField(auto_now_add = True)
def __str__(self):
 return self.titulo

class BoardsModel(models.Model):
    titulo = models.CharField(max_length = 200)
    autor = models.CharField(max_length = 200, default='Anonimo')
    descripcion = models.TextField()
    valor = models.FloatField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now = True)

    def get_valor_category(self):
        if self.valor < 1000:
            return "Baja"
        elif 1000 <= self.valor <= 2500:
            return "Media"
        else:
            return "Alta"

    class Meta:
        verbose_name = "libro"
        verbose_name_plural = "libros"
        permissions = (
            ("es_miembro_1", "Es miembro con prioridad 1"),
            ("development", "Permiso como Desarrollador"),
            ("scrum_master", "Permiso como Scrum Master"),
            ("product_owner", "Permiso como Product Owner"),
        )

    def __str__(self):
        return self.titulo