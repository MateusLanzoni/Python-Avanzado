from django.db import models

class Propietario(models.Model):
    nombre   = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email    = models.EmailField()

    def __str__(self):
        return f"{self.nombre} ({self.telefono})"


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
        return f"{self.nombre} — {self.especie}"
