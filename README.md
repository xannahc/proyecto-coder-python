# El Blog de Felix — Las Aventuras de mi Gato

Proyecto final para el curso de **Python** de **Coderhouse**.

Un blog web interactivo y sencillo dedicado a relatar las anécdotas, siestas y travesuras de mi gato Felix. La aplicación permite a los usuarios leer historias, registrarse, iniciar sesión, crear sus propias publicaciones con fotos y administrar su perfil.

---

## Tecnologías Utilizadas

- **Lenguaje:** [Python 3.14+](https://www.python.org/)
- **Framework Web:** [Django](https://www.djangoproject.com/)
- **Procesamiento de Imágenes:** [Pillow](https://python-pillow.org/)
- **Base de Datos:** SQLite (integrada con Django)
- **Frontend / Estilos:** HTML5, CSS3, [Bootstrap 5](https://getbootstrap.com/) y [Bootstrap Icons](https://icons.getbootstrap.com/)

---

## Funcionalidades Principales

1. **Gestión de Publicaciones (CRUD Web Completo):**
   - **Listar:** Página de inicio con tarjetas de todas las historias publicadas.
   - **Detalle:** Vista completa de cada publicación con autor, fecha, subtítulo e imagen.
   - **Crear:** Formulario web para redactar nuevas historias y adjuntar fotos.
   - **Editar:** Modificación de publicaciones existentes.
   - **Eliminar:** Confirmación antes de borrar una publicación.
   - **Tolerancia a imágenes ausentes:** El diseño se adapta perfectamente tanto si la publicación incluye foto como si no la tiene.

2. **Sistema de Autenticación de Usuarios:**
   - **Registro de usuarios:** Formulario para crear una nueva cuenta.
   - **Inicio de sesión (Login):** Acceso seguro para usuarios registrados.
   - **Cierre de sesión (Logout):** Finalización de la sesión con redirección amigable.
   - **Diferenciación de accesos:** La barra de navegación muestra diferentes opciones según si el visitante es un usuario anónimo o autenticado.

3. **Perfil de Usuario:**
   - Vista de perfil donde el usuario puede consultar su información y fecha de alta.
   - Edición de datos personales (nombre, apellido, correo electrónico).
   - Listado de "Mis Publicaciones" para gestionar rápidamente las historias propias.

4. **Rutas Protegidas:**
   - La creación, edición, eliminación de publicaciones y la edición del perfil requieren iniciar sesión.
   - Implementado en las vistas del servidor mediante `LoginRequiredMixin` y el decorador `@login_required`.

5. **Buscador de Publicaciones:**
   - Búsqueda en tiempo real por coincidencia en el título o contenido.
   - Muestra los resultados encontrados o avisa claramente cuando no hay coincidencias, permitiendo reiniciar la búsqueda.

6. **Página "Sobre Felix":**
   - Sección informativa dedicada a la historia, edad, gustos y hábitos del gato protagonista.

---

## Instrucciones de Instalación y Uso

Sigue estos pasos para clonar, configurar y ejecutar el proyecto localmente:

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd Proyecto_blog
```

### 2. Crear y activar el entorno virtual

- **En Windows:**
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```

- **En macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar las migraciones de la base de datos
Prepara las tablas necesarias ejecutando:
```bash
python manage.py migrate
```
*(Nota: El repositorio excluye intencionalmente `db.sqlite3` y `media/` en `.gitignore` para que cada evaluador cuente con una base limpia. Este comando reconstruye la base de datos desde cero sin problemas).*

### 5. Crear un superusuario (Opcional)
Si deseas ingresar al panel de administración de Django (`/admin`) o administrar publicaciones y usuarios como administrador, crea un superusuario ejecutando:
```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

Abre tu navegador web e ingresa a:
http://127.0.0.1:8000/

---

## Ejecución de Pruebas Automatizadas

El proyecto cuenta con una batería de pruebas unitarias que validan el CRUD, la autenticación, la búsqueda y las rutas protegidas:

```bash
python manage.py test
```

---

## Estructura del Proyecto

```text
Proyecto_blog/
│
├── blog/                      # Aplicación principal del blog
│   ├── migrations/            # Migraciones de base de datos
│   ├── forms.py               # Formularios de publicaciones
│   ├── models.py              # Modelo Post
│   ├── tests.py               # Pruebas unitarias
│   ├── urls.py                # Rutas de la app blog
│   └── views.py               # Vistas basadas en clases (CBV)
│
├── cuentas/                   # Aplicación de usuarios y autenticación
│   ├── forms.py               # Formularios de registro y edición de perfil
│   ├── tests.py               # Pruebas de autenticación
│   ├── urls.py                # Rutas de login, logout, registro y perfil
│   └── views.py               # Vistas de autenticación
│
├── mi_blog/                   # Configuración global del proyecto Django
│   ├── settings.py            # Configuración principal (STATIC, MEDIA, APPS, etc.)
│   ├── urls.py                # Enrutador principal del proyecto
│   └── wsgi.py
│
├── static/                    # Archivos estáticos (CSS, fuentes, diseño)
│   └── css/
│       └── styles.css
│
├── templates/                 # Plantillas HTML con Bootstrap 5
│   ├── base.html              # Plantilla base y barra de navegación
│   ├── blog/                  # Templates de posts y acerca de
│   └── cuentas/               # Templates de autenticación y perfil
│
├── manage.py                  # Gestor de comandos de Django
├── requirements.txt           # Dependencias del proyecto
├── .gitignore                 # Exclusión de archivos innecesarios
└── README.md                  # Documentación del proyecto
```

---

