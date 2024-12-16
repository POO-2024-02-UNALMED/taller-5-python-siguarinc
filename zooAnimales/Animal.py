from gestion.zona import Zona
from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
class Animal:
    total_animales = 0

    def __init__(self, nombre=None, edad=None, habitat=None, genero=None):
        self.nombre = nombre
        self.edad = edad
        self.habitat = habitat
        self.genero = genero
        self.zona = None
        Animal.total_animales += 1

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getEdad(self):
        return self.edad

    def setEdad(self, edad):
        self.edad = edad

    def getHabitat(self):
        return self.habitat

    def setHabitat(self, habitat):
        self.habitat = habitat

    def getGenero(self):
        return self.genero

    def setGenero(self, genero):
        self.genero = genero

    def getZona(self):
        return self.zona

    def setZona(self, zona):
        self.zona = zona

    @staticmethod
    def getTotalAnimales():
        return Animal.total_animales

    @staticmethod
    def setTotalAnimales(total):
        Animal.total_animales = total

    @staticmethod
    def totalPorTipo():
        # Suponiendo que existen las clases Mamifero, Ave, Reptil, Pez y Anfibio
        return (f"Mamiferos: {Mamifero.cantidadMamiferos()}\n"
                f"Aves: {Ave.cantidadAves()}\n"
                f"Reptiles: {Reptil.cantidadReptiles()}\n"
                f"Peces: {Pez.cantidadPeces()}\n"
                f"Anfibios: {Anfibio.cantidadAnfibios()}")

    def __str__(self):
        if self.zona is None:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                    f"habito en {self.habitat} y mi género es {self.genero}")
        else:
            return (f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, "
                    f"habito en {self.habitat} y mi género es {self.genero}, "
                    f"la zona en la que me ubico es {self.zona}, en el {self.zona.getZoo()}")

    def movimiento(self):
        return "desplazarse"
    