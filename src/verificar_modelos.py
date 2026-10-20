from modelos import Pelicula


def main():
    pelicula = Pelicula("1", "Toy Story (1995)", "Animación|Comedia")

    pelicula.agregar_puntuacion("4")
    pelicula.agregar_puntuacion("5")

    assert pelicula.cantidad_valoraciones() == 2
    assert pelicula.promedio() == 4.5
    assert pelicula.obtener_anio() == 1995
    print("Correcto: cantidad, promedio y año.")

    sin_opiniones = Pelicula("2", "Película sin año", "Drama")

    assert sin_opiniones.promedio() is None
    assert sin_opiniones.obtener_anio() is None
    print("Correcto: película sin opiniones y sin año.")

    for puntuacion in ["6", "3.2", "nan", "texto"]:
        try:
            pelicula.agregar_puntuacion(puntuacion)
        except ValueError:
            print("Correcto: se rechazó la puntuación", puntuacion)
        else:
            raise AssertionError("Se aceptó una puntuación inválida.")

    assert pelicula.cantidad_valoraciones() == 2
    print("Correcto: los rechazos no modificaron las opiniones válidas.")


if __name__ == "__main__":
    main()