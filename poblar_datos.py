import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_blog.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post

# Crear usuario administrador si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')
    print("Usuario 'admin' creado con contraseña: admin1234")
else:
    print("El usuario 'admin' ya existe.")

usuario = User.objects.get(username='admin')

# Publicaciones de ejemplo sobre Michi
posts_muestra = [
    {
        'titulo': 'La fascinación inexplicable por las cajas de cartón',
        'subtitulo': 'Ignorando olímpicamente la cama acolchonada nueva',
        'contenido': (
            'Le compré a Michi una cama acolchonada con tela térmica de última generación. '
            '¿El resultado? La miró con total indiferencia durante tres segundos, dio media vuelta '
            'y se metió de cabeza en la caja de cartón donde venía el envío. '
            'Ahí duerme desde hace semanas, hecho una rosca perfecta y feliz de la vida. '
            'Lección aprendida: nunca subestimes el poder de una simple caja de cartón vacía.'
        )
    },
    {
        'titulo': 'La persecución épica del punto rojo láser',
        'subtitulo': 'Una batalla diaria contra un enemigo intangible',
        'contenido': (
            'Todos los días a las 6 de la tarde comienza la hora de la cacería. '
            'Michi se prepara, agazapa las patas traseras y menea la cola con máxima concentración '
            'antes de dar un salto acrobático hacia la pared persiguiendo la misteriosa luz roja. '
            'Aunque nunca logra atraparlo físicamente, su espíritu cazador sigue intacto día tras día.'
        )
    },
    {
        'titulo': 'El concierto de maullidos a las 5:00 AM',
        'subtitulo': 'Porque se ve el fondo del plato de comida',
        'contenido': (
            'Michi no necesita alarma para despertarse. Llega puntualmente a las 5:00 AM, '
            'se sube a la almohada y me toca la nariz con su patita fría mientras emite un concierto '
            'de maullidos dramáticos. Al ir a revisar la cocina, descubro la tragedia: el plato '
            'todavía tiene comida, pero se puede ver un milímetro del fondo en el centro. '
            'Un par de caricias, acomodar las croquetas y la paz vuelve al hogar.'
        )
    }
]

for p in posts_muestra:
    if not Post.objects.filter(titulo=p['titulo']).exists():
        Post.objects.create(
            titulo=p['titulo'],
            subtitulo=p['subtitulo'],
            contenido=p['contenido'],
            autor=usuario
        )
        print(f"Publicación creada: {p['titulo']}")

print("Datos iniciales de prueba cargados correctamente.")
