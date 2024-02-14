from django.test import TestCase #Cuando no hay bd se usa simple
from django.urls import reverse # 
from .models import Publicacion

# Create your tests here.
class PruebasPublicaciones (TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pub = Publicacion.objects.create(texto='Esto es una prueba!')
        return super().setUpTestData()
    
    def test_contenido_modelo(self):
        self.assertEqual(self.pub.texto, 'Esto es una prueba!')

    def test_url_existe_en_ubicacion_correcta(self):
        respuesta = self.client.get('/')
        self.assertEqual(respuesta.status_code,200) #codigo 200 todo ok

    #def test_url_disponible_por_nombre(self):
    #    respuesta = self.client.get(reverse('inicio'))
    #    self.assertEqual(respuesta.status_code,200)
    #
    #def test_nombre_plantilla_correcto(self):
    #    respuesta = self.client.get(reverse('inicio'))
    #    self.assertTemplateUsed(respuesta, 'inicio.html')
    #
    #def test_contenido_plantilla(self):
    #    respuesta = self.client.get(reverse('inicio'))
    #    self.assertContains(respuesta, 'Esto es una prueba!')
    def test_paginainicio(self):
        respuesta = self.client.get(reverse('inicio'))
        self.assertEqual(respuesta.status_code,200)
        self.assertTemplateUsed(respuesta, 'inicio.html')
        self.assertContains(respuesta, 'Esto es una prueba!')

