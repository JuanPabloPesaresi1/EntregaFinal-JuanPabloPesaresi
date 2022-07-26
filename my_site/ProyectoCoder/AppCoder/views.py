from distutils.log import info
from re import template
import re
from tkinter.messagebox import RETRY
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.template import Context, Template
from AppCoder.models import *
from django.db.models import Q
from .forms import tiendaFormulario, contactoFormulario, formularioPeliculas, peliculasFormulario
from django.forms.models import inlineformset_factory
from django.db.models import DEFERRED
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import *
import datetime
from django.views.generic.detail import DetailView
from django.contrib import messages

# Create your views here.

page_title = "Cine Ya"

base_context = {
    'page_title': page_title,
}


#Entrada, index y base

def entrada(request):
    return redirect("inicio")

def index(request):

    return render(request,"index.html")

def base(request):
    base_context.update({"active":"base"})
    
    hoy = datetime.datetime.now().strftime("%d/%m/%Y")
    
    return render(request,"base.html",{"dia_hora":hoy})

#Todo Pelicula
@login_required
def peliculas(request):    
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
            peliculas = Peliculas.objects.filter(Q(nombrePelicula__icontains=search))#.values()
            
            return render(request,"peliculas.html",{"peliculas":peliculas, "search":True, "busqueda":search})
    
    pelis=Peliculas.objects.all()
    
    ctx={"peliculas":pelis}
    
    return render(request,"peliculas.html",ctx)
@login_required
def eliminar_peliculas(request, pk):
    
    pelicula= get_object_or_404(Peliculas, id=pk)
    pelicula.delete()
    
    return redirect('peliculas')
@login_required
def modificar_peliculas(request,pk):
    
    peliculas = Peliculas.objects.get(id=pk)

    if request.method == "POST":

        formulario = peliculasFormulario(request.POST)

        if formulario.is_valid():
            
            info_peliculas = formulario.cleaned_data
            
            peliculas.nombrePelicula = info_peliculas["nombrePelicula"]
            peliculas.genero = info_peliculas["genero"]
            peliculas.anioDeLanzamiento = info_peliculas["anioDeLanzamiento"]
            peliculas.descripcion = info_peliculas["descripcion"]
            peliculas.save()

            return redirect("peliculas")

    # get
    formulario = peliculasFormulario(initial={"nombrePelicula":peliculas.nombrePelicula, "genero":peliculas.genero, "anioDeLanzamiento": peliculas.anioDeLanzamiento, "descripcion": peliculas.descripcion})
    
    return render(request,"modificar_peliculas.html",{"form":formulario})
@login_required
def formulario_peliculas(request):
    
    if request.method == "POST":
        
        formulario= peliculasFormulario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
        
            pelicula = Peliculas(nombrePelicula=info["nombrePelicula"],genero=info["genero"],anioDeLanzamiento=int(info["anioDeLanzamiento"]),descripcion=info["descripcion"])
            pelicula.save()
        
        return redirect("peliculas")
    
    else:
        formulario = peliculasFormulario()
        return render(request,"formulario_peliculas.html",{"form":formulario})
@login_required
def busqueda_pelicula(request):
    if request.method == "POST":
        
        pelis=request.POST["pelicula"]
        
        peliculasBusqueda =Peliculas.objects.filter(nombrePelicula__icontains=pelis)
        
        return render(request,"busqueda_pelicula.html",{"peliculas":peliculasBusqueda})
    
    else:
        
        peliculasBusqueda=[]
    
        return render(request,"busqueda_pelicula.html",{"peliculas":peliculasBusqueda})

class PeliculaDetail(DetailView):

    model = Peliculas
    template_name = "peliculas_detail.html"

#Todo Tienda
@login_required
def tienda(request):
    
    if request.method == "POST":
        
        search = request.POST["search"]
        
        if search != "":
            productos = Tienda.objects.filter(Q(productos__icontains=search))#.values()
            
            return render(request,"tienda.html",{"tienda":productos, "search":True, "busqueda":search})
    
    cards=Tienda.objects.all()
    
    ctx={"tienda":cards}

    
    return render(request,"tienda.html",ctx)
@login_required
def formulario_productos(request):
    
    if request.method == "POST":
        
        formulario=tiendaFormulario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            guardar= Tienda(productos=info["productos"],precio=info["precio"])
            guardar.save()
            return redirect("tienda")
        else:
            return redirect("formulario_productos")
        
    else:
        formulario = tiendaFormulario()
        return render(request,"formulario_productos.html",{"form":formulario})
@login_required
def eliminar_producto(request, pk):
    
    tienda= get_object_or_404(Tienda, id=pk)
    tienda.delete()
    
    return redirect('tienda')
@login_required
def editar_producto (request,pk):
    
    producto = Tienda.objects.get(id=pk)

    if request.method == "POST":

        formulario = tiendaFormulario(request.POST)

        if formulario.is_valid():
            
            info_producto = formulario.cleaned_data
            
            producto.productos = info_producto["productos"]
            producto.precio = info_producto["precio"]
            producto.save()

            return redirect("tienda")

    # get
    formulario = tiendaFormulario(initial={"productos":producto.productos, "precio": producto.precio})
    
    return render(request,"editar_producto.html",{"form":formulario})
@login_required
def busqueda_producto(request):
    if request.method == "POST":
        
        productos=request.POST["producto"]
        
        productosBusqueda =Tienda.objects.filter(nombrePelicula__icontains=productos)
        
        return render(request,"busqueda_pelicula.html",{"producto":productosBusqueda})
    
    else:
        
        productosBusqueda=[]
    
        return render(request,"busqueda_producto.html",{"producto":productosBusqueda})

class TiendaDetail(DetailView):

    model = Tienda
    template_name = "productos_detail.html"

#Login, registro y Avatar

def register_user(request):
    if request.method == "POST":
        
        # form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1') # es la primer contraseña, no la confirmacion

            form.save() # registramos el usuario
            # iniciamos la sesion
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")

        return render(request,"register.html",{"form":form})

    # form = UserCreationForm()
    form = UserRegisterForm()

    return render(request,"register.html",{"form":form})

@login_required
def edit_user (request):
    
    user = request.user # usuario con el que estamos loggueados
    
    try:
        avatar= Avatar.objects.get(usuario=user)
    except:
        avatar = Avatar(usuario=user)
        avatar.save()

    if request.method == "POST":
        
        form = UserEditForm(request.POST,request.FILES) # cargamos datos llenados

        if form.is_valid():

            info = form.cleaned_data
            user.username = info["username"]
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            avatar.imagen = info["imagen"]

            user.save()
            avatar.save()

            return redirect("inicio")
        else:
            return render(request,"editar_perfil",{"form":form})
    else:
        form = UserEditForm(initial={"username":user.username,"email":user.email, "first_name":user.first_name, "last_name":user.last_name,"imagen":avatar.imagen})
    return render(request,"editar_usuario.html",{"form":form})

def login_user (request):
    if request.method == "POST":

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
        else:
            return redirect("login")
    
    form = AuthenticationForm()

    return render(request,"login.html",{"form":form})

@login_required
def logout_request(request):
    
    logout(request)
    return redirect("inicio")

@login_required
def agregar_avatar(request):
    
    if request.method == "POST":
            
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():

            user = User.objects.get(username=request.user.username) # usuario con el que estamos loggueados

            avatar = Avatar(usuario=user, imagen=form.cleaned_data["imagen"])

            avatar.save()

            # avatar = Avatar()
            # avatar.usuario = request.user
            # avatar.imagen = form.cleaned_data["imagen"]
            # avatar.save()

            return redirect("inicio")

    else:
        form = AvatarForm()
    
    return render(request,"agregar_avatar.html",{"form":form})

#CONTACTO
@login_required
def contacto(request):

    contacto=Contacto.objects.all()
    
    return render(request,"contacto.html",{"nombre":contacto})
@login_required
def formulario_contacto(request):
    
    if request.method == "POST":
        
        formulario=contactoFormulario(request.POST)
        
        if formulario.is_valid():
            
            info = formulario.cleaned_data
            guardar= Contacto(nombreCompleto=info["nombreCompleto"],dni=info["dni"],profesion=info["profesion"],cv=info["cv"])
            guardar.save()
            return redirect("contacto")
        else:
            return redirect("formulario_contacto")
        
    else:
        formulario = contactoFormulario()
        return render(request,"formulario_contacto.html",{"form":formulario})

#CONTACTO
@login_required
def nosotros(request):
    
    base_context.update({"active":"nosotros"})

    return render(request,"nosotros.html")

#Mensajes
@login_required
def enviar_mensaje(request):
    if request.method == "POST":
        form = CreateMensajeFrom(request.POST)
        if form.is_valid():
            info  = form.cleaned_data
            nuevo_mensaje = Mensaje(remitente=request.user,destinatario=User.objects.get(email=info["destinatario"]), mensaje = info["mensaje"])
            nuevo_mensaje.save()
            # form.save()
            messages.success(request, "Mensaje enviado!")
            return redirect("inicio")
        else:
            messages.error(request, "Error al enviar el mensaje!")
            return redirect("mensajes")
    else:
        form = CreateMensajeFrom()
        base_context.update({"form":form})
        return render(request,"mensajes.html", base_context)

def ver_mensajes(request):
    user = request.user

    mensajes = Mensaje.objects.filter(destinatario=user)

    base_context.update({"active":""})
    base_context.update({"mensajes":mensajes})
    return render(request, 'index.html', base_context)