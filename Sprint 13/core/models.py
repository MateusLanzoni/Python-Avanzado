# core/models.py
from django.db import models
import logging

logger = logging.getLogger(__name__)

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


class Medicamento(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    cantidad_disponible = models.PositiveIntegerField(default=0)
    fecha_vencimiento = models.DateField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} (Stock: {self.cantidad_disponible})"
    
    @property
    def estado_vencimiento(self):
        from datetime import date, timedelta
        hoy = date.today()
        if self.fecha_vencimiento < hoy:
            return 'vencido'
        elif self.fecha_vencimiento <= hoy + timedelta(days=30):
            return 'por_vencer'
        else:
            return 'vigente'
    
    def save(self, *args, **kwargs):
        logger.info(f"Medicamento {'actualizado' if self.pk else 'creado'}: {self.nombre}")
        super().save(*args, **kwargs)


class Veterinario(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Dr. {self.nombre}"


class Cirugia(models.Model):
    ESTADOS = [
        ('programada', 'Programada'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]
    
    fecha = models.DateTimeField()
    tipo_cirugia = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='programada')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.tipo_cirugia} - {self.mascota.nombre} ({self.fecha.strftime('%d/%m/%Y')})"
    
    def save(self, *args, **kwargs):
        logger.info(f"Cirugía {'actualizada' if self.pk else 'programada'}: {self.tipo_cirugia} para {self.mascota.nombre}")
        super().save(*args, **kwargs)


class BitacoraConsulta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE, related_name='bitacoras')
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE, null=True, blank=True)
    observaciones = models.TextField()
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    medicamentos_recetados = models.ManyToManyField(Medicamento, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    temperatura = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return f"Consulta {self.mascota.nombre} - {self.fecha.strftime('%d/%m/%Y')}"
    
    def save(self, *args, **kwargs):
        logger.info(f"Bitácora de consulta registrada para {self.mascota.nombre}")
        super().save(*args, **kwargs)
