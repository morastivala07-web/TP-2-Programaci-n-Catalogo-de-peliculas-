from pathlib import Path
from fuentes import FuenteCSV
from pipeline import buscar_titulos, filtrar_genero


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

    try:
        peliculas = FuenteCSV().cargar(carpeta_data / "peliculas.csv")
    except (OSError, UnicodeError, ValueError) as error:
        print("No se pudo cargar el catálogo:", error)
        return

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
            print("La lista de valoraciones estará disponible próximamente.")

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Ingresá un número del 1 al 4.")


if __name__ == "__main__":
    main()