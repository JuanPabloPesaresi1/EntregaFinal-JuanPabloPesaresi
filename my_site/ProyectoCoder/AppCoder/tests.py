from django.test import TestCase

from AppCoder.models import Peliculas

# Create your tests here.

class PeliculasTest(TestCase):
    
    def setUp(self):
        Peliculas.objects.create(nombrePelicula="Peliculas de Django", genero="Accion", anioDeLanzamiento ="2002")
        
    def test_Peliculas_nombre(self):
        peliculas = Peliculas.objects.get(genero="Accion")
        self.assertEqual(peliculas.nombrePelicula, "Peliculas de Django")
    
    def test_Peliculas_creado(self):
        peliculas = Peliculas.objects.get(genero="Accion")
        self.assertNotEquals(peliculas, None)