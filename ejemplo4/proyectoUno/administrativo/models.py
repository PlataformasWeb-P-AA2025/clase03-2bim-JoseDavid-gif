from django.db import models

# Create your models here.
class Pais(models.Model):
    # nombre
    nombre = models.CharField(max_length=30)
    # capital
    capital = models.CharField(max_length=30)
    # número de provincias
    num_provincias = models.IntegerField()
    # número de habitantes
    num_habitantes = models.IntegerField()
    
    def __str__(self):
    return f"{self.nombre} - Capital: {self.capital} - Provincias: {self.num_provincias} - Habitantes: {self.num_habitantes}"



class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return "%s %s %s" % (self.nombre,
                self.apellido,
                self.cedula)

class NumeroTelefonico(models.Model):
    telefono = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.telefono, self.tipo)
