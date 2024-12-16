class Zoologico:
    def __init__(self, nombre=None, ubicacion=None, zonas=None):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = zonas if zonas is not None else []

    def cantidadTotalAnimales(self):
        cantidad = 0
        for r in self._zonas:
            cantidad += r.cantidadAnimales()
        return cantidad

    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    def getZona(self):
        return self._zonas

    def setZona(self, zonas):
        self._zonas = zonas
