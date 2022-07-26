from django.db import models

# Create your models here.
class Cliente(models.Model):
    identificacion = models.CharField(max_length=10)
    correo = models.EmailField()

    def __str__(self):
        return "%s - %s" % (
            self.identificacion,
            self.correo)

class MarcaMedidor(models.Model):
    nombre = models.CharField(max_length=30)
    origen = models.CharField(max_length=10)

    def __str__(self):
        return "%s - %s" % (
            self.nombre,
            self.origen)

class Medidor(models.Model):
    marca = models.ForeignKey(MarcaMedidor, on_delete=models.CASCADE,
            related_name="marcas")
    costoMedidor = models.DecimalField(max_digits=10, decimal_places=2)
    origen = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,
            related_name="clientes")
    direccion = models.CharField(max_length=40)     
    parroquia = models.CharField(max_length=30)

    def __str__(self):
        return "%f - %s - %s - %s" % (
            self.costoMedidor,
            self.origen,
            self.direccion,
            self.parroquia)