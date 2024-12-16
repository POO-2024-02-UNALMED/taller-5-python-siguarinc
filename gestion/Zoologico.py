from gestion import Zona

class Zoologico:
    def __init__(self, nombre=None, ubicacion=None, zonas=None):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = zonas if zonas is not None else []

    def cantidadTotalAnimales(self):
        cantidad = 0
        for r in self.zonas:
            cantidad += r.cantidadAnimales()
        return cantidad

    def agregarZonas(self, zona):
        self.zonas.append(zona)

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getUbicacion(self):
        return self.ubicacion

    def setUbicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def getZona(self):
        return self.zonas

    def setZona(self, zonas):
        self.zonas = zonas
