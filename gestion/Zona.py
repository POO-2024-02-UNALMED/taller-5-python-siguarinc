from zooAnimales.animal import Animal

class Zona:
    def __init__(self, nombre=None, zoo=None):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = []

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getZoo(self):
        return self.zoo

    def setZoo(self, zoo):
        self.zoo = zoo

    def getAnimales(self):
        return self.animales

    def setAnimales(self, ani):
        self.animales = ani

    def agregarAnimales(self, ani):
        self.animales.append(ani)

    def cantidadAnimales(self):
        return len(self.animales)
