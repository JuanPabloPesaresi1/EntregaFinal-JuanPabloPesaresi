from django import views
from django.urls import path

from .views import *

urlpatterns = [
    #URLS
    path('inicio/',index, name="inicio"),
    
    #TodoLogin
    path('account/login/',login_user,name="login"),
    path('account/signup/',register_user,name="register"),
    path('account/logout/', logout_request, name="logout"),
    path('account/edit/', edit_user, name="editar_perfil"),
    path('agregar_avatar/', agregar_avatar, name="agregar_avatar"),
    
    #TodoPeliculas
    path('catalogo/peliculas/',peliculas, name="peliculas"),
    path('formulario_peliculas/',formulario_peliculas, name="formulario_peliculas"),
    path('eliminar_pelicula/<int:pk>/',eliminar_peliculas, name="eliminar_peliculas"),
    path('modificar_peliculas/<int:pk>/',modificar_peliculas, name="modificar_peliculas"),
    path('peliculas_detail/<int:pk>/', PeliculaDetail.as_view(), name="peliculas_detail"),
    
    #TodoProductos
    path('tienda/productos/',tienda, name="tienda"),
    path('formulario_productos/',formulario_productos, name="formulario_productos"),
    path('eliminar_producto/<int:pk>/',eliminar_producto, name="eliminar_producto"),
    path('editar_producto/<int:pk>/', editar_producto, name="editar_producto"),
    path('producto_detail/<int:pk>/', TiendaDetail.as_view(), name="productos_detail"),
    
    #TodoContacto
    path('contacto/',contacto, name="contacto"),
    path('formulario_contacto/',formulario_contacto, name="formulario_contacto"),
    
    #Nosotros
    path('about/',nosotros,name="nosotros"),
    
    path('mensajes/',enviar_mensaje,name="mensajes"),
    path('ver_mensajes/',ver_mensajes,name="ver_mensajes"),
        
    path('base/',base,name="base"),
    
]
