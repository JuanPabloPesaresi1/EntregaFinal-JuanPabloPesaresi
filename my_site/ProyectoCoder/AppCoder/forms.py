from pyexpat import model
from dataclasses import field, fields
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .models import Avatar

class formularioPeliculas(ModelForm):
    class Meta :
        model = Peliculas
        fields = '__all__'
        

class contactoFormulario(forms.Form):
    
    nombreCompleto=forms.CharField(max_length=30)
    dni=forms.IntegerField()
    profesion=forms.CharField(max_length=30)
    cv=forms.FileField(required=False)
    
class peliculasFormulario(forms.Form):
    
    nombrePelicula=forms.CharField(max_length=40)
    genero=forms.CharField(max_length=15)
    anioDeLanzamiento=forms.IntegerField()
    descripcion=forms.CharField(max_length=250)
    
class tiendaFormulario(forms.Form):
    
    productos=forms.CharField(max_length=30)
    precio=forms.IntegerField()
        
class UserRegisterForm(UserCreationForm):
    
    username = forms.CharField(label="Nombre de usuario",max_length=20, required=False)
    first_name = forms.CharField(label="Nombre Completo")
    last_name = forms.CharField(label="Apellido . . .")
    email = forms.EmailField(label="Correo Electronico")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput, required=False) # la contraseña no se vea
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput, required=False)
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email', 'password1', 'password2']
        
        # help_texts = {k:"" for k in fields}
    
class UserEditForm(forms.Form):
    
    username = forms.CharField(label="Nombre de usuario",max_length=20, required=False)
    email = forms.EmailField(label="Correo electronico")
    first_name = forms.CharField(label="Nombre Completo")
    last_name = forms.CharField(label="Apellido . . .")
    imagen=forms.ImageField(label="Foto . . . .  . ",required=False)

    class Meta:
        model = User
        fields = ['username','email', 'first_name', 'last_name', 'imagen']
        
        # help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):

    imagen = forms.ImageField(label="Imagen", required=False)

    class Meta:
        model = Avatar
        fields = ['imagen']
        
        
class CreateMensajeFrom(forms.Form):
    
    destinatario = forms.EmailField(label='Usuario', required=True, widget=forms.Select(choices=[('', 'Seleccione un destinatario')] + [(user.email, user.email) for user in User.objects.all()]))
    
    mensaje= forms.CharField(label="Escribi tu mensaje aca",required=True, widget=forms.Textarea)