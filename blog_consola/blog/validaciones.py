def validar_post(post : {__getitem__} ):
    errores = []
    if post["titulo"] == "":
        errores.append("El titulo no puede estar vacío.")
    if post["contenido"] == "":
        errores.append("El contenido no puede estar vacío.")
    if len(post["tags"]) == 0:
        erorres.append("El post debe tener al menos una etiqueta.")
    if post["estado"] not in ("borrador", "publicado", "archivado"):
        errores.append("El estado del post no es válido.")
    return errores