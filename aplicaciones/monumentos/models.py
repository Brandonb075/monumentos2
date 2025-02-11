from django.db import models

# Create your models here.

class Encargado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    correo = models.EmailField(unique=True)
    
    def __str__(self):
        return self.nombre

class Monumento(models.Model):
    nombre = models.CharField(max_length=150)
    ubicacion = models.CharField(max_length=255)
    descripcion = models.TextField()
    fecha_construccion = models.DateField()
    foto=models.FileField(upload_to='monumento', null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Materiales(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    cantidad_disponible = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nombre

class Proyecto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin_estimada = models.DateField()
    monumento = models.ForeignKey(Monumento, on_delete=models.CASCADE)
    encargado = models.ForeignKey(Encargado, on_delete=models.SET_NULL, null=True)
    materiales = models.ManyToManyField(Materiales)
    foto=models.FileField(upload_to='proyectpo', null=True, blank=True)
    
    def __str__(self):
        return self.nombre
