import blog_consola.blog.datos as datos

import blog_consola.blog.formateador as formateador

from blog.datos import posts
from blog.formateador import listar_posts
from blog.validaciones import validar_post

print(datos.perfil_autor("nombre"))
formateador.listar_post(datos.posts)
listar_posts(datos.posts)
