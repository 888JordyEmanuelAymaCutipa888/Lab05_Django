from django.db import models

# Create your models here.

class Domicilio(models.Model):
    ciudad = models.TextField()
    provincia = models.TextField()
    departamento = models.TextField()
