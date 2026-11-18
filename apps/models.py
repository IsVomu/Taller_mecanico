from django.db import models

class TipoRepuesto(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateField()
    disponible = models.BooleanField(default=True)
    categoria = models.ForeignKey(TipoRepuesto, on_delete=models.CASCADE, related_name='repuestos')

    def __str__(self):
        return self.nombre