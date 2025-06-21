# core/models.py
from django.db import models

class Propietario(models.Model):
    nombre   = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email    = models.EmailField()

    def __str__(self):
        return self.nombre


class Mascota(models.Model):
    ESPECIES = [
        ("Perro", "Perro"),
        ("Gato",  "Gato"),
        ("Ave",   "Ave"),
        ("Otro",  "Otro"),
    ]
    nombre      = models.CharField(max_length=100)
    especie     = models.CharField(max_length=20, choices=ESPECIES)
    edad        = models.PositiveIntegerField()
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    fecha       = models.DateField()
    hora        = models.TimeField()
    motivo      = models.CharField(max_length=200)
    mascota     = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.fecha} {self.hora} — {self.mascota.nombre}"
