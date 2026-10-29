from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class CuentasTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = User.objects.create_user(
            username='gatito',
            email='gatito@test.com',
            password='Password123!'
        )

    def test_login_exitoso(self):
        """Verifica el login con credenciales correctas"""
        response = self.client.post(reverse('cuentas:login'), {
            'username': 'gatito',
            'password': 'Password123!'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('blog:inicio'))

    def test_perfil_requiere_login(self):
        """Verifica que el perfil no sea accesible para anónimos"""
        response = self.client.get(reverse('cuentas:perfil'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('cuentas:login')))

    def test_perfil_usuario_autenticado(self):
        """Verifica que un usuario autenticado pueda acceder a su perfil"""
        self.client.login(username='gatito', password='Password123!')
        response = self.client.get(reverse('cuentas:perfil'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'gatito')

    def test_logout(self):
        """Verifica que el logout cierre sesión y redirija"""
        self.client.login(username='gatito', password='Password123!')
        response = self.client.get(reverse('cuentas:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('blog:inicio'))
