from pathlib import Path
from fuentes import FuenteCSV, FuenteJSON


def verificar_archivos(carpeta_data, nombre):
    datos_csv = FuenteCSV().cargar(carpeta_data / (nombre + ".csv"))
    datos_json = FuenteJSON().cargar(carpeta_data / (nombre + ".json"))

    print(nombre, "- registros CSV:", len(datos_csv))
    print(nombre, "- registros JSON:", len(datos_json))

    if not datos_csv:
        raise ValueError("El archivo de " + nombre + " está vacío.")

    if datos_csv != datos_json:
        raise ValueError("Los formatos de " + nombre + " no coinciden.")

    print("Correcto: ambos formatos contienen los mismos datos.")


def main():
    carpeta_data = Path(__file__).resolve().parent.parent / "data"

    verificar_archivos(carpeta_data, "peliculas")
    verificar_archivos(carpeta_data, "valoraciones")


if __name__ == "__main__":
    main()