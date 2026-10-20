from pathlib import Path
from fuentes import FuenteCSV, FuenteJSON


def main():
    carpeta_data = Path(__file__).resolve().parent.parent / "data"

    peliculas_csv = FuenteCSV().cargar(carpeta_data / "peliculas.csv")
    peliculas_json = FuenteJSON().cargar(carpeta_data / "peliculas.json")

    print("Películas leídas del CSV:", len(peliculas_csv))
    print("Películas leídas del JSON:", len(peliculas_json))

    if not peliculas_csv:
        raise ValueError("El catálogo está vacío.")

    if peliculas_csv != peliculas_json:
        raise ValueError("Los archivos CSV y JSON contienen datos diferentes.")

    print("Correcto: ambos formatos contienen los mismos datos.")
    print("Primera película:", peliculas_csv[0]["titulo"])


if __name__ == "__main__":
    main()