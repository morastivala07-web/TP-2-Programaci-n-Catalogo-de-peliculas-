def buscar_titulos(peliculas, texto):
    texto = texto.strip().casefold()

    if not texto:
        raise ValueError("Escribí al menos un carácter para buscar.")

    return [
        pelicula
        for pelicula in peliculas
        if texto in pelicula["titulo"].casefold()
    ]
def filtrar_genero(peliculas, genero):
    genero = genero.strip().casefold()

    if not genero:
        raise ValueError("Escribí un género para filtrar.")

    return [
        pelicula
        for pelicula in peliculas
        if genero in [
            valor.strip().casefold()
            for valor in pelicula["generos"].split("|")
        ]
    ]