from pathlib import Path
from fuentes import FuenteCSV
from pipeline import (
    buscar_titulos,
    filtrar_genero,
    construir_catalogo,
    acumular_valoraciones,
    generar_lista
)


def mostrar_resultados(resultados):
    if not resultados:
        print("No se encontraron películas.")
        return

    for pelicula in resultados:
        print(
            pelicula["id"],
            "-",
            pelicula["titulo"],
            "|",
            pelicula["generos"]
        )


def main():
    carpeta_data = Path(__file__).resolve().parent.parent / "data"
    fuente = FuenteCSV()

    try:
        peliculas = fuente.cargar(carpeta_data / "peliculas.csv")
        valoraciones = fuente.cargar(carpeta_data / "valoraciones.csv")
        catalogo = construir_catalogo(peliculas)
        rechazos = acumular_valoraciones(catalogo, valoraciones)
    except (OSError, UnicodeError, ValueError, KeyError) as error:
        print("No se pudieron preparar los datos:", error)
        return

    if rechazos:
        print("Valoraciones rechazadas:", len(rechazos))
        for rechazo in rechazos:
            print("Fila", rechazo["fila"], "-", rechazo["motivo"])

    while True:
        print("\nCatálogo de películas")
        print("1. Buscar por título")
        print("2. Filtrar por género")
        print("3. Ver películas mejor valoradas")
        print("4. Salir")

        opcion = input("Elegí una opción: ").strip()

        if opcion == "1":
            texto = input("Escribí parte del título: ")

            try:
                resultados = buscar_titulos(peliculas, texto)
            except ValueError as error:
                print(error)
                continue

            mostrar_resultados(resultados)

        elif opcion == "2":
            genero = input("Escribí un género: ")

            try:
                resultados = filtrar_genero(peliculas, genero)
            except ValueError as error:
                print(error)
                continue

            mostrar_resultados(resultados)

        elif opcion == "3":
            entrada = input("Cantidad mínima de opiniones: ").strip()

            try:
                minimo = int(entrada)
                resultados = generar_lista(catalogo, minimo)
            except ValueError:
                print("Ingresá un número entero mayor que cero.")
                continue

            if not resultados:
                print("No hay películas con ese mínimo de opiniones.")
            else:
                for pelicula in resultados:
                    print(
                        pelicula.titulo,
                        "| Promedio:",
                        format(pelicula.promedio(), ".2f"),
                        "| Opiniones:",
                        pelicula.cantidad_valoraciones()
                    )

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Ingresá un número del 1 al 4.")


if __name__ == "__main__":
    main()
    