from pathlib import Path
from fuentes import FuenteCSV
from pipeline import construir_catalogo, acumular_valoraciones


def main():
    carpeta_data = Path(__file__).resolve().parent.parent / "data"
    fuente = FuenteCSV()

    peliculas = fuente.cargar(carpeta_data / "peliculas.csv")
    valoraciones = fuente.cargar(carpeta_data / "valoraciones.csv")

    catalogo = construir_catalogo(peliculas)
    rechazos = acumular_valoraciones(catalogo, valoraciones)

    assert len(catalogo) == 5
    assert len(rechazos) == 0

    toy_story = catalogo["1"]
    assert toy_story.cantidad_valoraciones() == 2
    assert toy_story.promedio() == 4.5
    print("Correcto: Toy Story tiene 2 opiniones y promedio 4.5.")

    total = sum(
        pelicula.cantidad_valoraciones()
        for pelicula in catalogo.values()
    )
    assert total == 10
    print("Correcto: se contabilizaron las 10 valoraciones.")

    catalogo_prueba = construir_catalogo(peliculas)

    entradas_prueba = [
        {"id_valoracion": "1", "id_pelicula": "1", "puntuacion": "4"},
        {"id_valoracion": "1", "id_pelicula": "1", "puntuacion": "4"},
        {"id_valoracion": "2", "id_pelicula": "999", "puntuacion": "5"},
        {"id_valoracion": "3", "id_pelicula": "1", "puntuacion": "6"}
    ]

    rechazos_prueba = acumular_valoraciones(
        catalogo_prueba, entradas_prueba
    )

    assert len(rechazos_prueba) == 3
    assert catalogo_prueba["1"].cantidad_valoraciones() == 1
    assert catalogo_prueba["1"].promedio() == 4

    print("Correcto: se rechazaron una repetición,")
    print("una película inexistente y una puntuación inválida.")

    for rechazo in rechazos_prueba:
        print("Fila", rechazo["fila"], "-", rechazo["motivo"])


if __name__ == "__main__":
    main()