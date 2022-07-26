from distutils.command.upload import upload
import email
from email.mime import image
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User


# modelo del avatar
class Avatar(models.Model):

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatar/', blank=True, null=True)

class Contacto(models.Model):
    
    nombreCompleto=models.CharField(max_length=30)
    dni=models.IntegerField()
    profesion=models.CharField(max_length=30)
    cv=models.FileField()
    
    class Meta:
        verbose_name_plural = "Contacto"
        
    def __str__(self) -> str:
        return f"Nombre : {self.nombreCompleto} - DNI {self.dni} - Profesion {self.profesion} - CV {self.cv}"
    
class Peliculas(models.Model):
    
    nombrePelicula=models.CharField(max_length=40)
    genero=models.CharField(max_length=15)
    anioDeLanzamiento=models.IntegerField()
    descripcion=models.CharField(max_length=250)
    
    
    class Meta:
        verbose_name_plural = "Peliculas"
    
    def __str__(self) -> str:
        return f"Pelicula : {self.nombrePelicula} - Genero {self.genero} - Año de Lanzamiento {self.anioDeLanzamiento} - Descripcion {self.descripcion}"
    
class Tienda(models.Model):
    
    productos=models.CharField(max_length=30)
    precio=models.IntegerField("Precio $")
    
    class Meta:
        verbose_name_plural = "Productos"
    
    def __str__(self) -> str:
        return f"Nombre del producto : {self.productos} - Precio {self.precio}  "
    
class Mensaje(models.Model):

    remitente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='remitente')
    destinatario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinatario')

    mensaje = models.TextField(max_length=500, blank=True, null=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mensaje