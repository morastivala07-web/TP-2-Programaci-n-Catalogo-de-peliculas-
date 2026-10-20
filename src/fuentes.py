import csv
import json
from abc import ABC, abstractmethod


class FuenteDatos(ABC):
    @abstractmethod
    def cargar(self, ruta):
        pass


class FuenteCSV(FuenteDatos):
    def cargar(self, ruta):
        with open(ruta, encoding="utf-8-sig", newline="") as archivo:
            lector = csv.DictReader(archivo)
            return list(lector)


class FuenteJSON(FuenteDatos):
    def cargar(self, ruta):
        with open(ruta, encoding="utf-8-sig") as archivo:
            datos = json.load(archivo)

        if not isinstance(datos, list):
            raise ValueError("El archivo JSON debe contener una lista.")

        if not all(isinstance(fila, dict) for fila in datos):
            raise ValueError("Cada elemento del JSON debe ser un objeto.")

        return datos