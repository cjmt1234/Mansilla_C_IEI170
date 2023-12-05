from django.db import models

# Create your models here.
class Reservas(models.Model):
    ID = models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=80)
    telefono= models.CharField(max_length=12)             
    fechaReserva = models.DateField()
    hora = models.TimeField()
    cantidad=models.IntegerField()
    correo=models.CharField(max_length=200)
    estado = models.CharField(max_length=60)
    observación = models.CharField(max_length=1000, blank=True, null=True)
