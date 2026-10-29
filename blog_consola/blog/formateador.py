def formatear_post(post:{__getitem__}):
    tags = ", ".join(post["tags"])
    return f"Titulo: {post['titulo']}"
##Autor: {post['autor']['nombre']}
##Etiquetas: {'tags'}"

def listar_posts(lista_posts:{__iter__}):
    for post in lista_posts:
        print(formatear_post(post))