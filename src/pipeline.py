from modelos import Pelicula
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
def construir_catalogo(peliculas):
    catalogo = {}

    for fila in peliculas:
        identificador = fila["id"].strip()
        titulo = fila["titulo"].strip()
        generos = fila["generos"].strip()

        if not identificador or not titulo or not generos:
            raise ValueError("Hay una película con campos obligatorios vacíos.")

        if identificador in catalogo:
            raise ValueError("Identificador de película repetido: " + identificador)

        catalogo[identificador] = Pelicula(
            identificador, titulo, generos
        )

    return catalogo


def acumular_valoraciones(catalogo, valoraciones):
    rechazos = []
    identificadores_vistos = set()

    for numero_fila, fila in enumerate(valoraciones, start=2):
        try:
            id_valoracion = fila["id_valoracion"].strip()
            id_pelicula = fila["id_pelicula"].strip()

            if not id_valoracion:
                raise ValueError("Falta el identificador de valoración.")

            if id_valoracion in identificadores_vistos:
                raise ValueError("Identificador de valoración repetido.")

            if id_pelicula not in catalogo:
                raise ValueError("La película indicada no existe.")

            catalogo[id_pelicula].agregar_puntuacion(fila["puntuacion"])
            identificadores_vistos.add(id_valoracion)

        except (KeyError, ValueError) as error:
            rechazos.append({
                "fila": numero_fila,
                "motivo": str(error),
                "registro": dict(fila)
            })

    return rechazos
def generar_lista(catalogo, minimo_valoraciones):
    if (
        isinstance(minimo_valoraciones, bool)
        or not isinstance(minimo_valoraciones, int)
        or minimo_valoraciones < 1
    ):
        raise ValueError("El mínimo debe ser un número entero mayor que cero.")

    seleccionadas = [
        pelicula
        for pelicula in catalogo.values()
        if pelicula.cantidad_valoraciones() >= minimo_valoraciones
    ]

    return sorted(
        seleccionadas,
        key=lambda pelicula: (
            -pelicula.promedio(),
            -pelicula.cantidad_valoraciones(),
            pelicula.titulo.casefold(),
            pelicula.identificador
        )
    )