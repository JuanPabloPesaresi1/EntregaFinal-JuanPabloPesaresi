from django.contrib import admin

from .models import *

# Register your models here.
class ContactoAdmin(admin.ModelAdmin):
        
        list_display = ("nombreCompleto","dni","profesion","cv")
        search_fields = ('nombreCompleto',"dni","profesion","cv")
        
admin.site.register(Contacto,ContactoAdmin)

class PeliculasAdmin(admin.ModelAdmin):

        list_display = ("nombrePelicula","genero","anioDeLanzamiento","descripcion")
        search_fields = ('nombre',"genero","anioDeLanzamiento","descripcion")
        
admin.site.register(Peliculas,PeliculasAdmin)

class TiendaAdmin(admin.ModelAdmin):

        list_display = ("productos","precio",)
        search_fields = ('productos',)
        
admin.site.register(Tienda,TiendaAdmin)

admin.site.register(Mensaje)
# admin, admin -> python manage.py createsuperuser

admin.site.register(Avatar)