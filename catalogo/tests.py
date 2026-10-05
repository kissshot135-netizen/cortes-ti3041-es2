from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Compra, Producto


class CatalogoTests(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre='Martillo',
            categoria='Herramientas',
            precio=12000,
            stock=5,
        )
        self.consumidor = User.objects.create_user(
            username='consumidor',
            password='Password12345!',
        )
        self.administrador = User.objects.create_user(
            username='administrador',
            password='Password12345!',
            is_staff=True,
        )

    def test_inicio_y_catalogo_cargan(self):
        self.assertEqual(self.client.get(reverse('inicio')).status_code, 200)
        respuesta = self.client.get(reverse('lista_productos'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Martillo')

    def test_superusuario_puede_gestionar_productos_en_admin(self):
        superusuario = User.objects.create_superuser(
            username='superusuario',
            email='superusuario@example.com',
            password='Password12345!',
        )
        self.client.force_login(superusuario)

        self.assertEqual(self.client.get('/admin/').status_code, 200)
        respuesta = self.client.get('/admin/catalogo/producto/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Martillo')

    def test_ingreso_redirige_segun_rol(self):
        self.assertEqual(self.client.get(reverse('ingreso')).status_code, 200)
        respuesta = self.client.post(
            reverse('ingreso'),
            {'username': 'consumidor', 'password': 'Password12345!'},
        )
        self.assertRedirects(respuesta, reverse('inicio'))

        self.client.logout()
        respuesta = self.client.post(
            reverse('ingreso'),
            {'username': 'administrador', 'password': 'Password12345!'},
        )
        self.assertRedirects(respuesta, reverse('gestionar_productos'))

    def test_registro_crea_cuenta_de_consumidor(self):
        self.assertEqual(self.client.get(reverse('registro')).status_code, 200)
        respuesta = self.client.post(
            reverse('registro'),
            {
                'username': 'nuevo',
                'email': 'nuevo@example.com',
                'password1': 'CompraSegura123!',
                'password2': 'CompraSegura123!',
            },
        )

        self.assertRedirects(respuesta, reverse('inicio'))
        usuario = User.objects.get(username='nuevo')
        self.assertFalse(usuario.is_staff)

    def test_consumidor_compra_y_se_actualiza_stock(self):
        self.client.force_login(self.consumidor)

        respuesta = self.client.post(
            reverse('comprar_producto', args=[self.producto.pk]),
            {'cantidad': 2},
        )

        self.assertRedirects(respuesta, reverse('lista_productos'))
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.stock, 3)
        compra = Compra.objects.get()
        self.assertEqual(compra.consumidor, self.consumidor)
        self.assertEqual(compra.cantidad, 2)

    def test_compra_rechaza_cantidad_superior_al_stock(self):
        self.client.force_login(self.consumidor)

        self.client.post(
            reverse('comprar_producto', args=[self.producto.pk]),
            {'cantidad': 6},
        )

        self.producto.refresh_from_db()
        self.assertEqual(self.producto.stock, 5)
        self.assertFalse(Compra.objects.exists())

    def test_solo_administrador_puede_agregar_y_eliminar_productos(self):
        url = reverse('gestionar_productos')
        self.client.force_login(self.consumidor)
        self.assertEqual(self.client.get(url).status_code, 302)
        self.assertEqual(self.client.post(url, {}).status_code, 302)
        self.assertEqual(Producto.objects.count(), 1)

        self.client.force_login(self.administrador)
        self.assertEqual(self.client.get(url).status_code, 200)
        respuesta = self.client.post(
            url,
            {
                'nombre': 'Taladro',
                'categoria': 'Herramientas eléctricas',
                'precio': 45000,
                'stock': 4,
            },
        )
        self.assertRedirects(respuesta, url)
        taladro = Producto.objects.get(nombre='Taladro')

        respuesta = self.client.post(
            reverse('eliminar_producto', args=[taladro.pk]),
        )
        self.assertRedirects(respuesta, url)
        self.assertFalse(Producto.objects.filter(pk=taladro.pk).exists())
