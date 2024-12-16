from gestion.zona import Zona

class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal.total_animales += 1

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = zona

    @staticmethod
    def getTotalAnimales():
        return Animal.total_animales

    @staticmethod
    def setTotalAnimales(total):
        Animal.total_animales = total

    @staticmethod
    def totalPorTipo():
        from zooAnimales.anfibio import Anfibio
        from zooAnimales.ave import Ave
        from zooAnimales.mamifero import Mamifero
        from zooAnimales.pez import Pez
        from zooAnimales.reptil import Reptil
        return (f"Mamiferos: {Mamifero.cantidadMamiferos()}\n"
                f"Aves: {Ave.cantidadAves()}\n"
                f"Reptiles: {Reptil.cantidadReptiles()}\n"
                f"Peces: {Pez.cantidadPeces()}\n"
                f"Anfibios: {Anfibio.cantidadAnfibios()}")

    def __str__(self):
        if self._zona is None:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                    f"habito en {self.habitat} y mi género es {self.genero}")
        else:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                    f"habito en {self.habitat} y mi género es {self.genero}, "
                    f"la zona en la que me ubico es {self.zona}, en el {self.zona.getZoo()}")

    def movimiento(self):
        return "desplazarse"
    
