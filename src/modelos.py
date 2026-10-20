import math
import re


class Pelicula:
    def __init__(self, identificador, titulo, generos):
        self.identificador = identificador
        self.titulo = titulo
        self.generos = generos
        self.puntuaciones = []

    def agregar_puntuacion(self, puntuacion):
        numero = float(puntuacion)

        if not math.isfinite(numero):
            raise ValueError("La puntuación debe ser un número finito.")

        if not 0.5 <= numero <= 5:
            raise ValueError("La puntuación debe estar entre 0.5 y 5.")

        if not (numero * 2).is_integer():
            raise ValueError("La puntuación debe avanzar de a 0.5.")

        self.puntuaciones.append(numero)

    def cantidad_valoraciones(self):
        return len(self.puntuaciones)

    def promedio(self):
        if not self.puntuaciones:
            return None

        return sum(self.puntuaciones) / len(self.puntuaciones)

    def obtener_anio(self):
        coincidencia = re.search(r"\(([0-9]{4})\)$", self.titulo.strip())

        if coincidencia:
            return int(coincidencia.group(1))

        return None