from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post

class BlogTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.usuario = User.objects.create_user(
            username='felixfan',
            email='felix@test.com',
            password='Password123!'
        )
        self.post = Post.objects.create(
            titulo='Aventura con una pluma',
            subtitulo='El juguete favorito',
            contenido='Felix saltó más de un metro persiguiendo una pluma.',
            autor=self.usuario
        )

    def test_inicio_muestra_publicaciones(self):
        """Verifica que la página de inicio liste los posts"""
        response = self.client.get(reverse('blog:inicio'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aventura con una pluma')

    def test_detalle_post(self):
        """Verifica que la página de detalle muestre el contenido del post"""
        response = self.client.get(reverse('blog:detalle_post', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Felix saltó más de un metro')

    def test_crear_post_requiere_login(self):
        """Verifica que un usuario anónimo sea redirigido al intentar crear un post"""
        response = self.client.get(reverse('blog:crear_post'))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('cuentas:login')))

    def test_editar_post_requiere_login(self):
        """Verifica que un usuario anónimo sea redirigido al intentar editar un post"""
        response = self.client.get(reverse('blog:editar_post', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('cuentas:login')))

    def test_eliminar_post_requiere_login(self):
        """Verifica que un usuario anónimo sea redirigido al intentar eliminar un post"""
        response = self.client.get(reverse('blog:eliminar_post', kwargs={'pk': self.post.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith(reverse('cuentas:login')))

    def test_usuario_autenticado_puede_crear_post(self):
        """Verifica que un usuario autenticado pueda crear un post correctamente"""
        self.client.login(username='felixfan', password='Password123!')
        response = self.client.post(reverse('blog:crear_post'), {
            'titulo': 'Nuevo post de prueba',
            'subtitulo': 'Subtítulo de prueba',
            'contenido': 'Contenido de prueba sobre Felix durmiendo.',
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(titulo='Nuevo post de prueba').exists())

    def test_busqueda_existente(self):
        """Verifica que la búsqueda por título encuentre el post"""
        response = self.client.get(reverse('blog:inicio') + '?buscar=pluma')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Aventura con una pluma')

    def test_busqueda_sin_coincidencias(self):
        """Verifica que la búsqueda informe cuando no hay resultados"""
        response = self.client.get(reverse('blog:inicio') + '?buscar=palabrainventadaquenoexiste')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No se encontraron publicaciones con')

    def test_acerca_de(self):
        """Verifica que la página Acerca de cargue correctamente"""
        response = self.client.get(reverse('blog:acerca_de'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Conoce a Felix')
